"""Biology · Ecology — the MRB-338 expansion, subtopic `adaptations`.

Spec 4.7.2. The weight falls on the three-way classification (structural,
behavioural, functional), because that is what the marks are for and it is
where pupils guess, and it is examined through the lesson's own named species
rather than in the abstract — Arctic fox, fennec fox, kangaroo rat, snowshoe
hare, ptarmigan, anglerfish, hoverfly, wolf. The second strand is the lesson's
common mistake, that an organism grows the feature it needs: several rows come
at that from the wrong side, and surface-area-to-volume reasoning is run in
both directions rather than only the Arctic one."""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ────────────────────────────────────────────────────────────
    {
        "id": "ks4-adaptations-e05",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dormouse hibernates through the winter. Name the type of "
                "adaptation this is.",
        "options": [
            "Structural",
            "Functional",
            "Behavioural",
            "Seasonal",
        ],
        "correct_index": 2,
        "why": "Hibernating is something the animal does rather than a "
               "feature of its body or its internal chemistry, so it is a "
               "behavioural adaptation.",
    },
    {
        "id": "ks4-adaptations-e06",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some Arctic fish carry antifreeze proteins in their blood. "
                "Name the type of adaptation this is.",
        "options": [
            "Structural",
            "Behavioural",
            "Environmental change",
            "Functional",
        ],
        "correct_index": 3,
        "why": "Making a protein that stops the blood freezing is an internal "
               "chemical process, which makes it a functional adaptation.",
    },
    {
        "id": "ks4-adaptations-e07",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An Arctic fox grows a white coat for the winter. Name the "
                "type of adaptation the coat itself is.",
        "options": [
            "Behavioural",
            "Functional",
            "Structural",
            "Learned",
        ],
        "correct_index": 2,
        "why": "The coat is a physical feature of the animal's body, so it is "
               "a structural adaptation — one that camouflages the fox against the "
               "snow.",
    },
    {
        "id": "ks4-adaptations-e08",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which the adaptations of a species arise.",
        "options": [
            "Interdependence",
            "Natural selection",
            "Decomposition",
            "Competition",
        ],
        "correct_index": 1,
        "why": "Individuals whose features suit their surroundings survive "
               "and breed more, so those features become more common in the "
               "population over many generations.",
    },
    {
        "id": "ks4-adaptations-e09",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Wildebeest cross the plains in very large herds. Name the "
                "type of adaptation this is.",
        "options": [
            "Behavioural",
            "Functional, because it changes their internal chemistry",
            "Structural, because a herd has a shape of its own",
            "Structural, because their legs are built for walking",
        ],
        "correct_index": 0,
        "why": "Moving in a herd is something the animals do, so it is "
               "behavioural — and it makes it harder for a predator to single one "
               "animal out.",
    },
    {
        "id": "ks4-adaptations-e10",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kangaroo rat produces very concentrated urine. Name the "
                "type of adaptation this is.",
        "options": [
            "Functional",
            "Behavioural",
            "Structural",
            "Inherited",
        ],
        "correct_index": 0,
        "why": "Concentrating the urine is an internal process carried out by "
               "the kidneys, so it is a functional adaptation that conserves water.",
    },
    {
        "id": "ks4-adaptations-e11",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the part of a cactus that stores its water.",
        "options": [
            "Its spines",
            "Its flowers",
            "Its root hairs",
            "Its thick stem",
        ],
        "correct_index": 3,
        "why": "A cactus holds its water in a thick, waxy stem, which also "
               "carries out the photosynthesis its reduced leaves cannot.",
    },
    {
        "id": "ks4-adaptations-e12",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an adaptation typical of a prey animal "
                "rather than a predator?",
        "options": [
            "Forward-facing eyes for judging the distance to the prey",
            "Eyes set on the sides of the head",
            "Sharp claws for holding on to a struggling animal",
            "Hunting cooperatively in an organised group",
        ],
        "correct_index": 1,
        "why": "Eyes on the sides of the head give the widest field of view, "
               "so a prey animal can spot a predator approaching from almost any "
               "direction.",
    },
    # ── standard ──────────────────────────────────────────────────────────
    {
        "id": "ks4-adaptations-s05",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a thick layer of blubber helps a seal survive in "
                "cold Arctic water.",
        "options": [
            "It makes the seal float, so it spends less energy on swimming",
            "It insulates the body, so much less heat is lost to the water",
            "It fills with warm air, which the seal breathes out slowly when "
            "diving",
            "It stops water entering the skin, so the seal cannot get cold",
        ],
        "correct_index": 1,
        "why": "Fat is a poor conductor of heat, so a thick blubber layer "
               "slows the rate at which body heat passes out into the cold water.",
    },
    {
        "id": "ks4-adaptations-s06",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A jackrabbit's very large ears carry many blood vessels "
                "close to the surface. Explain how this helps it in the desert.",
        "options": [
            "Blood is warmed inside the ears before it flows back into the "
            "body core",
            "The blood vessels carry extra water up to the ears for storage",
            "The ears detect the warmest patches of ground to be avoided",
            "Heat passes out of the blood through the large ear surface",
        ],
        "correct_index": 3,
        "why": "A large, thin, well-supplied surface lets heat pass from the "
               "blood to the air, so the animal cools down without having to lose "
               "water.",
    },
    {
        "id": "ks4-adaptations-s07",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Many desert animals have pale, sandy-coloured fur. Explain "
                "the two advantages this gives.",
        "options": [
            "It absorbs sunlight, and it warns predators that they are toxic",
            "It reflects sunlight, and it makes them visible to all of their "
            "own kind",
            "It reflects sunlight, and it camouflages them against the sand",
            "It absorbs water from the air, and it hides them from their prey",
        ],
        "correct_index": 2,
        "why": "A pale surface reflects rather than absorbs the sun's energy, "
               "and the same colour makes the animal hard to see against pale desert "
               "ground.",
    },
    {
        "id": "ks4-adaptations-s08",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cactus has spines in place of broad leaves. Explain how "
                "this reduces its water loss.",
        "options": [
            "Spines are hollow, so the water inside them cannot escape",
            "Spines have a much smaller surface area than leaves do",
            "Spines shade the stem, so the plant stays cooler throughout the "
            "whole day",
            "Spines have no stomata, and water is lost only through roots",
        ],
        "correct_index": 1,
        "why": "Water is lost by evaporation from a leaf's surface, so "
               "cutting that surface down to a spine cuts the rate of loss.",
    },
    {
        "id": "ks4-adaptations-s09",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why producing very concentrated urine counts as a "
                "functional adaptation and not a structural one.",
        "options": [
            "It happens only at night, and every night-time feature is "
            "functional",
            "It is a chemical process inside the body, not a body feature",
            "It involves the kidney, and every organ is called functional",
            "It can be switched on and off, unlike any structural feature",
        ],
        "correct_index": 1,
        "why": "Functional adaptations are internal chemical or physiological "
               "processes; the kidney is a structure, but concentrating the urine is "
               "something it does.",
    },
    {
        "id": "ks4-adaptations-s10",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how hunting as a pack lets wolves bring down prey "
                "much larger than a single wolf could.",
        "options": [
            "Wolves in a pack are individually stronger than lone wolves",
            "A pack frightens large prey into running towards the wolves",
            "Large prey animals cannot see a group as well as they see a "
            "single wolf",
            "Several wolves can tire and surround an animal together",
        ],
        "correct_index": 3,
        "why": "Cooperating lets the pack attack from several sides at once "
               "and wear the animal down, which no individual could manage alone.",
    },
    {
        "id": "ks4-adaptations-s11",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Camouflage is listed as both a predator adaptation and a "
                "prey adaptation. Explain how its purpose differs.",
        "options": [
            "A predator hides from its own young; prey hide from the wind and "
            "rain",
            "A predator uses colour and prey uses shape to hide themselves",
            "A predator hides to approach; prey hide to avoid being found",
            "A predator hides at night and prey hide during the daytime",
        ],
        "correct_index": 2,
        "why": "The same feature serves two different ends: concealment lets "
               "a hunter get close enough to strike, and lets prey escape being "
               "detected at all.",
    },
    {
        "id": "ks4-adaptations-s12",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A snowshoe hare's coat is brown in summer and white in "
                "winter. Explain the advantage of the change.",
        "options": [
            "White fur is warmer, so it suits the cold winter",
            "It stays camouflaged as the colour of its surroundings changes",
            "Brown fur absorbs water, which it needs in summer",
            "The change tells other hares the season",
        ],
        "correct_index": 1,
        "why": "Camouflage only works if it matches the background, so a coat "
               "that changes with the seasons keeps the hare hidden all year.",
    },
    {
        "id": "ks4-adaptations-s13",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An anglerfish living in deep water produces its own light. "
                "Explain how this helps it feed.",
        "options": [
            "The light draws prey towards the anglerfish's mouth",
            "The light lets the anglerfish photosynthesise its own food",
            "The light warms the water around it, which attracts fish looking "
            "for heat",
            "The light lets the anglerfish see the sea floor far below it",
        ],
        "correct_index": 0,
        "why": "In total darkness a point of light is the only thing prey can "
               "see, so the lure brings them within reach of the fish's jaws.",
    },
    {
        "id": "ks4-adaptations-s14",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fish living 3 km below the surface needs "
                "specialised cell membranes and proteins.",
        "options": [
            "Ordinary membranes and proteins would not work under the pressure",
            "Ordinary membranes dissolve in cold deep water",
            "The fish photosynthesises, which needs proteins",
            "Special proteins let it absorb oxygen through its skin",
        ],
        "correct_index": 0,
        "why": "The pressure kilometres down is enormous, so the fish needs "
               "membranes and enzymes that keep their shape and keep working under "
               "it.",
    },
    {
        "id": "ks4-adaptations-s15",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lynx has sharp retractable claws and long canine teeth. "
                "Classify these features and state what they are for.",
        "options": [
            "Structural, and they are for catching and killing prey",
            "Functional, and they are for digesting the meat it swallows",
            "Behavioural, and they are for signalling to rival lynx",
            "Functional, and they are for keeping the lynx warm through the "
            "winter",
        ],
        "correct_index": 0,
        "why": "Claws and teeth are physical features of the body, which "
               "makes them structural, and a predator uses them to seize and kill "
               "what it hunts.",
    },
    {
        "id": "ks4-adaptations-s16",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A common wasp has bold black and yellow bands. Explain how "
                "this colouring protects it.",
        "options": [
            "It camouflages the wasp against the flowers",
            "It reflects sunlight, so the wasp stays cool",
            "It warns predators that the wasp can sting, so it is left alone",
            "It makes the wasp look larger than it is",
        ],
        "correct_index": 2,
        "why": "Warning colouration teaches predators to associate the "
               "pattern with a painful sting, so they learn to avoid the species "
               "altogether.",
    },
    {
        "id": "ks4-adaptations-s17",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A polar bear's dense fur traps a layer of air next to its "
                "skin. Explain how the trapped air helps the bear.",
        "options": [
            "Air makes the bear lighter, so it can run across thin ice",
            "The trapped air is used for breathing while the bear swims",
            "Air is a poor conductor, so it slows the loss of body heat",
            "Trapped air keeps the fur dry, and dry fur reflects the sunlight "
            "well",
        ],
        "correct_index": 2,
        "why": "Still air conducts heat very poorly, so a trapped layer of it "
               "acts as insulation between the warm skin and the cold surroundings.",
    },
    {
        "id": "ks4-adaptations-s18",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hibernating is useful to a mammal living where "
                "winter food is scarce.",
        "options": [
            "It grows faster while asleep, so it is larger by the spring",
            "Predators hibernate at the same time, so nothing hunts it in "
            "winter",
            "Its body makes its own food while it is not moving about",
            "Its energy needs fall, so the food it stored lasts longer",
        ],
        "correct_index": 3,
        "why": "Hibernation lowers the animal's metabolic rate, so it needs "
               "far less energy and can survive the months when there is little to "
               "eat.",
    },
    {
        "id": "ks4-adaptations-s19",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a large surface area relative to volume helps an "
                "animal living in a hot climate.",
        "options": [
            "More surface means the animal can absorb more of the sunlight",
            "More surface means more heat can pass out to the surroundings",
            "A large surface area holds more water, so the animal dries out "
            "very slowly",
            "A large surface lets the animal take in oxygen through its skin",
        ],
        "correct_index": 1,
        "why": "Heat leaves an animal across its surface, so the more surface "
               "there is for each unit of volume, the faster the body can shed heat.",
    },
    {
        "id": "ks4-adaptations-s20",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camel can lose a quarter of its body water and still "
                "function. Classify this adaptation and explain its value.",
        "options": [
            "Structural, and it means the camel can drink far less often",
            "Behavioural, and it means the camel moves about at night so as "
            "to stay cool",
            "Structural, and it means the camel carries water in its hump",
            "Functional, and it means the camel can go longer between drinks",
        ],
        "correct_index": 3,
        "why": "Tolerating dehydration is an internal physiological property, "
               "so it is functional, and it lets the camel cross ground with no "
               "water on it.",
    },
    {
        "id": "ks4-adaptations-s21",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how staying in a large herd lowers the risk to an "
                "individual zebra.",
        "options": [
            "A zebra inside a herd can run considerably faster than a lone "
            "one can",
            "A herd is too heavy for a lion to knock over and attack",
            "A lion finds it hard to single one animal out of many",
            "Zebras in a herd take turns to sleep, so none is ever caught",
        ],
        "correct_index": 2,
        "why": "In a crowd there are more eyes watching and the predator "
               "struggles to pick out and follow one target, so each individual's "
               "chance of being taken falls.",
    },
    {
        "id": "ks4-adaptations-s22",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An owl's eyes both face forwards. Explain how this suits the "
                "way an owl feeds.",
        "options": [
            "It gives binocular vision, so the owl can judge distance",
            "It lets the owl watch two different mice at the same time",
            "It gives the owl the widest possible field of view during the "
            "night",
            "It means the owl can see colours that its prey cannot see",
        ],
        "correct_index": 0,
        "why": "The two fields of view overlap, which gives the depth "
               "perception a predator needs to judge exactly where to strike.",
    },
    {
        "id": "ks4-adaptations-s23",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cheetah's speed depends on long legs and on a heart that "
                "delivers oxygen very fast. Classify these two features.",
        "options": [
            "The legs are structural and the heart's output is functional",
            "Both are structural features of the cheetah's own body",
            "Both are behavioural, because running is something it does",
            "The legs are functional and the heart is a structural feature",
        ],
        "correct_index": 0,
        "why": "The limbs are physical features, so they are structural, "
               "while the rate at which the heart supplies oxygen is an internal "
               "process, so it is functional.",
    },
    {
        "id": "ks4-adaptations-s24",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a desert rodent that feeds at night loses less "
                "water than one feeding by day.",
        "options": [
            "Night air holds no water, so none can be drawn out of the rodent",
            "Night air is cooler, so less water evaporates from the animal",
            "The rodent drinks the dew that forms on the ground after dark",
            "Rodents do not respire at night, so they release no water vapour",
        ],
        "correct_index": 1,
        "why": "Evaporation is slower in cool air, so being active after dark "
               "cuts the water the animal loses from its breath and its skin.",
    },
    {
        "id": "ks4-adaptations-s25",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a thick waxy cuticle on a leaf's upper surface "
                "reduces the plant's water loss.",
        "options": [
            "Wax reflects the sunlight, so the leaf never warms up at all",
            "Wax seals the stomata shut whenever the air becomes dry",
            "Wax is denser than water, so it holds the water inside the whole "
            "leaf",
            "Wax is waterproof, so water cannot evaporate through it",
        ],
        "correct_index": 3,
        "why": "The cuticle is a waterproof layer, so water vapour can leave "
               "only through the stomata rather than across the whole leaf surface.",
    },
    {
        "id": "ks4-adaptations-s26",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ptarmigan's plumage matches grey mountain rock in summer "
                "and snow in winter. Suggest which predator this protects it from.",
        "options": [
            "A hunting bird, which finds its prey by sight",
            "A fox, which tracks its prey mainly by scent",
            "A stoat, which hunts inside burrows underground",
            "An owl, which locates its prey by sound in the dark",
        ],
        "correct_index": 0,
        "why": "Camouflage works against a predator that hunts visually, so "
               "it is of most use against a bird of prey searching the ground from "
               "above.",
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "ks4-adaptations-h05",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An Arctic fox has small rounded ears and a fennec fox has "
                "very large ones. Compare the two and explain the difference.",
        "options": [
            "Small ears cut heat loss in the cold; large ears increase it",
            "Small ears hear better in snow, and large ears hear better in "
            "sand",
            "Large ears protect the fennec fox from the desert sun overhead",
            "Small ears hold more fat, which the Arctic fox needs in winter",
        ],
        "correct_index": 0,
        "why": "Ear surface is where heat is exchanged, so the Arctic species "
               "keeps it small to conserve heat and the desert species makes it "
               "large to shed heat.",
    },
    {
        "id": "ks4-adaptations-h06",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a small mammal in the Arctic must eat far more "
                "food for its body mass than a large one.",
        "options": [
            "A small animal has more surface for its volume, so loses heat "
            "fast",
            "A small animal digests its food much less efficiently than a "
            "large",
            "A small animal moves about more, and movement uses all the energy",
            "A small animal has a larger volume for its surface, so cools fast",
        ],
        "correct_index": 0,
        "why": "A high surface area to volume ratio means heat escapes "
               "quickly, so the animal must respire more food simply to replace it.",
    },
    {
        "id": "ks4-adaptations-h07",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One desert plant has a single root 20 m deep; another has a "
                "wide shallow root mat. Suggest how both can succeed in the same "
                "desert.",
        "options": [
            "The shallow-rooted plant takes its water from the deeper one",
            "Deep roots work in summer and shallow roots work in winter",
            "They reach two different water supplies, deep and after rain",
            "Root depth has no effect, so any root pattern would succeed",
        ],
        "correct_index": 2,
        "why": "There is more than one way to solve a problem: the deep root "
               "reaches permanent ground water while the shallow mat captures brief "
               "rainfall before it drains away.",
    },
    {
        "id": "ks4-adaptations-h08",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a harmless hoverfly gains less protection from "
                "its wasp-like bands if wasps become rare in an area.",
        "options": [
            "Predators no longer learn to associate the pattern with a sting",
            "Hoverflies lose their banding whenever wasp numbers fall",
            "Rare species are hunted harder than common ones in every habitat",
            "Without wasps nearby, hoverflies have nothing left to feed on",
        ],
        "correct_index": 0,
        "why": "Mimicry works by borrowing a lesson predators have already "
               "learned, so if few predators meet the stinging model the pattern "
               "stops carrying a warning.",
    },
    {
        "id": "ks4-adaptations-h09",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why bright warning colours are an advantage even "
                "though they make an animal far easier to see.",
        "options": [
            "Bright colours make the animal look bigger than it really is",
            "Being seen and recognised as toxic stops the attack happening",
            "Predators cannot see bright colours as clearly as dull ones",
            "Bright colours reflect heat, which matters more than hiding",
        ],
        "correct_index": 1,
        "why": "The point is not to avoid detection but to be identified: a "
               "predator that has learned the pattern rejects the animal before "
               "eating it.",
    },
    {
        "id": "ks4-adaptations-h10",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare growing a thick winter coat with hibernating as ways "
                "of surviving a cold winter.",
        "options": [
            "A coat is structural and keeps the animal active; sleep is not",
            "A coat is behavioural and hibernating is a structural change",
            "Both are functional, since both change the animal's chemistry",
            "A coat works only for large animals and hibernating for small",
        ],
        "correct_index": 0,
        "why": "The coat is a structural adaptation that lets the animal keep "
               "feeding through the cold, while hibernation is a behavioural one "
               "that avoids the cold by shutting down.",
    },
    {
        "id": "ks4-adaptations-h11",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lantern fish has a light-producing organ. Explain why the "
                "light itself is classed as a functional adaptation while the organ "
                "is structural.",
        "options": [
            "The light can be switched off and a structure cannot be",
            "The organ is inherited and the light has to be learned",
            "The organ is a body part; making light is a chemical process",
            "Light is energy, so it is functional",
        ],
        "correct_index": 2,
        "why": "Structural describes a physical feature of the body, and "
               "functional describes an internal chemical or physiological process "
               "that the feature carries out.",
    },
    {
        "id": "ks4-adaptations-h12",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a chameleon's colour change is behavioural "
                "because the animal decides to do it. Evaluate this.",
        "options": [
            "It is sound, because any change an animal makes is behavioural",
            "It is unsound: the change is a physiological one in the skin",
            "It is unsound, because colour change is a structural feature",
            "It is sound, because the chameleon learns the trick when young",
        ],
        "correct_index": 1,
        "why": "The colour change is produced by cells in the skin responding "
               "to a stimulus, which makes it a functional adaptation rather than "
               "something the animal chooses to do.",
    },
    {
        "id": "ks4-adaptations-h13",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A polar bear's skin under its white fur is black. Suggest "
                "how this could be an advantage.",
        "options": [
            "A dark surface absorbs more of the heat from the sunlight",
            "A dark surface reflects sunlight away from the animal's body",
            "Black skin is thicker than pale skin, so it insulates the bear "
            "better",
            "Black skin camouflages the bear when it swims under the ice",
        ],
        "correct_index": 0,
        "why": "Light passing between the hairs reaches a dark surface, which "
               "absorbs the energy rather than reflecting it, so more of the sun's "
               "warmth is retained.",
    },
    {
        "id": "ks4-adaptations-h14",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over many generations both a hunting cat and the antelope it "
                "hunts become faster. Explain why neither gains a lasting advantage.",
        "options": [
            "Each improvement selects for improvement in the other species",
            "Both species reach the fastest speed any animal can ever reach",
            "Speed stops being useful once both species are equally quick",
            "Each species copies the other's adaptation within a generation",
        ],
        "correct_index": 0,
        "why": "Faster predators select the fastest prey, and faster prey "
               "select the fastest predators, so the pressure on each is renewed by "
               "the other's response.",
    },
    {
        "id": "ks4-adaptations-h15",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lizard P loses 8 g of water per kg of body mass each day and "
                "lizard Q loses 20 g per kg per day. Determine which is better "
                "adapted to a desert and explain.",
        "options": [
            "Q, because losing more water shows it can take in more",
            "P, because it conserves water, which is scarce in a desert",
            "Neither, because water loss does not affect desert survival",
            "Q, because a higher water loss cools the lizard down faster",
        ],
        "correct_index": 1,
        "why": "Water is the resource in shortest supply in a desert, so the "
               "animal losing 8 g per kg per day rather than 20 g can survive far "
               "longer between drinks.",
    },
    {
        "id": "ks4-adaptations-h16",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a fish caught 2 km down often dies when it is "
                "brought quickly to the surface.",
        "options": [
            "The surface water contains far too much dissolved oxygen for it",
            "It cannot see in bright light, so it is unable to find any food",
            "Its body is adapted to high pressure, which falls on the way up",
            "Its light-producing organ stops working as soon as it reaches "
            "daylight",
        ],
        "correct_index": 2,
        "why": "An adaptation suits one set of conditions: membranes, "
               "proteins and gas spaces built for enormous pressure are damaged when "
               "that pressure is removed.",
    },
    {
        "id": "ks4-adaptations-h17",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Arctic summers are becoming longer and warmer. Evaluate "
                "whether the Arctic fox's thick coat remains an advantage.",
        "options": [
            "It is still wholly an advantage, since winters remain very cold",
            "It becomes more valuable, because thick fur also keeps heat out",
            "It makes no difference, because fur thickness cannot be selected "
            "for",
            "Its value falls as warm spells make overheating more likely",
        ],
        "correct_index": 3,
        "why": "An adaptation is only an advantage in the conditions it "
               "suits, so insulation that is vital in a long hard winter becomes a "
               "cost as warm periods lengthen.",
    },
    {
        "id": "ks4-adaptations-h18",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A brown hare has long ears and long limbs; an Arctic hare's "
                "are much shorter. Explain the consequence for heat loss.",
        "options": [
            "The Arctic hare has more surface for its volume, so loses less",
            "Both lose heat at the same rate, since both are the same species",
            "The brown hare loses less heat, because its limbs are furred",
            "The Arctic hare has less surface for its volume, so loses less",
        ],
        "correct_index": 3,
        "why": "Shortening the extremities cuts the total surface area "
               "without cutting the volume, which lowers the surface area to volume "
               "ratio and so lowers heat loss.",
    },
    {
        "id": "ks4-adaptations-h19",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the plants on an exposed clifftop are nearly all "
                "low-growing and cushion-shaped.",
        "options": [
            "A low shape catches more of the light that reaches the cliff",
            "Tall plants cannot take up any minerals from a thin clifftop soil",
            "A low shape avoids the wind, cutting damage and water loss",
            "A cushion shape lets the plant roll when the wind uproots it",
        ],
        "correct_index": 2,
        "why": "Wind speed rises with height above the ground, so staying low "
               "reduces both the physical battering and the rate at which water is "
               "stripped from the leaves.",
    },
    {
        "id": "ks4-adaptations-h20",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare hibernating and migrating as behavioural answers to "
                "a cold winter.",
        "options": [
            "Hibernating is behavioural and migrating is a structural change",
            "Hibernating waits the winter out; migrating leaves it behind",
            "Both lower the animal's metabolic rate for the whole winter",
            "Migrating suits small animals and hibernating suits large ones",
        ],
        "correct_index": 1,
        "why": "Both are behavioural, but one avoids the cold season by "
               "shutting down where it is and the other avoids it by moving to "
               "somewhere the conditions are better.",
    },
    {
        "id": "ks4-adaptations-h21",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a stoat's white winter coat becomes a "
                "disadvantage in a winter with very little snow.",
        "options": [
            "White fur is thinner, so the stoat is colder without the snow",
            "White fur cannot be changed back once the snow has melted",
            "A white coat makes the stoat's own prey easier for it to see",
            "A white animal stands out against dark ground, so it is seen",
        ],
        "correct_index": 3,
        "why": "Camouflage depends on matching the background, so a coat "
               "selected for a snowy winter makes the animal conspicuous when the "
               "snow fails to arrive.",
    },
    {
        "id": "ks4-adaptations-h22",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camel's hump is a store of fat. Explain why this single "
                "feature can be described as both structural and functional.",
        "options": [
            "The hump is structural only in the summer",
            "The hump is a body feature; using the fat is a chemical process",
            "It is functional, as the camel chooses to use it",
            "Any feature that stores something counts as both",
        ],
        "correct_index": 1,
        "why": "The hump itself is a physical part of the body, so it is "
               "structural, while respiring the fat it holds to release energy is an "
               "internal process, so that is functional.",
    },
    {
        "id": "ks4-adaptations-h23",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A desert beetle is pale and a mountain-top beetle of a "
                "related species is almost black. Explain each colour.",
        "options": [
            "Pale absorbs the desert sun; dark reflects the mountain's warmth",
            "Pale reflects the desert sun; dark absorbs the mountain's warmth",
            "Both colours are camouflage and have nothing to do with heat",
            "Pale beetles are younger and darken as they grow older with age",
        ],
        "correct_index": 1,
        "why": "In a desert the problem is shedding heat, so a reflective "
               "pale surface helps, while on a cold mountain the problem is gaining "
               "it, so a dark absorbing surface helps.",
    },
    {
        "id": "ks4-adaptations-h24",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that an organism with more adaptations is "
                "better off than one with fewer.",
        "options": [
            "It is correct, because each adaptation raises survival further",
            "It is wrong, because an adaptation costs more than it gives in "
            "return",
            "It is correct, because adaptations can be counted and compared",
            "It depends: what matters is whether they fit the conditions",
        ],
        "correct_index": 3,
        "why": "An adaptation is only worth having in the environment it "
               "suits, so the number of them says nothing on its own about how well "
               "an organism is suited to where it lives.",
    },
    {
        "id": "ks4-adaptations-h25",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two unrelated desert mammals on different continents both "
                "have unusually large ears. Suggest why.",
        "options": [
            "The two species must be closely related after all",
            "One species copied the feature after meeting the other",
            "Similar conditions selected the same solution in each of them",
            "Large ears develop in any mammal born in heat",
        ],
        "correct_index": 2,
        "why": "Natural selection acts on whatever variation is present, so "
               "the same environmental problem — shedding heat without losing water "
               "— can select the same answer twice over.",
    },
    {
        "id": "ks4-adaptations-h26",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which single adaptation would be of most use to a "
                "mammal moving into a very hot, very dry desert, and justify your "
                "choice.",
        "options": [
            "Thicker fur, because insulation keeps the daytime heat out",
            "Darker skin, because dark copes with strong sun",
            "Larger body size, because it stores more body fat",
            "A means of conserving water, because water is the scarcest need",
        ],
        "correct_index": 3,
        "why": "In a hot desert an animal can find shade and shelter from the "
               "heat, but there is no substitute for water, so conserving it is the "
               "limiting problem.",
    },
]
