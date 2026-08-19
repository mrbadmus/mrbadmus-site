"""B5 lesson 05 — Lifestyle and the developing foetus: twelve questions (MRB-269).

These probe the one claim the lesson is built on — that the placenta is an
exchange surface and not a filter, so what reaches a foetus is decided by the
size and solubility of the molecule and by nothing else. The distractors are
built from the lesson's two declared misconceptions, REPRO-09 (the placenta
filters out anything harmful) and REPRO-10 (so anything that goes wrong is the
mother's fault), and from the third belief the page confronts without minting:
that crossing the placenta and doing harm are the same claim. Around those sit
the wrong ideas a Year 8 class actually produces on this page — that the two
blood supplies mix, that a virus dissolves and diffuses like alcohol does, that
a prescribed medicine is admitted because it is prescribed, that insulin being
held back means diabetes stops mattering, and that a raised risk is a
prediction about one pregnancy rather than a proportion across many. The
register follows the lesson's tone gate: third person throughout, no dose or
threshold beyond the two figures the page itself states, no advice, and nothing
anywhere that addresses the reader as pregnant.

`figure` is `None` on all twelve: the lesson's only figure record,
`b5-what-crosses`, is `status: "retired"`, so no artwork exists or will.
"""

UNIT = "B5"
LESSON = "lifestyle-and-the-developing-foetus"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-05-e01",
        "band": "easier",
        "text": "Weeks 3–8 of a pregnancy are called the embryo stage, and "
                "weeks 9–40 the foetus stage. What has changed by the time "
                "the foetus stage begins?",
        "options": [
            {"text": "Nothing has changed — embryo and foetus are two words "
                     "for the same stage of development.",
             "correct": False,
             "why": "They name different stages. Embryo is while the organs "
                    "are being laid down; foetus is from about week nine, "
                    "once those organs exist."},
            {"text": "The organs are still forming, but the developing "
                     "organism is now big enough to be seen.",
             "correct": False,
             "why": "Forming is largely over by week eight. The change of "
                    "name marks a change of job — from building organs to "
                    "growing and maturing them."},
            {"text": "The placenta has finished forming, which is what the "
                     "change of name is describing.",
             "correct": False,
             "why": "The name describes the developing organism, not the "
                    "placenta. The placenta starts being built in the first "
                    "two weeks, well before either stage."},
            {"text": "The organs have been laid down; from week nine they "
                     "grow and mature rather than form.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e02",
        "band": "easier",
        "text": "Insulin does not reach a foetus in any useful amount. What "
                "is the reason for that?",
        "options": [
            {"text": "The placenta recognises it as a medicine and keeps it "
                     "out of the foetus's blood.",
             "correct": False,
             "why": "The placenta recognises nothing at all. Insulin is held "
                    "back by its own size, not by any decision the placenta "
                    "makes about it."},
            {"text": "It is broken down by the placenta before it can get "
                     "across to the other side.",
             "correct": False,
             "why": "The placenta is not breaking anything down. It is a "
                    "surface for exchange, and insulin's molecules are simply "
                    "too big to cross it."},
            {"text": "It is a protein, and protein molecules are far too "
                     "large to cross an exchange surface.",
             "correct": True},
            {"text": "It does not dissolve in blood, so there is nothing for "
                     "it to diffuse through.",
             "correct": False,
             "why": "Insulin travels dissolved in the blood perfectly well. "
                    "Size is what stops it — which is exactly why it can "
                    "treat diabetes during pregnancy."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e03",
        "band": "easier",
        "text": "Carbon monoxide from tobacco smoke reaches the blood of "
                "someone who is pregnant. What does it do once it is there?",
        "options": [
            {"text": "It dissolves into the blood and thickens it, so the "
                     "blood flows to the placenta more slowly.",
             "correct": False,
             "why": "Nothing thickens. Carbon monoxide takes up seats on "
                    "haemoglobin that oxygen would otherwise be using, so "
                    "less oxygen is carried."},
            {"text": "It is too large to cross the placenta, so only the "
                     "mother is affected by it at all.",
             "correct": False,
             "why": "Carbon monoxide is a small molecule and crosses easily. "
                    "The problem it causes is a shortage of oxygen, and that "
                    "shortage reaches the foetus."},
            {"text": "It binds to haemoglobin far more tightly than oxygen "
                     "does, so the blood carries less oxygen.",
             "correct": True},
            {"text": "It infects the cells of the placenta directly, which is "
                     "what makes birth weight lower.",
             "correct": False,
             "why": "That is how rubella gets across, not how carbon monoxide "
                    "works. It occupies haemoglobin, and a foetus short of "
                    "oxygen grows more slowly."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e04",
        "band": "easier",
        "text": "The placenta is often described as a barrier. Why is that "
                "word misleading?",
        "options": [
            {"text": "It suggests something that decides what to admit, and "
                     "the placenta sorts nothing at all.",
             "correct": True},
            {"text": "It suggests the two blood supplies stay separate, when "
                     "in fact they mix inside the placenta.",
             "correct": False,
             "why": "The two circulations really are separate and never mix — "
                    "that much is right. What is wrong is the idea that the "
                    "surface between them chooses what crosses."},
            {"text": "It suggests the placenta is thin, when it is really a "
                     "thick wall of tissue between the two.",
             "correct": False,
             "why": "The placenta is a very thin, very large surface, and it "
                    "has to be, so oxygen and glucose arrive as fast as a "
                    "growing organism uses them."},
            {"text": "Nothing is misleading about it — the placenta does keep "
                     "harmful substances such as alcohol out.",
             "correct": False,
             "why": "It keeps nothing out. Alcohol is small and dissolves in "
                    "blood, so it crosses within minutes and reaches roughly "
                    "the concentration the mother has."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-05-s01",
        "band": "standard",
        "text": "A rubella virus particle is enormous compared with a "
                "molecule of alcohol, and far too big to diffuse anywhere. It "
                "still reaches the embryo. How?",
        "options": [
            {"text": "It dissolves in the blood plasma, and anything that "
                     "is dissolved in blood can diffuse across the surface.",
             "correct": False,
             "why": "Dissolving is not the issue — a virus particle is far "
                    "too large to diffuse. Rubella crosses by infecting the "
                    "placenta's own cells instead."},
            {"text": "It infects the placenta's own cells and is made again "
                     "on the other side, cell by cell.",
             "correct": True},
            {"text": "It passes through gaps in the placenta, where the "
                     "mother's blood and the foetus's blood meet.",
             "correct": False,
             "why": "The two blood supplies never meet, and there are no such "
                    "gaps. Rubella gets across by infecting the placenta's "
                    "cells and being rebuilt on the other side."},
            {"text": "The placenta carries it across using energy, in the "
                     "same way that it carries antibodies over.",
             "correct": False,
             "why": "Antibodies really are carried across deliberately, at a "
                    "cost in energy. Rubella is not carried — it infects the "
                    "placenta's cells and is copied through them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s02",
        "band": "standard",
        "text": "A substance interferes with how an organ is built. In which "
                "window of a pregnancy would it do the most structural "
                "damage, and why?",
        "options": [
            {"text": "Weeks 1–2, because the ball of cells is at its smallest "
                     "then and most easily damaged.",
             "correct": False,
             "why": "There are no organs yet in weeks 1–2 — the cells are "
                    "dividing, implanting and building the placenta. An "
                    "exposure then tends either to have no lasting effect or "
                    "to stop the pregnancy continuing."},
            {"text": "Weeks 9–40, because that window is much the longest and "
                     "covers most of the pregnancy.",
             "correct": False,
             "why": "By week nine the organs already exist. Weeks 9–40 affect "
                    "growth and function — birth weight, lung readiness, "
                    "brain development — not how an organ is built."},
            {"text": "The final weeks, because the foetus is largest then and "
                     "takes the most across the placenta.",
             "correct": False,
             "why": "Demand really is highest late on, but the structures "
                    "were built long before. Structure is settled in weeks "
                    "three to eight."},
            {"text": "Weeks 3–8, because the heart, brain, spine, limbs, eyes "
                     "and ears are all laid down then.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s03",
        "band": "standard",
        "text": "Alcohol reaches roughly the same concentration in a foetus's "
                "blood as in the mother's. Why does it then stay in the "
                "foetus's blood for longer?",
        "options": [
            {"text": "The foetus's liver is much less developed, so it breaks "
                     "the alcohol down far more slowly.",
             "correct": True},
            {"text": "The placenta lets alcohol in but will not let it back "
                     "out again the other way.",
             "correct": False,
             "why": "Diffusion across the surface works both ways. What "
                    "differs is the breakdown: the foetus's liver is nothing "
                    "like as developed as the mother's."},
            {"text": "More alcohol crosses than can fit back, so it builds up "
                     "to a higher concentration than the mother's.",
             "correct": False,
             "why": "The two concentrations end up roughly equal, not higher "
                    "on the foetal side. What keeps it there longer is a "
                    "liver that cannot yet break it down quickly."},
            {"text": "The foetus has no circulation yet, so nothing that "
                     "arrives can be carried away again.",
             "correct": False,
             "why": "The foetus has its own circulation — that is what the "
                    "placenta exchanges with. The delay comes from the "
                    "undeveloped liver, not from still blood."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s04",
        "band": "standard",
        "text": "Someone taking medicine for epilepsy becomes pregnant, and "
                "learns that the medicine crosses the placenta. What follows "
                "from that fact on its own?",
        "options": [
            {"text": "That it should be stopped at once, because a medicine "
                     "that crosses the placenta must do harm.",
             "correct": False,
             "why": "Crossing does not settle it. An untreated seizure can be "
                    "far more dangerous to a pregnancy than the medicine that "
                    "prevents it, and nobody should stop a prescribed "
                    "medicine on their own."},
            {"text": "Very little on its own — the risk of untreated "
                     "epilepsy has to be weighed against it.",
             "correct": True},
            {"text": "That the placenta will keep most of it out, because "
                     "prescribed medicines are tested as safe.",
             "correct": False,
             "why": "The placenta does not sort by whether something is "
                    "prescribed. Whether a medicine crosses depends on the "
                    "size and solubility of its molecules and nothing else."},
            {"text": "That it should be swapped for any medicine that does "
                     "not cross, whatever that medicine treats.",
             "correct": False,
             "why": "A medicine that does not cross but does not control the "
                    "epilepsy leaves the seizures untreated. Each one is "
                    "judged against what it is preventing."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-05-h01",
        "band": "harder",
        "text": "Rubella matters most in the first twelve weeks, while carbon "
                "monoxide matters mostly across the second half of a "
                "pregnancy. What explains the difference?",
        "options": [
            {"text": "Rubella damages organs while they are being formed; "
                     "carbon monoxide limits oxygen supply, and supply shows "
                     "up in growth.",
             "correct": True},
            {"text": "Rubella is a virus, and a virus can only survive in the "
                     "earliest weeks of a pregnancy, before the foetus "
                     "stage.",
             "correct": False,
             "why": "Rubella does not stop existing at week twelve. Its "
                    "window is early because the eyes, ears and heart are "
                    "formed early, and that forming is largely over by week "
                    "eight."},
            {"text": "Carbon monoxide needs several months of exposure to "
                     "build up to a level high enough to have any effect at "
                     "all.",
             "correct": False,
             "why": "It acts the moment it is breathed in, by occupying "
                    "haemoglobin. Its window is late because a shortage of "
                    "oxygen limits growth, and growth is the second half's "
                    "business."},
            {"text": "The placenta thickens as a pregnancy goes on, so "
                     "viruses stop crossing it while small molecules still "
                     "get through.",
             "correct": False,
             "why": "The placenta does not start sorting halfway through. The "
                    "two differ because one damages structures being built "
                    "and the other starves a built organism of oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h02",
        "band": "harder",
        "text": "A student writes: “Caffeine crosses the placenta, so any "
                "amount of caffeine harms a foetus.” Where does that argument "
                "go wrong?",
        "options": [
            {"text": "In the first half — caffeine is broken down in the "
                     "mother's liver and does not actually cross at all.",
             "correct": False,
             "why": "It crosses easily, and the foetus breaks it down slowly. "
                    "The error is in the second half, where crossing is "
                    "treated as the same claim as harming."},
            {"text": "In the second half — crossing the placenta and being "
                     "harmful at a given amount are two separate claims.",
             "correct": True},
            {"text": "Nowhere — anything that reaches a foetus does it harm, "
                     "which is why there is guidance on caffeine at all.",
             "correct": False,
             "why": "If that were true the guidance would be a ban, not a "
                    "limit. Whether a substance does harm, and at what "
                    "amount, has to be established separately from whether it "
                    "crosses."},
            {"text": "In both halves — caffeine neither crosses the placenta "
                     "nor has any effect at all on a pregnancy.",
             "correct": False,
             "why": "Caffeine does cross, and high intake is associated with "
                    "reduced growth. The only faulty step is the leap from "
                    "crossing to harm at any amount."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h03",
        "band": "harder",
        "text": "Insulin's molecules are far too large to reach a foetus. Why "
                "does controlling the blood glucose of a pregnant person with "
                "diabetes still matter a great deal?",
        "options": [
            {"text": "Because a small amount of the insulin does cross in "
                     "the end, and that amount is enough on its own.",
             "correct": False,
             "why": "Insulin does not arrive in any useful amount — that is "
                    "the whole reason it can be used as the treatment. What "
                    "does arrive is glucose."},
            {"text": "Glucose is small and crosses freely, so the mother's "
                     "blood glucose reaches the foetus even though the "
                     "insulin does not.",
             "correct": True},
            {"text": "Because the insulin that cannot cross builds up inside "
                     "the placenta and damages the exchange surface over the "
                     "months.",
             "correct": False,
             "why": "Nothing builds up in the placenta. The reason lies on "
                    "the other side of the same size rule: glucose is small, "
                    "so the mother's level becomes the foetus's level."},
            {"text": "It does not matter much, because nothing to do with "
                     "diabetes can reach the foetus across the placenta.",
             "correct": False,
             "why": "Glucose reaches it easily. Only the insulin is held back "
                    "by its size, which is precisely why the mother's glucose "
                    "still has to be controlled."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h04",
        "band": "harder",
        "text": "One pregnancy involves an exposure known to raise risk, and "
                "the baby is born with no problems. Another involves no such "
                "exposure, and the baby has a complication. What do the two "
                "outcomes together show?",
        "options": [
            {"text": "That the risk figure must be wrong, because the "
                     "exposed pregnancy came to no harm at all.",
             "correct": False,
             "why": "Neither result contradicts it. Risk is a probability "
                    "measured across large numbers of pregnancies, so both of "
                    "these are entirely ordinary outcomes."},
            {"text": "That the second pregnancy must have had some exposure "
                     "that nobody recorded or noticed at the time.",
             "correct": False,
             "why": "A great many pregnancy complications have no identified "
                    "cause at all. Assuming a hidden exposure turns a "
                    "statement about populations into a hunt for someone to "
                    "blame."},
            {"text": "That the exposure protects some pregnancies and harms "
                     "others, depending on who the person is.",
             "correct": False,
             "why": "It does neither selectively. A raised risk means a "
                    "higher proportion is affected across many pregnancies; "
                    "it says nothing about which one will be."},
            {"text": "Nothing that contradicts it — risk is a probability "
                     "across many pregnancies, not a prediction about one.",
             "correct": True},
        ],
        "figure": None,
    },
]
