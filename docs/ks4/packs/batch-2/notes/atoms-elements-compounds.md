# atoms-elements-compounds — lesson notes (batch-2, draft)

## Lesson record

```python
dict(slug="atoms-elements-compounds",
     source_file="atoms-elements-compounds.dc.html",
     subject="chemistry", topic_id="atomic-structure",
     title="Atoms, Elements and Compounds",
     spec="5.1.1.1", family="Classify", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

Spec: 8464 5.1.1.1 / 8462 4.1.1.1 (text identical in both), with 4.1.1.2 (mixtures) and 4.3.1.1 (balanced equations) as supporting statements. The eyebrow and key-note spec chip read `5.1.1.1` on Combined routes and `4.1.1.1` on Triple routes, computed from `R.isTriple`.

## Family: CLASSIFY, and why

The skill the lesson trains is a fast, justified decision: element, compound or mixture. AQA tests it mostly with particle-diagram boxes ("which box shows a mixture of an element and a compound?") and with named substances. Equations come second, as the symbolic form of the same idea, not as a separate mechanism. So the batch plan's provisional family stands.

The line-up differs from the pilot's CLASSIFY lesson (chemical-bonds). Here it is: hook, explainer, flagship, sort, explainer, spot-the-flaw, balancer, ladder. Chemical-bonds has no balancer, and its decider works from element pairs, not from particle drawings.

## Instruments and the demand each one trains

| scale | instrument | demand |
|---|---|---|
| L (flagship) | **Zoom in** (`#s-zoom`). Six particle boxes, unnamed: CO₂, O₂, He + Ne, N₂ + CO₂, an FeS layer, a bronze (Cu + Sn) layer. For each box the pupil commits to element, compound or mixture. Only after the commit is the box named and animated. In a mixture box the two substances slide apart, each particle unchanged. In element and compound boxes every particle is traced as an identical unit. In the FeS box the Fe:S pairs are traced, with the caption "1 : 1 in every part". In the bronze box the tin atoms are ringed, "no fixed ratio". The verdict names the specific wrong idea. | Classify from the particle model (diagram level). The answer is never visible before the commit. The options are fixed category words, so word shape gives nothing away. |
| M | **Ks4Sort**, 10 named substances (Cu, Au, O₂, H₂O, CO₂, MgO, air, seawater, crude oil, bronze). This replaces the matching activity. The examination's C19 items are reused without their give-away descriptions. Each card's `why` explains a misplacement. The done-note is the verbatim `common_mistake`. | Classify from the name or formula (symbol level). This is the step up from the diagram level to the symbol level. |
| M | **Balancer** (`#s-balance`). First a worked example: H₂ + O₂ → H₂O balanced in three revealed steps, from the theory's own example. Then the pupil balances three equations with − / + coefficient steppers, kept between 1 and 6: Mg + O₂, N₂ + H₂, CH₄ + O₂. A live tally shows the count of each atom on each side. On Check, the verdict is one of: balanced, balanced but not the simplest ratio (the gcd test), or which elements are still off. Formulae cannot be edited. | Produce a balanced symbol equation (Law 6 production; Law 5 watch then do). |
| micro | Hook `Ks4Choice` (unscored): why is salt safe? | Commitment within the first 150 words. |

## Misconceptions and where each is confronted

1. **"A diatomic element is a compound" (O₂ has two atoms).** Confronted in box 2 of the flagship. If the pupil calls it a compound, an amber three-beat panel opens.
2. **"Alloys are compounds."** Confronted in box 6 (bronze), with the same amber panel if the pupil picks compound.
3. **"A compound is a mixture" (salt water or iron sulfide treated as mixtures).** Confronted in box 5's wrong-pick reply, the sort's done-note (the verbatim common_mistake), the r3 chain herrings, and the r4 reject list.
4. **"Balance by changing a subscript" (H₂O → H₂O₂).** The examination says frozen q3 accidentally rewards this. Confronted head-on as a spot-the-flaw (`#s-think`) placed directly before the balancer, where the error is born. The three beats are: the quote, the option replies (why it is wrong), and the reveal (2H₂ + O₂ → 2H₂O).
5. **"A compound has the properties of its elements."** Confronted by the hook (sodium + chlorine → salt) and its reveal.

## Route tags

None. Every point taught is base. The examination route table confirms R1–R6 and R8 as base (4.1.1.1, 4.1.1.2, 4.3.1.1). The only HT content in 4.1.1.1, ionic and half equations (R7), is deliberately **not** taught, per the examination. No chemistry-only content.

## ⚑ Net-new science-bearing items

- ⚑ Hook text and options (sodium is a soft metal that reacts violently with water; chlorine is a toxic yellow-green gas). The reply "Over half the mass of salt is chlorine" is true: 35.5 ÷ 58.5 = 61 %.
- ⚑ Atom definition worded from the spec (examination C1). "About 100 elements (118 are known today)" follows examination C3. Compound properties are called "different", not "completely different" (C7).
- ⚑ All six flagship boxes, their verdict texts and both confront panels. FeS is drawn as an alternating 1:1 layer of a giant structure. Bronze is drawn as Cu with irregular Sn atoms and no fixed ratio. Both are disclosed in `legal`.
- ⚑ The ten sort `why` lines.
- ⚑ The spot-the-flaw options and replies.
- ⚑ The balancer equations and their answers: 2Mg + O₂ → 2MgO; N₂ + 3H₂ → 2NH₃; CH₄ + 2O₂ → CO₂ + 2H₂O.
- ⚑ The four command-word definitions and the key fact (the rule for reading a particle diagram).
- ⚑ Rung 2, data kind: the examination's drafted "__Na + Cl₂ → __NaCl, name the product, classify it". There are four pick parts for 3 marks. Distractors are "sodium chlorine" (the -ide ending missed) and "sodium chlorate" (-ate means oxygen is present).
- ⚑ Rung 3 chain: why air is a mixture. Fractional distillation is named as an example of a physical process (4.1.1.2 lists it).
- Rung 4 is the examination's own drafted 4-mark Explain question on iron + sulfur, with its marking points copied verbatim. ⚑ The two reject lines are new. "The iron has been destroyed" is corrected to the atoms being conserved, which addresses examination C24.

## Frozen items flagged wrong, and how they are handled

- **q2 (iron + sulfur, all routes).** wx3 states the false claim that sulfur stays solid. It is kept verbatim in the practice bank (`K.bank`). It is never a ladder rung and never quoted in the body. The scenario is reused only in rung 4, with fresh marking points.
- **q3 ("Which equation is correctly balanced?", all routes).** It has two correct answers. It is kept verbatim in the bank, never a rung, and never used in the body. Balancing is trained with fresh items (the balancer and rung 2), whose stems name the product.
- **Rung 1** = q1 (`'key difference between a compound and a mixture'`). Its fallback is q4. Both are clean on every route, and both needles exist in all four route copies, which are byte-identical.

## Other

- **Exam tip slot:** omitted. The subtopic has no `examiner_tip` on any route, and none was written.
- **New instrument or helper:** the Zoom-in particle boxes and the Balancer are both built inside the lesson's own Component logic, with namespaced CSS keyframes `aec-*` in the helmet. No `_ext` file. Motion is CSS keyframes on SVG groups. The resting inline style is the end state, so reduced motion (`animation: none`) shows the final picture instantly.
- **Connects:** `KS4.hrefFor('relative-formula-mass')` and `'chemical-bonds'`, with null hrefs filtered out.
- **Body prose:** hook 32 words, explainer 1 118 words, explainer 2 88 words. Total 238 words. Every block is at most 150 words before a commitment.
- **Self-check:** I rendered the lesson on all four routes in headless Chrome, on the pilot's `support.js` runtime with a source file generated by `build_ks4.build_source_js` (scratch only). Results: 0 console errors, no `undefined`/`NaN`/`{{`, and scrollWidth of 390 at 390 px. A drive confirmed the flagship's confront panel opens on box 2 and box 6, and the balancer's verdicts are right. `build_ks4.py --batch batch-2` was not run, because no batch-2 module is registered and the brief forbids editing `ks4_lessons/*.py`.
