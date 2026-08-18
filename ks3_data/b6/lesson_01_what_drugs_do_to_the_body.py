"""B6 L1 — What drugs do to the body (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b6/b6-01-what-drugs-do-to-the-body.dc.html` (618 lines), under
the MRB-220 build contract.

Every student-facing string is lifted byte-identical from that page except the
items listed under "What could not be lifted" and the six `vocabulary`
glosses, which the page does not draw at all. The four drugs, the five stage
titles, the three class cards and all four ladder rungs came out of
`node tools/extract_design_payload.js`; the static-markup prose — hook,
confrontations, key fact, key note, both layers and the foot line — was pulled
out of the page body by line number rather than retyped. On this unit that is
a safeguarding rule as much as an accuracy one.

── ⚠️ TONE IS A GATE, AND I CHANGED NOTHING ─────────────────────────────

NOTES-B6 §1 and `ks3_data/b6/__init__.py` both rule the register: clinical,
function-first, no scare copy, no reassurance copy, no euphemism, and **no
doses, thresholds or methods for any substance, legal or illegal**. A student
reading this page may be living with someone else’s addiction or their own.

Measured on the finished record, not asserted:

  * **The only quantity anywhere is the hook’s "Around 90 milligrams of
    caffeine".** It is a statement about what is already in a mug of coffee,
    not an amount to take, and it is Design’s (NOTES-B6 flag 2). No other
    number in this lesson is a quantity of any substance — "roughly one unit
    an hour" is a CLEARANCE rate for the liver, and "several litres in an
    hour" is water in the dose-response layer (flag 11).
  * **Nothing was softened, sharpened, or given a warning it did not have.**
    Two places tempt an author and both are left exactly as drawn: the
    nicotine `target` line calling addiction "a physical state of the nervous
    system rather than a weakness of character", and the think-again sentence
    that alcohol and nicotine "cause more illness and more deaths here than
    every illegal drug combined" (flag 10, deliberately unquantified).
  * **The support layer is not a warning and is not written as one.** It says
    what the lesson covers, where decisions belong, and who to ask. Lifted
    whole.

⚑ **FLAG 4 — PARACETAMOL AND THE LIVER — SHIPS AS WRITTEN, FOR MIDE.**
`DRUGS[paracetamol].elsewhere[0].effect` says a large dose damages liver
cells, that the damage can be permanent, and that **the person feels fine for
a day or two**; ladder rung 4 criterion 3 says it again. That last clause is
deliberately at KS3 because it is the one that saves a life. It is carried
byte-identical and it is not softened. `__init__.py` records it as settled;
this is the module that contains it, so it is flagged here too.

── `covers` is the SUB-ID, not the whole bullet ─────────────────────────

`KS3.B.HLTH.01` is the unit’s only statement — *"the effects of recreational
drugs (including substance misuse) on behaviour, health and life processes"* —
and `ks3_data/substatements.py` splits it three ways for B6. This lesson owns
**`KS3.B.HLTH.01a`**: what a recreational drug is, and how one acts on
behaviour, health and life processes once it is in the blood. It must NOT
claim `HLTH.01` whole — `alcohol-and-smoking` owns `b`,
`substance-misuse-and-decisions` owns `c`, and §5.7’s exactly-once rule would
fail the build on the overlap. The split is flagged in `substatements.py` as
the weakest-provenance mint in that file; that flag is the commander’s and is
not re-argued here.

── The flagship: stage 3 is the lesson ──────────────────────────────────

`#s-dose` is `route-tracer`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is MEASURED from Design’s own markup and matches the
table in `ks3_data/b6/__init__.py`.

⚖️ **STAGE 3 — *Once round the whole body* — IS THE WHOLE POINT AND IS ITS
OWN STAGE.** NOTES-B6 §2.1 says so in as many words: *"do not let a future
revision collapse stages 2 and 3 to save space."* Stage 2 says the dose is
dissolved in plasma and carries no address; stage 3 says the blood completes
the circuit in under a minute and offers the dose to every organ there is.
Those are two different claims — *it has no destination* and *it therefore
reaches all of them* — and it is the second that kills `DRUG-02`. They are
authored as two entries in `stages[]` with two separate bodies, and the
payload has no shape in which one could absorb the other: a renderer walks
`stages[]` in order and reveals one per press.

The tracer also gives no dose, no threshold and no timing for any of the four
substances. Design’s own foot line says that out loud, and it is carried.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-classes` came off the rail. Design draws FOUR stops and `#s-classes` ticks
on `s.step >= 5` (page line 447) — `#s-dose`’s predicate, verbatim, one
section to the left — and because `#s-classes` is an eyebrow, a display
statement, three static cards and a key fact, with no control, no commitment
and no field, the reading was that MRB-208’s completion rule ruled it out and
`ks3_parity.check_rail_reachable` would fail a `rule` section for carrying none
of the signals `doneByDom()` reads. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And Design’s `isDone()` states the tick condition. It is a rail-level function
and returns the identical expression for `#s-dose` and then for `#s-classes`.
The three classes are the payoff of following the dose to the end; the section
holds no control because the tracer already took the student’s commitment.
That is a MIRROR, resolved at rail level in `wireRail`’s `paint()`.

So the fourth stop is declared: anchor `s-classes`, `mirrors: "s-dose"`,
`done_when: "all_five_stages"` — `#s-dose`’s own predicate, named as borrowed,
and gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
b4-01’s `#s-parts`, c1-02’s `#s-matrix`, c1-05’s `#s-scale`, b3-01’s
`#s-nutrients` and b3-02’s `#s-limits` are restored the same way. The section
keeps its anchor, as it always did, so every hash link into it still works.

── What could not be lifted, and why ────────────────────────────────────

1. **The support layer’s EYEBROW.** Design heads the `ks3-layer ks3-support`
   block *"If any of this is about you or someone you know"*. `r_layer` takes
   its eyebrow as a positional argument and hard-codes `"Need a hand?"` for
   the support layer on every page in the key stage; there is no per-lesson
   override and R5 forbids authoring a key nothing reads. So the paragraph
   ships under `Need a hand?`.

   ⚑ **This is a DESIGN FLAG, not a tidy-up, and it is the one loss in this
   record that changes what a student is being offered.** "Need a hand?" is a
   study-support phrase; the block it now heads is a referral block about
   somebody’s drug use, and this is the first non-empty `support[]` in the key
   stage — every other lesson authors `"support": []`, so nothing has ever
   rendered under that heading before. The fix is a `support_heading` on the
   lesson, exactly as `connects_heading` already exists for the endmatter
   card, wired in `r_layer`. It is one line in the engine and it is not mine
   to write. **Reported, not worked around: the paragraph itself is carried
   byte-identical and no sentence of it was adjusted to fit the heading.**

2. **The class cards’ four parts become two.** Design draws each of the three
   as a mono `kind` eyebrow, a display `name`, an inset `does` panel and a
   body `examples` line. `r_rule`’s card is `term` + `gloss`. `name` and `kind`
   are joined with " · " — b4-01’s `Alveoli · Gas exchange — the only place`
   and b3-05’s `Mechanical digestion · Making pieces smaller` are the
   precedent, and it is Design’s own separator elsewhere on this page. `does`
   and `examples` are joined with a single space; both are complete sentences
   ending in a full stop, so they read as one paragraph and neither loses a
   byte. Nothing is dropped. What is given up is the inset panel that set
   `does` apart from `examples`.

3. **The key fact leaves Design’s band panel.** She nests it inside
   `#s-classes`; `r_rule` has no nested key-fact slot (only `r_comparison`
   does), so it renders as its own top-level block directly under the panel.
   `ground` is `card` because that is what Design paints it — `var(--ks3-card)`
   with the accent offset shadow, on the band section — and `card` is a valid
   `_GROUNDS` key. The words and the order are unchanged.

4. **⊕ RESOLVED (MRB-244) — the tracer’s three-state readout is intact.**
   Design’s `traceProgress` reads `not started` → `stage N of 5` →
   `all five stages`. `_head_counter` originally had a count shape with a
   bespoke zero (c2-01’s) and a two-state shape, and neither had a slot for a
   third label at the top of the count, so the closing state was given up and
   the fifth press read `stage 5 of 5`.

   The engine pass added `full` — the mirror of `zero` — in the same run, and
   this record authors it. All three states are Design’s again. Kept here
   rather than deleted because it is the useful half of the story: the loss
   was reported as a limitation of the shell, the shell was widened, and the
   authored key had to follow. **A widened engine is not a fixed page until
   some record actually takes the new key** — b6-01 shipped without it and
   read `stage 5 of 5` on a live page until this was noticed.

5. **Design draws TWO endmatter link cards; the engine emits one for the
   forward links.** "Before this lesson" (`b3-07`, `b1-05`) is `requires` and
   keeps its own card. "Connects to" (`b6-02`, `b4-04`) is `references` under
   `connects_heading`. Both survive; nothing is dropped.

6. **`ks4_links` gives way to `ks4_becomes`.** Design’s "At GCSE this becomes"
   card is authored prose and §4.8.1 D makes the two mutually exclusive.

7. **`vocabulary` is AUTHORED, and it is the only student-facing text here
   that is not Design’s.** She draws no keyword block on this page, so none of
   it reaches the lesson body; the terms reach a student as the unit page’s
   chips and the reading-age gate reads them as its exclusion list, which
   matters when "paracetamol", "stimulant" and "depressant" would otherwise
   count against the page. Five of the six definitions are page sentences
   verbatim or a page clause with its leading pronoun removed. b4-01 authored
   its seven the same way and for the same reason.

── The instrument payload, and which contract it was built against ──────

⚠️ **`docs/ks3/b6-inventory/PAYLOAD-SCHEMA.md` DOES NOT EXIST**, and when this
payload was written `build_ks3.py` contained no `r_route_tracer` either. So it
is authored against **NOTES-B6 §2.1**, which is the only written contract this
instrument has, extended only where the drawn page needs a key §2.1 does not
name — and in the shapes `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md`
established, so the engine finds nothing novel:

  * `drugs[]` — §2.1’s keys exactly: `id`, `label`, `name`, `klass`, `where`,
    `entry`, `target`, `elsewhere[{organ, effect}]`, `verdict`.
  * `stages[]` — NOT in §2.1, which gives only `step: 0..5`. The page holds the
    five titles in `STEP_TITLES`, two shared bodies in `STEP_2` / `STEP_3` and
    a third inline, and takes the other two bodies from the selected drug
    (`bodies = [drug.entry, STEP_2, STEP_3, drug.target, …]`, page line 489).
    Authored as five records carrying either a shared `body` or a `body_from`
    naming the per-drug field. A renderer reads one or the other; a stage can
    carry both keys never, and the five are ordered.
  * the control and panel labels Design draws around the stages — `dose_label`,
    `next_labels`, `reset_label`, `elsewhere_label` — none of which §2.1 names
    and all of which are on the page.
  * `start_drug` is Design’s `startDrug` tweak prop, defaulted to her default.

⊕ **The engine pass landed `r_route_tracer` while this was being authored, and
the two contracts agree key for key.** Verified against it rather than assumed:
every name above is one the renderer reads, and its five validations —
≥2 drugs, the six required per-drug keys, non-empty `elsewhere` rows, exactly
five stages, and exactly one of `body` / `body_from` per stage — all pass on
this payload unchanged. The convergence is not luck; both were derived from
NOTES-B6 §2.1 and the same drawn page. Nothing was retro-fitted, and the
renderer's own docstring makes the same stage-3 argument this one does.

`docs/ks3/b6-inventory/PAYLOAD-SCHEMA.md` is still absent, so **§2.1 plus this
comment is the contract of record for `route-tracer` until the engine pass
writes it.**

⚑ For Mide’s science gate — NOTES-B6 §3 flags landing on THIS lesson:
  * flag 1 — *"A drug is any substance that changes the way the body works."*
    The definition all three lessons are built on, and the one that makes
    caffeine a drug. It is this page’s hook reveal, its key fact and its key
    note.
  * flag 2 — ~90 mg of caffeine in a mug of coffee. The lesson’s only quantity.
  * flag 3 — nicotine reaching the brain in about ten seconds.
  * flag 4 — paracetamol and the liver. Settled; see the tone section above.
  * flag 10 — alcohol and nicotine causing more illness and death in the UK
    than every illegal drug combined, stated without numbers on purpose.
  * flag 11 — the foxglove/digoxin dose-response layer, including *even water*
    at several litres in an hour.
  * flag 14 — **no diagrams and no figure slots.** Verified on this page: it
    contains no `<figure>`, no `ks3-figure`, no `img`, and its foot line names
    no slot. `figures` is `[]` and nothing is invented to fill it.

⚑ Two findings of my own, both reported rather than ruled on:

  A. **⊕ MRB-177 RULED, 17 Aug 2026 — rung 2’s distractors now state wrong
     RULES.** Measured with `verify_ks3.py`’s own `length_tell()`, the correct
     option was 22 words against a longest distractor of 10 and tripped both
     thresholds. Mide ruled the construct rather than the instance: the
     correct answer states a rule and the distractors stated one-clause wrong
     reasons, so the correct answer was longer by construction. His
     replacement distractors state wrong rules in the same shape, and length
     parity follows — 22 against 20 / 17 / 19. **The correct option, its
     index and the gate’s threshold are all unchanged.**

     ⛔ Superseded, kept: this finding used to read *"No distractor was
     rewritten and the correct option was not trimmed: rewriting a distractor
     changes what a marked question measures and MRB-177’s own register says
     that is Mide’s gate, not an author’s. It needs a `KNOWN_TELLS` entry —
     `("what-drugs-do-to-the-body", "ladder apply")` — or Mide’s ruling."*
     The ruling arrived; the register entry is now stale and the commander
     deletes it. `verify_ks3.py` is still not this module’s file to edit.

  B. **The page’s third wrong idea has no confrontation block and no id
     here.** The *Going further* layer names two beliefs and corrects both —
     that *poison* is a category of substance rather than a statement about
     quantity, and that *it is natural, so it must be gentle*. They are one
     belief in two sentences and they belong in the register as **`DRUG-07`**,
     which is outside this module’s allocation (`DRUG-01` and `DRUG-02`,
     nothing else, pre-allocated because B4’s parallel authors collided twice
     on `BREATH` ids). Not minted here. Reported for the register, with the
     statement in the report.

  C. **`ks3_key_audit.py B6` reports `entry` as read by nothing, and it is
     wrong.** `drugs[].entry` is stage 1's body and it IS read — by
     `r_route_tracer`'s `body_of()`, as `d[st["body_from"]]`, where
     `stages[0].body_from` is the string `"entry"`. The audit is a literal
     scan and cannot see through the indirection; `target` escapes only
     because some other renderer happens to read a key of that name. R5 says
     wire the read or drop the key, and the read exists, so the key stays.
     Renaming `entry` would silence the audit and break NOTES-B6 §2.1's key
     list and the renderer's own docstring, which names `entry` explicitly.
     Reported so the audit's blind spot is on the record rather than fixed by
     damaging the data.
"""

# ── the four drugs (page lines 338–379, via extract_design_payload.js) ───
#
# ⚠️ THE KEYS ARE NOTES-B6 §2.1's, character for character. That list is the
# only written contract this instrument has, so it is followed rather than
# improved on. `klass` keeps its k because `class` is a Python keyword, which
# is why Design spelled it that way too.
#
# `entry` is stage 1's body and `target` is stage 4's; the other three stage
# bodies are shared across all four drugs and live in `STAGES` below. Nothing
# in here is a dose, a threshold or a method, and nothing may be added that
# is — NOTES-B6 §1 makes that a gate, not a preference.
DRUGS = [{"id": "caffeine",
          "label": "Caffeine",
          "name": "Caffeine",
          "klass": "Stimulant",
          "where": "Coffee, tea, cola, energy drinks. Legal at any age, sold "
                   "in a café.",
          "entry": "Swallowed in a drink. It crosses the wall of the small "
                   "intestine into the blood within a few minutes.",
          "target": "It reaches the brain and blocks the chemical signal that "
                    "builds up through the day to make you feel sleepy. Nerve "
                    "cells go on firing readily, so you feel alert.",
          "elsewhere": [{"organ": "Heart",
                         "effect": "Beats faster. Two mugs is enough to "
                                   "measure the difference."},
                        {"organ": "Kidneys",
                         "effect": "Produce more urine, so more water leaves "
                                   "the body than you drank in the coffee."},
                        {"organ": "Stomach",
                         "effect": "Releases more acid, which is why coffee "
                                   "on an empty stomach can hurt."}],
          "verdict": "None of those three organs has anything to do with "
                     "feeling awake. They were simply on the route."},
         {"id": "paracetamol",
          "label": "Paracetamol",
          "name": "Paracetamol",
          "klass": "Painkiller",
          "where": "A legal medicine, bought without a prescription, with a "
                   "dose limit printed on the box.",
          "entry": "Swallowed as a tablet. It dissolves in the stomach and is "
                   "absorbed through the small intestine wall.",
          "target": "It acts on the pathways carrying pain signals, and on "
                    "the temperature control centre of the brain. It reduces "
                    "the pain and brings a fever down. It does nothing "
                    "whatever to the injury or infection causing them.",
          "elsewhere": [{"organ": "Liver",
                         "effect": "Breaks the drug down, at a fixed rate it "
                                   "cannot exceed. Too much in one day "
                                   "damages liver cells, and that damage can "
                                   "be permanent even though the person feels "
                                   "fine for a day or two."},
                        {"organ": "Kidneys",
                         "effect": "Filter the broken-down drug out into the "
                                   "urine. This is how the dose eventually "
                                   "leaves you."},
                        {"organ": "Every other organ",
                         "effect": "Received the drug and had no use for it."}],
          "verdict": "The tablet did not travel to your head. It went "
                     "everywhere, and your head is where there was something "
                     "for it to act on."},
         {"id": "nicotine",
          "label": "Nicotine",
          "name": "Nicotine",
          "klass": "Stimulant, strongly addictive",
          "where": "Cigarettes and vapes. Legal to sell to adults in the UK, "
                   "illegal to sell to under-18s.",
          "entry": "Inhaled. It crosses the thin alveoli walls straight into "
                   "the blood and reaches the brain in about ten seconds — "
                   "faster than any swallowed drug.",
          "target": "It triggers a release of the brain’s own reward "
                    "chemical. The brain adapts to expect that release, so "
                    "the wanting becomes a physical state of the nervous "
                    "system rather than a weakness of character. That "
                    "adaptation is what addiction is.",
          "elsewhere": [{"organ": "Heart",
                         "effect": "Beats faster, and blood vessels narrow, "
                                   "so blood pressure rises."},
                        {"organ": "Blood vessels in the skin",
                         "effect": "Narrow too, reducing blood flow to the "
                                   "surface — one reason wounds heal more "
                                   "slowly in smokers."},
                        {"organ": "Airways and lungs",
                         "effect": "Damaged by tar and by the other "
                                   "substances in smoke rather than by "
                                   "nicotine itself. Which substance does "
                                   "which damage is the subject of b4-04."}],
          "verdict": "Nicotine is the reason people keep smoking. The "
                     "substances that cause most of the harm are different "
                     "molecules travelling in the same smoke."},
         {"id": "alcohol",
          "label": "Alcohol",
          "name": "Alcohol (ethanol)",
          "klass": "Depressant",
          "where": "Beer, wine, spirits. Legal for adults in the UK, with age "
                   "limits on buying it.",
          "entry": "Swallowed. Unusually, it is absorbed straight through the "
                   "stomach wall as well as through the intestine, so it "
                   "arrives in the blood quickly.",
          "target": "It slows the signals passing between nerve cells "
                    "throughout the brain. Reactions lengthen, coordination "
                    "goes, and judgement goes first — which is the dangerous "
                    "part, because poor judgement is the thing least able to "
                    "notice itself.",
          "elsewhere": [{"organ": "Liver",
                         "effect": "Breaks it down at roughly one unit an "
                                   "hour, and nothing raises that rate. Years "
                                   "of heavy drinking scar the liver "
                                   "permanently."},
                        {"organ": "Kidneys",
                         "effect": "Produce more urine, so heavy drinking "
                                   "dehydrates you."},
                        {"organ": "Stomach",
                         "effect": "Lining irritated directly, which is why "
                                   "heavy drinking causes sickness."}],
          "verdict": "A depressant does not make you sad — it slows nerve "
                     "signals down. That is a statement about signalling "
                     "speed, not about mood."}]

# ── the five stages, in order (page lines 381–389 and 489) ──────────────
#
# ⚖️ STAGE 3 IS THE INSTRUMENT. `circuit` says the blood completes the round
# trip in under a minute and offers the dose to every organ there is; `blood`
# one above it says only that the dose is dissolved and carries no address.
# Two claims, not one, and it is the second that kills DRUG-02. NOTES-B6 §2.1:
# "do not let a future revision collapse stages 2 and 3 to save space."
#
# A stage carries EITHER a shared `body` or a `body_from` naming the field to
# read off the selected drug. Never both, and the order is the payload's.
STAGES = [{"id": "in",
           "title": "In",
           "body_from": "entry"},
          {"id": "blood",
           "title": "Into the blood",
           "body": "The drug is now dissolved in the blood plasma. Nothing "
                   "about the molecule says where it is supposed to go."},
          {"id": "circuit",
           "title": "Once round the whole body",
           "body": "Blood makes the full circuit in under a minute. Every "
                   "organ you have is offered this drug, whether it needs it "
                   "or not. There is no address on it and no way to send it "
                   "to one place."},
          {"id": "target",
           "title": "It acts where it fits",
           "body_from": "target"},
          {"id": "elsewhere",
           "title": "And everywhere else it reached",
           "body": "Listed below — and none of them is a fault in the drug."}]

# ── the three classes (page lines 391–398) ──────────────────────────────
#
# `name · kind` into `term`, `does` + " " + `examples` into `gloss` — see
# "What could not be lifted" 2. Every one of the six strings survives whole.
CLASS_CARDS = [{"term": "Stimulants · Speeds signals up",
                "gloss": "Nerve signals pass more readily, so heart rate and "
                         "alertness rise. Caffeine, nicotine. Prescribed "
                         "stimulants exist too, and they are prescribed "
                         "precisely because the effect is useful at a "
                         "controlled dose."},
               {"term": "Depressants · Slows signals down",
                "gloss": "Signals between nerve cells pass less readily, so "
                         "reactions, coordination and judgement all worsen. "
                         "Alcohol, and the sedatives used in anaesthetics. "
                         "Slower is not safer: most alcohol harm comes from "
                         "what a slowed nervous system then does."},
               {"term": "Painkillers · Blocks the message",
                "gloss": "The pain signal is reduced or blocked on its way to "
                         "the brain. The cause of the pain is untouched. "
                         "Paracetamol, ibuprofen, and morphine at the strong "
                         "end. Pain that stops being felt has not stopped "
                         "being a warning."}]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 133 character for character.
    "slug":          "what-drugs-do-to-the-body",
    "title":         "What drugs do to the body",
    "discipline":    "biology",
    "unit":          "health-and-drugs",
    "family":        "SYSTEM",

    # ── curriculum position ────────────────────────────────────────────────
    # The `a` clause of the split bullet — what a drug is and how one acts
    # once it is in the blood. See the docstring; `b` and `c` belong to the
    # other two lessons in this unit.
    "covers":        ["KS3.B.HLTH.01a"],
    # Named but not taught: the dose crosses the gut wall exactly as digested
    # food does (b3-07 owns NUT.04c), the route ends in a hierarchy of organs
    # (b1-05 owns CELLS.06), and the nicotine card hands smoke damage to
    # b4-04 by name rather than teaching it (GAS.03).
    "touches":       ["KS3.B.NUT.04c",
                      "KS3.B.CELLS.06",
                      "KS3.B.GAS.03"],
    "beyond_statutory": False,
    "threads":       [{"id": "cells-and-systems",
                       "level": 2},
                      {"id": "substances-and-reactions",
                       "level": 1}],
    "typical_year":  9,
    "typical_minutes": 55,

    # ── progression edges ──────────────────────────────────────────────────
    # Design draws a "Before this lesson" card with two entries and a
    # "Connects to" card with two more. NOTES-B6 §4: all four targets exist,
    # and no link in this unit dangles.
    "requires":      ["absorption-and-the-small-intestine",
                      "levels-of-organisation"],
    "assumes":       [],
    "references":    ["alcohol-and-smoking",
                      {"unit": "B4",
                       "lesson": "exercise-asthma-and-smoking"}],
    "connects_heading": "Connects to",
    "ks4_links":     [],
    "ks4_becomes":   "Drug development and testing: preclinical trials, "
                     "placebos, double-blind trials, and how a therapeutic "
                     "dose is decided.",

    # ── framing ────────────────────────────────────────────────────────────
    "big_question":  "Caffeine, paracetamol, nicotine and alcohol are all "
                     "drugs. That is not a judgement about any of them — it "
                     "is a description of what the molecules do once they are "
                     "in your blood.",

    # ── the progress rail (§4.8.1 A) ───────────────────────────────────────
    # FOUR stops, as Design draws them. `s-classes` is the third: no control
    # of its own, so it mirrors `s-dose` and ticks on the tracer's predicate —
    # see the docstring. `short` and `label` are Design's own RAIL_SHORT and
    # RAIL strings (page lines 330–336).
    "rail":          [{"anchor": "s-hook",
                       "short": "HOOK",
                       "label": "A mug of coffee",
                       "done_when": "committed"},
                      {"anchor": "s-dose",
                       "short": "DOSE",
                       "label": "Follow the dose",
                       "done_when": "all_five_stages"},
                      {"anchor": "s-classes", "short": "CLASSES", "label": "Three classes",
                       "mirrors": "s-dose", "done_when": "all_five_stages"},
                      {"anchor": "s-ladder",
                       "short": "LADDER",
                       "label": "Mastery ladder",
                       "done_when": "ladder_complete"}],

    # ── the hook (Law 1) ───────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). Option A is
    # DRUG-01 offered to the student in their own words, which is what makes
    # the hook the eliciting site for it.
    "phenomenon":    {"kind": "narrative",
                      "title": "A mug of coffee contains a drug.",
                      "prompt": "Around 90 milligrams of caffeine, bought in "
                                "a café, legal at any age, no prescription. "
                                "It changes how your nerve cells behave, and "
                                "that is why you drink it. So the word "
                                "<em>drug</em> cannot mean what most people "
                                "think it means.",
                      "commit": "What makes a substance a drug?",
                      "options": ["It is against the law to have it",
                                  "It changes the way the body works",
                                  "A doctor has to prescribe it",
                                  "You cannot stop taking it once you start"],
                      "reveal": "A drug is any substance that changes the way "
                                "the body works. That is the whole "
                                "definition. Whether it is legal, whether a "
                                "doctor prescribed it, and whether it is "
                                "addictive are three separate questions, and "
                                "the answers do not line up the way you would "
                                "expect."},

    # ── misconceptions (Law 3) ─────────────────────────────────────────────
    # ⚠️ The `DRUG` family is PRE-ALLOCATED per lesson, because B4's five
    # parallel authors collided twice on `BREATH` ids. This module owns
    # DRUG-01 and DRUG-02 and mints nothing else; the register is the
    # commander's to maintain centrally.
    #
    # DRUG-01 is cited by all three lessons in the unit and CONFRONTED HERE —
    # the register's `reappears_in` records the reappearance rather than
    # three near-duplicates being minted. It is elicited by the hook, where
    # option A is the belief stated as a choice, and killed by the first half
    # of #s-think.
    #
    # DRUG-02 is elicited by the tracer — a student who has pressed through
    # to stage 3 has watched the dose reach organs it was not taken for —
    # and killed by the second half of #s-think.
    "misconceptions": [{"id": "DRUG-01",
                        "statement": "Drugs are illegal substances.",
                        "elicited_by": "hook",
                        "confronted_by": "two-wrong-ideas"},
                       {"id": "DRUG-02",
                        "statement": "A painkiller goes to the part that "
                                     "hurts.",
                        "elicited_by": "follow-the-dose",
                        "confronted_by": "two-wrong-ideas"}],

    # Design draws no keyword block on this page, so these never reach the
    # lesson body — see "What could not be lifted" 7. They are the unit page's
    # chips and the reading-age gate's exclusion list.
    "vocabulary":    [{"term": "drug",
                       "definition": "Any substance that changes the way the "
                                     "body works.",
                       "note": "Whether it is legal, whether a doctor "
                               "prescribed it, and whether it is addictive "
                               "are three separate questions."},
                      {"term": "stimulant",
                       "definition": "Nerve signals pass more readily, so "
                                     "heart rate and alertness rise.",
                       "note": "Caffeine, nicotine."},
                      {"term": "depressant",
                       "definition": "Signals between nerve cells pass less "
                                     "readily, so reactions, coordination and "
                                     "judgement all worsen.",
                       "note": "Alcohol, and the sedatives used in "
                               "anaesthetics."},
                      {"term": "painkiller",
                       "definition": "The pain signal is reduced or blocked "
                                     "on its way to the brain. The cause of "
                                     "the pain is untouched.",
                       "note": "Paracetamol, ibuprofen, and morphine at the "
                               "strong end."},
                      {"term": "side effect",
                       "definition": "The unavoidable consequence of "
                                     "delivering a drug through a system that "
                                     "goes everywhere.",
                       "note": "Not a manufacturing fault."},
                      {"term": "dose",
                       "definition": "The amount of a drug taken, which is "
                                     "what decides whether it treats you or "
                                     "harms you.",
                       "note": None}],

    # ── figures (§4.10) ────────────────────────────────────────────────────
    # ⚑ NOTES-B6 flag 14: this unit names no diagram slots and draws none —
    # "the tracer, the clock and the claim board are the visuals". VERIFIED
    # on this page rather than taken on trust: no <figure>, no ks3-figure, no
    # <img>, and the foot line names no slot. Nothing is declared, because a
    # declaration here would invent a sourcing task Design did not ask for;
    # nothing is invented to fill one either.
    "figures":       [],

    # ── core, in the approved page's document order ────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-dose — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b6/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is measured, not inherited.
        #
        # ⚠️ Payload contract: NOTES-B6 §2.1, extended for the labels Design
        # draws. There is no b6 PAYLOAD-SCHEMA.md and no r_route_tracer yet.
        # See the docstring's own section on this.
        {"type": "route-tracer",
         "id": "follow-the-dose",
         "anchor": "s-dose",
         "demand": "investigate",
         "eyebrow": "At the bench · one dose, one bloodstream",
         "heading": "Follow the dose",

         # ⊕ MRB-244 — RESOLVED, and the note above it is no longer true.
         # Design's readout is three-state (`not started` → `stage 3 of 5` →
         # `all five stages`) and `_head_counter` had only two ends, so the
         # closing state was given up. The engine pass added `full` as the
         # mirror of `zero` in the same run; this authors it, and the readout
         # is Design's again in all three states.
         "head_counter": {"format": "stage {n} of {total}",
                          "total": 5,
                          "zero": "not started",
                          "full": "all five stages"},
         "prompt": "Pick a drug and follow one dose of it, one step at a "
                   "time. Watch step 3 carefully — it is the step everyone "
                   "skips, and it is the reason side effects exist at all.",

         # The four tabs and the five stages. `drugs[]` is §2.1's shape; a
         # stage names a shared `body` or a per-drug `body_from`.
         "drugs": DRUGS,
         "stages": STAGES,
         "start_drug": "caffeine",

         # The labels Design draws around the controls and the closing panel.
         # None is named by §2.1 and all five are on the page.
         "dose_label": "The dose",
         "next_labels": {"start": "Take the dose",
                         "more": "Next stage",
                         "done": "Journey complete"},
         "reset_label": "New dose",
         "elsewhere_label": "Where else the same dose went"},

        # #s-classes — the band panel. Rail stop 3, mirroring `s-dose`; see
        # the docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid.
        {"type": "rule",
         "anchor": "s-classes",
         "eyebrow": "Sorted by what they do, not by what they are called",
         "statement": "Three classes, and all three are about nerve signals.",
         "cards": CLASS_CARDS},

        # Design nests this inside #s-classes; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. `card` is the
        # ground she paints it — see "What could not be lifted" 3.
        {"type": "key-fact", "ref": "acts-wherever-it-fits",
         "ground": "card"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "DRUG-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ────────────────────────────────────────
    "key_facts":     [{"id": "acts-wherever-it-fits",
                       "text": "A drug is a substance that changes the way "
                               "the body works. The blood carries it to every "
                               "organ, so it acts wherever it fits — which is "
                               "why a drug taken for one job also does other "
                               "things you did not ask for.",
                       "placement": "top-level",
                       "ground": "card",
                       "eyebrow": "Key fact"}],

    # ── activities (§5.5) ──────────────────────────────────────────────────
    # TWO wrong ideas in one "Think again" block, the second behind an
    # amber-topped divider — `r_confrontation` renders exactly that from
    # `statements[]`, and an authored statement wins over the register. The
    # block asks for no commitment, on Design's page and here, so it is not a
    # rail stop and emits no completion contract.
    #
    # ⚠️ The quotes carry NO curly quotation marks: `_quoted()` adds them.
    # Design's markup has them and they are stripped here for that reason
    # alone — the rendered page is byte-identical to hers.
    "activities":    [{"id": "two-wrong-ideas",
                       "kind": "confrontation",
                       "demand": "explain",
                       "targets": "DRUG-01",
                       "statements": [{"quote": "Drugs are illegal substances.",
                                       "body": ["Legality is a decision made "
                                                "by a parliament. It differs "
                                                "between countries, it has "
                                                "changed several times within "
                                                "living memory, and the "
                                                "molecule is unaffected by "
                                                "any of it. Caffeine is a "
                                                "drug and it is sold to "
                                                "children. Paracetamol is a "
                                                "drug and it is in most "
                                                "kitchen drawers. Alcohol and "
                                                "nicotine are drugs, they are "
                                                "legal for adults in the UK, "
                                                "and between them they cause "
                                                "more illness and more deaths "
                                                "here than every illegal drug "
                                                "combined. Meanwhile morphine "
                                                "is a controlled drug that is "
                                                "also given in hospitals "
                                                "every day. So <em>legal</em> "
                                                "and <em>safe</em> are not "
                                                "the same word, "
                                                "<em>illegal</em> and "
                                                "<em>harmful</em> are not the "
                                                "same word, and <em>drug</em> "
                                                "and <em>medicine</em> "
                                                "describe overlapping sets "
                                                "rather than opposite ones: a "
                                                "medicine is simply a drug "
                                                "used to treat something."]},
                                      {"quote": "A painkiller goes to the "
                                                "part that hurts.",
                                       "body": ["Nothing in a tablet knows "
                                                "where your head is. It "
                                                "dissolves, crosses the gut "
                                                "wall into the blood, and the "
                                                "blood takes it round the "
                                                "entire body in under a "
                                                "minute — liver, kidneys, "
                                                "skin, feet, all of it, "
                                                "whether they need it or not. "
                                                "The tablet works on your "
                                                "headache because the pain "
                                                "pathways carrying that "
                                                "particular signal are "
                                                "something it can act on, not "
                                                "because it travelled there. "
                                                "Everything else it touched "
                                                "on the way is what we call a "
                                                "side effect, and side "
                                                "effects are not a "
                                                "manufacturing fault. They "
                                                "are the unavoidable "
                                                "consequence of delivering a "
                                                "drug through a system that "
                                                "goes everywhere. It also "
                                                "explains why the number on "
                                                "the box matters: your liver "
                                                "breaks the drug down at a "
                                                "fixed rate, and a second "
                                                "dose taken early does not "
                                                "get a second liver."]}]}],

    # ── the mastery ladder (Law 8, §5.8) ───────────────────────────────────
    #
    # ⊕ MRB-177 RULED BY MIDE, 17 Aug 2026 — RUNG 2'S DISTRACTORS ARE REPAIRED.
    #
    # The ruling: on a recall or apply rung the correct answer states a RULE
    # (subject, condition, consequence) while the distractors state one-clause
    # wrong REASONS, so the correct answer is longer BY CONSTRUCTION and a
    # student can score the question without reading it. The fix is that a
    # distractor states a WRONG RULE — the same shape as the correct answer,
    # with the misconception as the consequence. Length parity then follows
    # from the construct rather than from trimming anything.
    #
    # Rung 2's three distractors are Mide's own replacement copy, applied
    # verbatim. **The correct option is unchanged, its index is unchanged
    # (`answer: 1`), and the threshold in verify_ks3.py is unchanged.**
    # Measured after: correct 22w against 20 / 17 / 19 — gap 2 and ratio 1.10,
    # inside both limbs of `length_tell()`.
    #
    # ⛔ SUPERSEDED, KEPT AS HISTORY — the paragraph this replaced read:
    #   "rung 2: correct 22w against distractors of 10 / 10 / 7. Trips both.
    #    A NEW TELL, and it is a tell exactly as Design drew it. NOTHING WAS
    #    REWRITTEN. Rewriting a distractor changes what a marked question
    #    measures, which MRB-177's own register in verify_ks3.py says is
    #    Mide's gate and not an author's."
    # That was correct while the gate was unruled. It has been ruled, and the
    # `("what-drugs-do-to-the-body", "ladder apply")` register entry is now
    # stale — the commander deletes it in verify_ks3.py, which this module
    # still does not own.
    #
    #   rung 1: correct 7w against distractors of 3 / 6 / 5. Strictly longest,
    #           but 7 − 6 = 1 (< 4) and 7 < 1.4 × 6, so it clears both
    #           thresholds. Clean, and untouched by the ruling.
    "ladder":        {"recall": {"title": "Rung 1 · What the word means",
                                 "q": "Which statement is true of every drug "
                                      "— prescribed, bought in a shop, or "
                                      "illegal?",
                                 "options": ["It changes the way the body "
                                             "works",
                                             "It is addictive",
                                             "It is harmful in any amount",
                                             "It is controlled by law"],
                                 "answer": 0,
                                 "feedback": {1: "Many are not. Paracetamol "
                                                 "is a drug and is not "
                                                 "addictive; that is a "
                                                 "separate property some "
                                                 "drugs have and others do "
                                                 "not.",
                                              2: "Dose decides. The same "
                                                 "molecule can be a medicine "
                                                 "at one amount and a poison "
                                                 "at another, which is the "
                                                 "point of the foxglove "
                                                 "example below.",
                                              3: "Caffeine is not. Legality "
                                                 "is a decision a parliament "
                                                 "makes, and it changes; what "
                                                 "the molecule does to the "
                                                 "body does not."}},
                      "apply": {"title": "Rung 2 · The one that catches people",
                                "q": "You swallow a paracetamol tablet for a "
                                     "headache. Where does the drug go?",
                                "options": ["A painkiller travels through the "
                                            "blood to the part that hurts, "
                                            "because that is the part sending "
                                            "the pain signal",
                                            "Everywhere the blood goes — it "
                                            "acts on your head because that "
                                            "is where there is something for "
                                            "it to act on",
                                            "A tablet works where it "
                                            "dissolves, so a swallowed "
                                            "painkiller acts on the stomach "
                                            "and nowhere else",
                                            "The body sends a drug only to "
                                            "the organs that need it, and "
                                            "keeps it away from the rest"],
                                "answer": 1,
                                "feedback": {0: "Nothing in the tablet knows "
                                                "where your head is. Follow "
                                                "the dose on the bench above: "
                                                "it is in the blood, and the "
                                                "blood goes everywhere.",
                                             2: "Dissolving is not the end of "
                                                "the journey. It crosses the "
                                                "gut wall into the blood, "
                                                "exactly as digested food "
                                                "does.",
                                             3: "There is no such sorting "
                                                "step. Every organ is offered "
                                                "the dose, and that is what "
                                                "side effects are."}},
                      "explain": {"title": "Rung 3 · Explain a side effect",
                                  "q": "A friend takes a caffeine tablet to "
                                       "stay awake revising and finds their "
                                       "heart is racing. They think they have "
                                       "had a bad reaction to a faulty "
                                       "tablet. Explain what actually "
                                       "happened, using the route the drug "
                                       "took.",
                                  "field_label": "Your explanation",
                                  "placeholder": "The caffeine was absorbed…",
                                  "success": ["Says the caffeine was absorbed "
                                              "into the blood.",
                                              "Says the blood carried it "
                                              "round the whole body, not just "
                                              "to the brain.",
                                              "Says it acted on the brain, "
                                              "which is the effect they "
                                              "wanted.",
                                              "Says it also reached the "
                                              "heart, which speeds up in "
                                              "response — the racing heart is "
                                              "the same drug doing a second "
                                              "thing.",
                                              "Makes clear the tablet was not "
                                              "faulty: a side effect is the "
                                              "expected result of delivering "
                                              "a drug through a system that "
                                              "reaches everywhere."]},
                      "produce": {"title": "Rung 4 · Take it somewhere new",
                                  "q": "Someone has a bad headache. Two "
                                       "paracetamol have not worked after an "
                                       "hour, so they decide to take two more "
                                       "early, reasoning that a bigger dose "
                                       "must work better. Using what you know "
                                       "about the liver and about dose, "
                                       "explain the risk — and say what they "
                                       "should do instead.",
                                  "field_label": "Your answer",
                                  "placeholder": "The liver…",
                                  "success": ["Says the liver breaks the drug "
                                              "down at a fixed rate that "
                                              "cannot be hurried.",
                                              "Says a second dose taken early "
                                              "means more drug in the blood "
                                              "at once, because the first has "
                                              "not been cleared.",
                                              "Says too much paracetamol "
                                              "damages liver cells, and that "
                                              "the damage can be serious even "
                                              "when the person feels fine at "
                                              "the time.",
                                              "Explains that the dose "
                                              "interval on the box is a "
                                              "safety limit rather than a "
                                              "suggestion.",
                                              "Says what to do instead: wait "
                                              "the stated interval, and ask a "
                                              "pharmacist, the school nurse "
                                              "or a GP rather than guessing."]}},

    # ── the key note (fixed, last, photographable) ─────────────────────────
    "key_note":      "A drug is any substance that changes how the body "
                     "works. Stimulants speed nerve signals up, depressants "
                     "slow them down, painkillers block the pain signal "
                     "without touching its cause. Every drug is carried "
                     "everywhere by the blood, acts where it fits, and is "
                     "broken down mainly by the liver at a rate that cannot "
                     "be hurried. Dose decides whether a drug treats you or "
                     "harms you.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ───────────────
    # NOTES-B6 flag 11: digoxin and the foxglove, and dose-response as a
    # statement about quantity rather than a category of substance. The
    # "even water" clause is Design's and is carried; it is the one example
    # in the layer that is not a drug at all, which is what makes the point.
    "stretch":       [{"type": "explainer",
                       "id": "same-molecule-different-amount",
                       "text": "Digoxin comes from the foxglove in the "
                               "hedgerow. At the right dose it steadies a "
                               "failing heart and it has been prescribed for "
                               "two hundred years; a little above that dose "
                               "it stops the heart, which is why foxglove is "
                               "one of the most dangerous plants in Britain. "
                               "Same molecule, same body, different amount — "
                               "so <em>poison</em> is not a category of "
                               "substance at all, it is a statement about "
                               "quantity. Even water follows the rule: drink "
                               "several litres in an hour and you can dilute "
                               "your blood dangerously. This is why "
                               "pharmacists talk about doses rather than "
                               "about safe and unsafe substances, and why "
                               "<em>it is natural, so it must be gentle</em> "
                               "is a claim about where a molecule came from "
                               "rather than about what it does."}],

    # ── the support layer ──────────────────────────────────────────────────
    # ⚑ THE FIRST NON-EMPTY `support[]` IN THE KEY STAGE, and the one place
    # this record loses something that matters — `r_layer` hard-codes the
    # support eyebrow as "Need a hand?" and Design's is "If any of this is
    # about you or someone you know". See "What could not be lifted" 1; it is
    # a design flag for Mide, and the paragraph itself is byte-identical.
    #
    # Design points at "the services listed in your school's PSHE materials"
    # rather than naming a helpline, because a named helpline goes stale and
    # naming one is a safeguarding decision rather than an authoring one.
    # Carried as drawn. Nothing added, nothing softened.
    #
    # ⊕ MRB-244 — `support_heading` now exists and this lesson takes it. The
    # engine used to hard-code "Need a hand?" over every support layer, which
    # had never rendered anywhere because B6 is the first unit in KS3 with a
    # non-empty `support[]`. A study-support phrase over a referral block about
    # somebody's drug use is not a styling nit; it changes who thinks the block
    # is addressed to them. Design's eyebrow, lifted byte-identical.
    "support_heading": "If any of this is about you or someone you know",
    "support":       [{"type": "explainer",
                       "id": "if-this-is-about-you",
                       "text": "This lesson covers the biology only. "
                               "Decisions, pressure from other people and the "
                               "law belong to your PSHE and RSE lessons, "
                               "which is where to raise them. For anything "
                               "about your own health, a medicine you are "
                               "taking, or someone you are worried about, "
                               "talk to a trusted adult, the school nurse, a "
                               "pharmacist or a GP — a pharmacist will answer "
                               "a question about a medicine without an "
                               "appointment. Your school's PSHE materials "
                               "list the national confidential services by "
                               "name."}],

    # ── end matter (§4.8.1 C, D) ───────────────────────────────────────────
    "tutor":         {"prompt": "Ask Mr Badmus AI",
                      "body": "Want to talk through why side effects are "
                              "unavoidable rather than a fault?",
                      "cta": "Ask about this lesson",
                      "anchor": "s-dose"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph at the bottom edge and nothing in it is a safety
    # instruction — it is a note about what the tracer is and is not, and a
    # statement that the page gives no doses, thresholds or timings. Routing
    # it through `safety_note` would print it in the treatment reserved for
    # "never light a candle without an adult", which devalues the safety line
    # and would also read, on this unit, as the scare copy §1 forbids.
    # b4-01, b5-02, b3-05 and b3-07 resolve the identical foot line the same
    # way. §8.10: small, bottom edge, never a callout.
    "convention_note": "The tracer is a simplified model. It follows one dose "
                       "of one drug through five stages in order, and gives "
                       "no doses, thresholds or timings for any substance. "
                       "Real absorption, distribution and breakdown overlap "
                       "in time and differ between people. Nothing on this "
                       "page is medical advice.",

    # ── working scientifically (§5.7) ──────────────────────────────────────
    # The tracer is a MODEL walked in order and then reasoned from: the
    # student is told in the foot line that it is simplified, and rungs 3 and
    # 4 ask them to explain an observation from the route rather than to read
    # a measurement. The think-again block is the attitudes half — legality
    # against harm, and what a definition can and cannot decide.
    "ws":            ["analysis-and-evaluation",
                      "scientific-attitudes"],

    # ── governance (§5.10) ─────────────────────────────────────────────────
    "review_state":  "draft",
}
