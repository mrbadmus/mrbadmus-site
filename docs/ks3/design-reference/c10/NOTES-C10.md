# C10 — The Earth and its atmosphere · author's notes

**This file covers `c10-04` only.** The other six C10 lessons were packaged
without notes before this one was written, and their instrument payloads and
science flags cannot be reconstructed reliably after the fact. That gap is
recorded in `README.txt` and is unchanged by this pass.

---

## c10-04 · A planet with limits — SYSTEM · `KS3.C.EA.04`

Authored 21 Aug 2026 into the slot `structure.py` had reserved. Covers the
Earth as a source of limited resources **and** the efficacy of recycling — the
spec statement has two halves and the lesson has one instrument for each.

### The ruling that shaped it

Two designs were open: a finite-stock depletion clock, or a materials-flow loop
with recycling rates as the dials. **Chose the loop**, because the depletion
clock teaches the wrong lesson — it makes "years left" the interesting number,
and years-left is the one figure in this topic that is genuinely soft (a reserve
is an economic category, so the number moves without the planet changing). The
loop instead makes the *material* the variable, which is where the real physics
is: what comes back depends on whether melting destroys the structure, not on
how carefully anyone sorts a bin.

### The bench — `oxide-bench`'s sibling, same discipline

`s-loop`, on the dark panel. 1000 kg enters; the student sets **material** (5)
and **collection rate** (4). **20 reachable states, all enumerated**, no
unreachable combination — every material is legal at every rate, including 0%.

Readouts, all derived at render from the two settings:

- six mass bars, one per pass, `1000 × (collection × yield)ⁿ⁻¹`;
- **lifetimes per kg of ore**, the sum of every pass — `1/(1 − collection × yield)`;
- energy new-from-ore against energy-from-recycled, with the saving.

The verdict sentence has **six branches** and is computed from the two readings,
never stored per state: nothing-collected; yield-floor (the packet); multiplier
≥ 5; multiplier ≥ 1.7; low-yield-despite-collection; and
good-material-poor-collection. Each branch says something the others cannot.

Bar track is `rgba(0,0,0,.25)` with an inset `rgba(255,255,255,.16)` hairline —
the same fix applied to the b7/b8 oxygen readouts on 21 Aug, so the fill clears
3:1 against its track and the empty part of the bar stays visible.

### The numbers, and why these five materials

Yield = the fraction of *collected* material that comes back usable at the same
grade. Energy figures are order-of-magnitude teaching values in MJ/kg.

| Material | Yield | New | Recycled | Saving | At 9-in-10 |
|---|---|---|---|---|---|
| Aluminium can | 0.95 | 45 | 2.3 | 95% | **6.90×** |
| Steel can | 0.92 | 25 | 7.5 | 70% | 5.81× |
| Glass bottle | 0.90 | 15 | 11 | 27% | 5.26× |
| PET bottle | 0.50 | 85 | 17 | 80% | 1.82× |
| Crisp packet | 0.02 | 90 | 90 | 0% | **1.02×** |

The set is chosen so that **the two discriminating cases sit on the bench, not
in a footnote**:

1. **Aluminium** is the famous case and it is genuinely true — a 20th of the
   energy, and the metal does not degrade. It anchors the top of the range.
2. **Glass** is the case that contradicts the intuition the aluminium case
   builds: endlessly remeltable, and only a **27%** energy saving, because the
   melting *is* the energy. A student who has learned "recycling saves ~95%"
   from cans needs this one immediately.
3. **PET** degrades — half of what comes back cannot be a bottle again. This is
   what `downcycling` is for as a vocabulary card.
4. **The crisp packet** is the case where collection is irrelevant: nine in ten
   collected, 1.02× multiplier. It is the honest answer to "if we recycled
   everything" and it is a real object a KS3 student has in their bag.

**Rejected: a smartphone as the fifth material.** Per-kilogram energy figures
are not meaningful for a device, so its row would have been the only
non-comparable one on the bench. It moved to ladder rung 4, where "predict how
this recycles" is the actual question and no shared axis is needed.

### The second instrument

`s-stock`, five extracted things — bauxite, iron ore, crude oil, phosphate rock,
helium — each with **what it is for, the limit, and whether recycling helps**.
The point of the set is that **no two run out the same way**: bauxite's limit is
energy not rock; oil's carbon leaves the loop the moment it is burnt; phosphate
has no substitute at all and is the sharpest of the five; helium physically
leaves the planet. Rail ticks at three of five opened.

### True, not famous

- **Recycling does not make a finite stock infinite.** The loop leaks every
  pass. The key fact and the misconception both say so, and the bench proves it
  before either is read.
- **Reduce and reuse before recycle, in that order**, because they cut
  extraction and recycling only slows it.
- **A reserve is an economic category.** "Years left" moves when the price or
  the technology moves, which is why the going-further section leads with it.
  The real limit shows up as rising energy cost long before anything runs out.
- **The crisp packet is a trade-off, not a mistake** — the laminate keeps food
  fresh on very little material. Stated in going-further so the lesson does not
  end on "packaging is bad".

### Structure

Rail: HOOK · LOOP · STOCK · WORDS · THINK · LADDER (6 nodes).

- **Hook** — three quarters of all aluminium ever smelted is still in use. The
  reveal is the discriminating bit: almost perfect recyclability *and* mining
  still rising, because the stock in use is still growing.
- **KEY FACT** — one box: fixed stock, one-way extraction, several lifetimes per
  kilogram, every loop leaks.
- **Vocabulary (Law 7)** — finite resource · ore · recycling · downcycling ·
  reserve. Notes carry the trap, not extra content: finite ≠ nearly gone; ore is
  not the metal; a bottle that becomes fleece is not a bottle.
- **Misconception** — "if we recycled everything we would never run out". The
  reveal panel carries `id="think-reveal-recycling"` so a `confronted_by` join
  names the panel and not the surrounding section (the MRB-277 2d pattern).
- **Ladder** — 4 rungs, marked at A and A, self-marked at 3 and 4. Rung 2 is
  the discriminator: collection held equal at nine in ten for both the can and
  the packet, so the only available answer is the material.

### Tweaks

`startMaterial` (which material the bench opens on) and `barCycles` (3–8 passes
shown), plus the standard `showDraft`. Both are code-only changes — copy and
single colours are editable in place and deliberately not duplicated as props.

### Flags for science review

- Yields are teaching values chosen to be defensible and to order correctly, not
  audited industry figures. **The ordering is the claim**, not the second
  decimal place.
- Glass at 27% is the figure most likely to be challenged. It is deliberate and
  it is the point of including glass; if review wants a range rather than a
  single number, the row is one edit.
- "About three quarters of all aluminium ever smelted is still in use" is a
  widely published industry figure and is stated as approximate in the hook.

### One token note for the next author

The bench's two mono control-group labels are `--ks3-on-dark-muted`, the same
token as the stat labels in the panel below them. **There is no on-dark accent
token in the KS3 family** — "ember" is `--st-ember`, which belongs to the studio
surface. Reaching for `--ks3-ember` fails silently: the declaration is dropped,
the label inherits `--ks3-on-dark`, contrast stays fine and no gate trips. It
was written that way in the first draft and caught on review.
