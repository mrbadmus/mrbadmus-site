# DEPARTURES-P1 — where the built page differs from Design's drawing

**MRB-223 · ruled by Mide, 24 Aug 2026.** Design's page is the DEFAULT and it
stays unless the departure can name what is *wrong* with it. Not "mine is
clearer", not "my analogy is better" — a defect. Where there was doubt, her
version stands and the doubt is recorded below as **considered, not changed**
so it can be seen rather than guessed at.

Mide may overrule any row.

**This register is deliberately short.** A long one would mean the port had
drifted into rewriting to taste, which is the failure mode the ruling warns
against.

---

## Rows — changed

### 1 · `p1-01` — "two of them are not stores at all" → "three of them"

| | |
|---|---|
| **Lesson** | `p1-01 energy-stores`, the store/pathway sort prompt |
| **She wrote** | "Every word of that is in common use and **two** of them are not stores at all. Sort each one before you read on." |
| **We wrote** | "Every word of that is in common use and **three** of them are not stores at all. Sort each one before you read on." |
| **The defect** | **Her page contradicts itself.** The sort on that same page carries six cards, and three of them are marked `store: false` in her own data — `Light`, `Sound` and `Electrical`. Her sentence says two. A student who counts the cards finds three and a student who reads the sentence expects two, and the sentence concedes store status to one of the three — most likely `Electrical`, which is the one her own lesson calls the one almost everyone gets wrong. |
| **Measured** | Her `SORT` array: `Kinetic store:true · Light store:false · Chemical store:true · Sound store:false · Elastic store:true · Electrical store:false`. Three false. |
| **Raised by** | content-phys (run 2), against its own work. Re-measured independently here before being kept. |

### 2 · CLASS ROW — the apply rung's correct answer is written fuller than its distractors

| | |
|---|---|
| **Lesson** | `p1-01`, `p1-02`, `p1-03` (and watched on `p1-04`, `p1-05`, `p1-08`) |
| **She wrote** | Marked-rung option sets in which the correct answer is the longest option by a wide margin — `p1-01 apply` 12w against 8w; `p1-03 apply` 15w against 9w. |
| **We wrote** | The same rungs with their **distractors written out to length**. No correct answer was shortened, no claim was altered, and every one of her feedback strings still answers its re-worded distractor. |
| **The defect** | **The rung can be answered without reading it.** Pick the longest option and score. `verify_ks3`'s MRB-177 gate measures exactly this — strictly longest AND clear of the next longest by ≥4 words or ≥1.4× — and `p1-01 apply` fails it outright (gap 6→ratio 1.50) as does `p1-03 apply` (gap 6, ratio 1.67). |
| **Why one row and not six** | It is a systematic habit in her authoring rather than six accidents: five of the six affected rungs in the unit are the `apply` rung. A reviewer should read this as one authoring pattern, not as six separate science disagreements — because **no claim changed anywhere in it**, only the length of wrong answers. |
| **Ruling followed** | MRB-177 fixes AT THE DISTRACTOR, never by trimming the correct answer. Precedent: `c10 lesson_01`, where Design's predict ran 11/15/7/7 and was re-authored to 15/15/16/16. |

### 3 · `p1-03` — "Four stores. One total that never moves." → "Three stores."

| | |
|---|---|
| **Lesson** | `p1-03 conservation-of-energy`, the running-total bench heading |
| **She wrote** | "**Four** stores. One total that never moves." |
| **We wrote** | "**Three** stores. One total that never moves." |
| **The defect** | **Her bench draws three stores, and the heading sits directly above it.** Measured off her own canvas code: `seg(grav, '#8E6C3F', 'GRAV')`, `seg(kin, '#D98A4A', 'KIN')`, `seg(th, '#E4572E', 'THERMAL')` — three segments, no fourth. Her readout row is Gravitational, Kinetic, "Thermal, surroundings" and **Total**, which is three stores and a sum, not four stores. A student counts the bars, gets three, and reads four immediately above them. |
| **Note** | `NOTES-P1.md` §3 repeats the same "four stores" in its instrument table, so the note and the heading agree with each other and both disagree with the drawing. Per the brief, the drawing was measured and the note was not followed. |
| **Same class as row 1** | This is the second place in P1 where a count word in Design's prose disagrees with the instrument beside it. Both were found by counting her data rather than reading her sentence, and `ks3_art/p1.py` already carries a `_count_word_agrees()` helper written for exactly this — it is now called by the running-total renderer so the engine catches the third one. |

---

## Rows — considered, not changed

These were weighed and **her version stands**. They are recorded because the
ruling asks for the doubt to be visible, not because anything was altered.

### A · `p1-06` — matt white against matt black for infrared

An earlier run authored a Leslie's-cube bench and ruled that for infrared it is
SHINE that decides emissivity, colour being a small effect, so matt white comes
within 8% of matt black. That is defensible physics — matt white paint really is
around 0.9 emissivity.

**Not applied, and the reason is stronger than a disagreement about ordering:
her page has no Leslie's cube and no emissivity bench at all.** Her `p1-06`
instruments are a three-routes bench (`SCENARIOS`) and a six-card harmless/risky
word sort (`WORD_CARDS`). Her only emissivity content on the whole page is one
key-fact line — *"more from matt black ones than from shiny silver ones"* —
which contrasts matt black with **shiny silver** and never raises matt white.
There is no defect in a sentence that does not make the claim being corrected,
and no page for the correction to live on.

### B · `p1-05` — the conduction times are illustrative, not measured

Her science flag 15 says so herself: Cu 9 s, Fe 22 s, glass 150 s, wood never —
"ratios are right; absolute values need review before any claim of realism". She
has already labelled the limitation, and a page that states what its numbers are
worth is not making a false claim. Left as drawn, and flagged to Mide as a
science-review item rather than a defect.

### C · `p1-02` — "wasted" framed as a judgement about intent

Her science flag 6 raises this against herself: *"'wasted' is framed as a
judgement about intent, not about physics — flagging because it is a wording
choice a reviewer may want tightened."* It is not wrong: her own closing panel
says a physicist saying "wasted" always means "ended up somewhere too spread out
to be useful", never "ceased to exist". That is the correct distinction and it
is stated explicitly. Left as drawn; it is Mide's to tighten if he wants it
tighter.

### D · `p1-03` — the hide-the-thermal-store control makes the law look false

Her flag 7 asks that it not be removed as a "confusing" control. Agreed and
kept: it is the confrontation of `ENER-12`, and a bench that only ever shows
conservation working cannot confront the belief that energy goes missing.
Recorded here so that a future reviewer meeting a control that appears to teach
the wrong thing finds the reason before deleting it.

---

## Not departures — engine policy, recorded so they are not mistaken for one

These changed student-visible output and take **no** register row, because they
are engine rules that apply to every KS3 page rather than judgements about
Design's science.

| What | Rule |
|---|---|
| The draft flag is removed | Her `showDraft` prop defaults TRUE and draws "Draft — not yet science-reviewed." on all 70 physics pages. MRB-221 revoked the review marker; MRB-223 requires no draft marking anywhere a student can see. |
| Marked-rung option ORDER is varied | MRB-278. She puts the correct answer first in both marked rungs of every lesson; P1's sixteen rungs are spread 4/4/4/4 across the four indices. **Her option text and every correction are verbatim** — only the button order moves. |
| `ENERGY-nn` ids become `ENER-nn` | Her `NOTES-P1.md` §1 names `ENERGY-01`..`ENERGY-14` and says they were added to the register on 15 Aug 2026. No `ENERGY-` id has ever existed, and the register's prefix table carries a dated ruling: *"A physics lane meeting an energy misconception adds to `ENER`; it does not open `ENERGY`."* The reservation was discharged when C7 opened `ENER` on 21 Aug. Affects no student-visible text. |
| Bars are DOM, not canvas | Her benches draw on `<canvas>`. Seventeen built KS3 pages carry one and every other unit's bar instrument is spans, so bars are spans here — the numbers become real text a screen reader reaches and a phone can scale. Shape, ordering and every string are hers. |

---

## Notes-versus-drawing contradictions found

Reported, not escalated, per the brief. In each case **the drawing was
measured** and the note was not followed.

1. **`NOTES-P1.md` §1 announces fourteen misconception ids; §2 names eleven.**
   Her coverage table lists eleven distinct beliefs across the eight lessons.
   P1 mints eleven — `ENER-09` through `ENER-19` — one per belief her table
   actually confronts, not fourteen.
2. **`NOTES-P1.md` §1 says the ids were added to the register on 15 Aug 2026.**
   They were not; no `ENERGY-` id has ever appeared there. Measured by grep over
   `docs/ks3/misconception-register.md`.
3. **§3 describes `p1-03`'s running total as showing "four stores".** Her bench
   draws three (`Gravitational`, `Kinetic`, `Thermal`) plus a `Total` readout.
   Built to the drawing: three stores and a total.
4. **The audit's rail-stop prose and her `RAIL` consts disagree on which
   sections are stops.** Her `PHYSICS-AUDIT` §3 says the misconception block
   loses its stop "where the lesson has a fuller third section"; on `p1-01`
   `#s-think` IS a stop and on `p1-02`–`p1-08` it is not, with `p1-07` and
   `p1-08` dropping a second one. Every rail was counted off her `RAIL` const
   directly, all eight, and the manifest matches those and not the prose.
