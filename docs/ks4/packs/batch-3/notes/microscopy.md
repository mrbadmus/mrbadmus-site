# microscopy — author notes (batch 3)

## Record

```python
dict(slug="microscopy", source_file="microscopy.dc.html",
     subject="biology", topic_id="cell-biology", title="Microscopy",
     spec="4.1.1.5", family="Quantitative", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-resolve": "check", "s-bench": "required-practical", "s-draw": "check"},
     withhold=[W("What is the maximum magnification of a light microscope?", "B3-W?"),
               W("An image is 45 mm wide. The actual size is 0.009 mm", "B3-W?")])
```

Spec: 8464 4.1.1.5 / 8461 4.1.1.5 (word-for-word identical); RP1 in both specs (printed under 4.1.1.2).
Built in a scratch clone with `build_ks4.py --batch batch-3` and a temporary record: 4 pages, zero console errors at 1280 and 360 px; driven at 390 px light and dark, no overflow, no `undefined`/`NaN`/`null`/`{{` text.

## Family: QUANTITATIVE, and why

The magnification calculation carries the lesson (the architecture names it as a QUANTITATIVE example), and the spec's two other demands (magnification vs resolution, standard form/units) both feed the calculation. RP1 is carried in full here (examination R9), but RP1 is an observing/drawing practical with no variables, so it is not the lesson's demand; it sits inside the QUANTITATIVE line-up as the simulation that produces the data. BATCH-PLAN's provisional family kept.

## Line-up and demands

| block | size | demand trained |
|---|---|---|
| `s-hook` Ks4Choice (ungraded) | micro | commit to what it takes to see a ribosome |
| `s-resolve` Resolve it | **M** | predict two-dots vs one-blur for four views (LM 2 µm, LM 40 nm, LM image enlarged ×10, EM 40 nm); discriminating magnification from resolution |
| `s-rp` Required practical RP1 | block | method, "no variables", risks, slide-preparation figure |
| `s-bench` Microscope bench | **L (flagship)** | predict-gated: total magnification (eyepiece × objective) at ×10; what the view shows at ×40; then messy data — count cells across three fields of a 0.45 mm view (3, 4, 3), commit to a mean cell length, worked processing |
| `s-draw` Check the drawing | micro | identify the wrong label (chloroplast in onion epidermis) |
| `s-equation` | block | Learn it (no biology sheet): M = I ÷ A + rearrangements (source verbatim), total = eyepiece × objective, unit ladder |
| `s-think` spot-the-flaw | micro | unit mismatch (mm ÷ µm) |
| `s-calc` Ks4Cfifa | worked/do | 5 worked (FIFA 1–3 verbatim + Convert step; authored convert-first chloroplast; authored nm + standard form membrane) + 2 write-it-outs; Foundation and Higher write-it-outs differ |
| ladder | — | r1 State (frozen q4 via `K.find`), r2 Calculate 3 marks (calc kind, Foundation guard cell ×800 / Higher ribosome 20 nm), r3 Explain chain, r4 Describe 6-mark RP1 with levels |

Flagship bench → CFIFA follows the family's "simulation feeding straight into FIFA". The flagship animates (zoom on objective change, slide on field change) with a reduced-motion swap; every control is a `<button>`.

New section ids needing `block_map`: `s-resolve` → check, `s-bench` → required-practical, `s-draw` → check (`s-rp` classifies itself from its "Required practical" eyebrow).

## Misconceptions, where confronted

| misconception | where |
|---|---|
| more magnification = more detail ("zoom in and the blur splits") | Resolve it, view 3: three-beat box after the bet |
| magnifications add (×10 + ×10 = ×20) / objective only | bench gate 1 |
| a light microscope at high power shows ribosomes | bench gate 2, option 3 |
| unit mismatch, mm ÷ µm (the source common_mistake); inverted ratio; ×100 for mm→µm | `s-think` |
| onion epidermis cells have chloroplasts | `s-draw` |
| a mean from one field / mm→µm ×10 000 | bench mean commit |
| resolution = "clearer/sharper"; EM can view living cells | command-word card, r3 red herrings |
| standard-form slips | CFIFA close lines |

## Route tags

None. Examination §2: no HT and no biology-only content in this lesson; the pack's `higher` field is base content mis-tagged as Higher (R7), so nothing is badged. Foundation/Higher differ only in CFIFA write-it-out numbers and rung 2, in logic by `R.isHigher`. Eyebrow: "AQA Combined Science (8464) 4.1.1.5" on Combined, "AQA Biology (8461) 4.1.1.5" on Triple.

## Frozen items wrong — withhold (commander, please add)

- q1 — needle `What is the maximum magnification of a light microscope?` — wx2 states a false equipment fact (×200 "common low-power objective"), examination C28. Withhold all routes.
- q2 — needle `An image is 45 mm wide. The actual size is 0.009 mm` — wx3 misdiagnoses the ×4500 distractor as subtraction, examination C32. Withhold all routes.

Neither is used anywhere on the page; the bank is `K.bank(slug, R.route)` unfiltered. Usable frozen items: q3, q4 (rung 1), q5.

## Frozen source text not shown / re-cut

- key_note line "Resolution = sharpness." replaced in `keyLines` by "Resolution = the ability to distinguish two points that are close together." (C24). Other key-note lines verbatim; three lines appended (equation + units, total magnification, RP1).
- th1 "Staining kills cells…" not used (C5); toluidine blue not used (C6); SEM/TEM, electron wavelength not used (NOT-IN-SPEC).
- FIFA 2 (mitochondrion 0.15 µm) is kept verbatim as a worked example although its size is unrealistic (C20); the lesson's own examples use realistic sizes. Its Answer step carries a standard-form note.
- `rp` field: number correct; the RP block is written from the spec/examination, not from the one-line field.

## ⚑ Net-new science-bearing items

1. ⚑ Hooke named cells looking at cork in 1665; electron microscope invented in the 1930s; ribosomes first seen in the 1950s with an EM; "nearly 300 years" (examination R6 history gap).
2. ⚑ Explainer: LM passes light through a thin specimen; figures ×2000 / 200 nm / ×2 000 000 / 0.1 nm / vacuum, dead specimen (from th1/th2, re-cut).
3. ⚑ Resolve it: mitochondria 2 µm apart resolved by LM; ribosomes 40 nm apart not resolved by LM; enlarging the image adds no detail; EM resolves 40 nm. The blur is schematic (legal line says so).
4. ⚑ Hook option replies: stain adds colour not detail; ribosomes in living and dead cells alike.
5. ⚑ RP1 method, "no variables", risks (examination §5), coverslip figure.
6. ⚑ Bench: ×10 eyepiece; ×4/×10/×40 objectives; view 0.45 mm across at ×400; counts 3, 4, 3 → 0.14 mm = 140 µm (examination: typical onion cell 0.1–0.3 mm).
7. ⚑ Onion epidermis (bulb, underground) has no chloroplasts; iodine stains the nucleus yellow-brown; cytoplasm a thin layer beside a large vacuole.
8. ⚑ CFIFA authored examples: chloroplast 5 µm / 25 mm → ×5000; membrane 7 nm / 0.35 mm → ×5 × 10⁴; write-it-outs: onion cell 70 mm / 0.14 mm → ×500; cheek cell 60 µm / 45 mm → ×750; nucleus 33 mm at ×3000 → 11 µm; mitochondrion 1.5 µm / 45 mm → ×3 × 10⁴.
9. ⚑ Rung 2: guard cell 40 µm / 32 mm → ×800 (F); ribosome 0.6 mm at ×30 000 → 20 nm (H). Rung 3 chain and herrings, rung 4 levels and indicative points (from examination §5).
10. ⚑ Key fact: more magnification without more resolution only makes a bigger blur.

## New instruments / helpers

All inside the lesson's own logic: `resSvg` (two-dot view with SVG Gaussian blur), `fieldSvg` (brick-pattern field of view, deterministic per field), `slideSvg`, `drawSvg`. CSS animations `mic-in`, `mic-zoom`, `mic-pan` (prefixed, reduced-motion off). No `_ext` file.

## Body prose

Hook ~45 words, explainer 1 ~105, explainer 2 ~50: ~200 words of explainer + hook prose; longest run before a commitment ~105.

## Review fixes (1 Oct 2026)

| row | change |
|---|---|
| science A-3 | `s-think` "×3.3" reply → "That divides the wrong way, real ÷ image, and still mixes µm with mm. Magnification is image ÷ real." |
| science A-2 | Not applied: FIFA 2 (0.15 µm mitochondrion) is a frozen worked example and stays verbatim. |
| science A-1 | Left, as the reviewer advised. |
| quality Q-1 | `hookOptions[0].reply` → "More magnification alone gives a bigger blur, not more detail. Resolve it, below, tests this." |
| quality Q-2 | `#s-rp` trimmed: Variables paragraph deleted; step 2 and Risks shortened to the reviewer's text. |
| quality Q-3 | Drawing title and `drawAlt` → "Onion epidermis cells, seen at ×400". |
| quality A-1 | Convert-first worked example → chloroplast 4 µm, drawing 30 mm, ×7500 (was 5 µm / 25 mm / ×5000, which mirrored eukaryotes-prokaryotes). ⚑ |
| quality A-2 | Key-note line "Magnification = size increase." shown as "Magnification = how many times bigger the image is than the real object." |
| quality A-3 | Unit-ladder card split onto two lines ("mm ×1000 → µm" / "µm ×1000 → nm"), so it no longer wraps mid-arrow. |
| quality A-4 | Not applied (number format in the frozen key note). |

Rebuilt in a scratch clone (batch-3, 44 pages, zero console errors) and driven at 390 px: no stray text, no overflow.
