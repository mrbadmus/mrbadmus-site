# Chemistry — judgement-layer audit (distractor quality, exam register, tier integrity)

Sample ~24 pages: full Bonding unit (11 pages, the pilot), quantitative (moles, using-moles, amounts-in-equations, percentage-yield, atom-economy), rates, energy (bond-energy), electrolysis/half-equations, titrations, plus recall spot-checks. Count + duplication checks run over all ~160 page-variants.

| page | tier | dimension | severity | evidence |
|---|---|---|---|---|
| ALL dual-tier pages (~60) | Higher | Tier integrity (R5) | major | Higher quiz byte-identical to Foundation on every dual-tier page. Higher adds at most a `higher_box`; questions never change. |
| ALL shared Triple pages (~70) | Triple | Tier integrity (R5) | major | Triple quiz byte-identical to Combined on every shared page. No Triple-only depth questions; Rule 1's "≥2 Triple-only" met by zero shared pages. |
| rates-equilibrium/calculating-rates | Higher | Tier integrity (R5) | major | Same two stems both tiers ("120 cm³ in 4 minutes… cm³/s"); only difference is `higher_box=YES`. |
| chemical-changes/electrolysis-aqueous | Higher | Tier integrity (R5) | major | Identical brine/copper-sulfate stems both tiers; Higher should demand half-equation derivation, gets none. |
| quantitative/atom-economy | F & H | Distractor quality (R1) | minor | Filler "75% — calculated incorrectly"; own feedback says "No standard formula gives 75% here" — non-diagnostic. |
| quantitative/percentage-yield | F & H | Distractor quality (R1) | minor | "43% — (14 ÷ 20) × 3 = 42%": label contradicts working, "×3" not a classic error — contrived filler. |
| bonding/states-of-matter | F & H | Register + distractor (R1) | minor | Lookup stem "What state symbol for a substance dissolved in water?" with invented filler "(d) — dissolved". |
| bonding/polymers | F & H | Exam register (R1) | minor | "What is the monomer used to make poly(ethene)?" is definition-recall lookup. |

Everything else sampled passed distractor quality and register.

## Bonding unit specifics (the pilot)
Good on the dimensions mechanical checks can't judge, bad on the one they can. **Distractor quality is genuinely strong** — options encode real misconceptions ("Water has more covalent bonds — takes more energy to break" tests intra- vs inter-molecular confusion; "Diamond has ionic bonds"; steel/brass "more metallic bonds = harder"). **Register is largely exam-grade** — "Why does graphite conduct but diamond does not?", "MgO has a higher melting point than NaCl. Why?", four-state NaCl conductivity. Weak spots: `states-of-matter` and `polymers` (lookup-recall + filler). **But every Bonding page fails structurally**: only **2 questions per tier** (floor 5, a defect "full stop"), and **Foundation === Higher === Triple verbatim** on all 11 pages. If Bonding is the template other units copy, it propagates a 2-question single-difficulty quiz everywhere — so the pilot must fix content, not just reskin.

## Patterns
1. **Corpus-wide defect is structural, not editorial.** Calc-page distractors are textbook-diagnostic (invert the ratio, multiply instead of divide, forget cm³→dm³, add bond energies instead of subtract) with per-option feedback tied to the error. Register uses real command words and data/context stems.
2. **Two mechanical failures dominate:** every page ships 2 questions (handful 3–4), below floor of 5; zero tier differentiation in the quiz (F = H = Triple on every shared page, distinguished only by an optional box).
3. **FIFA thin:** calc pages `fifas=1` (vs minimum 3); non-calc pages `fifas=0`.
4. **Net:** writing bar met; volume and tier bars failed almost everywhere. Remediation is "generate 3+ more questions per page and make Higher/Triple genuinely harder," not "rewrite bad questions."
