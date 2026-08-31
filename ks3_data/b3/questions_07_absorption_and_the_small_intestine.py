# -*- coding: utf-8 -*-
"""B3 lesson 07 — Absorption and the small intestine: twelve questions (MRB-269).

The lesson makes one argument twice over. First, geometrically: a six-metre
tube with half a square metre of inside surface becomes a six-metre tube with
about thirty, because the same sheet is folded at three scales that multiply
— ×3, ×5, ×4. Second, mechanically: nothing pushes anything across that
surface. Small soluble molecules diffuse, and they only keep diffusing because
flowing blood holds the concentration low on the far side. The four features —
large area, a wall one cell thick, a dense blood supply and a moist surface —
are the checklist both halves feed into.

The bank probes both halves. The area half is worked through the bench figures
(0.5 m², 1.5 m², 30 m², ×60), through which level gives the biggest single
gain, through the scale at which each level becomes visible, and through why
the factors multiply rather than add. The mechanical half is worked through
the direction of diffusion, through the ten-cell-thick wall, and through the
wet surface.

Distractors are built from the lesson's two declared misconceptions.
**DIET-15** ("villi make the intestine longer") supplies every option that
converts an area gain into a length gain — "it grows to about sixty metres",
"it grows a little, because each villus is about 1 mm long", "the tube also
gets longer each time a level is added", "about 6 m², one for each metre of
length". **DIET-16** ("the muscles push the food through the gut wall into the
blood") supplies every option that gives absorption a pusher — peristalsis
forcing food through the wall, muscles driving glucose across, and the softer
form of the same error, a one-way wall. Two further errors the lesson exists to
correct are worked as well: the teleological "molecules want to spread out",
which the lesson's own confrontation names and refuses, and the belief that
surface area alone decides the rate, which the four-features panel is built to
break.

⊕ MRB-233 (3c), 31 Aug 2026. This paragraph used to read: *"Three questions
come off the stretch layer and the convention note rather than the body,
because a student who meets 200 m² in a library book needs to know what to do
with it: that the older figure came from fixed, dried and stretched tissue,
that the 2014 figure is better for how it was measured rather than for being
newer, and that the exam-safe answer names the reason, not the number."*
The stretch layer it drew from is GONE (Mide's ruling — see the lesson's
`stretch` key), and with it the two questions that briefed the older figure.
The LAST clause survives everything: **the exam-safe answer names the reason,
not the number**, and that is exactly what the rewritten `h04` now marks.

No question restates a ladder rung. The rungs already own "villi increase
the…", the blocked blood supply, the whole-design explanation and coeliac
disease, so the bank works around all four: the blood supply appears only
inside distractor corrections, villous flattening is left entirely to rung 4,
and the trade-off between area and wall thickness is put as two model guts
rather than as one villus losing a feature.

`figure` is `None` throughout. The lesson declares `b3-villus-labelled`, but
with `status: "needed"` — it is a commissioned drawing that does not exist
yet, so a stem that told a student to read it would point at nothing. Every
stem here is self-contained.
"""

UNIT = "B3"
LESSON = "absorption-and-the-small-intestine"
LESSON_NUMBER = 7

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-07-e01",
        "band": "easier",
        "text": "Absorption is one particular step in what happens to a meal. "
                "Which of these is it?",
        "options": [
            {"text": "Large food molecules being broken down into small "
                     "soluble ones.", "correct": False,
             "why": "That is digestion, and it comes first. Absorption is the "
                    "step after it — the small molecules digestion produced "
                    "crossing the gut wall into the blood."},
            {"text": "Small, soluble molecules moving out of the gut into the "
                     "blood.", "correct": True},
            {"text": "Food being squeezed along the tube by the muscles in "
                     "the wall.", "correct": False,
             "why": "That is peristalsis. It moves food along the tube and "
                    "never moves anything through the wall."},
            {"text": "Blood carrying glucose away from the gut to the body’s "
                     "cells.", "correct": False,
             "why": "That is transport, and it happens after absorption. "
                    "Absorption is the crossing itself: gut to blood."},
        ],
        "figure": None,
    },
    # ⊕ MRB-233 (3c), 31 Aug 2026 — REWRITTEN TO TEST THE PRINCIPLE.
    # This question used to ask a student to PICK THE FIGURE ("how much does a
    # six-metre small intestine have?"), with 30 m² marked correct and "About
    # 200 m² — roughly the area of a tennis court" as the distractor. Mide's
    # ruling: a bank question may not mark a specific number as the answer, and
    # the tennis court leaves the estate with the lesson's revision explainer.
    # The hose framing is kept — it is the hook's own comparison and it does
    # real work — but what is now marked is WHERE the area comes from.
    # ⚠️ Deliberately NOT "villi increase the…", which is rung 1's and which
    # this bank has always worked around. This asks for all three levels.
    {
        "id": "b3-07-e02",
        "band": "easier",
        "text": "A six-metre hose and a six-metre small intestine are the "
                "same length and about the same width, yet the intestine has "
                "far more inner surface. What accounts for the difference?",
        "options": [
            {"text": "The intestine is coiled up tightly inside the abdomen.",
             "correct": False,
             "why": "Coiling packs the tube into a smaller space. It does not "
                    "add a square centimetre of inner surface — a coiled hose "
                    "has exactly the surface it had when it was straight."},
            {"text": "The intestine's wall is a great deal thinner than a "
                     "hose's, so much more of it counts as surface.",
             "correct": False,
             "why": "A thin wall is a real adaptation, and it is one of the "
                    "four — but it shortens the distance across, it does not "
                    "widen the area. Thickness and area are separate things."},
            {"text": "The intestine's wall is folded at three scales: folds, "
                     "villi and microvilli.",
             "correct": True},
            {"text": "The intestine stretches when a meal is inside it.",
             "correct": False,
             "why": "Stretching is temporary and small, and the figures in "
                    "this lesson hold the tube at six metres throughout. The "
                    "gain is built into the wall, not borrowed from a meal."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-e03",
        "band": "easier",
        "text": "Three levels of folding are switched on at the bench. Which "
                "level gives the biggest single gain in surface area?",
        "options": [
            {"text": "Villi — they multiply the area by five.", "correct": True},
            {"text": "Circular folds — they multiply the area by three.",
             "correct": False,
             "why": "The folds are the first level and the only one visible "
                    "without a lens, but ×3 is the smallest of the three "
                    "factors."},
            {"text": "Microvilli — they multiply the area by four.",
             "correct": False,
             "why": "Microvilli are the smallest structures, not the biggest "
                    "gain. Leaving them out costs less area than leaving out "
                    "the villi."},
            {"text": "All three levels give exactly the same gain.",
             "correct": False,
             "why": "The three factors are different: ×3, ×5 and ×4. Switch "
                    "the villi off and you lose more than switching off "
                    "either of the others."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-e04",
        "band": "easier",
        "text": "At the bench the absorbing surface climbs from 0.5 m² to "
                "30 m² as you switch the three levels on. What happens to the "
                "length of the tube while you do it?",
        "options": [
            {"text": "It grows to about sixty metres.", "correct": False,
             "why": "Sixty is how many times the area has grown, not a new "
                    "length. The area changed; the length did not."},
            {"text": "It grows a little, because each villus is about 1 mm "
                     "long.", "correct": False,
             "why": "Villi project inwards, into space the tube already has. "
                    "They add surface without adding a millimetre of length."},
            {"text": "It gets shorter, because folding a tube shortens it.",
             "correct": False,
             "why": "The circular folds run round the tube, not along it. "
                    "Nothing in this lesson moves the six metres."},
            {"text": "It stays at six metres the whole way through.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-07-s01",
        "band": "standard",
        "text": "Imagine a small intestine with all three levels of folding "
                "intact, but a wall ten cells thick instead of one. What "
                "happens to absorption?",
        "options": [
            {"text": "It runs at about a tenth of the rate — ten times the "
                     "distance.", "correct": True},
            {"text": "It is unchanged, because surface area is what decides "
                     "the rate.", "correct": False,
             "why": "Area is one of four features, not the whole story. "
                    "Making every molecule travel ten times further slows "
                    "every crossing, however much surface there is."},
            {"text": "It stops completely, because nothing gets through ten "
                     "cells.", "correct": False,
             "why": "Diffusion does not switch off at a distance, it slows "
                    "down. Molecules still cross a thick wall, just far more "
                    "slowly."},
            {"text": "It speeds up, because a thicker wall holds more "
                     "molecules.", "correct": False,
             "why": "A thicker wall is a longer journey, not a bigger store. "
                    "The one-cell wall is the shortest diffusion path the "
                    "body can build."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-s02",
        "band": "standard",
        "text": "Just after a meal there is far more glucose in the gut than "
                "in the blood. Why does glucose end up crossing into the "
                "blood rather than out of it?",
        "options": [
            {"text": "The wall of a villus only lets glucose through one way.",
             "correct": False,
             "why": "There is no valve in the wall. Molecules cross both ways "
                    "all the time — more happen to go inwards only because "
                    "there are more of them on the gut side."},
            {"text": "The muscles of the gut wall push the glucose across it.",
             "correct": False,
             "why": "Peristalsis moves food along the tube, never through the "
                    "wall. Nothing pushes a glucose molecule anywhere."},
            {"text": "Random movement, with more on the gut side, sends more "
                     "inwards.", "correct": True},
            {"text": "Glucose molecules want to spread out until the two sides "
                     "are even.", "correct": False,
             "why": "Nothing wants anything. Molecules have no aim; the net "
                    "movement falls out of random motion plus a difference in "
                    "numbers."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-s03",
        "band": "standard",
        "text": "A student writes: “Peristalsis squeezes the food hard enough "
                "to force it through the gut wall and into the blood.” What "
                "is wrong with that sentence?",
        "options": [
            {"text": "Nothing at all — that is exactly how food gets into the "
                     "blood.", "correct": False,
             "why": "It is the commonest wrong idea about the gut. Muscle "
                    "moves food along the tube; it never moves anything "
                    "through the wall."},
            {"text": "Peristalsis moves food along the tube; molecules cross "
                     "by diffusion.", "correct": True},
            {"text": "Only the route — the muscles force the food through the "
                     "villi instead.", "correct": False,
             "why": "Changing the route does not repair it. Nothing is forced "
                    "through anything: the crossing is diffusion, driven by a "
                    "difference in concentration."},
            {"text": "Peristalsis happens in the stomach, so it cannot be "
                     "acting here.", "correct": False,
             "why": "Peristalsis happens all along the gut, small intestine "
                    "included. The error is in what it does, not in where it "
                    "happens."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-s04",
        "band": "standard",
        "text": "Under a hand lens, the lining of the small intestine looks "
                "like velvet. What are you looking at?",
        "options": [
            {"text": "The circular folds.", "correct": False,
             "why": "The folds are ridges a few millimetres deep and you can "
                    "see them with no lens at all. Velvet is the level below "
                    "them."},
            {"text": "The microvilli.", "correct": False,
             "why": "Microvilli are about 0.001 mm — far too small for a hand "
                    "lens. Seeing those needs an electron microscope."},
            {"text": "The villi.", "correct": True},
            {"text": "The capillary networks.", "correct": False,
             "why": "The capillaries run inside the villi rather than over "
                    "the surface. What gives the velvet look is the "
                    "projections themselves."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-07-h01",
        "band": "harder",
        "text": "The three levels multiply the plain tube’s area by 3, then 5, "
                "then 4 — and the finished surface is sixty times the plain "
                "tube. Where does sixty come from?",
        "options": [
            {"text": "From adding the three factors: 3 + 5 + 4.",
             "correct": False,
             "why": "Adding gives twelve, not sixty. Each level folds a "
                    "surface that has already been folded, so the factors "
                    "multiply rather than add."},
            {"text": "From multiplying the three factors: 3 × 5 × 4.",
             "correct": True},
            {"text": "From the six metres of length, multiplied by ten.",
             "correct": False,
             "why": "Length takes no part in it. The tube is six metres "
                    "before and after, and every gain comes from folding "
                    "alone."},
            {"text": "From the largest factor, five, applied at each level.",
             "correct": False,
             "why": "Each level acts on the surface the level before it made, "
                    "so all three factors count once each — not the biggest "
                    "one three times."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-h02",
        "band": "harder",
        "text": "An earthworm has no lungs — oxygen diffuses straight through "
                "its skin, which it keeps moist. On hot dry paving a worm "
                "dies within minutes, surrounded by air holding far more "
                "oxygen than soil does. Which feature has it lost?",
        "options": [
            {"text": "The moist surface — oxygen must dissolve before "
                     "crossing.", "correct": True},
            {"text": "The large surface area — its skin shrinks as it dries "
                     "out.", "correct": False,
             "why": "Drying does not take the skin away. It takes away the "
                    "film of water, and without that nothing dissolves and "
                    "nothing crosses."},
            {"text": "The thin surface — dried skin becomes many cells "
                     "thick.", "correct": False,
             "why": "The skin is no thicker than it was a minute earlier. "
                    "What changed is that it is dry, and a dry surface "
                    "absorbs nothing at all."},
            {"text": "None of them — a worm can only use oxygen from water.",
             "correct": False,
             "why": "Air holds far more oxygen than water does. The problem "
                    "is not the air; it is that the worm’s surface is no "
                    "longer wet enough to dissolve it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-h03",
        "band": "harder",
        "text": "Two model guts. Gut A has 30 m² of surface and a wall ten "
                "cells thick. Gut B has 3 m² of surface and a wall one cell "
                "thick. Which absorbs faster?",
        "options": [
            {"text": "Gut A, because a large surface area matters more than "
                     "anything else.", "correct": False,
             "why": "Area is one of four features, not the deciding one. Gut "
                    "A has ten times the surface, but every crossing takes "
                    "ten times as long, and the two cancel."},
            {"text": "Gut B, because a thin wall always beats a large surface "
                     "area.", "correct": False,
             "why": "Neither always beats the other. Here ten times the area "
                    "and ten times the distance happen to cancel; change "
                    "either number and the answer changes."},
            {"text": "Gut A, because 30 m² is ten times as much surface as "
                     "3 m².", "correct": False,
             "why": "That is half the comparison. The ten times more surface "
                    "is exactly undone by a wall that is ten times thicker."},
            {"text": "About the same — ten times the area, each crossing a "
                     "tenth as fast.", "correct": True},
        ],
        "figure": None,
    },
    # ⊕ MRB-233 (3c), 31 Aug 2026 — THE TEXTBOOK HEDGE IS OUT OF THIS QUESTION.
    # It used to open "A textbook in the school library gives the small
    # intestine's surface area as 200 m². This lesson gives about 30 m². What
    # is the best thing to write in an exam?", with distractors arguing from
    # how often a number is printed and from which figure is newer. Mide's
    # ruling removes the hedge from the estate: the page teaches ONE figure and
    # does not brief a KS3 student on which books disagree.
    # ⚠️ THE TEACHING SURVIVES INTACT, and that is why this is a rewrite rather
    # than a deletion. The old question's real target was giving a NUMBER where
    # an explanation was wanted, and its correct option was already the
    # principle. The stem now reaches that target directly, and option 1 keeps
    # the number-worship distractor without naming a book.
    {
        "id": "b3-07-h04",
        "band": "harder",
        "text": "An exam question asks why the small intestine is well "
                "adapted for absorbing digested food. Which answer would earn "
                "the most credit?",
        "options": [
            {"text": "It has a very large surface area, which is what "
                     "absorption needs.",
             "correct": False,
             "why": "True, and it is the start of the answer rather than the "
                    "whole of it. An examiner wants to know what MAKES the "
                    "area large — name the folding and you have the mark."},
            {"text": "Its inner surface measures about thirty square metres, "
                     "which is remarkably large for a tube.",
             "correct": False,
             "why": "A figure is not an explanation. Quoting an area says "
                    "nothing about how the intestine achieves it, and a "
                    "question asking WHY is not answered by a number."},
            {"text": "Its wall is folded into villi and microvilli, giving a "
                     "large surface area for diffusion.",
             "correct": True},
            {"text": "It is six metres long, so food spends a long time "
                     "inside it before it finally leaves the small intestine.",
             "correct": False,
             "why": "Length gives time, not area, and it is the error this "
                    "whole lesson is built to break — the hose is six metres "
                    "too, and absorbs almost nothing."},
        ],
        "figure": None,
    },
]
