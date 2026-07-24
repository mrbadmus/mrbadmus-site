# Gate 0 Packet — Bonding v2, Phase 0 + Phase 1 (MRB-132 · MRB-133)

**For:** Mide (examiner review) · **Date:** 19 July 2026 · **Branch:** `content/bonding` (built, NOT committed — commit proposal at the end)
**Ground rule honoured:** the 8 frozen science fields are byte-identical to the run-start baseline (SHA256-verified). Everything below marked ⚑ needs your sign-off BEFORE any content changes; everything else is presentation/behaviour already built.

---

## 1 · Spec-defect list (council §8, with evidence — nothing ⚑ was changed)

**№1 — Matching drag-drop dead on touch (Ship-blocker) — FIXED this run.**
Old engine used HTML5 dragstart/dragover/drop, which never fire on iOS/Android. Replaced by TapMatch (tap-select / tap-place, same input model as the bins) on all 8 matching pages; the drag engine is fully retired from bonding output. Your students' phones can now do the activity at all.

**№2 — Bins drop-targets keyboard-inaccessible (WCAG) — FIXED this run.**
Bin headers are now real buttons: Tab reaches them, Enter/Space places the selected card, screen readers hear "Place the selected card in Diamond".

**№3 — Hero visuals silent to screen readers; 640px stepper canvas — aria FIXED; canvas noted.**
Every hero diagram now carries a spoken description that updates per state/step (e.g. "Dot-and-cross diagram: NaCl. Step 3 of 4: Transfer…"). The stepper's fixed 640px canvas still side-scrolls inside its own panel on phones (the page itself does not overflow — verified at 390px); the real fix is the Phase 3/4 practice-mode rebuild.

**№4 — ⚑ Graphene/fullerenes sit in the "Higher Tier Only" box but are NOT HT-only (Major, spec).**
Evidence: the frozen `higher` field of giant-covalent-structures reads "Graphene: a single layer of graphite… Fullerenes: C₆₀… Carbon nanotubes…". The generator only renders `higher` on Higher-tier pages, so **Foundation students never see graphene/fullerenes — yet AQA Trilogy 5.2.3.3 carries no HT marker**. Quiz Q7/Q8/Q11/Q12 (graphene/fullerene questions) ARE in the base quiz all tiers see, which makes the gap inconsistent as well as wrong. **Proposed fix (needs you):** move that text out of `higher` into the base theory (or a new theory section) so Foundation variants render it. One-field edit; I can apply it the moment you approve.

**№5 — ⚑ Nanoparticles page gaps (Major, spec).**
- Missing entirely: coarse particles (PM10) / fine particles (PM2.5), the 1–100 nm size-range recall as a tested item, and standard-form / order-of-magnitude practice.
- Quiz has **11 questions, not 12** (verified: `len(quiz) == 11`).
- Spec pill reads **5.2.3.3** — but nanoparticles is not in Trilogy at all; on Triple it is Chemistry-only **4.2.4** (bulk and surface properties). The pill number needs your call.
**Needs net-new content — drafted only after your sign-off.**

**№6 — ⚑ Correct MCQ option is almost always the longest (Minor, frozen).**
Audit rule `1-length-parity`: **319 hits across the 12 bonding pages** (0 critical, 0 major defects otherwise). Test-wise students learn "pick the long one". Fix = rewriting frozen quiz options → MRB-122, your review queue.

**№7 — ⚑ Matching answers leak (Major, trust) — engine fixed, texts PROPOSED below (§2).**
The new engine kills the position/order leaks. Word-leaks live in the frozen card texts, so the pages currently ship the frozen texts through TapMatch; §2 lists the rewrites for your approval.

**№8 — mrbEDrift ambient animation had no reduced-motion gate — FIXED.** Graphite's drifting electrons now render static under prefers-reduced-motion (screenshot in the run log); FIFA's entrance animations gated too.

**№9 — Inlined per-page engines (tech debt) — FIXED.** Quiz engine now ships once as `/shared/quiz.js`; matching runtime as `/shared/tap-match.js`. No inline blobs on bonding pages.

---

## 2 · ⚑ Proposed de-leaked matching card texts (frozen `matching` fields — nothing changed yet)

Principle: strip only the give-away word; the chemistry a student must supply stays. Where the "leak" is itself the knowledge (e.g. Steel = iron + carbon), no rewrite is proposed.

**polymers**
- Poly(ethene) card: "Monomer: ethene (CH₂=CH₂) — used in plastic bags and bottles" → **"Monomer: CH₂=CH₂ — used in plastic bags and bottles"** (the word "ethene" hands over the answer; the formula keeps the chemistry).
- PVC card: "Monomer: chloroethene (CH₂=CHCl) — used in pipes and window frames" → **"Monomer: CH₂=CHCl — used in pipes and window frames"**.
- Nylon / Protein / Starch: knowledge-matches, no change.

**ionic-bonding** (drop the ion symbol — the term side already names the element; students must derive charge from group)
- "Na⁺ — loses 1 electron to achieve noble gas configuration" → **"Loses 1 electron → 1+ ion with a noble gas configuration"**
- "Mg²⁺ — loses 2 electrons…" → **"Loses 2 electrons → 2+ ion…"**
- "Cl⁻ — gains 1 electron…" → **"Gains 1 electron → 1− ion…"**
- "O²⁻ — gains 2 electrons…" → **"Gains 2 electrons → 2− ion…"**
- "Al³⁺ — loses 3 electrons…" → **"Loses 3 electrons → 3+ ion…"**

**states-of-matter** (drop the direction arrow — supplying the direction IS the retrieval)
- Melting: "Solid → liquid — energy added, particles break free from fixed positions" → **"Energy added — particles break free of their fixed positions and can flow"**
- Boiling/evaporation: → **"Energy added — particles escape the liquid surface"** (keep)… arrow stripped
- Condensation: → **"Energy removed — particles slow and are pulled close together"**
- Freezing: → **"Energy removed — particles slow enough to form a regular lattice"**
- Sublimation: → **"No liquid stage at all — e.g. iodine, dry ice (CO₂)"** *(lower confidence — check it still reads unambiguous to you)*

**covalent-bonding** (drop the element letters; bond-count + electron-need carries the identification)
- H₂: → **"1 single bond — one shared pair between two identical atoms that each need just 1 more electron"**
- H₂O: → **"2 single bonds — the central atom needs 2 more electrons"**
- CH₄: → **"4 single bonds — the central atom needs 4 more electrons"**
- O₂: → **"1 double bond — 2 shared pairs between two identical atoms"**
- N₂: → **"1 triple bond — 3 shared pairs between two identical atoms"**

**ionic-compounds**
- "Conducts when molten or dissolved" card: "…free to move through the liquid — mobile charged particles carry the current" → **"Ions become free to move — mobile charged particles carry the current"** ("liquid" points at molten).
- "Often soluble in water" card: "Water molecules attract and surround ions…" → **"Solvent molecules attract and surround the ions, pulling them away from the lattice"** ("water" in the definition hands over the term).

**nanoparticles**
- Graphene: → **"A single one-atom-thick layer of carbon hexagons — extremely strong, conducts, potential flexible electronics"** ("graphite" stem stripped)
- Buckminsterfullerene (C₆₀): → **"A hollow sphere of carbon atoms — used in drug delivery and as a lubricant"** ("60 atoms" mirrors C₆₀)
- Carbon nanotube: → **"A rolled one-atom-thick carbon sheet forming a hollow cylinder — very strong, conducts electricity"** ("tube"/"graphene" stripped)
- Silver / TiO₂ cards: knowledge-matches, no change.

**metallic-bonding** *(lower confidence)*
- "Good thermal conductor" card contains "thermal energy": → **"Delocalised electrons carry energy rapidly from the hot end to the cold end"**. If you think "hot end" still leaks, leave as-is — the other four cards are clean.

**No changes proposed:** chemical-bonds, giant-covalent-structures, properties-ionic-compounds, properties-small-molecules (bins category sorts — card text is the knowledge itself), metals-alloys (alloy compositions are the content).

---

## 3 · Authored predict questions (Phase 1a — live now, grounded in frozen theory)

1. **giant-covalent-structures** (gates the switch to Graphite): "Graphite is pure carbon, just like diamond. Will it conduct electricity?" — Yes, it conducts / No — carbon never conducts. ✔ = conducts.
2. **metallic-bonding** (gates Electrons-pinned): "Imagine every outer electron stayed stuck to its own atom. Would the metal still conduct?" — Yes, metals always conduct / No — nothing free to carry charge. ✔ = no.
3. **metals-alloys** (gates the first Apply-force): "An alloy mixes different-sized atoms into the lattice. Under the same force, will it bend more or less than the pure metal?" — More, the gaps make it floppier / Less — the layers can no longer slide. ✔ = less.
4. **ionic-compounds** (gates Molten): "Solid sodium chloride does not conduct. What happens when it melts?" — Still no conduction / Conducts — ions free to move / Conducts — melting frees electrons. ✔ = ions. (The electrons distractor mirrors the frozen wrong-answer bank.)
5. **ionic-bonding** (gates the NaCl transfer step): "Sodium's single outer electron is highlighted. What happens to it?" — Shared between Na and Cl / Transfers completely to chlorine. ✔ = transfers.
6. **covalent-bonding** (gates the H₂ shared-pair step): "Two hydrogen atoms each need one more electron. How do both end up with a full shell?" — One gives its electron to the other / They share a pair of electrons. ✔ = share.

The FIFA hero (nanoparticles) has no predict gate by design — its practice steps already demand a commitment at every step.

---

## 4 · Per-page composition changes (all rendering-selection; frozen prose untouched)

**Deletions (Law 2 — replace, don't stack):**
- ionic-bonding: the 6-step transfer sequence AND the dot-and-cross example callout — both narrated exactly what the hero stepper animates (same molecules, same order).
- covalent-bonding: the 5-step sharing sequence (duplicate of the hero).
- nanoparticles: the static "⚽ FIFA Worked Examples" boxes (verbatim duplicate of the FIFA hero's worked spine; the frozen `fifas` field still feeds the hero).
- *Kept deliberately:* metallic-bonding's 5-step model sequence (it narrates formation of the sea; the hero shows on/off behaviour — not a verbatim duplicate). Flag if you disagree.

**Common Mistake moves (to the moment the error is born):**
- ionic-bonding, ionic-compounds, metallic-bonding, giant-covalent-structures → now render directly under the hero.
- nanoparticles → after the bulk-gold vs nano-gold compare (where "different substance" is born).
- covalent-bonding, metals-alloys → kept at end of theory (their misconceptions belong with the property content there).
- chemical-bonds, states-of-matter, properties-small-molecules, polymers → unchanged (their misconception already lives in the interactive spot-the-flaw block). properties-ionic-compounds → unchanged (end-of-theory = directly after the tap-to-reveal interactive it relates to).

**Examiner Tip placement (text untouched — approved tips; placement only):**
- Above the quiz (exam technique): chemical-bonds, states-of-matter, ionic-bonding, ionic-compounds, covalent-bonding, properties-small-molecules, polymers, metals-alloys, nanoparticles.
- Into the retrieval activity's success state (content-specific — appears on full marks): giant-covalent-structures (bins), properties-ionic-compounds (bins), metallic-bonding (TapMatch).

**Key Note:** restyled as a mono revision card with a Cover-and-recall toggle, moved to LAST content slot on all 12 pages (council §3.2 rule 8). Text untouched.

**Callout spacing:** nanoparticles' Uses callout and Risks aside were the one adjacent-callout pair; the Q4 checkpoint now sits between them. No page has two adjacent callout boxes.

**Section headings:** emoji titles → mono kickers ("Theory · read, then commit", "Retrieval · …", "Test yourself · …", "Key note · …", "Rate your confidence · …", "Stuck · ask Mr Badmus AI"). Kept: ⭐ Higher Tier Only / 🔬 Triple Science Only / 🧪 Required Practical / 📐 Key Equations (site-wide semantic markers) and the council-specified 📖/🎮/🎯 on the mode chooser.

**Kept pending Gate 1:** the standalone Ask-AI card (council split on cutting it — flagged as an option, not a decision).

---

## 5 · Inline checkpoint relocations (same frozen questions, MOVED from the quiz into the theory flow)

Question numbers are the original 1-based positions in each page's frozen quiz. The exam panel chunks are Warm-up / Exam standard / Stretch; sizes after relocation are shown (the relocated ones came out of Warm-up/Exam standard, which is why Warm-up shrinks).

- **chemical-bonds:** Q1, Q3 → after the three-bond compare table; Q6 → after the property cards. Panel: 2+3+4.
- **states-of-matter:** Q2 → after the states table; Q3 → after the changes cards; Q4 → after the state-symbols example. Panel: 1+4+4.
- **ionic-bonding:** Q1 → after the lead; Q3 → after the ion-charge cards. Panel: 2+4+4.
- **ionic-compounds:** Q3 → after the lattice cards; Q1 → after the property cards. Panel: 2+4+4.
- **properties-ionic-compounds:** Q5 → after the NaCl/MgO compare; Q2 → after the property cards. Panel: 3+4+4.
- **covalent-bonding:** Q3 → after the lead; Q4 → after the bond-count cards. Panel: 2+4+4.
- **properties-small-molecules:** Q5 → after the lead; Q4 → after the WITHIN/BETWEEN compare; Q2 → after the property cards. Panel: 2+3+4.
- **polymers:** Q5 → after the monomer/polymer cards; Q3 → after the polymerisation steps; Q4 → after the property cards. Panel: 2+3+4.
- **giant-covalent-structures:** Q4 → after the lead; Q5 → after the diamond/graphite compare. Panel: 3+3+4.
- **metallic-bonding:** Q3 → after the model steps; Q1 → after the property cards. Panel: 2+4+4.
- **metals-alloys:** Q3 → after the property cards; Q4 → after the alloys examples. Panel: 2+4+4.
- **nanoparticles:** Q3 → after the gold compare; Q4 → after the uses callout. Panel: 2+4+3 *(11-question bank — §1 №5)*.

---

## 6 · Verification summary

- Determinism: two full generator runs → 2,013 HTML files byte-identical.
- Freeze: all 4 chemistry data files SHA256-identical to the run-start baseline.
- Blast radius: zero non-bonding HTML changed.
- Interactions: 61 scripted assertions in headless Chrome across 6 pages (predict gates block-then-reveal, TapMatch flows, bins keyboard path, checkpoints, chunked check, retry-misses, persistence + delta vs best, keynote toggle, mode anchors, Combined-Foundation variant) — all pass.
- Keyboard: 154 interactive controls audited on 2 pages — every one a native button/link/summary.
- Mobile: 390px overflow probe on 4 pages — no horizontal page scroll (the stepper canvas scrolls inside its own panel only).
- Contrast: 21 colour pairs computed — all essential text ≥ 4.79:1 (AA); two pale hint tints darkened to pass during the run.
- Content audit: bonding = 0 critical, 0 major (319 minor = the frozen length-parity pattern, §1 №6; 4 info = block-lineup fingerprints).
- Reduced-motion: metallic-bonding screenshot confirms static electron sea.

## 7 · Review URLs (localhost:8899, serving `mrbadmus_site/`)

Triple Higher (fullest variant): `http://localhost:8899/triple/higher/chemistry/bonding/<page>.html` for: chemical-bonds · states-of-matter · ionic-bonding · ionic-compounds · properties-ionic-compounds · covalent-bonding · properties-small-molecules · polymers · giant-covalent-structures · metallic-bonding · metals-alloys · nanoparticles.
Suggested first look (Gate 1 pilots): **ionic-bonding** (every retrofit type) and **giant-covalent-structures** (the exemplar — drift is visible).
Variant spot-check: swap `triple/higher` for `combined/foundation` (no nanoparticles there — Triple-only).

## 8 · Proposed commit grouping (PROPOSAL ONLY — nothing committed; you push via GitHub Desktop)

Because the quiz engine file evolved Phase 0 → Phase 1 in place, a perfectly clean per-phase split isn't possible at file level. Recommended grouping:

1. **Commit 1 — "MRB-132 Phase 0: TapMatch + quiz.js extraction + keyboard/aria/reduced-motion + persistence"**: `shared/tap-match.js`, `shared/quiz.js`, `shared/heroes/categorise-bins.js`, `shared/heroes/fifa-step-reveal.js`.
2. **Commit 2 — "MRB-133 Phase 1: predict gates, exam-paper quiz, checkpoints, keynote card, mode chooser, dedup + tone (all 12 pages)"**: `shared/predict-wrapper.js`, `shared/rd-page.js`, `shared/heroes/two-state-compare.js`, `shared/heroes/state-toggle-lab.js`, `shared/heroes/dot-cross-stepper.js`, `shared/heroes/theory-blocks.js`, `shared/heroes/bonding-configs.js`, `bonding_redesign.py`, `generate_site_v5.py`, all regenerated bonding HTML + `mrbadmus_site/` mirror, `docs/redesign/` (architecture_v2.md, v2_progress.md, this packet).
   *Caveat:* the aria/reduced-motion hunks (Phase 0c) live in the three hero files in Commit 2 — noted in the commit message.

**Do not deploy until you've reviewed:** everything is behaviour students will feel. The branch is deploy-safe in the technical sense (zero non-bonding diff, deterministic), but Gate 0/Gate 1 review comes first.
