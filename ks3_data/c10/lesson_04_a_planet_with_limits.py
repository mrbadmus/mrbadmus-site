"""C10 L4 — A planet with limits: resources and recycling (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c10/c10-04-a-planet-with-limits.dc.html`, and her
author's notes `NOTES-C10.md`, which cover this lesson and no other in the
unit.

── ⭐ SIX RAIL STOPS, AND `#s-words` IS ONE OF THEM ─────────────────────

Design's own `RAIL` constant draws SIX — `s-hook s-loop s-stock s-words
s-think s-ladder` — where every other page in C10 draws five. The extra one is
the VOCABULARY block, which on this page is a rail stop in its own right
(`DONE('s-words')` is `s.flipped.length >= 5`). The engine's keyword block has
carried an anchor and a `data-stage-done` hook since MRB-272, so this needs no
new machinery; it needs the rail entry, which is here.

MRB-249's floor is four LIVE stops and the rule is to match Design stop for
stop. Six it is, and `docs/ks3/rail-manifest.md` records the same six.

── ⚖️ THE DESIGN RULING THIS LESSON RESTS ON ────────────────────────────

NOTES-C10 records two candidate benches and takes the second: a finite-stock
DEPLETION CLOCK, or a materials-flow LOOP with recycling rates as the dials.
The clock was rejected because it makes "years left" the interesting number,
and years-left is the one figure in this topic that is genuinely soft — a
reserve is an economic category, so the number moves without the planet
changing. The loop makes the MATERIAL the variable, which is where the
chemistry is: what comes back depends on whether melting destroys the
structure, not on how carefully anyone sorts a bin.

That ruling is why the going-further layer leads with the reserve, and why
`reserve` is a vocabulary card rather than a headline number anywhere.

── SCIENCE FLAGS, AND WHAT WAS ACCEPTED ────────────────────────────────

NOTES-C10 flags three things for review. All three are ACCEPTED as drawn, and
the reasons are recorded here because the flags are the author asking for a
decision rather than reporting a defect.

⚑ Flag 1 — THE YIELDS ARE TEACHING VALUES, AND THE ORDERING IS THE CLAIM.
0.95 / 0.92 / 0.90 / 0.50 / 0.02 are defensible order-of-magnitude figures,
not audited industry numbers, and the notes say so. ACCEPTED, and the claim is
made checkable rather than left as prose: the lesson authors `order_claim`,
and `ks3_art/c10.py` refuses to build if the five multipliers at the highest
collection rate no longer produce that order. A yield edited without thinking
now fails the build instead of quietly re-teaching the lesson.

⚑ Flag 2 — GLASS AT 27% IS THE FIGURE MOST LIKELY TO BE CHALLENGED, and it is
the point of including glass. ACCEPTED as a single number rather than a range.
A student who has just met aluminium at 95% needs a case that contradicts the
rule they have started to form, and a range ("15–40%") lets them keep the rule
and file the case as noise. The energy figures behind it — 15 MJ/kg new, 11
MJ/kg recycled — are on the panel as numbers, so the 27% is derived in front
of them and not asserted. If review wants a range, the row is one edit and
nothing else in the lesson moves.

⚑ Flag 3 — "ABOUT THREE QUARTERS OF ALL ALUMINIUM EVER SMELTED IS STILL IN
USE" is a widely published industry figure. ACCEPTED, and it is stated as
approximate in the hook, which is where the notes put it. The hook's reveal
does not rest on the precise fraction: the discriminating point is that a
material can be almost perfectly recyclable and the world can still be mining
more of it, which is true at 60% and at 80%.

⚑ Flag 4 — THE ALUMINIUM ENERGY SAVING IS QUOTED TWICE AND MUST AGREE.
`stock-limits` says recycled aluminium takes "about a twentieth of the
energy"; the bench derives 95% from 45 and 2.3 MJ/kg. A twentieth is 95%, so
the two agree — which is the only reason the prose form is allowed to stand
beside the derived one. MRB-225: nothing in the lesson body is retracted by a
later sentence in it.

── ⚖️ MRB-225 · TRUE, NOT FAMOUS ───────────────────────────────────────

Four things this lesson refuses to say the famous way:

1. **Recycling does not make a finite stock infinite.** The loop leaks every
   pass. The key fact says so, `EARTH-11` says so, and the bench proves it
   before either is read — a student who has run aluminium at nine-in-ten has
   already seen 6.90×, not ∞.
2. **Reduce and reuse come before recycle, in that order**, because they cut
   extraction and recycling only slows it. Stated in the `#s-think` reveal.
3. **A reserve is an economic category.** "Years left" moves when the price or
   the technology moves. The real limit arrives as rising energy cost long
   before anything runs out.
4. **The crisp packet is a trade-off, not a mistake.** The laminate keeps food
   fresh on very little material. Stated in going-further so the lesson does
   not end on "packaging is bad", which is a moral position rather than a
   scientific one and is not what `KS3.C.EA.04` asks for.

── ⚑ MRB-278 · ANSWER POSITION ─────────────────────────────────────────

Design draws both marked rungs with the correct option at index 0. Rung 2's
is moved to index 2. **Only the order moves; no option text is edited**, which
is the same treatment C9 gave its eight marked rungs.

⚑ MRB-177 · THE DISTRACTORS ARE LENGTHENED, NOT THE ANSWER SHORTENED. Design's
rung-2 answer is 92 characters and her three distractors are 49, 26 and 25 —
a fix length tell at the distractor, which is exactly what MRB-177 forbids.
Each distractor is rewritten as a WRONG RULE at the answer's own length: mass
per item decides it, care in collection decides it, scrap value decides it.
The correct option is untouched. The same repair is applied to rung 1.

── ⊖ NO `safety_note`, DELIBERATELY ────────────────────────────────────

Nothing on this page is a method or a demonstration. The loop bench is an
arithmetic model of a material flow and the stock shelf is a reference; there
is no apparatus, no substance and nothing to run in a room. C9's lessons carry
a safety note because their benches simulate real demonstrations. Recorded
rather than assumed, because the absence of a note is indistinguishable from
an oversight unless somebody writes down that it was checked.

── SAFEGUARDING ────────────────────────────────────────────────────────

The lesson touches consumption and waste, which are areas where a student's
home circumstances can be read as a moral failing. Nothing on the page asks
what a student's family buys, throws away or recycles, and the going-further
layer explicitly names the crisp packet as an engineering trade-off rather
than as somebody's bad choice. Design carried no Childline block and none is
added.
"""

LESSON = {
    "slug":  "a-planet-with-limits",
    "title": "A planet with limits: resources and recycling",
    "discipline": "chemistry",
    "unit": "The Earth and its atmosphere",
    "family": "SYSTEM",

    "covers": ["KS3.C.EA.04"],
    "touches": ["KS3.C.MATS.02", "KS3.C.MATS.03"],
    "beyond_statutory": False,
    "threads": [{"id": "earth-and-universe", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["the-rock-cycle"],
    "assumes": [],
    "references": ["getting-metals-out-of-rocks",
                   "ceramics-polymers-and-composites"],
    "ks4_links": [],

    "meta_description": "Everything made on Earth came out of the crust, "
                        "and only some of it comes back. Run the loop and "
                        "see how much — and why it depends on the material.",

    "big_question": "Everything manufactured on Earth came out of the crust, "
                    "and the crust is not being topped up. Recycling sends "
                    "some of it round again — but only some, and how much "
                    "depends on the material, not on how carefully you sort "
                    "it.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Still in use",   "done_when": "committed"},
        {"anchor": "s-loop",   "short": "LOOP",
         "label": "Run the loop",
         "done_when": "three_materials_opened_and_rate_changed"},
        {"anchor": "s-stock",  "short": "STOCK",
         "label": "Five limits",    "done_when": "three_of_five_opened"},
        # ⭐ The vocabulary block is a RAIL STOP on this page and on no other.
        # Design's `DONE('s-words')` is `s.flipped.length >= 5`, which is what
        # the engine's card grid already ticks on.
        {"anchor": "s-words",  "short": "WORDS",
         "label": "Five words",     "done_when": "all_five_cards_turned"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Recycle it all", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "About three quarters of all the aluminium ever smelted is "
                 "still in use today.",
        "prompt": "Smelting began in the 1880s. Roughly 75% of every tonne "
                  "produced since is still in a window frame, an engine "
                  "block, a can or a plane — not in a hole in the ground. "
                  "Almost no other material comes close.",
        "commit": "What does that tell you?",
        "options": [
            "Aluminium is not really a limited resource",
            "It reuses almost without loss, so the stock in use keeps "
            "building — but new cans still start as ore",
            "We have stopped mining aluminium",
            "Aluminium never wears out, so recycling it is unnecessary",
        ],
        "reveal": "Aluminium can be melted and cast again almost without "
                  "loss, so the amount in circulation keeps building up. But "
                  "the stock in use is still growing, which means new metal "
                  "is still being dug up every year — recycling is not "
                  "keeping pace with demand. <strong>A material can be almost "
                  "perfectly recyclable and the world can still be mining "
                  "more of it.</strong>",
    },

    "misconceptions": [
        {"id": "EARTH-11",
         "statement": "If we recycled everything, we would never run out of "
                      "anything.",
         "elicited_by": "think-commit-recycling",
         "confronted_by": "think-reveal-recycling"},
        # ⚑ The bench elicits it — a student who has just watched aluminium
        # reach 6.90× arrives at the packet expecting the same — and the
        # bench's own verdict confronts it, in the one place on the page
        # where collection is held equal and the material is the only thing
        # that changed.
        {"id": "EARTH-12",
         "statement": "How much comes back depends on how carefully people "
                      "sort their bins.",
         "elicited_by": "loop-bench",
         "confronted_by": "loop-bench"},
        # ⚑ NO `elicited_by`, DELIBERATELY (audit law 15). Nothing on this
        # page asks the student to commit to the belief that a reserve is a
        # measured amount of rock; the shelf and the going-further layer
        # simply say what a reserve is. Inventing an anchor to fill the
        # column would be the dishonest version, and MRB-248 makes absence
        # legal precisely so it need not be invented.
        {"id": "EARTH-13",
         "statement": "“Years left” is a measured fact about how "
                      "much is in the ground.",
         "confronted_by": "s-stock"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Ores, crude oil and phosphate rock took tens of millions of "
                 "years to concentrate, and we are using them in centuries. "
                 "On any human timescale the supply is <strong>finite</"
                 "strong>: extraction is a one-way trip out of the crust."},
        {"type": "explainer",
         "text": "Recycling is the only thing that sends any of it back. The "
                 "question this lesson answers is how much comes back — and "
                 "that turns out to be a property of the material."},

        # ── #s-loop — THE BENCH. Ink-dark (`ks3-block ks3-dark`), so the
        # unit's `_INSTRUMENT_SEGMENTS` map sends it to the `practical` shell;
        # the ruling and the two visible deltas are in `ks3_art/c10.py`.
        #
        # ⚠️ NOT ONE NUMBER BELOW IS A READOUT. Every mass, percentage and
        # multiplier on this bench is computed in the renderer from
        # `recovery`, `rate`, `e_primary` and `e_recycled`. The payload states
        # the inputs and the sentences; it never states an answer.
        {"type": "material-loop", "id": "loop-bench", "anchor": "s-loop",
         "eyebrow": "The bench · run the loop",
         "heading": "Start with 1000 kg. See how far it goes round.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} materials opened",
                          "start": 1, "total": 5},
         "rate_hint": "Change the collection rate to finish this bench.",

         "start_mass": 1000,
         "mass_unit": "kg",
         "energy_unit": "MJ/kg",
         "passes": 6,
         "pass_label": "Use {n}",
         "start_material": "al",
         "start_rate": "r90",
         "materials_to_tick": 3,

         "materials_label": "Pick a material",
         "rates_label": "How much gets collected",

         # `recovery` is the fraction of COLLECTED material that comes back
         # usable at the same grade — NOTES-C10 calls it "yield". Energy
         # figures are order-of-magnitude teaching values.
         "materials": [
             # ⚠️ ALUMINIUM'S ENERGY FIGURES ARE WHOLE-PROCESS, NOT
             # ELECTROLYSIS ALONE. They used to read 45 / 2.3 (C10-07, chem
             # audit 25 Aug 2026), which put new aluminium BELOW PET's 85 on
             # a bench captioned "what it costs to make the material the
             # first time" — while the bauxite panel three taps away calls
             # aluminium one of the most energy-hungry industrial processes
             # there is. Published whole-process primary aluminium is
             # ~150–200 MJ/kg. 170 / 8.5 restores the real ordering
             # (Al > film > PET > steel > glass) and keeps every ruled
             # sentence true: 8.5/170 is exactly a twentieth, so the saving
             # still prints 95%.
             {"id": "al", "label": "Aluminium can", "name": "Aluminium can",
              "recovery": 0.95, "e_primary": 170, "e_recycled": 8.5,
              "what": "Melts and casts again with almost nothing lost. The "
                      "metal does not care how many times it has been "
                      "round."},
             {"id": "fe", "label": "Steel can", "name": "Steel can",
              "recovery": 0.92, "e_primary": 25, "e_recycled": 7.5,
              "what": "Magnetic, so it sorts itself out of mixed waste. "
                      "Small amounts of other metals build up, which limits "
                      "what the steel can be used for."},
             {"id": "gl", "label": "Glass bottle", "name": "Glass bottle",
              "recovery": 0.90, "e_primary": 15, "e_recycled": 11,
              "what": "Endlessly remeltable, but the melting is most of the "
                      "energy — so recycling glass saves far less energy "
                      "than people expect."},
             {"id": "pet", "label": "PET bottle", "name": "PET bottle",
              "recovery": 0.50, "e_primary": 85, "e_recycled": 17,
              "what": "The polymer chains shorten every time it is melted. "
                      "Half of what comes back is only fit for something "
                      "less demanding than a bottle."},
             {"id": "film", "label": "Crisp packet",
              "name": "Crisp packet (metallised film)",
              "recovery": 0.02, "e_primary": 90, "e_recycled": 90,
              "what": "Plastic laminated to a few microns of aluminium. No "
                      "process separates the two layers economically, so "
                      "almost none of it comes back as either material."},
         ],

         # `label` is the button; `phrase` is what a verdict sentence calls
         # the same setting mid-sentence. One string cannot do both jobs —
         # "Even at 9 in 10" and "Even at nine in ten" are not the same
         # register.
         "rates": [
             {"id": "r0",  "label": "None collected", "phrase": "nothing",
              "rate": 0},
             {"id": "r25", "label": "1 in 4", "phrase": "one in four",
              "rate": 0.25},
             {"id": "r50", "label": "Half", "phrase": "half",
              "rate": 0.5},
             {"id": "r90", "label": "9 in 10", "phrase": "nine in ten",
              "rate": 0.9},
         ],

         "stat_lifetimes": {
             "label": "Lifetimes per kg of ore",
             "note": "Adding up every pass through the loop.",
             "note_zero": "Used once, then gone."},
         "stat_primary": {
             "label": "Energy, new from ore",
             "note": "What it costs to make the material the first time."},
         "stat_recycled": {
             "label": "Energy, from recycled",
             "note": "{saving}% less than new.",
             "note_none": "No recycling route, so no saving."},

         # Six branches, each saying something the other five cannot. The
         # numbers arrive at render; the sentences are authored once.
         "verdicts": {
             "none":
                 "Nothing comes back. Every kilogram used is a kilogram out "
                 "of the ground, used once and finished — whatever the "
                 "material is capable of.",
             "floor":
                 "Collection is not the problem here — the material is. Even "
                 "collecting {rate}, a kilogram of ore does the work of only "
                 "{mult} kilograms, and the second bar has already all but "
                 "vanished.",
             # ⚑ THE SUPERLATIVE ATTACHES TO THE MULTIPLIER, NOT TO THE
             # ENERGY. Design's sentence reads "…costs {saving}% less energy
             # than making it new. This is recycling working about as well as
             # it ever does." — and this branch is reached by GLASS at nine in
             # ten, where the saving is 27%. Written her way the page praises
             # 27% as the best recycling ever gets, in the one lesson whose
             # whole point is that glass contradicts the 95% rule a student
             # has just formed on aluminium. That is a sentence retracted by
             # the panel directly above it (MRB-225), so the clause order is
             # changed and nothing else: the loop running well is a claim
             # about the multiplier, and the energy saving is stated plainly
             # beside it.
             "strong":
                 "A kilogram of ore now does the work of about {mult_round} "
                 "kilograms — this loop is running about as well as a loop "
                 "ever does — and each pass costs {saving}% less energy than "
                 "making it new.",
             "real":
                 "A kilogram of ore does the work of about {mult_round} "
                 "kilograms — a real gain, and still a leaking loop. Look at "
                 "how fast the bars shrink.",
             "degraded":
                 "Even collecting {rate}, the multiplier is only {mult}. "
                 "What comes back is degraded, so most of it cannot do the "
                 "original job again.",
             "poor_collection":
                 "The multiplier is {mult}. The material would go round "
                 "well; not enough of it is being collected to find out.",
         },

         # ⚖️ THE ORDERING IS THE CLAIM. Checked against the multipliers the
         # figures above actually produce at the highest collection rate.
         "order_claim": ["al", "fe", "gl", "pet", "film"]},

        # ── #s-stock — the reference shelf. Light `ks3-block` → `check`.
        # `EARTH-13` is confronted here, on the bauxite and iron rows, which
        # are the two that say the limit is energy and grade rather than a
        # measured amount of rock.
        {"type": "stock-limits", "id": "stock-shelf", "anchor": "s-stock",
         "eyebrow": "Reference · five things we take out of the ground",
         "heading": "Tap one. Each has a different kind of limit.",
         "prompt": "Not one of these runs out in the same way.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} opened",
                          "start": 1, "total": 5},
         "start_entry": "bx",
         "entries_to_tick": 3,
         "limit_label": "The limit:",
         "recycle_label": "Does recycling help?",
         "entries": [
             {"id": "bx", "label": "Bauxite",
              "name": "Bauxite — aluminium ore",
              "limit_kind": "energy",
              "use": "The only ore aluminium is extracted from in quantity. "
                     "Smelting it needs electricity on a scale that decides "
                     "where smelters get built.",
              "limit": "Plenty in the ground for now, but extraction is one "
                       "of the most energy-hungry industrial processes there "
                       "is, so the real limit is energy rather than rock.",
              "recycle": "Enormously. Recycled aluminium takes about a "
                         "twentieth of the energy, and the metal comes back "
                         "as good as new."},
             {"id": "fe", "label": "Iron ore", "name": "Iron ore",
              "limit_kind": "grade",
              "use": "Steel — buildings, cars, ships, tools, tins. By mass, "
                     "the most used metal on the planet by a wide margin.",
              "limit": "The most abundant of the useful ores, but the "
                       "high-grade deposits get taken first, and lower "
                       "grades need more digging and more energy per tonne "
                       "of iron.",
              "recycle": "Well. Steel is easy to separate magnetically, and "
                         "a large share of new steel is already made from "
                         "scrap."},
             {"id": "oil", "label": "Crude oil", "name": "Crude oil",
              "limit_kind": "burnt-out-of-the-loop",
              "use": "Fuels, and the feedstock for almost every plastic, "
                     "dye, solvent and synthetic fibre.",
              "limit": "Formed over tens of millions of years from buried "
                       "marine organisms, and used in a couple of centuries. "
                       "Burning it also puts its carbon into the atmosphere.",
              "recycle": "Not once it is burnt — that carbon is gone from "
                         "the loop entirely. Plastics made from it can be "
                         "recycled, but only a few times before the polymer "
                         "is too degraded."},
             {"id": "ph", "label": "Phosphate rock",
              "name": "Phosphate rock",
              "limit_kind": "no-substitute",
              "use": "Fertiliser. Phosphorus is one of the few elements "
                     "crops cannot be grown without and for which there is "
                     "no substitute at all.",
              "limit": "Concentrated deposits are in a handful of countries, "
                       "and there is no alternative source. This is the "
                       "resource limit with the sharpest consequences.",
              "recycle": "In principle, from sewage and manure, and this is "
                         "starting to happen. Phosphorus spread thinly on "
                         "fields or washed into rivers is effectively lost."},
             {"id": "he", "label": "Helium", "name": "Helium",
              "limit_kind": "leaves-the-planet",
              "use": "Cooling the magnets in MRI scanners, and in welding "
                     "and leak detection. Nothing else stays liquid at 4 "
                     "kelvin.",
              "limit": "Made underground by radioactive decay over hundreds "
                       "of millions of years, and collected as a by-product "
                       "of natural gas. Released to the air, it leaves the "
                       "atmosphere for space and is gone for good.",
              "recycle": "Only by capturing it before it escapes, which good "
                         "MRI installations now do. Party balloons are a "
                         "one-way trip."},
         ]},

        {"type": "key-fact", "ref": "every-loop-leaks"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["finite resource", "ore", "recycling", "downcycling",
                   "reserve"]},

        {"type": "misconception", "id": "think-commit-recycling",
         "anchor": "s-think", "targets": "EARTH-11"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    # ⊖ NO FIGURES, DELIBERATELY (audit law 8). The one diagram this lesson
    # could want is a loop with an arrow leaking out of it, and the bench
    # above IS that diagram with the leak drawn to scale from real figures.
    # A static version beside it would be a worse copy that cannot be run.
    "figures": [],

    "activities": [
        {"id": "think-commit-recycling",
         "kind": "predict",
         "demand": "explain",
         "targets": "EARTH-11",
         "reveal_anchor": "think-reveal-recycling",
         "prompt": "You have just run the loop five times. Commit before you "
                   "read on.",
         # ⚑ MRB-177 — distractors at the answer's own length: 14, 15, 14, 14
         # words. Each is a wrong RULE about what a loop does, not a shorter
         # version of the right one.
         "options": [
             "Right — a recycled material is back where it started at the "
             "beginning of every pass",
             "Wrong — every pass loses some, so recycling slows the loss "
             "rather than stopping it",
             "Right, as long as everyone sorts their bins properly and "
             "nothing is put in the wrong one",
             "Wrong — recycling returns no useful material at all, so the "
             "loop is closed before it starts",
         ],
         "reveal": [
             "Every pass through the loop loses material. Some is never "
             "collected, some is lost in sorting and melting, and some comes "
             "back too degraded to do the original job. Even at nine "
             "collected out of ten, aluminium gets about seven lifetimes out "
             "of a kilogram of ore, not infinite lifetimes — and a crisp "
             "packet gets barely one, however carefully you put it in the "
             "right bin.",
             "So recycling buys time; it does not make a finite stock "
             "infinite. <strong>The two things that actually cut extraction "
             "are using less and using it for longer</strong> — which is why "
             "reduce and reuse come before recycle, and in that order.",
         ]},
    ],

    "key_facts": [
        {"id": "every-loop-leaks", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "The Earth holds a fixed stock of every ore, and extraction "
                 "is one-way. Recycling returns part of the material each "
                 "time round, so one kilogram from the ground can serve "
                 "several lifetimes — but every loop leaks, so recycling "
                 "slows the loss and never stops it."},
    ],

    "ladder": {
        # index 0 — Design's own.
        "recall": {
            "q": "Why is a metal ore described as a finite resource?",
            "options": [
                "It formed over millions of years and is not being replaced "
                "as fast as we extract it",
                "There is only a small amount of it left in the crust "
                "compared with what we have already used",
                "The metal in it can only be used once, so every kilogram is "
                "finished after a single lifetime",
                "It is going to run out within the next few years at the "
                "rate we are currently extracting it",
            ],
            "answer": 0,
            "feedback": {
                1: "Some ores are abundant. Finite is about not being "
                   "replaced, not about being scarce today.",
                2: "Metal can be used many times over by recycling. It is "
                   "the ore in the ground that is not coming back.",
                3: "No ore is that close to gone, and reserve figures move. "
                   "Finite means the stock only goes one way.",
            }},

        # index 2 — moved from Design's 0 (MRB-278). No option text edited by
        # the move; the three distractors are separately lengthened to the
        # answer's own length under MRB-177.
        "apply": {
            "q": "Nine out of ten crisp packets are collected, and nine out "
                 "of ten aluminium cans are collected. Why does recycling do "
                 "so much more for the cans?",
            "options": [
                "There is more aluminium in one can than in one packet, so "
                "each can returns a larger mass",
                "Cans are put in the right bin more carefully, so more of "
                "them survive the sorting stage",
                "Almost all of the collected aluminium comes back usable, "
                "while almost none of the packet does",
                "Aluminium is worth more per tonne, so recyclers work much "
                "harder at getting it back",
            ],
            "answer": 2,
            "feedback": {
                0: "True, and irrelevant — the bench compared equal masses "
                   "and the gap was still enormous.",
                1: "Both were collected at nine in ten. Collection was held "
                   "equal on purpose.",
                3: "Value affects whether anyone bothers, but the reason the "
                   "loop works is physical: the metal survives melting and "
                   "the laminate cannot be separated.",
            }},

        "explain": {
            "q": "A council doubles its collection rate for plastic bottles "
                 "and is disappointed that the amount of new plastic being "
                 "made barely falls. Explain why, using what the bench "
                 "showed you.",
            "field_label": "Your explanation",
            "placeholder": "Collecting more only helps if…",
            "success": [
                "Says collecting more material is only half of it — the "
                "material also has to survive the process.",
                "Says PET degrades when melted, so only about half comes "
                "back fit for a bottle.",
                "Says the loop leaks every pass, so the multiplier stays low "
                "even at a high collection rate.",
                "Compares with a material that does come back well, such as "
                "aluminium or steel.",
                "Says cutting new plastic needs using less or reusing, not "
                "only better collection.",
            ]},

        "produce": {
            "q": "A smartphone contains around thirty different elements, "
                 "each in tiny amounts and bonded into layers a few atoms "
                 "thick. Predict how well it recycles compared with an "
                 "aluminium can, and say what the designers would have to "
                 "change.",
            "field_label": "Your answer",
            "placeholder": "A phone recycles much worse than a can because…",
            "success": [
                "Predicts much worse recycling than a can.",
                "Says the materials are mixed or bonded together so they "
                "cannot be separated.",
                "Says the amount of each element per phone is tiny, so "
                "recovery is expensive per kilogram.",
                "Notes that some materials are recovered (gold, copper) "
                "while most are lost.",
                "Says designing for disassembly — fewer materials, separable "
                "parts — is what would change it.",
            ]},
    },

    "key_note": "Metal ores, crude oil and phosphate rock are finite: they "
                "formed over millions of years and are being extracted in "
                "centuries. Recycling returns part of the material to be "
                "used again, saving raw material and usually a large amount "
                "of energy — recycled aluminium takes about a twentieth of "
                "the energy of new metal from ore. But every loop loses some "
                "material, and some materials come back degraded or cannot "
                "be separated at all, so recycling slows extraction rather "
                "than ending it. Using less and using things for longer cut "
                "extraction more than recycling does.",

    "stretch": [
        {"type": "explainer", "id": "years-left-is-not-a-measurement",
         "text": "You will see headlines saying a metal has a certain number "
                 "of years left. Those figures move, and not because anyone "
                 "found more planet. A <strong>reserve</strong> is the part "
                 "of a resource that can be extracted at a profit with "
                 "today's technology, so when the price rises or the mining "
                 "gets cleverer, ore that was worthless becomes a reserve "
                 "and the number of years left goes up. That does not mean "
                 "the stock is unlimited — it means the cheap, concentrated "
                 "part gets used first, and everything after it takes more "
                 "energy to extract. The limit shows up as rising energy "
                 "cost long before anything physically runs out."},
        {"type": "explainer", "id": "the-packet-is-a-trade-off",
         "text": "The awkward one is the crisp packet. Plastic film "
                 "laminated to a layer of aluminium a few microns thick is a "
                 "brilliant piece of engineering — it keeps food fresh for "
                 "months using very little material — and it is close to "
                 "unrecyclable, because no process separates the two layers "
                 "economically. That is a real trade-off rather than a "
                 "mistake, and it is the shape of most recycling problems: "
                 "the property that makes a material useful is often the "
                 "same property that makes it hard to get back."},
    ],

    "support": [],

    # ⚠️ THE CARD FRONTS ARE LOWERCASE, BECAUSE DESIGN DREW THEM THAT WAY, and
    # `terms` above joins on this exact string.
    "vocabulary": [
        {"term": "finite resource",
         "definition": "Something taken from the Earth that is not being "
                       "replaced on any timescale that matters to us.",
         "note": "Finite does not mean nearly gone. It means the stock only "
                 "goes one way."},
        {"term": "ore",
         "definition": "Rock containing enough of a metal compound to be "
                       "worth extracting it.",
         "note": "Ore is not the metal. Whether a rock counts as ore depends "
                 "on the price and the technology, so the same rock can stop "
                 "and start being ore."},
        {"term": "recycling",
         "definition": "Collecting a used material and processing it so it "
                       "can be made into something again.",
         "note": "Every pass loses some. Recycling slows extraction; it does "
                 "not replace it."},
        {"term": "downcycling",
         "definition": "Recycling a material into something less demanding "
                       "than it was, because it comes back degraded.",
         "note": "A bottle that becomes fleece is not a bottle again, and "
                 "the fleece has nowhere to go after that."},
        {"term": "reserve",
         "definition": "The part of a resource that can be extracted at a "
                       "profit with the technology we have now.",
         "note": "This is why “years left” figures keep changing "
                 "without anyone finding more planet."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why recycling a can beats recycling a "
                      "crisp packet?",
              "cta": "Ask about this lesson",
              "anchor": "s-loop"},

    "ks4_becomes": "Life-cycle assessment, and the extraction of copper from "
                   "low-grade ores by phytomining and bioleaching.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
    "review_state": "draft",
}
