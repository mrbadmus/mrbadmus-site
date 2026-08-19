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
            {"text": "Helium particles have worked their way through the gaps "
                     "between the particles of the rubber.",
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
            {"text": "It predicts the solid will be denser and sink in its own "
                     "liquid; water is the other way round, so ice floats.",
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
            {"text": "Nothing in science may ever be ignored, so the whole "
                     "model has to go.",
             "correct": False,
             "why": "Too strong. Scientists do keep using models they know are "
                    "incomplete — the point is not that ignoring is banned, "
                    "but that these particular failures matter."},
            {"text": "Ice floating is why lakes do not freeze solid, and the "
                     "exceptions are where the next model came from.",
             "correct": True},
            {"text": "Three failures out of seven is far too many for anyone "
                     "to call them rare.",
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
                     "leaves out entirely.",
             "correct": False,
             "why": "The model copes with a change of state, where energy goes "
                    "in — it keeps the mass right to the milligram. What it "
                    "leaves out is structure."},
            {"text": "Each one needs the particles to differ from each other, "
                     "or to be joined together in a particular way.",
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
            {"text": "A gas is mostly empty space between its particles; in a "
                     "liquid the particles are already touching.",
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
            {"text": "Rubber is made of particles; the model fails because it "
                     "cannot join them into long tangled chains.",
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
            {"text": "Show that the dense nucleus does not exist after all.",
             "correct": False,
             "why": "The nucleus survived, and it is in every model since. "
                    "What broke was the account of the electrons, not the "
                    "evidence from the gold foil."},
            {"text": "Wait for a better experiment, since the problem was only "
                     "on paper.",
             "correct": False,
             "why": "The maths was the evidence. It predicted that every atom "
                    "in existence should already have collapsed, and plainly "
                    "none of them has."},
            {"text": "Keep everything Rutherford's model already explained, "
                     "and also explain why electrons do not spiral in.",
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
]
