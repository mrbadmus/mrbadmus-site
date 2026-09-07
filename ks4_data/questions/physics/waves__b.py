"""Physics · Waves — EM hazards and uses, refraction by wave fronts, lenses,
black bodies and the Earth's radiation balance (part B of `waves`).

Six subtopics: `properties-em-waves-2`, `uses-em-waves`, `wave-front-refraction`,
`lenses`, `infrared-black-bodies`, `radiation-balance-temperature`.

The distractors are built from the declared misconceptions in the brief and
from what those misconceptions look like when a student writes them out:
ionising confused with merely hot; MRI confused with X-ray imaging; refraction
described with cause and effect reversed (bending said to cause the slowing);
real and virtual images swapped, and magnification given a unit; a perfect
black body assumed to be a poor emitter because it is a perfect absorber; and
greenhouse gases said to reflect, rather than absorb and re-emit, the infrared
the Earth radiates.

⚠️ Not one question here needs a figure. Every lens arrangement is stated in
words as an object distance against a focal length, and every wave front
question describes the boundary rather than pointing at a drawing of it.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── properties-em-waves-2 ───────────────────────────────────────────
    # BASE (foundation, not triple). Radio-wave production and induced a.c.
    # are the HIGHER-TIER extension in the brief, so they appear NOWHERE in
    # either waves file — not here, and not under wave-front-refraction.
    # (Cold review, MRB-332: verified by grep across both files.)
    {
        "id": "ks4-properties-em-waves-2-e01",
        "subtopic_slug": "properties-em-waves-2",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these types of electromagnetic radiation is "
                "NOT ionising.",
        "options": [
            "Gamma rays",
            "Ultraviolet",
            "Infrared",
            "X-rays",
        ],
        "correct_index": 2,
        "why": "Infrared has too little energy per photon to remove electrons "
               "from atoms — it heats tissue rather than ionising it.",
    },
    {
        "id": "ks4-properties-em-waves-2-e02",
        "subtopic_slug": "properties-em-waves-2",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the order of these three types of electromagnetic "
                "radiation, from the least hazardous to the most hazardous: "
                "X-rays, infrared, ultraviolet.",
        "options": [
            "Infrared, ultraviolet, X-rays",
            "X-rays, ultraviolet, infrared",
            "Ultraviolet, infrared, X-rays",
            "Infrared, X-rays, ultraviolet",
        ],
        "correct_index": 0,
        "why": "Hazard rises with frequency across the spectrum, and of these "
               "three infrared has the lowest frequency and X-rays the "
               "highest.",
    },
    {
        "id": "ks4-properties-em-waves-2-e03",
        "subtopic_slug": "properties-em-waves-2",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which property of an electromagnetic wave increases as "
                "the hazard it presents increases.",
        "options": [
            "Its wavelength",
            "Its speed in a vacuum",
            "Its amplitude, with frequency having no effect",
            "Its frequency",
        ],
        "correct_index": 3,
        "why": "Hazard rises with frequency, because a higher-frequency wave "
               "carries more energy in each photon.",
    },
    {
        "id": "ks4-properties-em-waves-2-e04",
        "subtopic_slug": "properties-em-waves-2",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens when an electromagnetic wave is absorbed "
                "by a material.",
        "options": [
            "It passes through the material without changing it in any way",
            "Its energy is transferred to the material, which often heats up",
            "It bounces back off the boundary into the medium it came from",
            "It changes direction at the boundary because its speed changes",
        ],
        "correct_index": 1,
        "why": "Absorption means the wave's energy is transferred to the "
               "material — the other three options describe transmission, "
               "reflection and refraction instead.",
    },
    {
        "id": "ks4-properties-em-waves-2-s01",
        "subtopic_slug": "properties-em-waves-2",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave oven heats a bowl of soup. Explain why the soup "
                "gets hot.",
        "options": [
            "The microwaves are absorbed by water molecules in the soup, "
            "transferring energy to them",
            "The microwaves ionise the water molecules in the soup, and the "
            "ions formed release energy",
            "The microwaves are reflected by the surface of the soup, and "
            "each reflection releases energy into it",
            "The microwaves have a very short wavelength, so they carry "
            "thermal energy directly into the soup",
        ],
        "correct_index": 0,
        "why": "Microwaves are absorbed by water molecules, and the absorbed "
               "energy is transferred to the food's store of thermal energy.",
    },
    {
        "id": "ks4-properties-em-waves-2-s02",
        "subtopic_slug": "properties-em-waves-2",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician is exposed to the beam of a very high-power "
                "laser, which emits visible light. Describe the main hazard.",
        "options": [
            "Ionisation of DNA in the skin cells, leading to cancer",
            "Sunburn on every area of exposed skin",
            "Radiation sickness, because the dose received is very large",
            "Damage to the retina at the back of the eye",
        ],
        "correct_index": 3,
        "why": "Visible light is not ionising, but a very intense beam is "
               "focused by the eye onto a tiny area of the retina and can "
               "damage it.",
    },
    {
        "id": "ks4-properties-em-waves-2-s03",
        "subtopic_slug": "properties-em-waves-2",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One person is exposed to ultraviolet radiation and another "
                "to microwaves of the same intensity. Explain which exposure "
                "carries the greater risk of cancer.",
        "options": [
            "The microwaves, because they heat tissue from the inside and "
            "the heating damages the cells",
            "The ultraviolet, because it is ionising and can damage the DNA "
            "inside skin cells",
            "Both are equally risky, because cancer risk depends only on the "
            "intensity and not on the type of wave",
            "Neither, because cancer is only ever caused by gamma rays from "
            "radioactive materials",
        ],
        "correct_index": 1,
        "why": "Ultraviolet is ionising and can damage DNA, causing "
               "mutations; microwaves at these levels only warm tissue.",
    },
    {
        "id": "ks4-properties-em-waves-2-s04",
        "subtopic_slug": "properties-em-waves-2",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a lead apron is placed over the parts of a "
                "patient's body that are not being imaged during an X-ray.",
        "options": [
            "Lead reflects X-rays back towards the machine, which makes the "
            "image of the injured area sharper",
            "Lead is a good thermal insulator, so it prevents the X-ray beam "
            "from burning the skin underneath it",
            "Lead absorbs X-rays, so far fewer reach and ionise cells in "
            "tissue that does not need to be imaged",
            "Lead slows the X-rays down, so that by the time they reach the "
            "body they are no longer ionising",
        ],
        "correct_index": 2,
        "why": "Lead is a strong absorber of X-rays, so it cuts the dose of "
               "ionising radiation reaching tissue that gains nothing from "
               "being exposed.",
    },
    {
        "id": "ks4-properties-em-waves-2-h01",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Infrared radiation is dangerous because "
                "it is ionising, and that is what makes it burn skin.' "
                "Explain what is wrong with this statement.",
        "options": [
            "Nothing is wrong — infrared is weakly ionising, and the "
            "ionisation is what produces the burn",
            "Infrared is not absorbed by skin at all, so it cannot in fact "
            "cause a burn under any conditions",
            "Infrared is ionising, but the burns are actually caused by the "
            "ultraviolet that travels alongside it",
            "Infrared is not ionising — it burns because it is absorbed and "
            "transfers energy that heats the tissue",
        ],
        "correct_index": 3,
        "why": "A burn is a heating effect from absorbed energy; ionisation "
               "needs a much higher frequency than infrared has.",
    },
    {
        "id": "ks4-properties-em-waves-2-h02",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radiographer steps behind a lead screen for every X-ray "
                "image they take, but the patient does not. Suggest why.",
        "options": [
            "The patient receives a much larger dose, so a lead screen would "
            "be far too thin to give them any protection",
            "The radiographer takes many images every working day, so their "
            "total dose would be far larger than any one patient's",
            "The lead screen would block the X-ray beam completely, so it "
            "cannot be placed anywhere near the patient",
            "The patient is exposed only to non-ionising radiation, so there "
            "is no reason for them to be shielded at all",
        ],
        "correct_index": 1,
        "why": "Risk builds with total dose: one image is a small exposure, "
               "but many images every day would accumulate into a large one.",
    },
    {
        "id": "ks4-properties-em-waves-2-h03",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ultraviolet from the Sun reaches the ground, but gamma rays "
                "from space are almost all absorbed high in the atmosphere. "
                "A student concludes that ultraviolet must therefore be the "
                "more hazardous radiation. Evaluate this conclusion.",
        "options": [
            "Correct — whichever radiation actually reaches us is always the "
            "more hazardous of the two",
            "Correct — ultraviolet has a higher frequency than gamma "
            "radiation, so each photon carries more energy",
            "Incorrect — gamma radiation is more ionising and more hazardous "
            "per photon; the student has confused hazard with exposure",
            "Incorrect — gamma radiation is not ionising at all, so it would "
            "present no hazard to anyone even if it did reach the ground",
        ],
        "correct_index": 2,
        "why": "Gamma has the higher frequency and is the more ionising, so "
               "it is the more hazardous; the atmosphere only changes how "
               "much of it we are exposed to.",
    },
    {
        "id": "ks4-properties-em-waves-2-h04",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "X-rays pass through soft tissue but are absorbed by bone, "
                "while visible light is absorbed by both. Explain what "
                "decides whether a material absorbs a given electromagnetic "
                "wave.",
        "options": [
            "The wavelength of the wave together with the properties of the "
            "material it meets",
            "The amplitude of the wave alone — a wave of larger amplitude is "
            "always absorbed",
            "The speed of the wave in the material — a slower wave is always "
            "the one that is absorbed",
            "The temperature of the material alone — a hotter material "
            "absorbs every wavelength equally",
        ],
        "correct_index": 0,
        "why": "Absorption depends on the match between the wave's wavelength "
               "and the material, which is why one material can be opaque to "
               "one wavelength and transparent to another.",
    },

    # ── uses-em-waves ───────────────────────────────────────────────────
    {
        "id": "ks4-uses-em-waves-e01",
        "subtopic_slug": "uses-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of electromagnetic radiation used by a "
                "television remote control.",
        "options": [
            "Ultraviolet",
            "Infrared",
            "Microwaves",
            "X-rays",
        ],
        "correct_index": 1,
        "why": "A remote control sends coded pulses of infrared to a detector "
               "on the television.",
    },
    {
        "id": "ks4-uses-em-waves-e02",
        "subtopic_slug": "uses-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of electromagnetic radiation used in an MRI "
                "scanner.",
        "options": [
            "X-rays",
            "Gamma rays",
            "Ultraviolet",
            "Radio waves",
        ],
        "correct_index": 3,
        "why": "An MRI scanner uses radio waves with a strong magnetic field, "
               "so the patient is not exposed to any ionising radiation.",
    },
    {
        "id": "ks4-uses-em-waves-e03",
        "subtopic_slug": "uses-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the type of electromagnetic radiation used to scan "
                "luggage at an airport.",
        "options": [
            "X-rays",
            "Radio waves",
            "Infrared",
            "Visible light",
        ],
        "correct_index": 0,
        "why": "X-rays pass through fabric and plastic but are absorbed by "
               "denser objects such as metal, so the contents show up.",
    },
    {
        "id": "ks4-uses-em-waves-e04",
        "subtopic_slug": "uses-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of electromagnetic radiation a radio "
                "telescope collects from distant galaxies.",
        "options": [
            "Gamma rays",
            "Ultraviolet",
            "Radio waves",
            "Microwaves",
        ],
        "correct_index": 2,
        "why": "Radio telescopes detect the radio waves emitted by distant "
               "stars and galaxies.",
    },
    {
        "id": "ks4-uses-em-waves-s01",
        "subtopic_slug": "uses-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A television picture is broadcast to a rooftop aerial using "
                "radio waves rather than visible light. Explain why radio "
                "waves are used.",
        "options": [
            "Radio waves travel faster than visible light through the air, so "
            "the picture arrives without any delay",
            "Radio waves carry far more energy in each wave, so the signal is "
            "strong enough to reach the aerial",
            "Radio waves are ionising, so they can pass through solid walls "
            "in a way that visible light cannot",
            "Radio waves are not absorbed by cloud, walls and roofs in the "
            "way visible light is, so they still reach the aerial",
        ],
        "correct_index": 3,
        "why": "A material treats different wavelengths differently: radio "
               "waves pass through cloud and buildings that stop visible "
               "light, which is what makes them useful for broadcasting.",
    },
    {
        "id": "ks4-uses-em-waves-s02",
        "subtopic_slug": "uses-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radar is used to find the distance to an aircraft. Describe "
                "how that distance is determined.",
        "options": [
            "By measuring how much of the microwave beam is absorbed by the "
            "body of the aircraft",
            "By measuring the frequency of the microwaves that return to the "
            "radar station from the aircraft",
            "By measuring the time taken for a microwave pulse to travel to "
            "the aircraft and reflect back",
            "By measuring how far the microwave beam is refracted as it "
            "passes close to the aircraft",
        ],
        "correct_index": 2,
        "why": "The pulse travels at the speed of light, so the round-trip "
               "time gives the distance directly.",
    },
    {
        "id": "ks4-uses-em-waves-s03",
        "subtopic_slug": "uses-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Surgical instruments are sealed inside plastic packets and "
                "then sterilised using gamma rays. Explain why gamma rays "
                "are suitable for this.",
        "options": [
            "Gamma rays heat the contents of the packet to a high "
            "temperature, and it is the heat that kills the microorganisms",
            "Gamma rays are highly penetrating, so they pass through the "
            "sealed packet and kill the microorganisms inside it",
            "Gamma rays are reflected by the plastic packet onto the "
            "instruments, which concentrates the dose they receive",
            "Gamma rays are absorbed by the plastic packet, which then "
            "releases a chemical that kills the bacteria inside",
        ],
        "correct_index": 1,
        "why": "Gamma radiation penetrates the packaging, so the instruments "
               "can be sterilised after sealing and stay sterile until use.",
    },
    {
        "id": "ks4-uses-em-waves-s04",
        "subtopic_slug": "uses-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a night-vision camera detects infrared rather "
                "than visible light.",
        "options": [
            "Warm objects emit infrared even in complete darkness, so an "
            "image can be formed with no visible light present",
            "Infrared travels faster than visible light through air, so the "
            "image is formed more quickly in poor conditions",
            "Infrared is ionising, so it produces a much stronger signal in "
            "the detector than visible light would",
            "Infrared reflects off objects far better than visible light "
            "does once the surroundings have gone dark",
        ],
        "correct_index": 0,
        "why": "Every warm object emits infrared of its own, so the camera "
               "does not need any source of light to see by.",
    },
    {
        "id": "ks4-uses-em-waves-h01",
        "subtopic_slug": "uses-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital needs an image of a torn ligament, which is soft "
                "tissue. Explain why an MRI scan is chosen rather than an "
                "X-ray.",
        "options": [
            "X-rays are hardly absorbed by soft tissue, so the ligament would "
            "barely show; MRI uses radio waves, which image soft tissue well "
            "and are not ionising",
            "X-rays are strongly absorbed by soft tissue and reflected by the "
            "surrounding bone, so an image of the torn ligament would come "
            "out far too bright for anyone to interpret",
            "MRI uses gamma radiation, which penetrates soft tissue much "
            "better than X-rays do and gives a far sharper picture of a torn "
            "ligament",
            "X-ray machines can only be used on the chest and the skull, so "
            "an injury to a limb of this kind must always be scanned using "
            "an MRI machine",
        ],
        "correct_index": 0,
        "why": "Soft tissue absorbs X-rays too weakly to give contrast, "
               "whereas MRI's radio waves image it well without any ionising "
               "dose.",
    },
    {
        "id": "ks4-uses-em-waves-h02",
        "subtopic_slug": "uses-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower wants to find which parts of a greenhouse are "
                "losing the most energy. Determine which type of "
                "electromagnetic radiation a suitable camera should detect, "
                "and why.",
        "options": [
            "Ultraviolet, because warm surfaces emit ultraviolet while cool "
            "surfaces do not, which gives a very clear contrast",
            "Infrared, because every object emits infrared and warmer "
            "surfaces emit more of it, so the losses show up as bright areas",
            "Microwaves, because they pass straight through the glass of the "
            "greenhouse and reveal whatever lies behind it",
            "X-rays, because they penetrate the whole structure and show the "
            "exact thickness of every panel of glass",
        ],
        "correct_index": 1,
        "why": "A thermal camera detects emitted infrared, and the warmest "
               "areas — the places losing most energy — emit the most.",
    },
    {
        "id": "ks4-uses-em-waves-h03",
        "subtopic_slug": "uses-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A security pen writes in an ink that is invisible in "
                "ordinary light but glows brightly when a special lamp is "
                "shone on it. Explain how this works.",
        "options": [
            "The lamp emits infrared, which heats the ink until it becomes "
            "hot enough to glow with its own visible light",
            "The lamp emits visible light of a single colour, which the ink "
            "reflects while absorbing every other colour present",
            "The lamp emits X-rays, which pass through the ink and cast a "
            "visible shadow of the writing onto the paper",
            "The lamp emits ultraviolet, which the ink absorbs and then "
            "re-emits as visible light — this is fluorescence",
        ],
        "correct_index": 3,
        "why": "Fluorescent materials absorb ultraviolet and re-emit the "
               "energy at the longer wavelengths of visible light.",
    },
    {
        "id": "ks4-uses-em-waves-h04",
        "subtopic_slug": "uses-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A medical tracer is a radioactive substance injected into a "
                "patient so that its movement through the body can be "
                "followed from outside. Explain why a gamma emitter is "
                "chosen.",
        "options": [
            "Gamma radiation is strongly absorbed by tissue, so it collects "
            "in the organ being studied and can be seen there",
            "Gamma radiation is not ionising, so it can safely be injected "
            "into a patient in any quantity that is needed",
            "Gamma radiation penetrates the body and escapes, so a detector "
            "outside the patient can find where the tracer has gone",
            "Gamma radiation is emitted only by healthy tissue, so any dark "
            "region on the finished image must be a diseased organ",
        ],
        "correct_index": 2,
        "why": "Only a highly penetrating radiation can escape the body to "
               "reach an external detector, which is what a gamma camera "
               "needs.",
    },

    # ── wave-front-refraction ───────────────────────────────────────────
    # TRIPLE ONLY, higher tier.
    {
        "id": "ks4-wave-front-refraction-e01",
        "subtopic_slug": "wave-front-refraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by a wave front.",
        "options": [
            "A line drawn parallel to the direction in which the energy "
            "carried by the wave is travelling outwards from its source",
            "The leading edge of the very first wave to arrive at a detector "
            "from the source",
            "A line joining any two crests of the wave that happen to be one "
            "wavelength apart",
            "A line joining all points of the wave that are at the same point "
            "in their cycle, such as all the crests",
        ],
        "correct_index": 3,
        "why": "A wave front joins points that are in phase — every crest of "
               "one ripple lies on the same wave front.",
    },
    {
        "id": "ks4-wave-front-refraction-e02",
        "subtopic_slug": "wave-front-refraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A wave meets a boundary at an angle and crosses into a "
                "material in which it travels faster. State how its direction "
                "changes.",
        "options": [
            "It bends towards the normal",
            "It bends away from the normal",
            "It carries on in exactly the same direction",
            "It turns back along the path it arrived on",
        ],
        "correct_index": 1,
        "why": "The end of the wave front that reaches the faster material "
               "first pulls ahead of the rest, swinging the front away from "
               "the normal.",
    },
    {
        "id": "ks4-wave-front-refraction-e03",
        "subtopic_slug": "wave-front-refraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Wave fronts and rays are both used to represent a wave. "
                "State what a ray represents.",
        "options": [
            "The distance the wave travels in one second",
            "The height of each crest above the undisturbed level",
            "The direction in which the wave is travelling",
            "The number of wave fronts passing a point each second",
        ],
        "correct_index": 2,
        "why": "A ray is an arrow showing the direction of travel, drawn at "
               "right angles to the wave fronts, which mark where the crests "
               "are.",
    },
    {
        "id": "ks4-wave-front-refraction-e04",
        "subtopic_slug": "wave-front-refraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "The wave fronts of a wave are further apart in material B "
                "than they are in material A. State which material the wave "
                "travels faster in.",
        "options": [
            "Material B, because the fronts are one wavelength apart and the "
            "frequency is the same in both",
            "Material A, because a slower wave always spreads its wave fronts "
            "further apart",
            "Neither — the speed is the same in both, because the frequency "
            "has not changed",
            "It cannot be decided without being told the frequency of the "
            "wave in each material",
        ],
        "correct_index": 0,
        "why": "The gap between neighbouring wave fronts is the wavelength, "
               "and with the frequency set by the source, v = fλ makes the "
               "longer wavelength the faster material.",
    },
    {
        "id": "ks4-wave-front-refraction-s01",
        "subtopic_slug": "wave-front-refraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A water wave in a ripple tank travels from deep water into "
                "shallow water, where it moves more slowly, meeting the "
                "boundary at an angle. Describe the change in its direction.",
        "options": [
            "It bends away from the normal",
            "It carries straight on with no change of direction",
            "It bends towards the normal",
            "It is reflected back into the deep water",
        ],
        "correct_index": 2,
        "why": "A wave entering a medium where it travels more slowly always "
               "bends towards the normal.",
    },
    {
        "id": "ks4-wave-front-refraction-s02",
        "subtopic_slug": "wave-front-refraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain, in terms of wave fronts, why a wave changes "
                "direction when it crosses a boundary at an angle.",
        "options": [
            "One end of each wave front enters the new medium first and "
            "changes speed before the other end, so the wave front pivots",
            "The wave front is reflected at the boundary, and the reflected "
            "part interferes with the part that is still arriving",
            "The frequency of the wave changes at the boundary, and any "
            "change of frequency will always change the direction",
            "The wave front is squashed by the pressure of the denser medium, "
            "and this squashing turns the whole wave to one side",
        ],
        "correct_index": 0,
        "why": "Because the wave front meets the boundary at an angle, one "
               "end changes speed before the other, and the front swings "
               "round.",
    },
    {
        "id": "ks4-wave-front-refraction-s03",
        "subtopic_slug": "wave-front-refraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A student says that light bends when it enters glass, and "
                "that this bending is what makes it slow down. Explain the "
                "error in their reasoning.",
        "options": [
            "There is no error — the bending at the surface is what causes "
            "light to lose speed inside the glass",
            "The error is the direction — light bends away from the normal "
            "rather than towards it when it passes from air into a block of "
            "glass",
            "The error is the medium — light speeds up in glass, and it is "
            "the speeding up that causes it to bend",
            "The cause and the effect are reversed — the light slows at the "
            "boundary, and it is that change of speed which makes it bend",
        ],
        "correct_index": 3,
        "why": "The change of speed comes first; the bending is its "
               "consequence, not its cause.",
    },
    {
        "id": "ks4-wave-front-refraction-s04",
        "subtopic_slug": "wave-front-refraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A sound wave of frequency 300 Hz travels through air at "
                "340 m/s and then passes into water, where its speed is "
                "1500 m/s. Calculate its wavelength in the water.",
        "options": [
            "1.1 m",
            "5.0 m",
            "0.20 m",
            "50 m",
        ],
        "correct_index": 1,
        "why": "The frequency does not change on refraction, so "
               "λ = v ÷ f = 1500 ÷ 300 = 5.0 m.",
    },
    {
        "id": "ks4-wave-front-refraction-h01",
        "subtopic_slug": "wave-front-refraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A radio wave of frequency 6.0 × 10⁶ Hz travels through air "
                "at 3.0 × 10⁸ m/s. It then enters a slab of material in which "
                "its speed falls to 2.4 × 10⁸ m/s. Calculate the change in "
                "its wavelength.",
        "options": [
            "It decreases by 40 m",
            "It decreases by 10 m",
            "It increases by 10 m",
            "It does not change, because the frequency does not change",
        ],
        "correct_index": 1,
        "why": "λ = v ÷ f, so the wavelength goes from 50 m to 40 m while the "
               "frequency stays at 6.0 × 10⁶ Hz — a decrease of 10 m.",
    },
    {
        "id": "ks4-wave-front-refraction-h02",
        "subtopic_slug": "wave-front-refraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A narrow beam of light passes from air into a rectangular "
                "glass block and out again into air through the opposite, "
                "parallel face. Predict the direction of the emerging beam "
                "compared with the beam that entered.",
        "options": [
            "It emerges along exactly the same line as the entering beam, "
            "with no sideways shift at all",
            "It emerges at right angles to the entering beam, having been "
            "turned twice at the two surfaces",
            "It emerges parallel to the entering beam but shifted sideways, "
            "bending towards the normal on entry and away from it on exit",
            "It emerges bent even further towards the normal than it was "
            "inside the block, because it refracts a second time as it "
            "leaves the glass",
        ],
        "correct_index": 2,
        "why": "The two parallel surfaces bend the beam by equal and "
               "opposite amounts, so its direction is restored but its line "
               "is displaced.",
    },
    {
        "id": "ks4-wave-front-refraction-h03",
        "subtopic_slug": "wave-front-refraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "P-waves travel faster in denser rock. As a P-wave travels "
                "downwards into the Earth, the rock beneath it becomes "
                "steadily denser. Explain why the wave follows a curved path "
                "that eventually turns back upwards.",
        "options": [
            "The lower part of each wave front is in faster rock and moves "
            "ahead of the upper part, so the front pivots and the path curves "
            "upwards",
            "The wave is reflected off a series of flat boundaries deep "
            "inside the Earth, and these many reflections together add up to "
            "a smooth curve",
            "The frequency of the wave rises as the rock becomes denser, and "
            "a rising frequency will always turn a wave back towards the "
            "surface again",
            "The wave loses energy steadily as it travels deeper, and a wave "
            "that is losing energy always curves back round towards the "
            "surface",
        ],
        "correct_index": 0,
        "why": "Continuous refraction: each wave front keeps pivoting because "
               "its deeper end is always travelling faster than its shallower "
               "end.",
    },
    {
        "id": "ks4-wave-front-refraction-h04",
        "subtopic_slug": "wave-front-refraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "As a wave crosses a boundary, its wave fronts become closer "
                "together in the second medium. A student concludes that the "
                "frequency of the wave has increased. Evaluate this "
                "conclusion.",
        "options": [
            "Correct — closer wave fronts mean more of them pass a fixed "
            "point each second, so the frequency has risen",
            "Correct — the wave has entered a denser medium, and a denser "
            "medium always raises the frequency of a wave",
            "Incorrect — closer wave fronts mean a longer wavelength, and a "
            "longer wavelength means a lower frequency",
            "Incorrect — closer wave fronts mean a shorter wavelength; the "
            "frequency is unchanged and the wave has slowed down",
        ],
        "correct_index": 3,
        "why": "The spacing of wave fronts is the wavelength; with frequency "
               "fixed, a shorter wavelength means the wave has slowed.",
    },

    # ── lenses ──────────────────────────────────────────────────────────
    # TRIPLE ONLY, foundation tier. Every arrangement is stated in words —
    # object distance against focal length — so no question needs a ray
    # diagram to be readable.
    {
        "id": "ks4-lenses-e01",
        "subtopic_slug": "lenses",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to rays of light travelling parallel to "
                "the principal axis when they pass through a converging lens.",
        "options": [
            "They are brought together at the focal point on the far side of "
            "the lens",
            "They spread out as though they had come from a point on the near "
            "side of the lens",
            "They carry straight on without changing direction at all",
            "They are brought together at the centre of the lens itself",
        ],
        "correct_index": 0,
        "why": "A converging lens refracts parallel rays inwards so that they "
               "meet at the focal point.",
    },
    {
        "id": "ks4-lenses-e02",
        "subtopic_slug": "lenses",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the shape of a diverging lens.",
        "options": [
            "Thicker in the middle than at the edges",
            "The same thickness all the way across",
            "Thinner in the middle than at the edges",
            "Flat on one side and curved outwards on the other",
        ],
        "correct_index": 2,
        "why": "A diverging (concave) lens is thinnest at its centre, which "
               "is what makes it spread parallel rays outwards.",
    },
    {
        "id": "ks4-lenses-e03",
        "subtopic_slug": "lenses",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by the focal length of a lens.",
        "options": [
            "The distance from the object to the lens when a sharp image is "
            "formed",
            "The distance from the centre of the lens to the focal point",
            "The distance from the lens to the image, whatever the position "
            "of the object",
            "The greatest distance at which the lens can still form an image",
        ],
        "correct_index": 1,
        "why": "The focal length is measured from the centre of the lens to "
               "the point where parallel rays are brought to a focus.",
    },
    {
        "id": "ks4-lenses-e04",
        "subtopic_slug": "lenses",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what image a converging lens forms when the object is "
                "placed exactly at its focal point.",
        "options": [
            "A real, inverted image the same size as the object",
            "A virtual, upright, magnified image on the same side of the lens "
            "as the object",
            "A real, inverted image at twice the focal length on the far side "
            "of the lens",
            "No image at all, because the refracted rays leave parallel to "
            "one another and never meet",
        ],
        "correct_index": 3,
        "why": "Rays from a point at the focal point are refracted parallel "
               "to one another, so they never cross and no image can form.",
    },
    {
        "id": "ks4-lenses-s01",
        "subtopic_slug": "lenses",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object 4.0 cm tall forms an image 12 cm tall in a "
                "converging lens. Calculate the magnification.",
        "options": [
            "0.33",
            "3.0",
            "3.0 cm",
            "48 cm",
        ],
        "correct_index": 1,
        "why": "Magnification = image height ÷ object height = 12 ÷ 4.0 = "
               "3.0, and because it is a ratio of two lengths it has no unit.",
    },
    {
        "id": "ks4-lenses-s02",
        "subtopic_slug": "lenses",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object is placed 40 cm from a converging lens of focal "
                "length 12 cm. Describe the image that is formed.",
        "options": [
            "Virtual, upright and magnified, on the same side of the lens as "
            "the object",
            "Real, upright and magnified, on the far side of the lens from "
            "the object",
            "Virtual, inverted and diminished, on the same side of the lens "
            "as the object",
            "Real, inverted and diminished, on the far side of the lens from "
            "the object",
        ],
        "correct_index": 3,
        "why": "The object is beyond 2f (2f = 24 cm), which always gives a "
               "real, inverted, diminished image on the other side of the "
               "lens.",
    },
    {
        "id": "ks4-lenses-s03",
        "subtopic_slug": "lenses",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object is placed 5.0 cm from a converging lens of focal "
                "length 8.0 cm. Describe the image that is formed.",
        "options": [
            "Virtual, upright and magnified, on the same side of the lens as "
            "the object",
            "Real, inverted and magnified, on the far side of the lens from "
            "the object",
            "Real, upright and diminished, on the far side of the lens from "
            "the object",
            "No image at all, because the object is nearer to the lens than "
            "the focal point",
        ],
        "correct_index": 0,
        "why": "Inside the focal length a converging lens acts as a "
               "magnifying glass: the rays diverge, so the image is virtual, "
               "upright and magnified.",
    },
    {
        "id": "ks4-lenses-s04",
        "subtopic_slug": "lenses",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the image seen through a magnifying glass cannot "
                "be caught on a screen.",
        "options": [
            "The image is too faint, because a magnifying glass is small and "
            "gathers very little light",
            "The image is inverted, and a screen can only show an image that "
            "is the right way up",
            "The image is virtual — the rays of light only appear to come "
            "from it and never actually meet there",
            "The image is formed inside the glass of the lens itself, where "
            "no screen can possibly be placed",
        ],
        "correct_index": 2,
        "why": "Only a real image, where light rays genuinely cross, can be "
               "projected; a virtual image is where the rays appear to come "
               "from.",
    },
    {
        "id": "ks4-lenses-h01",
        "subtopic_slug": "lenses",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A camera uses a converging lens of focal length 5.0 cm to "
                "photograph a tree 50 m away. Determine roughly where the "
                "image is formed.",
        "options": [
            "50 m from the lens on the far side, because the image distance "
            "always equals the object distance",
            "2.5 cm from the lens on the far side, at half the focal length, "
            "because the object is very far away",
            "About 5.0 cm from the lens on the far side, at the focal point, "
            "because the rays arrive almost parallel",
            "10 cm from the lens on the far side, at twice the focal length, "
            "because the object lies beyond 2f",
        ],
        "correct_index": 2,
        "why": "Light from a very distant object reaches the lens as very "
               "nearly parallel rays, and parallel rays are brought to a "
               "focus at the focal point.",
    },
    {
        "id": "ks4-lenses-h02",
        "subtopic_slug": "lenses",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A projector must throw a large, sharp picture of a small "
                "slide onto a distant screen using a converging lens. "
                "Determine where the slide must be placed relative to the "
                "lens, and explain why.",
        "options": [
            "Between one and two focal lengths from the lens, which gives a "
            "real, inverted, magnified image far beyond 2f",
            "Closer to the lens than one focal length, because that is the "
            "arrangement which magnifies the slide the most",
            "Exactly at the focal point of the lens, because the "
            "magnification produced by a lens is greatest there",
            "Further from the lens than two focal lengths, because only "
            "beyond 2f is the image larger than the slide",
        ],
        "correct_index": 0,
        "why": "An object between f and 2f gives a real, inverted, magnified "
               "image beyond 2f — the only arrangement that can be projected "
               "and enlarged.",
    },
    {
        "id": "ks4-lenses-h03",
        "subtopic_slug": "lenses",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object 2.0 cm tall stands 15 cm from a converging lens, "
                "and its image is formed 45 cm from the lens on the other "
                "side. Calculate the height of the image.",
        "options": [
            "0.67 cm",
            "3.0 cm",
            "30 cm",
            "6.0 cm",
        ],
        "correct_index": 3,
        "why": "Magnification = image distance ÷ object distance = 45 ÷ 15 = "
               "3.0, so image height = 3.0 × 2.0 = 6.0 cm.",
    },
    {
        "id": "ks4-lenses-h04",
        "subtopic_slug": "lenses",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person is long-sighted: their eye lens is too weak, so "
                "light from a nearby book would be brought to a focus behind "
                "the retina. Explain how a converging lens in their glasses "
                "corrects this.",
        "options": [
            "It spreads the light out before it enters the eye, so the focus "
            "moves further back and lands on the retina",
            "It brings the light together before it enters the eye, so the "
            "focus moves forward onto the retina",
            "It makes the image on the retina larger, so the person can read "
            "the book even though the image is not sharp",
            "It changes the shape of the eye lens itself, so the ciliary "
            "muscles no longer have to adjust it at all",
        ],
        "correct_index": 1,
        "why": "The spectacle lens starts the converging early, so the eye's "
               "own weak lens has less bending left to do and the focus falls "
               "on the retina.",
    },

    # ── infrared-black-bodies ───────────────────────────────────────────
    # TRIPLE ONLY, foundation tier.
    {
        "id": "ks4-infrared-black-bodies-e01",
        "subtopic_slug": "infrared-black-bodies",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which objects emit infrared radiation.",
        "options": [
            "Only objects that are hotter than their surroundings",
            "Only objects hot enough to glow visibly",
            "All objects at a temperature above absolute zero",
            "Only objects with a dark, matt surface",
        ],
        "correct_index": 2,
        "why": "Every object above absolute zero emits infrared continuously "
               "— a cold object simply emits less of it.",
    },
    {
        "id": "ks4-infrared-black-bodies-e02",
        "subtopic_slug": "infrared-black-bodies",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which type of surface is the best reflector of "
                "infrared radiation.",
        "options": [
            "Matt and black",
            "Matt and dark grey",
            "Matt and white",
            "Shiny and silver",
        ],
        "correct_index": 3,
        "why": "A shiny silver surface reflects most of the infrared reaching "
               "it, which is why it is also a poor absorber and a poor "
               "emitter.",
    },
    {
        "id": "ks4-infrared-black-bodies-e03",
        "subtopic_slug": "infrared-black-bodies",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the radiation emitted by a perfect black body "
                "depends on.",
        "options": [
            "Its temperature alone",
            "The material it is made from alone",
            "Its temperature and the material it is made from together",
            "The wavelength of the radiation that last fell on it",
        ],
        "correct_index": 0,
        "why": "A black body's emission depends only on its temperature — two "
               "black bodies at the same temperature emit identically, "
               "whatever they are made of.",
    },
    {
        "id": "ks4-infrared-black-bodies-e04",
        "subtopic_slug": "infrared-black-bodies",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object absorbs energy by radiation at exactly the same "
                "rate as it emits it. State what happens to its temperature.",
        "options": [
            "It rises steadily",
            "It stays constant",
            "It falls steadily",
            "It rises at first and then falls",
        ],
        "correct_index": 1,
        "why": "When the rate of absorption equals the rate of emission the "
               "object is in thermal equilibrium, so its temperature does not "
               "change.",
    },
    {
        "id": "ks4-infrared-black-bodies-s01",
        "subtopic_slug": "infrared-black-bodies",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A blue-white star and a red star are compared. Explain which "
                "has the higher surface temperature.",
        "options": [
            "The red star, because red light has the longer wavelength and "
            "long wavelengths carry more energy",
            "The red star, because red is the colour we normally associate "
            "with the greatest heat",
            "Neither — the colour of a star depends on its chemical "
            "composition and not on its temperature",
            "The blue-white star, because a hotter body emits its peak "
            "radiation at a shorter wavelength",
        ],
        "correct_index": 3,
        "why": "The hotter a body is, the shorter the wavelength at which it "
               "emits most strongly, so blue-white stars are hotter than red "
               "ones.",
    },
    {
        "id": "ks4-infrared-black-bodies-s02",
        "subtopic_slug": "infrared-black-bodies",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the pipes of a solar water heater are painted "
                "matt black.",
        "options": [
            "Matt black surfaces reflect infrared back into the water, so the "
            "energy is kept inside the pipe",
            "Matt black surfaces are the best absorbers of the radiation "
            "arriving from the Sun",
            "Matt black surfaces are the best insulators, so very little "
            "energy can escape from the pipe",
            "Matt black surfaces conduct thermal energy into the water faster "
            "than any other colour does",
        ],
        "correct_index": 1,
        "why": "A dark matt surface absorbs the greatest fraction of the "
               "incoming solar radiation, so more energy is transferred to "
               "the water.",
    },
    {
        "id": "ks4-infrared-black-bodies-s03",
        "subtopic_slug": "infrared-black-bodies",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says: 'A perfect black body must be a very poor "
                "emitter, because it soaks up all the radiation and lets none "
                "back out.' Explain the error.",
        "options": [
            "There is no error — a perfect absorber traps the radiation "
            "inside it and so emits almost none",
            "The error is that no real object absorbs every last bit of the "
            "radiation falling on it, so a perfect black body cannot "
            "actually exist",
            "A perfect absorber is also a perfect emitter — a black body "
            "emits the maximum possible radiation for its temperature",
            "The error is that a black body absorbs only infrared, and it "
            "re-emits all the visible light it receives",
        ],
        "correct_index": 2,
        "why": "Being a perfect absorber and a perfect emitter go together: "
               "at any given temperature, a black body emits more than any "
               "other object.",
    },
    {
        "id": "ks4-infrared-black-bodies-s04",
        "subtopic_slug": "infrared-black-bodies",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An object is left in a room and its temperature falls "
                "steadily. Compare the rate at which it emits radiation with "
                "the rate at which it absorbs radiation.",
        "options": [
            "It emits radiation faster than it absorbs it",
            "It absorbs radiation faster than it emits it",
            "It emits and absorbs radiation at exactly the same rate",
            "It emits radiation but does not absorb any at all",
        ],
        "correct_index": 0,
        "why": "A falling temperature means the object is losing energy, so "
               "its rate of emission must exceed its rate of absorption.",
    },
    {
        "id": "ks4-infrared-black-bodies-h01",
        "subtopic_slug": "infrared-black-bodies",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical metal cans are filled with water at 80 °C. One "
                "is painted matt black and the other is polished silver. "
                "Predict which cools faster and explain why.",
        "options": [
            "The matt black can, because a matt black surface is a better "
            "emitter of infrared radiation",
            "The polished silver can, because a shiny surface radiates energy "
            "away more readily than a dull one",
            "Both cool at the same rate, because they hold the same mass of "
            "water at the same starting temperature",
            "The matt black can, because a black surface conducts thermal "
            "energy through the metal more quickly",
        ],
        "correct_index": 0,
        "why": "The surface that absorbs best also emits best, so the matt "
               "black can radiates energy away fastest.",
    },
    {
        "id": "ks4-infrared-black-bodies-h02",
        "subtopic_slug": "infrared-black-bodies",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Sun's surface is at about 5500 °C and the Earth's is at "
                "about 15 °C. Explain why the Sun's radiation is mostly "
                "visible light while the Earth's is mostly infrared.",
        "options": [
            "The Sun is far larger than the Earth, and a larger body always "
            "emits at shorter wavelengths",
            "The Sun's radiation has travelled a very long way and has been "
            "stretched to shorter wavelengths on the journey",
            "The peak wavelength a body emits depends on its temperature — "
            "the hot Sun peaks in the visible, the far cooler Earth in the "
            "infrared",
            "The Earth's atmosphere absorbs all of the visible light that the "
            "Earth emits, so that only infrared radiation is left able to "
            "escape to space",
        ],
        "correct_index": 2,
        "why": "A black body's emission spectrum depends only on its "
               "temperature, and a hotter body peaks at a shorter wavelength.",
    },
    {
        "id": "ks4-infrared-black-bodies-h03",
        "subtopic_slug": "infrared-black-bodies",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The James Webb Space Telescope observes in the infrared "
                "rather than in visible light. Suggest why this makes it "
                "well suited to studying cold clouds of dust between the "
                "stars.",
        "options": [
            "Cold dust clouds are transparent to infrared, so the telescope "
            "can see straight through them to the stars beyond",
            "Cold objects emit most of their radiation in the infrared, so "
            "they show up clearly there but are nearly invisible in visible "
            "light",
            "Infrared travels faster than visible light through space, so it "
            "arrives from very distant clouds far sooner",
            "Cold dust clouds reflect infrared very strongly, and radiation "
            "that has been reflected is always far easier to detect than "
            "radiation that has been emitted",
        ],
        "correct_index": 1,
        "why": "A cold body's peak emission lies in the infrared, so an "
               "infrared telescope detects the radiation the dust itself "
               "gives out.",
    },
    {
        "id": "ks4-infrared-black-bodies-h04",
        "subtopic_slug": "infrared-black-bodies",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hollow box with a very small hole in one side behaves "
                "almost exactly like a perfect black body. Explain why "
                "radiation entering the hole almost never comes back out.",
        "options": [
            "The walls of the box are made of a material that is unable to "
            "reflect any radiation at all",
            "The hole is so small that any radiation which enters it is "
            "immediately turned into thermal energy at the rim of the hole "
            "itself",
            "Radiation slows down once inside the box and no longer has the "
            "energy it would need to escape",
            "The radiation is reflected many times inside the box and a "
            "little is absorbed each time, so almost none finds the hole "
            "again",
        ],
        "correct_index": 3,
        "why": "Repeated reflection with a little absorption at every bounce "
               "means effectively all the radiation is absorbed, which is "
               "exactly what a black body does.",
    },

    # ── radiation-balance-temperature ───────────────────────────────────
    # TRIPLE ONLY, higher tier.
    {
        "id": "ks4-radiation-balance-temperature-e01",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Most of the radiation the Earth receives from the Sun "
                "arrives as visible light. State what happens to that "
                "radiation when it reaches the Earth's surface.",
        "options": [
            "It is reflected straight back out to space without warming the "
            "surface at all",
            "It is absorbed by the surface, which warms and then emits "
            "infrared radiation",
            "It passes through the surface and is absorbed by the rock far "
            "below it",
            "It is absorbed by the greenhouse gases before it can reach the "
            "surface at all",
        ],
        "correct_index": 1,
        "why": "The surface absorbs the Sun's visible radiation and warms; "
               "being far cooler than the Sun, it then re-radiates that "
               "energy as infrared.",
    },
    {
        "id": "ks4-radiation-balance-temperature-e02",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the main type of radiation the Earth emits to space.",
        "options": [
            "Infrared",
            "Visible light",
            "Ultraviolet",
            "Microwaves",
        ],
        "correct_index": 0,
        "why": "The Earth is far cooler than the Sun, so it radiates at the "
               "much longer wavelengths of the infrared.",
    },
    {
        "id": "ks4-radiation-balance-temperature-e03",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name two greenhouse gases.",
        "options": [
            "Nitrogen and oxygen",
            "Oxygen and argon",
            "Nitrogen and helium",
            "Carbon dioxide and methane",
        ],
        "correct_index": 3,
        "why": "Carbon dioxide and methane both absorb infrared strongly; "
               "the nitrogen and oxygen that make up most of the air do not.",
    },
    {
        "id": "ks4-radiation-balance-temperature-e04",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by the albedo of a surface.",
        "options": [
            "The rate at which the surface emits infrared radiation to space",
            "The temperature the surface reaches when it stands in direct "
            "sunlight",
            "The proportion of the radiation falling on the surface that it "
            "reflects",
            "The proportion of the radiation falling on the surface that it "
            "absorbs",
        ],
        "correct_index": 2,
        "why": "Albedo is reflectivity — ice has a high albedo, dark ocean a "
               "low one.",
    },
    {
        "id": "ks4-radiation-balance-temperature-s01",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why raising the concentration of carbon dioxide in "
                "the atmosphere raises the Earth's average temperature.",
        "options": [
            "More of the infrared leaving the Earth's surface is absorbed and "
            "re-emitted back downwards, so less energy escapes to space",
            "More of the Sun's visible light is absorbed by the atmosphere "
            "before it reaches the ground, so the air itself becomes warmer",
            "Carbon dioxide reflects the infrared leaving the Earth straight "
            "back down again without ever absorbing any of it",
            "Carbon dioxide releases stored chemical energy into the "
            "atmosphere as it builds up, and this energy warms the air",
        ],
        "correct_index": 0,
        "why": "Greenhouse gases absorb outgoing infrared and re-emit it in "
               "all directions, so some returns to the surface and less "
               "escapes.",
    },
    {
        "id": "ks4-radiation-balance-temperature-s02",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Large areas of Arctic sea ice melt and are replaced by open "
                "ocean. Explain the effect on the Earth's radiation balance.",
        "options": [
            "The ocean reflects more radiation than the ice did, so less is "
            "absorbed and the Earth cools",
            "There is no effect, because ice and liquid water are made of "
            "exactly the same substance",
            "The ocean has a lower albedo than ice, so more solar radiation "
            "is absorbed and the warming increases",
            "The ocean emits far more infrared than the ice did, so more "
            "energy escapes and the Earth cools",
        ],
        "correct_index": 2,
        "why": "Dark ocean reflects far less sunlight than bright ice, so "
               "more solar energy is absorbed — warming that causes more "
               "melting.",
    },
    {
        "id": "ks4-radiation-balance-temperature-s03",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the natural greenhouse effect with the enhanced "
                "greenhouse effect.",
        "options": [
            "The natural effect warms the Earth, while the enhanced effect "
            "cools it by reflecting sunlight back out to space",
            "The natural effect is caused by water vapour only, while the "
            "enhanced effect is caused by carbon dioxide only",
            "The natural effect is harmful, and the enhanced effect corrects "
            "it by restoring the balance of radiation",
            "The natural effect keeps the Earth warm enough for life; the "
            "enhanced effect is the extra warming from human emissions",
        ],
        "correct_index": 3,
        "why": "The natural greenhouse effect is necessary and beneficial; it "
               "is the extra warming added by human emissions that is the "
               "problem.",
    },
    {
        "id": "ks4-radiation-balance-temperature-s04",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Venus is almost the same size as the Earth and receives "
                "about twice as much solar radiation, yet its surface is at "
                "about 465 °C. Explain why it is so much hotter than the "
                "extra sunlight alone would suggest.",
        "options": [
            "Venus rotates very slowly, so one side is heated continuously "
            "and never gets a chance to cool down",
            "Venus has a thick carbon dioxide atmosphere, which absorbs the "
            "infrared it emits and gives an enormous greenhouse effect",
            "Venus has a very low albedo, so it reflects almost none of the "
            "sunlight that reaches it from the Sun",
            "Venus is very much closer to the Sun than the Earth is, and that "
            "difference alone accounts for the temperature",
        ],
        "correct_index": 1,
        "why": "Its dense carbon dioxide atmosphere traps outgoing infrared "
               "extremely effectively, so the balance is only reached at a "
               "very high temperature.",
    },
    {
        "id": "ks4-radiation-balance-temperature-h01",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "The Sun's output increases slightly and then stays at the "
                "new, higher level. Predict what happens to the Earth's "
                "average temperature over time.",
        "options": [
            "It rises without limit, because the Earth is now absorbing more "
            "energy than it was before",
            "It stays exactly the same, because the Earth's rate of emission "
            "is fixed by the greenhouse gases in its atmosphere",
            "It falls, because a warmer Earth emits more radiation and so "
            "loses energy faster than it gains it",
            "It rises until the Earth is hot enough to emit at the new, "
            "higher rate, and then settles at a new constant value",
        ],
        "correct_index": 3,
        "why": "A warmer Earth emits more, so the temperature climbs only "
               "until emission has risen to match the new absorption and "
               "balance is restored.",
    },
    {
        "id": "ks4-radiation-balance-temperature-h02",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A large volcanic eruption throws fine ash and droplets of "
                "sulfur dioxide high into the atmosphere. Predict the "
                "short-term effect on the Earth's average temperature and "
                "explain why.",
        "options": [
            "A rise, because the carbon dioxide from the eruption immediately "
            "strengthens the greenhouse effect more than anything else it "
            "does",
            "A fall, because the ash and droplets reflect some of the "
            "incoming solar radiation back to space, so less is absorbed at "
            "the surface",
            "A fall, because the ash absorbs the infrared the Earth emits and "
            "carries that energy away with it as the ash settles out",
            "No change, because the atmosphere always returns to exactly the "
            "same radiation balance whatever is added to it",
        ],
        "correct_index": 1,
        "why": "The ash and droplets raise the Earth's albedo for a few "
               "years, so less solar radiation is absorbed and the surface "
               "cools.",
    },
    {
        "id": "ks4-radiation-balance-temperature-h03",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "The Moon is the same distance from the Sun as the Earth, but "
                "its surface swings between about 120 °C by day and −170 °C "
                "by night. Explain why the Earth's surface temperature is far "
                "steadier.",
        "options": [
            "The Earth has an atmosphere that absorbs and re-emits infrared, "
            "so energy is held back and redistributed instead of going "
            "straight to space",
            "The Earth is much larger than the Moon, and a larger body always "
            "emits its radiation more slowly than a smaller one does",
            "The Earth spins far more slowly on its axis than the Moon does, "
            "so each part of its surface has much longer in which to settle "
            "at a steady temperature",
            "The Earth's surface has a much higher albedo than the Moon's, so "
            "it absorbs almost none of the radiation arriving from the Sun",
        ],
        "correct_index": 0,
        "why": "Without an atmosphere the Moon's surface radiates its energy "
               "directly to space at night; the Earth's atmosphere returns "
               "much of that infrared and evens the temperature out.",
    },
    {
        "id": "ks4-radiation-balance-temperature-h04",
        "subtopic_slug": "radiation-balance-temperature",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "The Earth is currently absorbing slightly more energy from "
                "the Sun than it emits to space. Explain what this tells us "
                "about the Earth's temperature, and what happens to the "
                "imbalance as the Earth warms.",
        "options": [
            "The temperature is constant, and the imbalance will stay the "
            "same for as long as greenhouse gas levels stay the same",
            "The temperature is falling, and the imbalance will grow larger "
            "as the Earth continues to cool down",
            "The temperature is rising, and the imbalance shrinks because a "
            "warming Earth emits infrared more rapidly",
            "The temperature is rising, and the imbalance grows larger "
            "because a warmer Earth always absorbs more than it emits",
        ],
        "correct_index": 2,
        "why": "Absorbing more than it emits means the Earth is warming, and "
               "a warmer Earth emits more — which closes the gap towards a "
               "new balance.",
    },
]
