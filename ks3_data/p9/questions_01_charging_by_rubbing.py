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
        # ⊕ MRB-297 · 1 Sep 2026 — THE RE-RANK MOVED COTTON AND THIS STEM
        # DID NOT FOLLOW IT. The stem read "A cotton cloth sits in the
        # middle of the list." On origin/main cotton was row 4 of 7, the
        # exact centre, and that was literally true. This branch re-ranked
        # the series (acetate above wool) and cotton is now row 5 of 7, so
        # the centre is the wool duster and the stem named a position
        # cotton no longer holds — while the lesson's badge still said
        # "middle". THE RANKING IS RIGHT AND STAYS: an acetate rod rubbed
        # with wool is the standard school demonstration of a POSITIVE rod,
        # so acetate must sit above wool, and cotton genuinely sits below
        # wool and near neutral. The stem is what moves, and it now says
        # the thing the badge says — that cotton sits between the materials
        # that lose electrons and the ones that gain them — which is true
        # at row 5 with rows 1–4 badged "loses" and rows 6–7 "gains".
        "text": "A cotton cloth sits between the materials that lose "
                "electrons and the ones that gain them. Why is it a poor "
                "choice for a classroom demonstration?",
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p9-01-e05",
        "band": "easier",
        "text": "Do protons ever move when an object is charged by rubbing?",
        "options": [
            {"text": "No — only electrons move", "correct": True},
            {"text": "Yes, protons move to the object that becomes positive",
             "correct": False,
             "why": "Protons are locked in the nucleus. An object becomes "
                    "positive by LOSING electrons."},
            {"text": "Yes, protons and electrons both move", "correct": False,
             "why": "Only the outer electrons are loose enough to cross "
                    "between two surfaces."},
            {"text": "Only in metals, where the protons are free",
             "correct": False,
             "why": "Even in a metal the protons stay in place; the free "
                    "particles are electrons."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e06",
        "band": "easier",
        "text": "An object is negatively charged. What does it have?",
        "options": [            {"text": "Fewer electrons than protons", "correct": False,
             "why": "Being short of electrons leaves an object POSITIVE."},
            {"text": "Equal numbers of protons and electrons", "correct": False,
             "why": "That is what makes an object neutral, not charged."},
            {"text": "More protons than it started with", "correct": False,
             "why": "The number of protons never changes; only electrons "
                    "move."},
            {"text": "More electrons than protons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e07",
        "band": "easier",
        "text": "Which of these can be charged by rubbing it?",
        "options": [            {"text": "A copper pipe held in a bare hand", "correct": False,
             "why": "Copper is a conductor, so any charge runs away through "
                    "the hand as fast as it is made."},
            {"text": "A steel spoon held in a bare hand", "correct": False,
             "why": "Steel conducts too, so the charge escapes through the "
                    "person holding it."},
            {"text": "An aluminium ruler held in a bare hand",
             "correct": False,
             "why": "Aluminium is a metal, and the charge leaks away through "
                    "the hand."},
            {"text": "A plastic rod held in a bare hand", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e08",
        "band": "easier",
        "text": "A balloon rubbed on a jumper becomes negatively charged. "
                "What has the jumper become?",
        "options": [            {"text": "Negatively charged as well", "correct": False,
             "why": "The electrons went one way, so one object must be short "
                    "of them."},
            {"text": "Charged only if it is made of wool", "correct": False,
             "why": "Whatever it is made of, the electrons that left it have "
                    "to leave it charged."},
            {"text": "Neutral, because it gave its charge away",
             "correct": False,
             "why": "It has lost electrons, which leaves it with more protons "
                    "than electrons."},
            {"text": "Positively charged, having lost electrons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e09",
        "band": "easier",
        "text": "What makes an object neutral?",
        "options": [
            {"text": "It has equal numbers of protons and electrons",
             "correct": True},
            {"text": "It has no protons or electrons in it at all",
             "correct": False,
             "why": "Every object is full of both; being neutral means they "
                    "balance."},
            {"text": "It has been rubbed with a material of the same kind",
             "correct": False,
             "why": "That happens to transfer almost nothing, but neutral is "
                    "about the balance of particles."},
            {"text": "It is made of an insulating material", "correct": False,
             "why": "Insulators and conductors alike are neutral until "
                    "electrons are moved."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e10",
        "band": "easier",
        "text": "The triboelectric series puts materials in order of…",
        "options": [            {"text": "how hard they are to rub", "correct": False,
             "why": "Roughness affects how well two surfaces meet, but it is "
                    "not what the list orders."},
            {"text": "how well they conduct electricity", "correct": False,
             "why": "That is a different property; the list is made up mostly "
                    "of insulators."},
            {"text": "how much charge they contain to start with",
             "correct": False,
             "why": "Every material starts neutral; the list is about what "
                    "happens when two are rubbed."},
            {"text": "how tightly they hold their outer electrons",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e11",
        "band": "easier",
        "text": "What charge does an electron carry?",
        "options": [            {"text": "Positive", "correct": False,
             "why": "That is the proton's charge. An electron is the negative "
                    "one."},
            {"text": "Positive or negative, depending on the material",
             "correct": False,
             "why": "An electron's charge is always the same, whatever it is "
                    "part of."},
            {"text": "None — it is neutral", "correct": False,
             "why": "A neutral particle could not be moved by rubbing to "
                    "leave anything charged."},
            {"text": "Negative", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e12",
        "band": "easier",
        "text": "An object loses some of its electrons. It becomes…",
        "options": [            {"text": "negatively charged", "correct": False,
             "why": "Losing negative particles leaves an object short of "
                    "them, so it is positive."},
            {"text": "lighter, but not charged", "correct": False,
             "why": "It is very slightly lighter, and it is certainly "
                    "charged: the balance is broken."},
            {"text": "neutral", "correct": False,
             "why": "It was neutral before; losing electrons is what upsets "
                    "the balance."},
            {"text": "positively charged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e13",
        "band": "easier",
        "text": "Rubbing a rod harder and for longer usually…",
        "options": [
            {"text": "transfers more electrons, so the charge grows",
             "correct": True},
            {"text": "makes the charge change sign", "correct": False,
             "why": "The direction is set by which material holds its "
                    "electrons more tightly, not by the effort."},
            {"text": "creates protons on the surface", "correct": False,
             "why": "Protons are never made or moved by rubbing."},
            {"text": "makes no difference to the charge at all", "correct": False,
             "why": "It does make a difference, though the charge stops "
                    "growing once the surfaces are fully involved."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e14",
        "band": "easier",
        "text": "Which of these is an insulator?",
        "options": [            {"text": "Copper", "correct": False,
             "why": "Copper is one of the best conductors there is."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal and conducts well."},
            {"text": "Steel", "correct": False,
             "why": "Steel is a metal, so charge moves through it easily."},
            {"text": "Polythene", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e15",
        "band": "easier",
        "text": "Where in an atom are the electrons?",
        "options": [            {"text": "In the nucleus, with the protons", "correct": False,
             "why": "The nucleus holds protons and neutrons; the electrons "
                    "are outside it."},
            {"text": "Only present in charged atoms", "correct": False,
             "why": "Every atom has them; a charged one simply has too many "
                    "or too few."},
            {"text": "Spread evenly through the whole atom", "correct": False,
             "why": "They are arranged around the nucleus rather than mixed "
                    "in with it."},
            {"text": "On the outside, around the nucleus", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e16",
        "band": "easier",
        "text": "After two insulators are rubbed together, their two charges "
                "are…",
        "options": [            {"text": "the same size and the same sign", "correct": False,
             "why": "The electrons went from one to the other, so the two "
                    "signs must differ."},
            {"text": "different sizes and opposite signs", "correct": False,
             "why": "Every electron that left one arrived at the other, so "
                    "the sizes match exactly."},
            {"text": "impossible to compare, because they are different "
                     "materials",
             "correct": False,
             "why": "Whatever the materials, the count of electrons "
                    "transferred is the same on both sides."},
            {"text": "the same size and opposite signs", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e17",
        "band": "easier",
        "text": "A charged plastic rod is gripped with a wet hand. What "
                "happens to its charge?",
        "options": [            {"text": "It grows, because water adds electrons", "correct": False,
             "why": "Water adds nothing; it provides a path for charge to "
                    "leave."},
            {"text": "It changes sign", "correct": False,
             "why": "Nothing reverses the charge; it simply drains away."},
            {"text": "It stays exactly as it was, because plastic is an "
                     "insulator",
             "correct": False,
             "why": "The plastic does hold it in place, but a wet hand on the "
                    "surface conducts it away."},
            {"text": "It leaks away, leaving the rod neutral", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p9-01-s05",
        "band": "standard",
        "text": "A polythene rod gains electrons from a woollen duster. What "
                "are the two charges afterwards?",
        "options": [
            {"text": "Rod negative, duster positive", "correct": True},
            {"text": "Rod positive, duster negative", "correct": False,
             "why": "Gaining electrons makes the rod negative, not "
                    "positive."},
            {"text": "Both negative, because rubbing makes negative charge",
             "correct": False,
             "why": "Rubbing makes nothing; the duster is short of exactly "
                    "the electrons the rod gained."},
            {"text": "Rod negative, duster still neutral", "correct": False,
             "why": "The duster lost those electrons, so it cannot still be "
                    "balanced."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s06",
        "band": "standard",
        "text": "A perspex rod is rubbed with wool and ends up positively "
                "charged. What happened to its electrons?",
        "options": [            {"text": "Some were destroyed by the rubbing", "correct": False,
             "why": "Electrons are never destroyed; they moved to the other "
                    "surface."},
            {"text": "They stayed put, and protons arrived instead",
             "correct": False,
             "why": "Protons never move between objects at all."},
            {"text": "Some moved from the wool to the perspex",
             "correct": False,
             "why": "That would make the perspex negative, and it is "
                    "positive."},
            {"text": "Some moved from the perspex to the wool", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s07",
        "band": "standard",
        "text": "A charged rod is touched against a metal plate connected to "
                "earth. What happens?",
        "options": [
            {"text": "The plate becomes charged and the rod stays charged",
             "correct": False,
             "why": "An earthed plate passes the charge straight to the "
                    "ground rather than keeping it."},
            {"text": "Nothing, because the plate is a conductor",
             "correct": False,
             "why": "Being a conductor is exactly what lets the charge move "
                    "away."},
            {"text": "The charge flows away and the rod is left neutral",
             "correct": True},
            {"text": "The rod's charge doubles as it meets the metal",
             "correct": False,
             "why": "Nothing multiplies charge; contact with earth removes "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s08",
        "band": "standard",
        "text": "A rod gains twenty billion electrons from a duster. How many "
                "did the duster lose?",
        "options": [
            {"text": "Ten billion, because they are shared", "correct": False,
             "why": "Nothing is shared out; every electron the rod gained "
                    "came from the duster."},
            {"text": "Forty billion, because both surfaces are involved",
             "correct": False,
             "why": "Both are involved, and exactly the same electrons are "
                    "counted on each side."},
            {"text": "None — the duster stays neutral", "correct": False,
             "why": "Losing twenty billion electrons is precisely what "
                    "charges the duster."},
            {"text": "Twenty billion, exactly the same number", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s09",
        "band": "standard",
        "text": "A balloon is rubbed on someone's hair and the strands rise "
                "and spread apart. Why?",
        "options": [
            {"text": "Because each strand took the same charge, and like "
                     "charges repel",
             "correct": True},
            {"text": "Because the balloon pulls each strand towards it",
             "correct": False,
             "why": "That would draw them together towards the balloon, not "
                    "spread them apart from one another."},
            {"text": "Because the hair has become lighter after rubbing",
             "correct": False,
             "why": "The mass barely changes; a force is pushing the strands "
                    "apart."},
            {"text": "Because static electricity makes hair curl",
             "correct": False,
             "why": "The strands stand apart rather than curling, and "
                    "repulsion is why."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s10",
        "band": "standard",
        "text": "Both the rod and the duster end up charged, but only the "
                "rod's charge is usually noticed. Why?",
        "options": [            {"text": "Because the duster's charge is much smaller",
             "correct": False,
             "why": "The two are exactly equal in size; what differs is "
                    "whether it stays put."},
            {"text": "Because the duster's charge is neutral", "correct": False,
             "why": "A charge cannot be neutral; the duster is genuinely "
                    "charged the opposite way."},
            {"text": "Because a cloth cannot hold any charge at all for long",
             "correct": False,
             "why": "A dry cloth on an insulating handle holds it perfectly "
                    "well."},
            {"text": "Because the duster is held in the hand and its charge "
                     "leaks away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s11",
        "band": "standard",
        "text": "A plastic ruler is rubbed on a sleeve and then picks up "
                "small pieces of paper. Where did electrons actually move?",
        "options": [
            {"text": "From the paper to the ruler, when they touched",
             "correct": False,
             "why": "The paper is picked up before contact, and the transfer "
                    "happened earlier."},
            {"text": "From the ruler to the paper, across the gap",
             "correct": False,
             "why": "Nothing crosses the gap; the ruler was already charged "
                    "before the paper came near."},
            {"text": "Between the ruler and the sleeve, during the rubbing",
             "correct": True},
            {"text": "Nowhere — the rubbing made new charge on the ruler",
             "correct": False,
             "why": "Charge is never made. It was separated between the two "
                    "rubbed surfaces."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s12",
        "band": "standard",
        "text": "Which statement about the triboelectric series is right?",
        "options": [            {"text": "It says exactly how much charge each material will "
                     "take",
             "correct": False,
             "why": "It gives no sizes at all — only the likely direction of "
                    "the transfer."},
            {"text": "It shows which materials are positive and which are "
                     "negative",
             "correct": False,
             "why": "Every material starts neutral; the sign depends on what "
                    "it is rubbed WITH."},
            {"text": "It lists materials in order of how well they conduct",
             "correct": False,
             "why": "That is a different property; these are mostly "
                    "insulators."},
            {"text": "It is a likely guide to which way electrons go, not a "
                     "guarantee",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s13",
        "band": "standard",
        "text": "Two identical rods are each rubbed with the same duster. "
                "What is true of their charges?",
        "options": [
            {"text": "They are opposite, because there are two rods",
             "correct": False,
             "why": "Each rod met the same material, so each lost or gained "
                    "electrons the same way."},
            {"text": "One is charged and the other is not", "correct": False,
             "why": "Both were rubbed with the same cloth, so both end up "
                    "charged."},
            {"text": "They have the same sign as each other", "correct": True},
            {"text": "They cancel each other out when brought together",
             "correct": False,
             "why": "Two like charges repel; cancelling would need opposite "
                    "signs."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s14",
        "band": "standard",
        "text": "A student says rubbing MADE the balloon's negative charge. "
                "What does looking at the jumper show?",
        "options": [
            {"text": "That the jumper is negative too, so charge was made "
                     "twice over",
             "correct": False,
             "why": "The jumper is positive, and that is the point: the "
                    "electrons came from it."},
            {"text": "That the jumper is still neutral, so charge was made",
             "correct": False,
             "why": "It cannot be neutral once it has lost the electrons the "
                    "balloon gained."},
            {"text": "That the jumper is positive by exactly the same amount, "
                     "so charge was separated",
             "correct": True},
            {"text": "That the jumper's charge depends on how hard it was "
                     "rubbed",
             "correct": False,
             "why": "The amount varies, but it always matches the balloon's "
                    "exactly — which is what settles the argument."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s15",
        "band": "standard",
        "text": "Why is it wrong to say a rod has GAINED positive charge?",
        "options": [            {"text": "Because positive charge is always smaller than negative "
                     "charge",
             "correct": False,
             "why": "A proton's charge matches an electron's exactly; size is "
                    "not the issue."},
            {"text": "Because charge cannot be gained or lost at all",
             "correct": False,
             "why": "Electrons certainly move between objects; it is protons "
                    "that stay put."},
            {"text": "Because a rod can only ever become negative",
             "correct": False,
             "why": "Rods are often positive — a perspex rod rubbed with wool "
                    "is."},
            {"text": "Because protons never move, so it has lost electrons "
                     "instead",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s16",
        "band": "standard",
        "text": "How could you show that a rubbed rod and its duster carry "
                "opposite charges?",
        "options": [            {"text": "Bring each near a hanging ball of known charge and "
                     "compare",
             "correct": True},
            {"text": "Weigh both before and after rubbing", "correct": False,
             "why": "The mass change is far too small to measure, and it "
                    "would not show the sign."},
            {"text": "See which one picks up more scraps of paper",
             "correct": False,
             "why": "Both attract paper whatever their sign, so this cannot "
                    "tell them apart."},
            {"text": "Touch them together and see whether a spark jumps",
             "correct": False,
             "why": "A spark shows charge was there, not which sign each one "
                    "had."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s17",
        "band": "standard",
        "text": "Why must both the rod and the duster be dry?",
        "options": [            {"text": "Because water stops electrons moving between the two "
                     "surfaces",
             "correct": False,
             "why": "The transfer still happens; the difficulty is keeping "
                    "the charge afterwards."},
            {"text": "Because water adds electrons to both surfaces",
             "correct": False,
             "why": "It adds nothing. It provides a path for charge to "
                    "leave."},
            {"text": "Because wet materials always take the opposite charge",
             "correct": False,
             "why": "The direction is unchanged; what changes is how long the "
                    "charge stays."},
            {"text": "Because a film of moisture conducts the charge away at "
                     "once",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p9-01-h05",
        "band": "harder",
        "text": "Two neutral insulators are rubbed together and both end up "
                "charged. Where did the charge come from?",
        "options": [
            {"text": "It was created by the energy of the rubbing",
             "correct": False,
             "why": "Rubbing supplies energy, not charge; the two together "
                    "are still neutral afterwards."},
            {"text": "It came out of the air between the two surfaces",
             "correct": False,
             "why": "The experiment works just as well in a vacuum, with no "
                    "air to supply anything."},
            {"text": "It was already there, and rubbing separated it",
             "correct": True},
            {"text": "It came from the person doing the rubbing",
             "correct": False,
             "why": "The two charges match each other exactly, which is what "
                    "shows the transfer was between them."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h06",
        "band": "harder",
        "text": "Why does the triboelectric series sometimes predict the "
                "wrong direction?",
        "options": [            {"text": "Because the surfaces matter — how clean, how rough, how "
                     "damp",
             "correct": True},
            {"text": "Because it was written before electrons were known "
                     "about",
             "correct": False,
             "why": "Its age is not the problem; it is that surfaces vary "
                    "from sample to sample."},
            {"text": "Because it applies only to conductors", "correct": False,
             "why": "It applies to insulators, which are the materials it "
                    "lists."},
            {"text": "Because charge is created at random each time",
             "correct": False,
             "why": "Nothing is created, and the results are far from random "
                    "— they are simply not guaranteed."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h07",
        "band": "harder",
        "text": "A charged rod is touched against a neutral metal sphere on "
                "an insulating stand, and the sphere becomes charged. Is that "
                "charging by rubbing?",
        "options": [            {"text": "Yes, because the two surfaces were in contact",
             "correct": False,
             "why": "Contact alone is not rubbing; nothing was dragged across "
                    "anything."},
            {"text": "Yes, because the sphere ends up with the opposite "
                     "charge",
             "correct": False,
             "why": "It ends up with the SAME sign as the rod, and the method "
                    "is contact either way."},
            {"text": "No, because a metal sphere cannot be charged at all",
             "correct": False,
             "why": "On an insulating stand it holds a charge perfectly "
                    "well."},
            {"text": "No — electrons moved, but by contact rather than by "
                     "rubbing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h08",
        "band": "harder",
        "text": "Why can a charged plastic rod hold its charge for minutes "
                "while a charged metal rod in a bare hand cannot?",
        "options": [
            {"text": "Because plastic holds more charge than metal can",
             "correct": False,
             "why": "How much it can hold is not the issue; whether the "
                    "charge can move is."},
            {"text": "Because metal repels charge and plastic attracts it",
             "correct": False,
             "why": "Neither attracts nor repels charge as a material; they "
                    "differ in whether it can travel."},
            {"text": "Because charge cannot travel through plastic, so it "
                     "stays where it was put",
             "correct": True},
            {"text": "Because plastic is lighter, so the charge has less to "
                     "move through",
             "correct": False,
             "why": "Mass has nothing to do with it; free charges are what "
                    "matter."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h09",
        "band": "harder",
        "text": "A student insists rubbing creates charge, because a neutral "
                "rod ends up charged. What single measurement settles it?",
        "options": [
            {"text": "Measure the rod again an hour later and see the charge "
                     "fade",
             "correct": False,
             "why": "Fading shows the charge leaking away, not where it came "
                    "from."},
            {"text": "Measure how hard the rod was rubbed and compare with "
                     "the charge",
             "correct": False,
             "why": "That relates size to effort; it says nothing about "
                    "whether charge was created."},
            {"text": "Measure the duster as well, and find an equal opposite "
                     "charge",
             "correct": True},
            {"text": "Measure the rod's mass before and after rubbing",
             "correct": False,
             "why": "The mass change is far too small to detect on any school "
                    "balance."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h10",
        "band": "harder",
        "text": "A photocopier charges a drum and then dusts it with fine "
                "toner powder, which sticks only where the charge is. Which "
                "physics is being used?",
        "options": [
            {"text": "The attraction between opposite charges",
             "correct": True},
            {"text": "The repulsion between like charges", "correct": False,
             "why": "Repulsion would drive the toner away from the drum "
                    "rather than hold it on."},
            {"text": "Magnetic attraction between the drum and the toner",
             "correct": False,
             "why": "The drum is charged, not magnetised, and the toner "
                    "responds to charge."},
            {"text": "Gravity pulling the toner onto the drum",
             "correct": False,
             "why": "Gravity would coat the whole drum evenly, not only the "
                    "charged parts."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h11",
        "band": "harder",
        "text": "A student claims a balloon and the jumper it was rubbed on "
                "are both negative. Why is that impossible?",
        "options": [
            {"text": "Because a jumper is a conductor and cannot be charged",
             "correct": False,
             "why": "Wool is an insulator, and it is genuinely charged — just "
                    "the other way."},
            {"text": "Because rubbing always makes both objects positive",
             "correct": False,
             "why": "It makes one of each, which is the whole point of the "
                    "transfer."},
            {"text": "Because the electrons went from one to the other, so "
                     "one is short",
             "correct": True},
            {"text": "Because two negatives would repel and fly apart",
             "correct": False,
             "why": "They would repel, but that is a consequence rather than "
                    "the reason it cannot happen."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h12",
        "band": "harder",
        "text": "Why is charging by rubbing described as SEPARATING charge "
                "rather than making it?",
        "options": [            {"text": "Because the two objects together are still neutral "
                     "afterwards",
             "correct": True},
            {"text": "Because the charge is small, so it hardly counts as "
                     "making any",
             "correct": False,
             "why": "Size is irrelevant; the total is unchanged however large "
                    "the charges are."},
            {"text": "Because the charge goes back when the objects are "
                     "parted",
             "correct": False,
             "why": "It stays where it went, which is why the rod works "
                    "minutes later."},
            {"text": "Because only electrons are involved, and they are too "
                     "small to count",
             "correct": False,
             "why": "They count exactly; every one that left is one that "
                    "arrived."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h13",
        "band": "harder",
        "text": "A charged plastic rod is cut in half. What is true of the "
                "two pieces?",
        "options": [
            {"text": "All the charge moves to one half", "correct": False,
             "why": "Charge cannot travel along an insulator, so it cannot "
                    "gather at one end."},
            {"text": "Both halves become neutral", "correct": False,
             "why": "Cutting removes nothing; the electrons stay on the "
                    "surfaces they were on."},
            {"text": "Each half keeps whatever charge was on its own surface",
             "correct": True},
            {"text": "Each half has exactly half the charge, whatever was "
                     "rubbed",
             "correct": False,
             "why": "Only if the rubbing was perfectly even, which it rarely "
                    "is on an insulator."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h14",
        "band": "harder",
        "text": "Charge builds up on a person walking across a carpet until a "
                "spark jumps to a door handle. What has happened?",
        "options": [            {"text": "The handle has become charged and reaches out to the "
                     "person",
             "correct": False,
             "why": "The handle is earthed; the charge on the person is what "
                    "drives the spark."},
            {"text": "The metal handle has attracted the carpet's electrons "
                     "directly",
             "correct": False,
             "why": "The carpet is not touching the handle, and the transfer "
                    "is from the person."},
            {"text": "The charge has run out and has to be topped up from the "
                     "handle",
             "correct": False,
             "why": "Nothing is topped up; the excess is escaping to earth."},
            {"text": "Enough charge has built up to push a current through "
                     "the air itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h15",
        "band": "harder",
        "text": "A class repeats a charging experiment on a dry January day "
                "and on a humid July one, and the July results are far "
                "weaker. What should be reported?",
        "options": [
            {"text": "That the July results are anomalous and should be "
                     "discarded",
             "correct": False,
             "why": "They are real results with a real cause; discarding them "
                    "hides what the experiment shows."},
            {"text": "That charge behaves differently in summer for reasons "
                     "unknown",
             "correct": False,
             "why": "The reason is known: damp air lets charge leak away."},
            {"text": "That humidity must be recorded, because damp air lets "
                     "charge leak away",
             "correct": True},
            {"text": "That the January apparatus must have been faulty",
             "correct": False,
             "why": "The stronger result is the one working as intended; the "
                    "damp day is what limited the other."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h16",
        "band": "harder",
        "text": "Why does rubbing two surfaces give a much bigger charge than "
                "simply pressing them together and lifting them apart?",
        "options": [            {"text": "Because rubbing brings far more points of the two "
                     "surfaces into contact",
             "correct": True},
            {"text": "Because the heat of rubbing frees extra electrons",
             "correct": False,
             "why": "Warming does not release electrons from an insulator in "
                    "any useful number."},
            {"text": "Because pressing cannot move any charge at all",
             "correct": False,
             "why": "It moves some — pressing and lifting does separate a "
                    "little charge."},
            {"text": "Because rubbing changes which material holds electrons "
                     "more tightly",
             "correct": False,
             "why": "That property belongs to the material and does not "
                    "change with handling."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h17",
        "band": "harder",
        "text": "Two students rub identical rods with different dusters and "
                "get opposite charges. What does that show?",
        "options": [
            {"text": "That one of them must have made a mistake",
             "correct": False,
             "why": "Both results can be perfectly correct, because the "
                    "dusters differed."},
            {"text": "That a rod's charge is unpredictable", "correct": False,
             "why": "It is quite predictable once you know BOTH materials "
                    "involved."},
            {"text": "That the sign depends on the pair of materials, not the "
                     "rod",
             "correct": True},
            {"text": "That rubbing sometimes moves protons instead of "
                     "electrons",
             "correct": False,
             "why": "Protons never move, whatever the two materials are."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "p9-01-e18",
        "band": "easier",
        "text": "A material sits higher up the triboelectric series than the "
                "one it is rubbed against. What happens to it?",
        "options": [
            {"text": "It loses electrons and is left positively "
                     "charged", "correct": True},
            {"text": "It gains electrons and is left negatively "
                     "charged", "correct": False,
             "why": "That is what happens to the lower material. The higher "
                    "one holds its electrons less tightly."},
            {"text": "It loses protons and is left negatively "
                     "charged", "correct": False,
             "why": "Protons stay in their nuclei, and losing them would not "
                    "leave an object negative."},
            {"text": "It stays neutral and only the lower one is "
                     "charged", "correct": False,
             "why": "Both objects change. Every electron that leaves one "
                    "arrives on the other."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e19",
        "band": "easier",
        "text": "Two materials from opposite ends of the triboelectric series "
                "are rubbed together. Compared with two that sit side by side "
                "on it, the charge produced is…",
        "options": [
            {"text": "smaller, because materials that differ so much barely "
                     "swap electrons", "correct": False,
             "why": "It is the other way round. A big difference in how "
                    "tightly the electrons are held drives more of them "
                    "across."},
            {"text": "the same, because only the number of strokes decides "
                     "the charge", "correct": False,
             "why": "Strokes matter, but so does how far apart the two "
                    "materials sit on the series."},
            {"text": "zero, because materials that far apart cannot charge "
                     "each other", "correct": False,
             "why": "They charge each other most strongly of all. Nothing "
                    "about the series stops a distant pair working."},
            {"text": "larger, because more electrons cross between "
                     "them", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e20",
        "band": "easier",
        "text": "A polythene rod is rubbed with a cotton cloth. Polythene is "
                "lower down the triboelectric series than cotton. Which "
                "object becomes negatively charged?",
        "options": [
            {"text": "The cotton cloth", "correct": False,
             "why": "Cotton is the higher of the two, so it gives electrons "
                    "up and is left positive."},
            {"text": "The polythene rod", "correct": True},
            {"text": "Both of them equally", "correct": False,
             "why": "They end up opposite, not the same. Electrons that leave "
                    "one arrive on the other."},
            {"text": "Neither of them at all", "correct": False,
             "why": "Two different insulators rubbed together always end up "
                    "charged, one each way."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e21",
        "band": "easier",
        "text": "Electrons cross at the points where two rubbed surfaces "
                "touch. What happens to those electrons once the surfaces are "
                "pulled apart again?",
        "options": [
            {"text": "They stay on the surface they crossed "
                     "to", "correct": True},
            {"text": "They travel straight back where they came "
                     "from", "correct": False,
             "why": "Nothing carries them back — both materials are "
                    "insulators, so the electrons are stuck where they "
                    "landed."},
            {"text": "They are shared out evenly between the "
                     "surfaces", "correct": False,
             "why": "Sharing would leave both objects neutral, and both are "
                    "measurably charged."},
            {"text": "They escape into the air as the gap between the "
                     "surfaces opens", "correct": False,
             "why": "Dry air is a very poor conductor, which is exactly why "
                    "the charge stays put."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e22",
        "band": "easier",
        "text": "Which object gains electrons when a glass rod and an acetate "
                "strip are rubbed together, given that glass is the higher of "
                "the two on the series?",
        "options": [
            {"text": "The glass rod, because glass is higher "
                     "up", "correct": False,
             "why": "Higher up means it holds its electrons less tightly, so "
                    "glass is the one that loses them."},
            {"text": "Both of them, from the friction between "
                     "them", "correct": False,
             "why": "Friction supplies contact, not electrons. One object "
                    "gains only what the other loses."},
            {"text": "The acetate strip", "correct": True},
            {"text": "Neither, since both are insulators", "correct": False,
             "why": "Being insulators is what makes this work: the charge "
                    "stays where the rubbing put it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e23",
        "band": "easier",
        "text": "Which of these would put the biggest charge on a polythene "
                "rod?",
        "options": [
            {"text": "Wiping it along a wet hand several "
                     "times", "correct": False,
             "why": "A wet hand conducts, so any charge separated runs "
                    "straight away through you."},
            {"text": "Rubbing it hard with a dry woollen "
                     "duster", "correct": True},
            {"text": "Rubbing it hard with a damp cotton "
                     "cloth", "correct": False,
             "why": "Damp material lets charge leak away as fast as the "
                    "rubbing separates it."},
            {"text": "Holding it close to a warm radiator", "correct": False,
             "why": "Warmth does nothing here. Charging needs two surfaces "
                    "pressed into contact and pulled apart."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e24",
        "band": "easier",
        "text": "A charged plastic rod is left lying on a bench in a damp "
                "room. What happens to its charge over the next few minutes?",
        "options": [
            {"text": "It grows, because damp air supplies extra "
                     "electrons", "correct": False,
             "why": "Air is not a store of spare electrons. Damp air takes "
                    "charge away rather than adding it."},
            {"text": "It stays exactly as it was, because plastic "
                     "insulates", "correct": False,
             "why": "Plastic does insulate, but the film of water on its "
                    "surface conducts and lets the charge go."},
            {"text": "It changes sign as water lands on the "
                     "surface", "correct": False,
             "why": "Water does not reverse a charge. It provides a route for "
                    "the charge to escape."},
            {"text": "It leaks away, because damp air lets charge "
                     "escape", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e25",
        "band": "easier",
        "text": "A rubbed rod is found to carry a charge of −4.0 nC. What "
                "charge is on the duster that rubbed it?",
        "options": [
            {"text": "−4.0 nC", "correct": False,
             "why": "Both objects cannot be negative. The electrons the rod "
                    "gained came off the duster."},
            {"text": "0.0 nC", "correct": False,
             "why": "The duster is charged too, by exactly as much as the rod "
                    "and in the opposite direction."},
            {"text": "+4.0 nC", "correct": True},
            {"text": "+8.0 nC", "correct": False,
             "why": "The two charges match in size. Nothing doubles the "
                    "duster's share."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e26",
        "band": "easier",
        "text": "A metal rod is fitted with a thick plastic handle and rubbed "
                "with a dry cloth while being held only by that handle. Can "
                "it be charged?",
        "options": [
            {"text": "Yes, because the plastic handle gives the charge no "
                     "route to earth", "correct": True},
            {"text": "No, because a metal is unable to hold any "
                     "charge", "correct": False,
             "why": "A metal holds charge perfectly well once it is insulated "
                    "from earth."},
            {"text": "No, because rubbing a metal destroys the charge it "
                     "makes", "correct": False,
             "why": "Charge is never destroyed. It simply flows away when "
                    "there is a route for it."},
            {"text": "Yes, but only while the cloth stays in contact with "
                     "it", "correct": False,
             "why": "The charge stays behind after the cloth is taken away, "
                    "which is the whole point."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e27",
        "band": "easier",
        "text": "In this topic, what does calling a material an insulator "
                "tell you about it?",
        "options": [
            {"text": "It contains no electrons of its own", "correct": False,
             "why": "It is full of electrons. They are just held in place "
                    "instead of being free to travel."},
            {"text": "Its electrons are free to move about inside it, so a "
                     "rubbed charge spreads out over it", "correct": False,
             "why": "That describes a conductor, which is why a conductor "
                    "cannot hold a rubbed charge."},
            {"text": "Charge cannot travel through it, so it stays where the "
                     "rubbing put it", "correct": True},
            {"text": "It cannot be given any charge at all", "correct": False,
             "why": "Insulators are the only things rubbing does charge. "
                    "Conductors are the awkward ones."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e28",
        "band": "easier",
        "text": "Rubbing two insulators together changes several things. "
                "Which of these does it leave exactly as it was?",
        "options": [
            {"text": "How many electrons sit on each object", "correct": False,
             "why": "This is the thing that does change: one object ends up "
                    "with more and the other with fewer."},
            {"text": "How many protons sit in each object", "correct": True},
            {"text": "Whether each object will lift a scrap of "
                     "paper", "correct": False,
             "why": "Before rubbing neither would; afterwards both will, "
                    "because both are charged."},
            {"text": "Whether each object is positive or "
                     "negative", "correct": False,
             "why": "Both start neutral and end charged, one each way, so "
                    "this changes for both of them."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e29",
        "band": "easier",
        "text": "What do you need if rubbing is going to charge something?",
        "options": [
            {"text": "Two pieces of the same insulator, both of them "
                     "dry", "correct": False,
             "why": "Identical materials hold their electrons equally "
                    "tightly, so none of them cross."},
            {"text": "An insulator and a metal rod held in the bare "
                     "hand", "correct": False,
             "why": "The metal and your hand conduct, so the charge runs away "
                    "as fast as it is separated."},
            {"text": "Two different insulators, both of them "
                     "dry", "correct": True},
            {"text": "Two different insulators, one of them slightly "
                     "damp", "correct": False,
             "why": "A damp surface conducts, so the charge leaks off before "
                    "it can build up."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-e30",
        "band": "easier",
        "text": "Wool holds its electrons less tightly than PVC does. After a "
                "PVC pipe has been rubbed with a wool duster, the duster is…",
        "options": [
            {"text": "negatively charged, having collected "
                     "electrons", "correct": False,
             "why": "The wool is the looser of the two, so it gives electrons "
                    "away rather than collecting them."},
            {"text": "positively charged, having given electrons "
                     "away", "correct": True},
            {"text": "still neutral, since cloth cannot hold a "
                     "charge", "correct": False,
             "why": "Wool is an insulator and holds a charge perfectly well — "
                    "it is charged as much as the pipe is."},
            {"text": "charged, but too weakly for a sign to be "
                     "given", "correct": False,
             "why": "The sign is set by which material holds electrons more "
                    "tightly, whatever the size of the charge."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p9-01-s18",
        "band": "standard",
        "text": "Acetate and PVC sit at opposite ends of a classroom set of "
                "materials, while wool and cotton sit side by side in it. "
                "Each pair is rubbed with the same number of strokes. Which "
                "pair ends up more strongly charged?",
        "options": [
            {"text": "The wool and the cotton, because similar materials "
                     "trade electrons more readily", "correct": False,
             "why": "Similar materials hold their electrons about equally "
                    "tightly, so very few of them cross."},
            {"text": "The acetate and the PVC, because they sit further apart "
                     "on the series", "correct": True},
            {"text": "Both pairs the same, because both were given the same "
                     "number of strokes", "correct": False,
             "why": "Strokes are only half of it. How far apart the materials "
                    "sit matters just as much."},
            {"text": "The wool and the cotton, because natural fibres charge "
                     "better than plastics", "correct": False,
             "why": "Being natural has nothing to do with it. Position on the "
                    "series is what decides the transfer."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s19",
        "band": "standard",
        "text": "An acetate strip is rubbed with a polythene rod, and acetate "
                "is the higher of the two on the triboelectric series. "
                "Predict what charge each of them ends up with.",
        "options": [
            {"text": "Acetate positive and polythene "
                     "negative", "correct": True},
            {"text": "Acetate negative and polythene "
                     "positive", "correct": False,
             "why": "That is the transfer the wrong way round. The higher "
                    "material is the one that loses electrons."},
            {"text": "Both of them negative, since rubbing adds "
                     "electrons", "correct": False,
             "why": "Rubbing adds nothing. It only moves electrons that were "
                    "already on the two objects."},
            {"text": "Acetate charged and polythene left "
                     "neutral", "correct": False,
             "why": "Whatever one object loses the other gains, so the two "
                    "always end up charged together."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s20",
        "band": "standard",
        "text": "A rod given eight strokes ends up at −2.4 nC. It is then "
                "given eight more strokes in exactly the same way. Which "
                "final charge is most likely?",
        "options": [
            {"text": "Exactly −4.8 nC, since the strokes have "
                     "doubled", "correct": False,
             "why": "The gain per stroke gets smaller as the charge builds, "
                    "so it never quite doubles."},
            {"text": "About −3.7 nC", "correct": True},
            {"text": "About −1.2 nC, as the charge spreads over more "
                     "strokes", "correct": False,
             "why": "More rubbing separates more charge. Nothing spreads it "
                    "thinner."},
            {"text": "About −9.6 nC, because each stroke adds more than the "
                     "last", "correct": False,
             "why": "Each stroke adds less than the one before, not more — "
                    "the charge is levelling off."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s21",
        "band": "standard",
        "text": "A student charges a polythene rod along its whole length, "
                "then runs a finger along one end of it. The other end still "
                "lifts paper. What does that show?",
        "options": [
            {"text": "The whole rod was discharged, and friction is lifting "
                     "the paper now", "correct": False,
             "why": "Friction cannot lift paper across a gap. The far end is "
                    "still charged."},
            {"text": "Charge cannot move along polythene, so only the part "
                     "touched was discharged", "correct": True},
            {"text": "Charge creeps slowly along an insulator, so the far end "
                     "will go in a moment", "correct": False,
             "why": "It will not. Charge on an insulator stays exactly where "
                    "it was put."},
            {"text": "Only the inside of the rod was charged, and the finger "
                     "took the outside", "correct": False,
             "why": "Rubbing charges the surface, and the finger removed the "
                    "surface charge it touched and no more."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s22",
        "band": "standard",
        "text": "One wool duster is used first on a polythene rod and then on "
                "a glass rod. Wool sits below glass but above polythene on "
                "the series. What charge does the duster end up with each "
                "time?",
        "options": [
            {"text": "Positive after the polythene, then negative after the "
                     "glass", "correct": True},
            {"text": "Negative after the polythene, then positive after the "
                     "glass", "correct": False,
             "why": "The signs are the wrong way round: wool loses electrons "
                    "to polythene and gains them from glass."},
            {"text": "Positive both times, because wool gives electrons up to "
                     "anything", "correct": False,
             "why": "Wool gives electrons up only to a material below it. "
                    "Glass is above it."},
            {"text": "Negative both times, because wool collects electrons "
                     "from anything", "correct": False,
             "why": "Wool collects electrons only from a material above it, "
                    "and polythene is below."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s23",
        "band": "standard",
        "text": "A student wants the largest charge they can get on a rod. "
                "Which set of choices is best?",
        "options": [
            {"text": "Two materials side by side on the series, dry, with "
                     "many strokes", "correct": False,
             "why": "Materials close together barely differ in how tightly "
                    "they hold electrons, so little crosses."},
            {"text": "Two materials far apart on the series, dry, with many "
                     "strokes", "correct": True},
            {"text": "Two materials far apart on the series, slightly damp, "
                     "with many strokes", "correct": False,
             "why": "Damp surfaces conduct, so the charge leaks off as fast "
                    "as it is separated."},
            {"text": "Two pieces of one material, dry, with as many strokes "
                     "as possible", "correct": False,
             "why": "Identical materials hold their electrons equally "
                    "tightly, so no strokes will charge them."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s24",
        "band": "standard",
        "text": "Waving a duster about a centimetre from a rod, without ever "
                "touching it, leaves the rod uncharged. Why must the rubbing "
                "be done in contact?",
        "options": [
            {"text": "Moving air strips the charge off the rod as fast as it "
                     "is separated", "correct": False,
             "why": "No charge is separated in the first place, so there is "
                    "nothing for the air to strip."},
            {"text": "The air in the gap soaks up any electrons that try to "
                     "cross over it", "correct": False,
             "why": "Dry air is a very poor conductor and absorbs nothing of "
                    "the sort."},
            {"text": "Electrons only cross where the two surfaces genuinely "
                     "touch", "correct": True},
            {"text": "The duster must be warmed by friction before it gives "
                     "electrons up", "correct": False,
             "why": "Warmth plays no part. What matters is surfaces pressed "
                    "together and pulled apart."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s25",
        "band": "standard",
        "text": "Investigating how the charge depends on the number of "
                "strokes, one group uses wool on polythene and another uses "
                "cotton on polythene. Their results disagree. What is the "
                "problem?",
        "options": [
            {"text": "One group must have counted its strokes "
                     "wrongly", "correct": False,
             "why": "Both counts can be perfectly correct and the results "
                    "still differ, because the cloths differ."},
            {"text": "Nothing — different groups are expected to "
                     "disagree", "correct": False,
             "why": "A disagreement with a known cause is a fault in the "
                    "design, not a result to accept."},
            {"text": "They changed the pair of materials as well as the "
                     "strokes, so the results cannot be "
                     "compared", "correct": True},
            {"text": "Cotton cannot charge polythene, so that group's "
                     "readings are meaningless and ought to be thrown "
                     "out", "correct": False,
             "why": "Cotton does charge polythene — it sits above it on the "
                    "series — just less strongly than wool."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s26",
        "band": "standard",
        "text": "A charged polythene rod is pressed firmly against a second "
                "polythene rod that has never been rubbed. What happens?",
        "options": [
            {"text": "The charge spreads itself out evenly over both of the "
                     "rods until the two carry the same "
                     "amount", "correct": False,
             "why": "Charge spreads out over a metal, which conducts. It "
                    "cannot travel through polythene."},
            {"text": "Almost nothing moves, because charge cannot flow along "
                     "an insulator", "correct": True},
            {"text": "All of the charge crosses onto the second "
                     "rod", "correct": False,
             "why": "There is no route for it to travel along, and no reason "
                    "for it to prefer the other rod."},
            {"text": "Both rods are left neutral, as the charges cancel "
                     "out", "correct": False,
             "why": "The second rod has no charge to cancel the first one "
                    "with; it is neutral to start with."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s27",
        "band": "standard",
        "text": "A rod wiped with a clean dry cloth first charges strongly, "
                "while an identical rod taken straight from a dusty drawer "
                "charges far more weakly. Suggest why.",
        "options": [
            {"text": "Dust adds extra protons to the rod's "
                     "surface", "correct": False,
             "why": "Protons never move between objects, and nothing adds "
                    "them to a surface."},
            {"text": "Dirt on the surface changes how the two materials meet "
                     "and hold their electrons", "correct": True},
            {"text": "A layer of dust turns the rod into a conductor, so any "
                     "charge separated runs straight off it", "correct": False,
             "why": "A layer of dust does not turn polythene into a "
                    "conductor; the rod charges, just less well."},
            {"text": "Dust makes the rod heavier, so more strokes are "
                     "needed", "correct": False,
             "why": "Mass has nothing to do with how many electrons cross "
                    "between two surfaces."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s28",
        "band": "standard",
        "text": "A long strip of plastic film is pulled quickly off a roll. "
                "It crackles, and afterwards it is charged, although nobody "
                "rubbed it. How was the charge separated?",
        "options": [
            {"text": "Stretching the film as it is pulled creates charge "
                     "inside it", "correct": False,
             "why": "Stretching creates nothing. Charge is only ever moved "
                    "from one surface to another."},
            {"text": "The two layers were pressed together on the roll and "
                     "then peeled apart", "correct": True},
            {"text": "Air rushing past the film carries electrons onto "
                     "it", "correct": False,
             "why": "Air is a very poor conductor and is not a supply of "
                    "spare electrons."},
            {"text": "The speed of the pull heats the film and frees "
                     "electrons in it", "correct": False,
             "why": "Warming an insulator does not release electrons in any "
                    "useful number."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s29",
        "band": "standard",
        "text": "A PVC pipe and an acetate strip are each rubbed with the "
                "same cotton cloth. Cotton sits between the two of them on "
                "the series. What charges do the pipe and the strip end up "
                "with?",
        "options": [
            {"text": "Both of them positive", "correct": False,
             "why": "Cotton is above acetate but below PVC, so the two rods "
                    "cannot come out the same way."},
            {"text": "The PVC positive and the acetate "
                     "negative", "correct": False,
             "why": "The signs are reversed: PVC is below cotton, so PVC "
                    "gains electrons and the acetate loses them."},
            {"text": "The PVC negative and the acetate "
                     "positive", "correct": True},
            {"text": "Both of them negative", "correct": False,
             "why": "Acetate sits above cotton, so acetate gives electrons up "
                    "and comes out positive."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-s30",
        "band": "standard",
        "text": "With no meter available, how could you compare the charge on "
                "a rod after five strokes with the charge after fifteen?",
        "options": [
            {"text": "Measure how much warmer the rod has become after each "
                     "of the rubbings", "correct": False,
             "why": "Warmth from friction tells you about the rubbing, not "
                    "about how much charge was separated."},
            {"text": "Count how many small scraps of paper each one "
                     "lifts", "correct": True},
            {"text": "Look for a glow on the surface of the "
                     "rod", "correct": False,
             "why": "A rubbed rod gives off no light at these charges; there "
                    "is nothing to see."},
            {"text": "Compare how quickly each rod cools "
                     "afterwards", "correct": False,
             "why": "Cooling depends on the rod and the room, and says "
                    "nothing about its charge."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ────────────────────────────────────────
    {
        "id": "p9-01-h18",
        "band": "harder",
        "text": "A new plastic is tested. Rubbed with wool it comes out "
                "negative, and rubbed with polythene it comes out positive. "
                "Where does it belong on the series?",
        "options": [
            {"text": "Above both wool and polythene", "correct": False,
             "why": "Above wool it would lose electrons to wool and come out "
                    "positive, not negative."},
            {"text": "Below wool but above polythene", "correct": True},
            {"text": "Below both wool and polythene", "correct": False,
             "why": "Below polythene it would take electrons from polythene "
                    "and come out negative, not positive."},
            {"text": "Level with wool, since it takes the opposite charge to "
                     "it", "correct": False,
             "why": "Two materials level with each other would swap no "
                    "electrons and neither would be charged."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h19",
        "band": "harder",
        "text": "A polythene rod holds something like a million million "
                "million million electrons, and rubbing moves about ten "
                "thousand million of them. What does that tell you?",
        "options": [
            {"text": "Only a tiny fraction of the rod's electrons take "
                     "part", "correct": True},
            {"text": "The rod has given up most of the electrons it "
                     "held", "correct": False,
             "why": "It has given up a fantastically small share of them — "
                    "the count that crosses is far smaller."},
            {"text": "The rod is close to running out of electrons "
                     "entirely", "correct": False,
             "why": "It is nowhere near. Rubbing touches only the outermost "
                    "layer of atoms."},
            {"text": "The rod's material has been chemically changed by the "
                     "rubbing", "correct": False,
             "why": "No new substance is made. The polythene is the same "
                    "material, with a slight imbalance of charge."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h20",
        "band": "harder",
        "text": "Objects A, B and C all start neutral. A is rubbed with B, "
                "and then B is rubbed with C. A is left at +2.0 nC and C at "
                "−5.0 nC. What charge is B left with?",
        "options": [
            {"text": "−3.0 nC", "correct": False,
             "why": "Add the three charges and you would get −6.0 nC, but the "
                    "total has to come back to zero."},
            {"text": "+3.0 nC", "correct": True},
            {"text": "−7.0 nC", "correct": False,
             "why": "That is A and C subtracted rather than added; the three "
                    "charges must sum to zero."},
            {"text": "+7.0 nC", "correct": False,
             "why": "The three together would then be +4.0 nC, and nothing "
                    "created any charge."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h21",
        "band": "harder",
        "text": "Flour is blown along a long plastic pipe into a silo, and a "
                "large charge builds up on the pipe. The firm is told to fit "
                "an earthed metal pipe instead. Explain why that helps.",
        "options": [
            {"text": "Metal does not rub against flour, so no charge is "
                     "separated at all", "correct": False,
             "why": "Flour rubs against metal just as it does against "
                    "plastic. The difference is what happens next."},
            {"text": "Metal conducts, so the separated charge runs to earth "
                     "instead of building up", "correct": True},
            {"text": "Earthing destroys the charge at the moment it is "
                     "separated", "correct": False,
             "why": "Charge is never destroyed. Earthing gives it somewhere "
                    "to go."},
            {"text": "Metal stores charge far better than plastic does, so it "
                     "holds the charge safely out of harm's "
                     "way", "correct": False,
             "why": "An earthed metal pipe stores nothing — that is exactly "
                    "the point of earthing it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h22",
        "band": "harder",
        "text": "A student records the charge after 5, 10, 15 and 20 strokes "
                "as 1.8, 3.2, 4.2 and 4.8 nC, and draws a straight line "
                "through the four points. Evaluate that.",
        "options": [
            {"text": "The rises are 1.4, 1.0 and 0.6 nC, so a curve that "
                     "flattens off fits far better", "correct": True},
            {"text": "A straight line fits, because the charge rises every "
                     "time", "correct": False,
             "why": "Rising is not enough for a straight line; the rises have "
                    "to be equal, and these are not."},
            {"text": "A straight line fits, because the strokes went up in "
                     "equal steps", "correct": False,
             "why": "Equal steps along the bottom are what let you see that "
                    "the rises are getting smaller."},
            {"text": "The last reading is anomalous and ought to be left "
                     "out", "correct": False,
             "why": "It is exactly what the levelling-off predicts, so it is "
                    "the most telling reading of the four."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h23",
        "band": "harder",
        "text": "After rubbing, a rod measures −8.0 nC and the duster that "
                "rubbed it measures +6.0 nC. What is the most likely "
                "explanation?",
        "options": [
            {"text": "The rod took more electrons off the duster than the "
                     "duster actually gave up to it", "correct": False,
             "why": "Every electron on the rod came off the duster, so the "
                    "two counts cannot differ."},
            {"text": "Some charge has leaked off the duster, since the two "
                     "ought to match", "correct": True},
            {"text": "Charge was created on the rod as well as "
                     "separated", "correct": False,
             "why": "Charge is never created. An imbalance in the readings "
                    "means some of it has gone somewhere."},
            {"text": "Protons moved from the duster across onto the "
                     "rod", "correct": False,
             "why": "Protons are locked in nuclei and take no part in any of "
                    "this."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h24",
        "band": "harder",
        "text": "Could you strip every electron off a rod by rubbing it for "
                "long enough?",
        "options": [
            {"text": "Yes, given enough strokes and a dry enough "
                     "room", "correct": False,
             "why": "The charge levels off long before that, however dry the "
                    "room and however long you rub."},
            {"text": "No — the charge levels off, leaking away as fast as "
                     "more of it is separated", "correct": True},
            {"text": "Yes, but only with two materials from opposite ends of "
                     "the series", "correct": False,
             "why": "A distant pair separates more charge, and it still "
                    "levels off at a ceiling."},
            {"text": "No, because rubbing stops working as soon as the rod "
                     "has taken on some charge of its own", "correct": False,
             "why": "Rubbing keeps working; each stroke simply adds less than "
                    "the one before it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h25",
        "band": "harder",
        "text": "Two identical polythene rods are rubbed the same number of "
                "times, one with a wool duster and one with a cotton cloth. "
                "Wool sits two places above polythene on the series and "
                "cotton one place. Which rod ends up more strongly charged?",
        "options": [
            {"text": "The one rubbed with wool", "correct": True},
            {"text": "The one rubbed with cotton", "correct": False,
             "why": "Cotton is only one place from polythene, so fewer "
                    "electrons cross than with wool."},
            {"text": "Both the same, since the strokes were the "
                     "same", "correct": False,
             "why": "Equal strokes are only half the story; the gap between "
                    "the materials matters too."},
            {"text": "Neither, because cotton cannot charge "
                     "polythene", "correct": False,
             "why": "Cotton sits above polythene, so it does charge it — just "
                    "less strongly than wool does."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h26",
        "band": "harder",
        "text": "A charged rod slowly loses its charge overnight, and a "
                "student writes that the charge has been used up. Why is \"it "
                "leaked away into the air\" the better statement?",
        "options": [
            {"text": "The two statements come to the same thing in the "
                     "end", "correct": False,
             "why": "They do not. One says charge can vanish, and the other "
                    "says it went somewhere."},
            {"text": "Charge is never used up; it has moved onto the air and "
                     "the surroundings", "correct": True},
            {"text": "Charge is used up whenever it does the work of lifting "
                     "paper", "correct": False,
             "why": "Lifting paper uses energy, not charge. The charge on the "
                    "rod is unchanged by it."},
            {"text": "The charge has turned back into the electrons that it "
                     "was made out of in the first place", "correct": False,
             "why": "Charge was never made from anything. The electrons were "
                    "there the whole time."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h27",
        "band": "harder",
        "text": "Charging something by rubbing needs insulators, while "
                "getting rid of unwanted static needs conductors. Which "
                "statement explains both?",
        "options": [
            {"text": "Insulators make charge and conductors destroy "
                     "it", "correct": False,
             "why": "Neither makes nor destroys charge. Both only affect "
                    "whether it can travel."},
            {"text": "Insulators hold on to their electrons, while conductors "
                     "have no electrons of their own to "
                     "hold", "correct": False,
             "why": "Conductors are full of electrons; theirs are simply free "
                    "to move."},
            {"text": "Whether charge can travel through a material decides "
                     "whether it stays or escapes", "correct": True},
            {"text": "Conductors are easier to rub than insulators "
                     "are", "correct": False,
             "why": "How easily something is rubbed is not the issue; where "
                    "the charge can go afterwards is."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h28",
        "band": "harder",
        "text": "How does the movement of electrons when a rod is charged by "
                "rubbing differ from the movement of electrons in a wire "
                "carrying a current?",
        "options": [
            {"text": "Protons move as well as electrons on the rod, while "
                     "only electrons move in the wire", "correct": False,
             "why": "Protons move in neither case. They are held in nuclei in "
                    "both."},
            {"text": "On the rod they cross once and stay put; in the wire "
                     "they keep flowing round", "correct": True},
            {"text": "Nothing really moves on the rod, while electrons do "
                     "move in the wire", "correct": False,
             "why": "Electrons genuinely cross between the surfaces; that is "
                    "what leaves the rod charged."},
            {"text": "They are the same, except that the rod's electrons "
                     "travel faster", "correct": False,
             "why": "They are not the same: a current keeps going, while a "
                    "rubbed charge sits where it landed."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h29",
        "band": "harder",
        "text": "Why is it especially worth repeating this experiment several "
                "times and taking a mean?",
        "options": [
            {"text": "A single result would not be allowed in any science "
                     "experiment", "correct": False,
             "why": "Plenty of measurements are trustworthy first time. This "
                    "one is not, and there is a reason why."},
            {"text": "The charge varies a good deal from try to try with the "
                     "surfaces and the air", "correct": True},
            {"text": "The rod needs several rubbings before it will take any "
                     "charge", "correct": False,
             "why": "A rod charges on the first stroke; repeats are about the "
                    "spread in the readings."},
            {"text": "The charge is too small to be read at all the first "
                     "time round", "correct": False,
             "why": "It is readable straight away. The trouble is that the "
                    "reading is not reliably the same twice."},
        ],
        "figure": None,
    },
    {
        "id": "p9-01-h30",
        "band": "harder",
        "text": "A duster is rubbed on rod A and loses sixty thousand million "
                "electrons, then rubbed on rod B and loses forty thousand "
                "million more. How does the duster's charge compare with rod "
                "A's?",
        "options": [
            {"text": "The duster's positive charge is the larger of the "
                     "two", "correct": True},
            {"text": "They are equal, since the duster rubbed rod A "
                     "first", "correct": False,
             "why": "They matched after the first rubbing, and the second one "
                    "took the duster further from neutral."},
            {"text": "The duster's charge is the smaller, having lost "
                     "electrons twice", "correct": False,
             "why": "Losing electrons twice leaves it further from neutral, "
                    "so its charge is bigger."},
            {"text": "The duster's charge is zero, as the two rubbings cancel "
                     "out", "correct": False,
             "why": "Both rubbings took electrons off the duster in the same "
                    "direction, so they add."},
        ],
        "figure": None,
    },
]
