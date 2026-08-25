"""P9 lesson 01 — Charging by rubbing: twelve questions (MRB-223).

Written against Design's page. The rod and the duster, the seven-material
ladder and the bench are hers.

The discriminations, in the order the lesson builds them:

  · charge is SEPARATED, never made (`CHRG-01`) — the easier band opens
    here because it is the sentence the whole unit rests on;
  · positive means electrons GONE, not protons arrived (`CHRG-02`);
  · BOTH objects end up charged, equally and oppositely (`CHRG-03`);
  · which way the transfer goes is a property of the PAIR, not of one
    material on its own (`CHRG-04`) — the harder band sits here, with the
    same-material case and the conductor case.

⚠️ POSITION IS AUTHORED — 2,3,0,1 · 0,1,3,2 · 1,0,2,3, three of each.

⚠️ Neither marked rung is restated: the glass-and-wool prediction and the
balloon-on-a-jumper argument are the ladder's, and nothing here reuses
either pairing or either scenario.
"""

UNIT = "P9"
LESSON = "charging-by-rubbing"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p9-01-e01",
        "band": "easier",
        "text": "When two insulators are rubbed together, what actually "
                "moves between them?",
        "options": [
            {"text": "Protons", "correct": False,
             "why": "Protons are held inside the nuclei and never move in "
                    "ordinary matter. Only electrons can cross."},
            {"text": "Whole atoms", "correct": False,
             "why": "The materials do not swap atoms. Nothing but the outer "
                    "electrons changes sides."},
            {"text": "Electrons", "correct": True},
            {"text": "Charge itself, made by the friction", "correct": False,
             "why": "Charge is not a substance that can be made and handed "
                    "over. What crosses is electrons, and they were already "
                    "there."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e02",
        "band": "easier",
        "text": "An object is positively charged. What does that mean about "
                "its protons and electrons?",
        "options": [
            {"text": "It has gained extra protons", "correct": False,
             "why": "Nothing positive was added. Protons stay in their "
                    "nuclei throughout."},
            {"text": "It has gained extra electrons", "correct": False,
             "why": "Extra electrons would make it negative. Positive is the "
                    "other way round."},
            {"text": "It has equal numbers of both, but arranged "
                     "differently across its surface", "correct": False,
             "why": "Equal numbers is exactly what neutral means. A charged "
                    "object no longer has them balanced."},
            {"text": "It has fewer electrons than protons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e03",
        "band": "easier",
        "text": "Why does rubbing a metal rod held in your bare hand leave "
                "it uncharged?",
        "options": [
            {"text": "Metal is a conductor, so the separated charge runs "
                     "away through you", "correct": True},
            {"text": "Metal has no electrons in it to move", "correct": False,
             "why": "Metals are full of loose electrons — that is exactly "
                    "what makes them conductors."},
            {"text": "Metal is too smooth for the rubbing to make contact "
                     "at enough points", "correct": False,
             "why": "Polish is not the issue. Charge does separate; it just "
                    "does not stay, because it can travel away."},
            {"text": "Metal is too heavy for a charge that small to have "
                     "any effect on it", "correct": False,
             "why": "Mass has nothing to do with it. A light plastic rod and "
                    "a heavy plastic rod both charge up."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e04",
        "band": "easier",
        "text": "Two neutral insulators are rubbed together. What is the "
                "total charge on the two of them afterwards?",
        "options": [
            {"text": "Twice what it was, because both are now charged",
             "correct": False,
             "why": "The two charges are opposite, so they cancel. Twice "
                    "nothing is still nothing."},
            {"text": "Zero — the two charges are equal and opposite",
             "correct": True},
            {"text": "Negative, because electrons were involved",
             "correct": False,
             "why": "The electrons only moved from one object to the other. "
                    "None were added and none were lost."},
            {"text": "It depends on which of the two materials was rubbed "
                     "harder against the other one", "correct": False,
             "why": "Rubbing harder moves more electrons, but it moves them "
                    "OFF one and ON TO the other, so the total is still "
                    "zero."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p9-01-s01",
        "band": "standard",
        "text": "Human hair sits at the top of the triboelectric list and "
                "PVC at the bottom. A PVC pipe is rubbed on someone's hair. "
                "What happens?",
        "options": [
            {"text": "The PVC becomes negative and the hair becomes "
                     "positive", "correct": True},
            {"text": "The PVC becomes positive and the hair becomes "
                     "negative", "correct": False,
             "why": "That is the transfer the wrong way. The material lower "
                    "on the list holds electrons more tightly, so PVC takes "
                    "them and ends negative."},
            {"text": "Both become negative, because rubbing always adds "
                     "electrons", "correct": False,
             "why": "Rubbing adds nothing. Every electron one object gains "
                    "is one the other lost."},
            {"text": "Neither changes, because hair is not an insulator "
                     "and cannot hold a charge at all", "correct": False,
             "why": "Dry hair is an insulator, and it is the classic "
                    "demonstration — a comb through it lifts paper."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s02",
        "band": "standard",
        "text": "A cotton cloth sits in the middle of the list. Why is it a "
                "poor choice for a classroom demonstration?",
        "options": [
            {"text": "Cotton is a conductor, so any charge escapes at once",
             "correct": False,
             "why": "Cotton is an insulator like everything else on the "
                    "list. Its problem is its position, not its "
                    "conductivity."},
            {"text": "It is only a few steps from most other materials, so "
                     "little charge crosses", "correct": True},
            {"text": "Cotton always ends up positive, whatever it is rubbed "
                     "against, so nothing can be predicted", "correct": False,
             "why": "It ends up positive against materials below it and "
                    "negative against those above it. That is the point of "
                    "the ordering."},
            {"text": "Cotton loses its charge to the air faster than any "
                     "other material on the list does", "correct": False,
             "why": "Charge does leak into the air, and humidity makes it "
                    "worse — but that affects every material, not cotton "
                    "especially."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s03",
        "band": "standard",
        "text": "A student rubs one acetate strip against a second, "
                "identical acetate strip. What should they find?",
        "options": [
            {"text": "One becomes positive and the other negative, decided "
                     "by which was moving", "correct": False,
             "why": "Which one you hold still makes no difference. The "
                    "transfer is set by the two materials, and here they are "
                    "the same."},
            {"text": "Both become positive, because acetate sits above the "
                     "middle of the list", "correct": False,
             "why": "A material's position matters only relative to what it "
                    "is rubbed against. Against itself there is no "
                    "difference to act on."},
            {"text": "Both become negative, because rubbing strips "
                     "electrons off into the air", "correct": False,
             "why": "Electrons do not leave into the air. They cross from "
                    "one surface to the other, and only if the two hold them "
                    "differently."},
            {"text": "Neither becomes charged, because the two hold their "
                     "electrons equally tightly", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s04",
        "band": "standard",
        "text": "A wool duster is rubbed on a polythene rod, and the rod "
                "gains thirty billion electrons. What has happened to the "
                "duster?",
        "options": [
            {"text": "It has gained thirty billion electrons as well",
             "correct": False,
             "why": "Both objects cannot gain. The electrons the rod now has "
                    "are the ones the duster no longer has."},
            {"text": "It has lost some electrons, but fewer than thirty "
                     "billion, because some are lost in the rubbing",
             "correct": False,
             "why": "None go missing. Every electron that left the duster "
                    "arrived on the rod, so the two counts are the same."},
            {"text": "It has lost thirty billion electrons, so it now "
                     "carries the same size of charge, positive",
             "correct": True},
            {"text": "It has stayed neutral, because the rod was the object "
                     "being charged", "correct": False,
             "why": "There is no such thing as charging one object on its "
                    "own. The duster is the place every one of those "
                    "electrons came from."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p9-01-h01",
        "band": "harder",
        "text": "Two surfaces are pressed firmly together and lifted "
                "straight apart, with no rubbing at all. Some charge is "
                "separated. Why?",
        "options": [
            {"text": "Pressing warms the surfaces, and warm materials give "
                     "up electrons more readily than cold ones do",
             "correct": False,
             "why": "Temperature is not the mechanism. What matters is that "
                    "the two surfaces were in contact at all."},
            {"text": "Contact is what lets electrons cross, and rubbing only "
                     "makes more of it", "correct": True},
            {"text": "Lifting the surfaces apart pulls electrons out of one "
                     "of them", "correct": False,
             "why": "The lifting does not pull anything out. It just leaves "
                    "the electrons wherever they crossed to."},
            {"text": "Charge cannot separate without rubbing, so the "
                     "measurement must be a mistake", "correct": False,
             "why": "It is a real and well known effect. Rubbing helps "
                    "because it multiplies the contacts, not because "
                    "friction itself makes charge."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h02",
        "band": "harder",
        "text": "The same experiment gives a strong charge in January and "
                "almost nothing on a humid July afternoon. Why?",
        "options": [
            {"text": "Water on the surfaces conducts, so charge escapes as "
                     "fast as it is separated", "correct": True},
            {"text": "Warm air makes electrons move faster, so they cross "
                     "back over", "correct": False,
             "why": "The electrons do not cross back through the insulator. "
                    "They leak away through the film of water on its "
                    "surface."},
            {"text": "Humid air is heavier, so it presses the two surfaces "
                     "together and stops them rubbing properly",
             "correct": False,
             "why": "The rubbing works exactly as well. What changes is "
                    "whether the separated charge stays where it was put."},
            {"text": "Charge is created more slowly at higher temperatures, "
                     "so a warm room gives a smaller reading",
             "correct": False,
             "why": "Charge is never created at any temperature. It is "
                    "separated, and in July it leaks away."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h03",
        "band": "harder",
        "text": "Aircraft carry small conducting wicks on their wingtips, "
                "and a fuel tanker is earthed before pumping starts. What "
                "problem do both solve?",
        "options": [
            {"text": "They stop the vehicle picking up charge from the "
                     "ground it is standing on", "correct": False,
             "why": "The charge is separated by movement — air over a wing, "
                    "fuel through a pipe — rather than picked up from the "
                    "ground."},
            {"text": "They make the metal skin a better insulator, so charge "
                     "cannot build up on it", "correct": False,
             "why": "The opposite: both work by CONDUCTING, giving the "
                    "separated charge somewhere to go."},
            {"text": "Moving air or fuel rubs against the surface, so charge "
                     "separates and could build to a spark", "correct": True},
            {"text": "They earth the vehicle so that lightning is drawn away "
                     "from it and into the ground", "correct": False,
             "why": "A wick cannot do anything about a lightning strike. It "
                    "bleeds away the small charge the vehicle's own movement "
                    "separates."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h04",
        "band": "harder",
        "text": "A rubbed rod is stroked twenty times instead of ten, and "
                "the charge is not twice as big. What is the best "
                "explanation?",
        "options": [
            {"text": "The rod runs out of electrons to give away",
             "correct": False,
             "why": "Nothing like enough electrons move for that. There are "
                    "vastly more in the rod than ever cross."},
            {"text": "The extra strokes rub some of the separated charge "
                     "back off again, exactly undoing the first ten",
             "correct": False,
             "why": "The charge still rises with more strokes — just by "
                    "less each time. It is not being undone."},
            {"text": "The measuring instrument saturates, so the charge is "
                     "really twice as big and cannot be read",
             "correct": False,
             "why": "The charge really does level off. Blaming the "
                    "instrument would leave you expecting a rod to charge "
                    "without limit, which it does not."},
            {"text": "Charge leaks away and the air breaks down, so the "
                     "amount levels off towards a ceiling", "correct": True},
        ],
        "figure": None,
    },
]
