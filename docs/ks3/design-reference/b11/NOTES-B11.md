# B11 — Evolution, extinction and biodiversity · author's notes

**Complete unit: four of four lessons authored.** Draft — nothing here has been
science-reviewed. Flags are numbered so they can be answered by number.

**This unit completes KS3 Biology.** All eleven biology units now have every
lesson authored, and every statutory statement in the two genetics-and-evolution
strands and the three earlier biology strands is covered. See §5 for the
build-wide position.

---

## 0. What exists

| Lesson | Type | Status |
|---|---|---|
| `b11-01-variation-and-competitive-success` | SYSTEM | **authored** |
| `b11-02-natural-selection` | PROCESS | **authored** |
| `b11-03-when-the-environment-changes-extinction` | SYSTEM | **authored** |
| `b11-04-biodiversity-and-gene-banks` | SYSTEM | **authored** |

Statutory position: all three B11 statements covered. `INH.05` (variation
meaning some organisms compete more successfully, which can drive natural
selection) by b11-01 and b11-02 — the statement contains both halves and they
are given a lesson each. `INH.06` (environmental change leaving individuals and
species less able to compete, which may lead to extinction) by b11-03.
`INH.07` (maintaining biodiversity and the use of gene banks) by b11-04.

---

## 1. New instruments

### 1.1 `advantage-bench` — flagship of `b11-01`
The same five mice through five environments. Survival percentages are stored
per environment, so **the ranking reverses between benches** — the thick-coated
mouse is best in winter and worst in drought, the pale mouse best in snow and
worst against the owl. The disease bench is the one where **no visible variation
helps**, which sets up rung 4 on why unused variation matters and hands off
directly to b11-04.

### 1.2 `selection-runner` — flagship of `b11-02`
Deterministic allele-frequency model over generations, drawn as a stacked
twin-bar history. Three barks: clean (pale favoured), sooty (dark favoured) and
patchy (**the control — no difference in survival, so nothing moves**). Starts at
90% pale, which is the real historical starting point.

### 1.3 `pressure-bench` — flagship of `b11-03`
Four real species × five pressures = twenty outcome texts, each written
individually rather than generated. Every species is resilient to at least one
pressure and vulnerable to at least one, so no row reads as a simple ranking.
The panda's *no natural predators* result is deliberately included as the case
where a high score explains nothing.

### 1.4 `blight-bench` — flagship of `b11-04`
A thousand potato plants as one variety, four, ten, or a mixed landrace; release
a blight that a fixed fraction of varieties resists. **The clone field returns
exactly zero survivors**, and the yield-per-plant bar runs the other way to the
variation bar, so the trade-off that makes monoculture attractive is visible
rather than asserted.

---

## 2. Science flags — numbered for review

1. **Survival percentages on the b11-01 bench** are teaching values, and the
   legal line says so. Confirm an explicitly illustrative bench is acceptable
   here, as in B9 and B10.
2. **"Fittest" defined as best fitted plus reproductive success** (b11-01
   think-again), including the mayfly-versus-fifty-year comparison. Confirm.
3. **The Grants' finches** (b11-01 *Going further*): forty years on Daphne
   Major, the 1977 drought, measurable increase in beak depth in one generation,
   reversal after the 1983 rains. Confirm the dates and the framing as
   "evolution watched rather than reconstructed".
4. **Lamarck treated with respect** (b11-02 think-again) — a serious theory,
   right that species change, wrong on mechanism. **Confirm you want that
   framing** rather than the usual dismissal; I think the respect makes the
   correction land harder.
5. **The peppered moth**. **RESOLVED, 16 Aug**, and resolved differently from
   B9 flag 6. Ruling: the conclusion is sound, Kettlewell's method was fairly
   criticised, and Majerus's later work vindicated the result — so teach it
   plainly, with no hedge, and move the method criticism into *Going further*
   where it is the strongest *how do we know?* story in the whole biology build
   rather than a disclaimer. The caveat sentence has been cut from the legal
   line, which now covers only the bench model. **One thing to check:** the
   moth-method story has been added as a first paragraph in *Going further*
   ahead of the existing antibiotic-resistance paragraph, so that layer now runs
   to two paragraphs, which no other lesson in the build does. Say the word and
   I will move antibiotic resistance elsewhere or cut it.
6. **Antibiotic resistance** (b11-02 *Going further*), including "finish the
   course as prescribed". The finish-the-course advice has been questioned in
   the research literature in recent years. The lesson says "as prescribed",
   which is deliberately the wording that survives that argument. **Confirm.**
7. **"Over 99% of species that ever lived are extinct"** and five mass
   extinctions, end-Permian ~90% of marine species, end-Cretaceous 66 Mya
   (b11-03). Standard figures. Confirm.
8. **"Current extinction rates tens to hundreds of times the background rate"**
   (b11-03). Estimates vary widely and some published figures are much higher.
   The lesson deliberately uses a conservative range. Confirm.
9. **The four species on the b11-03 bench** and their trait descriptions —
   brown rat, hazel dormouse, giant panda, herring gull. All accurate as
   described. Confirm the dormouse detail (will not cross open ground, one
   litter, strict seasonal diet), which does most of the teaching work.
10. **Kakapo** (b11-03 *Going further*): flightless, freeze response, breeding
    tied to mast years, population low point of 51. Confirm the figure and that
    a named recovery programme is wanted.
11. **"Two thirds of modern medicines traceable to compounds from living
    organisms"** (b11-03 think-again). Widely quoted, and the exact fraction
    depends on how it is counted. **Flag: soften or attach a figure you are
    happy to defend.**
12. **Gros Michel and Cavendish bananas** (b11-04 hook), and the current Panama
    disease strain moving through Cavendish plantations. Confirm.
13. **The Irish potato famine** referenced in the clone verdict (b11-04).
    Mentioned in one clause as the historical case; the lesson does not attempt
    the political history, which is deliberate but is a choice. **Confirm** —
    a single clause may be too little or exactly right depending on what
    history teaches alongside this.
14. **Svalbard** (b11-04 *Going further*): ~1,300 km from the North Pole, over a
    million samples, minus eighteen degrees, permafrost backup, and the real
    Aleppo/ICARDA withdrawal and return. Confirm the figures; the vault's
    holdings grow, so a rounded "well over a million" is used rather than a
    number that dates.
15. **Landrace resistance at 62%** (b11-04 bench). Invented, chosen so the
    landrace clearly beats the ten-variety field without looking immune.
    Confirm the model is acceptable.
16. **No diagrams anywhere in B11.** A peppered moth pair on two barks is the
    obvious candidate and is not in the diagram manifest.

---

## 3. For Code

- Four instruments, all DOM-only. **No `Math.random()` anywhere in B11** — every
  bench is deterministic, which is deliberate for a unit about a process people
  wrongly imagine to be directed.
- Rail stops: four in all four lessons.
- Cross-links inside B11 chain forwards and all resolve. Outward links to
  b9-02, b9-03, b9-04, b10-01, b10-04, b10-05, b7-02 all exist.
  **Every forward link in the biology build now resolves**: B9's two pointers
  (to b10-01 and b11-03) and B10's three (to b11-01 and b11-02) all land.
- Tweak props: `showDraft` on all four. None has a second tweak; the natural
  ones are a starting environment on b11-01 and a starting bark on b11-02.

---

## 4. Misconception register — `EVOL` family, opened with eight entries

`EVOL-01` to `EVOL-08`, two per lesson, written into
`docs/ks3/misconception-register.md` with a new prefix row.

`EVOL-01` and `EVOL-06` both carry a second lesson in `reappears_in`
(`natural-selection` and `disturbing-a-food-web` respectively), which is the
cross-referencing the register exists for.

---

## 5. Build-wide position at the end of biology

Eleven units, sixty lesson slots, **all authored**. Misconception families
opened across the biology build: `CELL`, `DIET`, `BREATH`, `REPRO`,
`DRUG`, `PLANT`, `RESP`, `ECO`, `GENE`, `EVOL`.

Three things are outstanding across the whole of biology and are worth listing
in one place now that the discipline is complete:

1. **B5 is still two of eight.** Reproduction remains the only partial unit in
   biology, and NOTES-B5 §4 still asks for a ruling on the tone treatment before
   the remaining six are written. Everything since has been written to that
   treatment anyway, so the ruling is now retrospective as well as prospective.
2. **No diagrams anywhere in the biology build**, and the diagram manifest has
   no biology entries. Each unit's notes name its best candidate. The three I
   would commission first are a labelled food web (B9), a leaf cross-section
   (B7) and the chromosome-to-DNA nesting (B10).
3. **The `NOS` family ruling is still open**, and it now affects three units:
   `PART-12`/`PART-13` in C1, `GENE-06` in B10, and arguably
   `ECO-12`/`DRUG-06`. IDs are permanent, so this needs deciding before
   publish rather than after.
