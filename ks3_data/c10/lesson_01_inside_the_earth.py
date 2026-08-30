"""C10 L1 — Inside the Earth: composition and structure (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c10/c10-01-inside-the-earth.dc.html`.

── ⚠️ THERE ARE NO AUTHOR'S NOTES FOR THIS LESSON ──────────────────────

`NOTES-C10.md` covers `c10-04` and no other page in the unit. Every science
call below is therefore RULED HERE, from Design's drawing, and written down so
that a reviewer can disagree with a decision rather than having to reconstruct
one. Where Design's drawing and any written text disagreed, the drawing won.

── TWO STATUTORY STATEMENTS, ONE LESSON ────────────────────────────────

`KS3.C.EA.01` (the composition of the Earth) and `KS3.C.EA.02` (the structure
of the Earth) are both owned WHOLE here. §4.4 rule 3 forbids one statement
living in two lessons; it permits one lesson holding two, and the unit spine
(`ks3_data/c10/__init__.py`) already records that ruling. No sub-ID is minted:
neither bullet is clause-split, so there is nothing to split.

The two statements are not two halves of the page. Composition is what each
layer is MADE OF and structure is where the boundaries ARE, and the layers
instrument answers both from one payload — a layer's `facts` carry the
composition, its `thickness` places the boundary, and the panel prints them
together because a student who can name the mantle and not say what it is made
of has learned a diagram rather than a planet.

── ⚖️ MRB-225 · THE VERSION THAT IS TRUE, NOT THE VERSION THAT IS FAMOUS

Five rulings, and the first is the one this whole topic turns on.

1. **THE MANTLE IS SOLID ROCK. The crust does not float on molten rock.**
   The famous version — a thin crust drifting on a sea of magma — is taught
   somewhere in most schools and it is wrong, and it is wrong in a way that
   the evidence on this very page refutes: S-waves cannot travel through
   liquid, and they pass through the whole mantle. What the mantle does is
   CREEP: solid rock, hot enough and squeezed hard enough to flow a few
   centimetres a year. Solid and rigid are not the same word, and the page
   says so in those words at `#s-think`. Nothing anywhere else in the lesson
   retracts it — the crust note says the plates move, never that they float.

2. **MAGMA IS THE EXCEPTION, NOT THE OCEAN.** Melt exists in pockets, mostly
   where pressure drops far enough to let a little of the rock melt. A page
   that says "the mantle is solid" and then talks about "the magma below"
   has retracted itself inside one lesson, which is exactly what MRB-225
   forbids, so the word magma appears only where it is being bounded.

3. **⚑ MARS IS NOT DESCRIBED AS HAVING A SOLID CORE.** Design's going-further
   layer and her rung-4 criteria both read "a cold, solid core". That is the
   textbook sentence and it stopped being true in 2021, when InSight's
   seismometer recorded waves reflecting off a large LIQUID core. What is
   true, and what carries her whole argument unchanged, is that **Mars has no
   global magnetic field today** — its core is no longer stirring in the way
   that generates one, and its oldest rocks record a field that switched off
   around four billion years ago. The chain the lesson teaches (moving liquid
   metal → field → atmosphere kept) is untouched; only the claim that has
   since been measured false is removed. **This is a change to what Design
   WROTE, made under MRB-225, and it is flagged for the science gate.**

4. **A PERMANENT MAGNET CANNOT EXPLAIN THE FIELD**, because iron loses its
   magnetism above about 770 °C and the core is thousands of degrees hotter.
   The field is evidence of MOTION, not of a buried bar magnet. Design draws
   this at evidence `e3` and it is kept exactly.

5. **THE INNER CORE IS SOLID BECAUSE OF PRESSURE, NOT BECAUSE IT IS COOLER.**
   It is the hottest part of the planet and it is solid anyway. Design's key
   fact says "held rigid by pressure"; the built page says "kept solid by the
   pressure at the centre", because RIGID is the word the mantle paragraph
   spends two sentences prising apart from SOLID, and using it here for the
   inner core would blunt that distinction eight lines earlier.

── SCIENCE FIGURES, RULED ──────────────────────────────────────────────

Every number below is Design's and every one is checked. Boundaries at 35,
2900 and 5150 km give thicknesses 35 / 2865 / 2250 / 1221, which sum to 6371 —
the Earth's mean radius. The payload authors the THICKNESSES and the renderer
derives the boundaries, so the bar and the captions cannot disagree; `radius`
is authored beside them as a CLAIM and the build refuses a set that no longer
sums to it. That is `c10-04`'s `order_claim` pattern applied to a geometry.

  · Kola: 12.262 km over about twenty years, abandoned with the rock at the
    bottom near 180 °C and closing the hole. 12.3 / 6371 is 0.19%, which is
    the "two tenths of one per cent" Design writes, and 12.3 / 35 is about a
    third of the way through the crust, which is the crust note's claim.
  · Crust "up to about 400 °C" is the base of continental crust. Accepted as
    a teaching value.
  · 2.7 g/cm³ surface rock against 5.51 g/cm³ for the whole planet. Accepted.
  · Inner core about 5500 °C, near the Sun's surface temperature. Accepted.
  · Pressure at the centre over three million times atmospheric (≈360 GPa).

⊖ **"AROUND 84 PER CENT OF THE EARTH BY VOLUME" IS NOT PRINTED.** Design puts
it in the mantle note. The bar beside it is a RADIUS bar, on which the mantle
is 45%, and the panel now derives that 45% as a number — so the drawn figure
and the printed figure would be two different true things about the same layer
sitting eight pixels apart, which at KS3 reads as an error. The note says "by
far the largest layer" and the instrument supplies the arithmetic.

── ⚑ §5A · WHAT THE INSTRUMENTS COMPUTE, AND WHAT THEY ARE TOLD ────────

Not one boundary depth, not one percentage and not one total is authored.
`earth-layers` is given four thicknesses and derives every depth range, every
share of the distance to the centre, the "Centre · 6371 km" caption and the
crust's share inside the scale panel's own sentence. `depth-evidence` computes
nothing numeric and claims nothing numeric.

⚠️ **THE ONE PLACE THE DRAWING IS NOT TO SCALE, SAID OUT LOUD.** A crust that
is 0.5% of the bar is under four pixels wide on a phone and cannot be tapped,
so the crust segment carries a minimum width — Design's own `min-width: 30px`.
The scale panel therefore states the true share as a derived number AND says
the bar exaggerates it. A distortion a page admits to is a scale lesson; the
same distortion unremarked is the misconception `EARTH-04` records.

── ⊖ NO `safety_note`, DELIBERATELY ────────────────────────────────────

There is no apparatus, no substance and nothing to run in a room: the page is
a model of a planet and a set of inferences from earthquake records. Recorded
rather than assumed, because an absent note is indistinguishable from an
oversight unless somebody writes down that it was checked.

── SAFEGUARDING ────────────────────────────────────────────────────────

CHECKED, AND NOTHING IS OWED. The lesson touches no student's body, health,
home or family circumstances; the only hazard named anywhere is a borehole in
Russia that was abandoned in 1992. Earthquakes appear solely as a source of
waves that are recorded by instruments — the page never describes damage,
injury or a named disaster, which is the one route by which this topic could
reach a student who has lived through one. Design carried no Childline block
and none is added.

── ⚑ MRB-278 · ANSWER POSITION ─────────────────────────────────────────

Design draws both marked rungs with the correct option at index 0, and
`c10-04` already holds recall=0 and apply=2. C10's ladder corpus is four rungs
and the gate refuses an index that is never the answer once the corpus can
fill every index, so this lesson takes **recall=1 and apply=3** and the unit
lands on one rung per index. **Only the ORDER moves; no option text is edited
by the move**, which is the treatment C9's eight rungs and c10-04's two took.

⚑ MRB-177 · THE `#s-think` DISTRACTORS ARE LENGTHENED, NOT THE ANSWER
SHORTENED. Design's think options run 11 / 15 / 7 / 7 words with the correct
one at 15 — a four-word tell, and the predict gate reads the SET rather than
the key, so a student could commit on shape alone and never commit to the
belief at all. Each distractor is rewritten as a WRONG RULE about what the
mantle is, at the answer's own length. The correct option is untouched.
"""

LESSON = {
    "slug":  "inside-the-earth",
    "title": "Inside the Earth",
    "discipline": "chemistry",
    "unit": "The Earth and its atmosphere",
    "family": "MODEL",

    "covers": ["KS3.C.EA.01", "KS3.C.EA.02"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "earth-and-universe", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["ceramics-polymers-and-composites"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "Nobody has been more than twelve kilometres down, "
                        "and the centre is six thousand kilometres away. "
                        "Open the four layers and see how anyone knows what "
                        "is there.",

    "big_question": "Nobody has ever been more than twelve kilometres into "
                    "the ground, and the centre is six thousand kilometres "
                    "down. So how does anyone know what is there?",

    "rail": [
        {"anchor": "s-hook",     "short": "HOOK",
         "label": "Twelve kilometres", "done_when": "committed"},
        {"anchor": "s-layers",   "short": "LAYERS",
         "label": "Four layers",       "done_when": "all_four_layers_opened"},
        {"anchor": "s-evidence", "short": "PROOF",
         "label": "How we know",       "done_when": "all_three_answered"},
        {"anchor": "s-think",    "short": "THINK",
         "label": "The mantle",        "done_when": "committed"},
        {"anchor": "s-ladder",   "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The deepest hole ever drilled took twenty years and "
                 "reached 12.3 kilometres. The centre of the Earth is 6371 "
                 "kilometres down.",
        "prompt": "The Kola borehole was abandoned because the rock at the "
                  "bottom was 180 °C and behaving like plastic — it kept "
                  "closing the hole. Twelve kilometres is two tenths of one "
                  "per cent of the way to the middle. On a football-sized "
                  "Earth, that hole would not break the skin of the leather.",
        "commit": "So how do we know what the inside is made of?",
        "options": [
            "Deeper boreholes that were never published",
            "From the way earthquake waves travel through the planet",
            "From what comes out of volcanoes, all the way down",
            "Nobody knows; it is a guess",
        ],
        "reveal": "By listening to earthquakes. Every large earthquake sends "
                  "waves through the whole planet, and those waves bend, "
                  "speed up, slow down and sometimes stop dead depending on "
                  "what they are travelling through. Hundreds of "
                  "seismometers around the world record when each wave "
                  "arrives. From those arrival times — and nothing else — "
                  "you can work out where the boundaries are and whether "
                  "each layer is solid or liquid. <strong>The inside of "
                  "the Earth was mapped by sound, not by digging.</strong>",
    },

    "misconceptions": [
        {"id": "EARTH-01",
         "statement": "The mantle is a sea of molten lava, and volcanoes are "
                      "holes that let it out.",
         "elicited_by": "think-commit-mantle",
         "confronted_by": "think-reveal-mantle"},
        # ⚑ The hook's fourth option IS this belief, offered plainly, and the
        # evidence set is where it dies — three inferences a student can
        # follow, none of which needs anybody to have gone down there.
        {"id": "EARTH-02",
         "statement": "Nobody has ever been down there, so what is inside "
                      "the Earth is really only a guess.",
         "elicited_by": "s-hook",
         "confronted_by": "s-evidence"},
        # ⚑ NO `elicited_by`, DELIBERATELY (audit law 15 / MRB-248). Nothing
        # on this page asks a student to commit to "hot means melted"; the
        # inner-core panel simply states the temperature and the state in the
        # same three cards and lets the pair do the work. Inventing an anchor
        # to fill the column would be the dishonest version.
        {"id": "EARTH-03",
         "statement": "Anything that hot must be melted, so the hottest part "
                      "of the Earth is liquid.",
         "confronted_by": "s-layers"},
        # ⚑ NO `elicited_by` either, and for the same reason. The bar is
        # where the belief is answered, in the one treatment that can answer
        # it: the crust's share of the distance to the centre, derived and
        # printed beside a bar drawn from the same number.
        {"id": "EARTH-04",
         "statement": "The crust is a thick shell, and mines and boreholes "
                      "have been most of the way through it.",
         "confronted_by": "s-layers"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "The Earth is not one substance. It is a set of "
                 "<strong>layers</strong>, each with its own composition, "
                 "temperature and state — and the boundaries between them "
                 "are sharp."},
        {"type": "explainer",
         "text": "Everything you have ever seen, mined or built on is the "
                 "<strong>crust</strong>: a skin so thin that on the scale "
                 "of the whole planet it is barely there."},

        # ── #s-layers — the four layers, drawn from their thicknesses.
        # Light `ks3-block` in Design's file, so the unit's
        # `_INSTRUMENT_SEGMENTS` map sends it to the `check` shell.
        #
        # ⚠️ NOT ONE DEPTH BELOW IS AUTHORED. The payload states four
        # thicknesses and a radius to check them against; every boundary,
        # every share and both end captions are computed in
        # `ks3_art/c10.py`.
        {"type": "earth-layers", "id": "layers-bar", "anchor": "s-layers",
         "eyebrow": "Your turn · four layers",
         # ⚠️ The heading used to read "The bar is drawn to scale." and the
         # prompt "The widths are the real proportions." (C10-02, chem audit
         # 25 Aug 2026). The crust is drawn at the bar's minimum segment
         # width — roughly ten times its true share — and the page's only
         # admission of that was locked behind opening all four layers. Both
         # lines now carry the honesty up front, and `scale_note` puts the
         # number under the drawing itself. Heading change flagged to Design.
         "heading": "Tap a layer. The widths are the real proportions — "
                    "except the crust.",
         "prompt": "Almost everything on this bar is drawn to scale. The "
                   "crust is the exception, and it is the sliver at the very "
                   "top.",
         "scale_note": "One honest exception: the {thin_name} is really only "
                       "{thin_share} of the way down, which is thinner than "
                       "a line you could tap. It is drawn wider here so you "
                       "can reach it — everything else is to scale.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} opened",
                          "start": 1, "total": 4},

         "depth_unit": "km",
         "radius": 6371,
         "start_layer": "crust",
         "layers_to_tick": 4,
         "thinnest_claim": "crust",
         "surface_label": "Surface · 0 {unit}",
         "centre_label": "Centre · {total} {unit}",
         "state_label": "State",
         "share_label": "Share of the depth",

         "layers": [
             {"id": "crust", "label": "Crust", "name": "Crust",
              "thickness": 35,
              "state": "solid", "state_detail": "Solid rock",
              "facts": [["Temperature", "Up to about 400 °C"],
                        ["Made of", "Silicon and oxygen compounds"]],
              "note": "Thinner under the oceans, thicker under mountains, "
                      "and cracked into plates that move a few centimetres "
                      "a year. Everything anyone has ever mined or built on "
                      "is in this layer, and the deepest borehole reached "
                      "only a third of the way through it."},
             {"id": "mantle", "label": "Mantle", "name": "Mantle",
              "thickness": 2865,
              "state": "solid", "state_detail": "Solid, but flows slowly",
              "facts": [["Temperature", "500 – 4000 °C"],
                        ["Made of", "Silicon, oxygen, iron, magnesium"]],
              "note": "By far the largest layer. It is solid rock, but hot "
                      "enough and under enough pressure to creep like "
                      "extremely stiff toffee. Those slow currents are what "
                      "drag the plates above them around."},
             {"id": "outer", "label": "Outer core", "name": "Outer core",
              "thickness": 2250,
              "state": "liquid", "state_detail": "Liquid",
              "facts": [["Temperature", "4000 – 5000 °C"],
                        ["Made of", "Iron and nickel"]],
              "note": "Molten metal, and the only genuinely liquid layer in "
                      "the planet. It is known to be liquid because one type "
                      "of earthquake wave cannot pass through it at all — "
                      "and that same swirling liquid metal generates the "
                      "Earth’s magnetic field."},
             {"id": "inner", "label": "Inner core", "name": "Inner core",
              "thickness": 1221,
              "state": "solid", "state_detail": "Solid",
              "facts": [["Temperature", "About 5500 °C"],
                        ["Made of", "Iron and nickel"]],
              "note": "Hotter than the liquid layer above it and solid "
                      "anyway, because the pressure at the centre of the "
                      "Earth is too great to let the atoms move apart. A "
                      "ball of iron about two-thirds the width of the Moon, "
                      "as hot as the surface of the Sun."},
         ],

         # The panel that opens once all four have been read. `{crust_share}`,
         # `{crust_name}`, `{total}` and `{unit}` are filled at render.
         "scale_panel": {
             "title": "Look at how little of that bar is crust.",
             "text": [
                 "Every mine, every borehole, every fossil, every ocean and "
                 "every mountain range is in the thin strip on the left. The "
                 "{thin_name} is {thin_share} of the {total} {unit} from the "
                 "surface to the centre. Scale the Earth down to the size of "
                 "an apple and it is thinner than the skin.",
                 "On the bar above it is drawn wider than that, because "
                 "{thin_share} of a screen is a hairline nobody could tap. "
                 "Every other width on the bar is the real proportion.",
             ]}},

        {"type": "key-fact", "ref": "four-layers"},

        # ── #s-evidence — three inferences, each committed to before it is
        # answered. Light `ks3-block` → `check`.
        {"type": "depth-evidence", "id": "evidence-set", "anchor": "s-evidence",
         "eyebrow": "Three questions · how we know",
         "heading": "The evidence, not the picture in the textbook",
         "prompt": "Commit before you read. Every one of these was worked "
                   "out without anyone going down there.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} answered",
                          "start": 0, "total": 3},
         "entries_to_tick": 3,
         "entries": [
             {"id": "wave",
              "q": "One type of earthquake wave travels through the mantle "
                   "but stops dead at 2900 km. What does that show?",
              "choices": [
                  {"id": "a", "label": "There is a layer of liquid there"},
                  {"id": "b", "label": "The rock gets too hot"},
                  {"id": "c", "label": "The wave runs out of energy"},
              ],
              "answer": "A liquid layer. S-waves cannot travel through "
                        "liquids at all, so the depth at which they vanish "
                        "marks the top of the liquid outer core exactly. The "
                        "wave that stops tells you as much as the wave that "
                        "arrives."},
             {"id": "dense",
              "q": "The whole Earth is much denser than any rock found at "
                   "the surface. What does that suggest?",
              "choices": [
                  {"id": "a", "label": "The surface rocks are unusual"},
                  {"id": "b", "label": "Something much denser is inside"},
                  {"id": "c", "label": "The Earth is hollow"},
              ],
              "answer": "Something far denser is inside. Surface rock "
                        "averages about 2.7 g/cm³ and the whole planet "
                        "averages 5.5, so the interior must be made of "
                        "something heavy. Iron fits, and meteorites, which "
                        "formed from the same material, are full of it."},
             {"id": "field",
              "q": "The Earth has a magnetic field strong enough to swing a "
                   "compass needle anywhere on the surface. What does that "
                   "require?",
              "choices": [
                  {"id": "a", "label": "A giant bar magnet in the middle"},
                  {"id": "b", "label": "Moving liquid metal inside"},
                  {"id": "c", "label": "The Sun’s magnetism"},
              ],
              "answer": "Moving liquid metal. A permanent magnet cannot "
                        "survive those temperatures — heat destroys "
                        "magnetism. What does work is electric current, and "
                        "a churning ocean of molten iron carries enormous "
                        "currents. The field is evidence that part of the "
                        "core is liquid and in motion."},
         ]},

        # ⊕ The keyword block is the ENGINE's, not Design's — she drew none on
        # this page, as she drew none on any of C9's four, and all four ship
        # one. It is OFF THE RAIL: `docs/ks3/rail-manifest.md` records five
        # stops for this page and `#s-words` is not one of them.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["crust", "mantle", "core", "seismic wave", "density"]},

        {"type": "misconception", "id": "think-commit-mantle",
         "anchor": "s-think", "targets": "EARTH-01"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    # ⊖ NO FIGURES, DELIBERATELY (audit law 8). The one diagram this lesson
    # wants is a cross-section of the Earth with its layers to scale, and
    # `#s-layers` IS that diagram, drawn from the thicknesses and openable.
    # A static copy beside it would carry the same claim with none of the
    # arithmetic and no way to check it.
    "figures": [],

    "activities": [
        {"id": "think-commit-mantle",
         "kind": "predict",
         "demand": "explain",
         "targets": "EARTH-01",
         "reveal_anchor": "think-reveal-mantle",
         # ⚠️ THE QUOTE IS NOT REPEATED HERE. `r_misconception` already prints
         # the belief as `.ks3-mis-quote` from the register statement, which
         # is Design's own treatment; putting it in the prompt as well ships
         # the sentence twice, eight pixels apart.
         "prompt": "Lava does come out of volcanoes, and it comes from "
                   "below. Commit before you read on.",
         # ⚑ MRB-177 — the distractors are wrong RULES about what the mantle
         # is, at the answer's own length: 15, 15, 16, 16 words. Design's ran
         # 11 / 15 / 7 / 7 with the answer longest, which the predict gate
         # reads as a set a student can solve on shape.
         "options": [
             "Right — the mantle is a layer of molten rock that volcanoes "
             "tap straight into",
             "Wrong — the mantle is solid rock that flows slowly; magma "
             "forms only in pockets",
             "Right — the crust floats on liquid rock, which is why the "
             "plates can move around",
             "Wrong — the mantle is solid all the way down and lava rises "
             "from the core",
         ],
         "reveal": [
             "The mantle is <strong>solid rock</strong>. It has to be: "
             "earthquake waves that cannot travel through liquid pass "
             "straight through it, which is how anyone knows. What makes it "
             "confusing is that solid rock under that much heat and pressure "
             "can <em>flow</em> — a few centimetres a year, like extremely "
             "stiff toffee. Solid and rigid are not the same word.",
             "Magma exists only in small pockets, mostly where the pressure "
             "drops enough to let a little of the rock melt. It is the "
             "exception, not the ocean. <strong>If the mantle really were "
             "liquid, the crust would not be floating on it — it would have "
             "sunk into it long ago.</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "four-layers", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Crust, mantle, outer core, inner core. The mantle is solid "
                 "rock that flows very slowly; the outer core is liquid "
                 "iron; the inner core is solid iron, kept solid by the "
                 "pressure at the centre."},
    ],

    "ladder": {
        # index 1 — moved from Design's 0 (MRB-278). No option text edited.
        "recall": {
            "q": "Name the four layers of the Earth in order from the "
                 "surface inwards.",
            "options": [
                "Crust, outer core, mantle, inner core",
                "Crust, mantle, outer core, inner core",
                "Mantle, crust, core, inner core",
                "Crust, mantle, core, magma",
            ],
            "answer": 1,
            "feedback": {
                0: "The mantle comes immediately below the crust; the core "
                   "is the innermost region.",
                2: "The crust is on the outside — it is the layer you are "
                   "standing on.",
                3: "Magma is not a layer. It is melted rock in pockets, "
                   "mostly near the top of the mantle.",
            }},

        # index 3 — moved from Design's 0 (MRB-278). No option text edited.
        "apply": {
            "q": "The inner core is hotter than the outer core, yet it is "
                 "solid and the outer core is liquid. Why?",
            "options": [
                "The inner core is made of a different metal with a higher "
                "melting point",
                "The inner core has cooled down more than the outer core",
                "The outer core is closer to the surface, so it is heated "
                "by the Sun",
                "The pressure at the centre is so great that the iron "
                "cannot melt",
            ],
            "answer": 3,
            "feedback": {
                0: "Both are iron and nickel. The difference is the "
                   "pressure, not the material.",
                1: "It is the hottest part of the planet, at around "
                   "5500 °C.",
                2: "The Sun heats nothing below a metre or so of soil. Core "
                   "heat is left over from formation and from radioactive "
                   "decay.",
            }},

        "explain": {
            "q": "Explain how scientists know the Earth has a liquid layer "
                 "inside it, when nobody has ever been deeper than 12 km.",
            "field_label": "Your explanation",
            "placeholder": "Earthquakes send waves…",
            "success": [
                "Says earthquakes send waves right through the Earth.",
                "Says the waves are detected at stations all over the "
                "world.",
                "Says one type of wave cannot travel through liquid.",
                "Says that wave disappears beyond a certain depth, marking "
                "the liquid outer core.",
                "Says the conclusion comes from measurement and inference, "
                "not from direct observation.",
            ]},

        # ⚑ RULED (MRB-225, ruling 3 above). Design's version opens "Mars has
        # a cold, largely solid core", which InSight measured false in 2021.
        # The question keeps her argument and drops the claim.
        "produce": {
            "q": "Mars has no global magnetic field today, although its "
                 "oldest rocks record one, and its atmosphere is very thin. "
                 "Suggest how those facts might be connected, and say what "
                 "evidence would test your idea.",
            "field_label": "Your answer",
            "placeholder": "A magnetic field needs…",
            "success": [
                "Says a magnetic field needs liquid metal that is moving "
                "inside the planet.",
                "Says a core that has stopped stirring cannot generate one.",
                "Says the Earth’s field deflects charged particles streaming "
                "from the Sun.",
                "Says without a field the solar wind can strip a planet’s "
                "atmosphere away over time.",
                "Suggests testable evidence, such as measuring the magnetism "
                "locked into Mars’s oldest rocks.",
            ]},
    },

    "key_note": "The Earth has four layers: a thin rocky crust, a thick "
                "mantle of solid rock that flows very slowly, a liquid iron "
                "outer core and a solid iron inner core. The structure is "
                "known from the way earthquake waves travel through the "
                "planet, because different waves behave differently in "
                "solids and liquids.",

    "stretch": [
        {"type": "explainer", "id": "the-core-and-the-compass",
         "text": "The liquid outer core is the reason a compass works. Iron "
                 "that hot cannot be a magnet in the ordinary sense — heat "
                 "destroys magnetism — but the core is molten metal, it "
                 "moves, and moving metal carries electric currents. Those "
                 "currents generate the magnetic field that surrounds the "
                 "planet, deflects the solar wind and keeps the atmosphere "
                 "from being stripped away. Mars has no global field today: "
                 "its oldest rocks record one that switched off around four "
                 "billion years ago, whatever was stirring its core stopped, "
                 "and almost none of its atmosphere is left."},
        {"type": "explainer", "id": "the-inner-core-is-growing",
         "text": "The inner core is the strangest part. It is hotter than "
                 "the liquid layer above it — around 5500 °C, roughly the "
                 "surface temperature of the Sun — and it is solid anyway, "
                 "because the pressure at the centre of the Earth is over "
                 "three million times atmospheric pressure and will not let "
                 "the atoms move apart. It is also growing: every year a "
                 "little more of the outer core freezes onto it, and the "
                 "energy released as it does helps drive the currents that "
                 "make the magnetic field."},
    ],

    "support": [],

    # ⚠️ THE CARD FRONTS ARE LOWERCASE, matching `c10-04`'s, and `terms`
    # above joins on this exact string.
    "vocabulary": [
        {"term": "crust",
         "definition": "The thin outer layer of solid rock that the whole "
                       "surface of the Earth sits on.",
         "note": "Thin is not a figure of speech. It is under one per cent "
                 "of the way to the centre."},
        {"term": "mantle",
         "definition": "The thick layer of solid rock below the crust, hot "
                       "enough and squeezed hard enough to flow very "
                       "slowly.",
         "note": "Solid and rigid are not the same word. It creeps a few "
                 "centimetres a year."},
        {"term": "core",
         "definition": "The iron and nickel centre of the Earth: a liquid "
                       "outer part and a solid inner part.",
         "note": "The inner part is the hotter of the two and is solid "
                 "because of the pressure."},
        {"term": "seismic wave",
         "definition": "A wave sent through the Earth by an earthquake and "
                       "recorded by instruments all over the world.",
         "note": "One type stops at liquid. Where it disappears is where a "
                 "liquid layer starts."},
        {"term": "density",
         "definition": "How much mass a material has for its size, measured "
                       "in grams per cubic centimetre.",
         "note": "The whole Earth is about twice as dense as the rock at "
                 "the surface, which is why the inside cannot be more of "
                 "the same."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how solid rock can flow?",
              "cta": "Ask about this lesson",
              "anchor": "s-layers"},

    "ks4_becomes": "Plate tectonics driven by convection in the mantle, and "
                   "using P-wave and S-wave shadow zones as evidence for a "
                   "liquid outer core.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
    "review_state": "draft",
}
