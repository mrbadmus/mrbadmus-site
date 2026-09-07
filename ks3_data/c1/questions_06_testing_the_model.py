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
            {"text": "A ball of positive charge with tiny negative electrons "
                     "dotted through it.",
             "correct": True},
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
            {"text": "Because a theory is a much weaker kind of idea than a "
                     "model, so it would be a step backwards.",
             "correct": False,
             "why": "A theory is not weaker than a model. The trouble with "
                    "the swap is that it changes nothing about the "
                    "predictions."},
            {"text": "Because a theory that predicts ice will sink has "
                     "exactly the same problem as a model that does.",
             "correct": True},
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
            {"text": "They had to be explained all over again from nothing.",
             "correct": False,
             "why": "Nothing had to be started again. Conservation of mass is "
                    "explained today the way Dalton explained it."},
            {"text": "They are still explained the same way today.",
             "correct": True},
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
            {"text": "Only diamond and graphite, since they are the same "
                     "element.",
             "correct": False,
             "why": "Being the same element makes that one vivid, but ice and "
                    "rubber fail for the same reason — featureless spheres."},
            {"text": "All three, because all three come from treating "
                     "particles as identical featureless spheres.",
             "correct": True},
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
            {"text": "The failures trace to one assumption, and the "
                     "gas-pressure explanation does not rest on it.",
             "correct": True},
            {"text": "Gas pressure belongs to physics rather than chemistry, "
                     "so the two have nothing to do with each other.",
             "correct": False,
             "why": "They are the same model at work in both places. What "
                    "separates them is which assumption each one uses."},
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
            {"text": "No — a replacement must reproduce what the old model "
                     "explained as well as fixing what broke it.",
             "correct": True},
            {"text": "No — the particle model has been used for so long that "
                     "it cannot now be replaced.",
             "correct": False,
             "why": "Age protects nothing. The timeline shows four "
                    "replacements, each of a model that everyone had been "
                    "using."},
        ],
        "figure": None,
    },
]
