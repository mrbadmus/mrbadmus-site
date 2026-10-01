# early-atmosphere — authoring notes (batch 3)

## Lesson record

```python
dict(slug="early-atmosphere", source_file="early-atmosphere.dc.html",
     subject="chemistry", topic_id="atmosphere",
     title="The Earth's early atmosphere and how it changed",
     spec="5.9.1.2–5.9.1.4 (8462 4.9.1.2–4.9.1.4)",
     family="Process", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-clock": "worked-example"})
```

Section ids: `s-hook` (hook), `s-clock` (needs the block_map entry above), `s-equation` (equation, by id), `s-oil` (Ks4Chain → check), `s-evidence` (Ks4Sort → check), command-words block (keyword), `s-ladder`, `s-keynote`. Proven on the real compiler: `build_ks4.py --batch batch-3` in a scratch clone with a temporary `batch_3.py` holding only this lesson and greenhouse-gases. It built 8 pages with zero console errors at 1280 and 360 px.

## Family: PROCESS, and why
The spec content is a sequence in time. Each change has a cause, and the cause is the mark: volcanoes, then oceans, then algae, then plants, then burial, with nitrogen building up all along. The flagship is a worked stepper with a prediction at every stage, which is PROCESS's flagship shape. The BATCH-PLAN's provisional family (Process) is kept.

## Instruments and the demand each trains
- **Flagship (L) `#s-clock`, "Run the clock".** Six stages, each predict-gated. The pupil picks first. Only then does the scene change (oceans fade in, rain falls, algae, plants, buried stores) and the air bar animate from the old gas shares to the new ones (SMIL; reduced motion gets the instant swap). Demand: **sequence and cause**, predicting each change from the mechanism. Options are in hash order, so the key is not always first. Every distractor is a named misconception with corrective feedback. The reply shows only on a wrong pick, and the reveal never repeats the key.
- **Micro, inside `#s-equation`: spot the flaw.** A pupil has written the respiration equation to explain where the oxygen came from. Demand: tell photosynthesis from respiration by which side the oxygen is on (examiner misconception: "writing the respiration equation instead").
- **Mid (M1) `#s-oil`: Ks4Chain.** How crude oil and natural gas formed: 4 links, 3 red herrings (coal from swamp plants, full decay, dinosaurs). Demand: **describe a formation sequence** (spec 5.9.1.4, "describe and explain the formation of deposits of … crude oil and natural gas").
- **Mid (M2) `#s-evidence`: Ks4Sort, supports or weakens.** Six evidence cards on "early Earth's air was like Mars's". Demand: **evaluate a theory from given evidence** (5.9.1.2, base). The cards are balanced, three per bin. The negative words ("no", "little") appear in both bins, so the sort cannot be solved by word shape.
- Ladder:
  - r1: frozen q2 ("Why did CO₂ levels decrease…"), Give, 1 mark. It passes the length-parity rule (13 vs 13 words).
  - r2: data, Suggest, 2 marks, on a sketch graph. Part 1 reads off when oxygen first appeared. Part 2 asks why CO₂ fell before any oxygen appeared: the answer is the oceans, and the "plants" distractor is ruled out because there was no photosynthesis yet.
  - r3: chain, Explain, 3 marks, on why nitrogen became the main gas.
  - r4: the examiner's classic 6-mark Describe with Levels 1–3.
- No CFIFA (no calculation). No RP: AQA names none, and the examiner confirmed it.

## Misconceptions and where each is confronted
- "Volcanoes released oxygen": stage 0 asks which gas is missing from what volcanoes release. The three-beat panel ("The volcanoes gave the Earth its oxygen.") appears right there, at that commitment.
- "CO₂ condenses / rains out" and "only living things remove CO₂": stage 1 distractors.
- Photosynthesis versus respiration direction, and "nitrogen from photosynthesis": stage 2 distractors and the `#s-equation` spot-the-flaw.
- "Plants were there from the start" and "oxygen removes CO₂": stage 3.
- "Fossil fuels from dinosaurs", "coal and oil swapped", "remains fully decay": stage 4 and the `#s-oil` herrings.
- "Nitrogen from photosynthesis / from the oceans", "oxygen became nitrogen": stage 5 and the rung 3 herrings.
- Treating the theory as fact, and evaluations that only say "nobody was there": the evidence explainer and `#s-evidence`.

## Route tags
**None.** Every point is base on all four routes: 8464 5.9.1.2–5.9.1.4 and 8462 4.9.1.2–4.9.1.4 carry no HT label and no chemistry-only label (examination §2). Evaluating evidence, which the pack had in the Higher-only field (R8), is taught as base to every route. The eyebrow reads "AQA Combined Science (8464) 5.9.1.2–5.9.1.4" on Combined and "AQA Chemistry (8462) 4.9.1.2–4.9.1.4" on Triple. The header is the route chip only (no RP pill).

## ⚑ Net-new science-bearing items
- ⚑ Hook figure: Venus about 96% CO₂, Mars about 95% CO₂, Earth N₂ 78%, O₂ 21%, CO₂ about 0.04%.
- ⚑ Hook: most of Earth's carbon is now underground, in sedimentary rocks and fossil fuels, not in living things.
- ⚑ "Some books call these first organisms cyanobacteria; AQA calls them algae." This follows the examiner's re-cut C7.
- ⚑ Stage 1: carbonates precipitate and settle as sediment (spec 5.9.1.2 wording; missing from the pack).
- ⚑ Stage 4 and `#s-oil`: limestone from shells and skeletons; coal from plants; crude oil and gas from plankton buried in mud, kept from oxygen, compressed under heat and pressure over millions of years. This is the examiner's §5 text, covering the pack's gap R6.
- ⚑ Stage 3: oxygen rose gradually over about a billion years to a level that let animals evolve (spec 5.9.1.3, covering gap R5).
- ⚑ Stage 5 and rung 3: nitrogen was released by volcanoes and is unreactive, so little was removed; its share also rose as CO₂ was removed (C14 re-cut). Argon is named among today's other gases.
- ⚑ Evidence cards:
  - volcanoes today give out mainly water vapour and CO₂;
  - very old rocks contain minerals that only form with little oxygen;
  - Mars is smaller and has lost much of its atmosphere to space;
  - Mars has no oceans and no life.
- ⚑ Rung 2 sketch graph. The shape is schematic, with no y values: CO₂ falls steeply between 4 and 3 billion years ago, and O₂ is zero until about 2.7 billion years ago, then rises to about 21%. The air-bar shares in the flagship are a labelled sketch ("not to scale"; the legal line also says so).
- ⚑ Rung 4 marking points and levels (from the examiner's 6-mark Describe), and the rung 2 and rung 3 mark-scheme lines.

## Frozen items and source fields
- **No quiz item is withheld.** q1 ("What was the main source of oxygen…") stays in the bank on all routes. Its key says "cyanobacteria" (C22). The page names algae and explains that cyanobacteria are among them, as the examiner requires. q1 is not used as a rung anyway: it fails length parity (14 vs 9 words).
- q2 wx1 calls CO₂ in rain "acid rain" (C27, minor). It is kept verbatim and used as rung 1, as the examiner allows.
- **Key note:** the frozen key_note is not shown verbatim. It says O₂ came from "cyanobacteria" (C7/C18), omits fossil fuels (R6) and "outgassing". It is replaced by six authored lines using AQA's "algae and plants", adding fossil fuels and limited evidence. **This is a DEPARTURES §2 row.**
- Not shown, as NOT-IN-SPEC: Miller–Urey (`higher` field, R9), the ozone/UV story, banded iron, isotopes (R10), and "cooled below 100 °C" (C11).
- The equation is shown verbatim from `equations[0]`: the symbol part, with its parenthetical as a caption. It is labelled "Learn it" (chemistry has no equation sheet), plus a net-new word equation (C6).

## New instruments and helpers
These all live inside the lesson's own Component; there is no `_ext` file:
- the "Run the clock" stepper: `clockSvg`, `barSvg`, `volcano`, `tree`, `legendSvg`;
- the hook share-bar figure: `hookSvg`;
- the rung 2 sketch graph: `graphSvg`;
- `order()`, a hash-ordered option list (uses `KS4.hash`).

## Body prose
About 120 words of explainers. Counting the hook text, the stage texts and reveals, the panel, and the sort and chain prompts, it comes to about 600 words in all, under the ~700 budget. The longest run of prose before a commitment is about 90 words.

## Review fixes
| id | what I did / why not |
|---|---|
| Q-1 | First explainer cut to its first sentence, "AQA examines one theory …". |
| Q-2 | Rung 2 part (b) replaced with the reviewer's graph-reading part: how the percentage of oxygen changed after 2.7 billion years ago. `model[1]` and `wrong` replaced with the reviewer's text. Rung 2's command chip changed from Suggest to Describe to match the new parts. In the command-words block, the Suggest card is replaced with Give, which rung 1 uses. |
| Q-3 | Hook figure segment labels drop to 19 px when the segment is narrower than 120 units. |
| A-9 (science) | Hook heading now reads "Venus and Mars **may** still have the kind of air Earth started with" (spec 5.9.1.2 wording). |
| A-1 | Rung 3 oceans herring now has its own feedback, so it no longer repeats clock stage 6. The Explain command card is now generic: "link each step to the next with so or because". |
| A-2 | Eyebrow is now just "Equation". The chip reads "Learn it · no chemistry equation sheet". |
| A-3 / A-4 | Not changed. A-3 is a structural change to the stepper. A-4 (shared stepper shape): the two lessons' instruments differ in family and content. |
| A-8 (science) | Kept, as the reviewer and the examination advised. |
