"""Biology · Infection & response — the MRB-338 expansion, subtopic
`viral-diseases`.

The original twelve rows take a virus's basic structure, TMV as an example
disease, antiretroviral drugs, and a measles complication at easier;
measles clearing without an antiviral, TMV spread on tools, HIV's silent
progression, and droplet spread in a school at standard; and a mineral
deficiency versus TMV, why antivirals are harder to develop than
antibiotics, blood screening despite honest donors, and rising HIV
prevalence under a good treatment programme at harder.

This file takes what they leave: Koplik's spots and the order a measles
rash spreads, the T-helper lymphocyte HIV specifically destroys and how it
reaches a baby, the named plants TMV infects besides tobacco, how a virus
uses a host cell's own machinery, and the whole mechanism this subtopic
turns on — that a virus is not a living cell and cannot be killed the way
a drug kills a bacterium, so treatment manages a viral infection rather
than curing it. Comparison and evaluation sit at `harder`, because the
genuine demand here is applying that one idea — no cure, only control — to
an unfamiliar case each time, alongside genuine two-step biology such as
distinguishing a fresh from a resolved HIV infection.
"""

TOPIC = "infection-response"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    {
        "id": "ks4-viral-diseases-e05",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name of the white spots that can appear inside "
                "the mouth during measles, and are used to diagnose it.",
        "options": [
            "Koplik's spots",
            "Rash spots, said to appear a week before any fever begins",
            "Fever spots, which are claimed to clear within a single hour",
            "Measles spots, which are said to appear on the hands only",
        ],
        "correct_index": 0,
        "why": "Koplik's spots are small white spots inside the mouth that "
               "are a recognised early sign of measles.",
    },
    {
        "id": "ks4-viral-diseases-e06",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the order in which a measles rash typically spreads "
                "across the body.",
        "options": [
            "It is said to appear everywhere on the body at exactly the "
            "same moment",
            "From the face, spreading down to the rest of the body",
            "It is claimed to spread from the feet upward towards the "
            "face",
            "From the chest outward to the arms and legs equally",
        ],
        "correct_index": 1,
        "why": "The measles rash characteristically starts on the face and "
               "then spreads downward over the following days.",
    },
    {
        "id": "ks4-viral-diseases-e07",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of lymphocyte that HIV specifically targets "
                "and destroys.",
        "options": [
            "Red blood cells, which HIV is said to invade and destroy",
            "Phagocytes, which HIV is claimed to disable permanently",
            "T-helper lymphocytes",
            "B-lymphocytes, said to be the only cells HIV ever infects",
        ],
        "correct_index": 2,
        "why": "HIV specifically infects and destroys T-helper "
               "lymphocytes, the cells that coordinate the wider immune "
               "response.",
    },
    {
        "id": "ks4-viral-diseases-e08",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how HIV can pass from a mother to her baby.",
        "options": [
            "Only ever through breastfeeding, and never at any other time",
            "Only if the mother has already developed AIDS herself",
            "Only during birth itself, and at no other stage",
            "During pregnancy, during birth, or through breastfeeding",
        ],
        "correct_index": 3,
        "why": "HIV can be passed from mother to baby at any of three "
               "points: during pregnancy, during birth, or through "
               "breastfeeding.",
    },
    {
        "id": "ks4-viral-diseases-e09",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what antiretroviral drugs do to HIV inside the body.",
        "options": [
            "They stop HIV replicating",
            "They are said to kill HIV directly outside of any cell",
            "They are claimed to replace the lymphocytes HIV has already "
            "destroyed",
            "They vaccinate the patient against catching HIV again",
        ],
        "correct_index": 0,
        "why": "Antiretroviral drugs work by stopping HIV from making "
               "further copies of itself inside the patient's cells.",
    },
    {
        "id": "ks4-viral-diseases-e10",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name three crops, besides tobacco, that tobacco mosaic "
                "virus is known to infect.",
        "options": [
            "Wheat, barley and rice, which are all said to carry TMV",
            "Tomatoes, peppers and cucumbers",
            "Potatoes, carrots and onions, claimed to be common TMV hosts",
            "Roses, orchids and lilies, said to be frequently infected",
        ],
        "correct_index": 1,
        "why": "Tobacco mosaic virus infects a wide range of plants "
               "besides tobacco, including tomatoes, peppers and "
               "cucumbers.",
    },
    {
        "id": "ks4-viral-diseases-e11",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a virus uses to make copies of itself once it "
                "is inside a host cell.",
        "options": [
            "It is said to use its own separate set of ribosomes",
            "Enzymes it is claimed to manufacture before entering the "
            "cell",
            "The host cell's own machinery",
            "Nutrients absorbed directly from the patient's blood",
        ],
        "correct_index": 2,
        "why": "A virus has no machinery of its own to reproduce, so it "
               "hijacks the host cell's machinery to make new copies of "
               "itself.",
    },
    {
        "id": "ks4-viral-diseases-e12",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which class of drug specifically targets HIV to stop "
                "it replicating.",
        "options": [
            "Antibiotics, said to be effective against HIV specifically",
            "Antifungals, claimed to stop HIV multiplying inside cells",
            "Painkillers, which are said to slow the virus down directly",
            "Antiretroviral drugs",
        ],
        "correct_index": 3,
        "why": "Antiretroviral drugs are the class of drug developed "
               "specifically to stop HIV replicating.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    {
        "id": "ks4-viral-diseases-s05",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the fever and aches a person feels during a "
                "viral infection are not caused directly by the virus "
                "itself.",
        "options": [
            "They are mostly caused by the immune system's own response "
            "to fighting the infection",
            "They are caused by toxins the virus is said to release into "
            "the bloodstream as it spreads",
            "They are caused by the host cells bursting open, which is "
            "claimed to trigger pain receptors directly",
            "They are caused by the virus multiplying so fast that body "
            "temperature is said to rise on its own",
        ],
        "correct_index": 0,
        "why": "Symptoms such as fever and aches largely reflect the "
               "immune system working to fight the virus, not damage done "
               "by the virus itself.",
    },
    {
        "id": "ks4-viral-diseases-s06",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A child develops a rash on the chest, a high fever and a "
                "cough. Explain why a doctor might suspect measles before "
                "checking for Koplik's spots.",
        "options": [
            "These three signs together occur in measles and in no "
            "other childhood illness, so they confirm it",
            "Fever, cough and rash together fit the usual pattern of "
            "measles",
            "A cough on its own is enough to diagnose measles, so the "
            "rash and the fever add nothing to the judgement",
            "A rash on the chest is a feature of measles and of no "
            "other viral illness, so the cough can be set aside",
        ],
        "correct_index": 1,
        "why": "The combination of fever, cough and rash fits the pattern "
               "doctors associate with measles, though Koplik's spots give "
               "a more specific confirmation.",
    },
    {
        "id": "ks4-viral-diseases-s07",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why unvaccinated adults are advised to have the "
                "MMR vaccine even if they believe they already had measles "
                "as a child.",
        "options": [
            "Immunity from a past infection is said to fade completely "
            "within around ten years",
            "The MMR vaccine is claimed to remove any measles infection "
            "already present in the body",
            "A childhood illness remembered as measles may have been a "
            "different infection with similar symptoms",
            "Vaccination as an adult is claimed to be more effective than "
            "the immunity gained from an actual infection",
        ],
        "correct_index": 2,
        "why": "Without a confirmed diagnosis at the time, a remembered "
               "illness cannot be relied on as proof of measles immunity.",
    },
    {
        "id": "ks4-viral-diseases-s08",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person newly infected with HIV can "
                "unknowingly infect others for years before any symptoms "
                "of AIDS appear.",
        "options": [
            "Early HIV infection produces no virus particles in any "
            "body fluid, so transmission cannot happen yet",
            "HIV stays dormant and non-infectious for several years, "
            "becoming transmissible when symptoms begin",
            "A person becomes infectious once AIDS has developed, "
            "some years after they were first infected",
            "The virus is in body fluids long before enough T-helper "
            "cells are destroyed",
        ],
        "correct_index": 3,
        "why": "The virus can be transmitted from early in an infection, "
               "long before the immune system has been damaged enough for "
               "symptoms to appear.",
    },
    {
        "id": "ks4-viral-diseases-s09",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why AIDS is defined by the appearance of "
                "opportunistic infections rather than by a measurement of "
                "HIV in the blood alone.",
        "options": [
            "The clinical harm of AIDS is that the weakened immune system "
            "allows infections a healthy body would otherwise resist",
            "A blood measurement of HIV is said to be technically "
            "impossible to carry out reliably",
            "Opportunistic infections are claimed to occur before HIV "
            "itself is even present in the blood",
            "The level of HIV in the blood is said to have no "
            "relationship whatsoever to how weak the immune system has "
            "become",
        ],
        "correct_index": 0,
        "why": "AIDS is defined by its clinical effect — the immune system "
               "becoming too weak to resist infections it would normally "
               "handle easily.",
    },
    {
        "id": "ks4-viral-diseases-s10",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a baby born to a mother with HIV is given "
                "antiretroviral treatment immediately after birth, even "
                "before any test confirms infection.",
        "options": [
            "The treatment is said to be harmless, so giving it "
            "immediately removes any need for testing at all",
            "Starting treatment early reduces the chance the virus "
            "becomes established if transmission did occur around birth",
            "A newborn baby is claimed to be unable to be tested for HIV "
            "until several years old",
            "Antiretroviral treatment is said to prevent every possible "
            "future infection the baby might ever go on to catch",
        ],
        "correct_index": 1,
        "why": "Starting treatment straight away gives the best chance of "
               "preventing the virus taking hold if transmission happened "
               "around the time of birth.",
    },
    {
        "id": "ks4-viral-diseases-s11",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tomato grower finds mosaic-patterned leaves on one plant "
                "and removes it immediately, rather than waiting to see if "
                "it recovers. Explain why.",
        "options": [
            "TMV is said to be curable within a few days if the plant is "
            "simply left alone",
            "Removing the plant is claimed to be required only once the "
            "whole crop has become infected",
            "There is no cure for TMV, and an infected plant remains a "
            "source of the virus for as long as it survives",
            "A mosaic-patterned leaf is said to recover fully by itself "
            "once new growth appears the following growing season",
        ],
        "correct_index": 2,
        "why": "With no cure available, an infected plant left in place "
               "continues to act as a source the virus can spread from.",
    },
    {
        "id": "ks4-viral-diseases-s12",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a mosaic-patterned tomato leaf produces less "
                "fruit than a healthy leaf on the same plant.",
        "options": [
            "The virus is claimed to consume the sugars the leaf has "
            "already made before they can reach the fruit",
            "A mosaic-patterned leaf is claimed to lose its stomata "
            "completely, stopping gas exchange",
            "TMV is said to block the flow of water into the leaf "
            "entirely, stopping photosynthesis outright",
            "The patterned areas make less chlorophyll, so the leaf "
            "photosynthesises less and makes less glucose",
        ],
        "correct_index": 3,
        "why": "The mosaic patches have reduced chlorophyll, so those "
               "areas of the leaf photosynthesise less and the whole plant "
               "makes less food.",
    },
    {
        "id": "ks4-viral-diseases-s13",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why TMV outbreaks are more likely on a farm that "
                "reuses the same pruning tools across different fields "
                "without cleaning them.",
        "options": [
            "Sap carrying the virus can be carried on the blade from an "
            "infected plant straight into the next plant's cut tissue",
            "Dirty tools are said to attract the insects that are claimed "
            "to be TMV's main vector",
            "Unwashed tools are claimed to lower the soil pH enough by "
            "themselves for TMV to be able to survive between fields",
            "TMV is said to be produced by the rust that forms on "
            "unwashed metal tools",
        ],
        "correct_index": 0,
        "why": "TMV spreads readily by contact, and a contaminated blade "
               "carries infected sap directly into the next plant it "
               "touches.",
    },
    {
        "id": "ks4-viral-diseases-s14",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why growers use virus-free certified seed rather "
                "than seed saved from a previous crop that showed no "
                "symptoms.",
        "options": [
            "Certified seed is claimed to be genetically resistant to "
            "every plant disease that exists",
            "A symptom-free plant can still be carrying TMV without "
            "showing visible signs of it",
            "Saved seed is said to always carry TMV, regardless of "
            "whether the parent plant showed symptoms",
            "Certified seed is said to grow faster than any saved seed, "
            "for reasons unrelated to disease",
        ],
        "correct_index": 1,
        "why": "A plant can be infected with TMV without showing visible "
               "symptoms, so the absence of symptoms is not proof the "
               "seed is virus-free.",
    },
    {
        "id": "ks4-viral-diseases-s15",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a virus destroys the host cell it has "
                "infected once it has finished replicating inside it.",
        "options": [
            "The virus is claimed to inject a toxin into the cell once "
            "replication is complete",
            "The host cell is said to digest itself once the virus's "
            "genetic material has been copied",
            "New virus particles burst out of the cell, breaking it open "
            "as they are released",
            "The immune system is said to destroy the host cell before "
            "the virus can leave it",
        ],
        "correct_index": 2,
        "why": "New virus particles are released by bursting out of the "
               "host cell, which destroys it in the process.",
    },
    {
        "id": "ks4-viral-diseases-s16",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says HIV and AIDS are the same thing. Explain "
                "the distinction between the two.",
        "options": [
            "HIV is the drug used to treat the condition known as "
            "AIDS, which is the name given to the virus itself",
            "AIDS is the virus; HIV is the set of symptoms that "
            "appears later",
            "The two terms describe the same stage of the same "
            "infection and can be used interchangeably",
            "HIV is the virus; AIDS is the condition it leads to only "
            "once the immune system is damaged",
        ],
        "correct_index": 3,
        "why": "HIV is the virus that causes the infection; AIDS is the "
               "later condition that results once the virus has weakened "
               "the immune system enough.",
    },
    {
        "id": "ks4-viral-diseases-s17",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why doctors monitor a HIV-positive patient's "
                "T-helper lymphocyte count over time.",
        "options": [
            "The count shows how much damage the virus has done to the "
            "immune system and how well treatment is working",
            "The count is said to determine how the virus was originally "
            "transmitted to the patient",
            "T-helper lymphocyte counts are claimed to have no "
            "relationship to how weak the immune system has become",
            "Monitoring the count is said to be required only once AIDS "
            "has already developed",
        ],
        "correct_index": 0,
        "why": "The T-helper lymphocyte count is a direct measure of how "
               "much immune damage HIV has caused and how well treatment "
               "is controlling the infection.",
    },
    {
        "id": "ks4-viral-diseases-s18",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why antiretroviral drugs must be taken every day "
                "for the rest of a patient's life, rather than as a single "
                "course.",
        "options": [
            "The drugs are said to lose their effectiveness permanently "
            "after only a few weeks of use",
            "The drugs control HIV replication but do not remove the "
            "virus from the body, so stopping lets it multiply again",
            "A single course is claimed to be enough to fully clear HIV, "
            "but only from the blood and not from other body tissues",
            "Daily doses are said to be required purely to prevent the "
            "drug being passed on to other people",
        ],
        "correct_index": 1,
        "why": "Antiretrovirals suppress the virus rather than removing "
               "it, so the infection would begin multiplying again if "
               "treatment stopped.",
    },
    {
        "id": "ks4-viral-diseases-s19",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why measles is more dangerous to a malnourished "
                "child than to a well-nourished one.",
        "options": [
            "The measles virus replicates much faster inside the body "
            "cells of a malnourished child than a well-fed one",
            "A malnourished child cannot make antibodies against "
            "measles at any stage, so the virus is left unchecked",
            "A weaker immune response makes serious complications "
            "more likely",
            "Malnutrition brings the Koplik's spots out earlier",
        ],
        "correct_index": 2,
        "why": "Malnutrition weakens the immune response, so a "
               "malnourished child is less able to fight off measles and "
               "more likely to develop serious complications.",
    },
    {
        "id": "ks4-viral-diseases-s20",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a school reports a confirmed measles case to "
                "public health authorities immediately.",
        "options": [
            "Measles is said to be reportable only once several confirmed "
            "cases have already been recorded at that same school",
            "Public health authorities are said to be the only body able "
            "to prescribe the MMR vaccine",
            "Reporting a case is claimed to be required only if a child "
            "is admitted to hospital",
            "Rapid action lets unvaccinated contacts be identified and "
            "offered protection before the virus spreads further",
        ],
        "correct_index": 3,
        "why": "Acting quickly gives the best chance of protecting "
               "unvaccinated contacts before the highly infectious virus "
               "has a chance to spread further.",
    },
    {
        "id": "ks4-viral-diseases-s21",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why TMV cannot be treated with an antiviral spray "
                "once a plant is infected.",
        "options": [
            "No treatment exists that removes TMV from a plant once it "
            "has already infected the plant's cells",
            "Antiviral sprays are said to work well against TMV but are "
            "simply too expensive for most growers to buy",
            "TMV is claimed to be resistant only to sprays applied after "
            "midday, and effective earlier in the day",
            "Antiviral sprays are said to kill TMV outright but leave the "
            "plant unable to recover afterwards",
        ],
        "correct_index": 0,
        "why": "There is no treatment that removes TMV once a plant is "
               "infected, which is why prevention and removal are the "
               "only real controls.",
    },
    {
        "id": "ks4-viral-diseases-s22",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient who tests positive for HIV asks whether "
                "antiretroviral treatment will cure them. Explain the "
                "correct answer.",
        "options": [
            "Yes, provided the treatment is taken correctly for at least "
            "one full year without a break",
            "No; the drugs control the virus and allow a near-normal "
            "life, but the infection itself remains in the body",
            "Yes; the drugs remove HIV from the body entirely once the "
            "T-helper count has returned fully to normal",
            "No; the drugs are said to have no measurable effect on how "
            "the infection progresses at all",
        ],
        "correct_index": 1,
        "why": "Antiretroviral treatment controls HIV rather than curing "
               "it — the virus stays in the body even while the patient "
               "remains well.",
    },
    {
        "id": "ks4-viral-diseases-s23",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why encephalitis, a complication of measles, can "
                "be more serious than the rash itself.",
        "options": [
            "The rash is claimed to be permanent, while encephalitis is "
            "said to clear within a day or two",
            "Encephalitis is said to be simply a more severe form of "
            "that very same skin rash, just spread over a larger area",
            "Encephalitis is inflammation of the brain, which can cause "
            "lasting damage or death, unlike the rash, which fades on its "
            "own",
            "Encephalitis is said to only ever occur in patients who have "
            "already fully recovered from the rash",
        ],
        "correct_index": 2,
        "why": "Encephalitis affects the brain directly and can cause "
               "permanent damage or death, which is far more serious than "
               "the temporary skin rash.",
    },
    {
        "id": "ks4-viral-diseases-s24",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a country with a high measles vaccination rate "
                "can still see occasional local outbreaks.",
        "options": [
            "Outbreaks are said to occur only when the vaccine itself has "
            "stopped working nationwide",
            "A high national vaccination rate is said to make local "
            "outbreaks statistically impossible under any circumstances",
            "Measles is claimed to only spread in countries with low "
            "vaccination rates overall",
            "Pockets of unvaccinated people can still let the virus "
            "spread locally, even where the national average is high",
        ],
        "correct_index": 3,
        "why": "A national average can hide local pockets of low coverage, "
               "and the virus can still spread readily within one of "
               "those pockets.",
    },
    {
        "id": "ks4-viral-diseases-s25",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a virus is described as unable to reproduce on "
                "its own.",
        "options": [
            "It has no cell structure of its own, so it can only copy "
            "itself inside a host cell",
            "It has no genetic material of its own until it copies "
            "some from the nucleus of a host cell",
            "It runs out of stored energy within a few minutes unless "
            "a host cell keeps supplying it",
            "It needs sunlight in order to copy its genes",
        ],
        "correct_index": 0,
        "why": "A virus has no cell structure of its own, so it cannot "
               "carry out the processes of reproduction without taking "
               "over a living host cell.",
    },
    {
        "id": "ks4-viral-diseases-s26",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one reason screening blood donations for HIV "
                "remains necessary even in countries with high public "
                "awareness of the virus.",
        "options": [
            "Public awareness of HIV is said to remove the need for any "
            "kind of laboratory testing whatsoever",
            "A recently infected donor can be unaware they carry the "
            "virus, however well informed they are generally",
            "Screening is claimed to be required only in countries where "
            "HIV was first identified",
            "Awareness campaigns are said to make every donor's blood "
            "automatically safe to use",
        ],
        "correct_index": 1,
        "why": "Even a well-informed donor can be unaware of a very "
               "recent infection, so testing the blood itself remains "
               "necessary regardless of public awareness.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    {
        "id": "ks4-viral-diseases-h05",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how HIV and TMV each cause long-term damage to "
                "their host, even though neither is a toxin-producing "
                "bacterium.",
        "options": [
            "HIV reduces the rate of photosynthesis in its host, "
            "while TMV destroys immune cells as HIV does",
            "Both damage their host in the same underlying way, by "
            "producing toxins that spread around the body",
            "HIV destroys immune cells; TMV only lowers "
            "photosynthesis in infected leaves",
            "Neither causes long-term damage after the first stage",
        ],
        "correct_index": 2,
        "why": "The two act on entirely different systems: HIV damages "
               "immunity in an animal host, while TMV damages a plant's "
               "ability to photosynthesise.",
    },
    {
        "id": "ks4-viral-diseases-h06",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with HIV has a normal T-helper lymphocyte count "
                "for several years, then it falls sharply. Explain what is "
                "happening during each of these two periods.",
        "options": [
            "The patient is said to be completely uninfected during the "
            "whole of the first period, and only becomes infected once "
            "the count falls",
            "The virus is said to be entirely dormant at first, then "
            "becomes active only once several years have passed",
            "The immune system is claimed to attack the virus completely "
            "at first, then stops working for no clear reason",
            "The virus is present but the immune system is keeping pace "
            "with it at first; later, it is overwhelmed and lymphocyte "
            "numbers fall",
        ],
        "correct_index": 3,
        "why": "For a period the immune system can replace the "
               "T-helper cells HIV destroys, but eventually the virus "
               "outpaces that replacement and the count falls.",
    },
    {
        "id": "ks4-viral-diseases-h07",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that because HIV can now be controlled "
                "with drugs, it is no longer a serious infection.",
        "options": [
            "It overstates the case; treatment is lifelong and the "
            "virus never leaves the body",
            "It is reasonable, because an infection controlled by "
            "drugs carries no further risk to the patient or to "
            "others",
            "It is reasonable, because antiretroviral treatment "
            "removes HIV from the body within a few months of "
            "starting",
            "It understates the case; HIV remains untreatable outside "
            "a small number of wealthy countries",
        ],
        "correct_index": 0,
        "why": "Treatment has changed the outlook, but the infection is "
               "not cured, is still transmissible, and remains serious if "
               "left untreated.",
    },
    {
        "id": "ks4-viral-diseases-h08",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tomato crop shows mosaic symptoms in one corner of a "
                "greenhouse only. Suggest how the outbreak most likely "
                "began there, and why it has not yet spread further.",
        "options": [
            "The virus is said to have arrived through the air all across "
            "the whole greenhouse at once, but for some reason only shows "
            "symptoms in one corner",
            "A single contaminated tool or plant most likely introduced "
            "the virus there, and it has not yet been carried by contact "
            "to the rest of the greenhouse",
            "TMV is claimed to spread only in greenhouses with a "
            "particular temperature, which happens to exist in one corner "
            "only",
            "The soil in that corner is said to be the only part of the "
            "greenhouse capable of carrying TMV",
        ],
        "correct_index": 1,
        "why": "TMV spreads by contact rather than through the air, so an "
               "outbreak confined to one area points to a localised "
               "source that has not yet been carried further.",
    },
    {
        "id": "ks4-viral-diseases-h09",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on crop yield of a fungal leaf disease "
                "that causes defoliation with the effect of TMV, which "
                "leaves the leaf attached but mosaic-patterned.",
        "options": [
            "The fungal disease has no effect on yield, whereas TMV "
            "kills the whole plant within a single season",
            "Both reduce yield in the same way, by causing whole "
            "leaves to fall from the plant before replacement",
            "The fungus removes leaf area; TMV only lowers "
            "photosynthesis in the leaf that remains",
            "TMV removes leaf area, while the fungal disease lowers "
            "photosynthesis and leaves every leaf attached",
        ],
        "correct_index": 2,
        "why": "The two act by different mechanisms: losing leaf area "
               "altogether versus keeping the leaf but photosynthesising "
               "less efficiently within it.",
    },
    {
        "id": "ks4-viral-diseases-h10",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newborn tests positive for HIV antibodies at birth, but "
                "negative for the virus itself six months later. Explain "
                "how this can happen.",
        "options": [
            "HIV antibodies are said to always disappear completely from "
            "an infected baby's blood within six months regardless of "
            "infection",
            "The baby was infected at birth and the infection is said to "
            "have cleared itself completely without any treatment",
            "The antibody test is claimed to be inaccurate in every "
            "newborn until several years of age",
            "The baby carried the mother's own antibodies at birth "
            "without being infected, and these have since faded from the "
            "baby's blood",
        ],
        "correct_index": 3,
        "why": "A newborn can carry the mother's antibodies without being "
               "infected themselves, and those maternal antibodies fade "
               "over the following months.",
    },
    {
        "id": "ks4-viral-diseases-h11",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the reasoning that a person who tests HIV-negative "
                "one week after a risky exposure can be confident they are "
                "not infected.",
        "options": [
            "It is flawed; only after some weeks is there enough "
            "antibody to detect",
            "It is sound, because HIV antibodies appear within hours "
            "of an exposure and would show by then",
            "It is sound, because a negative antibody test is "
            "conclusive at any point after a possible exposure",
            "It is flawed, because HIV tests are unreliable",
        ],
        "correct_index": 0,
        "why": "There is a window before the body has produced enough "
               "antibody to be detected, so an early test cannot rule out "
               "infection on its own.",
    },
    {
        "id": "ks4-viral-diseases-h12",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher compares measles death rates before and after "
                "the MMR vaccine was introduced. Suggest what other "
                "explanation should be ruled out before concluding the "
                "vaccine alone caused the fall.",
        "options": [
            "No other explanation needs to be ruled out at all, because a "
            "fall in deaths is said to prove the vaccine was the sole cause",
            "Improvements in nutrition or medical care over the same "
            "period could also have reduced deaths, independently of the "
            "vaccine",
            "The vaccine is claimed to be the only medical intervention "
            "ever introduced during that period, in any country",
            "Death rates are said to be unaffected by anything other than "
            "vaccination, by definition",
        ],
        "correct_index": 1,
        "why": "A fall in deaths over time could have several causes, so "
               "other changes over the same period must be considered "
               "before crediting the vaccine alone.",
    },
    {
        "id": "ks4-viral-diseases-h13",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a virus that mutates rapidly, such as "
                "influenza, is harder to control with a single vaccine "
                "than one that mutates slowly, such as measles.",
        "options": [
            "A slowly mutating virus is claimed to be immune to "
            "vaccination altogether, unlike a fast-mutating one",
            "A rapidly mutating virus is said to become progressively "
            "weaker with every mutation, which somehow makes vaccination "
            "less useful",
            "A rapidly mutating virus changes its antigens often, so a "
            "vaccine matched to an earlier version may no longer fit the "
            "current strain",
            "Mutation rate is said to have no bearing on how well a "
            "vaccine continues to work against a virus",
        ],
        "correct_index": 2,
        "why": "Frequent antigen changes mean a vaccine matched to an "
               "earlier strain can lose its fit, which is why a fast-"
               "mutating virus is harder to protect against long-term.",
    },
    {
        "id": "ks4-viral-diseases-h14",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A greenhouse worker wears gloves when handling "
                "TMV-infected plants but does not disinfect their pruning "
                "scissors between plants. Evaluate whether this precaution "
                "is likely to be effective.",
        "options": [
            "It makes no difference either way, because TMV is said to "
            "spread through the air regardless of any precaution taken",
            "It is likely to be fully effective, because gloves are said "
            "to remove every possible route the virus could use",
            "It is likely to be fully effective, because TMV is claimed "
            "to spread only through direct skin contact and never through "
            "tools",
            "It is likely to be ineffective on its own, because the "
            "scissors can still carry the virus directly from one plant "
            "to the next",
        ],
        "correct_index": 3,
        "why": "Gloves protect against contact from the worker's hands, "
               "but unclean scissors remain a separate route by which the "
               "virus can be carried between plants.",
    },
    {
        "id": "ks4-viral-diseases-h15",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the route by which HIV is transmitted with the "
                "route by which TMV is transmitted, and explain why the "
                "same hygiene measure would not protect against both.",
        "options": [
            "HIV travels only in body fluids and TMV only in plant "
            "sap, so one measure cannot cover both",
            "Both are transmitted by the same route, direct contact "
            "with a contaminated surface, so one measure covers both",
            "HIV travels in plant sap and TMV in body fluids, which "
            "is why the same precautions apply to each",
            "Neither has a defined route, so no hygiene measure could "
            "reduce the spread of either of them",
        ],
        "correct_index": 0,
        "why": "The two spread through entirely different pathways, so a "
               "precaution designed for one, such as a barrier method, has "
               "no bearing on the other.",
    },
    {
        "id": "ks4-viral-diseases-h16",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital reports that patients on long-term "
                "antiretroviral therapy still occasionally develop "
                "opportunistic infections. Suggest why treatment does not "
                "remove this risk entirely.",
        "options": [
            "Antiretroviral therapy is said to have no measurable effect "
            "on the immune system at all, in any patient",
            "Treatment controls the virus and allows some immune "
            "recovery, but it may not restore the immune system to its "
            "full original strength",
            "Opportunistic infections are claimed to occur only in those "
            "patients who have never once started treatment of any kind "
            "at all",
            "The drugs are said to actively suppress the parts of the "
            "immune system that fight ordinary infections",
        ],
        "correct_index": 1,
        "why": "Treatment limits the damage HIV does, but a patient's "
               "immune system may not fully recover to the strength it "
               "had before infection.",
    },
    {
        "id": "ks4-viral-diseases-h17",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a plant showing no visible mosaic "
                "symptoms cannot be carrying TMV.",
        "options": [
            "The claim is true, because a symptom-free plant is claimed "
            "to be incapable of transmitting the virus to another plant",
            "The claim is true, because TMV is said to always produce "
            "visible symptoms within a day of infection",
            "The claim is false; a plant can carry TMV and act as a "
            "source of infection without showing any visible symptoms",
            "The claim is false only in plants younger than one month, "
            "and is otherwise reliable",
        ],
        "correct_index": 2,
        "why": "A plant can be infected with TMV and carry the virus "
               "without displaying visible mosaic symptoms, which is why "
               "symptom checks alone cannot rule out infection.",
    },
    {
        "id": "ks4-viral-diseases-h18",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because a virus is not a living "
                "cell, it cannot be affected by natural selection. "
                "Evaluate this claim.",
        "options": [
            "The claim is wrong for plant viruses alone",
            "The claim is correct, because natural selection requires "
            "a nucleus, which a virus does not possess",
            "The claim is correct, because a virus makes perfect, "
            "unchanging copies of itself each time it replicates",
            "The claim is wrong; viral genes mutate, and helpful "
            "mutations spread",
        ],
        "correct_index": 3,
        "why": "A virus still replicates its genetic material with "
               "occasional errors, and any mutation that helps it survive "
               "or spread can become more common, exactly as natural "
               "selection predicts.",
    },
    {
        "id": "ks4-viral-diseases-h19",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an unvaccinated traveller entering a country "
                "with high measles vaccination coverage can still trigger "
                "a local outbreak.",
        "options": [
            "Coverage gaps mean some local groups remain unprotected "
            "and can pass it on",
            "High national coverage makes transmission impossible, "
            "whoever enters the country and however long they stay",
            "A single traveller cannot infect more than one other "
            "person, so an outbreak could not begin from one case",
            "An outbreak requires the traveller to remain in the "
            "country for several months before spread begins",
        ],
        "correct_index": 0,
        "why": "A high national average can still leave local pockets of "
               "unvaccinated people through whom the virus can spread once "
               "introduced.",
    },
    {
        "id": "ks4-viral-diseases-h20",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare why antibiotic resistance in bacteria and drug "
                "resistance in HIV are both examples of natural selection, "
                "even though one is a cell and the other is not.",
        "options": [
            "The two are unrelated processes, because natural selection "
            "is said to apply only to bacteria and never to a virus",
            "In both cases, individuals carrying a resistance mutation "
            "survive treatment and reproduce, so resistant forms become "
            "more common over time",
            "Resistance in bacteria is claimed to arise from drug use, "
            "while resistance in HIV is said to arise only from mutation "
            "with no involvement of drug use at all",
            "Neither process is a genuine example of natural selection, "
            "because both are driven entirely by human choice",
        ],
        "correct_index": 1,
        "why": "Both cases follow the same pattern: a treatment acts as a "
               "selection pressure, and whichever forms happen to resist "
               "it survive and reproduce, becoming more common.",
    },
    {
        "id": "ks4-viral-diseases-h21",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tomato grower burns all infected plant material rather "
                "than composting it. Evaluate whether burning is a "
                "stronger precaution than composting for a TMV outbreak "
                "specifically.",
        "options": [
            "Composting is stronger, because the heat generated in a "
            "compost heap is claimed to always exceed that of burning",
            "It makes no difference, because TMV is said to be destroyed "
            "equally well by composting and by burning",
            "It is stronger, because burning destroys the virus "
            "particles, while TMV can persist on plant debris left in a "
            "compost heap",
            "Neither method has any effect, because TMV is said to "
            "survive indefinitely regardless of how infected material is "
            "disposed of",
        ],
        "correct_index": 2,
        "why": "Burning destroys the virus outright, while TMV can survive "
               "on undecomposed plant material in a compost heap and "
               "later reinfect a crop.",
    },
    {
        "id": "ks4-viral-diseases-h22",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person can be highly infectious with HIV "
                "during the first few weeks after infection, before any "
                "antibody test would detect it.",
        "options": [
            "Early infection involves no virus particles in the "
            "blood, so the virus is found in other body fluids",
            "A person becomes infectious once antibodies are "
            "produced, and antibodies appear as soon as infection "
            "starts",
            "Infectiousness depends on the test result",
            "Virus levels are often very high, and only later does "
            "antibody become detectable",
        ],
        "correct_index": 3,
        "why": "Virus levels can be very high soon after infection, well "
               "before the antibody response a standard test relies on "
               "has fully developed.",
    },
    {
        "id": "ks4-viral-diseases-h23",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why global measles elimination has proved harder "
                "to achieve than smallpox eradication, given that both "
                "have an effective vaccine.",
        "options": [
            "Measles spreads so easily that it needs unusually high "
            "coverage to stop it",
            "Smallpox had no effective vaccine until after it had "
            "been eradicated worldwide",
            "The measles vaccine works in fewer than half of the "
            "people who receive it, unlike the smallpox vaccine",
            "The two diseases require identical vaccination coverage, "
            "so the difference in progress is unexplained",
        ],
        "correct_index": 0,
        "why": "Measles is so easily transmitted that it needs an "
               "unusually high level of population coverage to stop it "
               "spreading, so any gap in coverage lets it persist.",
    },
    {
        "id": "ks4-viral-diseases-h24",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant breeder develops a tomato variety resistant to "
                "TMV. Evaluate the claim that this single measure removes "
                "the need for any other TMV control practice.",
        "options": [
            "The claim is correct, because a resistant variety is said to "
            "be immune to every plant disease, not only TMV",
            "The claim overstates the case; resistance reduces risk but "
            "hygiene measures such as clean tools and virus-free seed "
            "remain useful, especially against other plant viruses",
            "The claim is correct, because TMV is claimed to be the only "
            "disease risk a tomato crop ever faces",
            "The claim understates the case, because resistant varieties "
            "are said to still catch TMV as often as any other variety",
        ],
        "correct_index": 1,
        "why": "Resistance to one virus does not remove every risk a crop "
               "faces, so other hygiene measures remain worthwhile "
               "alongside it.",
    },
    {
        "id": "ks4-viral-diseases-h25",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what a cure would mean for a bacterial infection "
                "treated with antibiotics with what it would mean for HIV "
                "treated with antiretrovirals.",
        "options": [
            "A cured bacterial infection still carries live bacteria, "
            "in the same way that HIV treatment leaves the virus in "
            "place",
            "Both are cured in the same sense, with no pathogen of "
            "either kind left anywhere in the body afterwards",
            "Antibiotics can clear the bacteria; antiretrovirals only "
            "control HIV",
            "Neither antibiotics nor antiretrovirals remove a "
            "pathogen, so neither counts as a cure",
        ],
        "correct_index": 2,
        "why": "Antibiotics can clear bacteria from the body entirely, "
               "whereas current antiretroviral treatment suppresses HIV "
               "without eliminating it.",
    },
    {
        "id": "ks4-viral-diseases-h26",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer sees mosaic symptoms return each year in the "
                "same field despite planting new, virus-free seed each "
                "season. Suggest why.",
        "options": [
            "The seed supplier is said to be the only possible source, "
            "so the seed itself cannot truly be virus-free",
            "Virus-free seed is said to become infected automatically "
            "once it is planted in any field that has grown tomatoes "
            "before",
            "TMV is claimed to be produced fresh each year by the soil "
            "itself, regardless of what was grown there previously",
            "The virus can be persisting in the soil, on old plant "
            "debris, or on tools used in that field from one season to "
            "the next",
        ],
        "correct_index": 3,
        "why": "Even with clean seed, the virus can persist in the field "
               "on debris, tools or other material left from a previous "
               "infected crop, and reinfect the new planting.",
    },
]
