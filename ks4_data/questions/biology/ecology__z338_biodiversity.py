"""Biology · Ecology — the MRB-338 expansion, subtopic `biodiversity`.

Spec 4.7.3.1. The weight falls on the two halves of the definition — species
diversity, which is a count AND a set of relative abundances, and genetic
diversity within one species — because the lesson's own common mistake is that
biodiversity is just a species count. From there the rows work outwards through
the ecosystem services people actually depend on (pollination, clean water,
clean air, medicines from willow, mould and the Pacific yew, stability) and the
five named threats, each through a real case: the American mink and the water
vole, Japanese knotweed, an oil spill, a drained wetland, a warming range.
Conservation appears only where the existing rows already reach into it.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-biodiversity-e05",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two components that biodiversity is made up of.",
        "options": [
            "Species diversity and genetic diversity",
            "Plant diversity and animal diversity",
            "Habitat diversity and climate diversity",
            "Population size and community size",
        ],
        "correct_index": 0,
        "why": "Biodiversity covers the variety of different species in an area "
               "and the variety of alleles held within each of those species.",
    },
    {
        "id": "ks4-biodiversity-e06",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two populations of the same species look identical, but one "
                "carries a much wider range of alleles than the other. Name "
                "the property that differs between them.",
        "options": [
            "The number of individuals the species has in that area",
            "Genetic diversity",
            "The number of other species it is closely related to",
            "The range of habitats across which it can be found living",
        ],
        "correct_index": 1,
        "why": "Genetic diversity is the range of different versions of genes — "
               "alleles — present across the individuals of one species.",
    },
    {
        "id": "ks4-biodiversity-e07",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the tree that a cancer drug was originally obtained from.",
        "options": [
            "The willow",
            "The oak",
            "The Pacific yew",
            "The Scots pine",
        ],
        "correct_index": 2,
        "why": "A compound from the bark of the Pacific yew was developed into a "
               "cancer drug, which is one of many medicines that began in a wild "
               "species.",
    },
    {
        "id": "ks4-biodiversity-e08",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an invasive species now living in the UK?",
        "options": [
            "The red squirrel",
            "The barn owl",
            "The common frog",
            "The American mink",
        ],
        "correct_index": 3,
        "why": "The American mink was brought here for fur farming and escaped, "
               "and it now preys on native species that had no defence against "
               "it.",
    },
    {
        "id": "ks4-biodiversity-e09",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the threat to biodiversity that consists of clearing large "
                "areas of forest.",
        "options": [
            "Deforestation",
            "Eutrophication",
            "Desalination",
            "Sedimentation",
        ],
        "correct_index": 0,
        "why": "Deforestation destroys the habitat of every species that lived "
               "in the forest, which is the commonest route by which "
               "biodiversity is lost.",
    },
    {
        "id": "ks4-biodiversity-e10",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forest absorbs carbon dioxide and influences the rainfall "
                "around it. Name the ecosystem service this describes.",
        "options": [
            "Pollination of crops",
            "Climate regulation",
            "Seed dispersal",
            "Water purification",
        ],
        "correct_index": 1,
        "why": "Taking carbon dioxide out of the air and shaping local rainfall "
               "patterns are both part of the climate regulation that "
               "vegetation provides.",
    },
    {
        "id": "ks4-biodiversity-e11",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an example of overexploitation?",
        "options": [
            "Setting aside a field margin for wild flowers",
            "Planting a mixed hedge along the edge of a field",
            "Catching more fish each year than the stock can replace",
            "Restoring a drained bog back to open wet ground",
        ],
        "correct_index": 2,
        "why": "Overexploitation is taking a species faster than it can "
               "reproduce, which drives the population down towards a level from "
               "which it cannot recover.",
    },
    {
        "id": "ks4-biodiversity-e12",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give a reason for protecting a species that has nothing to do "
                "with its usefulness to people.",
        "options": [
            "It may hold a medicine that has not yet been discovered",
            "Its wild relatives may be needed to improve a crop plant",
            "It may turn out to be a pollinator of a future food crop",
            "Many people argue that a species has a right to exist",
        ],
        "correct_index": 3,
        "why": "The ethical argument is that species have value in their own "
               "right, independently of any use a human being may find for them.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-biodiversity-s05",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why plant breeders value the wild relatives of a crop "
                "plant.",
        "options": [
            "They hold alleles the crop has lost, such as disease resistance",
            "They grow faster than the crop, so they give a quicker harvest",
            "They can be sold as a crop themselves without any further work",
            "They take up less space in a field than the cultivated crop does",
        ],
        "correct_index": 0,
        "why": "A crop bred for yield has lost much of its genetic diversity, "
               "and the wild relatives are the reservoir of useful alleles a "
               "breeder can draw on.",
    },
    {
        "id": "ks4-biodiversity-s06",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how an oil spill along a coast reduces the biodiversity "
                "of the shore.",
        "options": [
            "Oil adds carbon to the water, which the seaweeds use to grow",
            "Oil coats and poisons the organisms, so many species are lost",
            "Oil floats, so it changes nothing about the shore beneath it",
            "Oil warms the water, and warmer water holds fewer species",
        ],
        "correct_index": 1,
        "why": "Pollution is a direct threat: the oil smothers and poisons the "
               "organisms living on the shore, so the species that cannot "
               "tolerate it disappear from the area.",
    },
    {
        "id": "ks4-biodiversity-s07",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how acid rain reduces the number of species living in "
                "an upland lake.",
        "options": [
            "The rain raises the water level, so the shallows are drowned",
            "The rain washes extra minerals in, which the fish cannot use",
            "The falling pH kills the species that cannot tolerate acid",
            "The rain cools the lake below what its invertebrates can stand",
        ],
        "correct_index": 2,
        "why": "Acid rain lowers the pH of the water, and pH is an abiotic "
               "factor with a narrow tolerance range, so sensitive species such "
               "as mayfly larvae are lost first.",
    },
    {
        "id": "ks4-biodiversity-s08",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "After American mink escaped from fur farms, water vole numbers "
                "along British rivers collapsed. Explain why.",
        "options": [
            "The voles left the rivers to avoid the smell of the mink",
            "The mink ate the same waterside plants that the voles had eaten",
            "The mink carried a disease that only affected the water voles",
            "The voles had no defence against a predator new to the river",
        ],
        "correct_index": 3,
        "why": "An introduced predator meets prey that has not evolved "
               "behaviours or defences against it, so the native population is "
               "taken far faster than it can breed.",
    },
    {
        "id": "ks4-biodiversity-s09",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Japanese knotweed spreads along a railway embankment and the "
                "native plants disappear. Name this threat and state its "
                "mechanism.",
        "options": [
            "An invasive species, which outcompetes the plants already there",
            "Overexploitation, because the natives are removed far too fast",
            "Habitat destruction, because the embankment itself is destroyed",
            "Pollution, because the knotweed releases a toxin into the soil",
        ],
        "correct_index": 0,
        "why": "Knotweed is an introduced species that grows faster and taller "
               "than the natives, so it takes the light, water and space before "
               "they can.",
    },
    {
        "id": "ks4-biodiversity-s10",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why draining a wetland for farmland reduces "
                "biodiversity.",
        "options": [
            "Dry soil holds more minerals, and minerals attract fewer species",
            "The species that needed wet ground have nowhere left to live",
            "The drained land is colder, so fewer species can survive on it",
            "Drainage removes the soil itself, so nothing can grow there",
        ],
        "correct_index": 1,
        "why": "Habitat destruction removes the conditions a community depends "
               "on, and the wetland specialists cannot simply move onto dry "
               "farmland.",
    },
    {
        "id": "ks4-biodiversity-s11",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two ways in which a large forest helps to regulate the "
                "climate.",
        "options": [
            "It reflects the sunlight and it takes nitrogen out of the air",
            "It releases carbon dioxide and it lowers the local rainfall",
            "It absorbs carbon dioxide and it influences local rainfall",
            "It warms the air above it and it produces its own clouds of dust",
        ],
        "correct_index": 2,
        "why": "Photosynthesis removes carbon dioxide from the atmosphere, and "
               "the water the trees release shapes the rainfall pattern over and "
               "downwind of the forest.",
    },
    {
        "id": "ks4-biodiversity-s12",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a pesticide sprayed on one field can reduce "
                "biodiversity in a river a kilometre away.",
        "options": [
            "The pesticide changes the field's soil pH, and rivers follow it",
            "The pesticide evaporates and then falls again as acid rain",
            "Insects carry the pesticide to the river on their own bodies",
            "Rain washes the pesticide off the field and into the river",
        ],
        "correct_index": 3,
        "why": "A pollutant does not stay where it is applied: run-off carries "
               "it into watercourses, where it harms species the sprayer never "
               "intended to reach.",
    },
    {
        "id": "ks4-biodiversity-s13",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why plastic waste in the sea is a threat to marine "
                "biodiversity.",
        "options": [
            "Animals swallow it or become entangled, and many of them die",
            "Plastic dissolves in seawater and raises the salt content of it",
            "Plastic floats, so it blocks the light that fish need to see by",
            "Plastic is eaten by bacteria, which then multiply out of control",
        ],
        "correct_index": 0,
        "why": "Plastic is a pollutant that kills directly — by blocking guts "
               "when it is swallowed and by trapping animals that cannot free "
               "themselves.",
    },
    {
        "id": "ks4-biodiversity-s14",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a warming climate can reduce biodiversity in a "
                "region without any organism being killed by the heat itself.",
        "options": [
            "Warm air holds more oxygen, which upsets the balance of species",
            "Species shift their range, and some have nowhere left to go",
            "Warming stops every species from reproducing for a whole season",
            "Warming makes the soil more alkaline, so plants cannot take water",
        ],
        "correct_index": 1,
        "why": "As the band of tolerable temperature moves, species have to "
               "follow it, and one already at the top of a mountain or the edge "
               "of a coast has nowhere to move to.",
    },
    {
        "id": "ks4-biodiversity-s15",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lake P holds 18 species, one of which makes up 95% of the "
                "individuals. Lake Q holds 18 species in roughly equal numbers. "
                "Compare their biodiversity.",
        "options": [
            "P's is higher, because one of its species is clearly thriving",
            "They are equal, because each lake contains 18 species in all",
            "Q's is higher, because its species are more evenly abundant",
            "P's is higher, because it must hold more individuals in total",
        ],
        "correct_index": 2,
        "why": "Biodiversity depends on relative abundance as well as the count, "
               "so a community dominated by a single species is less diverse in "
               "practice than an even one.",
    },
    {
        "id": "ks4-biodiversity-s16",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the illegal trade in wild animals threatens the "
                "species being traded.",
        "options": [
            "Buyers keep the animals in conditions that are too cold for them",
            "Traded animals stop breeding as soon as they leave the wild",
            "The trade moves animals abroad, so their species is reclassified",
            "Animals are taken faster than the population can replace them",
        ],
        "correct_index": 3,
        "why": "This is overexploitation: removing individuals faster than they "
               "are born pushes the population below the level from which it can "
               "recover.",
    },
    {
        "id": "ks4-biodiversity-s17",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how building a new housing estate on grassland reduces "
                "biodiversity.",
        "options": [
            "The habitat is replaced, so its community has nowhere to live",
            "The estate raises the soil pH until nothing is able to grow",
            "The residents introduce species, and new species lower diversity",
            "Concrete releases minerals that the grassland plants cannot use",
        ],
        "correct_index": 0,
        "why": "Urbanisation is habitat destruction: the abiotic conditions the "
               "grassland community needed are covered over, so the species "
               "living there are lost from the site.",
    },
    {
        "id": "ks4-biodiversity-s18",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Penicillin was first obtained from a mould. Explain what this "
                "shows about the value of biodiversity.",
        "options": [
            "Moulds are the only group of organisms that produce medicines",
            "Wild species can hold medicines that people have not yet found",
            "A species is worth protecting once a use has been found for it",
            "Medicines are made in laboratories rather than by living things",
        ],
        "correct_index": 1,
        "why": "Many drugs began as a chemical made by a wild organism, so every "
               "species lost is a possible medicine lost before it was ever "
               "examined.",
    },
    {
        "id": "ks4-biodiversity-s19",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An old flower-rich meadow is ploughed and sown with maize. "
                "Predict the effect on the site's biodiversity.",
        "options": [
            "It stays the same, because the same area of land is still there",
            "It rises, because maize is a tall plant that shelters wildlife",
            "It falls sharply, because one crop replaces many wild species",
            "It rises, because ploughing releases minerals into the topsoil",
        ],
        "correct_index": 2,
        "why": "Replacing a species-rich community with a monoculture removes "
               "both the variety of plants and the insects, birds and mammals "
               "that depended on them.",
    },
    {
        "id": "ks4-biodiversity-s20",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a marine protected area where fishing is banned "
                "can raise the catch on the fishing grounds around it.",
        "options": [
            "The reserve warms the water outside it, which attracts more fish",
            "Fish inside it grow faster, so they are worth more when caught",
            "The ban makes fish move outwards to escape the crowded reserve",
            "Fish breed inside it, and the young spread out beyond its edge",
        ],
        "correct_index": 3,
        "why": "Protecting the breeding adults raises the number of young "
               "produced, and those young disperse across the boundary into the "
               "fished waters.",
    },
    {
        "id": "ks4-biodiversity-s21",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an ecologist records how common each species is as "
                "well as how many species are present.",
        "options": [
            "A community dominated by one species is less diverse in practice",
            "The number of species present cannot be counted reliably at all",
            "Abundance decides which species is the most important one there",
            "Rare species are always removed from a biodiversity calculation",
        ],
        "correct_index": 0,
        "why": "High biodiversity means many species AND reasonable numbers of "
               "each, so a count on its own can make a badly unbalanced "
               "community look healthy.",
    },
    {
        "id": "ks4-biodiversity-s22",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how leaving a mixed hedge along a field edge raises the "
                "biodiversity of a farm.",
        "options": [
            "The hedge takes minerals from the crop, which slows its growth",
            "The hedge is a habitat that feeds and shelters many species",
            "The hedge shades the crop, and shade suits most wild species",
            "The hedge keeps farm machinery out of that part of the field",
        ],
        "correct_index": 1,
        "why": "A hedge adds a woody habitat with flowers, berries and nest "
               "sites, so insects, birds and small mammals that the crop cannot "
               "support have somewhere to live.",
    },
    {
        "id": "ks4-biodiversity-s23",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river is dredged straight and its banks are lined with "
                "concrete. Predict the effect on the species living there.",
        "options": [
            "Numbers stay the same, because the same water is still present",
            "Numbers rise, because the water now flows much more quickly",
            "Numbers of species fall, as the varied habitats are removed",
            "Numbers rise, because concrete banks hold more plant minerals",
        ],
        "correct_index": 2,
        "why": "A natural river has pools, riffles, shallows and vegetated "
               "banks, and each supports different species; straightening and "
               "lining it leaves one uniform habitat.",
    },
    {
        "id": "ks4-biodiversity-s24",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the loss of one wild bee species matters to a fruit "
                "farmer.",
        "options": [
            "The farmer is required by law to keep every bee species present",
            "The bees had been feeding on the pests that attack the fruit trees",
            "The bees had been keeping the orchard's soil minerals in balance",
            "Fewer pollinators means fewer flowers are fertilised, so less fruit",
        ],
        "correct_index": 3,
        "why": "Pollination is an ecosystem service, and around three quarters "
               "of the world's food crops depend on an animal to move their "
               "pollen.",
    },
    {
        "id": "ks4-biodiversity-s25",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why clearing land for agriculture is the largest single "
                "threat to biodiversity in many countries.",
        "options": [
            "It removes whole habitats over very large areas of land",
            "It uses fertiliser, and fertiliser is toxic to most species",
            "It introduces invasive species onto every field that is cleared",
            "It takes the minerals out of the soil, so nothing grows again",
        ],
        "correct_index": 0,
        "why": "Habitat destruction is the commonest cause of species loss, and "
               "agriculture is what clears the greatest area of natural habitat "
               "worldwide.",
    },
    {
        "id": "ks4-biodiversity-s26",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why water leaving a species-rich wetland is cleaner "
                "than water leaving a bare drainage ditch.",
        "options": [
            "Wetland water moves faster, so the pollutants are carried onwards",
            "Wetland plants and soil organisms trap and break down pollutants",
            "Bare ditches are warmer, and warm water dissolves more pollutant",
            "Wetland plants add oxygen, and oxygen dissolves every pollutant",
        ],
        "correct_index": 1,
        "why": "Clean water is an ecosystem service: the roots, sediments and "
               "microorganisms of a wetland hold pollutants back and decompose "
               "them.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-biodiversity-h05",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a species with no known use to people "
                "does not need protecting.",
        "options": [
            "It is unsound, because every species has a known medical use",
            "It is sound, because protection costs money that could be saved",
            "It is unsound: its uses and its role may be undiscovered",
            "It is sound, because a species with no use has no ecological role",
        ],
        "correct_index": 2,
        "why": "Uses are found after the fact — aspirin and penicillin both were "
               "— and the species may also be doing something in its community "
               "that nobody has measured.",
    },
    {
        "id": "ks4-biodiversity-h06",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a new pathogen is more dangerous to a genetically "
                "uniform population than to a varied one.",
        "options": [
            "A varied population produces a vaccine against the pathogen",
            "A uniform population is larger, so the pathogen spreads faster",
            "Uniform individuals are unable to pass on any of their alleles",
            "No individual carries an allele giving any resistance to it",
        ],
        "correct_index": 3,
        "why": "In a varied population some individuals happen to carry "
               "resistance alleles and survive to breed, but if every individual "
               "is alike then what infects one infects all.",
    },
    {
        "id": "ks4-biodiversity-h07",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a nature reserve has to be large as well as legally "
                "protected in order to conserve a top predator.",
        "options": [
            "A large predator needs a wide territory to find enough prey",
            "A large reserve is easier for wardens to patrol and police",
            "Legal protection has no effect on any species inside a reserve",
            "Small reserves are colder, which large predators cannot tolerate",
        ],
        "correct_index": 0,
        "why": "Carrying capacity is set by the resources within the boundary, "
               "so a reserve too small to supply a hunting range cannot hold a "
               "viable population however well the law protects it.",
    },
    {
        "id": "ks4-biodiversity-h08",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Wood R holds 9 plant species with 40 plants of each. Wood S "
                "holds 24 species, of which 20 are represented by a single "
                "plant. Determine which has the higher biodiversity.",
        "options": [
            "S, because it holds nearly three times as many species",
            "R, because its populations are large enough to persist",
            "R, because it contains more individual plants in total",
            "S, because 20 of its species are rare, and rarity adds value",
        ],
        "correct_index": 1,
        "why": "Biodiversity needs many species AND reasonable numbers of each; "
               "20 single plants are populations on the edge of disappearing, so "
               "S's higher count is not the better community.",
    },
    {
        "id": "ks4-biodiversity-h09",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an introduced species often does more damage to a "
                "community than a native one of the same kind.",
        "options": [
            "Introduced species reproduce far faster than any native species",
            "An introduced species is always larger than a native one",
            "The natives have no adaptations against something new to them",
            "Native species are unable to compete for any resource at all",
        ],
        "correct_index": 2,
        "why": "Native species have been selected over many generations against "
               "the predators, competitors and diseases already present, and a "
               "newcomer arrives outside all of that.",
    },
    {
        "id": "ks4-biodiversity-h10",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the birds of a remote island are especially "
                "vulnerable when a rat is introduced.",
        "options": [
            "Island birds cannot fly, so they are unable to escape the rats",
            "Island birds are smaller than mainland birds of the same species",
            "Rats breed faster on an island than they do on the mainland",
            "They evolved with no ground predator, so nest defences are absent",
        ],
        "correct_index": 3,
        "why": "Adaptations arise only against pressures a population has "
               "actually met, so birds that have never faced a ground predator "
               "nest in places a rat can reach.",
    },
    {
        "id": "ks4-biodiversity-h11",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Overfishing one species of grazing fish is followed by a fall "
                "in the number of species on a coral reef. Suggest why.",
        "options": [
            "Algae grow unchecked and smother the coral the others depend on",
            "The fishing boats damage the coral directly with their nets",
            "The remaining fish species interbreed and become a single species",
            "The missing fish had been the only food of every other species",
        ],
        "correct_index": 0,
        "why": "The grazer kept the algae in check; without it the algae "
               "overgrow the coral, and the coral is the habitat the rest of the "
               "reef community lives in.",
    },
    {
        "id": "ks4-biodiversity-h12",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that planting a million trees of one species "
                "restores a cleared forest's biodiversity.",
        "options": [
            "It is sound, because a million trees is more than were cleared",
            "It is unsound: one species is a plantation, not a community",
            "It is unsound, because trees cannot be planted by people at all",
            "It is sound, because tree cover is what biodiversity is measured by",
        ],
        "correct_index": 1,
        "why": "Biodiversity is variety, so replacing a mixed forest with a "
               "single-species plantation restores the tree cover while leaving "
               "the community it held unreplaced.",
    },
    {
        "id": "ks4-biodiversity-h13",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a species found in only one small valley is at "
                "greater risk of extinction than a widespread one.",
        "options": [
            "Widespread species are protected by law and narrow ones are not",
            "Species in small areas are unable to reproduce successfully",
            "A single event in that valley could remove the whole species",
            "A small valley holds fewer minerals than a wide range does",
        ],
        "correct_index": 2,
        "why": "A widespread species survives a local disaster somewhere else, "
               "but one whose entire population is in a single place has no "
               "population left in reserve.",
    },
    {
        "id": "ks4-biodiversity-h14",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a warming climate can raise the number of species "
                "recorded in southern England while lowering biodiversity "
                "worldwide.",
        "options": [
            "Species recorded twice in two countries are counted twice over",
            "Warming creates entirely new species in the places it reaches",
            "Local counts and global counts measure two unrelated things",
            "Species move north into it, but lose ground at their other edge",
        ],
        "correct_index": 3,
        "why": "A shifting range gains a species at its leading edge and loses "
               "one at its trailing edge, and where the trailing edge runs out "
               "of land the species is lost altogether.",
    },
    {
        "id": "ks4-biodiversity-h15",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farm wants to protect its wild pollinators. Determine which "
                "measure would help most, and justify it.",
        "options": [
            "Sowing flower-rich margins, to give nectar right through the year",
            "Spraying more often, to remove the insects that compete with bees",
            "Ploughing the field margins, to give the bees bare ground to nest",
            "Planting a single crop, because one crop is simpler for a bee",
        ],
        "correct_index": 0,
        "why": "Pollinators need forage and nest sites across the whole season, "
               "and a monoculture flowers for only a few weeks, so a permanent "
               "flowering margin is what sustains them.",
    },
    {
        "id": "ks4-biodiversity-h16",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a drug company might argue against clearing an area "
                "of rainforest.",
        "options": [
            "Rainforest air is needed in order to manufacture most medicines",
            "Undiscovered species there could be the source of new medicines",
            "Clearing the forest would release chemicals that spoil its drugs",
            "The company is required by law to protect every tropical forest",
        ],
        "correct_index": 1,
        "why": "Aspirin, penicillin and a cancer drug all came from wild "
               "organisms, so clearing habitat destroys species before anyone "
               "has looked at what they make.",
    },
    {
        "id": "ks4-biodiversity-h17",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species-poor community recovers less readily from "
                "a fire than a species-rich one.",
        "options": [
            "A rich community holds more water, so it does not catch fire",
            "Species-poor communities burn at a much higher temperature",
            "Fewer species means fewer able to take over a lost one's role",
            "Poor communities have no decomposers to clear the burnt material",
        ],
        "correct_index": 2,
        "why": "Resilience comes from overlap: where several species share a "
               "role the loss of one is absorbed, and a community with no spare "
               "capacity cannot close the gap.",
    },
    {
        "id": "ks4-biodiversity-h18",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the biodiversity of a habitat can be "
                "measured simply by counting its species.",
        "options": [
            "It is complete, provided the same observer does all the counting",
            "It is complete, because a species count is what diversity means",
            "It is incomplete, because a count ignores the abiotic factors",
            "It is incomplete: how common each species is matters as well",
        ],
        "correct_index": 3,
        "why": "A community holding 100 species of which one makes up 99% of the "
               "individuals has low diversity in practice, so relative "
               "abundance has to be recorded too.",
    },
    {
        "id": "ks4-biodiversity-h19",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how losing a top predator can lower the biodiversity of "
                "a habitat even though the predator killed nothing but its own "
                "prey.",
        "options": [
            "Its prey increase and graze out many of the plant species",
            "Its prey leave the habitat, and the plants follow them out",
            "The predator's droppings had held the habitat's only minerals",
            "The habitat becomes warmer once the largest animal is gone",
        ],
        "correct_index": 0,
        "why": "Removing the predator releases the herbivore, and heavy grazing "
               "removes the plant species least able to recover — a change two "
               "steps away from the predator itself.",
    },
    {
        "id": "ks4-biodiversity-h20",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the long-term effect on biodiversity of a single "
                "chemical spill and of building a road across the same wood.",
        "options": [
            "The spill is worse, because a chemical is toxic and a road is not",
            "The spill can be recovered from; the road removes habitat for good",
            "Both have the same effect, because both reduce the species present",
            "The road is less damaging, because it covers only a narrow strip",
        ],
        "correct_index": 1,
        "why": "Pollution is usually reversible once it stops, while habitat "
               "destruction permanently removes the conditions a community "
               "needed and also cuts the wood in two.",
    },
    {
        "id": "ks4-biodiversity-h21",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a law protecting an endangered bird may fail to "
                "save it.",
        "options": [
            "Endangered birds are unable to breed once they are protected",
            "A law cannot be enforced against any private landowner",
            "A law protects the bird but not the habitat it needs",
            "A protected species loses its natural fear of people quickly",
        ],
        "correct_index": 2,
        "why": "Protecting individuals from being taken is of little use if the "
               "nesting and feeding habitat continues to be destroyed, so "
               "legislation has to be paired with habitat protection.",
    },
    {
        "id": "ks4-biodiversity-h22",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Farm A has 3 crop species and no hedges; farm B has 3 crops, "
                "hedges, a pond and uncut margins. Determine which supports "
                "more pollinator species and explain.",
        "options": [
            "A, because open ground is what most pollinating insects prefer",
            "A, because its crops are not competing with any wild flowers",
            "Both the same, because the two farms grow the same three crops",
            "B, because it offers more habitats and a longer flowering season",
        ],
        "correct_index": 3,
        "why": "Pollinators need forage, nest sites and shelter across the whole "
               "season, and the hedges, pond and margins supply all three where "
               "bare crop fields do not.",
    },
    {
        "id": "ks4-biodiversity-h23",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why restoring an ancient woodland can take many decades "
                "even after the threat to it is removed.",
        "options": [
            "Old trees and their specialist species take that long to return",
            "Threats removed from a woodland always come back within a decade",
            "The soil has to be replaced completely before anything will grow",
            "Woodland species will not return until every tree is the same age",
        ],
        "correct_index": 0,
        "why": "Some habitat features — large old trees, deadwood, undisturbed "
               "soil — take a century to develop, and the species that need them "
               "cannot arrive before they exist.",
    },
    {
        "id": "ks4-biodiversity-h24",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why storing a plant's seeds in a seed bank is not a "
                "full substitute for protecting it in the wild.",
        "options": [
            "Stored seeds lose the ability to germinate within a single year",
            "The community and the conditions it lived in are not stored",
            "A seed bank can hold only one seed from each plant species",
            "Seeds stored in a bank become a different species over time",
        ],
        "correct_index": 1,
        "why": "A seed bank preserves the genetic material but not the habitat, "
               "the pollinators or the rest of the community, so there may be "
               "nowhere left to put the seed back.",
    },
    {
        "id": "ks4-biodiversity-h25",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the value of biodiversity to medicine cannot be "
                "worked out before a species has been studied.",
        "options": [
            "Species are studied in the order of how valuable they turned out",
            "Medicines are worth the same amount whatever species they come from",
            "What a species makes is unknown until somebody examines it",
            "Every species holds a medicine, so the value is always the same",
        ],
        "correct_index": 2,
        "why": "The compounds an organism produces have to be found and tested "
               "before their use is known, so a species lost before it is "
               "examined takes an unmeasured value with it.",
    },
    {
        "id": "ks4-biodiversity-h26",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An estate is farmed intensively from hedge to hedge. Determine "
                "which single change would raise its biodiversity most, and "
                "justify it.",
        "options": [
            "Draining the wet corners, so the whole estate can be cropped",
            "Using a stronger pesticide, because pests reduce wild species",
            "Growing a single higher-yielding crop, to free land elsewhere",
            "Restoring uncropped habitat, because habitat loss is the main cause",
        ],
        "correct_index": 3,
        "why": "Habitat destruction is the largest cause of biodiversity loss, "
               "so giving habitat back — margins, ponds, rough grass, hedges — "
               "addresses the cause rather than a symptom.",
    },
]
