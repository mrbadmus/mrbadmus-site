# DEPARTURES — P11 *Matter and the particle model*

Design's page is the default and it stays unless the change can be defended
to an examiner. ⊕ **Widened by Mide, 25 Aug 2026:** a deliberate, registered
improvement is allowed where the lane genuinely judges that its version
teaches better, so the old "name the defect in hers" column is a RATIONALE
column. What did not widen: her STRUCTURE is untouched, MRB-205 stands, and
the register is expected to be SHORT. A row that would not be defended to
Mide is not written.

**This one has NINE changed rows and SIX considered-not-changed rows.** Three
are her own instrument contradicting her own prose and the instrument
winning (5A.1); two are a state her code cannot describe truthfully; two are
length tells at her own threshold; one is a colour ruling; one is an ordering
forced by a shared component. Nothing in her structure moved, and every
figure that moved moved because her own bench prints a different one.

There is also **one finding at the end that is not a departure from anything
of hers**: the key stage's segmented control paints its pressed state amber,
Design's P11 component paints it blue, and the two cannot both be right for
long.

---

## Changed — 9 rows

### 1. The density bench gains a third branch, for water

| | |
|---|---|
| **Where** | `p11-01` `#s-bench` — the fourth readout ("Dropped in water it") and the closing note |
| **What she drew** | `const floats = T.d < 1.00;` — two branches, `floats` and everything else. |
| **What is built** | Three branches: `floats`, `sinks`, and `same`. Water reads *"stays put · exactly 1.00 g/cm³"*, and its note ends *"At exactly 1.00 g/cm³ this one does neither: a cubic centimetre of it weighs exactly as much as the cubic centimetre it would have to push out of the way, so it stays where you put it. This is the line the other five bars are read against."* |
| **Rationale** | **WATER IS ONE OF HER OWN SIX TABS.** Under `d < 1.00` it falls to the else branch, so the bench told a student that water dropped in water **sinks**, at *"over 1.00 g/cm³"*, when it is exactly 1.00 and does neither. That is 5A.1's equal-state rule and the alveoli defect exactly — a comparative that is true on the majority of the state space. It is also the most useful state on the bench: 1.00 is the line the other five materials are read against, and a student who has seen it is better placed on rung 4 (the steel ship's average density) than one who has not. `r_matter_bench` refuses a `density` payload with no tab at 1.00, so the branch cannot become unreachable later. |

### 2. `p11-02`'s legal line stops calling both speeds root-mean-square

| | |
|---|---|
| **Where** | `p11-02` legal line (`convention_note`) |
| **What she wrote** | *"Molecular speeds are root-mean-square figures for the gas or liquid named, scaled with the square root of absolute temperature from 500 m/s for air and 590 m/s for water at 20 °C…"* |
| **What is built** | *"Typical molecular speeds are quoted for the gas or liquid named, scaled with the square root of absolute temperature from about 500 m/s for air and about 590 m/s for water at 20 °C…"* Both figures are unchanged and the scaling is unchanged. |
| **Rationale** | **The claim is true of one of the two figures and not the other.** 500 m/s is the root-mean-square speed of an air molecule at 20 °C; 590 m/s is the MEAN speed of a water molecule, whose rms is about 640. Ruled before the build: the speeds stand and the prose changes. Nothing a student reads on the page depends on which average it is — the bench prints "roughly", and the point is the ORDER of the number — so *typical* is both true and enough at KS3, where neither average has been defined. |

### 3. "Faster than a rifle bullet" becomes "faster than a bullet from a handgun"

| | |
|---|---|
| **Where** | `p11-02` `#s-bench` closing note, first sentence |
| **What she wrote** | *"…are moving at roughly {vmol} m/s — faster than a rifle bullet, in every direction at once."* |
| **What is built** | *"…faster than a bullet from a handgun, in every direction at once."* |
| **Rationale** | **The comparison is false at every state her own bench can reach.** The readout runs from 483 m/s (air at 0 °C) to 647 m/s (water at 80 °C); a rifle bullet leaves the muzzle at 800–1000 m/s. A handgun bullet is 340–400 m/s, so the sentence is true across the whole slider — including the cold end, which is where a false version would be most obviously wrong. 5A.1: the instrument is the measurement and the prose is what changes. Same image, same job, and the figure beside it is one a student can check. |

### 4. `p11-03`'s note stops sending the student to a slider position that does not exist

| | |
|---|---|
| **Where** | `p11-03` `#s-bench` closing note, last sentence; and the legal line |
| **What she wrote** | *"Drop the temperature to 0 °C and every bar collapses, because you have taken the energy out — but the number of particles has not changed at all."* Her legal line adds *"…and no energy is shown for 0 °C because the reference point is 0 °C itself."* |
| **What is built** | *"Take the temperature down and every bar shrinks, because you are taking the energy out — but the number of particles has not changed at all."* The legal line now reads *"…and 0 °C is the reference the energies are measured above rather than a reading the bench takes."* |
| **Rationale** | **Her `SLIDER` is `[10, 20, 40, 60, 80, 100]` — there is no 0 on it.** The sentence is an instruction to move a control to a place it does not go, and a student tries it. Her `pct` also carries an `e <= 0 ? 1.5` branch that nothing can select for the same reason; it is not ported, and `r_matter_bench` refuses a zero or negative slider position on this model so the branch cannot come back. The re-authored sentence says the same physics and is true at every step she drew: the bars do shrink, all the way down. Registered rather than "fixed" by adding a 0 to her slider, because adding a position is changing her drawing and dropping a dead branch is not. |

### 5. "About a ninth above the surface" becomes a derived 8%

| | |
|---|---|
| **Where** | `p11-04` `#s-bench` closing note, `odd` branch |
| **What she wrote** | *"…so it floats — with about a ninth of it above the surface and the rest below."* |
| **What is built** | *"…so it floats — with about 8% of it above the surface and the rest below."* The 8 is computed as `1 − solid ÷ liquid` from the two densities in the payload. ⊕ Integration note: the legal line gains the clause *"and the fraction of a floating lump above the surface"* to its list of what is calculated from the quoted densities, so the derived figure is disclosed where the other derived figures are. |
| **Rationale** | **A ninth is 11%, and it is the SEAWATER figure** (ice 0.917 against seawater 1.025). This page is about fresh water at 1.00, where the fraction above is 8% — which is what her own rung 1 marks correct (*"About 8%"*) and what her own Think-again says (*"about 92% of itself below the surface"*). Two sentences on the page against one, and the two are the ones a student is marked on. Deriving it rather than retyping it means the note cannot drift from the bars above it. |

### 6. The bar in focus takes `--ks3-data` **and** a structural ring

| | |
|---|---|
| **Where** | All four benches. `p11-01`, `p11-03` and `p11-04` mark the selected material / amount / state; `p11-02` marks the one visible quantity. |
| **What she drew** | `tone: 'var(--ks3-alert)'` on the bar in focus, `var(--ks3-blue-light)` on the rest. |
| **What is built** | The focus bar's fill is `var(--ks3-data)`; its track border goes from 2px `--ks3-on-dark-muted` to **3px `--ks3-on-dark`**, and its label from 600 to 800. Everything else is unchanged. |
| **Rationale** | **MRB-252 reserves amber for warning and confrontation and sends category and selection to `--ks3-data`** — and this is a selection on three benches and a category on the fourth. ⚠️ The token substitution ON ITS OWN would have made it worse, not better: `--ks3-data` and `--ks3-blue-light` are the same value today (`#8FB7FF`, minted that way deliberately so the roles can separate later), so swapping the token would leave six identical bars and make the panel's own aria-label — *"…with gold highlighted"* — false. That is the `p9-03` test-point argument, and here it has an answer: take the correct token, so the role is named and the two colours can move apart, and carry the distinction on something that is not a hue. 5A.4 rules exactly that where no legal category hue is available, and each bar's own sub-line says in words what it is. Measured in the browser: focus track 3px, every other track 2px, on all four benches. |

### 7. Her unit-pairing line moves down one block inside the triangle

| | |
|---|---|
| **Where** | `p11-01` `#s-formula`, the panel beside the triangle |
| **What she drew** | result (40px display) → *"g with cm³ gives g/cm³ · kg with m³ gives kg/m³"* (26px display) → *"Two things side by side means multiply…"* (18px) → the three unit rows. |
| **What is built** | result → rule → unit legend → *"g with cm³ gives g/cm³ · kg with m³ gives kg/m³"* in the `condition` slot (21px display). Every word is hers. |
| **Rationale** | The shared `r_cover_triangle` emits its closing stack in a FIXED order — rule, units, condition — and `build_ks3.py` is not a file a content lane may edit. The `condition` slot is the right one on its own terms: the CSS comment beside it says it is for *"the statement that makes every question on the page solvable"*, which is precisely what a matched unit pair is on this page, and it is display type as hers is. Ordering only; nothing is lost and nothing is added. |

### 8. One distractor is finished on each of the eight marked rungs' worst cases

| | |
|---|---|
| **Where** | `p11-01` rung 2 · `p11-02` rungs 1 and 2 · `p11-03` rungs 1 and 2 · `p11-04` rungs 1 and 2 — seven of the eight marked rungs in the unit |
| **What she wrote** | Correct answers of 31, 24, 31, 22, 25, 17 and 31 words against longest distractors of 15, 12, 11, 15, 13, 10 and 14. |
| **What is built** | In every case ONE distractor is finished so that it states its wrong rule completely, and the longest distractor comes within her own threshold. **Every correct answer is untouched to the character, and every correction is untouched.** Example, `p11-01` rung 2 option C: *"…because density does not depend on how much you have"* becomes *"…so it comes out at the same number for oak and for gold alike."* |
| **Rationale** | **`verify_ks3`'s own threshold: the correct option is strictly the longest and clears the longest distractor by ≥4 words or by ≥1.4×.** Seven of eight rungs cleared it, so a student could score most of the unit by choosing the longest option without reading it. The remedy is always at the distractor — never shorten a correct answer, never move an index for this, never edit a correction — and in every case the added clause is the sentence her own correction was already written against. |

⚠️ **THE SAME THRESHOLD WAS APPLIED TO THE QUESTION BANK, WHICH IS THIS
LANE'S OWN WRITING AND NOT A DEPARTURE FROM ANYTHING OF HERS.** Twelve of
the forty-eight authored questions came out as tells on the first
measurement, and all twelve were remedied at the distractor before the
gates ran: `p11-01-e04` · `p11-02-s01/s02/s04` · `p11-03-e03/h02/h03/h04` ·
`p11-04-e02/e04/s03/h04`. Measured after: none. `verify_ks3`'s MRB-177 gate
reads the LADDER and the activities and does not walk the bank, so this one
is measured by hand — which is why it is written down.

⚠️ **MRB-278 · THE ORDER OF EVERY MARKED RUNG'S OPTIONS MOVES, AND IT IS NOT
A ROW HERE.** All eight marked rungs in P11 put the correct answer at index 0.
Measured across the eight sets before: `[8, 0, 0, 0]`. After: `[2, 2, 2, 2]`,
every index used and none over half. **Every option's text and every
correction is verbatim; only the ORDER changes, and the `answer` index
follows the correct option.** Engine policy, recorded in each lesson's
docstring, and explicitly not the length-tell remedy — which never moves an
index.

### 9. `p11-01`'s "Before this lesson" edge is not authored

| | |
|---|---|
| **Where** | `p11-01` endmatter |
| **What she drew** | A link back to `p10-05-how-a-motor-works`. |
| **What is built** | `requires: []`, which renders the engine's own *"Nothing — this is where the unit starts."* |
| **Rationale** | The edge crosses into P10, which is a different lane and is not in this worktree, and `validate()` fails a `requires` naming a lesson the registry cannot resolve (`UNKNOWN PREREQUISITE`). The rendered sentence is true as it stands — P11 is where the unit starts — and restoring her edge is one line when the lanes merge. Flagged for the commander rather than worked around. |

⊕ **Ruled at integration, 25 Aug 2026: the edge stays empty.** P10 is authored now and the link would resolve, but P11's typical year is 7 and `p10-05` sits in year 9, so a `requires` edge would be a forward reference — a lesson pointing at one a student meets two years later. Her "before this lesson" link is the folder's prev-link, which the engine already emits from the unit order (5A.5) on the index and the page nav; it is not a prerequisite claim. No row needed beyond this one.

---

## Considered, not changed — 6 rows

| # | What was considered | Why it stands |
|---|---|---|
| 1 | **`p11-02`'s "Strikes each second: billions".** The real collision rate on a micron speck in air is of order 10^16 per second (`¼ n v A` with `n ≈ 2.5 × 10^25` per cubic metre, `v ≈ 470 m/s` and `A ≈ 3 × 10^-12 m²`), so "billions" understates it by about seven orders of magnitude. | It is a FLOOR, not a measurement, and it is the only readout on the bench that is not computed. Her explainer says "enormous numbers" and rung 2's own correction quotes 10^25 per cubic metre, so the page does not leave a student believing the count is small. Raising it to a power of ten in a readout card would be the only power of ten in the unit outside a distractor, and at KS3 "billions" is the word that lands. |
| 2 | **The pressed tab is amber.** Design's `seg(on, dark)` in this delivery paints a pressed segmented button `var(--ks3-blue-light)`; the shipped `.ks3-dark .ks3-seg-btn[aria-pressed="true"]` paints it `var(--ks3-alert)`. | Drift 4 ruled ONE segmented control for the system, and MRB-242 put the dark branch's amber back deliberately as *"Design's own pair"* from B1. A P11-scoped override would restyle four pages out of 199 and leave a student meeting two different segmented controls between P9 and P11 — which is the drift that ruling exists to stop. It stands, and it is raised as a finding below rather than fixed in one lane. |
| 3 | **`p11-04`'s comparison bar is nearly the colour of its own track border.** `--ks3-on-dark-muted` fill inside an `--ks3-on-dark-muted` bordered track. | Measured from the rendered pixels rather than judged from a thumbnail: the fill is `#C6B9A7` and the unfilled remainder `#4B453E`, which is about 4.9:1 — legible, and deliberately recessive because the bar is the line the other two are read against rather than one of them. Hers, and right. |
| 4 | **`p11-01`'s bench `lead` names its own controls** (*"Pick a material, choose how big a block…"*). | 5A.1's no-bench-intro-narration rule is about a paragraph of PROSE above the instrument. This is the instrument's own lead inside Design's `Bench` component, it is one sentence, and its second half is teaching (*"…the bars are the density league table — and they do not move when you change the volume"*), which is the claim the whole bench exists to demonstrate. The same shape shipped on all three P9 benches. |
| 5 | **`p11-03`'s fourth readout is labelled "A bathful holds", which hard-codes one tab's name.** | A readout's LABEL is static in the shipped bytes — only `value` and `sub` are templates — and this is her wording. The drawer refuses a payload with two tabs tied at the largest mass, so the sentence cannot come to name the wrong one; the comparison itself (`{ratio} × more` / `this one`) is derived. Changing the label to a token would have meant widening the shared tile shape for one page. |
| 6 | **Her `odd: true` flag on `p11-04`'s water tab.** | Read by nothing in her own `benchVals()` — the branch is computed from the two densities. Not ported: an authored key with no read site is what `ks3_key_audit` exists to catch, and deriving the verdict is what makes it true for a substance nobody has classified by hand. |

---

## Notes vs drawing — 3 contradictions

| # | What her note says | What her page measures | What is built |
|---|---|---|---|
| 1 | `NOTES-P11-P12.md` §6: *"p11-02 quotes root-mean-square molecular speeds. Confirm 500 m/s for air and 590 m/s for water at 20 °C are the figures you want."* | The figures are right; the LABEL is right for one of them. 590 m/s is the mean speed of a water molecule, not its rms (≈640). | The figures are built exactly as drawn. The legal line's wording changes — changed row 2. |
| 2 | `p11-03`'s legal line: *"no energy is shown for 0 °C because the reference point is 0 °C itself"*, and its note tells the student to *"drop the temperature to 0 °C"*. | `SLIDER = [10, 20, 40, 60, 80, 100]`. There is no 0 on the control, and the `e <= 0` branch in her `pct` is unreachable. | The DRAWING is built — six positions, no dead branch — and both sentences are re-authored to describe the control she drew. Changed row 4. |
| 3 | `p11-04`'s note: *"about a ninth of it above the surface"*. | Her own rung 1 marks *"About 8%"* correct and her own Think-again says *"about 92% of itself below the surface"*. | The page's own two other sentences win, and the figure is derived from the payload. Changed row 5. |

---

## Engine policy — recorded here, not registered as departures

- **Rung order (MRB-278).** See the note after changed row 8. `[8,0,0,0]` → `[2,2,2,2]`.
- **Question-bank order.** Forty-eight questions, twelve per index, authored across all four positions from the start.
- **Draft chrome dropped.** Every delivered page carries `showDraft` and a `ks3-review-flag`; none of it is ported, and `verify_ks3` asserts its absence. Swept by concept — *draft*, *review*, *not yet checked*, *provisional* — not by string.
- **Her aria descriptions.** The bar panel is `role="img"` with a live `aria-label` composed from the values, which is hers. It ships with the panel's CAPTION as its resting name rather than an empty string, so a reader with JavaScript off gets a name rather than "image". There is no `<desc>` convention to follow in this unit because there is no SVG in it: Design's §3 records that no P11/P12 bench puts a live label inside one.
- **No Childline block.** She places one on `p10-01` and on no other page in P10–P12. Nothing in P11 asks a student to disclose a risk in their own home.
- **No keyword block.** Her physics deliveries supply none, so `vocabulary` is authored from the terms HER PAGE DEFINES — 4 per lesson, 16 in all — and no `keyword` block is placed.

---

## Findings — not departures from anything of Design's

### The key stage's pressed tab and Design's pressed tab have come apart

`shared/ks3.css` paints `.ks3-dark .ks3-seg-btn[aria-pressed="true"]` in
`var(--ks3-alert)`, adopted under MRB-242 as *"Design's own pair"* from B1.
Design's `Bench.dc.html` for P11 and P12 paints the same control
`var(--ks3-blue-light)` with an ink label. Both are her drawings, eight
months apart.

It matters for two reasons rather than one. It is a **selection** use of
amber, which MRB-252 rules against in terms; and it is now the treatment on
**ten more pages** as P11 and P12 land, so the amber reading of "careful,
this is a wrong idea" is being spent on "this is the tab you pressed" on a
growing share of the key stage.

It is NOT fixed in this lane: `.ks3-seg-btn` is one control for the whole
system by an explicit ruling, the change would move every KS3 page's bytes,
and a per-unit override is exactly the drift that ruling forbids. Raised for
an engine pass on `main`, with P10 and P12 arriving at the same fork.

### `verify_ks3.py`'s P11 pending-reference gate has outlived its premise

⚠️ **THIS UNIT TURNS TWO GATES RED, AND IT DOES IT BY BEING CORRECT.**

`verify_ks3.py` lines 542–548, under the heading *"P11 cross-reference
renders before P11 exists"*:

    p = "ks3/chemistry/particles-and-their-behaviour/testing-the-model.html"
    check("P11 reference renders a graceful pending state",
          "ks3-pending" in html and "coming soon" in html.lower())
    check("P11 pending reference is not a link",
          "why-ice-floats.html" not in html)

Measured, before and after, on the same page:

| | `ks3-pending` | "coming soon" | link to `why-ice-floats.html` |
|---|---|---|---|
| at `HEAD` (P11 unauthored) | present | present | absent |
| with P11 authored | gone | gone | `/ks3/physics/matter-and-the-particle-model/why-ice-floats.html` |

That is the behaviour §4.6 asks for. A cross-discipline `references` edge
renders as a graceful pending card *until the referenced unit exists* and
resolves to a real link once it does; C1's own record carries the note
*"P11 owns it (§7.4); this lesson points at it and must render gracefully
before P11 exists."* The gate hard-asserts the pending half and the ABSENCE
of the link, so it now asserts the absence of the thing MRB-223 was opened
to build. It can only go green again if P11 does not exist.

**Not fixed in this lane.** `verify_ks3.py` is on the do-not-edit list for a
content lane, and this is a one-line engine change on `main`: the two checks
should either be inverted (the reference now RESOLVES, and the pending
state belongs to a unit still unbuilt) or retired with the slice they were
written for. Every other gate in the run is green — 137 pass, these 2 fail,
and no P11 page, component, figure, contrast, rail or content check is
among them.

---

## ⊖ Commander's Phase 3 — 25 Aug 2026

The built pages were compared against her JavaScript constants and her HTML
prose, string by string, by the commander's own comparator after the
executor's pass. Every residue it returned is a row above (rows 2–5, 8), the
engine's ladder chrome, or her `aria-label` composition. **Zero reverts.**
