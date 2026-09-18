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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-05-e05",
        "band": "easier",
        "text": "UK guidance on caffeine during pregnancy sets a daily limit "
                "rather than banning it. Roughly what is that limit?",
        "options": [
            {"text": "About 20 mg a day — a small fraction of one mug",
             "correct": False,
             "why": "That is ten times stricter than the guidance, and would "
                    "rule out even one mug of coffee. The published figure is "
                    "larger."},
            {"text": "About 2000 mg a day — roughly twenty mugs",
             "correct": False,
             "why": "That is ten times more than the guidance allows. A limit "
                    "set that high would not be a limit at all."},
            {"text": "About 200 mg a day — roughly two mugs of instant coffee",
             "correct": True},
            {"text": "There is no limit, because caffeine does not cross the "
                     "placenta", "correct": False,
             "why": "Caffeine crosses easily, and the foetus breaks it down "
                    "slowly. It is precisely because it arrives that a figure "
                    "is given at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e06",
        "band": "easier",
        "text": "Which vaccination given in childhood also protects a "
                "pregnancy years later, and against what?",
        "options": [
            {"text": "The MMR vaccination, which protects against rubella",
             "correct": True},
            {"text": "There is none — rubella cannot be vaccinated against",
             "correct": False,
             "why": "It can, and the MMR vaccination is how. That is why "
                    "rubella in pregnancy is far rarer than it once was."},
            {"text": "A vaccination given during the pregnancy itself, "
                     "against rubella", "correct": False,
             "why": "The protection has to be in place before the pregnancy "
                    "begins, because the damage is done in the earliest "
                    "weeks. That is why it is given in childhood."},
            {"text": "The MMR vaccination, against carbon monoxide",
             "correct": False,
             "why": "Carbon monoxide is a gas from burning tobacco, not an "
                    "infection, and nothing can be vaccinated against it. "
                    "Rubella is a virus, and that is what MMR covers."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-05-s05",
        "band": "standard",
        "text": "Tobacco smoke supplies both carbon monoxide and nicotine. "
                "Taken together, what is their effect on a developing foetus?",
        "options": [
            {"text": "Its blood becomes thicker and harder for its heart to "
                     "pump", "correct": False,
             "why": "Neither substance thickens blood. What carbon monoxide "
                    "does is take up space on haemoglobin that oxygen would "
                    "otherwise have used."},
            {"text": "The placenta is damaged, so that nothing can cross it "
                     "at all", "correct": False,
             "why": "Substances go on crossing — that is the problem. What "
                    "falls is the amount of oxygen there is to cross."},
            {"text": "Only the smoker is affected, because the foetus has its "
                     "own blood supply", "correct": False,
             "why": "That supply is loaded across the placenta from hers, and "
                    "carbon monoxide is breathed in by anyone in the room, "
                    "not only by the smoker."},
            {"text": "Less oxygen reaches it, so it grows more slowly and is "
                     "lighter at birth", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s06",
        "band": "standard",
        "text": "Weeks one and two of a pregnancy are described as “very "
                "little, or everything”. What does that mean?",
        "options": [
            {"text": "An exposure then damages every organ at once, because "
                     "they are all being built", "correct": False,
             "why": "There are no organs at all in the first fortnight. The "
                    "ball of cells is implanting and beginning to build the "
                    "placenta."},
            {"text": "An exposure then tends either to leave no lasting mark "
                     "or to stop the pregnancy continuing", "correct": True},
            {"text": "Almost nothing crosses the placenta yet, so hardly "
                     "anything can reach the cells", "correct": False,
             "why": "The placenta is still being built during those weeks, "
                    "but that is not the point. The point is that there is "
                    "not yet any structure to alter."},
            {"text": "The effects appear later, in whichever week the organ "
                     "concerned is being formed", "correct": False,
             "why": "That describes weeks three to eight, when organs are "
                    "laid down. The first fortnight is the window with no "
                    "structure in it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-05-h05",
        "band": "harder",
        "text": "Two doctors working separately traced a pattern of severely "
                "shortened limbs back to thalidomide, and it was withdrawn in "
                "1961. What made the timing of the doses the decisive "
                "evidence?",
        "options": [
            {"text": "The mothers who had taken it were all of a similar age",
             "correct": False,
             "why": "Age was not what separated the cases. What ran with the "
                    "pattern was which days of the pregnancy the tablets were "
                    "taken on."},
            {"text": "The larger the dose taken, the more severe the "
                     "malformation was", "correct": False,
             "why": "It was not chiefly a matter of how much. The window in "
                    "which it was taken decided which structure was "
                    "affected."},
            {"text": "Which limb was affected shifted with the days of "
                     "pregnancy on which it was taken", "correct": True},
            {"text": "Laboratory animals given a very large dose were not "
                     "harmed by it", "correct": False,
             "why": "That was true, and it is why the drug was believed safe. "
                    "It is the reason the disaster happened, not the evidence "
                    "that solved it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h06",
        "band": "harder",
        "text": "Thalidomide is still prescribed today, under tight controls, "
                "for conditions including a cancer of the blood. Which "
                "conclusion does that support?",
        "options": [
            {"text": "Whether a substance is safe depends on who is taking "
                     "it and why", "correct": True},
            {"text": "The original reports of harm must have been exaggerated",
             "correct": False,
             "why": "They were not. Thousands of babies were affected, and "
                    "the pattern was traced twice, independently, in two "
                    "countries."},
            {"text": "The molecule was later altered so that it is no longer "
                     "harmful", "correct": False,
             "why": "It is the same substance it always was. What changed is "
                    "the knowledge of who must never take it, and the "
                    "controls that enforce that."},
            {"text": "Any medicine becomes safe once enough time has passed "
                     "since it was withdrawn", "correct": False,
             "why": "Time settles nothing on its own. What made this drug "
                    "usable again was evidence about which patients it helps "
                    "and which it must not reach."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ─────────────────────────────────────────
    {
        "id": "b5-05-e07",
        "band": "easier",
        "text": "What decides whether a substance in the mother's blood "
                "reaches a foetus?",
        "options": [
            {"text": "The size of its molecules and whether they dissolve in "
                     "blood", "correct": True},
            {"text": "Whether the substance would be harmful to a developing "
                     "foetus", "correct": False,
             "why": "Harm is not a property the placenta can read. Alcohol is "
                    "harmful and crosses in minutes; insulin is useful and "
                    "does not cross at all."},
            {"text": "Whether the developing foetus has any use for the "
                     "substance", "correct": False,
             "why": "Usefulness decides nothing either. The surface passes "
                    "small dissolved molecules whether or not anything on the "
                    "other side needs them."},
            {"text": "Whether the substance was prescribed by a doctor or "
                     "bought over a counter", "correct": False,
             "why": "The placenta has no way of knowing where a substance came "
                    "from. Some prescribed medicines cross easily and some do "
                    "not, and the molecule settles it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e08",
        "band": "easier",
        "text": "How long after alcohol enters the mother's blood does it "
                "reach the foetus?",
        "options": [
            {"text": "About a week", "correct": False,
             "why": "Diffusion across a thin surface is fast. The foetal "
                    "concentration is close to the mother's within a few "
                    "minutes."},
            {"text": "Within minutes", "correct": True},
            {"text": "It does not reach the foetus", "correct": False,
             "why": "It crosses freely. Alcohol is a small molecule that "
                    "dissolves in blood, which is the only qualification the "
                    "crossing requires."},
            {"text": "Not until the final weeks", "correct": False,
             "why": "There is no stage at which the surface starts passing it. "
                    "It crosses from the earliest weeks onwards."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e09",
        "band": "easier",
        "text": "Alcohol dissolves in two things, which is what lets it into "
                "every tissue of an adult body. Which two?",
        "options": [
            {"text": "Starch and protein", "correct": False,
             "why": "Neither is a solvent in the body. What matters is that "
                    "alcohol dissolves in the watery part of blood and in fat "
                    "as well."},
            {"text": "Fat and protein", "correct": False,
             "why": "Half right: alcohol does dissolve in fat. The other "
                    "solvent is water, which is what carries it round in the "
                    "blood in the first place."},
            {"text": "Water and fat", "correct": True},
            {"text": "Water and haemoglobin", "correct": False,
             "why": "Haemoglobin is the protein that carries oxygen, and "
                    "nothing dissolves in it. Alcohol dissolves in water and "
                    "in fat."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e10",
        "band": "easier",
        "text": "Which kind of substance passes across the placenta most "
                "easily?",
        "options": [
            {"text": "Whole cells from the mother's blood",
             "correct": False,
             "why": "No cells cross at all, in either direction. The two blood "
                    "supplies stay separate and only dissolved substances move "
                    "between them."},
            {"text": "Large proteins, which are built for it",
             "correct": False,
             "why": "Large proteins are the ones held back. Insulin is the "
                    "standard example, and it is held back by its size and "
                    "nothing else."},
            {"text": "Substances the developing foetus is short of",
             "correct": False,
             "why": "Shortage on the far side does not open a door. What "
                    "crosses is decided by the molecule, not by what is needed "
                    "on the other side."},
            {"text": "Small molecules that dissolve in blood", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e11",
        "band": "easier",
        "text": "Which organ breaks alcohol down in the body?",
        "options": [
            {"text": "The liver", "correct": True},
            {"text": "The kidneys", "correct": False,
             "why": "The kidneys make urine and remove waste already dissolved "
                    "in blood. Breaking alcohol down is the liver's work."},
            {"text": "The lungs", "correct": False,
             "why": "The lungs exchange oxygen and carbon dioxide with the "
                    "air. They do not break substances down."},
            {"text": "The placenta", "correct": False,
             "why": "The placenta is a surface for exchange and breaks nothing "
                    "down. That is why what crosses it stays as it was."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e12",
        "band": "easier",
        "text": "Nicotine crosses the placenta. What does it do to blood "
                "vessels?",
        "options": [
            {"text": "It widens them, so more blood arrives", "correct": False,
             "why": "It does the opposite. Narrower vessels carry less blood, "
                    "which reduces the supply reaching the placenta."},
            {"text": "It narrows them, which reduces the supply again",
             "correct": True},
            {"text": "It blocks them completely with a clot", "correct": False,
             "why": "No clot is formed. The vessels narrow, so the supply "
                    "falls rather than stopping."},
            {"text": "It has no effect on them, because it acts only on "
                     "haemoglobin", "correct": False,
             "why": "Taking up seats on haemoglobin is carbon monoxide's "
                    "effect. Nicotine narrows blood vessels, and the two "
                    "together reduce the oxygen supply twice over."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e13",
        "band": "easier",
        "text": "Rubella is usually a mild illness in a child. What does it "
                "involve?",
        "options": [
            {"text": "A few days of rash and fever", "correct": True},
            {"text": "Several weeks of breathlessness", "correct": False,
             "why": "Rubella in a child is short and mild. Its seriousness is "
                    "for an embryo, not for the child who catches it."},
            {"text": "A permanent loss of hearing", "correct": False,
             "why": "Damage to the ears is what rubella can do to an embryo "
                    "early in a pregnancy. A child who catches it has a rash "
                    "and a fever for a few days."},
            {"text": "Stomach pain lasting about a month",
             "correct": False,
             "why": "That is not what rubella does at any age. The illness in "
                    "a child is a rash and a fever, over in days."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e14",
        "band": "easier",
        "text": "Rubella caught early in a pregnancy can damage three "
                "developing structures. Which three?",
        "options": [
            {"text": "The liver, kidneys and bladder", "correct": False,
             "why": "Those are not the structures rubella is known for. The "
                    "eyes, ears and heart are the ones at risk, and all three "
                    "are formed early."},
            {"text": "The eyes, ears and heart", "correct": True},
            {"text": "The skin, hair and nails", "correct": False,
             "why": "A rash is what rubella does to the person who catches it. "
                    "In an embryo the damage is to the eyes, ears and heart."},
            {"text": "The arms and legs, and nothing else", "correct": False,
             "why": "Limb damage in a particular few-week window is what "
                    "thalidomide caused. Rubella affects the eyes, ears and "
                    "heart."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e15",
        "band": "easier",
        "text": "In which group of drinks is caffeine found?",
        "options": [
            {"text": "Milk, water and fruit juice", "correct": False,
             "why": "None of those contains caffeine. It is in coffee, tea, "
                    "cola and energy drinks."},
            {"text": "Coffee, and no other drink", "correct": False,
             "why": "Coffee is the best-known source but not the only one. Tea, "
                    "cola and energy drinks all supply caffeine too, which is "
                    "why a daily limit is given rather than a number of cups."},
            {"text": "Coffee, tea, cola and energy drinks", "correct": True},
            {"text": "Beer, wine and spirits", "correct": False,
             "why": "Those supply alcohol, and the advice on alcohol is a "
                    "different one. Caffeine is in coffee, tea, cola and "
                    "energy drinks."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e16",
        "band": "easier",
        "text": "Caffeine is the most widely used drug in the world. What kind "
                "of drug is it?",
        "options": [
            {"text": "A stimulant", "correct": True},
            {"text": "A sedative", "correct": False,
             "why": "A sedative makes someone drowsy. Caffeine does the "
                    "opposite, which is why it is drunk in the morning."},
            {"text": "A painkiller", "correct": False,
             "why": "Caffeine does not relieve pain. It is a stimulant, found "
                    "in coffee, tea, cola and energy drinks."},
            {"text": "An antibiotic", "correct": False,
             "why": "An antibiotic treats a bacterial infection. Caffeine "
                    "treats nothing — it is a stimulant."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e17",
        "band": "easier",
        "text": "What is the standard treatment for diabetes during a "
                "pregnancy?",
        "options": [
            {"text": "Extra glucose", "correct": False,
             "why": "Diabetes is a problem of blood glucose being too high, "
                    "not too low. Adding more would make the very thing that "
                    "does cross the placenta worse."},
            {"text": "Rubella vaccine", "correct": False,
             "why": "A vaccine protects against an infection. Diabetes is not "
                    "an infection, and nothing can be vaccinated against it."},
            {"text": "A sedative", "correct": False,
             "why": "A sedative makes someone drowsy and does nothing to blood "
                    "glucose. Thalidomide was one, which is a separate story "
                    "on this page."},
            {"text": "Insulin", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e18",
        "band": "easier",
        "text": "Antibodies are large molecules, and they still reach the "
                "foetus. How?",
        "options": [
            {"text": "The placenta carries them across, using energy to do it",
             "correct": True},
            {"text": "They diffuse across, in the same way that oxygen does",
             "correct": False,
             "why": "Diffusion is for small dissolved molecules. An antibody "
                    "is far too large for that, which is why the placenta has "
                    "to spend energy moving it."},
            {"text": "They are broken into pieces small enough to diffuse over",
             "correct": False,
             "why": "Nothing is taken apart at the placenta. Antibodies arrive "
                    "whole, carried across deliberately."},
            {"text": "They infect the placenta's cells and are rebuilt on the "
                     "other side", "correct": False,
             "why": "That is how a virus such as rubella gets across. An "
                    "antibody is not an infection and does not copy itself."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e19",
        "band": "easier",
        "text": "What is happening during weeks one and two of a pregnancy?",
        "options": [
            {"text": "The heart, brain, spine and limbs are being laid down",
             "correct": False,
             "why": "That is the next stage, from about week three. In the "
                    "first fortnight there are no organs yet at all."},
            {"text": "The organs that already exist are growing and maturing "
                     "into their final form", "correct": False,
             "why": "Growing and maturing is what happens from about week "
                    "nine, once the organs are there. Nothing has been built "
                    "yet in the first fortnight."},
            {"text": "The ball of cells divides, implants and begins to build "
                     "the placenta", "correct": True},
            {"text": "The lungs are being made ready for the first breath",
             "correct": False,
             "why": "Lung readiness is a late question, in the growth half of "
                    "the pregnancy. The first fortnight is dividing, implanting "
                    "and starting the placenta."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e20",
        "band": "easier",
        "text": "By about which week is the laying down of organs largely "
                "over?",
        "options": [
            {"text": "Week two", "correct": False,
             "why": "Nothing has been laid down by week two. The ball of cells "
                    "is still dividing and implanting."},
            {"text": "Week eight", "correct": True},
            {"text": "Week twenty", "correct": False,
             "why": "Long before week twenty the organs exist and are growing. "
                    "Building them is largely finished by week eight."},
            {"text": "Week forty", "correct": False,
             "why": "Week forty is the end of the pregnancy. Structure is "
                    "settled thirty-two weeks earlier."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e21",
        "band": "easier",
        "text": "Which part of a developing organism keeps developing right up "
                "to birth and beyond?",
        "options": [
            {"text": "The limbs", "correct": False,
             "why": "Limbs are laid down early, in the embryo stage, and after "
                    "that they grow. The brain is the one still being built at "
                    "the end."},
            {"text": "The eyes", "correct": False,
             "why": "The eyes are formed in the first weeks, which is why "
                    "rubella is dangerous then. Development after birth is the "
                    "brain's."},
            {"text": "The spine", "correct": False,
             "why": "The spine is laid down in weeks three to eight along with "
                    "the heart and limbs. The brain goes on developing far "
                    "longer."},
            {"text": "The brain", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e22",
        "band": "easier",
        "text": "When a study reports a risk in pregnancy, what is being "
                "described?",
        "options": [
            {"text": "A probability measured across large numbers of "
                     "pregnancies", "correct": True},
            {"text": "A prediction of what will happen in one particular "
                     "pregnancy", "correct": False,
             "why": "A risk figure cannot say which pregnancy will be "
                    "affected. It describes a proportion across many of them."},
            {"text": "A measure of how harmful a substance is at a given "
                     "amount of it", "correct": False,
             "why": "How harmful something is at a given amount is a separate "
                    "question. Risk is about how often an outcome occurs "
                    "across a population."},
            {"text": "A certainty that harm will follow from an exposure of "
                     "that kind", "correct": False,
             "why": "Nothing about a raised risk is certain. An exposed "
                    "pregnancy coming to no harm is an entirely ordinary "
                    "result."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e23",
        "band": "easier",
        "text": "Thalidomide was sold from 1957. What was it sold as?",
        "options": [
            {"text": "A vaccine given against rubella in childhood",
             "correct": False,
             "why": "Rubella is prevented by the MMR vaccination given in "
                    "childhood. Thalidomide was a sedative."},
            {"text": "An antibiotic, for treating infections during a "
                     "pregnancy", "correct": False,
             "why": "It treated no infection. It was sold as a safe sedative "
                    "and prescribed widely for morning sickness."},
            {"text": "A safe sedative, prescribed widely for morning sickness",
             "correct": True},
            {"text": "A treatment for diabetes during a pregnancy",
             "correct": False,
             "why": "Insulin is the treatment for diabetes in pregnancy. "
                    "Thalidomide was a sedative."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e24",
        "band": "easier",
        "text": "In which year was thalidomide withdrawn?",
        "options": [
            {"text": "1941", "correct": False,
             "why": "It had not been sold by then. It went on sale in 1957 and "
                    "was withdrawn four years later."},
            {"text": "1957", "correct": False,
             "why": "That is the year it went on sale. The withdrawal came "
                    "after two doctors traced the pattern back to it."},
            {"text": "1972", "correct": False,
             "why": "The withdrawal was a good deal earlier than that, once "
                    "the pattern had been traced back to the drug."},
            {"text": "1961", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e25",
        "band": "easier",
        "text": "Carbon monoxide is produced whenever tobacco burns. Who "
                "breathes it in?",
        "options": [
            {"text": "Anyone in the room, not only the smoker", "correct": True},
            {"text": "The person holding the cigarette, and nobody else",
             "correct": False,
             "why": "The gas is in the air of the room, not only in the smoke "
                    "drawn through a cigarette. Everybody present breathes it."},
            {"text": "People who smoke themselves, whichever room they are "
                     "in", "correct": False,
             "why": "Someone who has never smoked breathes it in if they are "
                    "in the room where tobacco is burning."},
            {"text": "Nobody — it stays inside the cigarette until it burns "
                     "out", "correct": False,
             "why": "It is produced by the burning and goes straight into the "
                    "air. That is why it reaches everybody nearby."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e26",
        "band": "easier",
        "text": "Which measurement is lowered by smoking during a pregnancy?",
        "options": [
            {"text": "The number of organs", "correct": False,
             "why": "The organs still form. What falls is how much the foetus "
                    "grows, because less oxygen is reaching it."},
            {"text": "Blood group", "correct": False,
             "why": "A blood group is inherited and is not a measurement that "
                    "can go up or down. Birth weight is the figure that falls."},
            {"text": "Birth weight", "correct": True},
            {"text": "The length of the pregnancy", "correct": False,
             "why": "The effect the lesson names is on weight rather than on "
                    "dates: a foetus short of oxygen grows more slowly."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e27",
        "band": "easier",
        "text": "For which conditions might someone need treatment while "
                "pregnant?",
        "options": [
            {"text": "Infections, since every other condition can wait "
                     "until after the birth", "correct": False,
             "why": "Epilepsy, diabetes, asthma and mental health conditions "
                    "do not pause for nine months. Any of them may need "
                    "treating throughout."},
            {"text": "Epilepsy, diabetes, asthma, an infection or a mental "
                     "health condition", "correct": True},
            {"text": "Conditions that began after the pregnancy did",
             "correct": False,
             "why": "Most are conditions someone already had. That is exactly "
                    "why the first appointment asks what is already being "
                    "taken."},
            {"text": "None — every medicine is stopped for the whole "
                     "pregnancy", "correct": False,
             "why": "Stopping is often the greater risk. An untreated seizure "
                    "or an untreated infection can be far more dangerous than "
                    "the medicine that prevents it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e28",
        "band": "easier",
        "text": "Who should decide whether a prescribed medicine is continued "
                "during a pregnancy?",
        "options": [
            {"text": "The person taking it, on their own",
             "correct": False,
             "why": "Nobody should stop a prescribed medicine on their own. "
                    "The condition it controls may be more dangerous than the "
                    "medicine."},
            {"text": "Nobody — a medicine that crosses is stopped "
                     "automatically", "correct": False,
             "why": "Crossing does not settle it. Each medicine is judged "
                    "against what would happen if the condition went "
                    "untreated."},
            {"text": "A doctor or pharmacist who knows the case",
             "correct": True},
            {"text": "A midwife, at some point after the birth has happened",
             "correct": False,
             "why": "The decision is needed during the pregnancy, not after "
                    "it, which is why the question is asked at the first "
                    "appointment."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e29",
        "band": "easier",
        "text": "Oxygen and glucose have to arrive at the rate a growing "
                "organism uses them. What does that require of the placenta?",
        "options": [
            {"text": "A thick wall between the two", "correct": False,
             "why": "Thickness would slow the arrival. The placenta is very "
                    "thin for the opposite reason."},
            {"text": "A pump, which pushes substances from one side to the "
                     "other", "correct": False,
             "why": "There is no pump. Small dissolved molecules move from "
                    "where there is more of them to where there is less."},
            {"text": "A filter, which selects the substances that are allowed "
                     "across", "correct": False,
             "why": "There is no filtering ability at all. The surface passes "
                    "what is small and soluble, whatever it happens to be."},
            {"text": "A very thin surface with a very large area",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-e30",
        "band": "easier",
        "text": "After about which week of a pregnancy is the risk from "
                "rubella very low?",
        "options": [
            {"text": "About four weeks", "correct": False,
             "why": "Week four is inside the most dangerous period, not past "
                    "it. The eyes, ears and heart are being formed then."},
            {"text": "About twenty weeks", "correct": True},
            {"text": "About thirty-six weeks", "correct": False,
             "why": "The risk has fallen away long before that, once the "
                    "structures rubella damages are already formed."},
            {"text": "It does not become low at any stage", "correct": False,
             "why": "It does. The danger is concentrated in the first twelve "
                    "weeks and is very low after about twenty."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ───────────────────────────────────────
    {
        "id": "b5-05-s07",
        "band": "standard",
        "text": "Someone who is pregnant does not smoke but lives with a "
                "person who does. Why does the oxygen reaching the foetus "
                "still fall?",
        "options": [
            {"text": "It does not fall — only a smoker's own blood carries "
                     "carbon monoxide, and hers does not",
             "correct": False,
             "why": "The gas is in the air of the room. Anyone breathing that "
                    "air takes it into their blood, smoker or not."},
            {"text": "Carbon monoxide in the air of the room is breathed in "
                     "and takes up seats on her haemoglobin",
             "correct": True},
            {"text": "Nicotine is passed on in food and drink rather than in "
                     "air, so it reaches her that way",
             "correct": False,
             "why": "Nicotine is breathed in with the smoke, not eaten. The "
                    "oxygen problem is carbon monoxide occupying haemoglobin."},
            {"text": "Smoke damages the placenta itself, so oxygen can no "
                     "longer cross the exchange surface",
             "correct": False,
             "why": "The surface goes on working. What falls is the amount of "
                    "oxygen the blood arriving at it can carry."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s08",
        "band": "standard",
        "text": "Why does the effect of one exposure depend on which week of a "
                "pregnancy it happens in?",
        "options": [
            {"text": "Because the placenta thickens as the pregnancy goes on "
                     "and lets less through",
             "correct": False,
             "why": "The surface does not start sorting or thickening part way "
                    "through. What changes is on the other side of it."},
            {"text": "Because the mother's blood carries less of a substance "
                     "later in a pregnancy",
             "correct": False,
             "why": "The concentration in her blood depends on the exposure, "
                    "not on the week. The week decides what the substance "
                    "arrives among."},
            {"text": "Because what is being built or grown changes from week "
                     "to week",
             "correct": True},
            {"text": "Because a substance only crosses during certain weeks of "
                     "a pregnancy",
             "correct": False,
             "why": "A small soluble molecule crosses throughout. Timing "
                    "changes what it meets, not whether it gets there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s09",
        "band": "standard",
        "text": "Birth weight, lung readiness and brain development are the "
                "three things named for weeks 9 to 40. What do they have in "
                "common?",
        "options": [
            {"text": "They are all settled in weeks three to eight, before "
                     "that stage of the pregnancy begins", "correct": False,
             "why": "Weeks three to eight settle whether a structure forms. "
                    "These three are about how well it then works."},
            {"text": "They are all changes in how well something works, rather "
                     "than whether it formed", "correct": True},
            {"text": "They are all measured at the first appointment of a "
                     "pregnancy", "correct": False,
             "why": "None of the three can be measured that early. They are "
                    "grouped because they are all questions of function."},
            {"text": "They are all caused by substances that do not cross the "
                     "placenta", "correct": False,
             "why": "A substance that never arrives affects nothing. These are "
                    "the effects of substances that do cross, late on."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s10",
        "band": "standard",
        "text": "UK advice gives a daily limit for caffeine but says no amount "
                "of alcohol is known to be safe. What is the difference "
                "between those two statements?",
        "options": [
            {"text": "Alcohol crosses the placenta and caffeine does not",
             "correct": False,
             "why": "Both cross easily. The difference is in what is known "
                    "about the amount at which each does harm."},
            {"text": "Caffeine is broken down quickly by the foetus and "
                     "alcohol is not", "correct": False,
             "why": "The foetus breaks both down slowly. The difference is "
                    "that an amount has been established for one and not for "
                    "the other."},
            {"text": "Alcohol matters only in the first twelve weeks, so no "
                     "figure is useful", "correct": False,
             "why": "Alcohol's window is the whole pregnancy, because the "
                    "brain and nervous system are built throughout."},
            {"text": "One has an amount that evidence supports and the other "
                     "does not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s11",
        "band": "standard",
        "text": "“No amount is known to be safe.” What kind of statement is "
                "that?",
        "options": [
            {"text": "A statement about missing knowledge as much as about the "
                     "alcohol itself", "correct": True},
            {"text": "A statement that every amount has been shown to cause "
                     "harm in studies", "correct": False,
             "why": "It does not say that. It says no amount has been shown to "
                    "be safe, which is a different claim about what has been "
                    "established."},
            {"text": "A statement that alcohol does not cross the placenta",
             "correct": False,
             "why": "Alcohol crosses within minutes. The sentence is about "
                    "what is known, not about whether it arrives."},
            {"text": "A statement that the risk is identical at every amount "
                     "taken", "correct": False,
             "why": "Nothing in the wording says the risk is flat. It says "
                    "that no safe level has been identified."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s12",
        "band": "standard",
        "text": "Why is insulin the treatment of choice for diabetes during a "
                "pregnancy?",
        "options": [
            {"text": "It crosses the placenta and controls the glucose of "
                     "the foetus as well as that of the mother herself",
             "correct": False,
             "why": "It does not arrive at all. The foetus's glucose follows "
                    "the mother's because glucose crosses, not because insulin "
                    "does."},
            {"text": "It is broken down by the placenta before it can reach "
                     "the foetus and do harm", "correct": False,
             "why": "The placenta breaks nothing down. Insulin is held back by "
                    "being a large protein."},
            {"text": "It stops glucose crossing the placenta, so the foetus is "
                     "protected from a high level", "correct": False,
             "why": "Glucose goes on crossing freely. Insulin lowers the "
                    "mother's level, and the foetus's level follows it down."},
            {"text": "It controls the mother's glucose and never arrives in "
                     "the foetus's blood in any useful amount",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s13",
        "band": "standard",
        "text": "Someone catches rubella at week thirty of a pregnancy. "
                "Compared with catching it at week six, what is the risk to "
                "the developing organism?",
        "options": [
            {"text": "Much lower, because the eyes, ears and heart were formed "
                     "long before", "correct": True},
            {"text": "Much higher, because there is far more of the foetus for "
                     "the virus to reach", "correct": False,
             "why": "Size is not what decides it. The damage rubella does is "
                    "to structures being formed, and that forming happened "
                    "early."},
            {"text": "Exactly the same, because the virus crosses at any stage "
                     "of a pregnancy", "correct": False,
             "why": "It does cross at any stage. What changes is that after "
                    "about twenty weeks there is no longer an eye or an ear "
                    "being built for it to damage."},
            {"text": "Zero, because a virus cannot cross the placenta after "
                     "week twelve", "correct": False,
             "why": "Nothing stops crossing at week twelve. The risk is very "
                    "low after about twenty weeks, which is not the same as "
                    "nothing crossing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s14",
        "band": "standard",
        "text": "Someone who is pregnant swaps a morning mug of instant coffee "
                "for a large energy drink. Why might that matter?",
        "options": [
            {"text": "Energy drinks contain no caffeine, so the swap removes "
                     "it entirely", "correct": False,
             "why": "Energy drinks are one of the four sources the lesson "
                    "names. The swap changes the amount, not whether there is "
                    "any."},
            {"text": "Caffeine from an energy drink does not cross the "
                     "placenta the way coffee's does", "correct": False,
             "why": "Caffeine is the same molecule whichever drink it comes "
                    "in, and it crosses easily from all of them."},
            {"text": "The guidance is about the amount of caffeine, not about "
                     "which drink supplies it", "correct": True},
            {"text": "The limit applies only to coffee, so any other drink "
                     "falls outside it", "correct": False,
             "why": "The figure is a daily total in milligrams. Tea, cola and "
                    "energy drinks all count towards it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s15",
        "band": "standard",
        "text": "The placenta is called an exchange surface. What does "
                "exchange mean here?",
        "options": [
            {"text": "The mother's blood is swapped for the foetus's blood, a "
                     "little at a time, at the surface where the two meet",
             "correct": False,
             "why": "No blood is swapped, and the two supplies never mix. Only "
                    "dissolved substances move between them."},
            {"text": "Only dissolved substances move, both ways, from where "
                     "there is more of them to where there is less",
             "correct": True},
            {"text": "The surface chooses which substances to admit in each "
                     "direction", "correct": False,
             "why": "There is no choosing. Movement is decided by the "
                    "concentration difference and by the size of the "
                    "molecule."},
            {"text": "Harmful substances are converted into safe ones as they "
                     "pass", "correct": False,
             "why": "Nothing is converted. What arrives is what left, which is "
                    "why the foetal concentration ends up close to the "
                    "mother's."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s16",
        "band": "standard",
        "text": "Someone stops using an asthma inhaler on finding out they are "
                "pregnant. Why is that a risk in itself?",
        "options": [
            {"text": "Uncontrolled asthma can be far more dangerous to a "
                     "pregnancy than the medicine that prevents it",
             "correct": True},
            {"text": "It is not a risk — stopping any medicine is always the "
                     "safer choice while pregnant", "correct": False,
             "why": "Stopping is often the greater risk. That is why the "
                    "decision belongs to a doctor or pharmacist who knows the "
                    "case."},
            {"text": "The inhaler was blocking harmful substances from "
                     "crossing the placenta", "correct": False,
             "why": "No medicine blocks the placenta. An inhaler treats the "
                    "airways of the person using it."},
            {"text": "Asthma medicines are the one kind that does not cross "
                     "the placenta at any stage of a pregnancy",
             "correct": False,
             "why": "Whether a medicine crosses depends on its own molecules. "
                    "The reason not to stop is what the asthma would do "
                    "untreated."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s17",
        "band": "standard",
        "text": "Glucose and insulin are both to do with blood sugar, yet only "
                "one of them reaches the foetus. Why?",
        "options": [
            {"text": "The placenta sorts them by which one the foetus needs",
             "correct": False,
             "why": "It sorts nothing. Glucose is a small molecule and insulin "
                    "is a large protein, and size is the whole of it."},
            {"text": "Glucose is small and insulin is a large protein",
             "correct": True},
            {"text": "Insulin is broken down on the way across the surface",
             "correct": False,
             "why": "Nothing is broken down at the placenta. Insulin simply "
                    "does not fit through."},
            {"text": "Insulin crosses only when the mother's glucose is high",
             "correct": False,
             "why": "It does not arrive in any useful amount at any level. "
                    "That is exactly why it is the treatment used."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s18",
        "band": "standard",
        "text": "Why does the first appointment of a pregnancy ask what "
                "medicines someone is already taking?",
        "options": [
            {"text": "Because every medicine someone is taking is stopped at "
                     "that point, as a matter of routine, until the birth",
             "correct": False,
             "why": "Nothing is stopped as a routine. Each medicine is judged "
                    "against what would happen if the condition went "
                    "untreated."},
            {"text": "Because weeks three to eight are the most sensitive for "
                     "structural effects, and they come early", "correct": True},
            {"text": "Because the placenta has not formed yet, so everything "
                     "crosses more easily", "correct": False,
             "why": "There is nothing to cross to before the placenta exists. "
                    "The reason the question is early is that organ formation "
                    "is early."},
            {"text": "Because medicines taken later in a pregnancy cannot "
                     "cross the placenta", "correct": False,
             "why": "They cross throughout. What changes is what is being "
                    "built when they arrive."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s19",
        "band": "standard",
        "text": "What changed in the way medicines are licensed after "
                "thalidomide?",
        "options": [
            {"text": "Testing on laboratory animals was stopped", "correct": False,
             "why": "It continues. What changed is that a large dose not "
                    "killing an adult animal is no longer taken as evidence "
                    "about a pregnancy."},
            {"text": "Sedatives were banned from sale in this country "
                     "completely", "correct": False,
             "why": "Sedatives are still prescribed. The change was to how "
                    "drugs are tested and licensed for use in pregnancy."},
            {"text": "Drugs are now tested on pregnancy specifically",
             "correct": True},
            {"text": "Every medicine became available without a prescription",
             "correct": False,
             "why": "The change went the other way: licensing was tightened, "
                    "which is why a pharmacist checks before handing an "
                    "ordinary medicine over."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s20",
        "band": "standard",
        "text": "The placenta has no filtering ability. Does it follow that a "
                "complication in a pregnancy must be somebody's fault?",
        "options": [
            {"text": "Yes, because everything that crossed the placenta came "
                     "from the mother's own blood supply", "correct": False,
             "why": "Where a substance crossed from says nothing about how it "
                    "got into that blood. Second-hand smoke and roadside air "
                    "are not chosen."},
            {"text": "Yes, because nothing was blocked that could have been "
                     "blocked", "correct": False,
             "why": "Nothing could have been blocked at all — the surface has "
                    "no mechanism for it. A failure needs something that could "
                    "have worked and did not."},
            {"text": "Only when the exposure happened in the first twelve "
                     "weeks", "correct": False,
             "why": "The week changes what an exposure can affect. It changes "
                    "nothing about whether anyone is to blame."},
            {"text": "No — much exposure is not chosen, and many "
                     "complications have no identified cause at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s21",
        "band": "standard",
        "text": "Second-hand smoke, roadside air pollution and an infection "
                "caught from someone else have one thing in common. What?",
        "options": [
            {"text": "None of them is chosen at all by the person who is "
                     "pregnant", "correct": True},
            {"text": "All three are blocked by the placenta before they reach "
                     "the foetus", "correct": False,
             "why": "The placenta blocks none of them. Carbon monoxide "
                    "diffuses across and rubella infects the placenta's own "
                    "cells."},
            {"text": "All three have their effect only in the first two weeks "
                     "of a pregnancy", "correct": False,
             "why": "Their windows differ: rubella is early, carbon monoxide "
                    "is mostly late. What they share is that none is a choice."},
            {"text": "All three are made of molecules too large to cross the "
                     "placenta", "correct": False,
             "why": "Carbon monoxide is one of the smallest molecules on the "
                    "page. Size is not what these three have in common."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s22",
        "band": "standard",
        "text": "Addiction is described as a condition of the nervous system "
                "rather than a decision repeated daily. What follows from "
                "that?",
        "options": [
            {"text": "That the substance involved cannot reach a foetus "
                     "across the placenta", "correct": False,
             "why": "Whether it reaches a foetus depends on its molecules and "
                    "nothing else. The description is about the person, not "
                    "about the crossing."},
            {"text": "That risk figures stop applying to that particular "
                     "pregnancy", "correct": False,
             "why": "A risk figure is a proportion across many pregnancies and "
                    "applies the same way whatever the exposure's cause."},
            {"text": "That treating it as a simple choice misdescribes what is "
                     "happening", "correct": True},
            {"text": "That an exposure of that kind has no effect on how "
                     "the pregnancy goes", "correct": False,
             "why": "The effect of a substance does not change with why it was "
                    "taken. What the description changes is the idea that it "
                    "was freely chosen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s23",
        "band": "standard",
        "text": "A student writes that oxygen crosses the placenta because the "
                "foetus needs it. Correct that.",
        "options": [
            {"text": "Oxygen crosses because the placenta recognises it as "
                     "a substance that is useful", "correct": False,
             "why": "The placenta recognises nothing. Oxygen crosses on "
                    "exactly the same terms as alcohol does."},
            {"text": "Oxygen crosses because it is carried over using energy, "
                     "as a needed substance", "correct": False,
             "why": "Antibodies are the ones carried over using energy. Oxygen "
                    "diffuses, because it is small and dissolved."},
            {"text": "Oxygen crosses because it is small and dissolved, not "
                     "because it is needed", "correct": True},
            {"text": "Oxygen does not cross — the foetus makes its own",
             "correct": False,
             "why": "A foetus makes no oxygen. Everything it uses arrives "
                    "across the placenta from the mother's blood."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s24",
        "band": "standard",
        "text": "Why does a shortage of oxygen show up as slower growth?",
        "options": [
            {"text": "Because growth needs a steady oxygen supply, and less "
                     "oxygen is being carried", "correct": True},
            {"text": "Because the foetus spends its energy breaking the carbon "
                     "monoxide down instead", "correct": False,
             "why": "It breaks the carbon monoxide down very little. The "
                    "problem is the oxygen that is not arriving."},
            {"text": "Because a shortage of oxygen makes the blood of the "
                     "foetus clot more easily than usual", "correct": False,
             "why": "Nothing clots. Less oxygen simply means less of what "
                    "growing tissue needs."},
            {"text": "Because oxygen is the material that organs are built "
                     "from", "correct": False,
             "why": "Organs are built from the substances in food, not from "
                    "oxygen. Oxygen is what releases the energy for building "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s25",
        "band": "standard",
        "text": "The lesson says the interesting question is not “does it get "
                "through”. What is it instead?",
        "options": [
            {"text": "Whether the placenta could have stopped it from "
                     "reaching the foetus, and why it did not",
             "correct": False,
             "why": "It could not have stopped anything, ever. That is the "
                    "settled part, which is why it is not the interesting "
                    "question."},
            {"text": "Whether the substance was chosen by the person or not",
             "correct": False,
             "why": "That matters for how an exposure happened, not for what "
                    "the substance does once it has arrived."},
            {"text": "How large the molecule is, and whether it dissolves",
             "correct": False,
             "why": "Size is what answers the first question. The one still "
                    "open is what the substance does at the other end."},
            {"text": "What it does when it arrives, and whether that matters "
                     "more in some weeks than others", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s26",
        "band": "standard",
        "text": "Rubella is far too large to diffuse and still gets across. "
                "What does that show about the size rule?",
        "options": [
            {"text": "That the size rule is wrong, since something very "
                     "large has crossed the placenta after all",
             "correct": False,
             "why": "The rule is about diffusion, and rubella does not "
                    "diffuse. A different route does not break it."},
            {"text": "That viruses are smaller than they are usually said to "
                     "be", "correct": False,
             "why": "A virus particle is enormous next to a molecule of "
                    "alcohol. Its route is infection of cells, not squeezing "
                    "through."},
            {"text": "That the size rule is about diffusion, and there is more "
                     "than one route across", "correct": True},
            {"text": "That the placenta chooses which infections to admit",
             "correct": False,
             "why": "It admits nothing deliberately. Rubella infects the "
                    "placenta's own cells, which is not a decision the "
                    "placenta makes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s27",
        "band": "standard",
        "text": "Antibodies are large and reach the foetus anyway. Why does "
                "that not contradict the claim that the placenta passes small "
                "molecules?",
        "options": [
            {"text": "Because antibodies turn out to be smaller than insulin "
                     "is", "correct": False,
             "why": "Both are large. The difference is that one is carried "
                    "over deliberately and the other is not."},
            {"text": "Because alcohol is carried across by the same "
                     "mechanism, so the rule did not apply", "correct": False,
             "why": "Alcohol diffuses, like oxygen and glucose. Carrying is a "
                    "separate mechanism, used for antibodies."},
            {"text": "Because the placenta spends energy only on molecules the "
                     "foetus needs, and that is a kind of filtering",
             "correct": False,
             "why": "Carrying something over is not the same as keeping "
                    "anything out. Nothing is filtered in either direction."},
            {"text": "Because they are carried across using energy, rather "
                     "than diffusing", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s28",
        "band": "standard",
        "text": "Every substance on the lesson's list has a window saying when "
                "it matters most, except insulin, whose bar is empty. Why?",
        "options": [
            {"text": "It matters equally in every week, so no window can be "
                     "drawn for it", "correct": False,
             "why": "That would be a full bar rather than an empty one. The "
                    "bar is empty because the substance never arrives."},
            {"text": "It never arrives, so there is no window to draw",
             "correct": True},
            {"text": "It matters only in weeks three to eight, which is too "
                     "narrow to show", "correct": False,
             "why": "Weeks three to eight is the window given for prescribed "
                    "medicines that do cross. Insulin does not."},
            {"text": "The window has not yet been measured for it",
             "correct": False,
             "why": "Nothing is waiting to be measured. A substance that does "
                    "not reach the foetus has no window by definition."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s29",
        "band": "standard",
        "text": "The caffeine limit is given as about 200 mg a day, “roughly "
                "two mugs of instant coffee”. Why roughly?",
        "options": [
            {"text": "Because the limit changes with each week of a pregnancy",
             "correct": False,
             "why": "The figure is a single daily amount for the whole "
                    "pregnancy. What varies is the drink, not the guidance."},
            {"text": "Because caffeine does not always cross the placenta",
             "correct": False,
             "why": "It crosses easily every time. The vagueness is about how "
                    "much caffeine is in a mug, not about what happens to it."},
            {"text": "Because different drinks contain different amounts of "
                     "caffeine", "correct": True},
            {"text": "Because the limit is worked out from each person's "
                     "weight", "correct": False,
             "why": "A single figure is given rather than a calculation. The "
                    "mug is an illustration of that figure, not a measurement."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-s30",
        "band": "standard",
        "text": "Why will a pharmacist check before handing an ordinary "
                "medicine to someone who is pregnant?",
        "options": [
            {"text": "Because no medicine at all may be taken during a "
                     "pregnancy", "correct": False,
             "why": "Many are taken, and stopping some would be the greater "
                    "risk. The check is about which one, not about whether."},
            {"text": "Because the placenta blocks most medicines, so the dose "
                     "has to be raised", "correct": False,
             "why": "The placenta blocks nothing. Whether a medicine crosses "
                    "depends on its own molecules."},
            {"text": "Because medicines have a stronger effect during a "
                     "pregnancy", "correct": False,
             "why": "Strength is not the issue. The issue is that a second "
                    "developing organism is now on the other side of an "
                    "exchange surface."},
            {"text": "Because each medicine always has to be judged "
                     "separately for a pregnancy", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "b5-05-h07",
        "band": "harder",
        "text": "A substance is a small molecule, dissolves readily in blood, "
                "and is completely harmless to an adult. Predict what happens "
                "at the placenta, and what is still unknown.",
        "options": [
            {"text": "It reaches the foetus, and whether that matters has to "
                     "be established separately", "correct": True},
            {"text": "It does not reach the foetus, because the placenta "
                     "passes only what is needed", "correct": False,
             "why": "Need has nothing to do with it. A small soluble molecule "
                    "crosses whether or not anything wants it."},
            {"text": "It reaches the foetus, and is therefore harmless there "
                     "as well", "correct": False,
             "why": "Harmless to an adult and harmless to a developing "
                    "organism are two different claims, and the second has to "
                    "be shown separately."},
            {"text": "It does not reach the foetus, because it is harmless and "
                     "so nothing carries it", "correct": False,
             "why": "Nothing has to carry a small soluble molecule. It "
                    "diffuses, exactly as oxygen and alcohol do."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h08",
        "band": "harder",
        "text": "Oxygen and carbon monoxide are both small molecules that "
                "cross the placenta easily. One is essential and one is "
                "damaging. What does that pair show about the placenta?",
        "options": [
            {"text": "That it passes oxygen faster, because the foetus needs "
                     "it more", "correct": False,
             "why": "Speed of diffusion depends on the molecule and the "
                    "concentration difference, not on what is needed."},
            {"text": "That carbon monoxide must be getting across by some "
                     "other route", "correct": False,
             "why": "It diffuses, like oxygen. Only a virus uses another "
                    "route, and carbon monoxide is not a virus."},
            {"text": "That it passes both on exactly the same terms, and "
                     "never sorts", "correct": True},
            {"text": "That it blocks carbon monoxide once the level in the "
                     "blood gets high enough", "correct": False,
             "why": "There is no level at which the surface starts blocking. "
                    "A higher concentration on one side means more crosses, "
                    "not less."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h09",
        "band": "harder",
        "text": "Why is there no stage of a pregnancy at which alcohol has "
                "nothing to reach?",
        "options": [
            {"text": "Because alcohol stays in the blood for the whole of "
                     "the pregnancy once any amount of it has been taken",
             "correct": False,
             "why": "It is broken down and cleared, more slowly in the foetus "
                    "than in the mother. What lasts the whole pregnancy is the "
                    "building of the nervous system."},
            {"text": "Because the brain and nervous system are being built and "
                     "rebuilt from the first weeks to the last",
             "correct": True},
            {"text": "Because the placenta passes more alcohol as a pregnancy "
                     "goes on", "correct": False,
             "why": "The surface does not change what it passes. The reason "
                    "the window is the whole pregnancy is on the other side of "
                    "it."},
            {"text": "Because alcohol is the only substance that crosses at "
                     "every stage", "correct": False,
             "why": "Caffeine, carbon monoxide and nicotine all cross "
                    "throughout as well. What is unusual is what alcohol "
                    "reaches, not when."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h10",
        "band": "harder",
        "text": "Insulin is held back while the mother's glucose crosses "
                "freely. What general point does that pair make?",
        "options": [
            {"text": "That the placenta passes only substances the foetus can "
                     "use", "correct": False,
             "why": "It passes alcohol and carbon monoxide, which no foetus "
                    "can use. Usefulness is not a property the surface can "
                    "read."},
            {"text": "That hormones are held back and nutrients are passed",
             "correct": False,
             "why": "The grouping is by size, not by what a substance is "
                    "called. A small hormone molecule would cross as readily "
                    "as glucose."},
            {"text": "That size decides what crosses, whatever the substance "
                     "does", "correct": True},
            {"text": "That the placenta holds back anything that would raise "
                     "the foetus's glucose", "correct": False,
             "why": "Glucose itself crosses freely and raises it. The one "
                    "thing held back is the large protein."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h11",
        "band": "harder",
        "text": "A new medicine is a very small molecule that dissolves in "
                "blood. Before any testing at all, what can be predicted and "
                "what cannot?",
        "options": [
            {"text": "Both can be predicted from the size of the molecule "
                     "alone, without any testing", "correct": False,
             "why": "Size predicts the crossing and nothing else. What a "
                    "substance does once it arrives has to be measured."},
            {"text": "That it will cross can be predicted; whether it does "
                     "harm cannot", "correct": True},
            {"text": "Neither can be predicted until the medicine has been "
                     "tested in a pregnancy", "correct": False,
             "why": "The crossing can be predicted: a small soluble molecule "
                    "diffuses across an exchange surface, and that is settled "
                    "before any testing."},
            {"text": "That it does harm can be predicted; that it crosses "
                     "cannot", "correct": False,
             "why": "That is the wrong way round. Crossing follows from the "
                    "molecule; harm is the open question."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h12",
        "band": "harder",
        "text": "Why does calling the placenta a neutral surface change how a "
                "complication can be explained?",
        "options": [
            {"text": "Because it passes harmful substances a good deal more "
                     "slowly than it passes the useful ones a foetus needs",
             "correct": False,
             "why": "It passes them on identical terms. Nothing about a "
                    "substance's effects changes how fast it diffuses."},
            {"text": "Because it lets nothing across during the first two "
                     "weeks", "correct": False,
             "why": "There is no such closed period. The first fortnight "
                    "matters because there are no organs yet, not because "
                    "nothing crosses."},
            {"text": "Because it protects against everything except viruses",
             "correct": False,
             "why": "It protects against nothing. Alcohol, caffeine, nicotine "
                    "and carbon monoxide all cross without hindrance."},
            {"text": "Because nothing is sorted at all, so there is no point "
                     "at which something got through that should not have",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h13",
        "band": "harder",
        "text": "One pregnancy meets carbon monoxide only in the first "
                "fortnight, and another meets rubella only at week thirty. "
                "Predict the outcome of each.",
        "options": [
            {"text": "Both are likely to matter far less than they would in "
                     "their own windows", "correct": True},
            {"text": "Both would do the maximum damage that they are capable "
                     "of doing", "correct": False,
             "why": "Each has met the exposure outside the window in which it "
                    "does most. Carbon monoxide limits growth, and rubella "
                    "damages structures being formed."},
            {"text": "Carbon monoxide would matter most, and rubella would "
                     "matter least", "correct": False,
             "why": "Carbon monoxide is a supply problem and the first "
                    "fortnight has almost nothing to supply. Both are outside "
                    "their windows."},
            {"text": "Neither substance would reach the developing organism at "
                     "those times", "correct": False,
             "why": "Both reach it at any stage. What changes with the week is "
                    "what they find when they get there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h14",
        "band": "harder",
        "text": "Thalidomide is described as never having been the villain — "
                "the missing knowledge was. Evaluate that claim.",
        "options": [
            {"text": "It is wrong, because the harm has since been shown not "
                     "to have happened at all", "correct": False,
             "why": "Thousands of babies were affected, and the pattern was "
                    "traced twice, independently, in two countries."},
            {"text": "It is right, because the substance was chemically "
                     "altered before it came back into use", "correct": False,
             "why": "It is the same substance. What changed is the knowledge "
                    "of who must never take it."},
            {"text": "It is wrong, because a substance that causes harm is "
                     "harmful whatever anybody knows", "correct": False,
             "why": "The same substance is used safely today under controls, "
                    "which is precisely the point: the effect depended on who "
                    "took it and when."},
            {"text": "It is right — the effect depended on when it was taken, "
                     "which nobody yet knew", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h15",
        "band": "harder",
        "text": "A large dose of a drug does not kill adult laboratory "
                "animals. What does that establish about its use in a "
                "pregnancy?",
        "options": [
            {"text": "That it is safe for anyone at all to take",
             "correct": False,
             "why": "It establishes something about adult animals at a large "
                    "dose and nothing else. That was, in 1957, most of what "
                    "safe testing meant."},
            {"text": "Very little — a substance can be harmless to an adult "
                     "and damaging to a developing organism", "correct": True},
            {"text": "That the substance does not cross the placenta",
             "correct": False,
             "why": "A test on adult animals says nothing about a placenta. "
                    "Whether it crosses depends on the molecule."},
            {"text": "That it would only become harmful at a dose a great "
                     "deal larger than the one used in the test",
             "correct": False,
             "why": "The thalidomide damage did not need a large dose. What "
                    "mattered was which days of the pregnancy the tablets were "
                    "taken."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h16",
        "band": "harder",
        "text": "One medicine crosses the placenta and another does not. Why "
                "is that pair of facts not enough to choose between them?",
        "options": [
            {"text": "Because a medicine that does not cross cannot work at "
                     "all", "correct": False,
             "why": "It works on the person taking it, which is the point of "
                    "insulin in pregnancy. Not crossing is not the same as not "
                    "working."},
            {"text": "Because the placenta's behaviour changes from week to "
                     "week", "correct": False,
             "why": "The surface behaves the same way throughout. What changes "
                    "with the week is what is being built."},
            {"text": "Because what each one treats, and the risk of leaving it "
                     "untreated, has to be weighed too", "correct": True},
            {"text": "Because both of those statements turn out to be false "
                     "for almost any real medicine that is in use",
             "correct": False,
             "why": "Both are perfectly ordinary facts about medicines. The "
                    "point is that they do not settle the decision on their "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h17",
        "band": "harder",
        "text": "Nicotine narrows blood vessels and carbon monoxide occupies "
                "haemoglobin. Why do the two together matter more than either "
                "would alone?",
        "options": [
            {"text": "Because nicotine makes carbon monoxide cross the "
                     "placenta more easily than it otherwise would",
             "correct": False,
             "why": "Carbon monoxide crosses easily on its own. Nicotine's "
                    "effect is on the vessels carrying blood to the placenta."},
            {"text": "Because the two join into a single larger molecule that "
                     "the placenta cannot pass", "correct": False,
             "why": "They do not combine. They act separately, and both act "
                    "against the oxygen supply."},
            {"text": "Because nicotine stops the foetal liver breaking carbon "
                     "monoxide down", "correct": False,
             "why": "Carbon monoxide is not dealt with by the liver. It is "
                    "displaced from haemoglobin when there is oxygen to take "
                    "its place."},
            {"text": "Because both reduce the oxygen reaching the placenta, by "
                     "different routes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h18",
        "band": "harder",
        "text": "A foetus breaks both alcohol and caffeine down slowly. Why "
                "does that matter as much as how fast each one crosses?",
        "options": [
            {"text": "Because a slow breakdown means less of it crossed in the "
                     "first place", "correct": False,
             "why": "Breakdown happens after arrival and changes nothing about "
                    "the crossing. It changes how long the substance stays."},
            {"text": "Because the foetus is exposed for longer than the mother "
                     "is, whatever the crossing rate", "correct": True},
            {"text": "Because the placenta stops passing a substance once "
                     "the level on the foetal side is high enough",
             "correct": False,
             "why": "It never stops passing anything. Diffusion slows as the "
                    "two sides even out, which is not the same as a decision "
                    "to stop."},
            {"text": "Because the mother's liver takes over the breakdown for "
                     "both of them", "correct": False,
             "why": "Her liver works on what is in her own blood. The foetus "
                    "has to deal with what is in its own, with a much less "
                    "developed liver."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h19",
        "band": "harder",
        "text": "A researcher measures a substance in the mother's blood and "
                "in the foetus's blood and finds the two concentrations equal. "
                "What can be concluded?",
        "options": [
            {"text": "That the two blood supplies have mixed somewhere in the "
                     "placenta", "correct": False,
             "why": "Equal concentrations are what diffusion across a surface "
                    "produces. The two circulations stay separate throughout."},
            {"text": "That the placenta is carrying the substance across using "
                     "energy", "correct": False,
             "why": "Carrying is used for large molecules such as antibodies. "
                    "Levelling out on both sides is the signature of "
                    "diffusion."},
            {"text": "That the foetus is producing the substance itself",
             "correct": False,
             "why": "If it were, the foetal level would be the higher of the "
                    "two. Equal levels point to free movement across the "
                    "surface."},
            {"text": "That it crosses easily", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h20",
        "band": "harder",
        "text": "“Small and dissolves in blood means it crosses.” Evaluate "
                "that rule, and say where it would let a student down.",
        "options": [
            {"text": "It is a good rule, and it fails only for insulin",
             "correct": False,
             "why": "Insulin is the case it handles best: a large protein does "
                    "not cross. What it misses are the cases that cross "
                    "without diffusing."},
            {"text": "It is a good rule, but it misses viruses and molecules "
                     "carried across using energy", "correct": True},
            {"text": "It is a poor rule, because how harmful a substance is "
                     "decides whether it crosses at all", "correct": False,
             "why": "Harm decides nothing at the placenta. The rule's problem "
                    "is that diffusion is not the only route, not that the "
                    "rule is about the wrong thing."},
            {"text": "It is a poor rule, because everything crosses in the "
                     "end", "correct": False,
             "why": "Insulin does not, in any useful amount, and that is why "
                    "it can treat diabetes in pregnancy."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h21",
        "band": "harder",
        "text": "The placenta spends energy carrying antibodies over but does "
                "nothing to keep alcohol out. Why is that not inconsistent?",
        "options": [
            {"text": "Because alcohol is carried across by that same "
                     "mechanism", "correct": False,
             "why": "Alcohol needs no mechanism. It diffuses, using the route "
                    "built for oxygen and glucose."},
            {"text": "Because antibodies are smaller than alcohol molecules "
                     "are", "correct": False,
             "why": "An antibody is a large protein and a molecule of alcohol "
                    "is tiny. That is why one has to be carried and the other "
                    "does not."},
            {"text": "Because carrying something over is a mechanism the "
                     "placenta has, and blocking is not", "correct": True},
            {"text": "Because the placenta spends energy only on what the "
                     "foetus needs, which is a kind of sorting",
             "correct": False,
             "why": "Choosing what to carry in is not the same as choosing "
                    "what to keep out. Nothing is kept out except by size."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h22",
        "band": "harder",
        "text": "A student argues that because the foetal concentration of "
                "alcohol matches the mother's, the effect on each must be the "
                "same. Where does that go wrong?",
        "options": [
            {"text": "The two concentrations are not in fact equal",
             "correct": False,
             "why": "They end up roughly equal, which is the part of the "
                    "argument that is right. What differs is what the alcohol "
                    "meets on each side."},
            {"text": "The foetus breaks the alcohol down a good deal faster "
                     "than an adult body manages to", "correct": False,
             "why": "Far more slowly, with a much less developed liver, so the "
                    "alcohol stays in its blood longer."},
            {"text": "Alcohol has no effect at all on a nervous system that "
                     "is still developing", "correct": False,
             "why": "The developing brain and nervous system are exactly where "
                    "its clearest effects are."},
            {"text": "The foetus has a much less developed liver and a nervous "
                     "system still being built", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h23",
        "band": "harder",
        "text": "Weeks three to eight are six weeks out of forty. Why does so "
                "short a stretch carry so much weight for structure?",
        "options": [
            {"text": "Because the foetus grows fastest during those weeks",
             "correct": False,
             "why": "Growth is the business of the second half. Those six "
                    "weeks are when structures are laid down rather than "
                    "enlarged."},
            {"text": "Because the placenta is at its very thinnest during "
                     "those particular weeks of the pregnancy",
             "correct": False,
             "why": "The thickness of the surface is not what the window is "
                    "about. It is about what is being built on the other side "
                    "of it."},
            {"text": "Because almost every organ is laid down in them, and "
                     "that is largely over by week eight", "correct": True},
            {"text": "Because most exposures happen to fall in those weeks",
             "correct": False,
             "why": "Exposures are spread across a pregnancy. The window is "
                    "about consequence, not about frequency."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h24",
        "band": "harder",
        "text": "Two people learn the same fact about a prescribed medicine. "
                "One stops taking it that day; the other asks a pharmacist. "
                "Which course is safer, and why?",
        "options": [
            {"text": "Stopping, because a medicine that crosses will do harm "
                     "sooner or later", "correct": False,
             "why": "Crossing does not settle whether harm follows, and the "
                    "untreated condition carries a risk of its own."},
            {"text": "Stopping, because the risk is highest in the first few "
                     "weeks", "correct": False,
             "why": "Weeks three to eight are the most sensitive for "
                    "structure, but that is a reason to ask early rather than "
                    "to stop unaided."},
            {"text": "Neither course is safer, because the decision comes "
                     "out the same either way", "correct": False,
             "why": "It often does not. Many medicines are continued precisely "
                    "because stopping them is the greater danger."},
            {"text": "Asking, because stopping a prescribed medicine can be "
                     "the greater risk", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h25",
        "band": "harder",
        "text": "Evaluate this claim: “the placenta protects the foetus from "
                "most harmful things.”",
        "options": [
            {"text": "Broadly right, since most of the harmful substances "
                     "there are happen to be large molecules",
             "correct": False,
             "why": "Alcohol, nicotine, carbon monoxide and caffeine are all "
                    "small, and all cross. Size does not line up with harm."},
            {"text": "Right for viruses and wrong for small molecules",
             "correct": False,
             "why": "Rubella is a virus and it crosses too, by infecting the "
                    "placenta's own cells. Nothing is protected against."},
            {"text": "Wrong — it never protects against anything, and what "
                     "stays behind does so because of size", "correct": True},
            {"text": "Right in the first twelve weeks and wrong after that",
             "correct": False,
             "why": "There is no stage at which it sorts. What changes over a "
                    "pregnancy is what an arriving substance can affect."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h26",
        "band": "harder",
        "text": "A substance lowers the amount of oxygen the mother's blood "
                "can carry, but does not itself cross the placenta at all. "
                "Would the foetus be affected?",
        "options": [
            {"text": "No, because the substance itself never arrives",
             "correct": False,
             "why": "It does not have to arrive. Less oxygen reaching the "
                    "placenta means less oxygen crossing it."},
            {"text": "No, because a foetus makes its own oxygen supply",
             "correct": False,
             "why": "It makes none at all. Every molecule of oxygen it uses "
                    "crosses the placenta from the mother's blood."},
            {"text": "Only if the substance crossed later in the pregnancy",
             "correct": False,
             "why": "The effect does not depend on the substance crossing at "
                    "any point. It is the oxygen that crosses, and there is "
                    "less of it."},
            {"text": "Yes — less oxygen reaches the placenta, so less crosses "
                     "it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h27",
        "band": "harder",
        "text": "The damage thalidomide caused shifted with the particular "
                "days on which the tablets were taken. Why did that make the "
                "case decisive rather than merely suggestive?",
        "options": [
            {"text": "Because a pattern that tracks timing that precisely is "
                     "very hard to explain any other way", "correct": True},
            {"text": "Because laboratory animals had already shown exactly "
                     "the same pattern before the drug went on sale",
             "correct": False,
             "why": "They had not, which is why the drug was believed safe. "
                    "The pattern was found in people, afterwards."},
            {"text": "Because the drug had never been tested on anything at "
                     "all before sale", "correct": False,
             "why": "It had been tested, on adult animals at a large dose. The "
                    "testing was the wrong testing rather than absent."},
            {"text": "Because the effect was the same whichever week the "
                     "tablets were taken", "correct": False,
             "why": "It was the opposite: the specific malformation changed "
                    "with the day, and that is what mapped the sensitive "
                    "window."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h28",
        "band": "harder",
        "text": "Alcohol diffuses across, antibodies are carried across, and "
                "rubella infects cells to get across. What do three different "
                "routes show?",
        "options": [
            {"text": "That the placenta picks a route to suit each substance",
             "correct": False,
             "why": "Nothing picks anything. Each substance uses whichever "
                    "route its own size and nature allow."},
            {"text": "That only diffusion is a real crossing and the other two "
                     "are not", "correct": False,
             "why": "All three end with the substance on the foetal side. The "
                    "consequences are the same however it got there."},
            {"text": "That each route belongs to a different stage of a "
                     "pregnancy", "correct": False,
             "why": "All three operate throughout. The route depends on the "
                    "substance, not on the week."},
            {"text": "That there is more than one way across, and none of them "
                     "sorts for harm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h29",
        "band": "harder",
        "text": "Compare a rule that says “if it crosses the placenta, avoid "
                "it” with the position the lesson takes.",
        "options": [
            {"text": "The rule would agree with the lesson in every case",
             "correct": False,
             "why": "It would not. The lesson says a prescribed medicine that "
                    "crosses may still be the safer choice."},
            {"text": "The rule would be too cautious about caffeine and about "
                     "nothing else", "correct": False,
             "why": "Its most serious failure is with prescribed medicines, "
                    "where stopping can be considerably more dangerous than "
                    "continuing."},
            {"text": "The rule would mean stopping prescribed medicines that "
                     "are safer to continue", "correct": True},
            {"text": "The rule would fail only for insulin, which does not "
                     "cross anyway", "correct": False,
             "why": "Insulin is the case the rule gets right by accident. It "
                    "fails on the medicines that do cross and are still worth "
                    "taking."},
        ],
        "figure": None,
    },
    {
        "id": "b5-05-h30",
        "band": "harder",
        "text": "Insulin is offered as proof that the crossing rule is about "
                "size and not about safety. Set out that argument.",
        "options": [
            {"text": "Insulin is kept out because it would lower the foetus's "
                     "glucose too far", "correct": False,
             "why": "Nothing is kept out for a reason. Insulin is a large "
                    "protein and does not fit through an exchange surface."},
            {"text": "Insulin is kept out because it is a medicine rather than "
                     "a nutrient", "correct": False,
             "why": "Plenty of medicines cross freely. What separates insulin "
                    "from them is the size of its molecules."},
            {"text": "Insulin crosses in small amounts, which is why the "
                     "mother's glucose still has to be controlled",
             "correct": False,
             "why": "It does not arrive in any useful amount. Glucose is what "
                    "crosses, and that is why her level matters."},
            {"text": "Nothing decided insulin should be held back; it is a "
                     "large protein, and that is all", "correct": True},
        ],
        "figure": None,
    },
]
