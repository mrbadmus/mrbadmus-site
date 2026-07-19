# Bonding — 11-Page Redesign Port Map (MRB-113 Phase B)

**Status:** ✅ **BUILT — all 12 bonding pages redesigned** (B0/B1 pilots + B2–B5 + exemplar retrofit) + MRB-124 mobile fix. Verify-clean (0 critical/0 major, nanoparticles FIFA-practice major cleared, content frozen, deterministic, zero non-bonding pages touched). **AWAITING MIDE REVIEW — no commits.** See `port_progress.md` for the phase log, `PORTING.md` for spec-match compromises.
**Worktree:** `content/bonding` · **Generator:** `generate_site_v5.py` · No commits.
**Reference standard:** `giant-covalent-structures` (retrofitted onto the block system in Phase D2) + the Bonding Theory Block Library.

This is the map the whole 11-page port keys off. It is reconciled to **what is actually on
disk today** (three vanilla-JS components + a React design spec for everything else), not to
the aspirational hero list — so we lock a plan we can actually build, page by page.

The 11 pages: `chemical-bonds`, `states-of-matter`, `ionic-bonding`, `ionic-compounds`,
`properties-ionic-compounds`, `covalent-bonding`, `properties-small-molecules`, `polymers`,
`metallic-bonding`, `metals-alloys`, `nanoparticles`. (`giant-covalent-structures` is the
finished exemplar — not re-ported.)

---

## 0. Two canonical references — and the gap between them (READ FIRST)

The brief names two standards. They do **not** currently agree, and reconciling them is the
single biggest decision on this port.

**A. The LOCKED exemplar (`giant-covalent-structures.html`).** Its redesign is:
hero (Two-State Compare) → **In-Depth Theory still rendered as old `.theory-line` prose**
→ static Common-Mistake box → Key Note → Categorise-Bins activity → reveal-at-end quiz.
It does **not** use the theory block library. Its theory is plain prose in `.card` shells.

**B. The Theory Block Library (`Bonding Theory Block Library.dc.html`).** A 9-block vocabulary
(lead · feature-cards · compare-cards · step-sequence · example-callout · aside-callout ·
key-note · **mistake-check** ★ · **compare-reveal** ★) with three LOCKED rules:
- **Rule 1 — colour = meaning.** Green = conducts / mobile charge / favourable; red = does
  not / limitation; a plain fact is **neutral**. Never tint for decoration.
- **Rule 2 — pacing.** One idea per block, short lines, distinct facts on their own line.
  Past ~2 lines of prose = split into two blocks.
- **Rule 3 — parallel & mistake-first.** Compare-cards keep the same rows both sides
  (`highlightRow` marks the payoff row); misconceptions are stated first, then corrected.

**The gap:** the block library exists **only as a React `.dc.html` spec**. There is no vanilla
JS or generator code for any of the 9 blocks (confirmed: `grep` for feature-cards / compare-cards
/ mistake-check across `shared/` and the generator returns nothing). The exemplar never adopted
it. So "reshape theory into the block vocabulary" means **building the block system from scratch**
and pushing the 11 pages **ahead of the exemplar's own theory treatment**.

→ This forces **Decision 1** (§7). The rest of the map is written assuming we adopt the block
library (Path B). If Mide instead wants the 11 pages to match the exemplar *exactly* (prose
theory, Path A), the per-page hero/activity/interaction columns below still stand — only the
"theory decomposition" column is dropped.

---

## 1. What actually exists vs what must be built (honest ledger)

Nothing about the exemplar is free to copy except the four items in the first block.

**✅ Delivered vanilla JS, proven on the exemplar (reuse as-is):**
- `shared/heroes/two-state-compare.js` — **but only two renderers: `tetrahedral` + `hexLayers`
  (diamond/graphite).** No `metalLayers`, no electron-sea renderer.
- `shared/heroes/categorise-bins.js` — fully generic (bins + cards + browser shuffle). Reusable.
- Reveal-at-end quiz controller (`PILOT_QUIZ_JS` in the generator) + its CSS.
- Retokenised callout shells (`.mistake-box`, `.keynote-box`) + the `.rd` body-class gate.

**🔧 Must be built for this port (net-new, from the `.dc.html` specs):**

| Item | Needed by | Effort |
|---|---|---|
| **Theory-block system** — static blocks (lead, feature-cards, compare-cards, step-sequence, example-callout, aside-callout, key-note) as **generator-emitted HTML + CSS**; interactive blocks (**mistake-check**, **compare-reveal**) as a new `shared/heroes/theory-blocks.js` | all 11 pages (Path B) | **Large** — the backbone of the port |
| **Dot-and-Cross Stepper** → vanilla JS (`shared/heroes/dot-cross-stepper.js`) | ionic-bonding, covalent-bonding | Large (net-new hero) |
| **State Toggle Lab** → vanilla JS (`shared/heroes/state-toggle-lab.js`) | ionic-compounds | Large (net-new hero) |
| **Two-State Compare — new renderers:** `metalLayers` (pure vs alloy) + `electronSea`/`delocalised` (sea on/off) | metals-alloys, metallic-bonding | Medium (2 renderers on an existing hero) |
| **FIFA Step Reveal** → vanilla JS + interactive practice | nanoparticles | Large (net-new hero; port/adapt from Energy Changes) |
| **Shuffle-both-columns matching** — the current drag-match renders slots in source order (positional give-away, exactly the flaw the exemplar killed). The 8 true 1:1 pages need both columns shuffled | 8 pages (see §5) | Small–Medium |
| **Per-page hero configs** in `bonding-configs.js` + **generator wiring** — extend the single `if st_id == "giant-covalent-structures"` gate to a per-page table | all 11 | Medium (mechanical but broad) |

This is a substantial build, not a reskin. §8 proposes phasing it behind gates.

---

## 2. The interaction-budget rule (proposed — confirm in §7)

The exemplar carries **one interactive teaching anchor** (its hero), keeps the Common Mistake
**static**, and adds the standard activity + quiz. I propose the same budget for every page:

> **Exactly one "teaching interaction" per page, plus the always-on activity (bins/matching)
> and the reveal-quiz.**
> - **Hero pages:** the interactive hero *is* the teaching interaction. Common Mistake stays a
>   **static** `.mistake-box` (exemplar pattern). No mistake-check, no compare-reveal on top.
> - **Hero-less pages:** the teaching interaction moves into the theory body — an interactive
>   **mistake-check** (sharpest when there's a named misconception) **or** a **compare-reveal**
>   (best on structure→property pages). Never a compare-reveal alongside a comparison hero.

Result: 6 hero-anchored pages + 5 theory-interaction pages = 11. No page stacks two interactions.

---

## 3. Per-page map (the deliberate part)

Legend: **Hero** ✅ reuse · 🔧 build renderer · 🆕 build new hero · ⛔ none.
Activity: **Bins** = Categorise Bins (category sort) · **Match** = shuffle-both-columns 1:1.

| # | Page | Hero | One teaching interaction | Activity | Fixed extras |
|---|------|------|--------------------------|----------|--------------|
| 1 | chemical-bonds | ⛔ none | mistake-check | 🗂️ Bins (3: Ionic/Covalent/Metallic) | — |
| 2 | states-of-matter | ⛔ none | mistake-check | 🔀 Match (state→name) | — |
| 3 | ionic-bonding | 🆕 Dot-and-Cross Stepper (transfer, NaCl) | *hero* → static Common Mistake | 🔀 Match (element→ion) | — |
| 4 | ionic-compounds | 🆕 State Toggle Lab (NaCl, 4 states + force) | *hero* → static Common Mistake | 🔀 Match (property→explanation) | — |
| 5 | properties-ionic-compounds | ⛔ none | compare-reveal | 🗂️ Bins (3: Ionic/Metal/Both) | — |
| 6 | covalent-bonding | 🆕 Dot-and-Cross Stepper (share, H₂·Cl₂·HCl) | *hero* → static Common Mistake | 🔀 Match (molecule→bond count) | ⭐ Higher box |
| 7 | properties-small-molecules | ⛔ none | mistake-check | 🗂️ Bins (2: Simple/Giant) | — |
| 8 | polymers | ⛔ none | mistake-check | 🔀 Match (polymer→monomer) | Key Equations |
| 9 | metallic-bonding | 🔧 Two-State Compare (electron sea on/off) | *hero* → static Common Mistake | 🔀 Match (property→reason) | — |
| 10 | metals-alloys | 🔧 Two-State Compare (pure vs alloy layers) | *hero* → static Common Mistake | 🔀 Match (substance→property/use) | — |
| 11 | nanoparticles | 🆕 FIFA Step Reveal (SA:V) + practice | *hero* → static Common Mistake | 🔀 Match (nanostructure→description) | ⭐ Higher box · Triple-only |

**Distribution:** 6 pages carry a hero, 5 are deliberately hero-less. Of the 6 heroes: 2 need
only a new renderer on the existing Two-State Compare; 3 are net-new hero ports; 1 (nanoparticles)
is the FIFA port. Bins on 3 pages (genuine category sorts), shuffle-both Match on 8 (true 1:1).
No two adjacent pages share a block lineup — deliberate per content-standards §4.

---

## 4. Per-page theory decomposition (Path B)

Each page's existing theory headings, mapped to the block vocabulary. Content is frozen — these
blocks re-present the **same facts**; wording is condensed to Rule 2 pacing, no fact added or
changed. (Content-freeze mechanics in §9.)

**1 · chemical-bonds** — *decision-rule page.*
- `lead`: atoms bond to reach a stable full outer shell (like noble gases).
- `feature-cards` (3, neutral): the three drivers — metals **lose**, non-metals **gain**, non-metals **share**.
- `compare-cards` (3 cols: **Ionic / Covalent / Metallic**) — rows: *between which atoms · what happens to electrons · example*. This is the core of the page.
- `feature-cards` (3): property signatures — ionic = high MP (neutral) · simple covalent = low MP (neutral) · metallic = conducts (green). Rule 1 applies.
- **mistake-check**: "when a molecular substance melts, its covalent bonds break" → flaw → only weak intermolecular forces are overcome.
- Activity **Bins**: 3 bins Ionic / Covalent / Metallic; cards = NaCl, H₂O, Cu, MgO, CO₂ (verbatim from `matching`).

**2 · states-of-matter** — *three states + changes + symbols.*
- `lead`: all matter is solid, liquid or gas.
- `compare-cards` (3 cols: **Solid / Liquid / Gas**) — rows: *arrangement · movement · shape · volume · compressible*. `highlightRow` = movement (the concept that drives the rest).
- `feature-cards` (changes of state): melting / boiling / condensing / freezing / subliming — each a card, arrows + energy in/out.
- `example-callout` — state symbols (s)(l)(g)(aq) with the three equation examples.
- **mistake-check**: "melting/boiling must be a chemical change" → flaw → physical change, same substance (ice/water/steam all H₂O).
- Activity **Match** (1:1): state change → definition, both columns shuffled.

**3 · ionic-bonding** — *the transfer mechanism.* Hero = Dot-and-Cross Stepper (transfer).
- `lead`: ionic bonding = metal + non-metal, by electron transfer.
- `step-sequence` (the 6 steps): metal loses → non-metal gains → both full shells → metal +ion → non-metal −ion → opposite charges attract (= the bond).
- `example-callout`: NaCl, MgO, MgCl₂ dot-and-cross summaries (2.8.1→Na⁺ etc.).
- `feature-cards`: predicting charge from group (Group 1→+1 … Group 7→−1); overall compound charge = 0.
- Common Mistake **static** (hero already carries the interaction): "the bond IS the transfer" → it's the electrostatic attraction between the ions.
- Activity **Match** (1:1): element → ion formed.

**4 · ionic-compounds** — *giant lattice + conduction-by-state + solubility.* Hero = State Toggle Lab (NaCl, solid/molten/in-solution/force→shatter).
- `lead`: ions don't stay in pairs — they build a giant ionic lattice.
- `feature-cards` or `step`: lattice facts (regular 3-D alternating; each ion surrounded by 6; held by strong forces all directions).
- `feature-cards` (properties, Rule 1): high MP (neutral) · no conduction when solid (red/limit) · conducts when molten/dissolved (green) · brittle (neutral).
- `example-callout`: NaCl 1:1 ratio + solubility / AgCl precipitate.
- Common Mistake **static**: "ionic solids should conduct because they contain ions" → ions are fixed until molten/dissolved.
- Activity **Match** (1:1): property → structural explanation.

**5 · properties-ionic-compounds** — *distinct teaching point: charge magnitude → bond strength → higher MP.* Hero-less (avoids duplicating page 4's lab — see §6).
- `lead`: the giant ionic lattice explains every property; formula = simplest ion ratio.
- `compare-cards` (2 cols: **NaCl (±1) vs MgO (±2)**) — rows: *ion charges · force strength · melting point*. `highlightRow` = melting point (801 °C vs 2852 °C) — the payoff.
- `feature-cards` (Rule 1): brittle (neutral) · no conduction solid (limit) · conducts molten/dissolved (good).
- **compare-reveal**: tap a property (high MP / brittle / conducts when molten / soluble) → reveal the structural cause. This is the page's ideal interaction — pure structure→property, no comparison hero to clash with.
- Activity **Bins**: 3 bins **Ionic compound / Metal / Both** (the `matching` is an ionic-vs-metal sort; "Both" = high MP).

**6 · covalent-bonding** — *the sharing mechanism.* Hero = Dot-and-Cross Stepper (share). ⭐ Higher box (fixed furniture, on Higher/Triple variants).
- `lead`: covalent bonding = non-metals share electron pairs; each shared pair = one bond.
- `step-sequence` or `feature`: why sharing works — each atom counts shared electrons as its own → both reach full shells; shared pair attracted to both nuclei.
- `feature-cards` (single/double/triple): H₂ single · O₂ double · N₂ triple (+ H₂O/CH₄ as further examples).
- Common Mistake **static**: "covalent bonds must be weak because water boils low" → bonds are strong; weak intermolecular forces cause the low BP.
- Activity **Match** (1:1): molecule → number/type of covalent bonds.

**7 · properties-small-molecules** — *small-molecular vs giant contrast.* Hero-less.
- `lead`: simple molecular = small discrete molecules, strong covalent bonds within.
- `compare-cards` (2 cols: **Covalent bonds WITHIN vs Intermolecular forces BETWEEN**) — rows: *strength · what breaks on melting · effect on MP*. `highlightRow` = "what breaks on melting". This two-forces distinction is the whole page.
- `feature-cards`: no conduction (limit) · solubility "like dissolves like" (neutral).
- `example-callout`: HCl(g) ionising in water → H⁺(aq) + Cl⁻(aq) → conducts (dissolving can create ions).
- **mistake-check**: "simple molecules melt easily because their covalent bonds are weak" → the single most important correction on the page.
- Activity **Bins**: 2 bins **Simple molecular / Giant structure**.

**8 · polymers** — *long chains; addition polymerisation.* Hero-less; light page. Key Equations block (fixed furniture) carries the addition representation `n CH₂=CH₂ → [—CH₂—CH₂—]ₙ`.
- `lead`: polymers = many monomers joined into long chains (polymerisation).
- `feature-cards`: monomer · polymer · repeating unit `[—…—]ₙ` (vocabulary).
- `step-sequence`: addition polymerisation — C=C double bond opens → freed electrons bond the next monomer → saturated chain, no atoms lost.
- `feature-cards` (properties): solid at RT · insulator (limit) · flexible; thermoplastic vs thermosetting.
- **mistake-check**: "polymers are giant covalent structures because the chains are huge" → they're large molecules held by weak intermolecular forces (contrast with diamond).
- Activity **Match** (1:1): polymer → monomer + use.

**9 · metallic-bonding** — *the electron-sea model.* Hero = Two-State Compare, **new electron-sea renderer** (sea on → conducts + malleable; sea off → neither).
- `lead`: metallic bonding in metals and alloys.
- `step-sequence` (the 5-step model): atoms release outer electrons → become +ions → regular lattice → delocalised sea → electrostatic attraction (+ions↔sea) = the bond.
- `feature-cards` (Rule 1): high MP (neutral) · conducts electricity (good) · conducts heat (good) · malleable/ductile (neutral).
- `example-callout`: alloys — different-sized atoms disrupt the lattice → harder (steel/bronze/brass).
- Common Mistake **static**: "the metallic bond is between neighbouring atoms" → it's +ions to the electron sea; the sea is also why metals bend not shatter.
- Activity **Match** (1:1): property → structural reason.

**10 · metals-alloys** — *structure→property + conductors + alloys.* Hero = Two-State Compare, **new `metalLayers` renderer** (pure metal layers slide → soft; alloy's different-sized atoms block sliding → hard).
- `lead`: metals = giant metallic structures (regular +ion lattice + delocalised sea).
- `feature-cards` (Rule 1): high MP (neutral) · malleable/ductile (neutral) · conducts electricity + heat in the solid state (good) · high density (neutral).
- `example-callout`: key alloys + uses — steel, stainless steel, bronze, brass, aluminium alloys.
- Common Mistake **static**: "metals only conduct when molten, like ionic compounds" → metals conduct as solids (electrons already mobile); ionic carriers are ions, locked until molten.
- Activity **Match** (1:1): substance → property + use. (Conduction "sea on/off" angle belongs to page 9 — not repeated here.)

**11 · nanoparticles** — *SA:V + carbon nanostructures + uses/risks.* Triple-only, ⭐ Higher-flagged, **3 FIFA worked examples**. Hero = FIFA Step Reveal (SA:V) + interactive practice (clears the systemic FIFA-practice flag — content-standards §2).
- `lead`: nanoparticles = 1–100 nm; huge surface-area-to-volume ratio → different properties.
- `compare-cards` (2 cols: **Bulk gold vs Gold nanoparticles**) — rows: *colour · reactivity · melting point*. `highlightRow` = reactivity (the SA:V payoff).
- `feature-cards` (3): graphene · buckminsterfullerene C₆₀ · carbon nanotube (structure + one use each).
- `example-callout` (uses): TiO₂ sunscreen · silver antibacterial · drug delivery · catalysis. `aside-callout` (risks): may penetrate cell membranes; long-term effects unknown; environmental persistence.
- Common Mistake **static**: "gold nanoparticles are a different substance from ordinary gold" → same atoms; only the scale (SA:V) changes.
- **FIFA block** = the hero (3 escalating SA:V examples + student practice), replacing the old static FIFA rendering.
- Activity **Match** (1:1): nanostructure → description.

---

## 5. Activity classification (Bins vs shuffle-both Match)

Parsed from each page's `matching` block. A **category sort** (repeated left-hand labels) → Categorise
Bins. A **true 1:1** (unique left labels) → keep a matching widget but **shuffle both columns** (the
current widget renders slots in source order — a positional give-away, the exact flaw MRB-121 killed).

- **Categorise Bins (3):** `chemical-bonds` (Ionic/Covalent/Metallic), `properties-ionic-compounds`
  (Ionic/Metal/Both), `properties-small-molecules` (Simple/Giant).
- **Shuffle-both Match (8):** `states-of-matter`, `ionic-bonding`, `ionic-compounds`, `covalent-bonding`,
  `polymers`, `metallic-bonding`, `metals-alloys`, `nanoparticles`.

Cards/pairs are copied **verbatim** from the frozen `matching` field; bin labels/tints are presentation
only, adding no fact (same rule the exemplar's bins followed).

---

## 6. Deliberate non-obvious calls (justify-in-one-line)

- **`properties-ionic-compounds` gets NO hero even though the brief suggested State Toggle Lab.**
  Page 4 already owns the ion-lattice lab; repeating it on page 5 would give two adjacent pages the
  same interactive (content-standards §4 flag). Page 5's unique point is *charge magnitude → MP*, best
  carried by a `compare-cards` (NaCl vs MgO) + `compare-reveal`, and it halves the State-Toggle build.
- **`metallic-bonding` and `metals-alloys` both use Two-State Compare but different renderers.**
  Page 9 = the *bonding model* (electron sea on/off); page 10 = *structure→property* (layers slide vs
  blocked). Conduction is owned once, by page 9 — not duplicated on page 10.
- **`covalent-bonding` Dot-and-Cross is diatomic-only** (H₂/Cl₂/HCl). H₂O/CH₄/NH₃ exceed the stepper's
  2-atom geometry; they appear as static `feature-cards`, not in the hero. Flagged as a later hero
  enhancement, not a blocker.
- **No `compare-reveal` on hero pages, no second interaction anywhere.** Keeps the exemplar's
  one-anchor budget (§2).
- **Zoom/Scale Explorer (nanoparticles "one atom thick" wow) stays a gap.** Never delivered anywhere;
  FIFA is the priority because it clears the practice flag. Raise Zoom/Scale back to Design as follow-up.

---

## 7. Decisions for Mide (the gate — nothing builds until these are set)

1. **Theory depth — Path A or Path B?** *(the big one)*
   - **Path A:** match the exemplar exactly — keep theory as `.theory-line` prose; only add the hero,
     convert the activity, swap to the reveal-quiz, retokenise callouts. Small, proven, zero new block
     system. The block library is deferred.
   - **Path B (recommended):** adopt the block library — reshape theory into blocks per §4. Richer and
     what the brief asks for, but it's a **large net-new build** (§1) and pushes the 11 pages ahead of
     the exemplar's own prose theory (the exemplar would later want retrofitting for consistency).
   - *Recommendation: Path B, but phased (§8) and gated on a 2–3 page pilot before the full sweep.*

2. **Content-freeze ruling for Path B.** Reshaping a prose blob into `compare-cards`/`feature-cards`
   inherently **re-words** it (you can't drop 60 words of prose into a card row verbatim). The frozen
   source fields (`theory` etc.) stay byte-identical in the `.py` files; the block content is newly
   authored *from* them as presentation. **Confirm that "presentation reshape" may re-word frozen prose
   as long as no fact changes** — otherwise Path B is impossible and we fall back to Path A.

3. **Retokenise heroes to shipped `tokens.css`?** The `.dc.html` specs use Space Grotesk / IBM Plex +
   the old palette; the site is on Fraunces / Plus Jakarta + burnt-orange, and the exemplar already
   retokenised. *Recommend yes* — one warm system, treat the specs' fonts/colours as superseded.
   (Note: the exemplar's `redesign_css` still loads the IBM Plex/Space Grotesk font link — we should
   confirm whether that's actually used by the ported heroes or is dead and can be dropped.)

4. **Build order / scope for one sitting.** This is 6 heroes (3 net-new + 2 renderers + FIFA), a
   9-block theory system, a shuffle-both matching variant, 11 pages × generator wiring. *Recommend*
   the phasing in §8 rather than all-11-at-once — matches "slow and thorough beats fast and patchy".

5. **Per-page interaction swaps.** Any hero-less page's interaction can flip between mistake-check and
   compare-reveal. Current picks: mistake-check on chemical-bonds, states-of-matter, properties-small-
   molecules, polymers; compare-reveal on properties-ionic-compounds. Confirm or reassign.

---

## 8. Recommended phasing (behind gates)

Building all 11 in one pass is the "fast and patchy" failure mode. Proposed order, each a gate:

- **B0 — Foundations:** build the theory-block system (static HTML/CSS + `theory-blocks.js` for
  mistake-check/compare-reveal) and the shuffle-both matching variant, proven on a scratch page.
- **B1 — Block-only pilot (no new hero):** `chemical-bonds` + `properties-small-molecules`. Proves the
  block system + Bins + a hero-less page end-to-end. **Gate: Mide review.**
- **B2 — Renderer heroes:** `metallic-bonding` + `metals-alloys` (the two new Two-State renderers).
  **Gate.**
- **B3 — Net-new heroes:** Dot-and-Cross Stepper (`ionic-bonding`, `covalent-bonding`) → State Toggle
  Lab (`ionic-compounds`). **Gate.**
- **B4 — FIFA:** FIFA Step Reveal + practice (`nanoparticles`). **Gate.**
- **B5 — Remaining hero-less:** `states-of-matter`, `properties-ionic-compounds`, `polymers`. Final sweep.

Each phase: build → run generator → audit → screenshot → gate. No page is reskinned while carrying
failing content (content-standards §7).

---

## 9. Content-freeze + verification plan

- **Snapshot before porting:** the 8 protected fields (`quiz`, `matching`, `common_mistake`,
  `key_note`, `theory`, `fifas`, `higher`, `triple_only`) for all 11 pages across all four data files.
  **Byte-compare after.** Any non-deliberate diff fails. (Under Path B the block content is authored in
  generator/config code, *not* by editing these fields — so the fields stay byte-identical.)
- **`audit_content.py`:** 0 critical, 0 content majors on chemistry/bonding. Expected-to-remain:
  systemic FIFA-practice flags (only nanoparticles has maths) and the MCQ length-parity flags on these
  11 pages (that's MRB-122's bank pass, out of scope here).
- **`python3 generate_site_v5.py`:** clean run, green ticks.
- **Containment:** only the 11 pages' HTML (root + `mrbadmus_site/` mirror) + the new shared components
  change. Every other page byte-identical (the `.rd` gate stays page-scoped — every non-redesigned page
  keeps `body_class=""`).
- **Screenshots:** 3–4 representative pages (one hero-less block page, one renderer hero, one net-new
  hero, nanoparticles/FIFA). **Stop for Mide review. No commit.**

---

## 10. Recon method (for the record)

Page list, tier flags, theory/`common_mistake`/`key_note`/`matching`/`fifas`/`higher` fields parsed
directly from the four `all_subtopics_chemistry*.py` files via `CHEMISTRY_SUBTOPICS_ALL['bonding']`.
Hero capability read from `shared/heroes/*.js` (the *shipped* vanilla renderers, not the `.dc.html`
specs) and the exemplar's generated HTML + the generator's `giant-covalent-structures` gate. Block
vocabulary + rules read from `Bonding Theory Block Library.dc.html`. Nothing built; nothing committed.
