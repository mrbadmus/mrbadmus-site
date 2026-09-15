"""C1 lesson 06 — Testing the model: does it explain everything?: twelve questions (MRB-269).

These probe the thing an INVESTIGATION lesson is for: whether a student can say
what a model is judged on, read a prediction off it, and tell a failure that
matters from one that can be waved away. The distractors are built from the
lesson's two declared misconceptions — NOS-01 (a model is either true or false,
and one exception proves it wrong) and NOS-02 (models never change once
scientists agree) — together with the two errors the seven observations keep
catching: that particles themselves shrink or squash when a substance is
compressed or dissolved, and that a model is replaced because a newer idea
became more popular rather than because evidence broke it. The timeline
questions also test the over-correction the stretch layer exists to stop —
"superseded" read as "worthless". The lesson carries no figures, so every
question is figure=None.
"""

UNIT = "C1"
LESSON = "testing-the-model"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-06-e01",
        "band": "easier",
        "text": "A sealed helium balloon with no hole in it is noticeably "
                "smaller after three days. What does the particle model say "
                "has happened?",
        "options": [
            {"text": "The helium particles have slowly shrunk, so the balloon "
                     "needs less space.",
             "correct": False,
             "why": "Particles never change size. What changes is where they "
                    "are — here the helium particles have moved out of the "
                    "balloon altogether."},
            {"text": "Helium particles have squeezed through the gaps between "
                     "the rubber's particles.",
             "correct": True},
            {"text": "The helium has cooled down and turned into a liquid in "
                     "the bottom of the balloon.",
             "correct": False,
             "why": "Nothing here was cooled, and helium stays a gas at room "
                    "temperature. The gas has left the balloon, not changed "
                    "state inside it."},
            {"text": "The rubber is a solid, so there must be a hole in it too "
                     "small to see.",
             "correct": False,
             "why": "You are treating a solid as if it were sealed shut. The "
                    "rubber is itself made of particles with gaps between "
                    "them, so no hole is needed."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e02",
        "band": "easier",
        "text": "This lesson gives a rule for judging any scientific model. "
                "What is the rule?",
        "options": [
            {"text": "A model is judged by how many scientists have agreed to "
                     "it.",
             "correct": False,
             "why": "Agreement is not the test. Every model on the timeline "
                    "was once what everyone knew, and evidence overturned it "
                    "anyway."},
            {"text": "A model is judged by whether it is completely true, and "
                     "one exception proves it false.",
             "correct": False,
             "why": "That is the strictest possible standard, and no model in "
                    "science survives it. Applied consistently it would leave "
                    "you with nothing to think with."},
            {"text": "A model is judged by how long it has been in use "
                     "without being changed.",
             "correct": False,
             "why": "Age is not evidence. Democritus's idea lasted two "
                    "thousand years and still never won, because nothing "
                    "could test it."},
            {"text": "A model is judged by what it explains and where it "
                     "fails, not by being completely true.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e03",
        "band": "easier",
        "text": "The timeline gives every model the evidence that broke it. "
                "What broke Dalton's model of solid, unsplittable atoms?",
        "options": [
            {"text": "Thomson found electrons — pieces knocked off an atom "
                     "that was supposed to have no pieces.",
             "correct": True},
            {"text": "Rutherford fired alpha particles at gold foil and a few "
                     "bounced straight back.",
             "correct": False,
             "why": "Real evidence, but it broke the model after Dalton's — "
                    "Thomson's plum pudding. Dalton fell first, to the "
                    "electron."},
            {"text": "The maths showed that orbiting electrons should spiral "
                     "into the nucleus almost at once.",
             "correct": False,
             "why": "That broke Rutherford's model, two steps later. Dalton's "
                    "atom had no nucleus and no orbiting electrons in it at "
                    "all."},
            {"text": "Nothing broke it — a newer idea simply became more "
                     "popular among scientists.",
             "correct": False,
             "why": "Models are not replaced by fashion. Dalton was overturned "
                    "by evidence: electrons, and atoms of one element that "
                    "turned out to have different masses."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e04",
        "band": "easier",
        "text": "Follow the particle model through a substance freezing. What "
                "does it predict, and what does water actually do?",
        "options": [
            {"text": "It predicts the solid will be less dense and float, and "
                     "ice does exactly that.",
             "correct": False,
             "why": "The model predicts the opposite. Particles packed tightly "
                    "in rows should take up less room than the same particles "
                    "jumbled and looser."},
            {"text": "It predicts the solid and the liquid will have the same "
                     "density, and ice is slightly lighter.",
             "correct": False,
             "why": "The model has the spacing changing at every change of "
                    "state, so the density has to change too. It predicts a "
                    "denser solid."},
            {"text": "It predicts the solid will be denser and sink; water is "
                     "the other way round, so ice floats.",
             "correct": True},
            {"text": "It predicts the solid will be denser and sink, and ice "
                     "does sink, only very slowly.",
             "correct": False,
             "why": "Ice floats — it is why a lake freezes from the top and "
                    "the fish survive underneath. The prediction really is "
                    "wrong, and that is the point of the lesson."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-06-s01",
        "band": "standard",
        "text": "A student says the three failures are rare exceptions, so "
                "they can safely be ignored. Which reply deals with that best?",
        "options": [
            {"text": "Nothing in science can ever be ignored, so a model with "
                     "any failure has to be thrown out.",
             "correct": False,
             "why": "Too strong. Scientists do keep using models they know are "
                    "incomplete — the point is not that ignoring is banned, "
                    "but that these particular failures matter."},
            {"text": "Ice floating is why lakes do not freeze solid, and the "
                     "exceptions led to the next model.",
             "correct": True},
            {"text": "Three failures out of seven is far too many for anyone "
                     "to call them rare exceptions.",
             "correct": False,
             "why": "Counting is not the argument. Seven observations were "
                    "chosen for this page; what makes these three matter is "
                    "what they led to, not how many there are."},
            {"text": "The model gets so little right that there is nothing "
                     "worth keeping anyway.",
             "correct": False,
             "why": "It gets a great deal right — melting, pressure, diffusion "
                    "and dissolving, with almost no effort. That is why it is "
                    "still used every day."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s02",
        "band": "standard",
        "text": "Floating ice, diamond against graphite, and a stretchy rubber "
                "band look unrelated. What do the three failures have in "
                "common?",
        "options": [
            {"text": "The particles involved are too small for the model to "
                     "describe properly.",
             "correct": False,
             "why": "Size is not the trouble. The model handles particles far "
                    "too small to see quite happily — what it cannot handle is "
                    "particles that differ from one another."},
            {"text": "They all happen too slowly for the model to predict a "
                     "result for them.",
             "correct": False,
             "why": "Speed is not the trouble either. The model got the timing "
                    "of a smell crossing a still room right, and that is a "
                    "prediction about how long something takes."},
            {"text": "They all involve energy going in or out, which the model "
                     "leaves out of the picture entirely.",
             "correct": False,
             "why": "The model copes with a change of state, where energy goes "
                    "in — it keeps the mass right to the milligram. What it "
                    "leaves out is structure."},
            {"text": "Each one needs particles that differ from each other, or "
                     "are joined in a particular way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s03",
        "band": "standard",
        "text": "A gas can be squashed into a fraction of its volume. The same "
                "substance as a liquid cannot be squashed at all. Why not?",
        "options": [
            {"text": "A gas is mostly empty space between particles; in a "
                     "liquid they are already touching.",
             "correct": True},
            {"text": "Gas particles are squashy and flatten under pressure, "
                     "while liquid particles are hard.",
             "correct": False,
             "why": "Particles themselves never squash. What gets smaller when "
                    "you compress a gas is the space between them, not the "
                    "particles."},
            {"text": "The particles of a gas are smaller than the particles of "
                     "the same substance as a liquid.",
             "correct": False,
             "why": "It is the same substance, so they are the same particles. "
                    "Only the spacing and the movement change."},
            {"text": "A gas weighs far less than a liquid, so there is less of "
                     "it there to compress.",
             "correct": False,
             "why": "Mass is not what you are compressing. Sealed in a "
                    "syringe, the gas keeps all its particles — you are "
                    "closing the gaps between them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s04",
        "band": "standard",
        "text": "A student writes: \"The model fails on the rubber band "
                "because rubber is not really made of particles.\" What is "
                "wrong with that sentence?",
        "options": [
            {"text": "Nothing — the model only covers solids, liquids and "
                     "gases, and rubber is none of them.",
             "correct": False,
             "why": "Rubber is a solid, so the model does claim to cover it. "
                    "The failure is genuine, and it is about structure, not "
                    "about which state rubber is in."},
            {"text": "Rubber is made of particles, and the model explains "
                     "stretching perfectly well.",
             "correct": False,
             "why": "It does not. Loose spheres sliding past each other cannot "
                    "stretch to five times their length and snap back — that "
                    "is exactly what defeats the model."},
            {"text": "Rubber is made of particles; the model cannot join them "
                     "into long tangled chains.",
             "correct": True},
            {"text": "Rubber's particles are much bigger than glass's, and "
                     "that is what the model gets wrong.",
             "correct": False,
             "why": "The model is not beaten by particle size. It is beaten "
                    "because it has no way of joining particles into chains at "
                    "all."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-06-h01",
        "band": "harder",
        "text": "NASA still uses Newton's laws to land spacecraft, even though "
                "Einstein's work superseded them. Which idea from this lesson "
                "does that illustrate?",
        "options": [
            {"text": "A model that has been superseded should no longer be "
                     "trusted for anything at all.",
             "correct": False,
             "why": "Then NASA would have to stop landing spacecraft. "
                    "Replacement is almost never demolition — Newton still "
                    "gives the right answer for the job it is used for."},
            {"text": "Einstein's model cannot be right, since Newton's is the "
                     "one still being used.",
             "correct": False,
             "why": "A new model has to reproduce everything the old one "
                    "already got right, so the two agreeing at ordinary speeds "
                    "is expected — not evidence against Einstein."},
            {"text": "Keep using a model where it works, and record exactly "
                     "where it stops working.",
             "correct": True},
            {"text": "Scientists have not yet decided between the two, so both "
                     "are kept until they do.",
             "correct": False,
             "why": "It is decided. Einstein's is the more complete account; "
                    "Newton's is kept because it is simpler and accurate "
                    "enough for landing a spacecraft."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h02",
        "band": "harder",
        "text": "Here is an eighth observation for the bench. Sugar dissolves "
                "into water and the level in the beaker barely rises. Does the "
                "simple particle model handle it?",
        "options": [
            {"text": "Yes — the sugar particles fit into gaps that were "
                     "already there between the water particles.",
             "correct": True},
            {"text": "No — the model has no way for one substance to disappear "
                     "into another one.",
             "correct": False,
             "why": "Nothing disappears. The sugar particles are still there, "
                    "spread out among the water particles, and the model "
                    "handles that without trouble."},
            {"text": "Yes — the sugar particles shrink, so they take up less "
                     "room once they are in the water.",
             "correct": False,
             "why": "Particles do not change size. The level barely rises "
                    "because the sugar fits into gaps in the liquid, not "
                    "because anything got smaller."},
            {"text": "No — the model says a solid must sink to the bottom and "
                     "stay whole there.",
             "correct": False,
             "why": "The model says no such thing. Dissolving is one of the "
                    "things it gets right with almost no effort, which is why "
                    "it is still used."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h03",
        "band": "harder",
        "text": "Rutherford's model broke when the maths said electrons should "
                "spiral into the nucleus. What did the model that replaced it "
                "have to do?",
        "options": [
            {"text": "Start again from nothing, since Rutherford's model had "
                     "been shown to fail.",
             "correct": False,
             "why": "Replacement is not demolition. A new model has to "
                    "reproduce everything the old one already explained, which "
                    "is why the changes build up instead of cancelling out."},
            {"text": "Show that the dense nucleus does not exist after all, "
                     "since the model holding it failed.",
             "correct": False,
             "why": "The nucleus survived, and it is in every model since. "
                    "What broke was the account of the electrons, not the "
                    "evidence from the gold foil."},
            {"text": "Wait for a better experiment, since a problem that shows "
                     "up only in the maths proves nothing.",
             "correct": False,
             "why": "The maths was the evidence. It predicted that every atom "
                    "in existence should already have collapsed, and plainly "
                    "none of them has."},
            {"text": "Keep everything Rutherford explained, and also explain "
                     "why electrons do not spiral in.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h04",
        "band": "harder",
        "text": "Someone claims that everything is made of a substance no "
                "experiment could ever detect. Using this lesson, what is the "
                "main problem with the claim?",
        "options": [
            {"text": "It is wrong, because we already know everything is made "
                     "of particles.",
             "correct": False,
             "why": "Disagreeing with you is not the problem. Democritus's "
                    "untestable idea turned out to be broadly right, and it "
                    "still could not win."},
            {"text": "No evidence could ever overturn it, so it can never be "
                     "shown to beat its rivals.",
             "correct": True},
            {"text": "There is no problem, so long as most scientists come to "
                     "agree with it.",
             "correct": False,
             "why": "Agreement is not what makes an idea scientific. Being the "
                    "kind of thing evidence could overturn is."},
            {"text": "There is no problem, since Democritus made a claim like "
                     "that and was proved right.",
             "correct": False,
             "why": "He was — eventually, by other people's experiments. His "
                    "own version sat beside the rival view for twenty "
                    "centuries with nothing to choose between them."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-06-e05",
        "band": "easier",
        "text": "This lesson uses the word prediction in a particular way. "
                "What is a prediction?",
        "options": [
            {"text": "What a model says should happen, worked out before "
                     "anyone checks.",
             "correct": True},
            {"text": "An explanation of something that has already been "
                     "carefully measured.",
             "correct": False,
             "why": "That is an explanation, and it is much easier to "
                    "produce. A prediction has to come first, before the "
                    "result is known."},
            {"text": "A guess about something nobody could ever test.",
             "correct": False,
             "why": "An untestable guess is exactly what a prediction is "
                    "not. A prediction has to be checkable."},
            {"text": "A rule that has never once been found to fail.",
             "correct": False,
             "why": "Predictions fail all the time, and a failed one is the "
                    "most useful thing a model can produce."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e06",
        "band": "easier",
        "text": "The lesson talks about the limits of a model. What is a "
                "limit?",
        "options": [
            {"text": "The smallest thing the model is able to describe.",
             "correct": False,
             "why": "Size is not what is meant. A limit is where the model "
                    "starts giving wrong answers, whatever the size."},
            {"text": "The point where the model stops giving the right "
                     "answer.",
             "correct": True},
            {"text": "The number of things a model is allowed to explain.",
             "correct": False,
             "why": "Nothing caps what a model may explain. A limit is found, "
                    "not set."},
            {"text": "A mistake made by the scientist who built the model.",
             "correct": False,
             "why": "A limit is not a blunder. Every model has limits, "
                    "including carefully built ones."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e07",
        "band": "easier",
        "text": "Which of these does the simple particle model handle "
                "completely?",
        "options": [
            {"text": "Ice floating on water.",
             "correct": False,
             "why": "This is one of the three failures. The model predicts "
                    "the solid should sink."},
            {"text": "Diamond and graphite being so different.",
             "correct": False,
             "why": "This is one of the three failures. Identical particles "
                    "should give one substance one set of properties."},
            {"text": "Sealing a melting ice cube in a bag and finding the "
                     "mass unchanged.",
             "correct": True},
            {"text": "A rubber band springing back into its old shape when it "
                     "is let go.",
             "correct": False,
             "why": "This is one of the three failures. It needs particles "
                    "joined into long chains, which this model has no way to "
                    "draw."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e08",
        "band": "easier",
        "text": "According to the timeline, what did Thomson's model say an "
                "atom was?",
        "options": [
            {"text": "A solid sphere that cannot be split, created or "
                     "destroyed.",
             "correct": False,
             "why": "That is Dalton's model, the one Thomson's replaced when "
                    "he found the atom had parts."},
            {"text": "A tiny dense centre with electrons a long way out.",
             "correct": False,
             "why": "That is Rutherford's, which came next — after his "
                    "experiment broke the plum pudding."},
            {"text": "The smallest possible piece of matter, reached by pure "
                     "argument alone.",
             "correct": False,
             "why": "That is Democritus, two thousand years earlier, with no "
                    "experiment behind it."},
            {"text": "A ball of positive charge with tiny negative electrons "
                     "dotted through it.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-06-s05",
        "band": "standard",
        "text": "One of the verdict options is to call the particle model a "
                "theory instead, since a theory is allowed exceptions. Why "
                "does that fix nothing?",
        "options": [
            {"text": "Because a theory that predicts ice will sink has "
                     "exactly the same problem as a model that does.",
             "correct": True},
            {"text": "Because a theory is a much weaker kind of idea than a "
                     "model, so it would be a step backwards.",
             "correct": False,
             "why": "A theory is not weaker than a model. The trouble with "
                    "the swap is that it changes nothing about the "
                    "predictions."},
            {"text": "Because only physicists are allowed to use the word "
                     "theory.",
             "correct": False,
             "why": "Chemistry uses the word freely. The objection is about "
                    "the prediction, not about who may use the word."},
            {"text": "Because the exceptions would then have to be listed "
                     "somewhere.",
             "correct": False,
             "why": "The exceptions are listed either way, and listing them "
                    "is a good thing. Renaming simply does not change what "
                    "the idea predicts."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s06",
        "band": "standard",
        "text": "A student holds that a model is either true or false, and "
                "that one exception proves it false. What would happen to "
                "chemistry if that rule were applied consistently?",
        "options": [
            {"text": "Only the very newest models would survive it.",
             "correct": False,
             "why": "The newest models have limits too — they are simply "
                    "further out. None of them would survive either."},
            {"text": "Chemistry would be left with no models at all, because "
                     "every one of them has limits.",
             "correct": True},
            {"text": "Chemistry would end up far more reliable, because only "
                     "perfect ideas would be kept.",
             "correct": False,
             "why": "There would be no ideas left to be reliable. A standard "
                    "nothing can meet is not a high standard, it is an "
                    "unusable one."},
            {"text": "Nothing would change, because the particle model has no "
                     "exceptions.",
             "correct": False,
             "why": "This lesson names three of them, and the bench is built "
                    "to make you find them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s07",
        "band": "standard",
        "text": "The timeline gives the evidence that broke every model "
                "except one. What broke Democritus's idea?",
        "options": [
            {"text": "The discovery that atoms have smaller parts inside "
                     "them, which he had said was impossible.",
             "correct": False,
             "why": "That broke Dalton's model, two thousand years later. By "
                    "then Democritus's version had long been overtaken."},
            {"text": "The measurement of 50 ml and 50 ml giving 97 ml.",
             "correct": False,
             "why": "That measurement supports the particle idea rather than "
                    "breaking it. It is one of the numbers that finally made "
                    "it science."},
            {"text": "Nothing broke it — and that was the problem, because an "
                     "idea nobody can test cannot win.",
             "correct": True},
            {"text": "Rutherford's experiment with the gold foil.",
             "correct": False,
             "why": "That broke Thomson's plum pudding, and it came in the "
                    "twentieth century."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s08",
        "band": "standard",
        "text": "The lesson says the three failures were treated as a map. "
                "What does that mean?",
        "options": [
            {"text": "That they were written down and then set aside as "
                     "unimportant.",
             "correct": False,
             "why": "The opposite of setting aside. Each one was followed "
                    "up, and each one led somewhere."},
            {"text": "That they showed the model was worthless and had to be "
                     "abandoned as soon as they were found.",
             "correct": False,
             "why": "Nobody abandoned it. It is still used every day by "
                    "people who know exactly where it breaks."},
            {"text": "That they had to be hidden until a better model was "
                     "ready.",
             "correct": False,
             "why": "They were published and argued over. Hiding a failure is "
                    "how you lose the discovery in it."},
            {"text": "That each one marked a place where a better model was "
                     "needed, and each one eventually got built.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-06-h05",
        "band": "harder",
        "text": "Dalton's claim that atoms cannot be split turned out to be "
                "wrong. What happened to the things he used that claim to "
                "explain?",
        "options": [
            {"text": "They are still explained the same way today.",
             "correct": True},
            {"text": "They had to be explained all over again from nothing.",
             "correct": False,
             "why": "Nothing had to be started again. Conservation of mass is "
                    "explained today the way Dalton explained it."},
            {"text": "They turned out to be wrong as well, once the claim "
                     "fell.",
             "correct": False,
             "why": "The observations never changed. Mass still balances "
                    "through a reaction, exactly as it did in 1803."},
            {"text": "They are now regarded as coincidences.",
             "correct": False,
             "why": "They are regarded as well-established results. A model "
                    "being superseded does not turn its successes into "
                    "luck."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h06",
        "band": "harder",
        "text": "Suppose a new model gave particles a shape and let them be "
                "joined together in different arrangements. Which of the three "
                "failures would that deal with?",
        "options": [
            {"text": "Only ice floating, since the other two are about "
                     "solids.",
             "correct": False,
             "why": "Diamond, graphite and rubber are solids and all three "
                    "failures come from the same assumption. Shape and "
                    "joining reach all of them."},
            {"text": "All three, because all three come from treating "
                     "particles as identical featureless spheres.",
             "correct": True},
            {"text": "Only diamond and graphite, since they are the same "
                     "element.",
             "correct": False,
             "why": "Being the same element makes that one vivid, but ice and "
                    "rubber fail for the same reason — featureless spheres."},
            {"text": "None of them, because once a model has failed a test it "
                     "cannot be repaired, only replaced.",
             "correct": False,
             "why": "Repairing a model on the evidence is exactly what the "
                    "timeline shows happening, four times over."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h07",
        "band": "harder",
        "text": "A student argues: “The model is wrong about ice, so what it "
                "says about gas pressure cannot be trusted either.” What is "
                "wrong with that reasoning?",
        "options": [
            {"text": "Nothing — a model that fails once should not be trusted "
                     "anywhere.",
             "correct": False,
             "why": "That is the standard no model in science survives. It "
                    "would leave you unable to explain anything at all."},
            {"text": "Gas pressure belongs to physics rather than chemistry, "
                     "so the two have nothing to do with each other.",
             "correct": False,
             "why": "They are the same model at work in both places. What "
                    "separates them is which assumption each one uses."},
            {"text": "The failures trace to one assumption, and the "
                     "gas-pressure explanation does not rest on it.",
             "correct": True},
            {"text": "The ice failure is too small to matter.",
             "correct": False,
             "why": "It is not small — it is why lakes do not freeze solid. "
                    "The answer is not that the failure is minor but that it "
                    "is traceable."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h08",
        "band": "harder",
        "text": "Someone proposes a new model of matter that explains ice "
                "floating perfectly but gets gas pressure wrong. Should it "
                "replace the particle model?",
        "options": [
            {"text": "Yes — it explains something the old model could not, "
                     "and that is exactly what replacement means.",
             "correct": False,
             "why": "Only half of what replacement means. It also has to keep "
                    "everything the old model already got right."},
            {"text": "Yes, but only until someone finds a limit in it too.",
             "correct": False,
             "why": "Every model has limits, so that would be no test at "
                    "all. The test is whether it loses ground the old one "
                    "held."},
            {"text": "No — the particle model has been used for so long that "
                     "it cannot now be replaced.",
             "correct": False,
             "why": "Age protects nothing. The timeline shows four "
                    "replacements, each of a model that everyone had been "
                    "using."},
            {"text": "No — a replacement must reproduce what the old model "
                     "explained as well as fixing what broke it.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-06-e09",
        "band": "easier",
        "text": "The lesson uses the word evidence. What does evidence mean?",
        "options": [
            {"text": "Observations or measurements used to decide whether an "
                     "idea works.",
             "correct": True},
            {"text": "An explanation published by a scientist in a journal.",
             "correct": False,
             "why": "Publishing is how evidence is shared, not what it is. "
                    "Evidence is the observation or the measurement itself."},
            {"text": "An idea that most people have agreed on.",
             "correct": False,
             "why": "Agreement is not evidence. Every model on the timeline "
                    "was once agreed on, and evidence overturned it anyway."},
            {"text": "A guess about what will happen, made before measuring.",
             "correct": False,
             "why": "That is a prediction. Evidence is what you collect in "
                    "order to judge the prediction."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e10",
        "band": "easier",
        "text": "The timeline's first entry is Democritus. What did his idea "
                "claim?",
        "options": [
            {"text": "That every element is made of identical solid atoms that "
                     "cannot be split.",
             "correct": False,
             "why": "That is Dalton, twenty-two centuries later. Democritus "
                    "made no claim about elements and had no numbers."},
            {"text": "That matter cannot be divided forever, so there must be "
                     "a smallest piece.",
             "correct": True},
            {"text": "That matter is continuous, and can be cut into smaller "
                     "pieces without end.",
             "correct": False,
             "why": "That was the rival idea his own argument was set against, "
                    "not his."},
            {"text": "That an atom has a tiny dense centre.",
             "correct": False,
             "why": "That is Rutherford, in 1911. Democritus had no way of "
                    "knowing anything about the inside of a particle."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e11",
        "band": "easier",
        "text": "What did Dalton's model say every element is made of?",
        "options": [
            {"text": "A ball of positive charge with tiny negative electrons "
                     "dotted through it.",
             "correct": False,
             "why": "That is Thomson's plum pudding, which replaced Dalton's "
                    "once the electron was found."},
            {"text": "Particles joined into long tangled chains that can "
                     "straighten out and spring back.",
             "correct": False,
             "why": "No model on the timeline says that. It is the repair a "
                    "stretchy material needs, and it comes much later."},
            {"text": "Identical solid atoms that cannot be split, created or "
                     "destroyed.",
             "correct": True},
            {"text": "A tiny dense nucleus with electrons somewhere around it.",
             "correct": False,
             "why": "That is Rutherford's. Dalton's atom had nothing inside "
                    "it, because it had no parts at all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e12",
        "band": "easier",
        "text": "According to the timeline, what does Rutherford's model say "
                "about where an atom's mass is?",
        "options": [
            {"text": "It is spread evenly through the whole of the atom's "
                     "volume.",
             "correct": False,
             "why": "That is closer to Thomson's picture. Rutherford's whole "
                    "point was that the mass is concentrated."},
            {"text": "It is carried by the electrons, which is why they are so "
                     "hard to knock off.",
             "correct": False,
             "why": "Electrons were knocked off easily — that is how Thomson "
                    "found them. They carry hardly any of the mass."},
            {"text": "It is shared equally between the nucleus and the "
                     "electron shells.",
             "correct": False,
             "why": "Not equally. Almost all of the mass is in the nucleus, "
                    "which is why a few alpha particles bounced back."},
            {"text": "Almost all of it sits in a tiny dense nucleus.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e13",
        "band": "easier",
        "text": "Bohr's model and the ones after it describe electrons in a "
                "particular way. Which description is it?",
        "options": [
            {"text": "As identical solid spheres packed tightly together in "
                     "rows.",
             "correct": False,
             "why": "That is how a solid is drawn in the particle model, not "
                    "how an electron is described in any model of the atom."},
            {"text": "As a smear of positive charge filling the whole atom.",
             "correct": False,
             "why": "Electrons are negative, and the smear of positive charge "
                    "was Thomson's pudding rather than his electrons."},
            {"text": "As restricted to particular energy levels, and better "
                     "described as clouds of probability.",
             "correct": True},
            {"text": "As tiny lumps of matter with no charge, scattered at "
                     "random throughout the whole atom.",
             "correct": False,
             "why": "An electron carries a negative charge; that is the one "
                    "thing Thomson established about it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e14",
        "band": "easier",
        "text": "The timeline names the evidence that broke Thomson's plum "
                "pudding model. What was it?",
        "options": [
            {"text": "The discovery of the electron inside the atom.",
             "correct": False,
             "why": "That is what Thomson himself found, and it is what broke "
                    "the model before his rather than his own."},
            {"text": "A calculation showing that orbiting electrons should "
                     "spiral into the nucleus.",
             "correct": False,
             "why": "That came later and broke Rutherford's model. Thomson's "
                    "pudding had no nucleus for anything to spiral into."},
            {"text": "Atoms of one element were found to have different "
                     "masses from one another.",
             "correct": False,
             "why": "That is one of the two things that broke Dalton's model, "
                    "not Thomson's."},
            {"text": "Alpha particles fired at gold foil, a few of which "
                     "bounced straight back.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e15",
        "band": "easier",
        "text": "The timeline gives the current model, shells and then clouds. "
                "What does it say has broken that model so far?",
        "options": [
            {"text": "A calculation showing that atoms should have collapsed "
                     "long ago.",
             "correct": False,
             "why": "That broke Rutherford's model two steps earlier, and the "
                    "current model was built to answer it."},
            {"text": "The discovery that atoms of one element have different "
                     "masses.",
             "correct": False,
             "why": "That broke Dalton's model, more than a century before "
                    "the current one."},
            {"text": "An experiment in which alpha particles bounced back off "
                     "gold foil.",
             "correct": False,
             "why": "That broke Thomson's plum pudding. It is the evidence "
                    "the current model's own ancestor was built on."},
            {"text": "Nothing yet, for chemistry.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e16",
        "band": "easier",
        "text": "The lesson says that knowing where a model's limits are is "
                "part of what?",
        "options": [
            {"text": "Part of understanding the model.",
             "correct": True},
            {"text": "Part of proving that the model is completely true.",
             "correct": False,
             "why": "Nothing proves a model completely true, and the lesson "
                    "says a model is not judged on that in the first place."},
            {"text": "Part of showing that the model should be thrown away.",
             "correct": False,
             "why": "Limits are not grounds for throwing a model away. Every "
                    "model has them, including the ones in use today."},
            {"text": "Part of deciding which scientists to believe about it.",
             "correct": False,
             "why": "Who to believe is not the question. A limit is a fact "
                    "about the model, not about the people using it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e17",
        "band": "easier",
        "text": "Ice floating is one of the three observations the model gets "
                "wrong. What would the model need in order to explain it?",
        "options": [
            {"text": "Particles that are smaller in the solid than they are in "
                     "the liquid.",
             "correct": False,
             "why": "Particles never change size. The spacing and the pattern "
                    "change; the particles themselves do not."},
            {"text": "Particles that stop moving altogether once a substance "
                     "has frozen.",
             "correct": False,
             "why": "Particles in a solid still vibrate, and stopping them "
                    "would not make the solid less dense than the liquid."},
            {"text": "Particles with a shape, that hold each other at arm's "
                     "length in a fixed pattern.",
             "correct": True},
            {"text": "Particles that gain extra mass as the liquid turns into "
                     "a solid.",
             "correct": False,
             "why": "Mass is conserved through a change of state — the sealed "
                    "bag on the bench is the evidence for exactly that."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e18",
        "band": "easier",
        "text": "Diamond and graphite are both nothing but carbon, yet they "
                "are completely different materials. What must a model have "
                "before it can explain that?",
        "options": [
            {"text": "Particles that can be created and destroyed during a "
                     "change of state.",
             "correct": False,
             "why": "Particles are neither created nor destroyed, and neither "
                    "diamond nor graphite is being changed in state here."},
            {"text": "Particles that move faster in one than the other.",
             "correct": False,
             "why": "Speed does not make one material hard and the other "
                    "soft. Both sit on the bench at the same temperature."},
            {"text": "Particles that are much larger in diamond than they are "
                     "in graphite.",
             "correct": False,
             "why": "It is the same element, so they are the same carbon "
                    "particles. Only the way they are joined differs."},
            {"text": "Particles that can be joined together in different "
                     "arrangements.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e19",
        "band": "easier",
        "text": "A rubber band stretches to five times its length and snaps "
                "back. What does a model need in order to explain that?",
        "options": [
            {"text": "Particles that are squashy and change shape when they "
                     "are pulled.",
             "correct": False,
             "why": "Particles are not squashy, and a squashy particle would "
                    "not pull the band back to where it started."},
            {"text": "Particles that are packed in neat rows and slide past "
                     "one another freely.",
             "correct": False,
             "why": "That is roughly what the simple model already offers, "
                    "and it is precisely what cannot stretch and recoil."},
            {"text": "Particles that leave the rubber while it is stretched "
                     "and return to it afterwards.",
             "correct": False,
             "why": "Nothing leaves the band. Weigh it stretched and slack "
                    "and the reading does not move."},
            {"text": "Particles joined into long tangled chains that "
                     "straighten out and spring back.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e20",
        "band": "easier",
        "text": "A melting ice cube is sealed in a bag, and the mass does not "
                "change by a milligram. What does the model say has happened "
                "to the particles?",
        "options": [
            {"text": "They have been destroyed, and new water particles have "
                     "taken their place.",
             "correct": False,
             "why": "Nothing is destroyed and nothing is made. If particles "
                    "were being swapped the mass would not hold so exactly."},
            {"text": "They have gained mass from the warm air, which balances "
                     "what the melting takes.",
             "correct": False,
             "why": "The bag is sealed, so nothing enters it. Two changes "
                    "cancelling to the milligram would be a coincidence."},
            {"text": "They have become fewer, but each of the survivors is now "
                     "heavier.",
             "correct": False,
             "why": "The count does not change either. A change of state "
                    "moves particles about; it does not remove any."},
            {"text": "They have only been rearranged.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e21",
        "band": "easier",
        "text": "The model handles a smell spreading through a room. What does "
                "the lesson say carries the smell most of the way?",
        "options": [
            {"text": "The particles of the air, which push the smell ahead of "
                     "them.",
             "correct": False,
             "why": "Air particles do not push a smell along in front of "
                    "them; they collide with it from every side at once."},
            {"text": "The random movement of the smell's own particles, and "
                     "nothing else.",
             "correct": False,
             "why": "Random movement alone is far too slow for a room. It "
                    "covers the last stretch, not the journey."},
            {"text": "Nothing carries it; the smell is simply noticed sooner "
                     "as it grows stronger.",
             "correct": False,
             "why": "Something really does travel across the room — the "
                    "particles of the smelly substance reach your nose."},
            {"text": "Draughts and convection.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e22",
        "band": "easier",
        "text": "A sealed helium balloon gets smaller over three days. Why "
                "does the lesson call this a good test of the model?",
        "options": [
            {"text": "Because only a balloon lets a gas escape.",
             "correct": False,
             "why": "Gases work their way out of plenty of containers. The "
                    "balloon is simply where you can watch it happen."},
            {"text": "Because the answer is not obvious — the balloon has no "
                     "hole in it.",
             "correct": True},
            {"text": "Because it is the only observation on the bench the "
                     "model gets right.",
             "correct": False,
             "why": "The model handles four of the seven. The balloon is one "
                    "of those four, not the only one."},
            {"text": "Because it can be repeated at home, which no other "
                     "observation can.",
             "correct": False,
             "why": "Ice floating can be watched in any kitchen. Where a test "
                    "is done is not what makes it a good test."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e23",
        "band": "easier",
        "text": "The lesson names four things the model gets right with almost "
                "no effort. Which set is it?",
        "options": [
            {"text": "Melting, pressure, diffusion and dissolving.",
             "correct": True},
            {"text": "Melting, floating, stretching and dissolving.",
             "correct": False,
             "why": "Floating and stretching are two of the three failures, "
                    "so neither belongs on a list of successes."},
            {"text": "Pressure, diffusion, hardness and stretching.",
             "correct": False,
             "why": "Hardness is the diamond and graphite problem, and "
                    "stretching is the rubber band. Both are failures."},
            {"text": "Floating, hardness, stretching and dissolving.",
             "correct": False,
             "why": "Three of these four are the three failures. Only "
                    "dissolving belongs on the list."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e24",
        "band": "easier",
        "text": "Democritus's idea had a rival that lasted just as long. What "
                "did the rival idea say?",
        "options": [
            {"text": "That matter is made of atoms that carry an electric "
                     "charge.",
             "correct": False,
             "why": "Charge arrives with Thomson, twenty-three centuries "
                    "later. Nobody in 400 BC had any idea of it."},
            {"text": "That matter is continuous, with no smallest piece in it "
                     "at all.",
             "correct": True},
            {"text": "That matter is a single unbroken substance only inside "
                     "living things.",
             "correct": False,
             "why": "The rival view made no distinction between living and "
                    "non-living matter. It applied to everything."},
            {"text": "That matter is made of particles that are constantly in "
                     "motion.",
             "correct": False,
             "why": "That is part of the particle picture itself, so it is on "
                    "Democritus's side of the argument rather than against."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e25",
        "band": "easier",
        "text": "The timeline puts five models in order. Which one came first?",
        "options": [
            {"text": "Dalton's solid spheres.",
             "correct": False,
             "why": "Dalton is 1803, and he is second. The timeline opens on "
                    "him only because he is the model you have been using."},
            {"text": "Democritus's uncuttable piece.",
             "correct": True},
            {"text": "Thomson's plum pudding.",
             "correct": False,
             "why": "Thomson is 1897, and he is third. His model replaced "
                    "Dalton's."},
            {"text": "Rutherford's nucleus.",
             "correct": False,
             "why": "Rutherford is 1911, and he is fourth. Only the current "
                    "model comes after him."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e26",
        "band": "easier",
        "text": "The lesson pictures Rutherford's atom as a marble on the "
                "centre spot of a football pitch. Where would the nearest "
                "electron be?",
        "options": [
            {"text": "Somewhere in the stands.",
             "correct": True},
            {"text": "Just outside the centre circle.",
             "correct": False,
             "why": "Far too close. The picture is chosen to show that an "
                    "atom is overwhelmingly empty."},
            {"text": "On the penalty spot at one end of the pitch.",
             "correct": False,
             "why": "Still on the pitch, so still much too close. The "
                    "electron is further out than the playing surface."},
            {"text": "Touching the marble, on the centre spot itself.",
             "correct": False,
             "why": "That would be an atom with nothing empty in it, which is "
                    "the opposite of what Rutherford found."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e27",
        "band": "easier",
        "text": "Dalton's version of the particle idea was the first with "
                "numbers attached. Which of these was one of those numbers?",
        "options": [
            {"text": "Elements combine in whole-number ratios.",
             "correct": True},
            {"text": "Every atom of every element weighs the same.",
             "correct": False,
             "why": "Dalton said atoms of ONE element are identical. Atoms of "
                    "different elements have different masses."},
            {"text": "Atoms lose mass each time they take part in a reaction.",
             "correct": False,
             "why": "The opposite: mass is conserved through a reaction, and "
                    "that was one of Dalton's strongest points."},
            {"text": "Every element is made of exactly one hundred atoms.",
             "correct": False,
             "why": "No model has ever said that. A sample of any element "
                    "holds an enormous number of atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e28",
        "band": "easier",
        "text": "For about how long did Democritus's idea sit beside its rival "
                "with nothing to choose between them?",
        "options": [
            {"text": "Roughly a hundred years.",
             "correct": False,
             "why": "Far too short. The argument was still unsettled long "
                    "after the Roman empire had come and gone."},
            {"text": "Roughly five hundred years.",
             "correct": False,
             "why": "Still far too short. Nothing could test the idea until "
                    "measurement caught up, and that took much longer."},
            {"text": "Roughly two thousand years.",
             "correct": True},
            {"text": "Roughly fifty years.",
             "correct": False,
             "why": "Fifty years is about the life of one thinker. The "
                    "argument outlasted many generations of them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e29",
        "band": "easier",
        "text": "The lesson says a wrong prediction is not a disgrace. What "
                "does it say a wrong prediction actually gives you?",
        "options": [
            {"text": "A reason to stop trusting the person who made it.",
             "correct": False,
             "why": "Dalton was not careless; he was working with the "
                    "evidence he had. A wrong prediction is not a character "
                    "fault."},
            {"text": "A place to look next, which is the most useful thing a "
                     "model can produce.",
             "correct": True},
            {"text": "Proof that the model was built carelessly in the first "
                     "place.",
             "correct": False,
             "why": "Careful models make wrong predictions too. That is how "
                    "their limits are found at all."},
            {"text": "Grounds for dropping the model and starting the whole "
                     "thing again from nothing.",
             "correct": False,
             "why": "Nobody started again. The particle model is still in "
                    "daily use, failures and all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-e30",
        "band": "easier",
        "text": "Thomson's model kept one thing from Dalton's and added "
                "another. What did it add?",
        "options": [
            {"text": "That atoms of one element all have exactly the same "
                     "mass.",
             "correct": False,
             "why": "That was Dalton's claim, and it is one of the two things "
                    "that later turned out to be wrong."},
            {"text": "That atoms are arranged in rows inside a solid.",
             "correct": False,
             "why": "That is the particle model's picture of a solid, and it "
                    "is about arrangement rather than about the atom."},
            {"text": "That atoms have parts, and one of those parts carries "
                     "charge.",
             "correct": True},
            {"text": "That atoms are created and destroyed during a reaction.",
             "correct": False,
             "why": "Conservation of mass is exactly what Thomson kept from "
                    "Dalton. Nothing on the timeline ever said this."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c1-06-s09",
        "band": "standard",
        "text": "A few alpha particles fired at gold foil bounced straight "
                "back. Explain why that broke the plum pudding model.",
        "options": [
            {"text": "Because the plum pudding model said an atom had no "
                     "electrons inside it anywhere.",
             "correct": False,
             "why": "Electrons are the one thing the plum pudding definitely "
                    "had. Thomson built the model around them."},
            {"text": "Because a charge spread thinly through the whole atom "
                     "could not turn one back.",
             "correct": True},
            {"text": "Because the model said an atom was much too small for "
                     "anything at all to strike it.",
             "correct": False,
             "why": "Nobody claimed atoms could not be hit. The experiment "
                    "hit them, and most of the alpha particles went through."},
            {"text": "Because gold was the one element the plum pudding did "
                     "not cover.",
             "correct": False,
             "why": "The model claimed to describe every element. Gold was "
                    "chosen because it can be beaten very thin, not because "
                    "it was an exception."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s10",
        "band": "standard",
        "text": "A student says the model failed on the helium balloon, "
                "because the gas escaped from a container with no hole in it. "
                "Explain why that is wrong.",
        "options": [
            {"text": "The model explains it — the rubber is particles with "
                     "gaps, and helium fits through.",
             "correct": True},
            {"text": "The model does not deal with gases at all, so there is "
                     "nothing here for it to fail at.",
             "correct": False,
             "why": "Gases are what the model handles best. Squashing, "
                    "pressure and diffusion are all gas behaviour."},
            {"text": "The balloon must have had a hole in it that nobody spotted.",
             "correct": False,
             "why": "No hole is needed. A solid is particles with gaps "
                    "between them, and small particles work their way "
                    "through."},
            {"text": "Helium is not made of particles, so a model about "
                     "particles has nothing to say about it.",
             "correct": False,
             "why": "Helium is made of particles like everything else. It is "
                    "the smallness of those particles that matters here."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s11",
        "band": "standard",
        "text": "The hook offers the answer that somebody must have measured "
                "the ice wrongly. Explain why that answer will not do.",
        "options": [
            {"text": "Because measurements in chemistry are checked over and "
                     "over, so they are hardly ever wrong.",
             "correct": False,
             "why": "Measurements are wrong often enough to be worth "
                    "checking. This one is safe for a different reason: it is "
                    "seen everywhere, by everyone."},
            {"text": "Because ice floating is seen every winter by everybody; "
                     "the observation is not in doubt.",
             "correct": True},
            {"text": "Because the model is older than the measurement, and so "
                     "the model is the one to be believed.",
             "correct": False,
             "why": "Age gives a model no authority over an observation. The "
                    "whole timeline is old models losing to new evidence."},
            {"text": "Because only the scientist who built a model may test "
                     "what it predicts.",
             "correct": False,
             "why": "Anybody may test a prediction, and a model nobody else "
                    "is allowed to test is not being tested at all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s12",
        "band": "standard",
        "text": "The model is still used every day by people who know exactly "
                "where it breaks. Explain why they keep using it.",
        "options": [
            {"text": "Because no better account of matter has ever been "
                     "suggested by anybody.",
             "correct": False,
             "why": "Better accounts exist, and the next unit begins one. The "
                    "simple model is kept because it is quick, not because "
                    "there is nothing else."},
            {"text": "Because changing to a different model would mean "
                     "rewriting every textbook in the country.",
             "correct": False,
             "why": "Textbooks are rewritten whenever the science moves. "
                    "Convenience for publishers is not why a model survives."},
            {"text": "Because it answers melting, pressure, diffusion and "
                     "dissolving with almost no effort.",
             "correct": True},
            {"text": "Because a model with any failure at all has to be "
                     "kept in use until a perfect one is built.",
             "correct": False,
             "why": "No such rule exists, and no perfect model has ever been "
                    "built. A model is kept for as long as it is useful."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s13",
        "band": "standard",
        "text": "Dalton's model was broken partly because atoms of one element "
                "turned out to have different masses. Explain why that was a "
                "problem for him.",
        "options": [
            {"text": "He had said atoms of one element are identical, so "
                     "different masses contradict him.",
             "correct": True},
            {"text": "He had said that atoms gain mass during a reaction, so "
                     "equal masses before and after contradict him.",
             "correct": False,
             "why": "Dalton said mass is conserved through a reaction, and "
                    "that part of his model survived him."},
            {"text": "He had measured every one of those atoms himself, so a "
                     "difference in mass meant an error.",
             "correct": False,
             "why": "Nobody in 1803 could weigh a single atom. Dalton worked "
                    "from the masses of whole samples."},
            {"text": "He had said atoms could be split, so a difference in "
                     "mass could not arise.",
             "correct": False,
             "why": "Dalton said the opposite — that an atom cannot be split "
                    "at all. Thomson is the one who showed it has parts."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s14",
        "band": "standard",
        "text": "Explain why identical featureless spheres cannot account for "
                "diamond being the hardest natural substance while graphite is "
                "soft enough to write with.",
        "options": [
            {"text": "Because the model gives it no way to make one "
                     "substance's particles move faster than another "
                     "substance's do.",
             "correct": False,
             "why": "Speed is about temperature, and both materials sit at "
                    "the same temperature. The difference is in structure."},
            {"text": "Because identical particles give one substance one set "
                     "of properties, and these are one substance.",
             "correct": True},
            {"text": "Because the model says a hard substance must be made of "
                     "larger particles than a soft one.",
             "correct": False,
             "why": "The model says nothing of the kind, and here the "
                    "particles are the same carbon in both materials."},
            {"text": "Because carbon is the one element the model was never "
                     "intended to cover.",
             "correct": False,
             "why": "The model claims to cover all matter. Carbon is awkward "
                    "for it, which is not the same as being excluded."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s15",
        "band": "standard",
        "text": "Explain why the changes on the timeline add up instead of "
                "cancelling each other out.",
        "options": [
            {"text": "Because each new model was built by people who had "
                     "spent their whole careers with the last one.",
             "correct": False,
             "why": "Rutherford had worked under Thomson, but who built a "
                    "model is not what makes the changes accumulate."},
            {"text": "Because scientists decide in advance exactly how much "
                     "of any model may be altered at one time.",
             "correct": False,
             "why": "No such rule exists. What limits a new model is the "
                    "evidence it has to account for, not an agreed quota."},
            {"text": "Because each new model had to keep everything the old "
                     "one got right, and fix what broke it.",
             "correct": True},
            {"text": "Because a model may only be replaced once every hundred "
                     "years or so.",
             "correct": False,
             "why": "Thomson's model lasted fourteen years and Rutherford's "
                    "two. There is no timetable."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s16",
        "band": "standard",
        "text": "Explain why the lesson calls Democritus's idea untestable "
                "rather than simply wrong.",
        "options": [
            {"text": "No observation at all could have settled it either way.",
             "correct": True},
            {"text": "It disagreed with what most other thinkers of the time "
                     "believed.",
             "correct": False,
             "why": "Disagreeing with the majority is not a fault in an idea. "
                    "Every model on the timeline did that at first."},
            {"text": "It was written down in a language nobody could read "
                     "afterwards.",
             "correct": False,
             "why": "The argument came down to us perfectly well. What was "
                    "missing was a way of checking it."},
            {"text": "It made a prediction that was checked by others and "
                     "found to be false.",
             "correct": False,
             "why": "It made no checkable prediction at all, which is the "
                    "whole difficulty. A false prediction would have been "
                    "progress."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s17",
        "band": "standard",
        "text": "Explain why the lesson goes looking for the model's edges on "
                "purpose, rather than collecting more evidence that fits.",
        "options": [
            {"text": "Because evidence that fits is much harder to find than "
                     "evidence that does not.",
             "correct": False,
             "why": "Evidence that fits is the easy kind, which is why the "
                    "first five lessons are full of it."},
            {"text": "Because a model that fits every observation has to be "
                     "wrong somewhere.",
             "correct": False,
             "why": "Fitting everything is not itself a fault. The trouble "
                    "with an untested model is that nobody knows where it "
                    "stands."},
            {"text": "Because collecting evidence that fits is the job of "
                     "physics rather than chemistry.",
             "correct": False,
             "why": "Both subjects test their models the same way. There is "
                    "no division of labour of that sort."},
            {"text": "Because a model is only worth something once you know "
                     "where it stops working.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s18",
        "band": "standard",
        "text": "A scientist finds an observation their model gets wrong and "
                "writes it down carefully rather than setting it aside. "
                "Explain what that gains them.",
        "options": [
            {"text": "It shows every other scientist that the model was put "
                     "together carefully in the first place.",
             "correct": False,
             "why": "A recorded failure says nothing about how carefully the "
                    "model was built. It says where the model stops."},
            {"text": "It proves the observation must have been made by "
                     "somebody who was careless.",
             "correct": False,
             "why": "The observation is usually sound; it is the model that "
                    "is short. Ice really does float."},
            {"text": "It allows the model to keep its name even after it has "
                     "been shown to fail.",
             "correct": False,
             "why": "Names are not what is at stake. Renaming a model changes "
                    "nothing about what it predicts."},
            {"text": "It marks the place where a better model is needed, "
                     "which is where the next one comes from.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s19",
        "band": "standard",
        "text": "Explain why Thomson's model was an advance on Dalton's, even "
                "though Dalton's had been in use for nearly a century.",
        "options": [
            {"text": "Because it dropped everything Dalton had claimed and "
                     "started again from nothing.",
             "correct": False,
             "why": "It kept a great deal of Dalton. Replacement in science "
                    "is almost never demolition."},
            {"text": "Because a far larger number of scientists had come to "
                     "agree with it than had ever agreed with Dalton's.",
             "correct": False,
             "why": "Head-counting is not what makes one model better than "
                    "another. Evidence is."},
            {"text": "Because it came later, and in science the model that "
                     "comes later is always the better one.",
             "correct": False,
             "why": "Being newer earns a model nothing on its own. It has to "
                    "account for something the old one could not."},
            {"text": "Because it kept what Dalton got right about reactions "
                     "and added that atoms have parts.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s20",
        "band": "standard",
        "text": "A student asks what would have to happen before chemists "
                "replaced the model of shells and clouds. Which answer fits "
                "the lesson?",
        "options": [
            {"text": "A larger group of chemists would have to come to prefer "
                     "a different account of the atom.",
             "correct": False,
             "why": "Preference is not the test. Every model on the timeline "
                    "was preferred by the chemists of its day until evidence "
                    "moved."},
            {"text": "The model would have to reach its two-hundredth "
                     "birthday without being changed by anyone.",
             "correct": False,
             "why": "Surviving a long time is not a reason to replace a "
                    "model. Age settles nothing either way."},
            {"text": "Evidence would have to turn up that the model gets "
                     "wrong, and a better account of it.",
             "correct": True},
            {"text": "Somebody would have to show that the periodic table had "
                     "been drawn up wrongly.",
             "correct": False,
             "why": "The table is not the model. It is one of the things the "
                    "current model explains."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s21",
        "band": "standard",
        "text": "Explain why the model's success on dissolving does not rescue "
                "it from the diamond and graphite problem.",
        "options": [
            {"text": "Because dissolving is a physical change and hardness is "
                     "a chemical one, so the two never meet.",
             "correct": False,
             "why": "Hardness is not a chemical change at all. The two are "
                    "not separated by any such rule."},
            {"text": "Because a model is judged on both what it explains and "
                     "where it fails, not on one alone.",
             "correct": True},
            {"text": "Because dissolving is a great deal easier to explain "
                     "than any other observation on the bench.",
             "correct": False,
             "why": "How hard an explanation is does not enter into it. A "
                    "success does not cancel a failure elsewhere."},
            {"text": "Because the model only claims to cover liquids, and "
                     "diamond and graphite are solids.",
             "correct": False,
             "why": "The model covers all three states. Solids are where it "
                    "started."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s22",
        "band": "standard",
        "text": "The three failures need particles that differ from each "
                "other, or particles joined in a particular way. Explain which "
                "of the two the rubber band needs.",
        "options": [
            {"text": "Joined, because stretching and recoiling needs long "
                     "chains to unfold and pull back.",
             "correct": True},
            {"text": "Differing, because rubber is made of two different "
                     "substances mixed together in it.",
             "correct": False,
             "why": "Rubber's trouble is not a mixture. A single substance "
                    "made of long chains behaves this way."},
            {"text": "Differing, because a stretched band is a different "
                     "substance from a slack one.",
             "correct": False,
             "why": "Stretching a band does not change what it is made of. "
                    "Let it go and it is the same rubber as before."},
            {"text": "Neither, because the rubber band is the one failure "
                     "that giving the particles a shape would fix.",
             "correct": False,
             "why": "Shape alone is the repair ice needs. Stretching and "
                    "recoiling needs particles joined into chains."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s23",
        "band": "standard",
        "text": "The timeline ends without saying the current model is finally "
                "correct. Explain why it stops short of that.",
        "options": [
            {"text": "Because chemists have not yet finished agreeing on what "
                     "the current model says.",
             "correct": False,
             "why": "There is no disagreement about what it says. The point "
                    "is that no model can be declared final."},
            {"text": "Because the current model is known to be wrong and is "
                     "waiting to be replaced.",
             "correct": False,
             "why": "Nothing has broken it for chemistry. It is the "
                    "best-tested account available, not a known failure."},
            {"text": "Because no model can be shown to be final, and this one "
                     "has limits of its own.",
             "correct": True},
            {"text": "Because the timeline was written before the current "
                     "model had been worked out.",
             "correct": False,
             "why": "The timeline runs up to the present and includes the "
                    "current model as its last entry."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s24",
        "band": "standard",
        "text": "A weather service keeps a forecasting model that is right "
                "four days out of five, and publishes the conditions under "
                "which it goes wrong. Apply this lesson's rule to it.",
        "options": [
            {"text": "The list of failures shows the model is not fit to be "
                     "used at all.",
             "correct": False,
             "why": "A model with known failures is exactly what scientists "
                    "keep and use. The particle model is one."},
            {"text": "The model should be given the name forecasting theory, "
                     "which allows exceptions.",
             "correct": False,
             "why": "A word change fixes nothing. The forecast is just as "
                    "wrong on the fifth day whatever it is called."},
            {"text": "The fifth day should simply be left out of every "
                     "forecast the service publishes.",
             "correct": False,
             "why": "Hiding the failure loses the information in it. The "
                    "conditions that break it are worth knowing."},
            {"text": "Knowing where it fails is part of understanding it, so "
                     "the list is a strength.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s25",
        "band": "standard",
        "text": "Explain why the model's account of a smell crossing a room "
                "needs draughts as well as the movement of particles.",
        "options": [
            {"text": "Because a smell cannot travel through still air at all "
                     "without being pushed.",
             "correct": False,
             "why": "It can. Random movement will take it there in the end — "
                    "it simply takes far longer than a minute."},
            {"text": "Because draughts are what break the smell up into "
                     "particles small enough to move.",
             "correct": False,
             "why": "The particles are already that size. A draught moves "
                    "them; it does not break anything up."},
            {"text": "Because the model has nothing to say about how gases "
                     "move from one place to another.",
             "correct": False,
             "why": "Gas movement is one of the things the model is best at. "
                    "That is why the observation counts as handled."},
            {"text": "Because particle movement alone would be far too slow "
                     "to do the whole job.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s26",
        "band": "standard",
        "text": "A model of matter is proposed that explains every observation "
                "made so far but predicts nothing new. Explain the difficulty "
                "with it.",
        "options": [
            {"text": "It would have to be abandoned, because a model that "
                     "fits everything must be false.",
             "correct": False,
             "why": "Fitting everything is not proof of falsehood. The "
                    "trouble is that nothing could ever put it to the test."},
            {"text": "It would be too complicated for anybody to use on an "
                     "ordinary observation.",
             "correct": False,
             "why": "Nothing here says it is complicated. A simple model can "
                    "be just as untestable."},
            {"text": "It could not be published, because journals require a "
                     "prediction to be made.",
             "correct": False,
             "why": "Publication is not the difficulty. Democritus's idea was "
                    "known to everybody and still could not win."},
            {"text": "There would be no way to test it, and an idea evidence "
                     "cannot reach cannot win.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s27",
        "band": "standard",
        "text": "Explain how the sealed bag of melting ice supports the claim "
                "that particles are neither made nor destroyed.",
        "options": [
            {"text": "Because the bag stops any particles getting in or out, "
                     "so nothing inside it can change at all.",
             "correct": False,
             "why": "Plenty changes inside it — the ice melts. What does not "
                    "change is the number of particles."},
            {"text": "Because the ice and the water are two different "
                     "substances with the same mass.",
             "correct": False,
             "why": "They are the same substance in two states. That is what "
                    "makes the unchanged mass tell you something."},
            {"text": "Because the mass holds to the milligram while the "
                     "arrangement of the particles changes.",
             "correct": True},
            {"text": "Because water is the one substance whose particles can "
                     "never be created or destroyed at all.",
             "correct": False,
             "why": "No substance's particles are created or destroyed in a "
                    "change of state. Water is not special here."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s28",
        "band": "standard",
        "text": "Explain why the lesson describes the current model of the "
                "atom as the one behind the periodic table.",
        "options": [
            {"text": "Because energy levels are what the table's rows and "
                     "columns are built from.",
             "correct": True},
            {"text": "Because the periodic table was drawn up before any "
                     "model of the atom existed.",
             "correct": False,
             "why": "The table came after Dalton, and the current model "
                    "explains the pattern the table had already shown."},
            {"text": "Because Dalton arranged the table using the "
                     "whole-number ratios he had measured.",
             "correct": False,
             "why": "Dalton did not draw up the periodic table, and his model "
                    "could not have explained its pattern."},
            {"text": "Because the table is a model in its own right and needs "
                     "no atom standing behind it.",
             "correct": False,
             "why": "The table is a pattern that needed explaining, and the "
                    "current model is what explains it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s29",
        "band": "standard",
        "text": "A student says that because the particle model is a model, it "
                "is only somebody's opinion. Explain what is wrong with that.",
        "options": [
            {"text": "A model is not an opinion but a proven fact, which is "
                     "why it is used.",
             "correct": False,
             "why": "Nothing proves a model a fact. It is kept because it "
                    "survives testing, which is a different thing."},
            {"text": "It is tested against observations, and this one has "
                     "survived two centuries of that.",
             "correct": True},
            {"text": "A model is an opinion, but it belongs to somebody who "
                     "has studied the subject for years.",
             "correct": False,
             "why": "Who holds an idea is not what settles it. Democritus was "
                    "right and still could not win the argument."},
            {"text": "A model is only a drawing, and a drawing cannot be "
                     "anybody's opinion about anything at all.",
             "correct": False,
             "why": "A model is a set of claims, not a picture, and those "
                    "claims make predictions that can be checked."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-s30",
        "band": "standard",
        "text": "A bent copper wire stays bent, while a rubber band springs "
                "back. Explain why that pair is a difficulty for a model of "
                "identical spheres.",
        "options": [
            {"text": "Because copper is heavier than rubber for the same size.",
             "correct": False,
             "why": "Density is not what separates them. A heavy solid is no "
                    "more likely to hold a new shape than a light one."},
            {"text": "Because the model says every solid must spring back "
                     "into its original shape.",
             "correct": False,
             "why": "The model makes no such prediction. Its difficulty is "
                    "that it cannot predict either behaviour."},
            {"text": "Because identical spheres give no way for one solid to "
                     "hold a new shape and another not.",
             "correct": True},
            {"text": "Because copper is a metal, and the particle model was "
                     "written for non-metals only.",
             "correct": False,
             "why": "The model covers all matter, metals included. Nothing in "
                    "it excludes copper."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-06-h09",
        "band": "harder",
        "text": "Democritus said matter has a smallest piece, and today we "
                "agree. Evaluate the claim that he should therefore count as "
                "the person who discovered atoms.",
        "options": [
            {"text": "Correct — being right first is what scientific "
                     "discovery has always meant, whatever the evidence.",
             "correct": False,
             "why": "Discovery in science means showing something, not "
                    "guessing it. Being right by luck settles nothing."},
            {"text": "Weak — he had no way to test the idea, so it could not "
                     "be told apart from its rival.",
             "correct": True},
            {"text": "Correct, because his idea lasted longer than any of the "
                     "models that came after it.",
             "correct": False,
             "why": "It lasted because nothing could touch it either way, "
                    "which is the difficulty rather than the credit."},
            {"text": "Weak, because his idea disagrees with what the current "
                     "model says about matter.",
             "correct": False,
             "why": "It does not disagree; the current model still has a "
                    "smallest piece. The fault is that he could not show it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h10",
        "band": "harder",
        "text": "Compare Democritus's idea with Dalton's, and state the single "
                "change that turned the particle idea into science.",
        "options": [
            {"text": "Dalton wrote in English rather than in Greek, so far "
                     "more people could read what he said.",
             "correct": False,
             "why": "Language changed who could read it, not whether it could "
                    "be tested. That is the change that mattered."},
            {"text": "Dalton was believed by the scientists of his day, and "
                     "Democritus was not.",
             "correct": False,
             "why": "Being believed is not what makes an idea science. "
                    "Belief without a test is exactly Democritus's problem."},
            {"text": "Dalton attached numbers to it — fixed proportions by "
                     "mass, and mass conserved through reactions.",
             "correct": True},
            {"text": "Dalton made his claim about elements, and Democritus "
                     "made his about matter in general.",
             "correct": False,
             "why": "That is a real difference between them, but a narrower "
                    "claim is not a testable one. The numbers are what did "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h11",
        "band": "harder",
        "text": "Here is another observation for the bench. Salt stirred into "
                "water disappears into it, while sand stirred into the same "
                "water sits on the bottom unchanged. Does the simple model "
                "handle it?",
        "options": [
            {"text": "No — identical featureless spheres give no reason at "
                     "all for one solid to dissolve and another not.",
             "correct": True},
            {"text": "Yes — the salt particles are smaller than the sand "
                     "particles, and small particles dissolve.",
             "correct": False,
             "why": "Size is not what decides it, and the model has no way to "
                    "say which substance's particles are smaller anyway."},
            {"text": "Yes — the model explains why every solid put into water "
                     "eventually dissolves into it.",
             "correct": False,
             "why": "Not every solid dissolves, as the sand shows. The model "
                    "makes no such claim."},
            {"text": "No — the model says nothing about solids in water, so "
                     "neither case is covered by it.",
             "correct": False,
             "why": "Dissolving is one of the four things the model handles "
                    "well. What it cannot do is tell the two solids apart."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h12",
        "band": "harder",
        "text": "A student says the model failed on the helium balloon and on "
                "the rubber band, so rubber is what defeats it. Evaluate that.",
        "options": [
            {"text": "Correct — both observations are about rubber, so rubber "
                     "is the substance the model cannot reach.",
             "correct": False,
             "why": "Only one of them is a failure, and it fails because of "
                    "structure rather than because the material is rubber."},
            {"text": "Wrong — the balloon is handled; the rubber band fails, "
                     "and it fails because of structure.",
             "correct": True},
            {"text": "Wrong, because the model was never meant to be used on "
                     "a material made by people.",
             "correct": False,
             "why": "The model covers all matter, manufactured or not. "
                    "Nothing in it turns on where a material came from."},
            {"text": "Correct, because a model that fails twice on one "
                     "material has failed on that material.",
             "correct": False,
             "why": "It did not fail twice. The shrinking balloon is one of "
                    "the four cases the model gets right."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h13",
        "band": "harder",
        "text": "Suggest what would have to be shown before chemists accepted "
                "a sixth model in place of shells and clouds.",
        "options": [
            {"text": "That most chemists had grown tired of the current model "
                     "and wanted a fresh one to use.",
             "correct": False,
             "why": "Weariness is not evidence. No model on the timeline was "
                    "replaced because people had lost interest in it."},
            {"text": "That the current model has lasted longer than any before "
                     "it.",
             "correct": False,
             "why": "Longevity is not a fault. Democritus's idea lasted "
                    "longest of all and was never overturned by evidence."},
            {"text": "That it keeps everything the current model explains and "
                     "also explains what breaks it.",
             "correct": True},
            {"text": "That it can be drawn more simply than the current "
                     "model, so students find it easier.",
             "correct": False,
             "why": "Simplicity is convenient, not decisive. The simplest "
                    "model on this page gets three things wrong."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h14",
        "band": "harder",
        "text": "Two candidate repairs are offered: one gives particles a "
                "shape, the other lets particles join together. Evaluate which "
                "failures each repair reaches.",
        "options": [
            {"text": "Shape reaches all three; joining reaches none of them, "
                     "because joining is about reactions.",
             "correct": False,
             "why": "Joining is what diamond, graphite and rubber all need. "
                    "It is about structure, not only about reactions."},
            {"text": "Joining reaches all three; shape reaches none, because "
                     "shape has nothing to do with packing.",
             "correct": False,
             "why": "Shape is exactly what ice needs — particles held at "
                    "arm's length in a fixed pattern."},
            {"text": "Shape reaches ice; joining reaches diamond against "
                     "graphite and the rubber band.",
             "correct": True},
            {"text": "Neither reaches any of them, since all three failures "
                     "come from the particles being far too small.",
             "correct": False,
             "why": "Size is not the trouble at all. The model handles "
                    "particles far too small to see without difficulty."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h15",
        "band": "harder",
        "text": "Nothing has broken the current model of the atom for "
                "chemistry. Evaluate the claim that this shows it must be "
                "true.",
        "options": [
            {"text": "Correct — a model nobody has broken after a century of "
                     "trying has been proved true.",
             "correct": False,
             "why": "Surviving tests is not proof. Dalton's model survived "
                    "nearly a century and was still overturned."},
            {"text": "Correct, because being true is exactly what surviving "
                     "every test is taken to mean.",
             "correct": False,
             "why": "It means the model is the best-tested account available, "
                    "which is a different and weaker claim."},
            {"text": "Weak, because no model of the atom has ever been tested "
                     "seriously enough to break.",
             "correct": False,
             "why": "Four of them were tested until they broke. That is what "
                    "the timeline is a record of."},
            {"text": "Weak — every model on the timeline was unbroken until "
                     "the day it was broken.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h16",
        "band": "harder",
        "text": "Water and cooking oil are stirred hard together and separate "
                "again within minutes. Does the simple particle model account "
                "for that?",
        "options": [
            {"text": "No — with identical spheres there is nothing to make "
                     "one liquid's particles prefer their own.",
             "correct": True},
            {"text": "Yes — the model says particles of different substances "
                     "always settle into layers.",
             "correct": False,
             "why": "The model says nothing of the kind, and plenty of "
                    "liquids mix and stay mixed."},
            {"text": "Yes, because the model says two liquids can mix only "
                     "when their particles are the same size.",
             "correct": False,
             "why": "Size is not the rule. Water and alcohol have differently "
                    "sized particles and mix perfectly well."},
            {"text": "No, because the model covers a single substance at a "
                     "time and says nothing about mixtures.",
             "correct": False,
             "why": "It handles mixtures happily — dissolving and diffusion "
                    "are both about two substances at once."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h17",
        "band": "harder",
        "text": "The nucleus first appears in Rutherford's model. Evaluate the "
                "claim that when his model was broken, the nucleus was broken "
                "with it.",
        "options": [
            {"text": "Correct — when a model fails, everything it claimed "
                     "fails along with it.",
             "correct": False,
             "why": "Almost nothing works that way. Each replacement had to "
                    "keep what the old model got right."},
            {"text": "Wrong — the nucleus survived, and the account of the "
                     "electrons is what had to change.",
             "correct": True},
            {"text": "Correct, because the gold foil experiment was later "
                     "shown to have been set up wrongly.",
             "correct": False,
             "why": "The experiment stands, and the bouncing alpha particles "
                    "are still the evidence for a nucleus."},
            {"text": "Wrong, because the nucleus had already been proposed by "
                     "Thomson some years earlier.",
             "correct": False,
             "why": "Thomson's atom had no nucleus in it. That is precisely "
                    "what the gold foil result forced."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h18",
        "band": "harder",
        "text": "Evaluate this test for judging a model: count how many "
                "observations it explains, and choose the model with the "
                "highest count.",
        "options": [
            {"text": "Sound — the model that explains most observations is by "
                     "definition the better model to use.",
             "correct": False,
             "why": "A count says nothing about which observations were "
                    "missed, and the misses are where the next model comes "
                    "from."},
            {"text": "Unsound — it ignores where a model fails, and the "
                     "failures are half of the judgement.",
             "correct": True},
            {"text": "Sound, provided the observations counted are all taken "
                     "from the same list.",
             "correct": False,
             "why": "Where the observations come from does not rescue the "
                    "method. Counting alone is what is wrong with it."},
            {"text": "Unsound, because observations cannot be counted, only "
                     "described in words.",
             "correct": False,
             "why": "Observations can perfectly well be counted — the bench "
                    "has seven of them. The fault is elsewhere."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h19",
        "band": "harder",
        "text": "Compare the way Democritus's idea came to an end with the way "
                "Dalton's did.",
        "options": [
            {"text": "Democritus's was never put to a test; Dalton's was "
                     "broken by evidence.",
             "correct": True},
            {"text": "Both were ended by a single experiment that anybody "
                     "could repeat in a laboratory.",
             "correct": False,
             "why": "No experiment ended Democritus's idea, and Dalton's fell "
                    "to two separate findings rather than one."},
            {"text": "Both were simply forgotten, and neither left anything "
                     "behind in the models after them.",
             "correct": False,
             "why": "Dalton's conservation of mass is still used today. "
                    "Neither idea was forgotten."},
            {"text": "Democritus's was broken by evidence; Dalton's was "
                     "overtaken with nothing testing it.",
             "correct": False,
             "why": "That is the pair the wrong way round. Dalton is the one "
                    "evidence reached."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h20",
        "band": "harder",
        "text": "A chemist keeps two models of the atom side by side: the "
                "simple particle model for everyday work, and the current "
                "model for bonding. Evaluate that practice.",
        "options": [
            {"text": "Unsound — holding two models of one thing at once means "
                     "at least one of them is being used wrongly.",
             "correct": False,
             "why": "Each is being used where it works, which is what the "
                    "lesson says scientists actually did."},
            {"text": "Unsound, because a chemist must use the most complete "
                     "model available for every job.",
             "correct": False,
             "why": "The most complete model is often the slowest. NASA still "
                    "lands spacecraft with Newton for the same reason."},
            {"text": "Sound — each is used where it works, which is what the "
                     "lesson says was actually done.",
             "correct": True},
            {"text": "Sound, because the simple model has no failures in "
                     "everyday work of any kind.",
             "correct": False,
             "why": "Ice floating is everyday work, and the simple model gets "
                    "it wrong. The practice is sound for another reason."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h21",
        "band": "harder",
        "text": "A student lists the three failures and concludes that "
                "particles must not exist after all. Evaluate that conclusion.",
        "options": [
            {"text": "Sound — three failures out of seven observations show "
                     "the whole idea to be mistaken.",
             "correct": False,
             "why": "Three failures show where the model needs work. None of "
                    "them casts any doubt on particles existing."},
            {"text": "Weak — the failures are about what particles are like, "
                     "not about whether they are there.",
             "correct": True},
            {"text": "Sound, because a model that fails at all cannot "
                     "describe anything that is really there.",
             "correct": False,
             "why": "Every model has limits, and all of them describe real "
                    "things. This standard would empty chemistry."},
            {"text": "Weak, because a model can only ever be judged on the "
                     "observations it was originally built from.",
             "correct": False,
             "why": "A model is judged on everything it claims to cover, "
                    "including cases nobody had in mind when it was built."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h22",
        "band": "harder",
        "text": "Predict what would happen to the four observations the model "
                "already handles if particles were given a shape and allowed "
                "to join together.",
        "options": [
            {"text": "They would still be explained — a repair has to keep "
                     "what already worked.",
             "correct": True},
            {"text": "They would have to be explained again from nothing, "
                     "since the model has changed.",
             "correct": False,
             "why": "A repair keeps the old explanations. Rebuilding from "
                    "nothing is what replacement in science does not do."},
            {"text": "They would become failures, because a more complicated "
                     "model explains less than a simple one.",
             "correct": False,
             "why": "Adding detail does not remove what was already "
                    "explained. Thomson's model kept Dalton's successes."},
            {"text": "They would be left out, since a repaired model covers "
                     "only the cases that broke it.",
             "correct": False,
             "why": "A model covering only its own exceptions would be no "
                    "use. It has to cover both."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h23",
        "band": "harder",
        "text": "A chemist says the three failures are not failures of the "
                "model but failures of the person using it. Evaluate that.",
        "options": [
            {"text": "Sound — a model cannot fail, since it is only a set of "
                     "ideas somebody has written down.",
             "correct": False,
             "why": "A set of ideas that makes a wrong prediction has failed. "
                    "That is what a failure is."},
            {"text": "Unsound — the model itself predicts ice will sink, "
                     "whoever is doing the predicting.",
             "correct": True},
            {"text": "Sound, because a careful user could still get ice right.",
             "correct": False,
             "why": "No amount of care extracts a floating solid from "
                    "identical spheres packed tighter than the liquid."},
            {"text": "Unsound, because a model can fail only when it is used "
                     "on a substance it never claimed to cover.",
             "correct": False,
             "why": "The model claims to cover water, which is why the wrong "
                    "prediction counts against it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h24",
        "band": "harder",
        "text": "Two new models are offered. Model A explains everything the "
                "particle model does and also ice floating. Model B explains "
                "ice floating and nothing else. Evaluate them.",
        "options": [
            {"text": "Both should replace the particle model, because both "
                     "explain something it cannot.",
             "correct": False,
             "why": "Explaining something new is only half the requirement. "
                    "The other half is keeping what already worked."},
            {"text": "Neither should, because the particle model has been in "
                     "use for two centuries already.",
             "correct": False,
             "why": "Age protects no model. Four on the timeline were "
                    "replaced while everybody was still using them."},
            {"text": "Model B should replace it, because a model that "
                     "explains one thing well is the clearest.",
             "correct": False,
             "why": "Clarity bought by giving up melting, pressure, "
                    "diffusion and dissolving is not worth having."},
            {"text": "Model A should replace it; Model B gives up more than "
                     "it gains.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h25",
        "band": "harder",
        "text": "Evaluate this account of the timeline: each new model showed "
                "that the one before it had been a waste of time.",
        "options": [
            {"text": "Wrong — each replacement had to reproduce what the old "
                     "model got right, so none was wasted.",
             "correct": True},
            {"text": "Right, because a model that gets replaced was clearly "
                     "not worth building in the first place.",
             "correct": False,
             "why": "Every model on the timeline gets replaced eventually, "
                    "which would make all of them not worth building."},
            {"text": "Right, because the timeline shows four replacements in "
                     "a row, and four failures in a row.",
             "correct": False,
             "why": "A replacement is not a failure of the whole model. Most "
                    "of what each one said was carried forward."},
            {"text": "Wrong, because a model is never actually replaced; it "
                     "is simply used less often over time.",
             "correct": False,
             "why": "Thomson's pudding really was replaced. Nobody uses it "
                    "for anything today."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h26",
        "band": "harder",
        "text": "Suggest one reason why the lesson puts the failures of the "
                "model in front of a student rather than only its successes.",
        "options": [
            {"text": "Because failures are easier to remember than successes, "
                     "so they make better revision.",
             "correct": False,
             "why": "How memorable something is has nothing to do with it. "
                    "The failures are there because they are the test."},
            {"text": "Because a teacher is required to give both sides of "
                     "every idea that is taught.",
             "correct": False,
             "why": "A model's limits are not another side of an argument. "
                    "They are part of what the model is."},
            {"text": "Because a student who only sees evidence that fits has "
                     "not tested the model at all.",
             "correct": True},
            {"text": "Because the successes had all been covered already, and "
                     "there was nothing new left to say about any of them.",
             "correct": False,
             "why": "Four of the seven observations on the bench are "
                     "successes, and they are gone over again here."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h27",
        "band": "harder",
        "text": "A student proposes judging models by how simple they are, so "
                "the simplest account of matter should always be preferred. "
                "Evaluate that rule.",
        "options": [
            {"text": "Sound — the simplest account is always the one science "
                     "chooses, whatever it leaves out.",
             "correct": False,
             "why": "Simplicity is a tie-breaker between accounts that work, "
                    "not a reason to keep one that does not."},
            {"text": "Unsound — the simplest account here is identical "
                     "spheres, and it gets three things wrong.",
             "correct": True},
            {"text": "Sound, provided the simplest model is also the one that "
                     "most scientists have agreed on.",
             "correct": False,
             "why": "Agreement does not repair the rule. A simple model that "
                    "makes wrong predictions is still wrong."},
            {"text": "Unsound, because simple models are harder to test than "
                     "complicated ones are.",
             "correct": False,
             "why": "Simple models are usually easier to test. The fault is "
                    "that simplicity is not what a model is judged on."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h28",
        "band": "harder",
        "text": "Suggest why the lesson names the exact evidence that broke "
                "each model rather than just saying the model was replaced.",
        "options": [
            {"text": "Because the name of an experiment is easier to remember "
                     "than a date.",
             "correct": False,
             "why": "How memorable something is has nothing to do with it. "
                    "The evidence is named because it did the work."},
            {"text": "Because each scientist insisted that their own evidence "
                     "be recorded alongside the model.",
             "correct": False,
             "why": "The evidence that breaks a model usually comes from "
                    "somebody else, as Thomson's did for Dalton."},
            {"text": "Because it shows the models were overturned by evidence "
                     "and not by fashion.",
             "correct": True},
            {"text": "Because a model cannot be described at all unless the "
                     "evidence against it is described at the same time.",
             "correct": False,
             "why": "A model can be described on its own perfectly well. The "
                    "current one is, and nothing has broken it yet."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h29",
        "band": "harder",
        "text": "Evaluate this reply to the three failures: keep the model, "
                "and tell anyone using it which three observations to avoid.",
        "options": [
            {"text": "Sound — the three observations are the only places the "
                     "model has ever been found to fail.",
             "correct": False,
             "why": "Seven observations were chosen for the bench; they are "
                    "not a complete list of everything the model meets."},
            {"text": "Weak — avoiding them hides the very places the next "
                     "model was going to come from.",
             "correct": True},
            {"text": "Sound, because a user who avoids the failures will "
                     "never get a wrong answer out of it.",
             "correct": False,
             "why": "It would keep them out of trouble, and it would also "
                    "keep them from the discovery. That is the cost."},
            {"text": "Weak, because those three are all the model is good at.",
             "correct": False,
             "why": "They are the three it is worst at. Four of the seven are "
                    "handled completely."},
        ],
        "figure": None,
    },
    {
        "id": "c1-06-h30",
        "band": "harder",
        "text": "Compare what happened to the particle model after its "
                "failures with what happened to Thomson's model after the gold "
                "foil result.",
        "options": [
            {"text": "Both were dropped at once and rebuilt from nothing.",
             "correct": False,
             "why": "Neither was. The particle model is still in use, and "
                    "Rutherford kept a great deal of Thomson."},
            {"text": "Both are still in daily use, and neither has ever "
                     "needed replacing at all.",
             "correct": False,
             "why": "Thomson's pudding is used for nothing today. Only the "
                    "particle model is still working."},
            {"text": "The particle model is still used with its limits "
                     "recorded; Thomson's was replaced.",
             "correct": True},
            {"text": "Both were kept, and the failures of each were written "
                     "down and then quietly ignored.",
             "correct": False,
             "why": "Neither set of failures was ignored. Each one was "
                    "followed up, and each led somewhere."},
        ],
        "figure": None,
    },
]
