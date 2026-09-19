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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Six further rows, two per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-07-e05",
        "band": "easier",
        "text": "How thick is the wall of a villus, and what is immediately on "
                "the other side of it?",
        "options": [
            {"text": "One cell thick, with a capillary on the other side.",
             "correct": True},
            {"text": "Ten cells thick, with a capillary on the other side.",
             "correct": False,
             "why": "A wall ten cells thick would absorb about a tenth as "
                    "fast for the same area. A real villus wall is a single "
                    "cell."},
            {"text": "One cell thick, with the large intestine on the other "
                     "side.", "correct": False,
             "why": "On the far side of a villus wall is blood in a "
                    "capillary. The large intestine is further along the same "
                    "tube, not behind the wall."},
            {"text": "Several cells thick, with a layer of muscle behind it.",
             "correct": False,
             "why": "Muscle in the gut wall moves food along the tube. What "
                    "sits behind the absorbing surface is a capillary "
                    "network."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-e06",
        "band": "easier",
        "text": "Four features make a good exchange surface. Which one keeps "
                "the concentration difference going?",
        "options": [
            {"text": "A very large surface area.", "correct": False,
             "why": "Area sets how many molecules can cross at once. It does "
                    "nothing to stop the blood side filling up."},
            {"text": "A wall one cell thick.", "correct": False,
             "why": "A short distance makes each crossing fast. It does not "
                    "keep the two sides unequal."},
            {"text": "A dense blood supply.", "correct": True},
            {"text": "A moist surface.", "correct": False,
             "why": "Molecules can only diffuse through a membrane while "
                    "dissolved in water. That is a condition for crossing, "
                    "not what maintains the difference."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-07-s05",
        "band": "standard",
        "text": "About 30 m² of absorbing surface is packed into a tube six "
                "metres long. Why is folding a better answer than simply "
                "growing a longer intestine?",
        "options": [
            {"text": "Because a longer tube would fill more slowly, so food "
                     "would reach the villi too late.", "correct": False,
             "why": "How long the journey takes is not the problem. The "
                    "problem is where sixty metres of tube would go."},
            {"text": "Sixty times the area would need sixty metres of tube, "
                     "and no body has room for it.", "correct": True},
            {"text": "Because folding also makes the wall thinner, which "
                     "extra length would not do.", "correct": False,
             "why": "Folding changes area, not thickness. The wall being one "
                    "cell thick is a separate feature altogether."},
            {"text": "Because a longer tube would carry fewer villi, so the "
                     "area would not grow anyway.", "correct": False,
             "why": "Length and folding are independent. A longer tube would "
                    "carry more villi — it simply would not fit inside the "
                    "animal."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-s06",
        "band": "standard",
        "text": "A starch molecule in a mouthful of bread has to be digested "
                "before it can be absorbed. Why can those two never happen the "
                "other way round?",
        "options": [
            {"text": "Because absorption happens in the large intestine, "
                     "after all digestion has finished.", "correct": False,
             "why": "Almost all absorption happens in the small intestine, "
                    "alongside the last of the digestion. The order is set by "
                    "molecule size, not by which organ."},
            {"text": "Because the blood would end up digesting the starch, "
                     "which the body cannot allow.", "correct": False,
             "why": "Blood does not digest starch. The real reason is that a "
                    "starch molecule cannot cross the wall in the first "
                    "place."},
            {"text": "Because peristalsis pushes food past the villi before "
                     "the enzymes can reach it.", "correct": False,
             "why": "Peristalsis moves food along the tube and decides "
                    "nothing about what crosses the wall. Nothing pushes "
                    "molecules through it."},
            {"text": "A starch molecule is far too large to cross the wall "
                     "until it is cut to glucose.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-07-h05",
        "band": "harder",
        "text": "A model gut is a length of artificial membrane tubing holding "
                "starch and amylase, standing in a beaker of still water. An "
                "hour later there is glucose in the beaker and no starch. "
                "Which features of a real small intestine does the model have, "
                "and which does it lack?",
        "options": [
            {"text": "It has the folding, but lacks a wall thin enough for "
                     "glucose to cross.", "correct": False,
             "why": "Glucose did cross, so the membrane is thin enough. What "
                    "smooth tubing has no trace of is the folding."},
            {"text": "It has all four features, which is why glucose appears "
                     "in the beaker at all.", "correct": False,
             "why": "The tubing is smooth — no folds, no villi, no "
                    "microvilli — and still water carries nothing away."},
            {"text": "It has a thin membrane only small molecules cross, and "
                     "lacks folding and blood flow.", "correct": True},
            {"text": "It has the blood supply, because the beaker water "
                     "carries glucose away as fast as it arrives.",
             "correct": False,
             "why": "The water is still, so glucose builds up in it. Blood "
                    "flows past constantly, which is what keeps the "
                    "concentration low on the far side."},
        ],
        "figure": None,
    },
    {
        "id": "b3-07-h06",
        "band": "harder",
        "text": "Fish gills are folded into thousands of thin filaments, each "
                "with blood flowing through it, and they sit in water. Which "
                "of the four features is supplied by the fish's surroundings "
                "rather than by its own body?",
        "options": [
            {"text": "The moist surface — the water the fish lives in "
                     "provides it.", "correct": True},
            {"text": "The large surface area — water flowing past spreads the "
                     "filaments out.", "correct": False,
             "why": "The folding into filaments is the fish's own structure, "
                    "exactly as villi are yours. Water does not create the "
                    "area."},
            {"text": "The thin wall — the pressure of the water keeps each "
                     "filament squashed thin.", "correct": False,
             "why": "A filament is thin because it is built that way. Nothing "
                    "outside the fish sets the thickness of its own tissue."},
            {"text": "The dense blood supply — the water carries the blood "
                     "past the filaments.", "correct": False,
             "why": "The fish's own heart moves its blood. What the water "
                    "carries is the oxygen, on the other side of the wall."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ───────────────────────────────────────────
    # 24 further rows per band, e07-e30 / s07-s30 / h07-h30, appended at
    # bank_position 18+ so bank_position 0-17 (the twelve MRB-269 rows plus
    # the six MRB-335 top-up rows) remain untouched.

    {
        "id": 'b3-07-e07',
        "band": 'easier',
        "text": 'What is a villus?',
        "options": [
            {"text": 'One of the millions of finger-shaped '
                     'projections that line the small intestine, each '
                     'with capillaries inside it.', "correct": True},
            {"text": 'A fold in the outer wall of the small '
                     'intestine, visible without magnification.', "correct": False,
             "why": 'That describes a circular fold, the first and '
                    'largest-scale level of folding. A villus is the '
                    'finer, finger-shaped structure sitting on top of '
                    'the folds.'},
            {"text": 'A single tiny projection on the surface of one '
                     'cell, needing an electron microscope to see.', "correct": False,
             "why": 'That describes a microvillus, the smallest of '
                    'the three scales. A villus is far bigger, '
                    'visible with just a hand lens, and is covered in '
                    'thousands of microvilli.'},
            {"text": 'A muscle in the gut wall that squeezes food '
                     'along the tube.', "correct": False,
             "why": 'Muscle doing that job is peristalsis, and it has '
                    "nothing to do with the wall's folding. A villus "
                    'is a finger-shaped projection, not a muscle.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e08',
        "band": 'easier',
        "text": 'What are microvilli?',
        "options": [
            {"text": 'The finger-shaped projections, about a '
                     'millimetre long, that give the small intestine '
                     'wall its velvet appearance.', "correct": False,
             "why": 'That describes villi, the middle scale of '
                    'folding, visible with a hand lens. Microvilli '
                    'are the smaller structures sitting on top of '
                    'them.'},
            {"text": 'The hundreds of tiny projections on the outer '
                     'surface of each cell covering a villus.', "correct": True},
            {"text": 'The ridges that throw the whole gut wall into '
                     'folds, visible without any microscope.', "correct": False,
             "why": 'Those are circular folds, the first and '
                    'largest-scale level. Microvilli are the smallest '
                    'of the three, invisible without an electron '
                    'microscope.'},
            {"text": 'The capillaries running through the middle of a '
                     'villus, carrying blood.', "correct": False,
             "why": 'Capillaries are blood vessels, not projections '
                    'on a cell surface. Microvilli are structural, on '
                    "the outside of a villus's cells."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e09',
        "band": 'easier',
        "text": "What does 'surface area' mean here, and what does "
                'folding do to it?',
        "options": [
            {"text": 'The total volume enclosed by a surface; folding '
                     'shrinks the volume without changing the area.', "correct": False,
             "why": 'Surface area is not volume, it is the total area '
                    'of the surface itself. Folding also does not '
                    'reliably shrink volume; that is not what this '
                    "lesson's bench measures."},
            {"text": 'The total length of a surface; folding '
                     'increases the length without changing the area.', "correct": False,
             "why": 'Length and area are different measurements. '
                    'Folding in this lesson leaves the six-metre '
                    'length exactly where it was and changes the area '
                    'instead.'},
            {"text": 'The total area of a surface; folding increases '
                     'it without changing the length or width.', "correct": True},
            {"text": 'The total weight a surface can hold; folding '
                     'makes it stronger without changing its size.', "correct": False,
             "why": 'Surface area has nothing to do with strength or '
                    'weight. What folding changes is how much surface '
                    'is packed into the same length and width.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e10',
        "band": 'easier',
        "text": 'Why does it matter that the wall of a villus is one '
                'cell thick?',
        "options": [
            {"text": 'It lets the wall stretch further when a meal '
                     'arrives.', "correct": False,
             "why": 'The wall being thin has nothing to do with '
                    'stretching. What a thin wall changes is the '
                    'distance a molecule has to cross.'},
            {"text": 'It stops any bacteria getting through the wall.', "correct": False,
             "why": 'A thin wall is not a filter against bacteria, '
                    'its whole point is to let small molecules cross '
                    'easily. Keeping bacteria out is not what this '
                    'feature does.'},
            {"text": 'It makes the wall stronger, so it can withstand '
                     'the muscle squeezing food past it.', "correct": False,
             "why": 'A single cell is not a stronger structure than '
                    'several. What a thin wall gives is a short path, '
                    'not strength.'},
            {"text": 'It gives molecules the shortest possible '
                     'distance to diffuse across, so each crossing '
                     'happens fast.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e11',
        "band": 'easier',
        "text": 'Once digestion is complete, which of these is a '
                'small, soluble molecule that can cross the villus '
                'wall into the blood?',
        "options": [
            {"text": 'Glucose.', "correct": True},
            {"text": 'Starch.', "correct": False,
             "why": 'Starch is a large molecule and cannot cross the '
                    'wall. It has to be digested into glucose first.'},
            {"text": 'Protein.', "correct": False,
             "why": 'Whole protein molecules are far too large to '
                    'cross. Protein must be digested into amino acids '
                    'before it can be absorbed.'},
            {"text": 'Fat, as large fat droplets.', "correct": False,
             "why": 'Fat droplets are not soluble enough to cross the '
                    'wall as they are. They must be broken down '
                    'first, into fatty acids and glycerol.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e12',
        "band": 'easier',
        "text": 'Once a glucose molecule has diffused into a '
                'capillary inside a villus, what happens to it next?',
        "options": [
            {"text": 'It stays inside the villus, stored for later '
                     'use.', "correct": False,
             "why": 'Nothing is stored inside a villus. The capillary '
                    'network exists to carry absorbed molecules away, '
                    'not to hold them.'},
            {"text": 'It is carried away in the bloodstream, towards '
                     'the rest of the body.', "correct": True},
            {"text": 'It diffuses straight back out into the gut once '
                     'the concentrations are equal.', "correct": False,
             "why": 'The blood keeps flowing, carrying glucose away '
                    'as fast as it arrives, so the gut side stays '
                    'higher and the net movement stays inward.'},
            {"text": 'It is broken down, into carbon dioxide and '
                     'water, by the villus wall that absorbed it.', "correct": False,
             "why": 'That breakdown, respiration, happens inside body '
                    'cells generally, not inside the wall of a '
                    "villus. The villus's job is absorption, not "
                    'respiration.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e13',
        "band": 'easier',
        "text": 'Besides small soluble food molecules, what else does '
                'this lesson say is absorbed by the small intestine, '
                'and again by the large intestine?',
        "options": [
            {"text": 'Vitamin K.', "correct": False,
             "why": 'Vitamin K is made by bacteria in the large '
                    'intestine, not absorbed as a raw material '
                    'passing through in food.'},
            {"text": 'Fibre.', "correct": False,
             "why": 'Fibre is what is not absorbed, it passes through '
                    'undigested. It is water that both intestines '
                    'absorb.'},
            {"text": 'Water.', "correct": True},
            {"text": 'Oxygen.', "correct": False,
             "why": 'Oxygen is absorbed in the lungs, not the gut. '
                    'Nothing in this lesson describes the intestines '
                    'taking in oxygen.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e14',
        "band": 'easier',
        "text": 'Three of these are genuine features of a good exchange '
                'surface. Which one is not?',
        "options": [
            {"text": 'A very large surface area.', "correct": False,
             "why": 'That is Feature 1, one of the genuine four.'},
            {"text": 'A wall one cell thick.', "correct": False,
             "why": 'That is Feature 2, one of the genuine four.'},
            {"text": 'A dense blood supply.', "correct": False,
             "why": 'That is Feature 3, one of the genuine four.'},
            {"text": 'A muscular wall that pushes food along it.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e15',
        "band": 'easier',
        "text": 'According to this lesson, roughly what does the '
                'finished absorbing surface, about 30 m², compare to '
                'in size?',
        "options": [
            {"text": 'About a third of a badminton court.', "correct": True},
            {"text": 'A full-size tennis court.', "correct": False,
             "why": 'A tennis court is far bigger, over 200 m². That '
                    "was the older, since-corrected figure's "
                    "comparison, not this lesson's."},
            {"text": 'The floor of a small bedroom.', "correct": False,
             "why": 'A small UK bedroom is only 7 to 10 m², much '
                    "smaller than 30 m². This lesson's comparison is "
                    'a badminton court, not a bedroom.'},
            {"text": 'A football pitch.', "correct": False,
             "why": 'A football pitch measures thousands of square '
                    'metres, far too big. Thirty square metres is a '
                    'much smaller comparison.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e16',
        "band": 'easier',
        "text": 'Before any folding at all, the plain tube has about '
                '0.5 m² of inner surface. What does this lesson '
                'compare that to?',
        "options": [
            {"text": 'A bath towel.', "correct": False,
             "why": 'A bath towel is considerably bigger than half a '
                    "square metre. This lesson's comparison is a "
                    'smaller item, a tea towel.'},
            {"text": 'A tea towel.', "correct": True},
            {"text": 'A postage stamp.', "correct": False,
             "why": 'A postage stamp measures a few square '
                    'centimetres, nowhere near half a square metre. '
                    'That comparison is far too small.'},
            {"text": 'A dinner plate.', "correct": False,
             "why": 'A dinner plate has an area of only a few hundred '
                    'square centimetres, well under half a square '
                    'metre.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e17',
        "band": 'easier',
        "text": 'Diffusion moves small soluble molecules from an area '
                'of ___ concentration to an area of ___ '
                'concentration.',
        "options": [
            {"text": 'low; high', "correct": False,
             "why": 'That is the wrong way round. Diffusion moves '
                    'molecules from where there are more of them to '
                    'where there are fewer, not the reverse.'},
            {"text": 'high; high', "correct": False,
             "why": 'If both areas had the same concentration there '
                    'would be no net movement. Diffusion needs a '
                    'difference between the two sides.'},
            {"text": 'high; low', "correct": True},
            {"text": 'low; low', "correct": False,
             "why": 'With low concentration on both sides there is '
                    'nothing to drive a net movement. A difference is '
                    'exactly what diffusion needs.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e18',
        "band": 'easier',
        "text": 'Which of these needs an electron microscope to see, '
                'rather than just a hand lens?',
        "options": [
            {"text": 'Circular folds.', "correct": False,
             "why": 'Circular folds are the biggest of the three '
                    'structures, visible to the naked eye, with no '
                    'instrument needed.'},
            {"text": 'The whole small intestine.', "correct": False,
             "why": 'The small intestine as an organ is visible with '
                    'the naked eye. It needs no microscope of any '
                    'kind.'},
            {"text": 'Villi.', "correct": False,
             "why": 'Villi are visible with just a hand lens, giving '
                    'the wall its velvet look. They do not need an '
                    'electron microscope.'},
            {"text": 'Microvilli.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e19',
        "band": 'easier',
        "text": 'Roughly how long is a single villus?',
        "options": [
            {"text": 'About 1 mm.', "correct": True},
            {"text": 'About 1 cm long.', "correct": False,
             "why": 'A centimetre would be ten times too long. A '
                    'villus is roughly a millimetre, visible with a '
                    'hand lens as part of the velvet-looking surface.'},
            {"text": 'About 1 m.', "correct": False,
             "why": 'A whole metre is enormously larger than a '
                    'villus, which is a barely-visible structure a '
                    'fraction of a millimetre to about a millimetre '
                    'long.'},
            {"text": 'About 0.001 mm.', "correct": False,
             "why": 'That figure is the size of a microvillus, not a '
                    'villus. A villus is roughly a thousand times '
                    'bigger.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e20',
        "band": 'easier',
        "text": 'Roughly how large is a single microvillus?',
        "options": [
            {"text": 'About 1 mm.', "correct": False,
             "why": 'That is roughly the size of a villus, a thousand '
                    'times bigger. A microvillus is far smaller.'},
            {"text": 'About 0.001 mm.', "correct": True},
            {"text": 'About 1 cm.', "correct": False,
             "why": 'A centimetre is enormous compared with a '
                    'microvillus, which needs an electron microscope '
                    'just to be seen.'},
            {"text": 'About 10 mm.', "correct": False,
             "why": 'Ten millimetres is a centimetre, visible easily '
                    'to the naked eye. A microvillus is thousands of '
                    'times smaller than that.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e21',
        "band": 'easier',
        "text": 'How deep are the circular folds in the small '
                'intestine wall, and can they be seen without '
                'magnification?',
        "options": [
            {"text": 'About 0.001 mm deep, and an electron microscope '
                     'is needed.', "correct": False,
             "why": 'That is the scale of a microvillus, the smallest '
                    'of the three structures. Circular folds are far '
                    'bigger than that.'},
            {"text": 'About 1 mm deep, and visible only with the help of a hand lens.', "correct": False,
             "why": 'A millimetre and a hand lens describe villi, the '
                    'middle scale. Circular folds are bigger again, '
                    'and visible with no instrument.'},
            {"text": 'A few millimetres deep, and yes, visible to the '
                     'naked eye.', "correct": True},
            {"text": 'Several centimetres deep, and yes, visible to '
                     'the naked eye.', "correct": False,
             "why": 'The folds are real but not that deep, a few '
                    'millimetres, not centimetres. The visibility '
                    'claim is right; the depth is exaggerated.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e22',
        "band": 'easier',
        "text": 'By what factor does the level of circular folds, on '
                "its own, multiply the plain tube's surface area?",
        "options": [
            {"text": '×4.', "correct": False,
             "why": "That is the microvilli level's factor, not the "
                    "folds'. Circular folds multiply the area by "
                    'three.'},
            {"text": '×5.', "correct": False,
             "why": "That is the villi level's factor, the biggest "
                    'single gain. Circular folds multiply the area by '
                    'three.'},
            {"text": '×60.', "correct": False,
             "why": 'Sixty is the combined effect of all three levels '
                    'multiplied together, not the folds acting alone.'},
            {"text": '×3.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e23',
        "band": 'easier',
        "text": 'How many separate levels of folding does the wall of '
                'the small intestine have, according to this lesson?',
        "options": [
            {"text": 'Three.', "correct": True},
            {"text": 'Two.', "correct": False,
             "why": 'Two would miss one of the three named levels, '
                    'folds, villi and microvilli all appear in this '
                    'lesson.'},
            {"text": 'Four.', "correct": False,
             "why": 'Three levels are named: circular folds, villi '
                    'and microvilli. There is no fourth level of '
                    'folding in this lesson.'},
            {"text": 'One.', "correct": False,
             "why": 'A single level could not explain a sixty-fold '
                    'increase in area. Three separate levels, each '
                    'folding the one before, are what does it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e24',
        "band": 'easier',
        "text": 'Circular folds and villi are both switched on, but '
                'not microvilli. What is the absorbing surface area '
                'at this point?',
        "options": [
            {"text": '6 m².', "correct": False,
             "why": 'Six square metres is the figure for folds and '
                    'microvilli switched on with villi left out, a '
                    'different combination from this one.'},
            {"text": '7.5 m².', "correct": True},
            {"text": '10 m².', "correct": False,
             "why": 'Ten square metres is the figure for villi and '
                    'microvilli switched on with folds left out, a '
                    'different combination from this one.'},
            {"text": '30 m².', "correct": False,
             "why": 'Thirty square metres needs all three levels on '
                    'together. With microvilli still off, the area '
                    'has not reached that yet.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e25',
        "band": 'easier',
        "text": 'If villi were the only level of folding present, no '
                'circular folds, no microvilli, what would the '
                'surface area be?',
        "options": [
            {"text": '6 m².', "correct": False,
             "why": 'That figure comes from folds and microvilli '
                    'together, with villi left out, the opposite '
                    'combination.'},
            {"text": '2 m².', "correct": False,
             "why": 'That is the figure for microvilli acting alone. '
                    'Villi acting alone give a bigger single gain '
                    'than microvilli do.'},
            {"text": '2.5 m².', "correct": True},
            {"text": '10 m².', "correct": False,
             "why": 'Ten square metres needs villi and microvilli '
                    'together. Villi acting completely alone give a '
                    'smaller area than that.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e26',
        "band": 'easier',
        "text": 'A single villus is roughly 1 mm long. How does that '
                'compare with the six-metre length of the whole small '
                'intestine?',
        "options": [
            {"text": 'It is thousands of times shorter than the whole '
                     'tube.', "correct": True},
            {"text": 'It is about the same length as the whole tube, '
                     'just coiled up smaller.', "correct": False,
             "why": 'A villus is a tiny projection on the wall, not a '
                    'coiled-up copy of the whole intestine. It is a '
                    'very small fraction of six metres.'},
            {"text": "It is about a tenth of the whole tube's length.", "correct": False,
             "why": 'A tenth of six metres would be sixty '
                    'centimetres, vastly bigger than a '
                    'millimetre-long villus.'},
            {"text": 'It is longer than the whole tube, because there '
                     'are millions of them end to end.', "correct": False,
             "why": 'Adding up millions of villi is not how length '
                    'works here, each one individually is a tiny '
                    'fraction of the six-metre length.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e27',
        "band": 'easier',
        "text": "Folds and villi together multiply the plain tube's "
                'area by ×15 (3×5). Roughly how does that compare '
                'with the full ×60 you get once microvilli are added '
                'too?',
        "options": [
            {"text": 'It reaches a quarter of the full multiplying '
                     'effect.', "correct": True},
            {"text": 'It reaches about three-quarters of the full '
                     'multiplying effect.', "correct": False,
             "why": 'Fifteen is a quarter of sixty, not '
                    'three-quarters. Microvilli still have most of '
                    'their contribution left to add.'},
            {"text": 'It already matches the full multiplying effect, '
                     'so microvilli add nothing further.', "correct": False,
             "why": 'Fifteen is far short of sixty. Adding the ×4 '
                    'from microvilli still has a long way to go.'},
            {"text": 'It overshoots the full multiplying effect, so '
                     'microvilli must reduce it back down.', "correct": False,
             "why": 'Fifteen is smaller than sixty, not larger. '
                    'Microvilli add further multiplication, they do '
                    'not reduce anything.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e28',
        "band": 'easier',
        "text": 'Of the three possible PAIRS of folding levels, folds '
                'with villi, folds with microvilli, or villi with '
                'microvilli, which pair gives the smallest surface '
                'area?',
        "options": [
            {"text": 'Folds with microvilli.', "correct": True},
            {"text": 'Folds with villi.', "correct": False,
             "why": 'That pairing includes villi, the single biggest '
                    'factor, so it beats a pairing that leaves villi '
                    'out.'},
            {"text": 'Villi with microvilli.', "correct": False,
             "why": 'That pairing has both of the two biggest '
                    'factors, so it gives the largest area of the '
                    'three pairs, not the smallest.'},
            {"text": 'All three pairs give exactly the same area.', "correct": False,
             "why": 'The three factors, ×3, ×5 and ×4, are different '
                    'sizes, so leaving out a different one each time '
                    'gives three different areas.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e29',
        "band": 'easier',
        "text": 'Once all three levels of folding are switched on, '
                'roughly how many times greater is the surface area '
                'than the plain, unfolded tube?',
        "options": [
            {"text": 'About ×12.', "correct": False,
             "why": 'Twelve times is what two of the three levels '
                    'give together, not all three combined.'},
            {"text": 'About ×20.', "correct": False,
             "why": 'Twenty times is what two of the three levels '
                    'give together, not all three combined.'},
            {"text": 'About ×60.', "correct": True},
            {"text": 'About ×30.', "correct": False,
             "why": 'Thirty is the finished area in square metres, '
                    'not the multiplying factor. The factor compared '
                    'with the plain tube is sixty.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-e30',
        "band": 'easier',
        "text": 'Which of the three levels of folding can be seen '
                'with the naked eye, needing no lens or microscope at '
                'all?',
        "options": [
            {"text": 'Villi.', "correct": False,
             "why": 'Villi need a hand lens to see clearly, that is '
                    'what gives the surface its velvet look under '
                    'magnification.'},
            {"text": 'Microvilli alone.', "correct": False,
             "why": 'Microvilli are the smallest of the three and '
                    'need an electron microscope, the most powerful '
                    'instrument of the three.'},
            {"text": 'Both villi and microvilli.', "correct": False,
             "why": 'Neither of those needs no instrument, villi need '
                    'a hand lens and microvilli need an electron '
                    'microscope.'},
            {"text": 'Circular folds.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s07',
        "band": 'standard',
        "text": 'Root hair cells in a plant also have a large surface '
                'area for absorbing water and minerals from the soil. '
                'Which of these is true of both a root hair cell and '
                'a villus?',
        "options": [
            {"text": 'Both increase the surface area available for '
                     'absorption.', "correct": True},
            {"text": 'Both are folded at three separate scales, like '
                     'the intestine wall.', "correct": False,
             "why": 'A root hair is a single long extension of one '
                    'cell, not three nested levels of folding. The '
                    'villus is built by stacking multiple folding '
                    'scales.'},
            {"text": 'Both use active transport rather than diffusion '
                     'to take substances in.', "correct": False,
             "why": 'This lesson describes absorption in the villus '
                    'as diffusion, driven by a concentration '
                    'difference, not as active transport.'},
            {"text": 'Both have a network of capillaries running '
                     'through them.', "correct": False,
             "why": 'Capillaries are blood vessels, found in animals. '
                    'A root hair cell is a plant cell and has no '
                    'blood supply of any kind.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s08',
        "band": 'standard',
        "text": "A model doubles a villus wall's thickness, from one "
                'cell to two cells, while everything else about it '
                'stays the same. What happens to the rate of '
                'absorption across it?',
        "options": [
            {"text": 'It roughly doubles.', "correct": False,
             "why": 'A thicker wall means a longer diffusion path, '
                    'which slows crossings down. It does not speed '
                    'them up.'},
            {"text": 'It roughly halves.', "correct": True},
            {"text": 'It stops completely.', "correct": False,
             "why": 'Diffusion does not switch off at a small '
                    'increase in distance, it slows down. Two cells '
                    'is still a very short path.'},
            {"text": 'It is unaffected, since the surface area has '
                     'not changed.', "correct": False,
             "why": 'Area is one of four features. Doubling the '
                    'distance a molecule has to travel slows every '
                    'crossing, whatever the area is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s09',
        "band": 'standard',
        "text": 'A villus keeps its blood supply and its '
                'one-cell-thick wall, but its surface dries out '
                'completely. What happens to absorption there?',
        "options": [
            {"text": 'It continues, because the wall and blood supply '
                     'are still working normally.', "correct": False,
             "why": 'Two of the four features being intact is not '
                    'enough. Molecules can only diffuse through a '
                    'membrane while dissolved in water.'},
            {"text": 'It slows to about half, because drying affects '
                     'some of the molecules but not the rest.', "correct": False,
             "why": 'A dry surface is not a partial effect, nothing '
                    'can dissolve and cross a surface with no water '
                    'on it.'},
            {"text": 'It stops, because molecules can only cross a '
                     'membrane while dissolved in water.', "correct": True},
            {"text": 'It speeds up, because dry surfaces let gases '
                     'and liquids move faster.', "correct": False,
             "why": 'That is not how diffusion across a living '
                    'membrane works. A dry surface stops molecules '
                    'dissolving, and dissolving is required before '
                    'anything can cross.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s10',
        "band": 'standard',
        "text": 'A model gut has its surface area increased by '
                'folding, but its wall stays very thick and its blood '
                'flow stays poor. Absorption barely improves. What '
                'does this suggest?',
        "options": [
            {"text": 'That surface area is the one feature that ever '
                     'matters.', "correct": False,
             "why": 'This result is the opposite of that, area '
                    'increased and absorption barely changed, which '
                    'shows the other features matter too.'},
            {"text": 'That folding a wall reduces its thickness at '
                     'the same time.', "correct": False,
             "why": 'Folding changes area, it does not automatically '
                    'change thickness. In this model, the thick wall '
                    'and poor blood flow are unaffected by the '
                    'folding.'},
            {"text": 'That diffusion does not depend on concentration '
                     'differences.', "correct": False,
             "why": 'This result says nothing about concentration. It '
                    'points at wall thickness and blood flow, not at '
                    'the diffusion mechanism itself.'},
            {"text": 'That area on its own is not enough, a thick '
                     'wall and poor blood flow are still holding '
                     'absorption back.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s11',
        "band": 'standard',
        "text": 'Instead of folding the wall, imagine the small '
                'intestine were simply made much wider, keeping the '
                'same six-metre length. Could this reach 30 m² of '
                'inner surface without any folding?',
        "options": [
            {"text": 'In principle a wider tube has more inner '
                     'surface, but a tube wide enough to reach 30 m² '
                     'unfolded would be far too bulky to fit in the '
                     'body.', "correct": True},
            {"text": 'Yes, easily, width has nothing to do with how '
                     'much room a tube takes up inside the crowded '
                     'space of the abdomen, so a wider tube costs '
                     'nothing extra to fit.', "correct": False,
             "why": 'A far wider tube takes up far more space in the '
                    'abdomen. Folding is the solution precisely '
                    'because it avoids needing that extra bulk.'},
            {"text": "No, width has no effect on a tube's inner "
                     'surface area whatsoever, so making it wider '
                     'could never get any closer to 30 m² of '
                     'absorbing surface.', "correct": False,
             "why": 'A wider tube genuinely does have more inner '
                    'surface for the same length. The real problem is '
                    'that reaching 30 m² this way would need an '
                    'impossibly bulky tube.'},
            {"text": 'Yes, and this is how the small intestine '
                     'achieves its area, by simply being wider than '
                     'most other tube-shaped organs in the body.', "correct": False,
             "why": 'The small intestine achieves its area by folding '
                    'at three scales, not by being unusually wide. '
                    'Its diameter is only about two and a half '
                    'centimetres.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s12',
        "band": 'standard',
        "text": 'With all three levels on, the area is 60 times the '
                'plain tube. If only the villi level were switched '
                'off, folds and microvilli left on, the multiple '
                'drops to ×12. By what factor has the area been '
                'reduced?',
        "options": [
            {"text": 'By a factor of 2.', "correct": False,
             "why": 'Sixty divided by twelve is five, not two. The '
                    'area has fallen by more than that.'},
            {"text": 'By a factor of 5.', "correct": True},
            {"text": 'By a factor of 12.', "correct": False,
             "why": 'Twelve is the new multiple itself, not the '
                    'factor by which it has fallen from sixty.'},
            {"text": 'By a factor of 48.', "correct": False,
             "why": 'Forty-eight is the difference between sixty and '
                    'twelve, not the factor by which one has been '
                    'divided into the other.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s13',
        "band": 'standard',
        "text": 'Could the villus wall be zero cells thick, to make '
                'absorption as fast as possible?',
        "options": [
            {"text": 'Yes, and real villi are extremely close to zero '
                     'cells thick already.', "correct": False,
             "why": 'A wall of zero cells is not a thin wall, it is '
                    'no wall at all, which is not what a real villus '
                    'has.'},
            {"text": 'Yes, thinner is faster with no limit.', "correct": False,
             "why": 'A wall of zero cells thick would not be a '
                    'barrier at all, there would be no living tissue '
                    'there to control what crosses or to stay intact.'},
            {"text": 'No, a living wall of at least one cell is '
                     'needed to control what crosses and to stay '
                     'intact as a structure.', "correct": True},
            {"text": 'No, because a wall must be several cells thick '
                     'to survive digestion.', "correct": False,
             "why": 'Real villus walls are one cell thick and survive '
                    "perfectly well. The reason a wall can't be zero "
                    'cells is structural, not about surviving '
                    'digestion.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s14',
        "band": 'standard',
        "text": 'An exam asks a student to describe how molecules '
                'move from the gut into the blood in the small '
                'intestine. Which answer is scientifically complete?',
        "options": [
            {"text": 'They are pushed through the wall by the muscles '
                     'of the intestine.', "correct": False,
             "why": 'Peristalsis moves food along the tube, not '
                    'through the wall. Nothing pushes molecules '
                    'across.'},
            {"text": 'They spread out because they want to reach a '
                     'lower concentration.', "correct": False,
             "why": 'Molecules have no intentions. Movement happens '
                    'because of random motion plus more molecules on '
                    'one side, not because anything wants anything.'},
            {"text": 'They diffuse because the gut wall actively '
                     'pulls them across, using energy released by the '
                     "wall's own cells in a process similar to active "
                     'transport.', "correct": False,
             "why": 'No pulling or energy-using pump is described in '
                    'this lesson. The movement is diffusion, driven '
                    'by the concentration difference alone.'},
            {"text": 'They diffuse across a moist membrane, from high '
                     'to low concentration, and the blood supply '
                     'keeps that difference going.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s15',
        "band": 'standard',
        "text": 'Alveoli in the lungs are another exchange surface: '
                'many of them, thin-walled, moist and surrounded by '
                'capillaries. Which feature do alveoli clearly share '
                'with a villus?',
        "options": [
            {"text": 'They are present in very large numbers, giving '
                     'a large total surface area.', "correct": True},
            {"text": 'They are folded at three separate scales, '
                     'exactly like the small intestine wall.', "correct": False,
             "why": 'This lesson describes three folding scales '
                    'specific to the gut wall. Alveoli achieve a '
                    'large surface differently, through sheer numbers '
                    'rather than nested folding.'},
            {"text": 'They rely on muscle contractions to push gases '
                     'across their walls and into the blood.', "correct": False,
             "why": 'Nothing pushes gases across the alveolar wall in '
                    'either exchange surface. Both rely on diffusion, '
                    'not muscular pushing.'},
            {"text": 'They contain no blood vessels of their own.', "correct": False,
             "why": 'A dense blood supply is one of the shared '
                    'features, not something either surface lacks. '
                    'Both villi and alveoli are surrounded by '
                    'capillaries.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s16',
        "band": 'standard',
        "text": "If blood flow through the villi's capillaries were "
                'slowed to half its normal rate, but not stopped, '
                'what would you expect?',
        "options": [
            {"text": 'Absorption would stop immediately, exactly as '
                     'if the blood supply had been cut off.', "correct": False,
             "why": 'Slowed blood flow is not the same as no blood '
                    'flow. Some concentration difference would still '
                    'be maintained, just less effectively.'},
            {"text": 'Absorption would slow, because the '
                     'concentration difference would be maintained '
                     'less effectively.', "correct": True},
            {"text": 'Absorption would be unaffected, since any blood '
                     'flow whatsoever is enough.', "correct": False,
             "why": 'The rate of blood flow matters, not just whether '
                    'it exists. Slower flow means molecules build up '
                    'more on the blood side, weakening the gradient.'},
            {"text": 'Absorption would speed up, because '
                     'slower-moving blood holds molecules for longer.', "correct": False,
             "why": 'Holding molecules longer raises the '
                    'concentration on the blood side, which weakens '
                    'rather than strengthens the gradient driving '
                    'diffusion inward.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s17',
        "band": 'standard',
        "text": 'Circular folds and villi are both in place, giving '
                '7.5 m² of surface, and microvilli are then switched '
                'on as well, taking it to the finished 30 m². By how '
                'many square metres does the surface grow when that '
                'last level is added?',
        "options": [
            {"text": '4 m².', "correct": False,
             "why": "Four is the microvilli level's multiplying "
                    'factor, not an area. Multiplying 7.5 m² by four '
                    'gives 30 m², which is a gain of 22.5 m².'},
            {"text": '30 m².', "correct": False,
             "why": 'Thirty square metres is the finished total, not '
                    'the amount added. The surface was already at '
                    '7.5 m² before microvilli were switched on.'},
            {"text": '22.5 m².', "correct": True},
            {"text": '7.5 m².', "correct": False,
             "why": 'Seven and a half square metres is the surface '
                    'before microvilli are added, not the extra area '
                    'they bring.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s18',
        "band": 'standard',
        "text": 'Gut C has 15 m² of surface and a wall one cell '
                'thick. Gut D has the same 15 m² of surface, but a '
                'wall five cells thick. About how many times faster '
                'does Gut C absorb, compared with Gut D?',
        "options": [
            {"text": 'About twice as fast.', "correct": False,
             "why": 'The wall is five times thicker in Gut D, not '
                    'two, so the speed difference should track that.'},
            {"text": 'The same speed, since the area is identical, '
                     'wall thickness makes no difference.', "correct": False,
             "why": 'Area is one of four features. With identical '
                    'area, the five-times-thicker wall in Gut D makes '
                    'every crossing about five times slower.'},
            {"text": 'About ten times faster.', "correct": False,
             "why": 'Ten is double the actual thickness difference. '
                    'The wall in Gut D is five times thicker, not '
                    'ten.'},
            {"text": 'About five times faster.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s19',
        "band": 'standard',
        "text": 'Digested food spends time in the stomach, the small '
                'intestine and the large intestine. Which organ '
                'carries out almost all absorption of small food '
                'molecules, and why?',
        "options": [
            {"text": 'The small intestine, because that is where the '
                     'folded, villus-covered surface is.', "correct": True},
            {"text": 'The stomach, because that is where digestion of '
                     'protein begins and where most of it finishes.', "correct": False,
             "why": 'Beginning digestion is not the same as '
                    "absorbing. The stomach's job is to start "
                    'breaking food down, not to absorb the products.'},
            {"text": 'The large intestine, because that is where the '
                     'largest population of gut bacteria is known to '
                     'live.', "correct": False,
             "why": 'The large intestine mainly absorbs water, plus '
                    'some products of bacterial fermentation. The '
                    'great bulk of nutrient absorption happens '
                    'earlier, in the small intestine.'},
            {"text": 'All three organs absorb an equal share of the '
                     'food molecules.', "correct": False,
             "why": 'The organs are not equal contributors. The small '
                    "intestine's folded, villus-covered wall is built "
                    'specifically for absorption, unlike the other '
                    'two.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s20',
        "band": 'standard',
        "text": 'A student says protein and starch are absorbed '
                'directly into the blood, in the form they arrive in '
                'food. What is the correct picture?',
        "options": [
            {"text": 'They are absorbed directly, and fats alone need '
                     'to be broken down first.', "correct": False,
             "why": 'Protein and starch also cannot cross the wall as '
                    'they are, every one of the three main food types '
                    'must be broken into small, soluble units first.'},
            {"text": 'Protein and starch are digested first, into '
                     'amino acids and glucose, and it is those small '
                     'products that are absorbed.', "correct": True},
            {"text": 'They are absorbed directly, because the villus '
                     'wall lets any size of molecule through it, '
                     'since its job is simply to move food from the '
                     'gut into the blood.', "correct": False,
             "why": 'The wall is a barrier to large molecules. Its '
                    'whole design, one cell thick, allowing only '
                    'small soluble molecules through, depends on that '
                    'not being true.'},
            {"text": 'They are not absorbed in any form whatsoever.', "correct": False,
             "why": 'Their digestion products, glucose and amino '
                    "acids, are absorbed in large quantities. What's "
                    'false is the idea that they cross whole.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s21',
        "band": 'standard',
        "text": 'Microvilli are the smallest of the three structures, '
                'needing an electron microscope to see at all. Why '
                'does switching them off still cost a genuine ×4 of '
                'surface area?',
        "options": [
            {"text": 'Because microvilli are, in size, larger than '
                     'villi, despite appearing smaller under a '
                     'microscope.', "correct": False,
             "why": 'Microvilli really are smaller than villi, about '
                    'a thousand times smaller. Their contribution is '
                    'not about individual size.'},
            {"text": 'Because microvilli replace the villi entirely '
                     'once they are switched on.', "correct": False,
             "why": 'Microvilli sit on top of villi, covering their '
                    "cells' surfaces, they do not replace them. Both "
                    'levels stack together.'},
            {"text": 'Because there are enormous numbers of them, and '
                     'their individual smallness is made up for by '
                     'their sheer number.', "correct": True},
            {"text": 'Because switching on microvilli also '
                     'automatically switches on more villi.', "correct": False,
             "why": 'Each level is independent in this model. '
                    'Switching on microvilli does not add any more '
                    'villi to the surface.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s22',
        "band": 'standard',
        "text": 'A car radiator has thin metal fins to help it lose '
                'heat quickly. Which principle does this share with '
                'the folded wall of the small intestine?',
        "options": [
            {"text": 'Fins work by raising the temperature of the '
                     'surrounding air, not the surface.', "correct": False,
             "why": 'Fins are a passive metal structure, they do not '
                    'heat the air. What they do is add exchange '
                    'surface for the same reason villi do.'},
            {"text": 'Fins work by increasing the thickness of the '
                     'metal, giving a bigger volume of metal that can '
                     "store and then slowly release the radiator's "
                     'heat.', "correct": False,
             "why": 'Fins are usually made as thin as possible, not '
                    'thick. Thickness would slow heat exchange, '
                    'exactly as a thick gut wall would slow '
                    'absorption.'},
            {"text": 'Fins and villi both rely on muscle movement to '
                     'force material across a surface.', "correct": False,
             "why": 'Neither a radiator fin nor a villus is powered '
                    'by muscle. Both work passively, by presenting '
                    'more surface for the exchange to happen across.'},
            {"text": 'Both increase the surface area available, which '
                     'increases the rate at which something can cross '
                     'or transfer.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s23',
        "band": 'standard',
        "text": 'A model doubles the number of villi per square '
                'millimetre of gut wall, without changing anything '
                'else. What would you expect?',
        "options": [
            {"text": 'A roughly proportional increase in total '
                     'surface area, and therefore in absorption rate.', "correct": True},
            {"text": 'No change, because villi number has nothing to '
                     'do with total surface area, the size of each '
                     'individual villus is what decides that.', "correct": False,
             "why": 'More villi packed into the same wall means more '
                    'absorbing surface overall, number and total area '
                    'are directly linked.'},
            {"text": 'A decrease in absorption, because crowded villi '
                     'block each other.', "correct": False,
             "why": "This lesson's whole argument is that adding more "
                    'folding structures increases area and '
                    'absorption. Doubling their number is not '
                    'described as reducing anything.'},
            {"text": 'The wall would automatically become thicker to '
                     'compensate.', "correct": False,
             "why": 'Thickness and the number of villi are separate '
                    'features. Adding more villi does not change how '
                    'many cells thick the wall is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s24',
        "band": 'standard',
        "text": "One person's small intestine has a normal density of "
                "villi. Another person's has, for an unrelated "
                'reason, only half the normal density, though '
                'otherwise a normal wall and blood supply. What would '
                'you expect for the second person?',
        "options": [
            {"text": 'No difference, since villi density does not affect '
                     'the rate at which a gut absorbs.', "correct": False,
             "why": 'Villi are the single biggest contributor to '
                    'surface area. Halving how many there are should '
                    'measurably reduce the absorbing surface and the '
                    'rate.'},
            {"text": 'A meaningfully lower rate of absorption, '
                     'roughly tracking the lost surface area.', "correct": True},
            {"text": 'A higher rate of absorption, because the '
                     'remaining villi would grow bigger to make up '
                     'the shortfall.', "correct": False,
             "why": 'There is no mechanism in this lesson by which '
                    'fewer villi work individually faster. Losing '
                    'surface area lowers the total rate.'},
            {"text": 'Complete failure to absorb anything whatsoever.', "correct": False,
             "why": 'Halving villi density lowers absorption, it does '
                    'not remove the other three features entirely. '
                    'Some folding, wall thinness and blood supply '
                    'remain intact.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s25',
        "band": 'standard',
        "text": 'A comparison between a hose and the small intestine '
                'keeps the length and the width the same for both. Why '
                'does that matter for the comparison to make its point?',
        "options": [
            {"text": "It doesn't matter, any lengths and widths would "
                     'show the same thing.', "correct": False,
             "why": 'If the hose and gut differed in length or width '
                    'as well as folding, a difference in surface area '
                    'could just be due to size, not folding.'},
            {"text": 'It matters because a wider hose would '
                     'automatically fold itself.', "correct": False,
             "why": 'Width does not cause folding to happen. Keeping '
                    'width fixed is about ruling out a size '
                    'difference as the explanation.'},
            {"text": 'It isolates folding as the one variable '
                     'responsible for the huge difference in surface '
                     'area, since size is kept the same.', "correct": True},
            {"text": 'It matters because hoses are usually much '
                     'longer than a small intestine.', "correct": False,
             "why": 'The comparison specifically keeps the length '
                    'equal at six metres. The point is not that hoses '
                    "are usually longer, it's controlling for size."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s26',
        "band": 'standard',
        "text": 'Why is a garden hose a useful thing to compare the '
                "small intestine to, for this lesson's point about "
                'surface area?',
        "options": [
            {"text": 'Because a hose is also found inside the human '
                     'body.', "correct": False,
             "why": 'A hose is not a body structure. It is useful '
                    'precisely because it is a plain, unfolded, '
                    'everyday tube, a simple baseline for comparison.'},
            {"text": 'Because a hose is exactly the same width as the '
                     'small intestine, and matching widths is what '
                     'makes any two tubes a fair comparison for this '
                     'purpose.', "correct": False,
             "why": 'Being a similar width helps make it a fair '
                    'comparison, but it is not the reason a hose is '
                    'chosen, its plain, unfolded surface is.'},
            {"text": 'Because hoses are made of the same material as '
                     'the gut wall.', "correct": False,
             "why": 'Material is irrelevant to a comparison about '
                    'surface area and folding. Nothing here claims '
                    'the two are made of similar material.'},
            {"text": 'Because it is a plain, unfolded tube of a '
                     'similar length and width, giving a fair '
                     'baseline with none of the folding the gut has.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s27',
        "band": 'standard',
        "text": "The stomach's wall is not folded into villi the way "
                "the small intestine's is. Based on this lesson, why "
                'would that make sense?',
        "options": [
            {"text": 'Villi are for absorbing digested food, and the '
                     "stomach's main job is digesting, not yet "
                     'absorbing, so it has less need for that '
                     'structure.', "correct": True},
            {"text": 'Because stomach acid would dissolve any villi '
                     'that grew there.', "correct": False,
             "why": "This lesson gives no such reason, and it isn't "
                    'the explanation offered, the point here is about '
                    'role, digesting versus absorbing.'},
            {"text": 'Because the stomach is too small to fit villi '
                     'inside it.', "correct": False,
             "why": 'Size is not the limiting factor here, villi are '
                    'microscopic structures that could fit on any '
                    "organ's lining. The reason is about the organ's "
                    'job.'},
            {"text": 'Because villi form in organs that are exactly '
                     'six metres long, and organ length is what '
                     'decides whether a lining can grow them in the '
                     'first place.', "correct": False,
             "why": 'Length has nothing to do with whether an organ '
                    "grows villi. The small intestine's length is "
                    'unrelated to why it has them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s28',
        "band": 'standard',
        "text": 'To test whether folding increases absorption rate, '
                'which pair of model guts would make a fair '
                'comparison?',
        "options": [
            {"text": 'One folded and thin-walled versus one unfolded '
                     'and thick-walled, then compare their absorption '
                     'rates directly.', "correct": False,
             "why": 'Changing two things at once, folding and wall '
                    'thickness, means you cannot tell which '
                    'difference caused any change in absorption rate.'},
            {"text": 'One folded and one unfolded, with the wall '
                     'thickness and blood flow kept the same in both.', "correct": True},
            {"text": 'One with a blood supply and one without, both '
                     'left unfolded.', "correct": False,
             "why": 'That tests the effect of blood supply, not '
                    'folding, it changes the wrong variable to answer '
                    'this question.'},
            {"text": 'One long and one short, both left unfolded.', "correct": False,
             "why": 'That tests length, which this lesson does not '
                    'link to surface area. It provides no information '
                    'about folding.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s29',
        "band": 'standard',
        "text": 'The three folding factors are applied as ×3, then '
                '×5, then ×4. If you multiplied them in a different '
                'order, say ×5, then ×4, then ×3, would the final '
                'total be different?',
        "options": [
            {"text": 'Yes, multiplying in a different order gives a '
                     'different answer every time.', "correct": False,
             "why": 'Multiplication gives the same result whatever '
                    'order the factors are multiplied in. Both orders '
                    'give sixty.'},
            {"text": 'No, multiplying the same three numbers together '
                     "gives the same answer whatever order they're "
                     'done in.', "correct": True},
            {"text": 'Yes, because biological structures must be '
                     'built in size order, largest first.', "correct": False,
             "why": 'This is a question about arithmetic, not '
                    'construction order. However you group or order a '
                    'multiplication, the three factors combine to '
                    'sixty.'},
            {"text": 'It depends which level is switched on first in '
                     'a real gut.', "correct": False,
             "why": 'The final multiplied total does not depend on '
                    'order, three numbers multiplied together give '
                    'the same product regardless of the sequence.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-s30',
        "band": 'standard',
        "text": 'Instead of folding, imagine evolution had produced a '
                'plain, unfolded gut sixty metres long to reach the '
                'same 30 m² of surface. What is the most likely '
                'problem with that design?',
        "options": [
            {"text": 'It would have far too little surface area to be '
                     'useful.', "correct": False,
             "why": 'A sixty-metre plain tube of the same width as '
                    'the real intestine would actually have close to '
                    'the right surface area, the issue is not too '
                    'little area.'},
            {"text": 'Digestion would happen far too quickly for '
                     'enzymes to work.', "correct": False,
             "why": 'This lesson gives no reason to think length '
                    'would speed digestion up. The problem with a '
                    'sixty-metre gut is a practical one of size.'},
            {"text": 'Diffusion would stop working entirely over such '
                     'a long tube, since molecules cannot travel that '
                     'far through a body by random movement.', "correct": False,
             "why": 'Diffusion still works the same way locally at '
                    'any point along a tube, length along the tube '
                    'does not change how molecules cross the wall at '
                    'a given point.'},
            {"text": 'It would need a body large enough to contain '
                     'sixty metres of tube, which is not a realistic '
                     'size for a human.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h07',
        "band": 'harder',
        "text": 'A model gut is changed in two ways at once: its '
                'surface area is reduced right back to the plain, '
                'unfolded 0.5 m² tube, a ×60 loss, and its wall is '
                'thickened from one cell to ten cells, a further ×10 '
                'slowdown. Blood supply and moisture stay normal. '
                'Roughly how much slower is absorption compared with '
                'a healthy villus?',
        "options": [
            {"text": 'About 600 times slower.', "correct": True},
            {"text": 'About 70 times slower.', "correct": False,
             "why": 'That would be the two factors added together, '
                    'but the two effects combine by multiplying, not '
                    'adding, because each slows every crossing '
                    'independently.'},
            {"text": 'About 60 times slower.', "correct": False,
             "why": 'That is the area loss alone. The wall being ten '
                    'times thicker adds a further slowdown on top of '
                    'it.'},
            {"text": 'About 10 times slower.', "correct": False,
             "why": 'That is the wall-thickness effect alone. Losing '
                    'sixty-fold worth of surface area on top of it '
                    'makes the true combined effect far larger.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h08',
        "band": 'harder',
        "text": 'The hose-and-gut comparison shows the size of the '
                'effect, sixty times the surface, same length and '
                'width. Which further evidence about the folding '
                'mechanism is needed to show why that happens?',
        "options": [
            {"text": 'None, the size of the difference is evidence '
                     'enough of the mechanism.', "correct": False,
             "why": "A big number on its own doesn't explain how it "
                    "arises. The fold-builder's stepwise breakdown is "
                    'what supplies the mechanism.'},
            {"text": 'The stepwise breakdown into three folding '
                     'levels, each multiplying the area achieved by '
                     'the level before it.', "correct": True},
            {"text": 'A measurement of how fast the hose transports '
                     'water compared with the gut, since flow speed '
                     'is what usually explains a difference between '
                     'two tubes.', "correct": False,
             "why": 'Flow speed through a hose has nothing to do with '
                    'explaining a difference in inner surface area. '
                    'The explanation needed is structural, not about '
                    'flow rate.'},
            {"text": 'Proof that the hose and the intestine are made '
                     'of different materials.', "correct": False,
             "why": 'Material is irrelevant to why one has more '
                    'surface than the other. What explains the '
                    'difference is the folding, not what either is '
                    'made of.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h09',
        "band": 'harder',
        "text": 'Villi give the single biggest factor, ×5. Yet '
                'removing the smallest factor, the circular folds at '
                '×3, from a fully folded gut does not just lose a ×3, '
                'it loses far more than that. Why?',
        "options": [
            {"text": "Because the folds' factor is applied twice in "
                     'the real gut, not once.', "correct": False,
             "why": "Each level's factor, including the folds', is "
                    'applied exactly once in this model. Nothing '
                    'doubles it.'},
            {"text": 'Because circular folds are, in reality, the '
                     'largest structure, and this lesson understates '
                     'their size.', "correct": False,
             "why": 'The folds genuinely are the biggest single '
                    'physical structure, visible without a '
                    'microscope, but that is not why removing them '
                    'costs more than ×3.'},
            {"text": 'Because villi and microvilli are folded on top '
                     'of the circular folds, remove the base level '
                     'and everything built on it goes too.', "correct": True},
            {"text": 'Because removing any level drops the total area '
                     "straight back to the plain tube's 0.5 m², every "
                     'time.', "correct": False,
             "why": 'Removing only the folds still leaves villi and '
                    'microvilli acting on what remains, the area does '
                    'not fall all the way back to the unfolded 0.5 m² '
                    'baseline.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h10',
        "band": 'harder',
        "text": 'Gut E has 3 m² of surface and a wall one cell thick. '
                'Gut F has 30 m² of surface and a wall three cells '
                'thick. Which absorbs faster, and roughly by what '
                'factor?',
        "options": [
            {"text": 'Gut E, about 3 times faster, since its thinner '
                     'wall matters more for the rate than any '
                     'advantage from a larger surface area.', "correct": False,
             "why": "Gut F's ten-times-greater area outweighs its "
                    'three-times-thicker wall. Gut F is the faster of '
                    'the two.'},
            {"text": 'They absorb at the same rate, since the two '
                     'differences cancel exactly.', "correct": False,
             "why": 'Ten times the area against three times the '
                    'thickness does not cancel exactly, ten divided '
                    'by three leaves Gut F still faster overall.'},
            {"text": 'Gut F, about 30 times faster, using the area '
                     'figures alone.', "correct": False,
             "why": 'That ignores the wall-thickness penalty '
                    "entirely. Gut F's wall is three times thicker, "
                    'which cuts into its area advantage.'},
            {"text": 'Gut F, roughly 3 to 4 times faster, once the '
                     'tenfold area gain is set against the threefold '
                     'thickness penalty.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h11',
        "band": 'harder',
        "text": 'An exam asks why a one-cell-thick wall helps '
                'absorption. Which answer would earn the most credit?',
        "options": [
            {"text": 'Because a one-cell wall gives molecules the '
                     'shortest possible distance to diffuse across, '
                     'making each crossing fast.', "correct": True},
            {"text": 'Because one cell is a very small, precise unit '
                     'of measurement.', "correct": False,
             "why": "This treats 'one cell' as a unit of measurement "
                    'rather than an explanation. It says nothing '
                    'about diffusion distance or speed.'},
            {"text": 'Because thin walls are a feature of small '
                     'intestines specifically, found in no other '
                     'organ or exchange surface anywhere in the body.', "correct": False,
             "why": 'This is untrue, other exchange surfaces such as '
                    'alveoli are also thin-walled, and it does not '
                    'explain why thinness itself helps.'},
            {"text": 'Because a thinner wall lets more blood flow '
                     'through the villus.', "correct": False,
             "why": 'Wall thickness and blood flow are two separate '
                    'features. A thin wall shortens the diffusion '
                    'path, it does not, by itself, increase how much '
                    'blood arrives.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h12',
        "band": 'harder',
        "text": "A treatment raises a person's villus surface area by "
                '20%, to ×1.2 of what it was, but also leaves the '
                'wall half as thick again, at ×1.5. Roughly what '
                'happens to their overall rate of absorption?',
        "options": [
            {"text": 'It rises by about 20%, since the extra surface '
                     'area is what decides the rate.', "correct": False,
             "why": 'Area is only half of it. A wall half as thick '
                    'again lengthens every crossing, and 1.2 divided '
                    'by 1.5 leaves the rate lower than before, not '
                    'higher.'},
            {"text": 'It falls by about a fifth, since the ×1.2 area '
                     'gain is outweighed by a wall ×1.5 thicker.',
             "correct": True},
            {"text": 'It stays exactly the same, since a gain in area '
                     'and a thicker wall cancel each other out.',
             "correct": False,
             "why": 'They would cancel if the two changes were the '
                    'same size. Here the thickening, ×1.5, is the '
                    'larger of the two, so the rate falls.'},
            {"text": 'It falls by about 30%, the difference between a '
                     '20% rise and a 50% rise.', "correct": False,
             "why": 'Subtracting the two percentages is not how they '
                    'combine. One divides into the other: 1.2 divided '
                    'by 1.5 is 0.8, a fall of about a fifth.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h13',
        "band": 'harder',
        "text": "A kidney dialysis machine filters a patient's blood "
                'across a thin, folded artificial membrane, kept warm '
                'and constantly bathed in fluid, with blood flowing '
                'past continuously. Which of the four features from '
                'this lesson is this machine copying by keeping blood '
                'flowing past continuously?',
        "options": [
            {"text": 'A large surface area.', "correct": False,
             "why": 'Continuous blood flow is not what creates the '
                    "membrane's surface area, its folding does that. "
                    'Flow speed is a separate feature.'},
            {"text": 'A wall one cell thick.', "correct": False,
             "why": "The membrane's thinness is a separate design "
                    'choice from how fast blood flows past it. Flow '
                    'rate does not make the membrane thinner.'},
            {"text": 'A dense, constantly renewed supply that keeps a '
                     'concentration difference across the membrane '
                     'going.', "correct": True},
            {"text": 'A moist surface.', "correct": False,
             "why": 'Moisture is about the membrane being wet enough '
                    'for substances to cross, which is separate from '
                    'how fast the blood on one side is refreshed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h14',
        "band": 'harder',
        "text": 'Suppose the small intestine reached its ×60 total '
                'using only two levels of folding instead of three, '
                'with the circular folds still contributing ×3. What '
                'factor would the single remaining level have to '
                'supply on its own?',
        "options": [
            {"text": '×12.', "correct": False,
             "why": 'Three times twelve is thirty-six, well short of '
                    'sixty. The remaining level has to supply more '
                    'than that.'},
            {"text": '×15.', "correct": False,
             "why": 'Three times fifteen is forty-five, still short '
                    'of sixty. Fifteen is what folds and villi give '
                    'together, not the factor needed here.'},
            {"text": '×4.', "correct": False,
             "why": "Four is the microvilli level's own factor, and "
                    'three times four is only twelve. With one level '
                    'doing the work of two, a far bigger factor is '
                    'needed.'},
            {"text": '×20.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h15',
        "band": 'harder',
        "text": 'A leaf is broad and thin, with gases diffusing in '
                'and out through tiny pores called stomata. Which '
                "shared principle links a leaf's shape to a villus's "
                'shape?',
        "options": [
            {"text": 'Being broad, or folded, increases surface area, '
                     'and being thin shortens the diffusion distance, '
                     'both raise the rate of exchange.', "correct": True},
            {"text": 'Both rely on a network of blood vessels to '
                     'carry substances away.', "correct": False,
             "why": 'Leaves have no blood vessels. Whatever role a '
                    'dense blood supply plays in the villus, it is '
                    "not shared by a leaf's veins, which carry sugars "
                    'and water.'},
            {"text": 'Both are folded at three separate, nested '
                     'scales, in exactly the same way as each other.', "correct": False,
             "why": 'This lesson describes three folding scales '
                    "specific to the gut wall. A leaf's flat, broad "
                    'shape achieves a large surface without that '
                    'stepwise folding.'},
            {"text": 'Both use muscle contractions to force gases '
                     'through their surface, in the same way '
                     'peristalsis forces food along the whole gut.', "correct": False,
             "why": 'Neither structure uses muscle to move substances '
                    'across its surface. Both rely on diffusion, '
                    'driven by a concentration difference.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h16',
        "band": 'harder',
        "text": 'In an artificial-membrane model gut standing in a '
                'beaker of water, what would you predict if the '
                'surrounding water were gently stirred throughout, '
                'instead of left still?',
        "options": [
            {"text": 'No change, since stirring affects gases much '
                     'more than dissolved sugars.', "correct": False,
             "why": 'Stirring moves dissolved substances too. It '
                    'carries newly-arrived glucose away from the '
                    'membrane, exactly the role blood plays for a '
                    'real villus.'},
            {"text": 'Faster glucose movement out of the tubing, '
                     'because stirring carries glucose away from the '
                     'membrane and keeps the concentration difference '
                     'high.', "correct": True},
            {"text": 'Slower glucose movement out of the tubing, '
                     'because stirring pushes glucose back towards '
                     'the membrane.', "correct": False,
             "why": 'Stirring disperses substances away from where '
                    'they entered, not back towards the source. It '
                    'should help maintain the gradient, not oppose '
                    'it.'},
            {"text": 'The membrane would become thicker in stirred '
                     'water.', "correct": False,
             "why": 'Stirring the surrounding water cannot change the '
                    'physical thickness of the membrane itself. It '
                    'only affects how quickly the outside '
                    'concentration builds up.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h17',
        "band": 'harder',
        "text": 'A tapeworm living in the human gut has no digestive '
                'system of its own, it absorbs already-digested '
                'nutrients directly through its entire body surface, '
                'which is long and flattened. Why is a long, flat '
                'shape well suited to this way of feeding?',
        "options": [
            {"text": "It keeps the worm's temperature constant, which "
                     'speeds up any diffusion.', "correct": False,
             "why": "The shape's main function here is not "
                    'temperature control. A long, flat shape '
                    'maximises the surface area available for '
                    "absorption over the worm's body."},
            {"text": 'It lets the worm swim faster through the gut '
                     'contents to find more food.', "correct": False,
             "why": 'Gut-dwelling tapeworms are not active swimmers '
                    'hunting for food, they are bathed in '
                    "already-digested nutrients. The shape's "
                    'advantage is surface area.'},
            {"text": 'It gives a very large surface area relative to '
                     "the worm's volume, for absorbing nutrients over "
                     'its whole body.', "correct": True},
            {"text": 'It allows the worm to fold its own outer '
                     'surface into villi-like projections, exactly as '
                     'a gut wall does inside a host.', "correct": False,
             "why": "The worm's own body surface does the absorbing, "
                    'it is not folding a gut wall, since it lives '
                    "inside somebody else's gut and has none of its "
                    'own.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h18',
        "band": 'harder',
        "text": "If blood flow past a villus's capillaries were made "
                'faster and faster without limit, would absorption '
                'also increase without limit?',
        "options": [
            {"text": 'Yes, blood flow speed is the one feature that '
                     'limits absorption.', "correct": False,
             "why": 'Blood flow is one of four features. Beyond a '
                    "point, the surface area and the wall's diffusion "
                    'path would limit how fast molecules could cross.'},
            {"text": 'No, because faster blood flow would eventually '
                     'dissolve the villus wall.', "correct": False,
             "why": 'This lesson describes no such damage mechanism. '
                    'The limit on absorption comes from the other '
                    'three features, not from blood flow destroying '
                    'tissue.'},
            {"text": 'Yes, doubling blood flow speed exactly doubles '
                     'the absorption rate, at any speed it is already '
                     'moving at, with no limit of any kind.', "correct": False,
             "why": 'That would only be true if blood flow were the '
                    'sole limiting feature at every speed. Once the '
                    'concentration difference is already well '
                    'maintained, further speed gives smaller gains.'},
            {"text": 'No, beyond a certain point, the surface area '
                     'and the diffusion distance across the wall '
                     'become the limiting features instead.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h19',
        "band": 'harder',
        "text": 'A test patch of gut wall measuring 2 m² absorbs '
                'glucose at about 5 g per minute. If a real small '
                "intestine's 30 m² of surface absorbed at the same "
                'rate per square metre, roughly how much glucose '
                'would it absorb per minute?',
        "options": [
            {"text": 'About 75 g per minute.', "correct": True},
            {"text": 'About 15 g per minute.', "correct": False,
             "why": 'That divides rather than scales up correctly. '
                    'Thirty square metres is fifteen times the 2 m² '
                    'patch, so the rate should be fifteen times five '
                    'grams.'},
            {"text": 'About 60 g per minute.', "correct": False,
             "why": "That comes from the area's ×60 comparison with "
                    'the plain, unfolded tube, a different number '
                    'from the ×15 scaling needed here.'},
            {"text": 'About 300 g per minute.', "correct": False,
             "why": 'Thirty square metres is fifteen times 2 m², not '
                    'sixty times. Multiplying by sixty over-scales '
                    'the rate.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h20',
        "band": 'harder',
        "text": 'If any one of the three folding factors, ×3, ×5 or '
                '×4, were halved, while the other two stayed the '
                'same, which one would cost the least total surface '
                'area?',
        "options": [
            {"text": 'Halving the villi factor, ×5, since it is the '
                     'largest number.', "correct": False,
             "why": 'Multiplying three numbers together, halving any '
                    'one of them halves the whole product by the same '
                    'amount, it does not matter which one is largest.'},
            {"text": 'It makes no difference which one, halving any '
                     'single factor halves the total area by exactly '
                     'the same amount.', "correct": True},
            {"text": 'Halving the microvilli factor, ×4, since it is '
                     'the smallest structure.', "correct": False,
             "why": 'Being the smallest structure physically does not '
                    "make its factor's mathematical effect any "
                    'smaller. Halving any one of the three has an '
                    'identical effect.'},
            {"text": 'Halving the circular-folds factor, ×3, since it '
                     'is the first level applied.', "correct": False,
             "why": 'Being applied first does not give a factor '
                    'special weight in a multiplication. All three '
                    'factors contribute equally to the final total.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h21',
        "band": 'harder',
        "text": 'If instead one folding level failed completely, its '
                'factor becoming ×1 instead of its usual value, which '
                "level's failure would cost the largest fraction of "
                'the total area?',
        "options": [
            {"text": 'Circular folds, ×3 becoming ×1.', "correct": False,
             "why": 'Losing a factor of three is a real loss, but it '
                    'is the smallest of the three factors, so its '
                    'failure costs the smallest fraction of the '
                    'total.'},
            {"text": 'Microvilli, ×4 becoming ×1.', "correct": False,
             "why": 'A factor of four failing costs more than the '
                    'folds failing, but villi contribute an even '
                    'bigger factor, so their failure costs a larger '
                    'fraction still.'},
            {"text": 'Villi, ×5 becoming ×1.', "correct": True},
            {"text": 'All three would cost exactly the same fraction, '
                     'whichever failed.', "correct": False,
             "why": 'Unlike halving each factor by the same '
                    'proportion, dropping a factor down to ×1 loses '
                    'more of the total the bigger that factor '
                    "originally was, and villi's ×5 is the biggest."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h22',
        "band": 'harder',
        "text": "A student writes: 'The small intestine has villi, "
                "which are tiny, so it can absorb lots of food.' A "
                'teacher marks this as only partially correct. What '
                'is the paragraph missing?',
        "options": [
            {"text": "It should say 'microvilli' instead of 'villi', "
                     'since microvilli, and not villi, are the '
                     'structures that matter for how much food a '
                     "student's gut absorbs.", "correct": False,
             "why": 'Villi are a genuine part of the answer, they are '
                    'the biggest single contributor to surface area. '
                    "Swapping the word would not fix what's missing."},
            {"text": "It should not mention villi being 'tiny', since "
                     'size is irrelevant to absorption.', "correct": False,
             "why": 'Being small individually is part of why villi '
                    'can be so numerous and give such a large total '
                    'area, the detail is not irrelevant.'},
            {"text": 'It should add that villi are found in the '
                     'stomach, to be geographically precise.', "correct": False,
             "why": 'Villi line the small intestine, not the stomach. '
                    'Adding a location this wrong would make the '
                    'answer worse, not more complete.'},
            {"text": 'It should explain how villi help, that they '
                     'increase surface area, rather than just '
                     'asserting that they do, without saying why that '
                     'matters for absorption.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h23',
        "band": 'harder',
        "text": 'A newspaper describes the small intestine as having '
                '"an absorbing surface the size of a tennis court". A '
                'doubles tennis court is about 261 m², and the figure '
                'for the small intestine is about 30 m². Evaluate the '
                "newspaper's comparison.",
        "options": [
            {"text": 'It overstates the surface by roughly nine '
                     'times, so it is a poor comparison.', "correct": True},
            {"text": 'It is a fair comparison, since both figures '
                     'describe areas that are large.', "correct": False,
             "why": '261 m² against 30 m² is nearly a ninefold '
                    'difference. Two numbers both being large does '
                    'not make one a fair stand-in for the other.'},
            {"text": 'It understates the surface, since a tennis '
                     'court is smaller than 30 m².', "correct": False,
             "why": 'A doubles tennis court is far larger than 30 m², '
                    'not smaller, so the comparison overstates the '
                    'surface rather than understating it.'},
            {"text": 'It cannot be judged, since a court has no fixed '
                     'area to compare against.', "correct": False,
             "why": 'A doubles tennis court has a fixed size, about '
                    '261 m². That is a definite number, and it is '
                    'enough to compare against 30 m².'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h24',
        "band": 'harder',
        "text": 'A blue whale is far bigger than a human and needs '
                'proportionally more food. If it achieved extra gut '
                'surface area the same way as us, by folding, would '
                'you expect more or fewer levels of folding than a '
                "human's three?",
        "options": [
            {"text": 'Fewer, because larger animals need less surface '
                     'area relative to their size.', "correct": False,
             "why": 'The whale needs a lot more absorbing surface for '
                    'its much greater food intake, not less, which '
                    'points towards more folding, not fewer levels.'},
            {"text": 'Very likely more, or at least a much bigger '
                     'tube, since it needs to fit far more absorbing '
                     'surface into its gut for a much larger '
                     'appetite.', "correct": True},
            {"text": 'Exactly the same three levels, since folding '
                     'tops out at three levels in any animal, '
                     'regardless of how large its body or its '
                     'appetite for food is.', "correct": False,
             "why": 'Nothing in this lesson claims three is a fixed '
                    'universal maximum. It states how the human '
                    'intestine achieves its area, not a rule for '
                    'every animal.'},
            {"text": 'None whatsoever, because larger animals absorb '
                     'food through their skin instead.', "correct": False,
             "why": 'Absorbing food through the skin is not how any '
                    'land or marine mammal, including a whale, takes '
                    'in nutrients. It still needs a gut with an '
                    'absorbing surface.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h25',
        "band": 'harder',
        "text": 'A teacher compares the blood flowing past a villus '
                'to a sink with the tap running and the plug out, so '
                'the water level never rises. Which part of the '
                'diffusion process does this analogy best represent?',
        "options": [
            {"text": 'The folding of the wall into villi and '
                     'microvilli.', "correct": False,
             "why": 'The sink analogy says nothing about surface '
                    'shape or folding, it is about flow keeping a '
                    'level low, which maps onto the blood supply.'},
            {"text": 'The one-cell thickness of the villus wall.', "correct": False,
             "why": 'Wall thickness is about the distance molecules '
                    'travel, not about anything continuously flowing '
                    'away. The analogy is about a maintained low '
                    'level.'},
            {"text": 'The blood supply constantly carrying absorbed '
                     'molecules away, which keeps the concentration '
                     'on the blood side low.', "correct": True},
            {"text": 'The moist surface needed for molecules to '
                     'dissolve before crossing.', "correct": False,
             "why": 'Moisture is about molecules being in solution to '
                    'cross at all, not about anything being '
                    'continuously carried away. The analogy fits the '
                    "blood supply's role."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h26',
        "band": 'harder',
        "text": "This lesson's four features fall into two kinds: "
                'those that make an individual crossing possible or '
                'fast, and those that make many crossings happen at '
                'scale, or keep the driving difference going. Which '
                "feature belongs in the 'making it possible or fast "
                "for one molecule' group, alongside the moist "
                'surface?',
        "options": [
            {"text": 'Large surface area, since a bigger surface is '
                     'what lets each individual molecule find a gap '
                     'to cross through more quickly than it could.', "correct": False,
             "why": 'Surface area is about how many crossings can '
                    'happen at once, across the whole surface, not '
                    "about what makes a single molecule's crossing "
                    'fast.'},
            {"text": 'A dense blood supply, since blood is the thing '
                     'that carries an individual molecule onward once '
                     'it has crossed the wall.', "correct": False,
             "why": 'Blood supply is about maintaining the difference '
                    'in concentration across the whole surface, over '
                    'time, not about one individual crossing.'},
            {"text": 'Both surface area and blood supply equally, '
                     'since each one plays some part in how fast one '
                     'molecule gets across the wall.', "correct": False,
             "why": 'Neither of those describes what makes one '
                    "molecule's crossing possible or quick, that role "
                    "belongs to the wall's thinness, alongside the "
                    'moist surface.'},
            {"text": 'A wall one cell thick, thinness, like moisture, '
                     "is about what makes an individual molecule's "
                     'crossing fast and possible.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h27',
        "band": 'harder',
        "text": 'A typical UK classroom floor measures about 56 m². '
                "Roughly what fraction of that floor does the small "
                "intestine's absorbing surface, about 30 m², cover?",
        "options": [
            {"text": 'A little over a half.', "correct": True},
            {"text": 'About a tenth.', "correct": False,
             "why": 'A tenth of 56 m² is under 6 m², far smaller than '
                    'the 30 m² in question.'},
            {"text": 'About a fifth.', "correct": False,
             "why": 'A fifth of 56 m² is roughly 11 m², still well '
                    'short of 30 m².'},
            {"text": 'Almost the whole floor.', "correct": False,
             "why": 'The whole floor is about 56 m², nearly twice the '
                    "small intestine's roughly 30 m². That is a poor "
                    'match.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h28',
        "band": 'harder',
        "text": 'A kitchen sponge has a highly porous structure, '
                'riddled with tiny holes, giving it an enormous '
                'surface area for its size. Sponges soak up water '
                'fast. Which of the four features from this lesson '
                "does a sponge's porous structure most directly "
                'provide?',
        "options": [
            {"text": 'A dense blood supply.', "correct": False,
             "why": 'A sponge has no blood supply, and nothing in it '
                    'carries water away to maintain a difference, '
                    'soaking is a different, passive process from the '
                    'blood-driven mechanism in a villus.'},
            {"text": 'A very large surface area.', "correct": True},
            {"text": 'A wall one cell thick.', "correct": False,
             "why": "A sponge's structure is not organised into a "
                    'one-cell-thick barrier the way a villus wall is, '
                    'its advantage is the sheer amount of surface its '
                    'holes create.'},
            {"text": 'A moist surface, before any water is added.', "correct": False,
             "why": 'A dry sponge has no moisture until water is '
                    "added to it, its porous structure's advantage is "
                    'the surface area itself, not moisture.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h29',
        "band": 'harder',
        "text": 'If each of the three folding factors were increased '
                'by 10%, so ×3 becomes ×3.3, and so on for the other '
                'two, roughly how much would the total surface area '
                'increase by overall?',
        "options": [
            {"text": 'Exactly 10%, since each factor rose by 10%.', "correct": False,
             "why": 'When three factors are each multiplied by 1.1, '
                    'the combined effect compounds rather than simply '
                    'adding, the total rises by more than 10%.'},
            {"text": 'Exactly 30%, since three lots of 10% add '
                     'together.', "correct": False,
             "why": 'Percentage increases applied together compound '
                    'rather than simply add. Three separate ×1.1 '
                    'increases multiply together to slightly more '
                    'than a 30% rise.'},
            {"text": 'A bit more than 30%, because the three 10% '
                     'increases compound together rather than simply '
                     'adding.', "correct": True},
            {"text": 'About 100%, because tripling the number of '
                     'increased factors roughly doubles the effect.', "correct": False,
             "why": 'Nothing here doubles or triples in that way. '
                    'Three separate 10% increases compound to a '
                    'little over 30%, nowhere near 100%.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-07-h30',
        "band": 'harder',
        "text": 'Species X has a smooth, unfolded gut lining but a '
                'very dense blood supply. Species Y has a highly '
                "folded gut lining, like a human's, but a poor blood "
                'supply. Both have the same wall thickness and '
                'moisture. Which is likely to absorb food fastest '
                'overall, and why?',
        "options": [
            {"text": 'Species X, because a dense blood supply on its '
                     'own guarantees fast absorption.', "correct": False,
             "why": 'Blood supply alone cannot compensate for a tiny '
                    'surface area. With hardly any folding, Species X '
                    'has very little surface for molecules to cross.'},
            {"text": 'Neither, without all four features present and '
                     'strong, absorption cannot happen in any useful '
                     'way.', "correct": False,
             "why": 'This lesson does not claim all four must be '
                    'equally strong for any absorption to occur, it '
                    'shows that weakening one feature reduces the '
                    'rate, not that absorption switches off.'},
            {"text": 'They are certain to absorb at exactly the same '
                     "rate, since one species' strength in one "
                     "feature must cancel out the other species' "
                     'single weakness, in a completely different '
                     'feature entirely.', "correct": False,
             "why": 'Nothing here shows the two effects are '
                    "numerically equal. Whether Species Y's large "
                    'area outweighs its poor blood supply, or the '
                    'reverse, cannot be assumed.'},
            {"text": 'It cannot be said for certain without knowing '
                     "the size of each species' strength and "
                     'weakness, a big enough advantage in one feature '
                     'could outweigh a big enough disadvantage in the '
                     'other.', "correct": True},
        ],
        "figure": None,
    },
]
