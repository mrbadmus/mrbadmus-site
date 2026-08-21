"""C7 L3 — Endothermic reactions (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c7/c7-03-endothermic-reactions.dc.html`, and her
author's notes `docs/ks3/design-reference/c7/NOTES-C7.md` §1, §2, §3, §4 flags
9, 10, 11, §5 (`ENER-05`, `ENER-06`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`ITEMS`, `USES`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the
hook options and reveal, the two explainer paragraphs, the sorter's eyebrow /
heading / lead / verdict lines, the closing panel, the key fact, the `#s-uses`
eyebrow and heading, the `#s-think` options and its two reveal paragraphs, the
key note and both "Going further" paragraphs were lifted from `lessonVals(s)`
and from the markup.

── THE PAIRS ARE THE LESSON, AND THEY ARE WHY THIS IS A CONTRAST ───────

NOTES-C7 §2: "an eight-item sorter, exothermic against endothermic, with three
deliberate pairs (melting/freezing, photosynthesis/respiration) so the reversal
rule falls out of the sort rather than being stated."

That is the whole architecture of the page, and it is why this lesson exists at
all rather than as a paragraph at the end of `c7-02`. A student who sorts
melting as endothermic and then meets freezing three rows later has to decide
what to do about it, and the closing panel names what they have just found
rather than announcing it in advance.

Two consequences, both enforced in `r_energy_sorter`:

  · THE COUNT IN THE LEAD IS DERIVED, NOT AUTHORED. How many of the eight are
    endothermic is computed from the items and asserted against the prose, so
    a ninth item or a flipped flag fails the build instead of shipping a
    sentence that contradicts the cards under it. ⭐ IT FIRED THE FIRST TIME IT
    RAN: Design's lead says "three of the eight" and her own items carry FOUR.
    See the block's own note in `core` for what changed and why.
  · THE PAIRS ARE ASSERTED. Melting against freezing, and photosynthesis
    against respiration, must be present and must carry OPPOSITE flags, or the
    closing panel's "run a change backwards and the energy runs backwards with
    it" is a claim the instrument does not support.

── THE FLAGS ──────────────────────────────────────────────────────────

⚑ flag 9 — "THERE IS NO SUCH THING AS COLD" STAYS, STATED FLATLY. ACCEPTED as
drawn. It is correct — cold is the absence of energy and not a substance — and
NOTES calls it "the strongest sentence in the unit", which is the reason to
keep it rather than a reason to hedge it. Hedging it would leave a student
holding exactly the belief `ENER-05` names.

⚑ flag 10 — AMMONIUM NITRATE COLD PACKS REACHING "NEAR 0 °C" stay in the
stretch, as drawn. A commercial instant pack takes water down by roughly 15–20
degrees from room temperature, so "near 0 °C" is the right order and is written
as an approximation rather than as a reading.

⚑ flag 11 — PHOTOSYNTHESIS AS "THE LARGEST ENDOTHERMIC PROCESS ON EARTH" stays,
as drawn. Defensible on any accounting: it is the input to the entire carbon
cycle, and the stretch paragraph makes the argument rather than asserting the
superlative on its own.

⚑ `#s-compare`, NOT `#s-sort`. Design's `RAIL` uses the anchor `s-compare` with
the short label SORT, and `docs/ks3/rail-manifest.md` records the anchor. The
built rail is asserted against that file stop for stop (MRB-249), so the anchor
is hers and not the label's.
"""

# ── the eight changes (Design's `ITEMS`) ────────────────────────────────
#
# ⚠️ `endo` IS THE ANSWER AND IT REACHES NO MARKUP AS A MARK. It is read at
# build time by `r_energy_sorter`, which uses it three ways: to choose which
# authored verdict line the card opens with, to derive the count the lead
# claims, and to assert that each `why` names the right one of the two words
# first. Nothing here paints a control green or red — only the ladder marks.
#
# ⚠️ THE ORDER IS DESIGN'S AND IT IS NOT ALPHABETICAL. The pairs are separated
# on purpose: melting is item 6 and freezing item 7, photosynthesis item 4 and
# respiration item 5, so a student meets each one and commits to it before the
# other arrives to contradict them.
_ITEMS = [
    {"id": "i1", "name": "Burning natural gas", "where": "a hob",
     "endo": False,
     "why": "Combustion is exothermic, always. The whole reason for burning "
            "anything is the energy it gives out."},
    {"id": "i2", "name": "Thermal decomposition of copper carbonate",
     "where": "a Bunsen", "endo": True,
     "why": "Endothermic. The Bunsen has to keep running: take the flame away "
            "and the reaction stops, because it can only proceed while energy "
            "is being supplied. That is why the decompositions you did with a "
            "Bunsen all needed the flame kept on."},
    {"id": "i3", "name": "Neutralising an acid with an alkali",
     "where": "a beaker", "endo": False,
     "why": "Exothermic — the mixture warms by several degrees. You measured "
            "this in the acids unit without naming it."},
    {"id": "i4", "name": "Photosynthesis", "where": "a leaf", "endo": True,
     "why": "Endothermic, and the biggest one on the planet. The energy comes "
            "from sunlight, which is why a plant in the dark cannot do it "
            "however much carbon dioxide and water it has."},
    {"id": "i5", "name": "Respiration", "where": "every living cell",
     "endo": False,
     "why": "Exothermic. It is the reverse of photosynthesis, so it releases "
            "what photosynthesis stored — and it is why a crowded room warms "
            "up."},
    {"id": "i6", "name": "Ice melting", "where": "a drink", "endo": True,
     "why": "Endothermic. Melting takes energy in, taken from the drink — "
            "which is exactly how the ice keeps it cold, as you worked out "
            "last lesson."},
    {"id": "i7", "name": "Water freezing", "where": "a freezer",
     "endo": False,
     "why": "Exothermic. Freezing is melting run backwards, so the energy "
            "runs backwards too: the water gives energy out, and the freezer "
            "has to carry it away. That is the heat coming off the back of "
            "the appliance."},
    {"id": "i8", "name": "Ammonium nitrate dissolving", "where": "a cold pack",
     "endo": True,
     "why": "Endothermic, strongly enough to be sold as a first aid device. "
            "Not every dissolving is — some warm up — but this one takes in "
            "enough energy to bring water close to freezing."},
]

# ── the three judgements (Design's `USES`) ──────────────────────────────
_USES = [
    {"id": "use-coldpack", "correct": "b",
     "q": "A sports cold pack is squeezed and goes cold in seconds. Why can "
          "it only be used once?",
     "options": [
         {"id": "a", "label": "The chemicals are used up"},
         {"id": "b", "label": "The dissolving cannot be reversed inside the "
                              "bag"},
         {"id": "c", "label": "The bag leaks"},
     ],
     "answer": "Because the change cannot be undone in the packet. To reset "
               "it you would have to evaporate the water off and recover the "
               "solid, which needs a heat source and an open container. "
               "Compare the reusable hand warmer from last lesson, which "
               "resets by boiling — the difference is whether the reverse "
               "change is practical, not whether it is possible."},
    {"id": "use-fuel", "correct": "b",
     "q": "Would an endothermic reaction be any use as a fuel?",
     "options": [
         {"id": "a", "label": "Yes, a very efficient one"},
         {"id": "b", "label": "No — it takes energy in rather than giving it "
                              "out"},
         {"id": "c", "label": "Only in an engine"},
     ],
     "answer": "No. A fuel is something you burn to get energy out, and an "
               "endothermic reaction does the opposite: you would have to "
               "keep supplying energy to make it run, and get nothing back. "
               "Endothermic reactions are useful for cooling, for storing "
               "energy and for taking things apart — not for powering "
               "anything."},
    {"id": "use-conservation", "correct": "b",
     "q": "A student claims an endothermic reaction breaks the law of "
          "conservation of energy, because energy disappears.",
     "options": [
         {"id": "a", "label": "They are right"},
         {"id": "b", "label": "They are wrong — the energy is stored in the "
                              "products"},
         {"id": "c", "label": "The law does not apply to chemistry"},
     ],
     "answer": "Wrong, and instructively so. The energy has not disappeared: "
               "it has been taken out of the surroundings and stored in the "
               "new substances, where a thermometer cannot see it. Run the "
               "reaction backwards and it comes out again. Nothing is lost — "
               "the accounting simply moved to a place the instrument does "
               "not read."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 236 character for character.
    "slug":        "endothermic-reactions",
    "title":       "Endothermic reactions",
    "discipline":  "chemistry",
    "unit":        "energy-changes-in-reactions",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.ENER.02` clause `b` — see `ks3_data/substatements.py`.
    "covers":      ["KS3.C.ENER.02b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "substances-and-reactions", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ THIS LESSON CANNOT BE READ WITHOUT c7-02, and not merely as a
    # convention: half the sorter's cards are exothermic, the reusable hand
    # warmer is quoted by name in use 1, and the whole page is written as a
    # mirror image. NOTES-C7 §2 also cross-links B7 and B8 for photosynthesis
    # and respiration, and C5-02 for thermal decomposition; all three are
    # `references`, because a student who has not done them can still sort the
    # card from what it says.
    "requires":    ["exothermic-reactions"],
    "assumes":     [],
    "references":  ["the-photosynthesis-reaction", "aerobic-respiration",
                    "thermal-decomposition", "changes-of-state"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two powders, both at room temperature, stirred together "
                    "in a beaker. Thirty seconds later the beaker is cold "
                    "enough to freeze it to a wet bench.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, matching `docs/ks3/rail-manifest.md` stop
    # for stop (MRB-249). Note `s-compare` carrying the short label SORT —
    # hers, and the anchor is what the gate reads.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "The cold beaker", "done_when": "committed"},
        {"anchor": "s-compare", "short": "SORT",
         "label": "Eight changes", "done_when": "all_eight_sorted"},
        {"anchor": "s-uses",    "short": "USES",
         "label": "Cold on demand", "done_when": "all_three_decided"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Making cold", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ "BOTH AT 20 °C, BOTH DRY" IS THE DOOR THIS HOOK CLOSES. Without it,
    # "one of them was in the fridge" is not a wrong answer, it is an untested
    # one — and the whole page depends on nothing having been cooled.
    "phenomenon": {
        "kind": "narrative",
        "title": "Nothing was cooled. Nothing was refrigerated. The beaker got "
                 "cold on its own.",
        "prompt": "Citric acid and sodium hydrogencarbonate, both at 20 °C, "
                  "both dry, are stirred into water. The thermometer falls to "
                  "12 °C and keeps going. Put a drop of water under the "
                  "beaker first and it freezes the beaker to the bench.",
        "commit": "Where has the energy gone?",
        "options": [
            "It was destroyed by the reaction",
            "The reaction took it in from the surroundings",
            "It escaped as an invisible gas",
            "There was never any energy there to begin with",
        ],
        "reveal": "Into the reaction. This one needs energy to proceed, and "
                  "it takes it from the nearest available source — the water, "
                  "the beaker, the bench and the air. Those things lose "
                  "energy, so they get colder, and the thermometer reports "
                  "it. A change that <strong>takes energy in</strong> from "
                  "its surroundings is <strong>endothermic</strong>. It is "
                  "the mirror image of last lesson, and it is far rarer.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ EVERY JOIN RESOLVES AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248).
    #
    # ⊖ NOTES-C7 §5 proposes `think-reveal-absence` for `ENER-05`. No
    # `think-reveal-*` id can be emitted from a lane, so the join names the
    # ACTIVITY that owns both the commitment and the reveal.
    #
    # ⊖ NOTES also proposes `rung-2` / `rung-2-feedback` for `ENER-06`. A
    # ladder rung is not a name the built page carries — the ladder emits no
    # per-rung id — so that join could never resolve. It is re-pointed at the
    # place the belief is actually taken apart, which is a better site anyway:
    # the SORTER puts melting and freezing three rows apart and then the
    # closing panel names the pair. `sort-eight` is the instrument's own
    # `data-activity`; `sort-close` is an `id` this lesson authors and
    # `r_energy_sorter` emits on the closing panel.
    "misconceptions": [
        {"id": "ENER-05",
         "statement": "An endothermic reaction produces cold.",
         "elicited_by": "think-commit-cold",
         "confronted_by": "think-commit-cold"},
        {"id": "ENER-06",
         "statement": "Melting and freezing both take energy in, because both "
                      "involve ice.",
         "elicited_by": "sort-eight",
         "confronted_by": "sort-close"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An <strong>endothermic</strong> change takes energy in from "
                 "its surroundings, so the surroundings get colder. The "
                 "thermometer falls, and nothing has been refrigerated."},
        {"type": "explainer",
         "text": "Both kinds obey the same law. Energy is never created and "
                 "never destroyed — it is transferred. Exothermic moves it "
                 "out of the chemicals and into the surroundings; endothermic "
                 "moves it the other way. <strong>The only question is which "
                 "direction.</strong>"},

        # #s-compare — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ NO NARRATION OF THE CONTROLS (§5A). The heading IS the ask —
        # "Exothermic or endothermic? The thermometer decides" — and it is a
        # better instruction than any line under it.
        {"type": "energy-sorter", "id": "sort-eight", "anchor": "s-compare",
         "eyebrow": "Your turn · eight changes",
         "heading": "Exothermic or endothermic? The thermometer decides.",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} sorted", "start": 0,
                          "total": 8},
         # ⚑ Design's live line reads "{n} of 8 sorted. Three of the eight are
         # endothermic, and two of those three are changes you have already
         # met under another name." The COUNT is the head-row readout and the
         # teaching half is the block's lead.
         #
         # ⭐ AND THE NUMBER IN IT IS WRONG ON HER PAGE. Her `ITEMS` carry FOUR
         # endothermic changes, not three — thermal decomposition,
         # photosynthesis, ice melting and ammonium nitrate dissolving — and
         # every one of the four is correctly classified. NOTES-C7 does not
         # flag it, and nothing in a browser would show it: the sentence sits
         # above the cards and a student counting them would be the first to
         # find out.
         #
         # Found by `r_energy_sorter`'s derived count, which is the §5A
         # assertion this block exists to carry. The standing build law applies
         # in its ordinary direction here — the DATA is right and the SENTENCE
         # is wrong — so the sentence changed. "Three of those four" is derived
         # too: decomposition was met in C5, photosynthesis in B7 and melting
         # last lesson; the cold pack is the only one that is new.
         "prompt": "Four of the eight are endothermic, and three of those "
                   "four are changes you have already met under another "
                   "name.",
         "endo_count_claim": 4,
         "options": [
             {"id": "exo", "label": "Exothermic"},
             {"id": "endo", "label": "Endothermic"},
         ],
         "verdict_exo": "Exothermic — the surroundings warm.",
         "verdict_endo": "Endothermic — the surroundings cool.",
         # The pairs the closing panel's rule depends on. Asserted at build
         # time to be present and to carry OPPOSITE flags.
         "pairs": [["i6", "i7"], ["i4", "i5"]],
         "items": _ITEMS,
         "close_id": "sort-close",
         "close_title": "Look at how lopsided that list is.",
         "close": [
             "Most changes give energy out. Endothermic ones are the "
             "exceptions, and they tend to be the ones that need something "
             "driving them — a Bunsen under a carbonate, sunlight falling on "
             "a leaf, or a solid pulling itself apart as it dissolves.",
             "Notice the pairs. Melting is endothermic and freezing is "
             "exothermic; photosynthesis is endothermic and respiration is "
             "exothermic. <strong>Run a change backwards and the energy runs "
             "backwards with it, by exactly the same amount.</strong>",
         ]},

        {"type": "key-fact", "ref": "which-direction"},

        # #s-uses — three judgements. Light `ks3-block` → `check`.
        {"type": "energy-uses", "id": "uses-cold", "anchor": "s-uses",
         "eyebrow": "Three judgements",
         "heading": "Cold on demand",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 3},
         "uses": _USES},

        # ⊖ NOT A RAIL STOP. Design's own `RAIL` does not carry `#s-words`.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. If "
                 "you cannot say it, you do not know it yet.",
         "terms": ["Endothermic", "Exothermic", "Conservation of energy",
                   "Photosynthesis", "Dissolving"]},

        {"type": "misconception", "id": "think-commit-cold",
         "anchor": "s-think", "targets": "ENER-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. NOTES-C7 §6 declares no figure anywhere in the unit.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "which-direction",
         "text": "Endothermic changes take energy in from the surroundings, "
                 "so the temperature falls. Exothermic changes give it out "
                 "and the temperature rises. Reverse a change and you reverse "
                 "its energy transfer.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-cold",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-05",
         "prompt": "The beaker genuinely does get cold. Commit before you "
                   "read on.",
         # MRB-177 / MRB-278: 11, 13, 5 and 12 words. The correct option is
         # index 1 and clears the next longest by one word, so nothing here
         # can be answered on shape. Design's set, unchanged.
         "options": [
             "Right — it makes cold and releases it into the beaker",
             "Wrong — there is no such thing as cold; the reaction removes "
             "energy",
             "Right, because the temperature falls",
             "Wrong — the beaker only feels cold, it is not really colder",
         ],
         "reveal": [
             "There is no such substance as cold. Cold is not a thing that "
             "can be made, pumped or released — it is simply the absence of "
             "energy. The reaction did not produce anything; it <strong>took "
             "energy away</strong>, and what is left behind has less than it "
             "did.",
             "The same correction applies to a fridge, which does not make "
             "cold but moves energy out of the food and dumps it out of the "
             "grille at the back. <strong>Every temperature change is energy "
             "going somewhere. Naming the direction is the whole of this "
             "unit.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # ⚑ MRB-278 · ANSWER POSITION. This lesson holds index 1 and index 0 of
    # C7's level eight. Only the ORDER moves on the recall rung — Design's
    # apply rung already sits at index 0 — and every `feedback` key is re-keyed
    # to the index its own option now sits at.
    "ladder": {
        "recall": {
            "q": "What happens to the temperature of the surroundings during "
                 "an endothermic change?",
            "options": [
                "It rises, because energy is released",
                "It falls, because energy is taken in by the reaction",
                "It stays the same",
                "It falls, because cold is produced by the reaction",
            ],
            "answer": 1,
            "feedback": {
                0: "That is exothermic — the previous lesson.",
                2: "If nothing changed there would be nothing to measure. The "
                   "thermometer falls.",
                3: "The direction is right but the reason is wrong. Cold is "
                   "not produced; energy is removed.",
            }},
        # The one that catches people, and it is `ENER-06` at the ladder: two
        # opposite changes that both involve ice. 10, 8, 7 and 8 words —
        # nothing is longest by four or by 1.4×. Design's set, unchanged.
        "apply": {
            "q": "Melting is endothermic. What does that tell you about "
                 "freezing?",
            "options": [
                "It is exothermic — the same energy comes back out",
                "It is also endothermic, because both involve ice",
                "It involves no energy change at all",
                "It depends on how cold the freezer is",
            ],
            "answer": 0,
            "feedback": {
                1: "They are opposite changes, so the energy travels in "
                   "opposite directions.",
                2: "A freezer has to remove energy continuously. That energy "
                   "is coming out of the water.",
                3: "The direction of the transfer is fixed. The freezer "
                   "temperature affects the rate, not the direction.",
            }},
        "explain": {
            "q": "Two powders at room temperature are stirred into water and "
                 "the temperature falls to 12 °C. Explain what has happened "
                 "in terms of energy, and why it does not break the law of "
                 "conservation of energy.",
            "field_label": "Your explanation",
            "placeholder": "The temperature fell because…",
            "success": [
                "Says the reaction is endothermic.",
                "Says energy has been taken in from the surroundings.",
                "Says the surroundings include the water, beaker and air, "
                "which therefore cool.",
                "Says the energy is now stored in the products.",
                "Says no energy has been destroyed — only transferred.",
            ]},
        "produce": {
            "q": "A designer wants a cold pack that can be reused "
                 "indefinitely. Explain what the chemistry would have to "
                 "allow, and why the ammonium nitrate pack cannot do it.",
            "field_label": "Your answer",
            "placeholder": "For a pack to be reusable the change would have "
                           "to…",
            "success": [
                "Says the change would have to be reversible.",
                "Says reversing it would release the energy that was taken "
                "in.",
                "Says the reverse change would need energy supplied from "
                "outside, such as heating.",
                "Says the ammonium nitrate would have to be recovered from "
                "solution by evaporating the water.",
                "Says that cannot be done inside a sealed bag, unlike the "
                "hand warmer which resets by boiling.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "An endothermic change takes energy in from its surroundings, "
                "so the temperature falls. Thermal decomposition, "
                "photosynthesis, melting and many dissolvings are "
                "endothermic; most other changes are exothermic. Energy is "
                "never created or destroyed in either case — only "
                "transferred, and reversing a change reverses the transfer.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Flags 10 and 11 both live here and both are KEPT byte-identical.
    "stretch": [
        {"type": "explainer", "id": "cold-packs",
         "text": "Instant cold packs in a first aid kit are a sealed bag of "
                 "ammonium nitrate with a pouch of water inside it. Squeeze "
                 "the pack, the pouch bursts, the ammonium nitrate dissolves, "
                 "and the temperature drops to near 0 °C within seconds — no "
                 "freezer, no electricity, and it works on a mountainside. It "
                 "is a single-use device because the dissolving cannot be "
                 "undone in the bag."},
        {"type": "explainer", "id": "photosynthesis-banks-it",
         "text": "The largest endothermic process on Earth is "
                 "photosynthesis, and it runs on sunlight. Every joule stored "
                 "in a leaf, and therefore in every food, every fuel and "
                 "every living thing, was taken in by an endothermic reaction "
                 "powered by a star. The exothermic reactions that follow — "
                 "respiration, combustion, digestion — are all spending what "
                 "photosynthesis banked. The whole carbon cycle is one "
                 "endothermic reaction feeding an enormous number of "
                 "exothermic ones."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The first five `term` strings match the `keyword` block's `terms` BYTE
    # FOR BYTE.
    "vocabulary": [
        {"term": "Endothermic",
         "definition": "A change that takes energy in from its surroundings, "
                       "so the surroundings get colder.",
         "note": "Nothing is refrigerated and no cold is made. Energy is "
                 "removed."},
        {"term": "Exothermic",
         "definition": "A change that gives energy out to its surroundings, "
                       "so the surroundings get warmer.",
         "note": "Reverse an endothermic change and you get an exothermic "
                 "one, by exactly the same amount."},
        {"term": "Conservation of energy",
         "definition": "Energy is never created and never destroyed. It can "
                       "only be moved from one store to another.",
         "note": "An endothermic reaction does not lose energy — it stores it "
                 "where a thermometer cannot read it."},
        {"term": "Photosynthesis",
         "definition": "The reaction in which a plant uses light energy to "
                       "build glucose from carbon dioxide and water. It is "
                       "endothermic.",
         "note": "This is why a plant in the dark cannot photosynthesise "
                 "however much water and carbon dioxide it has."},
        {"term": "Dissolving",
         "definition": "A solute spreading through a solvent to make a "
                       "solution. Some dissolvings take energy in and some "
                       "give it out.",
         "note": "Ammonium nitrate takes enough in to bring water close to "
                 "freezing."},
        {"term": "Reversible change",
         "definition": "A change that can be run backwards. Doing so reverses "
                       "the direction of its energy transfer as well."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚑ NEW PROSE, reported to the commander (contract §16).
    #
    # ⊖ NO SAFEGUARDING BLOCK. Nothing here touches a student's own body,
    # health or circumstances in the safeguarding sense.
    #
    # ⊕ A `safety_note` IS earned, and it is the one hazard this page has that
    # no other page in the unit does: the cold pack in the stretch layer is a
    # real object a student can find in a first aid kit, and something at 0 °C
    # held against skin will damage it. It adds to the method rather than
    # withdrawing anything the lesson taught.
    "safety_note": "An instant cold pack is a real first aid device and gets "
                   "cold enough to injure skin it is held against directly. "
                   "It goes on over clothing or a cloth, for short spells, "
                   "and a used one is thrown away rather than opened.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why cold is not a substance?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Energy level diagrams for endothermic changes, and bond "
                   "breaking as the energy-absorbing half of every reaction.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
