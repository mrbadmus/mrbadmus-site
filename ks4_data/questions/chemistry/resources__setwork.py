"""Chemistry · Using resources — the MRB-335 extension.

Combined Foundation stood at 48 and Combined Higher at 44 on the 7 Sep
table. Five of the ten subtopics are Triple-only (corrosion, alloys,
ceramics, the Haber process, NPK), so the four base subtopics carry the
Foundation cell and those four plus `alternative-metal-extraction` carry the
Higher one — which is why this file adds to the Higher subtopic as well,
where the other four chemistry files did not.

Much of this topic is judgement rather than recall — sustainability, life
cycle assessment, whether a claim about a bag or a bottle stands up. Those
are written as single-answer evaluations: the correct option states the
trade-off, and every distractor is a real one-sided reading a student
offers, most often 'recycling is always best' and 'natural is always
better'.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── earths-resources ──────────────────────── BASE (5.10.1.1) ── +5 ──
    {
        "id": "ks4-earths-resources-e05",
        "subtopic_slug": "earths-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a renewable resource.",
        "options": [
            "One that is replaced by natural processes as fast as it is used",
            "One that can never be used up, whatever people do",
            "One that can be recycled after it has been used",
            "One that is found only in living organisms",
        ],
        "correct_index": 0,
        "why": "Renewable is about the rate of replacement: a resource stays "
               "renewable only while it is replaced at least as fast as it "
               "is taken.",
    },
    {
        "id": "ks4-earths-resources-s05",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the difference between a natural resource and a "
                "synthetic material, giving an example of each.",
        "options": [
            "A natural resource can always be recycled after use but a "
            "synthetic one never can",
            "A natural resource is always renewable and a synthetic one is "
            "always finite",
            "A natural resource is a single compound and a synthetic one is "
            "a mixture",
            "A natural resource is taken from the Earth, sea or air; a "
            "synthetic one is manufactured to replace it",
        ],
        "correct_index": 3,
        "why": "The distinction is about origin: taken from the environment "
               "as it is, or made by people from other materials.",
    },
    {
        "id": "ks4-earths-resources-s06",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cotton is a natural fibre and polyester is a synthetic one. "
                "Suggest one advantage of each.",
        "options": [
            "Cotton is renewable and biodegradable; polyester is consistent "
            "and does not depend on the harvest",
            "Cotton needs no water at all to produce; polyester needs no "
            "energy at all to produce",
            "Cotton lasts for ever; polyester decomposes completely in "
            "landfill",
            "Cotton is a synthetic polymer; polyester is a natural fibre",
        ],
        "correct_index": 0,
        "why": "Natural fibres are renewable but vary with the growing "
               "season; synthetic ones are consistent but are made from a "
               "finite feedstock.",
    },
    {
        "id": "ks4-earths-resources-h05",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country's copper reserves are said to last 40 years at "
                "the current rate of use, but demand is rising by 3% a year. "
                "Evaluate whether the reserves will in fact last 40 years.",
        "options": [
            "Yes — a reserve figure is a fixed number of years by definition",
            "Yes — reserve figures already allow for rising demand",
            "No — the figure assumes today's rate, so rising demand will "
            "exhaust the reserves sooner",
            "No — they will last longer, because recycling always grows "
            "faster than demand",
        ],
        "correct_index": 2,
        "why": "A '40 years at current rates' figure is a division, not a "
               "prediction, and any growth in demand shortens it.",
    },
    {
        "id": "ks4-earths-resources-h06",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sustainable development means meeting today's needs without "
                "stopping future generations meeting theirs. Apply this "
                "definition to a plan to fell a forest and replant twice as "
                "many trees.",
        "options": [
            "It cannot be sustainable, because felling any tree at all uses "
            "up a resource permanently",
            "It is automatically sustainable, because more trees are "
            "planted than were felled",
            "Sustainability does not apply, because timber is renewable",
            "It can be sustainable, provided the new trees reach maturity "
            "and the habitat recovers in time",
        ],
        "correct_index": 3,
        "why": "The test is whether the resource is still there for the "
               "next generation — planting alone is not enough if the trees "
               "or the habitat do not recover.",
    },

    # ── potable-water ─────────────────────────── BASE (5.10.1.2) ── +5 ──
    {
        "id": "ks4-potable-water-e05",
        "subtopic_slug": "potable-water",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by potable water.",
        "options": [
            "Water that is chemically pure",
            "Water that is safe to drink",
            "Water that contains no dissolved substances at all",
            "Water that has been boiled",
        ],
        "correct_index": 1,
        "why": "Potable means safe to drink, and safe drinking water still "
               "contains dissolved salts and a trace of chlorine.",
    },
    {
        "id": "ks4-potable-water-s05",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how fresh water is obtained in a country with very "
                "little rainfall and no lakes or rivers.",
        "options": [
            "Rain water is filtered through beds of sand and gravel",
            "Ground water is chlorinated and then sterilised",
            "Sea water is desalinated, by distillation or by reverse osmosis",
            "Sewage effluent is treated aerobically and supplied directly",
        ],
        "correct_index": 2,
        "why": "Where there is no fresh water to treat, the salt has to be "
               "taken out of sea water instead.",
    },
    {
        "id": "ks4-potable-water-s06",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A walker says that water from a hill stream is safe to "
                "drink because it looks completely clear. Explain why this "
                "reasoning is unsafe.",
        "options": [
            "Clear water can still carry harmful microorganisms and "
            "dissolved substances, none of them visible",
            "Clear water always contains far more dissolved oxygen, which "
            "is harmful to drink",
            "Clear water has a higher boiling point, which shows it is "
            "impure",
            "Clear water cannot be tested for safety by any method",
        ],
        "correct_index": 0,
        "why": "Sterilising is needed because the dangerous things in "
               "untreated water — microbes and dissolved ions — are "
               "invisible.",
    },
    {
        "id": "ks4-potable-water-h05",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "UK tap water is potable, yet a laboratory distils it before "
                "using it to make up a standard solution. Explain why.",
        "options": [
            "Tap water contains microorganisms that would consume the "
            "solute before it dissolved",
            "Tap water has been chlorinated, which makes it strongly acidic",
            "Tap water boils above 100 °C and cannot dissolve solids",
            "Tap water holds dissolved ions that are harmless to drink but "
            "would interfere with a measurement",
        ],
        "correct_index": 3,
        "why": "Safe to drink and chemically pure are different standards, "
               "and a laboratory needs the second one.",
    },
    {
        "id": "ks4-potable-water-h06",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water from a roof-collection tank carries no harmful "
                "microorganisms but a high level of dissolved lead from old "
                "pipework. Determine the treatment needed and explain why "
                "sterilising alone would not do.",
        "options": [
            "Distillation or reverse osmosis to remove the lead, because "
            "sterilising leaves dissolved ions untouched",
            "Chlorination alone, because chlorine reacts with lead and "
            "removes it from the water",
            "Filtration through beds of sand and gravel, because the sand "
            "traps the dissolved lead ions",
            "No treatment at all, because lead in water is not harmful",
        ],
        "correct_index": 0,
        "why": "Sterilising and removing dissolved substances are different "
               "jobs, and only the second one deals with a dissolved metal "
               "ion.",
    },

    # ── life-cycle-assessment ─────────────────── BASE (5.10.2.1) ── +5 ──
    {
        "id": "ks4-life-cycle-assessment-e05",
        "subtopic_slug": "life-cycle-assessment",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the four stages considered in a life cycle "
                "assessment.",
        "options": [
            "Designing, advertising, selling and using the product",
            "Mining, refining, packaging and shipping the product",
            "Extracting raw materials, manufacturing, using and disposing",
            "Extracting, testing, marketing and recycling",
        ],
        "correct_index": 2,
        "why": "An LCA runs from cradle to grave, so it starts at the raw "
               "material and ends at disposal.",
    },
    {
        "id": "ks4-life-cycle-assessment-s05",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why transport appears inside every stage of an LCA "
                "rather than as a stage of its own.",
        "options": [
            "Materials are moved at every stage, so the energy and "
            "emissions belong wherever they occur",
            "Transport is too small an effect to be worth its own stage",
            "Transport is only counted for goods that have been imported "
            "from abroad",
            "Transport is left out of every life cycle assessment",
        ],
        "correct_index": 0,
        "why": "Ore is moved to the smelter, parts to the factory and goods "
               "to the shop, so transport is spread across the whole life "
               "rather than sitting at one point in it.",
    },
    {
        "id": "ks4-life-cycle-assessment-s06",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An LCA gives a cotton shirt's water use as 2700 litres and "
                "a polyester shirt's as 150 litres. Suggest why this number "
                "alone does not decide which shirt is better.",
        "options": [
            "Water use is never included in a life cycle assessment",
            "Litres of water cannot be compared between two completely "
            "different materials",
            "The cotton figure must be wrong, because cotton is natural",
            "An LCA also covers energy, emissions and waste, and the shirts "
            "may differ the other way on those",
        ],
        "correct_index": 3,
        "why": "A life cycle assessment is a set of impacts, and picking "
               "one of them is how a partial LCA is used to mislead.",
    },
    {
        "id": "ks4-life-cycle-assessment-h05",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A supermarket claims its plastic bag has a lower "
                "environmental impact than its cotton bag. Deduce what the "
                "claim depends on and evaluate it.",
        "options": [
            "It depends on how many times each bag is reused: cotton takes "
            "far more energy to make",
            "It depends only on which of the two bags weighs less",
            "It cannot be true, because plastic is made from crude oil",
            "It depends only on which of the two bags is cheaper for the "
            "shop to buy",
        ],
        "correct_index": 0,
        "why": "A cotton bag starts with a much larger manufacturing "
               "impact, so the comparison is only meaningful once the number "
               "of uses is fixed.",
    },
    {
        "id": "ks4-life-cycle-assessment-h06",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two life cycle assessments of the same bottle, one by the "
                "manufacturer and one by an environmental group, reach "
                "opposite conclusions. Suggest two reasons why.",
        "options": [
            "One of the two must have made an arithmetic mistake",
            "They may have drawn the boundaries of the assessment "
            "differently, and weighted the impacts differently",
            "Life cycle assessments always agree, so one must be a forgery",
            "The manufacturer's assessment must be right, because only it "
            "has the production data",
        ],
        "correct_index": 1,
        "why": "What to include and how much each impact counts for are "
               "both choices, which is why an LCA can be used selectively "
               "to support a case.",
    },

    # ── reducing-use-of-resources ─────────────── BASE (5.10.2.2) ── +5 ──
    {
        "id": "ks4-reducing-use-of-resources-e05",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the three Rs of resource use, greatest benefit first.",
        "options": [
            "Recycle, reuse, reduce",
            "Reuse, recycle, reduce",
            "Reduce, reuse, recycle",
            "Reduce, recycle, reuse",
        ],
        "correct_index": 2,
        "why": "Not making something at all beats using it again, and using "
               "it again beats melting it down and remaking it.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s05",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a metal is recycled and state one saving it "
                "makes.",
        "options": [
            "The scrap is sorted, melted and cast into new products, which "
            "saves both the ore and much of the energy of extraction",
            "The scrap is dissolved in acid and the metal precipitated, "
            "which saves all the energy of extraction",
            "The scrap is buried so that it can re-form as ore, which saves "
            "mining",
            "The scrap is burned to release the metal, which saves the cost "
            "of sorting",
        ],
        "correct_index": 0,
        "why": "Recycling skips the extraction step entirely, so the ore "
               "stays in the ground and the energy of reducing it is never "
               "spent.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s06",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glass bottles are sometimes crushed and melted and "
                "sometimes just washed and refilled. Name each process and "
                "state which is better for the environment.",
        "options": [
            "Melting is reuse and refilling is recycling; melting is better "
            "because the glass is made new again",
            "Melting is recycling and refilling is reuse; refilling is "
            "better because it avoids the energy of melting altogether",
            "Both are recycling, and there is nothing to choose between "
            "them",
            "Both are reuse, and melting is better because it removes any "
            "contamination",
        ],
        "correct_index": 1,
        "why": "Reuse comes before recycling because a washed bottle needs "
               "only hot water, while a melted one needs a furnace.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h05",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium is extracted by electrolysis of molten aluminium "
                "oxide, which uses a very large amount of electricity. "
                "Explain why recycling aluminium saves more than recycling a "
                "metal that is extracted by reduction with carbon.",
        "options": [
            "Aluminium is the only metal that can be recycled again and "
            "again without loss",
            "Recycled aluminium is purer than newly extracted aluminium",
            "Aluminium ore is the only metal ore that is finite",
            "The electricity saved by not electrolysing again far exceeds "
            "the energy of a carbon reduction",
        ],
        "correct_index": 3,
        "why": "The saving from recycling is the extraction energy you no "
               "longer spend, and electrolysis is by far the most expensive "
               "extraction route.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h06",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a country exports plastic waste abroad for "
                "recycling, and evaluate whether this reduces the "
                "environmental impact.",
        "options": [
            "It is cheaper than sorting at home, but transport emissions "
            "and the risk of dumping may cancel the benefit",
            "Plastic can only be recycled in hot countries, and exporting "
            "it always reduces the impact",
            "It increases the amount of plastic in circulation, which "
            "always reduces the impact",
            "It has no environmental effect either way, because the plastic "
            "has already been made",
        ],
        "correct_index": 0,
        "why": "Exporting moves the problem rather than solving it, and "
               "whether it helps depends on what actually happens at the "
               "other end.",
    },

    # ── alternative-metal-extraction ─────────── HIGHER (5.10.1.3) ── +5 ──
    {
        "id": "ks4-alternative-metal-extraction-e05",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what happens to the plants after they are harvested "
                "in phytomining.",
        "options": [
            "They are buried, so that the metal returns to the soil",
            "They are burned, and the metal compounds are obtained from the "
            "ash",
            "They are pressed, and the metal is squeezed out as a liquid",
            "They are fed to bacteria, which release the metal",
        ],
        "correct_index": 1,
        "why": "Burning removes the plant material and leaves the metal "
               "compounds concentrated in the ash.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s05",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Describe how copper metal is obtained from the solution "
                "that bioleaching produces.",
        "options": [
            "By displacement with scrap iron, or by electrolysis of the "
            "solution",
            "By filtering the solution through beds of sand",
            "By heating the solution strongly with carbon",
            "By adding sodium hydroxide and drying the precipitate",
        ],
        "correct_index": 0,
        "why": "Bioleaching gives copper IONS in solution, and a more "
               "reactive metal or an electric current is what turns them "
               "into copper metal.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s06",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the ash from a phytomining crop is treated with "
                "acid before the copper is recovered.",
        "options": [
            "The acid neutralises the alkaline ash so that it is safe to "
            "handle afterwards",
            "The acid burns off the plant material still left in the ash",
            "The acid dissolves the metal compounds out of the ash, giving "
            "a solution to recover copper from",
            "The acid reduces the copper compounds directly to copper metal",
        ],
        "correct_index": 2,
        "why": "The copper in the ash is a solid compound, and it has to be "
               "in solution before displacement or electrolysis can get at "
               "it.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h05",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Compare the environmental impact of phytomining with "
                "open-cast mining of the same low-grade ore.",
        "options": [
            "Phytomining has no environmental impact of any kind",
            "Open-cast mining is cleaner, because it is finished far more "
            "quickly and the land is restored",
            "The two are identical, because both remove the same mass of "
            "metal",
            "Phytomining avoids the excavation, dust and rock waste of a "
            "mine, but occupies the land for years and is slower",
        ],
        "correct_index": 3,
        "why": "Phytomining trades the immediate destruction of a mine for a "
               "long, low-intensity use of the same land.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h06",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A low-grade ore holds its copper as copper sulfide, and the "
                "site sits beside a river used for drinking water. Evaluate "
                "the use of bioleaching there.",
        "options": [
            "It works chemically, because the bacteria oxidise sulfides, "
            "but the acidic leachate is a real risk to the river",
            "It is unsuitable, because bacteria are unable to act on an ore "
            "that holds its copper as a sulfide",
            "It is ideal, because bioleaching produces no waste at all",
            "It is unsuitable, because bioleaching only works on oxide ores",
        ],
        "correct_index": 0,
        "why": "Bioleaching suits this ore, but its by-product is an acidic "
               "solution, and that is the thing the river makes dangerous.",
    },
]
