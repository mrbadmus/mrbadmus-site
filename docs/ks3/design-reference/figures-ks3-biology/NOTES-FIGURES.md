# NOTES-FIGURES — WS1 diagram gaps, twelve figures

19 August 2026. Twelve standalone files plus `00-index.dc.html`, in this folder.
Read-only run: nothing branched, committed or pushed.

Numbering in filenames follows the **audit's** numbers, not delivery order, so
`fig-08` and `fig-12` are absent by design (Code) and `fig-15` is deferred.

---

## 1 · What every figure does the same way

- **Cream #FBF3E6 ground, ink #221E1B, accent #E4572E as a graphic value only.**
  Small labels are `--ks3-accent-text` #A93411. Nothing needs recolouring.
- **No amber anywhere.** Not once, in any of the twelve — not as a category, not
  as an accent. `--ks3-alert` warns and these figures have nothing to warn about.
- **No `--ks3-data` either.** It is minted in the engine's `tokens.css` under
  MRB-252 but is **not present in the shipped design-system token files** this
  work was drawn against. Rather than invent a hex for it, I removed the need:
  every distinction in these figures is carried by **shape, dash pattern,
  position, stroke weight, badge fill inversion or a numeral** — and by a label
  in every case. There is exactly one hue used as a category, below.
- **The one hue: `#2545A8` (`--ks3-blue-text`), blood in a capillary, in #7
  only** — matching the existing use in #5, which was already shipped in the
  earlier session. It carries a legend line, and the arrows carry the direction,
  so removing the colour loses nothing.
- **Greens are absent.** `--ks3-ok` is marks-and-fills for correctness only, so
  sepals in #9 are drawn as pointed flaps and labelled, never green. The figure
  says so on its own face: *"no colour in this figure carries a fact on its own."*
- **No `→`, `✓` or `✕` characters.** Every arrow is a drawn triangle plus a line.
- **No `{{ hole }}` inside any SVG `<text>`.** Every string in every drawing is a
  literal. (This bit once during the build — a nine-row key rendered as nine
  empty badges — which is exactly the failure mode the house rule describes.)
- **Each figure opens with a "What has to be checkable" band** naming the claim
  the drawing must make true. That band is the thing to review against, and it
  is where a future defect of the "coloured its boxes by the wrong rule" kind
  would be caught.
- **Reading order** runs drawing → labels → key → closing statement, and every
  `<desc>` walks the drawing in that order. Descs are 900–2,100 characters.
- **390px: these scroll, they do not shrink.** Each figure is a fixed-width SVG
  inside `overflow-x: auto` with `tabindex="0"`, `role="group"` and an
  `aria-label` ending "— scrollable diagram", which is the treatment the audit
  found WCAG-correct on the four existing code-drawn figures. No label is below
  13px, and the review switcher in each header renders the figure at Full / 768 /
  390 so a reviewer can check every label at width before implementation.
  **The switcher is a review affordance. Code should not implement it.**

---

## 2 · What I left out, and why

- **#6, the gut: no torso outline, and the coils are not in anatomical
  position.** The colon does not frame the small intestine here; the whole gut
  is one run down the frame. Drawn anatomically, the transverse colon has to
  cross in front of the small intestine and the duodenum has to cross back
  behind it, and at that point the reader is untangling two tubes instead of
  seeing one. The figure's job is continuity, order and the accessory
  distinction. **It says this on its own face**, bottom-right of the plate, so
  the simplification is disclosed rather than hidden. Wants ruling — see §4.
- **#7, the thorax: four divisions drawn, not twenty-three**, stated on the
  drawing. The branching is *generated recursively* rather than drawn by hand,
  so "divide, and divide again" is a property of the figure: each branch is
  0.7 of its parent's length and narrower, and the smallest tips carry sacs.
  Twenty-three generations is 8.4 million branches; four is what reads.
- **#7 shows one state.** No rest-versus-inspiration: that is #15, deferred.
- **#14: the key names the eight specimens and says nothing else about them.**
  No structural description, no "the tell", no method. Supplying the structure
  as prose is the defect this figure exists to remove, so repeating the
  descriptions beside the drawing would have undone it. See §3 — this is the
  brief I would argue with hardest, in the other direction.
- **#13: dropped "sepals often stay".** It is a real row on the page and a nice
  observation (the green star on a strawberry), but three labels were already
  competing for the top of that panel and it was the one carrying least weight.
  Easy to restore if wanted.
- **#2: no urethra label on the female side, no scrotal detail, no vas
  deferens/epididymis distinction.** Nine named structures and nothing else.
  The bladder is drawn, in grey, labelled *"no reproductive job"* — because the
  lesson's own note says the penis carries urine through the same tube, and a
  student who meets a bladder in a diagram with no explanation will place it.

---

## 3 · Where I would argue with the brief

**a. #14, "eight specimens drawn to scale", cannot be done at one scale and stay
legible — so I did it anyway, and flagged the seam.**

The range is real: goosegrass fruit-pair ~9 mm, coconut ~200 mm. That is 22:1,
and at a scale where the coconut fits an 852px plate the goosegrass is 17px
across, which is too small to infer hooks from. I kept **one scale** — the
comparison is the point, and two scales would have made the plate a lie — and
added a **single magnified detail of the goosegrass hooks, drawn at ×4 and
marked ×4 on the figure**, tied to the specimen with a dashed leader. A stated
magnification is not a broken scale; an unstated one would be.

The consequence is a plate with a lot of empty paper in it. I think that is
correct: the emptiness *is* the size difference, and it is the fact the prose
version cannot deliver. But it is a composition Mide may simply not want, and
it is the one figure here I would expect to be sent back.

**b. #14 again: the audit says "unlabelled by method", and I read that as
"unlabelled, full stop", except for the names.**

If the intention was "name the specimen and describe the structure, just not the
mechanism", say so and I will add the descriptions back. My reading is that a
student asked to infer mechanism from structure must be given the structure *as
structure*, and that a sentence describing hooks sitting next to a drawing of
hooks quietly re-converts the task into reading comprehension — the exact
finding in the audit's own "why prose falls short" column for this page.

---

## 4 · What I would like ruled

1. **#6's anatomical simplification.** One legible run down the frame, disclosed
   on the figure — or anatomical positions with two tube crossings? I chose the
   former. If the ruling is anatomical, the crossings need a drawn convention
   (a break in the tube behind) and the "one continuous path" claim gets harder
   to check, which was the whole point of the figure.
2. **#14's coconut at 200 mm.** The lesson gives no figure for it; sycamore
   (40 mm) and burdock (20 mm) are the page's own numbers and are used verbatim.
   200 mm is a whole husked fruit and it is **my** number. If a different one is
   wanted the whole plate rescales from it, which is a one-line change.
3. **#2's ninth structure.** The audit says the lesson names nine structures a
   student must place. The bench's `STRUCTURES` array holds **eight** — the
   vagina is not in it, though it is named in the key note and in
   `JOBS_COMPARE`. I numbered nine, with the vagina as 09. Confirm that is the
   ninth and not something else.
4. **#10's "about day 6".** The page says dividing takes "about five days" and
   that implantation is "several days later", which is a range, not a day. I
   printed **day 0** at fertilisation and **about day 6** at implantation
   because a number is what makes "days apart" checkable. If the science gate
   would rather it read "five or six days later" with no day numbers, that is
   two string changes and the figure survives it.
5. **The filled-badge device in #2** — a solid badge meaning "the male system
   has no counterpart for this" — is a convention I invented for that figure.
   It carries the lesson's named misconception ("the two systems are mirror
   images") inside the drawing rather than in a caption. Worth keeping? If so it
   should be written down somewhere, because the next figure that needs
   "this one has no partner" should use the same mark.
6. **Whether the review switcher and the "what has to be checkable" band stay
   in the implemented figures.** I assume both are for this review only and that
   Code drops them, keeping the `<title>`, `<desc>`, `<figcaption>` and the
   scroll container. Say if the band should survive into the page — there is an
   argument that a student benefits from being told what to look for, and a
   stronger one from §8.10 that they should not be told how the page works.

---

## 5 · Two things Code will want to know

- **The figures are self-contained SVG**, one `<g>` with `fill="none"` and
  per-element fills, no external assets, no new fonts, no raster. Font families
  are named inline as `'Bricolage Grotesque'`, `'Instrument Sans'` and
  `'DM Mono'` with system fallbacks, because SVG presentation attributes will not
  take `var(--ks3-font-display)`.
- **Four figures compute geometry rather than hard-coding it**, and those are
  the ones where a parity assertion has something to bite on:
  #1 (46 chromosomes on a jittered grid — a student who counts them finds 46),
  #7 (the recursive airway, and the magnified cluster picked as the lowest tip
  in the right lung, so the callout ring and the badge leader are derived, not
  placed), #9 (the feathery stigma's barbs sampled along the plume curves), and
  #14 (hooks, fibres, husk voids, pappus and drupelets all generated).
  Everything else is literal coordinates.
  Per §5A.4, each of those wants at least one assertion tying the encoding to
  the fact: #1 that the orange stroke is the same colour in all five panels and
  the count is 46; #7 that the sac clusters exist only at terminal tips and
  never on a bronchus; #14 that the drawn width ratio of coconut to goosegrass
  matches 200:9 within a pixel of rounding.
