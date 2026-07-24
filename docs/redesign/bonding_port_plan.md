# Chemistry Bonding — Redesign Port Plan (MRB-113, Phase 2 pilot)

**Status:** Phase A recon complete. **HELD for Mide's approval before any porting (Phase B).**
**Worktree:** `content/bonding` · **Generator:** `generate_site_v5.py` · No commits until reviewed.

This is the map the whole downstream port keys off. It is deliberately reconciled to
what Design has actually delivered, not to the aspirational archetype list — because the
pilot's job is to lock a pipeline we can trust, not to promise interactives that don't exist yet.

---

## 0. Precondition — MRB-118 (graphene at Foundation): ✅ CONFIRMED

The amended `giant-covalent-structures` content is present in the **Combined Foundation base**
file (`all_subtopics_chemistry.py`), so it flows to every tier/pathway:

- Graphene, fullerenes, buckminsterfullerene (C₆₀) and carbon nanotubes all appear at Foundation
  (Test Yourself Q5 graphene, Q6 buckminsterfullerene, Q7 nanotubes; key note references "one atom thick").
- These are in the **base** file → they are NOT gated behind Higher/Triple. Foundation students see them.

Safe to proceed with recon. (Note: the theory body still has three headings — *Giant Covalent
Structures / Diamond / Graphite* — with graphene/fullerene material carried in the key note and
Test Yourself. That is a content-shape observation, not a port blocker, and content is frozen.)

---

## 1. Authoritative page list (from generator source, not the design map)

The design map (`bonding_pilot_design_map.md`) imagined 14 pages. **The generator actually has 11
Combined pages + 1 Triple-only page = 12.** Several of the design map's separate pages are *merged*
in the real source. This plan is locked to the real source.

| # | id | spec (source label) | Tier reach | Higher box | Merges the design-map's… |
|---|----|----|----|----|----|
| 1 | `chemical-bonds` | 5.2.1.1 | all | — | — |
| 2 | `ionic-bonding` | 5.2.1.2 | all | — | — |
| 3 | `ionic-compounds` | 5.2.1.3 | all | — | — |
| 4 | `covalent-bonding` | 5.2.1.4 | all | ⭐ yes | — |
| 5 | `metallic-bonding` | 5.2.1.5 | all | — | — |
| 6 | `states-of-matter` | 5.2.2.1–5.2.2.2 | all | — | states of matter **+ state symbols** |
| 7 | `properties-ionic-compounds` | 5.2.2.3 | all | — | — |
| 8 | `properties-small-molecules` | 5.2.2.4 | all | — | — |
| 9 | `polymers` | 5.2.2.5 | all | — | — |
| 10 | `giant-covalent-structures` | 5.2.2.6 | all | ⭐ yes | diamond/graphite/silica **+ graphene/fullerenes** |
| 11 | `metals-alloys` | 5.2.2.7–5.2.2.8 | all | — | metals & alloys **+ metals as conductors** |
| 12 | `nanoparticles` | 5.2.3.3 (source label) | **Triple only** | ⭐ yes | nanoparticles |

**Tier/pathway facts (verified against the four data files):**
- Higher-tier box populated on exactly **3** pages: `covalent-bonding`, `giant-covalent-structures`, `nanoparticles`.
- **No page** carries a populated `triple_only` box. `nanoparticles` is a whole **Triple-only page** (absent from the two Combined files).
- **No page** has a Required Practical. Only `polymers` has a `Key Equations` entry (the addition-polymerisation representation — not a calculation).
- Test Yourself counts: 10 per page on Combined, 12 on Triple (nanoparticles 10/11). All already at/above the content-standard floor.

---

## 2. Hero availability audit — what actually exists on disk

The brief names **5 heroes + FIFA**. Reality on disk:

| Hero | Status | Source file |
|---|---|---|
| **State Toggle Lab** | ✅ delivered | `~/Desktop/Bonding Hero 1 - State Toggle Lab.dc.html` |
| **Dot-and-Cross Stepper** | ✅ delivered | `~/Desktop/Bonding Hero 2 - Dot-and-Cross Stepper.dc.html` |
| **Two-State Compare** | ✅ delivered | `~/Desktop/Bonding Hero 3 - Two-State Compare.dc.html` |
| **FIFA Step Reveal** | ⚠️ available, other unit | `…/Website Redesign/Energy Changes in Systems (Physics).dc.html` (port/adapt) |
| **Structure Hotspot** | ❌ NOT delivered for Bonding | pattern exists in `…/Standard Circuit Diagram Symbols (Physics).dc.html` |
| **Zoom / Scale Explorer** | ❌ NOT delivered anywhere | — |
| Page-template skeleton (`Bonding Tokens + Page Template.dc.html`) | ❌ referenced by the heroes, **absent** | — |

**What the 3 delivered heroes can do (from reading their CONFIG + state machines):**
- **State Toggle Lab** — a +/− ion lattice; toggle solid / molten / in-solution / (force→)shattered; live conduction verdict + brittleness demo. Ships with two configs: **NaCl** (4 states + force) and **MgO** (2 states, 2+/2− charges → stronger attraction).
- **Dot-and-Cross Stepper** — ordered electron-move steps; `mode: transfer | share`; `layout: di | tri`. Ships **NaCl transfer** and **HCl share**. *Limitation:* geometry covers 2-atom (`di`) and metal-plus-two (`tri`) only — polyatomic molecules (H₂O, CH₄, NH₃) exceed the current model.
- **Two-State Compare** — an A/B flip with two built-in visual renderers: `metalLayers` (pure vs alloy) and `delocalised` (electron sea on/off). New renderers can be added without touching the state machine.

---

## 3. Token & font reconciliation — ⚠️ decision needed

The delivered `.dc.html` heroes were designed against the **pre-MRB-112** palette:
**Space Grotesk / IBM Plex Sans / IBM Plex Mono**, page `#E7E1D4`, panel `#FFFDF8`, accent `#C0392B`.

The **shipped, canonical** `shared/tokens.css` (MRB-112) — which every generated page already loads
first — is **Fraunces / Plus Jakarta Sans**, page `#F7F1E5`, card `#FFFFFF`, accent `#A63C12`.
The live Bonding pages are already on the Fraunces/Jakarta system.

**Recommendation (needs Mide's OK):** on port, retokenise every hero to `tokens.css` variables
(`var(--bg)`, `var(--card)`, `var(--accent)`, `var(--font-serif)`, `var(--font-sans)`, etc.) so heroes
and page chrome are one warm system. The hero `.dc.html` hardcoded colours/fonts are treated as
superseded. Without this, a hero would clash with its own page. *(The task brief line still says
"Space Grotesk / IBM Plex" — that line predates the shipped tokens; flagging the conflict rather than
silently picking.)*

---

## 4. Fixed furniture vs per-page slots

**Fixed furniture — identical on every Bonding page (already in the generator template):**
1. Topic header — back link, subject·topic kicker, H1, spec pill, tier badge
2. In-Depth Theory section (theory cards)
3. Key Note box
4. Matching activity
5. Test Yourself quiz (wired to existing quiz engine)
6. Star rating (existing mechanism)
7. Ask Mr Badmus AI panel (existing tutor integration)
8. Subtopic prev / all / next nav
- Common Mistake block is present on all 12 Bonding pages, so it is *effectively* fixed here — but it stays a genuine optional slot in the template (some units won't have one).

**Per-page slots — vary by the map below:**
- **Hero interactive** — 0, 1, or (potentially) 2 per page. Sits at the top of the content area, directly under the topic header, ahead of In-Depth Theory.
- **Higher-Tier box** — only pages 4, 10, 12.
- **Key Equations** — only page 9 (polymers).
- **FIFA block** — only page 12 (nanoparticles).

**Placement rule to confirm:** hero renders **between the topic header and In-Depth Theory** (interactive-first, then the prose backs it up). This matches the heroes' self-contained card design.

---

## 5. Per-page hero map (the deliberate part)

Legend — ✅ delivered as-is · ⚙️ delivered hero, new config · 🔧 delivered hero, **new visual renderer needed** · 🔁 port from another unit · ⛔ deliberately none.

| # | Page | Hero decision | One-line justification |
|---|------|---------------|------------------------|
| 1 | chemical-bonds | ⛔ **None** | Decision-rule page; the classification is already carried by the Matching widget + 10 MCQs. None of the 3 structural heroes is about *choosing* a bond type. *(Design map wanted Categorise Bins — undelivered; first home for it if built.)* |
| 2 | ionic-bonding | ✅ **Dot-and-Cross Stepper** — transfer, NaCl (option: +MgCl₂ `tri`) | The transfer mechanism *is* the page; the hero was literally extracted from this page. Perfect fit. |
| 3 | ionic-compounds | ✅ **State Toggle Lab** — NaCl, 4 states + force | Conduction-by-state and brittleness are the exam skill; hero extracted from this exact page. |
| 4 | covalent-bonding | ⚙️ **Dot-and-Cross Stepper** — share: H₂, Cl₂, HCl | Sharing mechanism; `share` mode delivered. **Diatomic only** — CH₄/NH₃/H₂O exceed current geometry (flagged as a future hero enhancement, not blocking). |
| 5 | metallic-bonding | ✅ **Two-State Compare** — `delocalised` (sea on/off) | The sea-of-electrons idea lands as a cause/effect flip; renderer delivered. Perfect fit. |
| 6 | states-of-matter | ⛔ **None** | Genuinely a *three*-state topic (+ state symbols). Two-State Compare only does 2 states; State Toggle Lab is ion-lattice-specific. Forcing either would misrepresent the science. *(Gap: Particle Motion Sim / heating-curve reader undelivered.)* |
| 7 | properties-ionic-compounds | ⚙️ **State Toggle Lab** — MgO config (2+/2− → stronger attraction) | Different teaching point from page 3: charge magnitude → bond strength → higher MP. MgO config is already in the delivered spec; not redundant with page 3's NaCl lab. |
| 8 | properties-small-molecules | ⛔ **None** | The learning is the *contrast* small-molecular vs giant. Two-State Compare could carry it but needs a molecule-drawing renderer (undelivered). Contrast is held by the Common Mistake block + matching + quiz. *(Gap flagged.)* |
| 9 | polymers | ⛔ **None** | Light page — mostly a labelled chain (static SVG). Design map itself said "keep it light." *(Gap: Structure Hotspot on the chain, undelivered.)* |
| 10 | giant-covalent-structures | 🔧 **Two-State Compare** — new `diamond ↔ graphite` renderer | Flagship structure→property page (just amended by MRB-118). Best treatment is the diamond(hard/insulator) vs graphite(soft/conductor) flip — but this needs a **new visual renderer** (Design-quality work) on top of the delivered hero. Graphene/fullerenes stay **static SVG** (Zoom/Scale Explorer undelivered). **Scope decision for Mide** — see §7. |
| 11 | metals-alloys | ✅ **Two-State Compare** — `metalLayers` (pure vs alloy) | Sliding-layers mechanism; renderer delivered and built for exactly this. Conduction angle (folded-in 5.2.2.8) already owned by page 5's delocalised compare, so one interactive here, not two. |
| 12 | nanoparticles | 🔁 **FIFA Step Reveal** (SA:V ratio) | **The only Bonding page carrying a FIFA worked-example set** (3 escalating examples in source). Gets FIFA Step Reveal to clear the systemic practice flag (content-standards §2). Port/adapt from the Energy Changes spec. *(Gap: Zoom/Scale Explorer for the "one-atom" scale wow — undelivered.)* |

**Distribution:** 8 pages carry a hero, 4 are deliberately none — a genuinely varied lineup, not a template stamped 12×. Of the 8: **5** use delivered heroes as-is or with an existing config (2, 3, 4, 5, 7, 11), **1** needs a new renderer on a delivered hero (10), **1** ports a hero from another unit (12).

---

## 6. FIFA worked-example note (systemic practice flag)

Only **`nanoparticles`** has a populated `fifas` list in the Bonding source (surface-area-to-volume
ratio, 3 worked examples, Triple only). Every other Bonding page is conceptual with an empty `fifas`
list — correct, per content-standards §2 (FIFA only where there's maths). So **FIFA Step Reveal is
mapped to page 12 only**, and it is the page that clears the practice flag for this unit.

---

## 7. Decisions for Mide before Phase B starts

1. **Retokenise heroes to shipped `tokens.css`?** (§3) — recommend **yes** (Fraunces/Jakarta/burnt-orange), treating the heroes' Space-Grotesk/IBM-Plex palette as superseded.
2. **Page 10 scope.** Build a **new diamond↔graphite renderer** for Two-State Compare (best pedagogy, extra Design-grade effort), or keep page 10 **static** for the pilot and defer the renderer? Recommend building it — it's the flagship page — but it is the one net-new visual in this port.
3. **Undelivered heroes — accept as gaps for the pilot?** Structure Hotspot, Zoom/Scale Explorer, Particle Motion Sim, and molecule/Categorise-Bins archetypes are not delivered. Pages 1, 6, 8, 9 ship **none** (clean static) rather than a wrong-fit interactive. Confirm that's acceptable, and that these archetypes get raised back to Design as a follow-up.
4. **Foundation layer.** Tokens are already wired site-wide, but there is **no `heroes/` module folder and no delivered page-template skeleton file** yet. Phase B 2a will build: (a) one vanilla JS module per delivered hero (`heroes/<archetype>.js`, init(container, config)), (b) the generator wiring to drop a hero into the per-page slot, (c) a scratch test page proving two configs per hero before integration.
5. **Hero placement** confirmed as top-of-content, above In-Depth Theory (§4)?

---

## 8. Content-freeze guarantee (Phase B)

Content is frozen. The port must not change any question, count, or tier flag. Verification plan:
- Snapshot the `quiz`, `matching`, `common_mistake`, `key_note`, `theory`, `fifas`, `higher`, `triple_only`
  fields for all 12 Bonding pages across all four data files **before** porting.
- After porting, re-parse and byte-compare those fields — any diff that isn't a deliberate,
  named edit fails the port. Quiz option order is seeded, so a re-run must produce zero content churn.
- Re-run the Phase-1 mechanical checks on the Bonding pages: zero critical/major defects expected.

---

## 9. Recon method (for the record)

Page list, tier flags and block matrix were parsed directly from the four `all_subtopics_chemistry*.py`
files via `CHEMISTRY_SUBTOPICS_ALL['bonding']` (scripts in the session scratchpad). Hero capabilities
were read from the three `Bonding Hero *.dc.html` specs. Fixed furniture was read from
`make_pathway_subtopic_page()` in the generator. Nothing was ported; nothing was committed.
