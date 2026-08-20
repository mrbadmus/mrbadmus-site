"""C2 L1 — The atom: Dalton's model (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-01-the-atom-daltons-model.dc.html` (774 lines),
and its measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §2.
Schema per architecture.md §4.8 as amended by §4.8.1 and §4.8.2.

Every student-facing string below is byte-identical to the approved page. The
named constants (`RAIL`, `CLAIMS`, `OBS`, `ZOOM`, `RUNGS`, `SELF_RUNGS`) were
lifted with `node tools/extract_design_payload.js`; the strings that live
INSIDE `renderVals()` — the hook options, the gate prompt, the think options,
the three branches of the model note, the progress formats and the two button
labels — were lifted from the line ranges the payload map records, because a
lift that copies only the top-level constants loses them all.

── What this record does that Design's page does not ────────────────────

1. **`#s-think` is a rail stop that ticks** (contract R1). The block asks for a
   commitment and gates a reveal behind it, which is a `predict`, and MRB-208
   says the rail is completion-based.

2. **The `#s-think` reveal is TWO paragraphs**, which the list form of `reveal`
   renders on Design's own card-on-ink panel.

3. **The gate's options are not authored twice.** Design's commit gate offers
   the three claim texts themselves, lettered A–C. `options_from: "claims"`
   reads them out of `claims[]` rather than storing a second copy of three
   science-bearing sentences — a second copy is a second place to drift.

── What is reproduced rather than corrected ────────────────────────────

* **`#s-model` ticks on TWO PRESSES IN ANY DIRECTION**, including switching a
  claim back on (`touched >= 2`, map §2.4). Lenient, deliberate, and not
  tightened: turning one off and back on is itself the investigation.
* **`#s-scale` needs all five levels reached by stepping IN.** `seenZoom` seeds
  level 0 and only the in-button adds to it, so `start` > 0 would make the
  stage unreachable without backing out and climbing again. Reproduced as
  drawn, with `start: 0`.
"""

# ── Dalton's three claims ────────────────────────────────────────────────
# Lifted from CLAIMS (page lines 344–348). They are also the three options of
# the commit gate, which is why the gate reads them from here.
#
# ⚑ NOTES flag 1 is Mide's: Dalton's own list is longer and includes "all
# matter is made of atoms". Whether three is the right number for KS3, and
# whether these are the three, is a science-gate question.
CLAIMS = [
    {"id": "kinds",
     "text": "All atoms of one element are the same as each other, and "
             "different from the atoms of every other element."},
    {"id": "solid",
     "text": "Atoms cannot be broken into anything smaller, and cannot be "
             "created or destroyed."},
    {"id": "ratio",
     "text": "When elements combine, their atoms join in simple whole-number "
             "ratios."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 167 character for character.
    "slug":        "the-atom-daltons-model",
    "title":       "The atom: Dalton's model",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    "covers":      ["KS3.C.AEC.01"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter points back at C1's particle model (page line 307) and
    # forward to Elements (313).
    "requires":    ["particle-model"],
    "assumes":     [],
    "references":  ["elements"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "People tried to turn lead into gold for fifteen hundred "
                    "years and never once managed it. What would have to be "
                    "true for that to be impossible?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, from the page's own RAIL constant (336–342). `done_when`
    # names the condition the page's own tick function checks (606–614).
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",  "label": "Lead into gold",
         "done_when": "committed"},
        {"anchor": "s-model", "short": "MODEL", "label": "Switch a claim off",
         "done_when": "two_claims_touched"},
        {"anchor": "s-scale", "short": "SCALE", "label": "How small",
         "done_when": "all_levels_seen"},
        {"anchor": "s-think", "short": "THINK", "label": "One copper atom",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Page 82–104; options at 635–639, reveal at 100.
    #
    # ⚑ NOTES flag 4 is Mide's: "fifteen hundred years" and an argument from a
    # long documented failure. Nuclear transmutation does turn lead into gold
    # and is not chemistry; the page hedges with "nothing you can do in a
    # flask" and the stretch layer draws the boundary. Confirm the hedge.
    "phenomenon": {
        "kind": "narrative",
        "title": "Fifteen centuries of failure is a result.",
        "prompt": "Alchemists were not fools. They were careful, they kept "
                  "records, and they had furnaces, acids and time. They "
                  "dissolved lead, burned it, mixed it with everything "
                  "available — and not one of them ever produced a single "
                  "grain of gold.",
        "commit": "What would explain a failure that complete?",
        "options": [
            "They were not skilled enough, and modern equipment would manage "
            "it",
            "Lead and gold are made of different kinds of particle, and no "
            "reaction changes one kind into another",
            "Gold is heavier, so more material would be needed",
            "They were kept secret whenever it worked",
        ],
        "reveal": "Lead is built from one kind of particle and gold from "
                  "another, and nothing you can do in a flask changes one kind "
                  "into the other. In 1803 John Dalton wrote that idea down "
                  "properly, and modern chemistry starts there.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The statement is the PAGE's line (196), stored WITHOUT its curly
    # quotes — the renderer adds them (b1-02's precedent).
    "misconceptions": [
        {"id": "ATOM-01",
         "statement": "A copper atom is a tiny bit of copper — orange, shiny, "
                      "and it conducts electricity.",
         "elicited_by": "think-commit-copper",
         "confronted_by": "think-commit-copper"},
        # ⊕ MRB-248 — `elicited_by` named `ladder-r2`, which is how the author
        # referred to the apply rung and is not a name the document carries: a
        # rung is emitted inside the ladder's section and has no id of its own.
        # The rung IS the elicitation — "Two of Dalton's three claims are now
        # known to be wrong. Why is his model still taught?" makes the student
        # commit, and all three distractors are versions of this belief — so
        # the place is real and only the name was wrong. The ladder's section
        # is emitted as `s-ladder`, which is what a browser can reach. Same
        # shape and same fix as `BODY-06` under MRB-244.
        {"id": "ATOM-02",
         "statement": "A model that turns out to be wrong about something has "
                      "been disproved and should be discarded.",
         "elicited_by": "s-ladder",
         "confronted_by": "stretch-boundary"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "You already have a particle model: everything is made of "
                 "particles, too small to see, always moving. It explained "
                 "melting, pressure and diffusion. It said nothing at all "
                 "about there being different <em>kinds</em> of particle — and "
                 "without that, nothing in chemistry works."},

        # #s-model — the flagship. ⚠️ A LIGHT `.ks3-block` (→ `check`). It
        # looks like a bench and it is not one; `practical` would paint the
        # whole instrument on ink and resolve every text token wrong.
        {"type": "claim-switch", "id": "switch-a-claim-off", "anchor": "s-model",
         "eyebrow": "The model · switch a claim off",
         "heading": "Dalton made three claims. Take one away.",
         "head_counter": {"zero": "All three claims on",
                          "format": "{n} switched off", "total": 3},
         "demand": "predict",
         "targets": "ATOM-02",
         "prompt": "A model earns its place by explaining things that were "
                   "already known. Switch a claim off and watch which "
                   "observations it takes down with it.",
         "gate": {"prompt": "Commit first. Which claim do you think the other "
                            "two could not manage without?",
                  "options_from": "claims"},
         "labels": {
             "claims": "Dalton's claims — tap to switch one off",
             "observations": "Things known before Dalton wrote",
             "on": "ON",
             "off": "OFF",
         },
         "verdicts": {"alive": "explained", "dead": "no longer explained"},
         "claims": CLAIMS,
         # Four observations that were all known before Dalton wrote, each
         # with the sentence that REPLACES it when a claim it needs goes off.
         # Page lines 350–363.
         "observations": [
             {"id": "o1",
              "text": "No amount of heating, dissolving or burning ever turned lead into gold.",
              "needs": ["kinds", "solid"],
              "fail": "If atoms could change kind or be taken apart, there is no reason this should never have worked."},
             {"id": "o2",
              "text": "Water from a river, from the sea and from a laboratory always contains exactly the same proportion of hydrogen to oxygen by mass.",
              "needs": ["kinds", "ratio"],
              "fail": "Without identical atoms joining in fixed ratios, the proportions would come out differently every time."},
             {"id": "o3",
              "text": "Seal a reaction in a flask and its mass is exactly the same afterwards as before.",
              "needs": ["solid"],
              "fail": "If atoms could be destroyed or made, mass would drift up or down and nobody would expect it to balance."},
             {"id": "o4",
              "text": "Copper and oxygen combine to make one compound in one ratio, and a second compound in another — but never anything in between.",
              "needs": ["ratio"],
              "fail": "Without whole-number ratios there is nothing to stop every proportion in between existing too."},
         ],
         # The three branches of `modelNote` (594–602). `some_broken` carries
         # Design's inline plural as a named slot, so "1 claim leaves" and
         # "2 claims leaves" both compose byte-identically.
         "note": {
             "all_on": "All three claims on, and every observation is "
                       "accounted for. That is what a model is for: not being "
                       "true, but paying its way.",
             "none_broken": "Nothing has broken — which would mean that claim "
                            "was doing no work. Look again: every one of "
                            "Dalton’s three is holding something up.",
             "some_broken": "Switching off {n} {claim} leaves {broken} of the "
                            "four observations with no explanation at all. A "
                            "claim earns its place by what falls over without "
                            "it.",
             "claim_word": {"one": "claim", "many": "claims"},
         },
         # Design's own rule, and lenient on purpose (map §2.4).
         "done_at": 2},

        {"type": "key-fact", "ref": "smallest-particle"},

        # #s-scale — ink-dark practical. Five drawings, two buttons.
        {"type": "scale-zoom", "id": "how-small", "anchor": "s-scale",
         "eyebrow": "How small · zoom until you find one",
         "heading": "Small is not a strong enough word",
         "head_counter": {"format": "{n} of {total} steps", "total": 5,
                          "start": 1},
         "demand": "investigate",
         "prompt": "Start at a centimetre of copper wire and go closer. "
                   "Watch the scale on each step: the jumps get bigger as "
                   "you go down, because the distance between what a lens "
                   "can show you and the size of an atom is enormous.",
         # ⊕ MRB-257 phase 4 — the button said "Ten times closer" and only
         # the first two steps are. Level 2's note still says it, correctly,
         # because that step genuinely is ×10.
         "labels": {"out": "Back out", "in": "Go closer"},
         "alt": {"template": "A magnified view of copper at {scale}: "
                             "{label}."},
         "start": 0,
         # ZOOM, page lines 365–376, plus the `drawing` key naming which of the
         # five drawn scenes each level paints. The names are validated at
         # build time against `SCALE_DRAWINGS`.
         #
         # ⊕ MRB-257 phase 4 — TWO CORRECTIONS, and the first is MRB-251's
         # class exactly. The prompt read "Each step is ten times closer than
         # the last" over steps of ×10, ×10, ×100 and ×10,000 — the same
         # defect as b10-02's "a thousandfold drop per zoom step" over
         # ×80,000 / ×3.3 / ×3 / ×7,000, and it resolves the same way: the
         # figures are what a student reads as evidence, so the figures stand
         # and the sentence goes. The replacement is the true claim and the
         # better teaching point — the jumps get bigger, which is precisely
         # why a zoom sequence needs stated magnifications rather than an
         # intuition about scale. Level 2's note still says "Ten times
         # closer" and is LEFT, because that step genuinely is.
         #
         # Second: the last level read 0.0000001 mm (0.1 nm) with "about a
         # hundred million would fit across that first centimetre". Both come
         # from an atom 0.1 nm across. A COPPER atom is 0.256 nm, so about
         # forty million fit across a centimetre — and a 0.1 nm field of view
         # would hold less than one atom, while the drawing is a lattice. The
         # level is now 0.000001 mm (1 nm), about four copper atoms across,
         # and the count is copper's.
         #
         # Third (⊕ MRB-269 finding 2): level 4 read 0.001 mm (1 µm) under
         # the label "Beyond any light microscope". Visible light's
         # diffraction limit is ~0.2 µm, so a 1 µm field is WITHIN reach —
         # the label contradicted the scale. The level is now 0.0001 mm
         # (0.1 µm), which is genuinely past the limit, so the label, the
         # caption and the note all stand as written.
         "levels": [
             {"scale": "1 cm across",
              "label": "A piece of copper wire",
              "drawing": "wire",
              "note": "A centimetre of wire. Solid, orange, bendable — everything you know about copper is true at this size."},
             {"scale": "1 mm across",
              "label": "The cut end, under a lens",
              "drawing": "grains",
              "note": "Ten times closer. Still copper, still orange. Nothing has changed except how much of it you can see."},
             {"scale": "0.1 mm across",
              "label": "Under a school microscope",
              "drawing": "scratches",
              "note": "This is about as far as the microscope from B1 reaches. Scratches and grains, and still no sign of anything smaller."},
             {"scale": "0.0001 mm across",
              "label": "Beyond any light microscope",
              "drawing": "beyond-light",
              # The canvas caption, drawn in mono at the centre of the frame.
              "caption": "past the reach of any light microscope",
              "note": "Light itself is too coarse to show anything at this scale. To go further you need electrons instead of light, and that machine was not built until the 1930s."},
             {"scale": "0.000001 mm across",
              "label": "Individual copper atoms",
              "drawing": "lattice",
              "note": "Atoms, stacked in a regular pattern. About forty "
                      "million of them would fit across that first "
                      "centimetre of wire."},
         ]},

        {"type": "misconception", "id": "think-commit-copper", "anchor": "s-think",
         "targets": "ATOM-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⊕ `card` ground, six for six across C2 — the unit's own choice against
    # the shipped `band` default. The 6px shadow / 25px body / 22px 26px
    # padding Design draws are NOT adopted: contract R3.
    "key_facts": [
        {"id": "smallest-particle",
         "text": "An atom is the smallest particle of an element. There are "
                 "about a hundred kinds, and no chemical reaction turns one "
                 "kind into another.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # ── #s-think · commit, then two paragraphs (contract R1) ────────────
        {"id": "think-commit-copper",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-01",
         "prompt": "Copper is orange, shiny, bendable and conducts. Commit to "
                   "how much of that a single copper atom has before you read "
                   "on.",
         "options": [
             "All of it — it is copper, just smaller",
             "The colour, but not the conducting",
             "None of it",
             "The conducting, but not the colour",
         ],
         "reveal": [
             "None of it. Colour is what happens when light meets a huge "
             "number of atoms together. Conducting is something that only "
             "makes sense when there is somewhere for the charge to go. "
             "Bending needs layers of atoms to slide over each other, and one "
             "atom has no layers.",
             "The properties of a substance belong to the crowd, not to the "
             "individual. What a copper atom has is a kind — it is a copper "
             "atom rather than a lead one — and a mass. Everything else about "
             "copper emerges when you put enough of them together.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # RUNGS 378–395, SELF_RUNGS 397–420. Every `correction` is science-bearing
    # and is lifted verbatim.
    "ladder": {
        "recall": {
            "q": "What is an atom?",
            "options": [
                "The smallest particle of an element",
                "The smallest particle of any substance",
                "A very small piece of a solid",
                "Anything too small to see with a microscope",
            ],
            "answer": 0,
            "feedback": {
                1: "Close, and it is the word \"element\" that does the work. "
                   "A particle of water is made of more than one atom.",
                2: "Gases and liquids are made of atoms too. The state has "
                   "nothing to do with it.",
                3: "A bacterium is too small for the naked eye and is not an "
                   "atom. Size is not the definition.",
            }},
        "apply": {
            "q": "Two of Dalton’s three claims are now known to be wrong. Why "
                 "is his model still taught and still used?",
            # ⊕ MRB-177, ruled 17 Aug 2026 — the three distractors now state
            # wrong RULES, in the same shape as the correct option. The
            # correct option and its index are unchanged.
            "options": [
                "It still explains everything it was built to explain, and "
                "the parts that are wrong are outside chemistry",
                "A model is kept while it is simple enough to teach, and "
                "swapped for the truth later on",
                "A model stays in use until someone replaces it, so a wrong "
                "model survives while no better one exists",
                "A model is only disproved by a perfect experiment, so "
                "faulty results leave it standing",
            ],
            "answer": 0,
            "feedback": {
                1: "It is not a simplified lie. Chemists use it, because for "
                   "chemical reactions it gives the right answer.",
                2: "It has been replaced, several times over, for the "
                   "questions it cannot answer. It is still the right tool "
                   "for reactions.",
                3: "The results were not faulty. Electrons and isotopes are "
                   "both real; Dalton was genuinely wrong about them.",
            }},
        "explain": {
            "q": "Explain why the failure of alchemy is evidence for Dalton’s "
                 "model, and say what alchemists would have had to be able to "
                 "do for the model to be wrong.",
            "field_label": "Your explanation",
            "placeholder": "For lead to become gold…",
            "success": [
                "Says lead and gold are made of different kinds of atom.",
                "Says a chemical change rearranges atoms but does not change "
                "what kind they are.",
                "Says that turning lead into gold would mean changing one "
                "kind of atom into another.",
                "Says that fifteen hundred years of careful failure is "
                "evidence, not just an absence of success.",
                "Says the model would be wrong if anyone ever did it "
                "chemically.",
            ]},
        "produce": {
            "q": "A student says: \"Dalton was wrong about atoms being "
                 "unsplittable, so his model should be thrown away.\" Reply to "
                 "them, using one thing the model still explains and one thing "
                 "it cannot.",
            "field_label": "Your reply",
            "placeholder": "Being wrong about one thing does not…",
            "success": [
                "Says a model is judged by what it explains, not by being "
                "completely true.",
                "Names something Dalton’s model still explains — fixed "
                "proportions, conservation of mass, or why alchemy failed.",
                "Names something it cannot explain — electricity from atoms, "
                "radioactivity, or atoms of one element with different masses.",
                "Says the model now has a known boundary rather than being "
                "discarded.",
                "Does not claim the later experiments were mistaken.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Dalton: everything is made of atoms; all atoms of one element "
                "are the same and different from every other element's; atoms "
                "are rearranged in reactions, never created, destroyed or "
                "changed into another kind. Two of those turned out to be not "
                "quite true, and the model is still the one you use.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ATOM-02's confrontation lives here: wrong in a way you can draw a line
    # around is how most good models end up.
    #
    # ⊕ MRB-244 — `anchor`, not `id`. This block was authored with the name on
    # the `id` key, which `_id_attr` documents as naming the ACTIVITY a block
    # renders; an explainer renders no activity, so the name was read by
    # nothing and emitted nowhere, and ATOM-02's `confronted_by` pointed at a
    # section that existed on the page and had no name in the document. It is
    # a SECTION anchor, which is what `anchor` means, and now it is one.
    "stretch": [
        {"type": "explainer", "anchor": "stretch-boundary",
         "text": "Dalton said atoms cannot be split. A century later J. J. "
                 "Thomson knocked pieces off them and found electrons, and it "
                 "turned out that atoms of the same element can have different "
                 "masses. Both of Dalton's claims were wrong. The model did "
                 "not get thrown away, because everything it was built to "
                 "explain is still explained by it — what happened is that it "
                 "got a boundary: <em>chemistry</em> never splits an atom or turns "
                 "one element into another, and that is exactly the range "
                 "Dalton was working in. Being wrong in a way you can draw a "
                 "line around is how most good models end up."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a model can be wrong and still be used?",
              "cta": "Ask about this lesson",
              "anchor": "s-model"},

    "ks4_becomes": "The nuclear atom, electron shells, and the experiments "
                   "that forced each change.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["scientific-attitudes", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
