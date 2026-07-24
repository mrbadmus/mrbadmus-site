# Council Review — Bonding Unit Reimagining (12 pages)

**Date:** 19 July 2026 · **Session type:** design review + reimagining (no code changes, no commits)
**Method:** five-member council deliberation (llm-council skill), each member independently read the rendered pages and hero-module source from a distinct expert lens, then the chairman synthesised. Members: Pedagogy · Interaction Design · Visual Design · GCSE Exam-Prep · Student Engagement.
**Scope reviewed:** all 12 pages on branch `content/bonding` (`triple/higher/chemistry/bonding/*.html`), the five hero modules + theory-blocks in `shared/heroes/`, and `bonding_redesign.py`.
**The brief (Mide's verdict, treated as binding):** "One interactive at the top followed by loads of text does not work. Every page forced into one simple structure is lazy work." He wants lots of labs, many ways to learn one topic on one page, structure driven by the topic, and the highest level of what a revision page can be.
**Revoked rules:** one-interaction-per-page; uniform page architecture.
**Standing constraints:** 8 frozen science fields (interactives built FROM frozen science; net-new activity content flagged for Mide); vanilla JS, no build step; locked design tokens + WCAG AA + keyboard + reduced-motion; tier/pathway gating; generator determinism; AQA accuracy.

---

## 1. Executive summary (chairman's verdict)

**The council unanimously agrees with Mide.** The 12 pages are one page, generated twelve times. Every page is the identical sequence — [optional hero] → theory blocks → Common Mistake → Key Note → Examiner Tip → one matching/sort → 12 stacked MCQs → stars → AI chat — and the unit's problems all flow from that:

1. **All encoding at the top, all retrieval at the bottom.** A student scrolls 600–900 words without being asked to commit to anything. On ionic-bonding the hero, a static 6-step block, and an example callout say *the same thing three times in a row* — the strongest single piece of evidence for "one interactive then loads of text."
2. **Only two of the five heroes are true interactions.** The dot-cross stepper is a click-next slideshow (the student's only verb is "Next"); the state buttons print their own answers ("🔥 Molten → Conducts ✓") so the student reads verdicts instead of earning them. Nothing anywhere asks for a **prediction** before a reveal.
3. **Everything trains recognition; the exam pays for production.** No writing practice, no drawing practice (dot-and-cross diagrams *are* assessed), no formula construction (five ionic-bonding questions test a build-it procedure by multiple choice), no 6-mark extended-response practice — despite Bonding owning three of AQA Paper 1's banker 6-markers.
4. **The matching activities leak their answers** ("Monomer: ethene…" can only go on "Poly(ethene)") — solvable by word-matching with zero chemistry. Strong students clock this instantly and lose trust. Worse: the drag-drop is HTML5 DnD, which **does not work on phones at all**, and the bins drop-targets are keyboard-inaccessible — two standing-constraint violations shipped today.
5. **Nothing persists, so nothing pulls a student back.** Quiz scores evaporate; "Try again" resets all 12 instead of "retry your 3 misses"; the stars are unanchored self-report.
6. **Visually, the pages have one rhythm — box, box, box.** On nanoparticles a student scrolls six left-bordered rounded rectangles in unbroken sequence. The tone system (green/red/neutral) exists but renders mostly beige-on-beige. Meanwhile real drawn atoms (`atom()`, `bond()`, `honeycomb()`) sit imprisoned inside one hero while emoji (🧂💧🔩) stand in for the very structures the unit teaches.
7. **Spec-accuracy defects found** (flagged for Mide, not fixed — content freeze): graphene/fullerenes sit in a "Higher Tier Only" box but are **not HT-only** in AQA 5.2.3.3 — a Foundation build would gate out examinable content; the nanoparticles page is missing coarse/fine particles (PM10/PM2.5) and size-range/standard-form practice, has 11 quiz questions not 12, and its spec pill number is questionable.

**The vision the council converged on:** keep one design language (tokens, type ramp, tone-tints, the proven "instrument panel" anatomy, identical end-matter ritual) and let every page's *architecture* follow its topic's dominant cognitive demand. A page becomes a chain of short encode→act cycles: never more than ~150 words of prose before the student must commit to something — a prediction, a construction, a classification, or a written answer. Each page gets **one flagship lab, one to two mid-size activities, micro-widgets woven into the prose, and a production-grade exam ladder** — recall → apply → explain-chain → extended response. The catalogue below (§4) proposes 3–6 interactives per page; ~14 reusable vanilla-JS archetypes (§6) cover all of them.

**Highest-leverage moves, in order:** (1) fix the shipped defects (touch-dead matching, keyboard-dead bins, spec flags); (2) retrofit **predict-gates** onto the five existing heroes — the cheapest pedagogy-per-line available; (3) build the two exam-production engines (**answer-chain builder** and **write-then-self-mark**) and deploy them on the four 6-marker pages; (4) then scale the new labs page-batch by page-batch behind Mide's gates.

---

## 2. Converged critique — what is flat, templated, or wasted

### 2.1 Pedagogy
- **Encoding/retrieval geography is wrong**: a strict two-act play (all theory, then all testing). Retrieval works when the attempt interrupts encoding; parked at the bottom it becomes a comprehension check.
- **Redundancy live in production**: ionic-bonding narrates electron transfer three times (hero → static 6-step block → example callout, same molecules); covalent duplicates its stepper with a 5-step block. Textbook extraneous load.
- **The most-examined production skill has zero practice affordance**: covalent's Higher box literally says "Draw dot-and-cross diagrams for: H₂, Cl₂, HCl, O₂, N₂, CH₄, H₂O, NH₃, CO₂" — a drawing instruction rendered as a paragraph with nothing to draw on.
- **States-of-matter is the biggest single miss**: no hero on the one topic where *motion is the concept*; the heating curve — tested twice in its own quiz — exists only as a graph described in prose inside a question.
- **What must be preserved**: the `data-wrong-exp` distractor explanations are genuine misconception-driven instruction — the best pedagogy on the site; the bins engine's shuffle + grade-by-mapping anti-gaming pattern; giant-covalent-structures' two-interaction-moments shape (the healthiest page).

### 2.2 Interaction
- **dot-cross-stepper**: no prediction, no manipulation, no way to be wrong; zero replay value. Good juice (electron-flight easing), but a fixed 640px canvas that side-scrolls on phones and is silent to screen readers.
- **two-state-compare / state-toggle-lab**: the force→shatter moment is the best on the site, but each is exhausted in 3–4 clicks and the button labels give away the verdicts. The pure `RENDERERS` registry (`f(params) → DOM`) is the single most valuable architectural asset — a slider could drive these renderers tomorrow.
- **Ship-blockers found**: matching uses HTML5 drag events → **dead on iOS/Android touch**, on every page that has it; bins drop-targets are plain divs → a keyboard user can select a card and never place it; hero visuals carry no aria. Also: ~110 lines of quiz engine are inlined verbatim into every generated page — centralise before interactives multiply.
- **Same verb repeated**: metallic-bonding and metals-alloys — consecutive pages — open with the same hero archetype; chemical-bonds' two activities are both "classify."

### 2.3 Visual
- **Scroll rhythm**: box → box → box at one scale in one column; the page is over by screen 4 and the remaining ten screens are denouement (twelve identical quiz cards).
- **Callout monotony**: up to six left-bordered rounded rectangles in unbroken sequence (nanoparticles); when everything is a callout, nothing is. The tone system renders mostly `--neutral` beige — even compare-table *highlight* rows.
- **Flat hierarchy**: every section title same size, same emoji-grammar (🎯 appears twice per page for different things). Emoji do content labour (🧂 = lattice) on the page whose job is to show real structures — while drawn-atom primitives exist in two-state-compare.js.
- **Wasted astonishment**: "1 nm = one billionth of a metre" is body copy. The Key Note — the one thing a student would photograph — is the worst-designed text on every page (run-on abbreviation paragraph in yet another box).
- **Audit flag**: `mrbEDrift` ambient animation has no visible reduced-motion override.

### 2.4 Exam-prep
- **"The best MCQ-only revision unit I've seen at this level — and it still trains almost none of what AQA pays marks for on Bonding."** Command words are used correctly; several stems are near-past-paper; the distractor bank is exam gold (a ready-made corpus of "do not accept" statements). But: recognition ≠ production. Aced MCQs = having *read* the perfect answer 12 times and *written* it zero times.
- **MCQ-craft flaw**: the correct option is almost always the longest — test-wise students learn "pick the long one." (Frozen content: flag, don't fix.)
- **Missing entirely**: dot-and-cross drawing practice, blank-line formula deduction, mark tariffs/AO tagging, the three 6-mark bankers this unit owns (ionic properties; diamond-vs-graphite compare; why alloys are harder).
- **Spec defects**: graphene/fullerenes mislabelled HT-only (biggest defect — Foundation students lose examinable content); nanoparticles missing PM10/PM2.5 + size-range recall + standard-form practice, and its quiz has 11 questions; spec-pill numbering to check. All flagged for Mide's examiner review.

### 2.5 Engagement
- **A competent student's session dies at the matching activity**: the answers are printed inside the cards (word-matchable with zero chemistry). "This is for the bottom set" is worse than boring — it poisons trust in every other activity.
- **No reason to return**: scores evaporate, no best-score, no delta, no "retry your 3 misses" (the cheapest one-more-go loop in existence, missing). No curiosity gap anywhere — every page shows everything immediately in the same order.
- **Predict-before-reveal is absent site-wide**: no commitment = no stake = no payoff when right. The shatter moment is the coolest thing in the library and it *tells* you the answer first.
- **Tone**: warm but over-cheered ("PERFECT! 🏆" for clicking a stars button reads as "dad texting"). The diagnostic wrong-answer explanations are the best copy on the site — extend that voice, cut the exclamation stacking.

---

## 3. Page-structure philosophy — what replaces the template

**One design language, variable architecture.** The language that stays fixed: design tokens, type ramp, tone-tints (green = conducts/favourable, red = limit/error, amber = examiner/aside), the "instrument panel" anatomy (head / tinted callout / viz / dark mono strap) as the only panel shape for interactives, quiz mechanics, and the identical end-matter ritual (stars → AI → prev/next). What varies per page: which instruments are mounted, where, at what scale, in what order — decided by the topic's **dominant cognitive demand**.

### 3.1 The learning-mode taxonomy ("many ways to learn one topic")
| Mode | What the student does | When it's the right tool |
|---|---|---|
| **Predict–observe–explain** | commits a prediction chip *before* any reveal/state change | wrapper for every stateful interactive; cheapest mode |
| **Build-it** | constructs the artifact the exam demands (formula, diagram, structure, chain) | any procedural/production skill |
| **Worked example → faded practice** | watches a full walkthrough, then repeats with steps progressively blanked | calculations, formula deduction (FIFA's dual mode, generalised) |
| **Sort-it / classify** | tap-tap categorisation (bins model) | property↔structure discrimination |
| **Rank-it** | orders items on a ladder (melting points, sizes, boiling points) | trend reasoning |
| **Simulate / parameter-sweep** | drives a slider; structure responds continuously | continuous phenomena (heating, alloying, scale) |
| **Probe / test-it** | wires a circuit, applies a force, attaches instruments | property verification (conductivity, malleability) |
| **Spot-the-mistake** | finds the flaw in a claim or a flawed model answer | every Common Mistake box, reborn |
| **Explanation-chain assembly** | orders scrambled causal links (with red herrings) | AQA "explain" answers — they ARE causal chains |
| **Write-then-self-mark** | writes free text, reveals marking points, self-awards | 2–4 markers and 6-mark extended response |
| **Teach-it-back** | self-explains, then compares against a model answer | near-zero build cost, high yield |
| **Speed retrieval** | timed low-stakes rounds with a best score | bus-session revision; opt-in timers only |

### 3.2 Composition rules
1. **The 150-word rule.** Never more than ~150 words of continuous prose (lead + one block) before the student must commit to something. A page is a chain of encode→act cycles, ending in mixed consolidation — not encode-everything-then-test-everything.
2. **Interactive ceiling with a micro floor.** Per page: one flagship lab + one–two mid-size activities + micro-widgets ad lib + the quiz. (Three committed-response interactives above the quiz is the ceiling; a page that is all instruments has no rhythm either.) The 3–6 counts in §4 include micro-widgets.
3. **Every interactive extracts a commitment.** No passive animation, no verdict shown before a prediction. Watch-mode (worked) is legitimate only when paired with a do-mode (practice).
4. **Replace, don't stack.** Any static block whose content an interactive now teaches gets deleted from the page composition (the frozen theory text itself is untouched — this is a rendering-selection decision, listed at the gate for Mide).
5. **Callout spacing.** Never two callout boxes adjacent; one breather moment mid-page (verdict strap / display-scale fact / dark surface); Common Mistake moves to the moment the error is born and becomes spot-the-flaw where possible; Examiner Tip splits (technique → above quiz; content-specific → the relevant interactive's success state).
6. **The exam ladder ends every page**: ① recall check → ② apply (deduce/calculate) → ③ explain (chain builder) → ④ extended response (write + self-mark), tariff-tagged, with per-question persistence and "retry my misses."
7. **Serve both sessions.** A top-of-page mode chooser — 📖 Teach me · 🎮 Labs · 🎯 Test me — three anchor links, so the 10-minute bus student jumps straight to an activity and the 40-minute desk student reads in order.
8. **Key Note stays last and static** (the one stable, photographable artifact), restyled as a proper revision card with an optional cover-and-recall toggle.

---

## 4. Lab catalogue — per page

Sizes: **S** = small inline widget · **M** = mid activity · **L** = flagship lab. Every item names the misconception it kills and its frozen-content source. Items marked **⚑ net-new** contain activity content beyond the frozen fields → Mide review packet. This is a menu: per-page builds pick the flagship + 1–2 mids; micros are cheap.

### 4.1 chemical-bonds (5.2.1.1) — *the decision page; currently no hero*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Bond Decider** (flagship hero) | L | Picks two element chips from a mini periodic-table tray, **commits a bond-type prediction**, then watches the chamber resolve it — transfer arrow / shared pair / electron sea — using real drawn-atom primitives (retiring 🧂💧🔩) | "predict bonding from position" as an action; sharing-vs-transfer confusion | theory + quiz Q8 |
| 2 | Sort-the-Substance speed triage | S | Formula flashes → tap ionic/covalent/metallic; streak + best score (opt-in timer) | classification fluency | quiz stems |
| 3 | Mystery Substance | M | Property cards flip one at a time; commit a bond-type guess as early as you dare — earlier = more credit | property→bonding deduction (quiz Q6/Q9/Q11 as a game) | quiz data |
| 4 | Conductivity bench | M | Probes NaCl(s), NaCl(molten), Cu, wax; predict the bulb before each | "conducts ⇔ mobile charged particles" | theory |
| 5 | Melting-point ranking ladder | S | Orders NaCl, H₂O, Cu, diamond by MP | giant-vs-molecular energy reasoning | theory |
| 6 | Bins 3-way sort (existing) + decision-tree micro-widget | S | Keep; decision tree replaces the equivalent prose | — | existing |
| — | *Ends with a visual index: the unit map, each page as a structure thumbnail* | — | — | — | — |

### 4.2 states-of-matter (5.2.2.1–2) — *the neglected page; no hero, on the topic that IS motion*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Heating-Curve Lab** (flagship) | L | Drives a heat control; ~30 particles go lattice→jiggle→free while a temperature-time graph draws itself live — the plateaus appear as you watch. Predict-gates at each phase ("will particles get bigger / faster / further apart?"); challenge mode: place the two plateaus on a blank graph before reveal | "temperature rises during melting"; "particles expand"; the graph currently described only in prose (quiz Q7/Q11) | theory compare-rows |
| 2 | State-Symbol speed round | S | 60s opt-in: equations flash → tap (s)/(l)/(g)/(aq); best score persisted | "(aq) = any liquid" | example block + quiz Q4 |
| 3 | State-from-data widget | S | Given MP/BP, types the state at a given temperature | data-question production (AQA classic) | theory |
| 4 | Particle-diagram error-spot | S | Taps the wrong drawing among three | drawing-level misconceptions | common_mistake |
| 5 | Matching (existing) — **de-leaked** ⚑ | S | State names stripped from the definition cards | restores retrieval value | matching (rewrite flagged) |

### 4.3 ionic-bonding (5.2.1.2)
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Electron-Drag Dot-Cross** (flagship) | M | The stepper's practice mode: drags electrons from metal to non-metal, snap-to-shell, wrong-shell rejection shake; charges appear when correct. Existing stepper stays as the worked mode | passive watching → doing; transfer direction | stepper configs (already encode the electron structures) |
| 2 | **Ionic Formula Forge** | M | Adds ion tiles (Mg²⁺, Cl⁻, Al³⁺, O²⁻…) until a live charge meter reads zero; formula assembles. Round 1 fully worked (Al₂O₃), rounds 2–4 faded | "subscripts come from group numbers"; "one of each ion" (live distractors in quiz Q3/6/8/10/11) | quiz + matching fields |
| 3 | Predict-the-ion gates on stepper | S | Before each step: "Which atom loses? What charge results?" | commitment before reveal | matching data |
| 4 | Spot-the-flaw | S | The frozen mistake ("the bond IS the transfer") as a tappable flawed answer | the unit's #1 ionic misconception | common_mistake |
| 5 | Write-then-mark: the transfer→ions→attraction chain ⚑ | M | Writes the 3–4 marker; self-marks against revealed points, incl. "do not accept: transfer = bond" | production of the causal chain | theory (marking-point decomposition needs Mide) |
| 6 | Dot-and-Cross Canvas (shared with covalent; Phase 4) | L | Places electrons + charges + brackets; per-feature self-check (the actual 3 marking points) | drawing — assessed, currently untrained | stepper configs |
| — | **Delete** the duplicated 6-step block + example callout (hero teaches them) | — | — | redundancy | gate item |

### 4.4 ionic-compounds (5.2.1.3)
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Heat the Lattice** (flagship) | M | Temperature slider 25→1000 °C drives the existing lattice renderer — jitter grows, lattice breaks at 801 °C, conduction verdict flips live; state buttons become waypoints on the track | the student *causes* melting instead of selecting "molten" | state-toggle-lab renderers |
| 2 | Lattice Builder | M | Places +/− ions on a grid; adjacent like charges glow red and repel-shake; goal: stable alternating arrangement; reads the formula off the lattice | "NaCl is a molecule" (quiz Q11); giant-structure concept | theory |
| 3 | Wire It Yourself | M | Moves electrodes between three beakers (solid/molten/solution); bulb responds; predict first | conduction conditions, discovered not read | theory |
| 4 | Shatter vs bend side-by-side | S | Same force applied to NaCl and Cu lattices; predict which survives | brittle-vs-malleable contrast | existing renderers |
| 5 | Lattice-diagram → empirical formula deducer | S/M | Counts ions in a lattice picture, types the formula | AQA "deduce the empirical formula from the diagram" | theory |
| 6 | Matching — de-leaked + tap-tap engine ⚑ | S | — | touch fix + retrieval fix | matching |

### 4.5 properties-ionic-compounds (5.2.2.3) — *owns 6-mark banker №1*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **6-Mark Chain Builder** (flagship) | M | Assembles the full banker — "high MP + conducts molten not solid" — from jumbled causal links with red herrings ("delocalised electrons carry the current", "melting creates the ions" — both already in the frozen wrong-exps) | Level-1-capping conflations; linked-chain writing | theory steps + data-wrong-exp bank |
| 2 | Be-the-Examiner ⚑ | M | Marks a flawed Level-1 answer ("electrons flow through the solution") against the scheme, 0–4; examiner reveal | discrimination the examiner reports demand | common_mistake (flawed answer prose needs Mide) |
| 3 | Conductivity predictor | S | Bench reuse: 4 compounds × 3 states, predict-then-test | "ionic solids conduct" | theory |
| 4 | Charge-vs-MP ranking + HT write ⚑ | S/M | Orders NaCl/MgO/KCl by MP; Higher: writes the charge-magnitude explanation | grade 8/9 charge reasoning | higher field |

### 4.6 covalent-bonding (5.2.1.4)
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Shared-Pair Builder / valence tray** (flagship) | M | Assembles H₂O, CH₄, NH₃, O₂, N₂ from an atom tray; drags shared pairs into the gap, choosing *how many*; bonds-still-needed badge per atom; instant shell-count feedback | "carbon forms 8 bonds"; "N₂ shares one pair" (quiz Q1/Q6/Q10 distractors); the Higher box's draw-list made practicable | higher + theory |
| 2 | Strong-bond vs weak-force bins | S | Sorts statements into TRUE vs MISCONCEPTION ("O–H bonds break when water boils"…) | the unit's #1 misconception, generatively | common_mistake + quiz Q8/Q11 |
| 3 | Halogen boiling-point POE | S | Predicts bp trend F→I, commits, bar-reveal with IMF explanation | bond strength ≠ IMF strength | quiz Q11 |
| 4 | Predict gates on stepper | S | — | — | — |
| 5 | Dot-and-Cross Canvas (Phase 4) | L | H₂ → CO₂ incl. double/triple bonds at Higher; self-check overlay | drawing production | higher field list |
| — | **Delete** the duplicated 5-step block | — | — | redundancy | gate item |

### 4.7 properties-small-molecules (5.2.2.4)
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Two-Forces Tug Lab** (flagship) | M | Wagers "which breaks first?", then heats liquid water: molecules fly apart *intact* — thick dark covalent bonds visibly persist while faint dotted IMFs stretch and snap | THE most-cited misconception in AQA examiner reports for this topic, animated | theory + common_mistake |
| 2 | Boiling-point ladder | S/M | Drags CH₄, Cl₂, Br₂, I₂ (marker size = molecule size) onto a temperature ladder; reveal | "bigger molecule → stronger IMF → higher bp" as a picture | quiz Q1/Q8/Q11 |
| 3 | Be-the-Examiner ⚑ | M | Marks "the covalent bonds between methane molecules break when it boils" | production-level discrimination | common_mistake |
| 4 | Conductivity bench reuse | S | Why simple molecules never conduct | "no charged particles" | theory |
| 5 | Bins (existing) + opt-in timed mode | S | — | — | existing |

### 4.8 polymers (5.2.2.5) — *currently no hero*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Polymer Chain Builder** (flagship) | M | Taps ethene monomers: C=C pops open, chain extends across a wide strip; the repeat unit renders as a display-scale bracket [—CH₂—CH₂—]ₙ. Challenge: "chain 8 monomers — how many atoms were lost?" (answer: zero — the misconception, embodied) | addition polymerisation as the act itself; "atoms are lost when polymers form" | theory steps (become the widget's states) + key equation |
| 2 | Thermoplastic vs thermosetting heat test | S | Predicts which softens, then toggles heat on two chain diagrams; cross-links hold one | thermo-classes confusion | theory |
| 3 | Ethene vs poly(ethene) compare | S | Two-state reuse: monomer ↔ polymer, property rows flip | monomer/polymer/repeat-unit distinction | theory |
| 4 | Write-then-mark: polymer vs small-molecule bp ⚑ | M | "Relatively strong IMFs because molecules are large" — writes and self-marks | the polymer-vs-giant-covalent trap in the examiner tip | theory + examiner tip |
| 5 | Matching — de-leaked (structures → names) ⚑ | S | — | word-match leak | matching |

### 4.9 giant-covalent-structures (5.2.2.6 + 5.2.3) — *the signed-off exemplar: refine, don't rebuild; owns 6-mark banker №2*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | Predict gates on the diamond/graphite hero | S | "Before you switch: conducts — yes/no? hard — yes/no?" | commitment | existing hero |
| 2 | **Explanation-Chain Builder ×2** (flagship) | M | Assembles "3 bonds per C → spare electron → delocalised → conducts" and "weak forces between layers → slide → soft/lubricant" | "graphite conducts because it's metallic" (live distractor Q1); the compare 6-marker | theory + wrong-exp bank |
| 3 | 6-mark compare builder | M | Drags each property onto its structural cause, two columns (the compare-cards block is the answer key) | *linked* comparison = Level 3 | compare block |
| 4 | Structure Detective | S/M | Property data cards → identify diamond/graphite/graphene/SiO₂/C₆₀ | transfer-level retrieval | theory + higher |
| 5 | Bond-counting hotspot | S | Taps any carbon; its 4 (or 3) bonds highlight and count | "tie every property to bond count" (examiner tip, enacted) | hero geometry |
| — | **⚑ Spec flag:** move graphene/fullerenes out of the HT-only box (not HT in AQA 5.2.3.3) | — | — | Foundation loses examinable content | Mide gate |

### 4.10 metallic-bonding (5.2.1.5)
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Electron-Sea Workbench** (flagship) | M/L | One lattice, two attachable instruments: battery (drift becomes directional, ammeter reads) and heat source (jiggle propagates end-to-end) — student chooses the experiment | electrical vs thermal conduction, one structure two stories | drawElectronSea renderer |
| 2 | Bond-strength sweep Na→Mg→Al ⚑ | S/M | Higher-gated: switches metal; electrons-per-atom densify the sea, MP readout climbs | charge/electron-density reasoning | higher-adjacent (net-new, flag) |
| 3 | Claim clinic (mistakeCheck v2) | S | 3-claim bank: "the bond is between atoms" / "electrons belong to their own atom" / "metals melt to conduct", resettable | the frozen mistake + siblings | common_mistake |
| 4 | Conduction chain builder | S/M | delocalised electrons → free to move → carry charge/thermal energy | explain-question production | theory |
| 5 | Hammer press | S | Press-and-hold: layers slide proportionally, springy release | malleability, felt | existing metalLayers |

### 4.11 metals-alloys (5.2.2.7–8) — *owns 6-mark banker №3*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Alloy Mixer** (flagship) | M | Slider 0→20% foreign atoms; lattice re-renders, live hardness/malleability meters; then "apply force" to *verify* the meters | "alloy = compound"; converts the binary toggle into a parameter sweep | existing renderer |
| 2 | Engineer's Pick workshop | S/M | 3 briefs drawn from a pool of ~8 (aircraft wing, cutlery, propeller…) → picks a material → marked with the structural reason | the matching pairs, re-verbed as decisions with stakes | matching field |
| 3 | 6-mark chain builder: why alloys are harder | M | regular layers slide ↔ distorted layers can't | banker №3 as production | theory + example block |
| 4 | Predict wrapper on the force hero | S | "Will the alloy bend more or less?" | commitment | existing hero |
| 5 | Three-sample stress bench | S | Pure iron / steel / stainless under one force slider | comparative reasoning | theory |

### 4.12 nanoparticles (Triple-only) — *the calculational page*
| # | Lab | Size | What the student does | Kills / trains | Source |
|---|---|---|---|---|---|
| 1 | **Powers-of-Ten Zoom** (flagship) | M | Steps a strip: hand → hair → red blood cell → virus → nanoparticle → atom, log-scale bar, mono annotations (button-stepped; stacked fallback on mobile) | scale sense; "1 nm = 10⁻⁹ m" set at display scale | theory |
| 2 | Cube-Splitting SA:V sim | M | Splits a cube 1→8→64, surface faces highlight; wagers on the ratio before reveal; feeds the FIFA calc — and FIFA moves to directly after the hero (before the matching game, fixing the scrambled order) | "÷10 side → ×10 ratio" (explicit spec statement) as a picture | fifas |
| 3 | FIFA faded practice + standard-form step ⚑ | S | Existing dual-mode extended: new numbers, one answer in metres/standard form | calculation production | fifas (net-new numbers, flag) |
| 4 | Evaluate-Answer Builder ⚑ | M | Assembles benefit + risk + judgement (the three-part structure Evaluate marks require) for sunscreen/silver | AO3 evaluate discipline | quiz Q9 content (structure needs Mide) |
| 5 | Size-order classify | S | Bins reuse: coarse (PM10) / fine (PM2.5) / nano — **requires the missing content** | spec coverage hole | ⚑ net-new content — Mide gate |
| — | **⚑ Fixes flagged:** quiz has 11 questions not 12; spec-pill numbering (5.2.3.3 vs chemistry-only 4.2.4) | — | — | — | Mide gate |

---

## 5. Text strategy — no page ever reads interactive-then-wall-of-text

1. **The 150-word rule** (see §3.2): lead paragraph stays; the first commitment lands immediately after it. Hard cap on continuous prose between actions.
2. **Micro-interactions replace paragraphs that describe actions.** Any `rd-blk-steps` whose content a stepper/builder animates is deleted from the composition (ionic and covalent both violate this today). Any "draw/deduce/predict X" prose becomes the thing itself.
3. **Callout discipline**: never two callout boxes adjacent — separate with plain prose, a diagram, or a micro-widget; max one amber element per screen; dark surfaces max two per page.
4. **Common Mistake** moves to the moment the error is born and becomes spot-the-flaw where possible (covalent's bond-strength mistake goes right after "covalent bonds are strong", *before* properties).
5. **Examiner Tip splits**: exam technique → directly above the quiz; content-specific coaching → the success state of the relevant interactive (giant-covalent's "tie every property to bond count" is the chain-builder's completion message).
6. **Key Note**: last, static, restyled as a photographable revision card (index-card styling, mono type, inset surface) with a cover-and-recall toggle. Frozen text untouched.
7. **Quiz presentation**: exam paper, not cards — one continuous panel, hanging mono numbers (CSS counters), hairline rules, compact lettered options; chunked *Warm-up / Exam standard / Stretch* (4+4+4) with later sets behind `<details>`; sticky progress chip; per-set check buttons; 2–3 retrieval questions moved inline as checkpoint micro-quizzes after the theory block they test.
8. **Tone pass** (copy, not science): keep the diagnostic wrong-answer explanations verbatim; one emoji per message max; cut exclamation stacking and "Well done!" appendages; low-score messages become diagnosis + route ("4/12 — most misses were intermolecular forces. Two minutes on the compare table, then retry your 8."); stars respond with a route, not congratulations.
9. **Section headers**: retire the emoji-title grammar in favour of the mono kicker voice (`rd-hero-kicker` pattern already on the pages); emoji survive only where irreplaceable in content.

---

## 6. Component library plan (deduped, vanilla JS)

### Tier 0 — fixes and extractions (before anything new)
| Component | Size | Notes |
|---|---|---|
| **TapMatch** — matching engine replacement | M | Tap-tap select/place (bins input model). Retires HTML5 DnD entirely. **Ship-blocker: current matching is dead on touch.** All matching pages |
| Bins keyboard fix | S | Drop-targets become buttons with tabindex + Enter/Space. All bins pages |
| Hero aria pass | S | `role="img"` + generated per-state `aria-label` on all hero visuals; verify reduced-motion on `mrbEDrift` |
| **quiz.js extraction** | S | The ~110-line engine inlined in every generated page → `/shared/quiz.js` before interactives multiply |
| Score persistence | S | `quiz_best_<page>`, `lab_best_<page>` in localStorage; delta display; **"retry only my misses"** |

### Tier 1 — retrofit multipliers
| Component | Size | Consumes |
|---|---|---|
| **PredictWrapper** — commit-chip decorator for any stateful hero (`config.predict: {question, options, revealsOn}`) | S | all 12 pages; highest pedagogy-per-line available |
| mistakeCheck v2 — reset + item bank | S | all pages |
| Cover-and-recall Key Note toggle + revision-card restyle | S | all pages |
| Page mode chooser (Teach me / Labs / Test me anchors) | S | all pages |
| Quiz exam-paper restyle + chunking + sticky progress | M | all pages |

### Tier 2 — the engines
| Component | Size | Consumes |
|---|---|---|
| **ChainBuilder** — causal-link sequencer with red herrings; levels-mapped feedback | M | 6+ pages (all explain-chains and 6-markers) |
| **WriteThenMark** — textarea → marking-point checkboxes → self-award, with "do not accept" lines | M | 6+ pages |
| **SliderSim** — range input driving the existing pure renderers | M | states-of-matter, ionic-compounds, metals-alloys, polymers, properties-small-molecules, nanoparticles |
| **CircuitBench** — substances × probes × bulb/ammeter | M | 6 pages |
| **TapDragConstruct** — shared select-and-place engine (snap targets, live rule feedback) | M | lattice builder, formula forge, electron drag, valence builder, chain builder — 5 labs, 1 engine |
| **RankLadder** | S/M | 3–4 pages |
| **SpeedRound** — opt-in timed retrieval, best-score | S | 2–3 pages |
| **FormulaDeducer** — ion picker + live charge meter + typed formula | M | ionic pages |
| **BeTheExaminer** — flawed answer + scheme + 0–N award (thin layer on WriteThenMark) | S/M | 3–4 pages |
| Micro-diagram primitives — extract `atom()/bond()/honeycomb()` from two-state-compare into a shared module | S | every page's drawn vocabulary (retires content-emoji) |

### Tier 3 — flagships
| Component | Size | Consumes |
|---|---|---|
| **DotCrossCanvas** — place electrons/charges/brackets, per-feature self-check | L | ionic-bonding, covalent-bonding |
| **Electron-Sea Workbench** (battery + heat instruments) | M/L | metallic-bonding |
| **ScaleZoom** (powers of ten) | M | nanoparticles |
| **HeatingCurveLab** (SliderSim + live graph) | L | states-of-matter |

**Upgrade, don't replace:** two-state-compare (its renderer registry is the platform), state-toggle-lab (absorbed by SliderSim), bins, fifa-step-reveal (add per-wrong-answer feedback + Enter-to-check). **Replace:** the matching DnD engine. **Keep as worked-mode:** dot-cross-stepper, paired with the drag practice mode — FIFA's watch/do dual-mode pattern generalised.

---

## 7. Phased build plan (batched autonomous runs, gated by Mide)

**Phase 0 — "Make it honest" (fixes only, no new features).**
TapMatch engine replacement (touch fix) · bins keyboard fix · hero aria + reduced-motion audit · quiz.js extraction · score persistence + retry-misses.
**Gate 0 packet for Mide:** the spec-defect list (graphene/fullerenes HT box; nanoparticles PM10/PM2.5 + size-range + standard-form gap; 11-question quiz; spec-pill number; longest-answer-is-correct MCQ pattern) — all touch frozen fields, so nothing is changed without his examiner sign-off. Plus the de-leaked matching card texts (rewrites flagged ⚑).

**Phase 1 — "Sharpen what exists" (retrofits, all 12 pages).**
PredictWrapper on the five heroes · mistakeCheck v2 · quiz exam-paper restyle + chunking + inline checkpoint questions · Key Note revision card + cover-recall · mode chooser · tone pass on feedback copy · delete the duplicated static blocks on ionic/covalent (composition change; listed for approval) · callout-spacing pass.
**Gate 1:** Mide reviews two pilot pages (recommend **ionic-bonding** — has every retrofit type — and **giant-covalent-structures** — the exemplar, so drift is visible).

**Phase 2 — "Exam engines" (production practice lands).**
ChainBuilder + WriteThenMark + FormulaDeducer built; deployed on the four 6-marker/property pages (properties-ionic-compounds, giant-covalent, metals-alloys, properties-small-molecules) + ionic-bonding.
**Gate 2 packet:** marking-point decompositions, "do not accept" lines, and Be-the-Examiner flawed answers — precisely Mide's examiner skillset, cheap for him to review, and all ⚑ net-new.

**Phase 3 — "Labs at scale" (SliderSim, TapDragConstruct, CircuitBench, RankLadder, SpeedRound; page batches).**
Batch A: states-of-matter (HeatingCurveLab flagship) · ionic-compounds (Heat-the-Lattice, Lattice Builder, Wire-It-Yourself) · ionic-bonding (Formula Forge, Electron-Drag).
Batch B: covalent-bonding (Shared-Pair Builder) · properties-small-molecules (Two-Forces Tug, BP ladder) · polymers (Chain Builder).
Batch C: chemical-bonds (Bond Decider, Mystery Substance) · metallic-bonding (Workbench) · metals-alloys (Alloy Mixer, Engineer's Pick) · nanoparticles (ScaleZoom, Cube-Splitting — content additions pending Gate 0 sign-off).
**Gate per batch:** Mide reviews the batch's pages; net-new activity content itemised per page.

**Phase 4 — "Flagship polish."**
DotCrossCanvas (ionic + covalent) · Be-the-Examiner deployments · command-word ladder · exam-readiness ladder assembly + anchored stars ("You scored 10/12 and self-marked 5/6 — 4 stars fits") · bonding.html mastery map from localStorage.
**Final gate:** full-unit review against this document.

Verification at every phase: keyboard walk, touch device, reduced-motion, WCAG contrast on any new tint, Foundation/Combined variants render correctly, generator determinism (two runs, identical output), zero non-bonding pages touched.

---

## 8. Pre-build defect list (found during review; all gated, none fixed)

| # | Defect | Severity | Where |
|---|---|---|---|
| 1 | Matching drag-drop dead on touch devices (HTML5 DnD) | **Ship-blocker** | every matching page |
| 2 | Bins drop-targets keyboard-inaccessible | **WCAG violation** | every bins page |
| 3 | Hero visuals silent to screen readers; fixed 640px stepper canvas side-scrolls on phones | Major | dot-cross-stepper et al. |
| 4 | Graphene/fullerenes in "Higher Tier Only" box but not HT in AQA 5.2.3.3 — Foundation build would gate out examinable content | **Major (spec)** ⚑ | giant-covalent-structures |
| 5 | Nanoparticles: no coarse/fine particles (PM10/PM2.5), no size-range recall, no standard-form practice; quiz has 11 questions; spec-pill numbering | Major (spec) ⚑ | nanoparticles |
| 6 | Correct MCQ option is almost always the longest | Minor (frozen) ⚑ | across pages |
| 7 | Matching answers leak (word-matchable) | Major (trust) ⚑ | most matching pages |
| 8 | `mrbEDrift` ambient animation: no confirmed reduced-motion override | Minor | two-state-compare |
| 9 | ~110-line quiz engine + matching JS inlined per generated page (~96 files) | Tech debt | generator output |

⚑ = touches frozen content → Mide's examiner review before any change.

---

## 9. Dissents and trade-offs (preserved, not smoothed over)

- **How many interactives is too many?** The brief says 3–6 per page. Pedagogy caps *committed-response* interactives at 2–3 per session ("beyond that you get novelty-seeking clicking"); Visual wants one superb moment over four adequate ones; Engagement caps at three above the quiz ("five toys is a fidget spinner"). **Chairman's ruling:** 1 flagship + 1–2 mids + micro-widgets + the quiz ladder — which lands inside the brief's 3–6 when micros are counted. The catalogue is a menu, not a per-page mandate.
- **Sims vs marks.** Exam-Prep dissents from lab-maximalism: "the heroes earn ~0 additional marks once the concept is grasped; the marginal hour goes to writing/drawing practice." Accepted in sequencing: the exam engines are Phase 2, before the lab batches in Phase 3.
- **Not everything becomes a sandbox.** Interaction Design dissents from universal direct manipulation: a linear worked sequence is *correct* for first exposure; the failure was having no do-it-yourself counterpart. Standardise FIFA's watch/do dual mode, not universal draggability.
- **Refused outright:** free-form electron-shell physics sandbox (students can build AQA-false configurations faster than we can validate); WebGL/3D lattices (build cost, no-build-step, accessibility cliff); parallax/scroll-jacking; XP/points/badges/streaks (the weekly challenge owns competition; page-level points inflate to meaninglessness); page-level leaderboards (weak students would avoid pages); forced timers (opt-in always — anxious students shut down).
- **Pedagogy defends the MCQ bank against replacement** — its misconception-tagged distractors are the best pedagogy on the site; upgrade inputs and presentation, don't gamify it. Exam-Prep concurs and would mine the wrong-exp bank as a ready-made corpus of "do not accept" statements.
- **Batch quiz check stays** (exam-realistic) with a per-set check compromise; Engagement's "retry my misses" accepted as the missing loop.
- **Engagement would cut the standalone "Ask Mr Badmus AI" section card** (the FAB already exists; that scroll position should hold "retry your misses"). Not unanimous — flagged as an option at Gate 1.
- **Honest risk (Visual):** per-page identity multiplies QA surface (12 layouts × mobile × reduced-motion × keyboard). Mitigation: every page's "unique" visual is composed from one shared drawn-primitive module — variety in arrangement, unity in material.
- **localStorage-only persistence is accepted as-is** — per-device, wipeable, no ceremony; keys are schema-ready if per-user persistence arrives later.

---

## Appendix — full member reports

The five member reports are preserved verbatim below for the record.

### A. Pedagogy

**Critique.** The encoding/retrieval geography is wrong: every page is a strict two-act play — all encoding at the top (hero + theory blocks), all retrieval at the bottom (matching, 12 MCQs) — with 600–900 words between where nothing asks for commitment. Retrieval practice works because the attempt interrupts encoding while the memory is labile; parked after the theory it becomes a comprehension check. Redundancy is live in production: on ionic-bonding the dot-cross-stepper narrates electron transfer, immediately followed by a static 6-step block saying the same six things in the same order, then an example callout restating the same molecules a third time; covalent duplicates its stepper with a 5-step block. The single most-examined production skill has zero practice affordance: covalent's Higher box says "Draw dot-and-cross diagrams for: H₂, Cl₂, HCl, O₂, N₂, CH₄, H₂O, NH₃, CO₂" — a drawing instruction with nothing to draw on. Four of ionic-bonding's twelve MCQs test the charge-balancing procedure by recognition. States-of-matter is the biggest miss: no hero on the topic where motion IS the concept, and the heating curve — tested twice in its own quiz — exists only as a graph described in prose. Genuinely good and to be preserved: the data-wrong-exp distractor explanations (real misconception-driven instruction), the bins engine's anti-gaming guarantees, and giant-covalent-structures' shape (hero → theory → mid-page sort → quiz — two interaction moments at different depths). Weak: the ionic matching is surface-matchable; the star rating is an unanchored judgment-of-learning; the Common Mistake box is passive prose about an error the student hasn't confronted.

**Philosophy.** Structure follows the topic's dominant cognitive demand. Modes: predict-observe-explain (commit before reveal — cheapest upgrade to every toggle/stepper); build-it (generation effect; the only mode that trains production); worked example → faded practice (mandatory for procedures); sort-it; spot-the-mistake (what Common Mistake boxes should become); explanation-chain assembly (AQA explain answers are causal chains); teach-it-back; consolidation retrieval. Interleaving rule: encode → act within ~150 words. Where more interactivity would HURT: passive animation (the hero-then-text problem in fancier clothes); stacked heroes (split attention); interactivising the Key Note (students need one stable artifact); free-exploration sandboxes (high extraneous load for novices); adding without deleting (ionic's triple redundancy) — every interactive that covers a static block's content replaces that block.

**Per-page (deep on four):** ionic-bonding — Ionic Formula Forge (charge meter to zero, worked→faded; kills "subscripts from group numbers"), predict-the-ion gates on the stepper, spot-the-flaw on "the bond IS the transfer", delete the duplicated step block. covalent-bonding — Shared-Pair Builder (choose how many pairs; kills "carbon forms 8 bonds"), strong-bond/weak-force TRUE-vs-MISCONCEPTION bins, halogen bp predict-reveal, delete duplicated steps. states-of-matter — Particle Chamber with discrete predict gates ("will particles get bigger, faster, or further apart?"), Heating-Curve Lab (predict each segment; the page's highest-value addition), state-symbol tagger. giant-covalent — predict gates on the hero, explanation-chain builder (two chains), structure detective, keep the mid-page bins as the pattern the other 11 should copy. (Brief proposals for the remaining eight as merged into §4.)

**Text strategy.** Hard cap ~150 words before an action; steps-blocks duplicated by interactives get deleted; Common Mistake moves to the moment of formation; Examiner Tip splits (technique above quiz, content into interactive success states); Key Note last, static, with cover-and-recall; anchor the stars against quiz evidence.

**Dissents.** 2–3 committed-response interactives per page is the ceiling. Passive/ambient animation is extraneous load dressed as engagement. Cut the duplicated blocks and the surface-matchable drag-match. Defend the 12-MCQ bank. States-of-matter, not the flashy bonding pages, is where the first new engineering should go.

### B. Interaction Design

**Critique.** Of the five heroes, only two are interactions; the rest are slideshows with buttons. dot-cross-stepper: the only verb is "Next"; the electron moves itself; no prediction, no way to be wrong; zero replay; fixed W=640 canvas side-scrolls on phones; viz is silent to screen readers. two-state-compare / state-toggle-lab: the force button is the best moment on the site (cause and effect within 700ms) and the pure RENDERERS registry (f(params) → DOM) is the most valuable architectural asset — but each is exhausted in 3–4 clicks and the button labels are the answers ("🔥 Molten → Conducts ✓"): the student reads verdicts, never earns them. categorise-bins: strongest true interaction (tap-tap works on touch and mouse; shuffle kills memorisation; grading by mapping) but has a real keyboard bug — bins are plain divs with click handlers; a keyboard user can select a card and never place it. fifa-step-reveal: pedagogical high-water mark (dual worked/practice modes, gated steps, careful input normalisation); gaps: one static wrong-answer string regardless of which wrong answer, and Enter doesn't submit. mistakeCheck is one-shot with no reset on a revision site. The matching drag-drop is broken on touch — raw HTML5 dragstart/dragover/drop does not fire on iOS/Android; every matching page is a dead panel on phones; also keyboard-inaccessible, and the pool scramble is baked into the HTML (static across visits). The MCQ quiz UX is good (per-wrong-option explanations, reshuffle on retry, real buttons); note the ~110-line engine is inlined into every generated page. Page-level: chemical-bonds has no hero and two classify-verb activities; metallic-bonding and metals-alloys — consecutive pages — open with the same hero archetype.

**Taxonomy.** Predict-then-reveal (S, wrapper); parameter-sweep slider (M — renderers already pure); tap-to-construct (M); probe/circuit test (M, huge reuse); classify (S, exists); sequence/rank (S/M); stress-test (S, exists); scale-zoom (M); goal puzzle (S on a sim); spot-the-error (S, needs reset+bank); sandbox (L — mostly refuse). Touch/keyboard parity rule: the bins tap-tap model is the canonical input pattern — drag-and-drop without drag events; nothing new uses HTML5 DnD.

**Per-page (deep on four):** chemical-bonds — Bond Decider (pick elements → commit prediction → chamber resolves), conductivity bench, Mystery Substance (commit early for more stars), MP ranking ladder. ionic-compounds — Heat the Lattice (slider replaces state buttons; student causes melting), Wire It Yourself (three beakers, one circuit), Lattice Builder (like charges repel-shake; goal = alternating arrangement; kills "NaCl is a molecule"), shatter-vs-bend side-by-side, replace the DnD matching (ship-blocker). metallic-bonding — Electron-sea workbench (battery + heat instruments), bond-strength sweep Na→Mg→Al (HT, flag), claim clinic, hammer press. metals-alloys — Alloy Mixer (0→20% slider, live meters, verify with force), alloy workshop briefs, three-sample stress bench, predict wrapper on the force button. (Others as merged into §4.)

**Component plan.** Order: (1) matching→tap-tap replacement (fix first — broken on touch); (2) bins keyboard fix; (3) PredictWrapper (highest pedagogy-per-line); (4) SliderSim (one module, six pages); (5) CircuitBench (six pages); (6) TapDragConstruct (five labs from one engine); (7) RankLadder; (8) mistakeCheck v2 + quiz engine extraction. Upgrade: two-state-compare, state-toggle-lab, bins, fifa. Replace: matching DnD. Keep dot-cross-stepper as worked mode paired with a drag practice mode — FIFA's dual-mode pattern generalised.

**Dissents.** Cheap beats rich at the margin: PredictWrapper on five heroes buys more learning than one new L-size sim; retrofit before building. Not everything becomes direct manipulation — a linear worked sequence is correct for first exposure. Refuse: free-form electron sandbox (emergent AQA-false states), WebGL/3D, points/streaks inside labs. Batch quiz check stays. Non-negotiables before features: touch-dead matching, keyboard-dead bins, screen-reader-silent heroes. Centralise the per-page inlined JS before the interactive count triples.

### C. Visual Design

**Critique.** Chemical-bonds walked viewport-by-viewport: one rhythm — box, box, box — at one scale in one column; over by screen 4; more than half the page is denouement (twelve identical quiz cards). The tone system is well-built and barely used: 5 of 6 feature-cards neutral; compare-table highlight rows tone-neutral; beige-on-beige. The callout stack does the opposite: nanoparticles runs six left-bordered rounded rectangles in unbroken sequence, four red-ish; left-border + 12px radius + padding is the entire compositional vocabulary. Emoji-title sameness flattens hierarchy (🎯 twice per page); emoji do content labour (🧂💧🔩) on the page whose job is showing real structures — while atom()/bond()/honeycomb() sit imprisoned in one hero. The two-state-compare panel is the best object in the system — it has anatomy (head/callout/viz/strap); the page around it does not. Three pages have no hero; chemical-bonds — the front door — is the flattest page in the unit. Nanoparticles' pacing is scrambled (hero does the SA:V calc; FIFA re-does it after the matching game). Wasted moments: "1 nm = one billionth of a metre" as body copy; the Key Note is the worst-designed text on every page. Flag: mrbEDrift has no visible reduced-motion override.

**Philosophy.** One design language, variable architecture: tokens, type ramp, tone-tints, one anchor anatomy (the instrument panel). Pacing contract per page: opener moment (hero instrument or display-scale typographic fact); alternate dense/light — never two callouts adjacent; one mid-page breather; ritual end-matter unchanged. Three sizes of interactive: hero instrument (one per page max), mid widget (1–2), micro widget inline in prose — the micro tier is missing entirely and is the cheapest to build. Colour as meaning extends to lab states (context-blue for cold/solid, accent-wash warmth for heat) without stealing green/red semantics. Pure-CSS devices: sticky pinned diagrams (disable <900px), button-stepped scroll-snap zoom (nanoparticles only), grid-template-areas macro-layouts, CSS counters for exam numbering, native details/summary. Avoid: parallax, scroll-jacking, sticky on short mobile viewports. Motion: state-change transitions only; ambient drift legitimate once per site (metallic-bonding) behind prefers-reduced-motion with a static fallback.

**Per-page identities.** chemical-bonds = the which-bond triage instrument + mini drawn diagrams in the compare columns + ends with a visual unit map; states-of-matter = particle motion with temperature as an annotated axis; ionic-bonding = the transfer step-through at large scale; ionic-compounds = lattice assembly; properties-ionic = the test bench (force → like charges align → shatters red); covalent = overlapping-shell shared pairs + a dot-cross gallery row; properties-small-molecules = the two-forces diagram (thick dark internal bonds, faint dotted IMFs; heat separates whole molecules) + a bp number line where marker size = molecule size, with the WITHIN/BETWEEN table sticky-pinned; polymers = chain-building with the repeat unit as a display-scale bracket device, the one earned wide bleed; giant-covalent = the exemplar, leave it; metallic = the drifting sea's one home; metals-alloys = A/B where odd-sized atoms visibly jam the layers; nanoparticles = the orders-of-magnitude zoom + cube-cutting visual before FIFA formalises it + the gold colour-flip as a startling moment.

**Quiz & text.** Exam paper, not cards: continuous panel, hanging mono numbers via counters, hairline rules, compact lettered options; chunk into Warm-up/Exam standard/Stretch with later sets behind details; sticky progress; per-set check; 2–3 questions moved inline as checkpoints. Key Note becomes the designed revision card. Cap adjacent callouts at one; amber earns its keep only if nothing amber is within a screen.

**Dissents.** "LOTS of labs" is a pacing trap — one superb moment beats four adequate ones. Coherence anchors non-negotiable: instrument anatomy, tone tokens, type ramp, identical end-matter (a ritual ending is a feature). Red lines: no parallax, no scroll-driven animation, horizontal scroll only with stacked fallback, dark surfaces max two per page, retire emoji headings for mono kickers. Honest risk: per-page identity multiplies QA surface — mitigate by extracting the drawn primitives into one shared module: variety in arrangement, unity in material.

### D. GCSE Exam-Prep

**Critique.** The best MCQ-only revision unit I've seen at this level — and it still trains almost none of what AQA pays marks for on Bonding. Good: correct command words (Explain/Deduce/Predict/Suggest/Compare/Evaluate); near-past-paper stems (X²⁺/Y³⁻ formula deduction; four-forms conduction); a misconception-driven distractor bank ("the transfer IS the bond", "electrons flow through solutions", "covalent bonds snap when the crystal shatters") worth more than the questions themselves. Problems: (1) everything is recognition, the exam is production — Paper 1 Bonding marks come from written causal chains, dot-and-cross drawing, blank-line formula deduction, and the levels-marked 6-marker (structure-property comparison is a banker); a student who aces the MCQs has read the perfect answer 12 times and written it zero times; (2) the correct option is almost always the longest and most complete (checked across all four pages) — test-wise students learn "pick the long one"; (3) no drawing practice anywhere though dot-and-cross IS assessed (3 marks both tiers); (4) formula deduction is choose-not-construct; (5) no tariffs/AO tags/timing; (6) stars are unanchored confidence — the least predictive metacognitive measure. Spec findings: graphene/fullerenes are NOT HT-only (Trilogy 5.2.3.3 carries no HT marker) yet sit in an HT-only box — Foundation students would lose examinable content — my single biggest defect; nanoparticles is missing coarse/fine particles (PM10/PM2.5), the size-range recall, standard-form/order-of-magnitude practice, and the explicit "÷10 side → ×10 ratio" statement is only implicit; its quiz is 11 questions; the spec pill number is questionable (nanoparticles is chemistry-only 4.2.4). Assigned-page coverage otherwise solid, including genuine AO3 asks (model limitations) and beyond-minimum charge-magnitude reasoning that is exactly what grade 8/9 questions probe.

**Exam-grade interactives.** Write-then-mark (textarea → marking-point checkboxes → self-award; theory/key_note supply points, common_mistake supplies "do not accept"; decomposition needs Mide — precisely his skillset). 6-mark answer builder (jumbled causal links + red herrings mined free from the frozen data-wrong-exp bank; feedback maps to levels descriptors). Formula deducer with live charge balance (LCM-of-charges as production). Dot-and-cross canvas with per-feature self-check (electron count / charges / brackets — the actual marking points; bonding-configs already encodes the electron structures). Be-the-examiner (flawed answers manufactured from the frozen mistake corpus; trains the discrimination examiner reports demand). Command-word ladder (State 1 → Explain 3 → Evaluate 6, same context).

**Per-page:** ionic-bonding — dot-cross canvas (NaCl, MgO, MgCl₂), formula deducer, write-then-mark on the transfer→ions→attraction chain with "transfer = bond" as do-not-accept; Foundation scaffolded shells, Higher X²⁺Y³⁻ + Al₂O₃ + model-limitations write. properties-ionic — 6-mark chain builder on the banker (lattice → strong electrostatic forces → all directions → much energy; solid fixed vs molten free), be-the-examiner on "electrons flow through the solution", HT data question on MP vs charge. giant-covalent — the compare 6-marker as a property→cause mapping builder; write-then-mark on "why does graphite have a high MP though soft" (the best question on any of my four pages); move graphene/fullerenes out of the HT box + Foundation-accessible uses matcher. nanoparticles — typed SA:V table (10/1/0.1 nm) forcing the ÷10→×10 statement into production; evaluate-builder (benefit + risk + judgement); add the missing PM content + standard-form drill (net-new, Mide). Brief for the rest as merged into §4. Assessment architecture: one 2-question mini-check after each theory block (interleaved recall of the previous block); tariff-tagged item bank (~4 recall AO1 / ~4 apply AO2 / ~4 explain AO2-3) with tariffs displayed; per-question persistence + "retry only my wrong answers" (the single cheapest high-value change); the four-rung exam-readiness ladder; stars earned against ladder evidence.

**Dissents.** Fun labs don't convert: the marginal build-hour goes to writing/drawing practice, where 135 students will actually gain grades. Matching/card-sorts are the weakest activity on these pages — warm-ups only, don't multiply them. Ruthless priority: (1) spec fixes; (2) write-then-mark + chain builder on the four property pages; (3) dot-and-cross canvas; (4) formula deducer; (5) be-the-examiner. One defence of the status quo: mine the frozen wrong-exp bank — it's a signed-off corpus of "do not accept" statements and flawed answers.

### E. Student Engagement

**Critique.** A real Year 11 at 8:40pm on states-of-matter: no hero; the first screen is the same solid/liquid/gas table that's in their exercise book, on Bitesize, and on the classroom wall; nothing asks them anything for two screens; the one mistakeCheck is one click, one reveal, dead forever. Engagement dies at the matching: the answers are printed inside the cards ("Monomer: ethene… plastic bags" → Poly(ethene) by literal word-matching; "Liquid → solid — energy removed" can only be Freezing) — a student with zero chemistry scores 5/5. Teens clock it instantly and file the activity as "for the bottom set" — worse than boring, it's insulting, and it poisons trust. The quiz is the best thing on the pages (wrong-answer explanations are genuinely good teaching; reshuffle on retry shows care) but: batch-check means a student lost by Q3 gets no feedback for nine more questions; the score evaporates — no best, no delta, no reason to return but guilt; "Try again" resets all 12 instead of "retry your 3 misses" — the cheapest one-more-go loop in existence, missing. metals-alloys' hero is the right instinct but a 2-click experience; the ⚡ shatter is the coolest thing in the library (breaking things is universally fun at 15) but the bulb verdict tells you the answer before you've guessed — no prediction = no stake = no dopamine. Replayability: quiz moderate, matching zero, mistakeCheck zero, heroes low. Curiosity gap: none anywhere. Reason to return: only the self-reported stars.

**Philosophy.** What motivates this cohort, in order: exam fear channelled into visible progress ("11/12, up from 7"); diagnostic honesty over praise (they smell hollow "PERFECT! 🏆" for clicking a button); one-more-go loops (≤90s attempt, best-score visible, restart one tap — the weekly challenge already proves it); agency ("skim → test me" vs "teach me from zero" are the same student on different days); low-stakes destruction and prediction. What backfires: points-for-clicking, streak guilt (a Year 11 who missed 4 days before a mock does not need a broken-streak notification), forced fun, any page-level leaderboard (weak students would avoid pages). Session realism: the 10-minute bus session wants one activity and a score; the 40-minute desk session wants theory → labs → quiz → retry misses; serve both with a three-link mode chooser (📖 Teach me · 🎮 Labs · 🎯 Test me) — nearly zero build.

**Per-page (deep on four):** states-of-matter — heating-curve lab with challenge mode (place the plateaus blind); 60-second state-symbol speed round with localStorage best; de-leak the matching. properties-small-molecules — two-forces tug lab with a "which breaks first?" wager gating the slider; boiling-point drag ladder; keep the bins, add opt-in timed mode. polymers — snap-together polymerisation (sandbox then challenge: "chain 8 — how many atoms lost?" answer zero, the misconception embodied); thermoplastic-vs-thermosetting predict-then-heat; matching de-leak (structures only). metals-alloys — hero challenge mode (wager, then a 3-round engineer's-pick from a pool of ~8 scenarios so each run differs); conductivity duel (metal vs ionic solid, which bulb lights). Ecosystem (localStorage only): quiz_best/lab_best keys beside star_; deltas at quiz end; a 12-tile mastery map on the bonding hub page — the visible-mastery pull that brings students back to the unit; a soft completion nudge routing to the weekly challenge.

**Tone.** Current voice is teacher-writes-what-teacher-thinks-teens-like ("You'll be flying! 🚀" reads as dad texting) — not fatal (Mr Badmus is a real, known teacher; that buys authenticity) but over-cheered. Keep the diagnostic wrong-answer explanations exactly as written — the best copy on the site. One emoji per message max; keep the wayfinding section emojis; cut exclamation stacking and "Well done!" appendages ("✅ Correct" alone reads more confident). Low-score messages become diagnosis + route. Reframe mistakes as intel ("What is the flaw in this reasoning?" is a strong, respectful frame — extend it). Stars: respond with a route, never congratulate the rating.

**Dissents.** These proposals are a menu, not a spec: one flagship + one speed/retrieval + the quiz; three interactives max above the quiz. No XP/points/badges — best-scores and deltas only, personal and honest. Timers opt-in always. The matching de-leak matters more than new toys — it's the one thing actively damaging credibility with strong students, and it's a content edit (flag the rewrites). Cut the standalone Ask-AI section card (the FAB exists; that position should hold "retry your misses"). localStorage fragility is acceptable — no ceremony around it.

---

*End of council record. No code was changed; no commits were made. Next step: Mide reviews §1 (verdict), §7 Gate 0 packet (spec defects — examiner sign-off needed), and the §4 catalogue as the menu for the build.*
