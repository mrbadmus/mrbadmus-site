# mixtures — author notes (batch 3)

## Record

```python
dict(slug="mixtures", source_file="mixtures.dc.html",
     subject="chemistry", topic_id="atomic-structure",
     title="Mixtures and separation techniques", spec="5.1.1.2",
     family="Classify", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-desk": "check", "s-kit": "practical"})
```

Spec: 8464 5.1.1.2 / 8462 4.1.1.2 (identical). No required practical (examination R8): no RP pill, no RP block.
Built in a scratch clone with `build_ks4.py --batch batch-3` and a temporary record: 4 pages, zero console errors at 1280 and 360 px; driven at 390 px light and dark through all five desk rounds, no overflow, no `undefined`/`NaN`/`null`/`{{` text.

## Family: CLASSIFY, and why

The spec's demand is "suggest suitable separation and purification techniques… when given appropriate information": decide the category (the technique) from the property that differs and the substance wanted. No calculation is owned here (Rf belongs to `chromatography`), so no CFIFA and no equation block. BATCH-PLAN's family kept; its RP = Y is wrong (examination) and not followed.

## Line-up and demands

| block | size | demand trained |
|---|---|---|
| `s-hook` Ks4Choice (ungraded) | micro | commit: what happened to dissolved sugar (physical change, nothing new made) |
| explainer | — | definition of a mixture (the GAP, R1), physical separation, the five named processes, the two questions for choosing |
| `s-desk` Separation desk | **L (flagship)** | five mixtures, five techniques: predict the method from mixture + goal, then the correct apparatus is drawn and animated (filtrate filling, crystals growing, drips, dyes rising); same ink twice with different goals (water → simple distillation; dyes → chromatography) |
| `s-think` predict-trap | micro | "a fine enough filter catches salt" (filtration sorts by solubility, examination C2) |
| `s-chain` Ks4Chain | **M** | sequence: dissolve → filter → crystallise → dry, with two spoiling steps as herrings |
| explainer | — | lab fractional distillation: beads, lowest boiling point first, collected one after another (C9) |
| `s-kit` Practical skills (AT 4) | micro | identify the faulty part of a distillation set-up (thermometer bulb in the liquid); badged practical skills, not "Required practical" |
| ladder | — | r1 Give 1 mark (authored definition ⚑), r2 Suggest 2 marks (data kind; Foundation chalk/water + copper chloride, Higher sugar solution + methanol/ethanol), r3 Explain chain (why fractional not simple), r4 Plan 6-mark rock salt with levels |

Adjacent `atoms-elements-compounds` (batch 2) is not duplicated: its hook is sodium + chlorine → salt and its flagship classifies particle boxes as element/compound/mixture. This lesson's hook is sugar in water and its flagship chooses separation techniques; the mixture definition appears once, as one sentence plus rung 1.

New section ids needing `block_map`: `s-desk` → check, `s-kit` → practical (`s-chain` classifies itself via its single Ks4Chain import).

## Misconceptions, where confronted

| misconception | where |
|---|---|
| dissolving is a reaction / the substance is gone | hook replies + reveal |
| filter salt out of salt water (source common_mistake) | desk wrong-pick replies; `s-think` three beats |
| crystallisation = boil dry; filter before dissolving | chain herrings |
| simple distillation works for close boiling points | desk round 4 reply; rung 3 |
| heaviest molecules rise to the top; ethanol and water do not mix | rung 3 herrings |
| thermometer bulb in the liquid | `s-kit` |
| evaporate to collect water | rung 4 reject line |

## Route tags

None. Examination §2: no HT and no chemistry-only content. Rung 2 differs by tier in logic (`R.isHigher`). Eyebrow: "AQA Combined Science (8464) 5.1.1.2" / "AQA Chemistry (8462) 4.1.1.2".

## Frozen items

- No quiz item is wrong for any route; nothing to withhold. q1 and q3 are not used as rungs (rung 1 is the authored definition, because the examination names the definition as the missing 1-mark recall staple; q1 is an apply item and the desk teaches its near-twin). The bank is `K.bank(slug, R.route)`, all three items, including q2 (Rf), which the examination says to keep in the bank.
- `rp` field (WRONG number and wrong lesson, C18): not shown.
- Rf equation, FIFA and variables: not shown (belong to `chromatography`); desk round 5 points there in one line.
- key_note line "Chromatography: dissolved substances — Rf = …" shown as "Chromatography: dissolved substances." (C14: keep Rf only if previewed). Other key-note lines verbatim; one definition line prepended.
- th1 "size of particles (filtration)" and "magnetism" not used (C2, R9); th2 "heat to saturate" re-cut as "evaporate some of the water" (C6); th3 industrial "collected at different heights" not used for the lab method (C9).
- q3 wx1 is imprecise (C27) but kept verbatim in the bank; the lesson's own round 4 and rung 3 give the "close boiling points" reason.

## ⚑ Net-new science-bearing items

1. ⚑ Hook: dissolved sugar is still sugar, recoverable by evaporation, nothing new made; option replies.
2. ⚑ Explainer definition and "physical processes make no new substances" (spec 5.1.1.2 verbatim sense).
3. ⚑ Desk: every round's correct explanation and every wrong-pick reply (20 replies), incl. "simple distillation only separates liquids whose boiling points are very different; at 78 °C and 100 °C the distillate would still contain a lot of water"; ethanol collected first at ~78 °C.
4. ⚑ Apparatus drawings: filtration, crystallisation (evaporate then cool), simple distillation (bulb at side arm, water in at the bottom), lab fractional distillation (bead column, 78 °C), paper chromatography (pencil line above solvent, three dyes).
5. ⚑ Filtration separates by whether a solid has dissolved; dissolved particles are smaller than any filter paper hole.
6. ⚑ Boiling dry can spit and leaves dissolved impurities in the solid.
7. ⚑ Anti-bumping granules make boiling smooth; water in at the bottom keeps the condenser full; thermometer at the side arm reads the boiling point of the substance collected.
8. ⚑ Ethanol–water cannot be distilled to pure ethanol (legal line).
9. ⚑ Rung 1 options and replies; rung 2 items (methanol 65 °C, ethanol 78 °C; copper chloride crystallisation); rung 3 links/herrings; rung 4 levels and points (from examination §5; salt obtained by evaporating the water, since NaCl solubility barely changes with temperature).

## New instruments / helpers

All in the lesson's logic: `flame`, `beaker`, `flask`, `thermo`, `condenser` (computes jacket, inner tube and water in/out pipes along any slope), `mixtureSvg`, `filtrationSvg`, `crystalSvg`, `simpleSvg`, `fractionalSvg`, `chromSvg`. CSS animations `mix-fill`, `mix-drip`, `mix-steam`, `mix-grow`, `mix-rise`, `mix-front` (prefixed, reduced-motion off). No `_ext` file.

## Body prose

Hook ~17 words, explainer 1 ~95, explainer 2 ~60: ~172 words; longest run before a commitment ~95.

## Review fixes (1 Oct 2026)

| row | change |
|---|---|
| science S-1 | `ROUNDS` sand round, Simple-distillation reply → "Distilling off all the water would leave the sand behind, but it takes a long time and a lot of energy. A filter catches insoluble sand in seconds." |
| science A-4 | Key-note line "Fractional distillation: liquids with different boiling points." shown as "Fractional distillation: liquids whose boiling points are close together." |
| science A-5 | Not applied by the author: withholding q2 (Rf) from the bank is the commander's call (needle `a spot travels 4.5 cm`). |
| science A-6 | Kept, as advised. |
| quality Q-1 | Desk reordered to blue ink → water, sand, copper sulfate, muddy pond water (NEW, filtration again ⚑), ethanol, same ink → dyes. Answers are no longer in button order, and filtration repeats, so the last round cannot be solved by elimination. Six rounds. |
| quality A-1 | Second explainer cut to the new content only: bead column; fractions collected one after another as the thermometer reading rises. |
| quality A-2 | The chromatography-lesson signpost cut from the last round's reveal. |
| quality A-3 | Not changed (labels were raised from 22 to 26 px before review). |

Rebuilt in a scratch clone (batch-3, 44 pages, zero console errors), and all six desk rounds driven at 390 px: no stray text, no overflow.
