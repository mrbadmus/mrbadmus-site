# KS3 design coverage manifest

**Purpose.** This document lists every distinct thing the Key Stage 3 page generator can put on a
screen, so that a visual design reference set can cover all of them and nothing turns up missing
when the design is integrated.

**Audience.** Written for a designer who has not seen this codebase and will not read it. Every
term is expanded on first use. Where the code and the written architecture disagree, the code is
reported as the fact and the disagreement is flagged.

**Read-only.** Nothing in the build was changed to produce this. Every number below was measured
by running the real data through the real generator, not estimated.

---

## 0. What you need to know before section 1

**What Key Stage 3 is.** In England, Key Stage 3 ("KS3") is school Years 7, 8 and 9 — ages 11 to
14. It is the three years before GCSE (the national exam course, ages 14–16, which this platform
calls "KS4"). KS3 has no exam board, no syllabus specification, no exam tiers and no subject
pathways. It has a short statutory document from the Department for Education listing what must be
taught. That absence of an exam is the single most important design fact: there are no marks, no
grade boundaries, no mark schemes and no "Higher tier" badges anywhere in KS3.

**The three sciences.** Biology, Chemistry, Physics. Each has its own accent colour, used for
subject identity only.

**The shape of the course.** 33 **units** (a unit is a multi-week block of teaching, e.g.
"Particles and their behaviour"), containing **183 lesson slots** in total. A lesson is roughly one
40-minute classroom lesson and is the atom of the system — one lesson, one web page.

**The state of the build, stated plainly.** Of the 183 lesson slots:

| | Count | What it renders as |
|---|---|---|
| Fully authored lessons | **6** | A real lesson page with all its content |
| Unwritten slots | **176** | A short "Coming soon" placeholder page |
| Cross-reference slots | **1** | No page of its own — it links to another discipline's lesson |

All six authored lessons are the same unit: **C1, "Particles and their behaviour"** (Chemistry,
typically Year 7). All six are marked `draft`, meaning not yet checked for scientific accuracy, so
all six currently show an under-review marker.

**Consequence for the design work.** There are only six real lesson pages in existence to design
against, and they are all one unit of one science. The other 177 slots are placeholders. A design
that only looks right on Chemistry particle lessons will break when Biology systems lessons and
Physics calculation lessons are written. Sections 1, 2 and 3 therefore describe the **full
vocabulary the generator can render**, not only what is currently on screen, and mark clearly which
parts have never yet been exercised by real content.

**Total pages the generator writes: 294.** That is 1 KS3 landing page + 3 discipline hubs + 33 unit
index pages + 182 lesson pages + 75 browse-layer index pages.

**Where the code lives.** The generator is `build_ks3.py`; the page behaviour is `shared/ks3.js`;
the styling is `shared/ks3.css`; the content is the `ks3_data/` folder; the governing design
document is `docs/ks3/architecture.md`. Section references below in the form "§5.1" point into that
architecture document.

---

## 1. Page families

Every lesson belongs to exactly one of seven **families**. A family is a teaching shape — it
decides which kinds of content block a lesson uses, how many, and in what order the middle of the
page runs. It is a plan for the page, not a visual style: the family name is printed on the page as
a small label above the lesson title, and otherwise has no visual consequence today.

The important design implication: **two lessons in different families have genuinely different page
shapes.** A lesson built around a simulation looks different from a lesson built around a
step-by-step mechanism, and that is deliberate. A design that assumes one page skeleton will fight
the system.

| Family | What it means, in one line | Lessons carrying it (of 183) | Named example |
|---|---|---|---|
| **MODEL** | One idea explains a whole class of behaviour. | **49** — Biology 8, Chemistry 17, Physics 24 | *The particle model* (unit C1) — **authored, viewable today** |
| **PROCESS** | A mechanism unfolds in steps. | **34** — Biology 12, Chemistry 15, Physics 7 | *Changes of state* (unit C1) — **authored, viewable today** |
| **SYSTEM** | Parts working together, and what happens when one part fails. | **32** — Biology 21, Chemistry 2, Physics 9 | *The digestive system* (unit B3) — not yet written |
| **CONTRAST** | Two things, one difference that discriminates between them. | **18** — Biology 4, Chemistry 7, Physics 7 | *Solids, liquids and gases* (unit C1) — **authored, viewable today** |
| **INVESTIGATION** | The scientific skill itself is the subject (fair testing, graphs, measurement error). | **18** — Biology 7, Chemistry 5, Physics 6 | *Testing the model: does it explain everything?* (unit C1) — **authored, viewable today** |
| **QUANTITATIVE** | A calculation carries the concept. | **17** — Biology 2, Chemistry 2, Physics 13 | *Speed* (unit P3) — not yet written |
| **CLASSIFY** | Decide which category, fast, and know why. | **15** — Biology 4, Chemistry 7, Physics 4 | *Acids and alkalis* (unit C6) — not yet written |

Counts sum to 183.

**Three families have never been rendered with real content:** SYSTEM (32 lessons), QUANTITATIVE
(17) and CLASSIFY (15). That is 64 of 183 lessons — just over a third of the course — whose page
shape exists only as a written intention. In particular:

- **QUANTITATIVE** is the only family that routinely needs a calculation layout. The generator has
  exactly one calculation component (see "FIFA" in section 2) and it has been used once, in one
  Chemistry lesson. Thirteen of the seventeen QUANTITATIVE lessons are Physics.
- **SYSTEM** is a Biology-heavy family (21 of its 32 lessons). Its defining component is
  "perturbation" — break one part of a system, predict the knock-on effect, reveal the result.
  Nothing like that has been built yet.
- **CLASSIFY** needs sorting and category-decision components. Nothing like that has been built
  yet.

**The two "authored" families are unevenly represented too.** Four of the six written lessons are
MODEL or CONTRAST. Only one PROCESS lesson and one INVESTIGATION lesson exist.

---

## 2. Block types

A lesson page is assembled from a **closed list of ten block types**. "Closed" means the generator
refuses to build and stops with an error if a lesson asks for anything not on this list; adding an
eleventh type requires a written amendment to the architecture document. This is the single most
useful fact in this manifest: **the renderer will only ever have ten kinds of section to style.**

In the table, "CSS class" is the class attribute the generator actually writes into the HTML.

| Block type | What it is for | Can it repeat in one lesson? | CSS class it renders as |
|---|---|---|---|
| `hook` | The opening phenomenon — something observed, not something defined. Ends in a commitment ("which do you think?"). Required, and always first. | No — one per lesson | `ks3-block ks3-hook` |
| `explainer` | Body prose. Capped at about 90 words before the student must do something, and about 450 words per whole lesson. | Yes — up to 3 observed | `ks3-block ks3-explainer` |
| `figure` | A diagram or image. | Yes — up to 2 observed | `ks3-figure`, plus `ks3-figure-pending` when the artwork does not exist yet |
| `worked-example` | A calculation or procedure modelled for the student. Never allowed to ship without its `check` partner. | Yes in principle — **used exactly once in all existing content** | `ks3-block ks3-worked` |
| `check` | The student does the same thing themselves and produces the same artefact. The workhorse block. | Yes — up to 7 observed, the most repeated block by far | `ks3-block ks3-check` |
| `keyword` | Vocabulary: technical terms introduced with plain-English definitions, sometimes with a note about a word it is confused with. | No — one per lesson observed | `ks3-block ks3-keywords` |
| `practical` | A hands-on or simulated investigation. This is where the particle simulations live. | Yes — up to 2 observed | `ks3-block ks3-practical` |
| `misconception` | The block that confronts a specific wrong belief head-on: draw it out, show it failing, replace it. Required in every lesson. | Yes — up to 2 observed | `ks3-block ks3-misconception` |
| `summary` | The "key note" — a photographable revision card. Always last before the ladder ends the page. | Effectively no | `ks3-block ks3-keynote` |
| `quiz` | The four-rung mastery ladder that ends every lesson. | Effectively no | `ks3-block ks3-ladder` |

**Two of these ignore their own content.** `summary` renders a single dedicated field on the lesson
record (the key note), and `quiz` renders the lesson's entire four-rung ladder. Neither reads
anything from the block itself, so a second copy would simply duplicate the first. Treat both as
one-per-page.

**Two things that are *not* block types, and this matters.** Flip cards and particle simulations
are **not** blocks. They are optional extras that can appear *inside* a `check`, `practical` or
`misconception` block. This was a deliberate choice so that the ten-type list stays closed. When
designing, expect a card grid or a canvas simulation to appear as a component nested inside one of
those three section types, never as a section of its own.

**Sections the generator adds automatically, outside the ten types.** Every authored lesson page
also gets, in this order after the blocks:

| Auto-section | CSS class | When it appears |
|---|---|---|
| Header: unit name · family label, lesson title, big question, draft marker | `ks3-lesson-head` | Always |
| "Going further" — the stretch layer | `ks3-layer ks3-stretch` | When the lesson has stretch content (all 6 do) |
| "Need a hand?" — the support layer | `ks3-layer ks3-support` | When the lesson has support content (**0 of 6 do**) |
| "Before this lesson" — prerequisite lesson links | `ks3-block ks3-prereqs` | When the lesson declares prerequisites |
| "Connects to" — cross-discipline references | `ks3-block ks3-refs` | When the lesson references another discipline's lesson |
| "At GCSE this becomes" — forward links into the exam course | `ks3-block ks3-ks4` | When the lesson declares GCSE links (all 6 do) |
| "Stuck? Ask Mr Badmus AI" | `ks3-block ks3-tutor` | Always |

**One invisible element to be aware of.** Each activity block writes a paragraph
`<p class="ks3-demand" hidden>` recording the intended cognitive demand of the activity. It is
authoring metadata, hidden from view, and should stay hidden.

---

## 3. Activity kinds

An **activity** is the interactive unit inside a block: a prompt, optionally some answer buttons,
optionally a reveal, optionally a card grid or a simulation. There are 50 activity records across
the six written lessons — exactly one per activity-bearing block.

**Critical fact for a designer: the generator does not branch on `kind` at all.** The `kind` value
is authoring metadata. What actually decides how an activity renders is **which keys are present**
on the record — if there are `options`, buttons render; if there is a `sim`, a canvas renders; and
so on. So `kind` tells you the author's intent, and the key list tells you what appears on screen.
Both are given below.

"Gated by a prediction" means: the student must click one of the answer buttons before the answer
area unhides. That gate is driven purely by the presence of `options` alongside a `reveal`.

| `kind` | Count | Keys always present | Keys sometimes present | Gated by a prediction? |
|---|---|---|---|---|
| `construct` | 14 | `id`, `kind`, `demand`, `prompt`, `success` | `targets` | **No** — the student writes an answer and self-marks against a plain-English success list |
| `predict` | 12 | `id`, `kind`, `demand`, `prompt`, `options`, `answer`, `reveal`, `targets` | — | **Yes**, all 12 |
| `confrontation` | 7 | `id`, `kind`, `demand`, `prompt`, `reveal`, `targets` | — | **No** — the reveal has no buttons in front of it and is visible from the start |
| `lab` | 7 | `id`, `kind`, `demand`, `prompt`, `options`, `answer`, `reveal`, `sim` | `targets` | **Yes**, all 7 — the simulation stays frozen until a button is clicked |
| `reveal-cards` | 5 | `id`, `kind`, `demand`, `prompt`, `cards` | — | **No recorded prediction** — see the note below |
| `classify` | 2 | `id`, `kind`, `demand`, `prompt` | `options`, `reveal`, `success`, `targets` | 1 of 2 |
| `predict-then-reveal` | 1 | `id`, `kind`, `demand`, `prompt`, `options`, `answer`, `reveal`, `targets` | — | **Yes** |
| `worked-example` | 1 | `id`, `kind`, `demand`, `prompt`, `fifa` | — | **No** |
| `investigation` | 1 | `id`, `kind`, `demand`, `prompt`, `success` | — | **No** |

Key meanings:

- `prompt` — the question or instruction. Always present.
- `options` — 2 or 3 answer buttons. Never more than 3 in existing content. (The mastery ladder is
  separate and always uses 4 — see section 5.)
- `answer` — the index of the correct option. Recorded but **not currently used in the rendered
  page for activities** (only the ladder uses correctness, section 5).
- `reveal` — the text that unhides after the commitment.
- `success` — a plain-English checklist the student marks their own written answer against. Renders
  as a collapsed "Check your answer" disclosure. Present on 16 of the 50 activities.
- `cards` — a flip-card grid. See section 5.
- `sim` — a particle simulation. See section 4.
- `fifa` — a four-line calculation layout: **F**ormula, **I**nsert, **F**ix, **A**nswer. This is the
  platform's house style for every calculation. Used **once** in all existing content.
- `targets` — the identifier of the specific wrong belief this activity is aimed at. Metadata; not
  rendered.
- `demand` — the intended thinking demand. Rendered hidden.

**`reveal-cards` and the prediction rule.** The system's fourth law says nothing is revealed until
the student has committed to a prediction. A card grid has no bet to place — "which word means the
tiny pieces everything is made of?" has one right answer and no interesting wrong ones. A ruling on
7 August 2026 settled this: a card grid discharges the rule through a **declared** prediction
rather than a recorded one. The student is asked in words to say the answer out loud before tapping.
The design consequences are binding and are checked automatically at build time:

- The card back is delivered hidden in the HTML, so no answer is on screen even briefly before the
  page script runs.
- **No hover reveal. No automatic flip.**
- One tap flips one card, and only that card.
- **The block must ask for the declaration in words.** A build check fails if a card grid ships
  without a commitment prompt above it.

---

## 4. Simulation kinds

There are **three** implemented simulations, and **seven** instances of them across the six written
lessons. Each is a canvas drawing of particles moving in a box, with sliders. They are the flagship
interactive component of the whole system.

Shared mechanics for all three:

- Canvas is 560 × 200 pixels in the markup, styled to scale fluidly to the container width with
  proportional height.
- Rendered inside the activity's section, alongside the answer buttons. That adjacency is what makes
  the prediction gate work — the script walks up to the enclosing activity, finds the buttons, and
  keeps the simulation frozen until one is clicked.
- The control panel and the readout paragraph are delivered **empty**; the script builds the sliders
  and writes the readout text. If the script fails to load, the page must not appear to promise
  controls it cannot deliver.
- The canvas carries a long written description for screen-reader users — one per simulation kind,
  plus the lesson's own caption appended, because a canvas is an empty rectangle to assistive
  technology.
- Animation runs only while the simulation is scrolled into view, and stops when the browser tab is
  hidden.

### The three kinds

| Kind | What it shows | Readout (the words under the canvas) |
|---|---|---|
| `particle-states` | 64 large particles. Cold: touching in a regular pattern, **vibrating on the spot**. Warm: still touching but jumbled, sliding past each other. Hot: far apart, moving freely. | `"Solid — particles are touching, in a regular pattern, and vibrating on the spot."` / `"Liquid — particles are still touching, but jumbled and sliding past each other."` / `"Gas — particles are far apart and moving freely in every direction."` The three bands are temperature under 33, 33–65, and 66 or above on a 0–100 scale. |
| `gas-pressure` | 90 particles bouncing in a box with a **movable wall**. Each wall strike counts as one push. | `"Wall hits per second: <N> — that IS the pressure. Squeeze the gas or heat it and the hits get more frequent."` Sampled every 500 milliseconds. |
| `diffusion` | 120 particles in two coloured populations — orange starting on the left, blue on the right — each on its own random path, mixing in **both directions at once**. | `"<N> orange particles have crossed to the right, and <M> blue ones have crossed to the left. Both ways at once — nothing is pushing them, and nothing is trying to spread out."` Correctly says "1 orange particle has" in the singular. |

Each simulation exists to kill a specific wrong belief, and the visual detail is not decorative:

- `particle-states` **must** show the solid vibrating, never frozen — "particles in a solid are
  completely still" is exactly the misconception the lesson is attacking.
- `gas-pressure` **must** express pressure as a count of wall hits — a number that merely goes up
  confronts nothing.
- `diffusion` **must** show movement in both directions — a one-way spreading animation would
  confirm the belief that particles "want" to spread out.

### Legal controls

The controls a simulation may declare are a **closed list of four**. The generator refuses to build
if a lesson names anything else, and the page script holds the matching list. This gate exists
because earlier content declared five dials that the script did not implement, and they rendered as
an empty or half-populated control panel with nothing to indicate the problem.

| Control | Rendered as | Visible label | Range |
|---|---|---|---|
| `temperature` | Range slider | "Temperature" | 0–100, default 50 |
| `volume` | Range slider | "Space to move in" | 30–100, default 100 |
| `particles` | Range slider | "How many particles" | 10 to the population size, default full |
| `medium` | Two-option dropdown | "What it spreads through" | "In a gas" / "In a liquid" |

Every slider uses the accent colour as its fill, and is 8–12rem wide.

**Which controls each shipped simulation actually uses:**

| Lesson | Simulation kind | Controls |
|---|---|---|
| *Solids, liquids and gases* | `particle-states` | `temperature` |
| *Changes of state* | `particle-states` | `temperature` |
| *Gas pressure* (first of two) | `gas-pressure` | `volume` |
| *Gas pressure* (second of two) | `gas-pressure` | `volume`, `temperature`, `particles` |
| *Diffusion* (first of two) | `diffusion` | `temperature`, `medium` |
| *Diffusion* (second of two) | `diffusion` | `temperature` |
| *Testing the model* | `diffusion` | `temperature`, `medium` |

So the widest control panel in existence is three sliders; the narrowest is one. A panel of four is
legal but has never shipped.

**One flag worth carrying into design.** The `volume` slider only has a visible effect in
`gas-pressure` — that is the only kind with a movable wall. If a future lesson declared `volume` on
a `particle-states` or `diffusion` simulation, the build would pass and the slider would render and
appear to do almost nothing. That is a latent content trap, not a rendering state you need to
design for, but it means a "volume" slider should not be styled as if it were universal.

---

## 5. States

Every state below changes what appears on screen. Each is listed with the signal in the HTML that
carries it, so a design can be specified against something concrete.

### Lesson-level states

| State | Signal | What renders |
|---|---|---|
| **Draft / under review** | ⛔ **REVOKED — MRB-221, 16 Aug 2026** | The `.ks3-review-flag` marker paragraph and the `Draft` badge are **deleted**. Nothing renders here. Kept as a row so the state is not re-invented: it was a visible under-review marker in the lesson header, mandatory on every non-frozen lesson, and it existed to protect a student from unreviewed science. Mide and colleagues have since reviewed the content, so it protects nobody and says nothing true. `verify_ks3.py` now asserts its ABSENCE. Do not reinstate. ~~It must stay legible and prominent — the one thing on a page more important than the science is protecting a student from unreviewed science.~~ |
| **Reviewed and frozen** | Review state is "frozen" | No marker. **Zero lessons are in this state today.** |
| **Coming-soon lesson slot** | The lesson has no authored content | An entirely different, much shorter page: header with unit name and family label, then one section `ks3-block ks3-coming-soon` containing a small "Coming soon" tag, the single sentence *"This lesson has not been written yet."*, and a link back to the unit. **176 of 183 pages are in this state today.** |
| **Cross-reference slot** | The slot points at another discipline's unit | **No page at all.** It appears only as a row on index pages, styled `ks3-lesson-row is-ref`, carrying a badge naming the owning unit and a pointer paragraph: *"Taught in Chemistry — Particles and their behaviour. You'll meet the full lesson there."* There is exactly **one** of these in the whole course. |

### Figure states

| State | Signal | What renders |
|---|---|---|
| **Drawn** ⊕ | Figure status is "drawn" | An inline `<svg>` the generator drew itself, in the same 2px ink frame and 24px radius the image branch uses, carrying `<title>` and `<desc>`, announced as one image via `role="img"` and `aria-labelledby`, with the caption below. Every colour is a `--ks3-*` token; every distinction the drawing makes in ink is also stated in words in its legend. **Two figures are in this state — the oak wood web on b9-01 and b9-03.** |
| **Artwork exists** | Figure status is "drafted" or "final" | A normal `<figure>` with an image and a caption, sourced from `ks3/figures/<id>.svg`. **Zero figures are in this state today, and the directory that branch reads has never existed** — which is why naming a diagram slot could only ever produce the placeholder below, and why the `drawn` state above exists. |
| **Figure declared but pending** | Figure status is "needed" | An honest placeholder: a dashed-border box with a "Diagram coming soon" tag, plus the real caption underneath, and the caption also serves as the accessible description. **15 figures are in this state**, across B3, B4 and B5 — and none of those lessons authors a `figure` BLOCK to render one through, so the placeholder is reachable code with nowhere it currently appears. |

⊕ **The `drawn` state is Mide's ruling of 18 Aug 2026 (MRB-248): code draws the diagrams
itself, Design does not author a pass for them.** Inline SVG only — no raster, no external
asset, no new font. A drawer lives in `build_ks3.py`'s `SVG_ART`, a closed registry that
raises on an unknown name, and it must register components in §10.2 and carry parity rows or
the gate cannot see it. The bindings that are enforced in code rather than trusted:
`--ks3-accent` (3.4:1) raises if it is given text under 24px, and a link that would be drawn
through a third node's box raises rather than being drawn — on a food web that is not a
tidiness problem but a feeding relationship the data does not contain.

Every figure a lesson declares is also written into a generated sourcing worklist,
`docs/ks3/diagram-manifest.md`. These are **schematic** assets — a photograph of a beaker does not
substitute for a particle diagram, which is also why the `drawn` state can discharge one and a
photography commission cannot.

### Simulation states

| State | Signal | What renders |
|---|---|---|
| **Locked before prediction** | `data-locked="1"` on the simulation container | The canvas is **blurred by 2 pixels and desaturated to 65%**; a semi-transparent veil covering exactly the canvas area shows **"Make your prediction first — then the lab runs."**; the control panel is **hidden entirely**. One frozen frame is drawn behind the veil. The caption below stays readable, because it contains the instructions for the prediction. |
| **Unlocked** | The lock attribute is removed after any answer button is clicked | Veil gone, canvas sharp, controls appear, animation starts, readout begins updating. |
| **Unlocked, reduced motion** | Same, but the visitor has asked for reduced motion | **No animation at all.** The simulation is run forward internally for 1,400 steps to a settled state, one representative frame is drawn, and the readout carries the result in words. Every control change re-settles from scratch, so the single frame always matches the current slider positions. This is a complete experience, not a degraded one — nothing in the science is motion-only. |
| **Ungated** | The enclosing activity has no answer buttons | The simulation starts immediately with no veil. Legal, but no shipped content uses it. |

### Flip-card states

| State | Signal | What renders |
|---|---|---|
| **Resting (face down)** | `aria-expanded="false"`; the back is `hidden` | Card front only: bold text on a panel background, thin border, and an accent-coloured **dog-ear** in the top-right corner — a turned-up corner implying something underneath. The dog-ear is the mark that identifies the card as interactive. |
| **Flipped** | `aria-expanded="true"` and class `is-flipped`; the back is unhidden | Accent-washed background, accent border doubled to 2 pixels via an inset shadow, dog-ear fill removed, and the answer text appears beneath the front text. The visual language is deliberately identical to a reveal — it is the same act: the answer arriving after the commitment. |
| **Flipped, reduced motion** | Same, with reduced motion requested | The colour transition is switched off; the swap is instant. |

Each card is a real `<button>`, not a clickable box, so keyboard operation and assistive-technology
semantics come for free. `aria-expanded` is the source of truth; the visual class is only a
consequence of it.

### Mastery-ladder states

The ladder is the four-rung quiz that ends every lesson. Every lesson has exactly four rungs:
① Recall, ② Apply, ③ Explain, ④ Produce / transfer.

**The four rungs render in two visually different shapes, and this is completely regular across all
six lessons:**

| Rung | Shape | Answer buttons | Self-marking list |
|---|---|---|---|
| ① Recall | Multiple choice | **4 buttons** | No |
| ② Apply | Multiple choice | **4 buttons** | No |
| ③ Explain | Written answer | **None** | Yes — "Mark your answer against this list" |
| ④ Produce / transfer | Written answer | **None** | Yes — "Mark your answer against this list" |

So the bottom half of every ladder has no buttons at all: a question, then a collapsed disclosure
holding the plain-English criteria. Only the top two rungs are machine-markable, and only they
participate in the score and in "Retry my misses" — see the note at the end of this subsection.

| State | Signal | What renders |
|---|---|---|
| **Rung unlocked (unanswered)** | No lock attribute on the rung | Question, then answer buttons, all enabled. |
| **Rung locked (answered)** | `data-locked="1"` on the rung | **Every button in that rung is disabled**, the correct one is marked with a success border and tint, and a wrong choice the student made is marked with an error border and tint. A feedback line appears underneath. One attempt per rung until the student explicitly retries. |
| **Feedback: correct** | — | The single word "Correct." |
| **Feedback: wrong** | — | The **specific** correction written for that wrong answer, not a generic "try again". Every wrong option carries its own feedback text targeting the particular misconception it encodes. Falls back to "Not quite." only if none was authored. |
| **Score summary** | Appears once any rung is answered | A live line: *"You got 3 of 4."* If a previous best is stored: *"That's your best yet — up 1."* or *"Your best so far is 2."* Announced to screen readers as a status region. |
| **Retry available** | At least one rung answered wrongly | A **"Retry my misses"** button appears. Clicking it re-enables only the missed rungs, clears their feedback and marks, and moves keyboard focus to the first re-opened question. |
| **Retry unavailable** | No wrong answers outstanding | The retry button is hidden. |
| **Written-answer rung** | The rung has a success checklist instead of options | A collapsed disclosure: *"Mark your answer against this list"*. Rung ④ typically takes this form. Plain-English criteria — *"did you say the particles move faster?"* — never mark-scheme tariffs, because there is no exam board to award marks. |

Scores persist in the browser's local storage per lesson. **Never punish** is a standing rule: no
streaks, no guilt wording, no points, no timers.

⚠️ **Behaviour worth designing around, not designing over.** The score line counts only rungs
answered by button. Because rungs ③ and ④ have no buttons in any existing lesson, a student who
completes the whole ladder sees **"You got 2 of 2."** — never "of 4". The two written rungs
contribute nothing to the score and can never be a "miss". Whether that is the intended behaviour is
a product question for Mide, not a design one, but a score component sized for "of 4" will look
wrong against what the page actually says today.

### Option-button states — every state of every answer button ⊕

*Added 2026-08-12 (MRB-202).* The three tables below are the **complete** state set for every
option button the key stage renders, with the token each state resolves to and the name of the
assertion in `ks3_parity.py` that holds it. Nothing here is new rendering — every value is what
the build already produced, now written down and gated.

**Why this section exists.** Before it, the only option-button state registered anywhere was the
activity button *at rest*. Every state a student actually ends up looking at — the one they
chose, the one that was right, the one they got wrong, the ones that went spent — was compared
against nothing, so the parity gate reported green over all of them. That is what MRB-202 cost.
A state that is not in this section and not in `COMPONENTS` is a state nobody is checking.

**Where the states come from.** Layer C now drives the page into each state in a real browser
before measuring, because a state that only exists after a click cannot be read off the built
HTML. Three drives: `activity-chosen`, `dark-option-chosen`, `ladder-answered`.

#### Ladder options — the only surface allowed to mark right and wrong (R3)

Provenance: SPEC.md §5's option-state table, transcribed.

| State | Signal | Ground | Border | Badge fill / glyph | Mark |
|---|---|---|---|---|---|
| **Resting** | no state class | `--ks3-ground` `#FBF3E6` | `--ks3-option-border` `#DDCFB6` | `--ks3-band` / `--ks3-ink-muted` | letter A–D |
| **Chosen-correct** | `.is-correct` | `--ks3-ok-tint` `#E4F7EB` | `--ks3-ok` `#12A150` | `--ks3-ok` / white | drawn **✓**, `ks3-pop .35s` |
| **Chosen-wrong** | `.is-wrong` | `--ks3-band` `#F4E9D8` | `--ks3-ink` `#221E1B` | `--ks3-ink` / `--ks3-on-dark` | drawn **✕** |
| **Spent** | `.is-spent` | `--ks3-row-dim` `#FBF6EC` | `--ks3-option-spent` `#EBDFCB` | `--ks3-band` / `--ks3-ink-ghost` | letter, dimmed |

The correct answer is marked **whether or not the student chose it** — answering wrongly reveals
which one was right, in green, alongside their own choice in ink. All four buttons are disabled
once the rung is answered.

Feedback line: correct → `--ks3-ok-tint` on `2px --ks3-ok` with a drawn ✓ in `--ks3-ok-text`;
wrong → that option's authored correction on `--ks3-band` on `2px --ks3-ink` with a drawn ✕.

#### Activity options — never mark correctness (R3)

Provenance: SPEC.md §4, *"Resting `--ks3-ground` on `--ks3-option-border`. Chosen:
`--ks3-accent-tint` ground, `2px solid --ks3-accent`. R3: never green, never red, never
disabled."*

| State | Signal | Ground | Border | Badge fill / glyph |
|---|---|---|---|---|
| **Resting** | `aria-pressed="false"` | `--ks3-ground` `#FBF3E6` | `--ks3-option-border` `#DDCFB6` | `--ks3-band` / `--ks3-ink-muted` |
| **Chosen** | `aria-pressed="true"` | `--ks3-accent-tint` `#FCE7DE` | `--ks3-accent` `#E4572E` | `--ks3-accent` / `--ks3-on-dark` |

There is **no correct or wrong state here by design.** Every chosen option renders identically
whichever one it is, and `check_r3_runtime()` asserts that directly — it presses each option in
turn and requires the resolved colours to be identical and to contain no marking colour.

⚠️ **This is the surface MRB-202 was reported against, and R3 is why it looks the way it does.**
The authored data *does* carry the right answer (`"answer": <index>` on every `predict`), so the
information exists; R3 is a deliberate decision not to render it, so that committing before
revealing stays safe rather than becoming a test. Whether that holds is Design's **R10**, flagged
for Mide on 2026-08-09 and still unruled. Until it is ruled, this table is the specification and
the gate holds the build to it.

#### Options on an ink-dark block (hook, practical)

⚠️ **Translation, not transcription — the weakest provenance in this document.** SPEC.md §4 row 1
draws the hook's option buttons and puts its reveal on `--ks3-dark-panel` with a `2px` alert
border, which is where the alert accent comes from: orange on ink cannot be read. Design never
drew the **chosen** state of a dark option button. The values below are what the build renders
today, registered so they cannot drift while that screen is outstanding.

| State | Signal | Ground | Border | Badge fill / glyph |
|---|---|---|---|---|
| **Resting** | `aria-pressed="false"` | `--ks3-dark-panel` `#3E3730` | `--ks3-on-dark-muted` `#C6B9A7` | `--ks3-on-dark-muted` / `--ks3-ink` |
| **Chosen** | `aria-pressed="true"` | `--ks3-dark-panel` (unchanged) | `--ks3-alert` `#FFC53D` | `--ks3-alert` / `--ks3-ink` |

On this surface the chosen state is carried by the **border alone**, so that border is a
state-bearing mark and is held to 3:1 against the panel behind it.

### Prediction-gate states (activities that are not simulations)

| State | Signal | What renders |
|---|---|---|
| **Unanswered** | All option buttons `aria-pressed="false"`; the reveal is `hidden` | Prompt and buttons only. |
| **Answered** | The clicked button flips to `aria-pressed="true"` | The pressed button takes an accent border and accent wash. The reveal panel unhides — accent-washed box with an accent-tinted border — and is announced to screen readers. Unlike the ladder, buttons stay enabled and the student may change their choice; the reveal never re-hides. |
| **Reveal appearing, motion allowed** | — | Fades in over 220 milliseconds with a 4-pixel upward slide. |
| **Reveal appearing, reduced motion** | — | Instant swap, no animation. |

### Layer states

| State | Signal | What renders |
|---|---|---|
| **Stretch section present** | The lesson has stretch blocks | A section headed **"Going further"** with an uppercase small-caps heading over a hairline rule. Opt-in depth, visible to everyone, never allocated by a teacher. **All 6 written lessons have exactly 2 stretch blocks: one explainer and one check.** |
| **Stretch section absent** | No stretch blocks | Nothing renders. Legal. |
| **Support section present** | The lesson has support blocks | A section headed **"Need a hand?"**, same styling. Scaffolding on demand — worked examples, sentence starters, vocabulary pre-teach. |
| **Support section absent** | No support blocks | Nothing renders. **This is the state of all six written lessons.** The support slot is deliberately designed in and required to be *present but empty* on every lesson; writing support content is deferred. An empty slot is legal; a missing slot fails the build. |

There is **no tier and no attainment gating**. Nothing is ever hidden from a student because of who
the system thinks they are. Support and stretch are chosen by the student, in the moment, and cap
nothing.

### Index-row states

Lesson rows on index pages carry one of four appearances:

| Row state | What renders |
|---|---|
| **Written and frozen** | Number, title link, family label. No badge. (No lesson is in this state today.) |
| **Written but draft** | Same, plus a **"Draft"** badge with a tooltip repeating the under-review wording. This appears on browse-layer pages only. |
| **Not yet written** | Same, plus a **"Coming soon"** badge. |
| **Cross-reference** | Row wraps to two lines: number, title link to the owning discipline, a "from *unit code*" badge, and the pointer paragraph on its own line. |

### Browse-layer decorative states

| State | Signal | What renders |
|---|---|---|
| **Season tint** | `data-season="autumn" \| "spring" \| "summer"` | Half-term cards and page headers take one of three tints, derived from the half-term name. Autumn uses the strong accent, spring the success green, summer a contextual blue. The three are well separated from each other. |
| **Subject tint** | `data-discipline="biology" \| "chemistry" \| "physics"` | Subject cards take the subject's identity colour, shown as a coloured dot plus card accent. |
| **Year strip** | Six small spans on each year card | A miniature six-segment bar, one segment per half term, tinted by season. Purely decorative and hidden from assistive technology. |

---

## 6. Browse layer

There are **two independent routes** to the same 182 lesson pages, plus a chooser above them both.
Neither route mints a lesson URL of its own; both link to pages that already exist at a single
address.

### Route A — by year and term (the "browse layer", 75 pages)

This is the newer route and the landing page leads with it, because it matches how both a teacher
and a student actually think: *what am I doing this term?*

| Level | Address pattern | Pages | What it shows | What varies between instances |
|---|---|---|---|---|
| 0 | `/index.html` | 1 | Site chooser: Key Stage 3 or GCSE, with the helper line *"Not sure which one? Years 7, 8 and 9 are KS3. Years 10 and 11 are GCSE."* | Nothing — one page. Lives outside the KS3 generator. |
| 1 | `/ks3/index.html` | 1 | Three **year cards** (7, 8, 9), each with unit and lesson counts, a decorative six-segment season strip, and a "Browse by half term →" call to action. Below, a clearly-labelled secondary section offering the subject route. | Nothing — one page. |
| 2 | `/ks3/year-<n>/index.html` | **3** | Six **half-term cards** for that year, each with the half-term name, a lesson count, a unit count, and a per-subject split line ("Biology 4 · Chemistry 3 · Physics 4"). | Year number; the six counts. Lessons per half term range from **8 to 14**: Year 7 runs 11, 9, 10, 8, 9, 8; Year 8 runs 14, 14, 14, 14, 12, 11; Year 9 runs 10, 9, 8, 8, 8, 8. **Year 8 is the heavy year and this is stated rather than smoothed over.** |
| 3 | `/ks3/year-<n>/<half-term>/index.html` | **18** | Three **subject cards**, one per science, each with lesson and unit counts and the names of the units involved. | Always exactly three cards — every science appears in every half term of every year, guaranteed and asserted by the sequencing code. The season tint changes across the six. Unit-name lists vary in length and can run to several titles. |
| 4 | `/ks3/year-<n>/<half-term>/<discipline>/index.html` | **54** | The actual lesson rows, **grouped into unit sections**. Each group header reads e.g. "C6 · lessons 4 to 7 of 7" and links to the full unit. | Lessons per page range from **2 to 6**. A page may contain one unit group or several. A unit sliced across a term boundary shows its true position in the unit ("lessons 4 to 7"), not a restart at 1 — that slicing is expected, not a defect. |

Half-term slugs are `autumn-1`, `autumn-2`, `spring-1`, `spring-2`, `summer-1`, `summer-2`. Their
display names are "Autumn First Half", "Autumn Second Half", and so on.

Levels 2, 3 and 4 also carry a small "alternate route" link at the foot of the page ("← All six
half terms of Year 7", "The whole KS3 Chemistry course →").

### Route B — by subject and unit (36 index pages)

| Level | Address pattern | Pages | What it shows | What varies between instances |
|---|---|---|---|---|
| 1 | `/ks3/index.html` | (shared) | The secondary section on the landing page: three **discipline cards** with unit counts and written-lesson counts. | — |
| 2 | `/ks3/<discipline>/index.html` | **3** | A grid of **unit cards**, each with the unit code, title, and "N of M lessons" progress. | Biology has 11 unit cards, Chemistry 10, Physics 12. |
| 3 | `/ks3/<discipline>/<unit>/index.html` | **33** | Numbered lesson rows for the whole unit, plus a header line: "N of M lessons written · statutory area: …". | **Units contain between 3 and 9 lessons** — a card grid and a row list must both look right across a 3× range. Only **1 of 33 units** has an introduction paragraph; the other 32 have none, so that slot is usually empty. |
| 4 | `/ks3/<discipline>/<unit>/<lesson>.html` | **182** | The lesson itself, in one of the states in section 5. | — |

Every page in both routes carries a breadcrumb trail at the top, from 1 to 4 items deep, e.g.
`KS3 › Chemistry › Particles and their behaviour › The particle model`. The last item is always
plain text, not a link.

### The rule that governs the browse layer

**A year or a half term may appear on an index page. It may never appear on a lesson page — not in
the address, not in the folder name, and not in a single byte of the page.** The reason is
multi-school fit: a school may re-order the whole course, and doing so must regenerate only the
browse index pages while leaving every lesson page byte-for-byte identical. That property is
verified on every build.

Two design consequences follow directly:

1. **A lesson page can never say "you'll meet this in Year 9."** Where a lesson has to point at
   content owned elsewhere, the pointer says **where**, never **when** — *"Taught in Chemistry —
   Particles and their behaviour"* — because the "when" is false for any school teaching in a
   different order.
2. **The browse layer renders the platform's own suggested order, not any particular school's.** It
   must never claim to be a specific school's scheme. It also carries **no explanation of itself** —
   see the rule in section 8.

---

## 7. Content variance

**How to read this section.** Only **6 of the 183 slots** have content. Every range below marked
*(from 6 lessons)* is measured across those six — all Chemistry, all one unit. Treat them as the
narrowest possible sample, not as the shape of the finished course. Ranges marked *(all 183)* are
measured across every slot, because titles and family labels exist for all of them.

### Blocks per lesson *(from 6 lessons)*

| Measure | Minimum | Median | Maximum |
|---|---|---|---|
| Blocks in the core layer | **13** | 14 | **17** |
| Blocks in the stretch layer | 2 | 2 | 2 (identical in all six: one explainer, one check) |
| Blocks in the support layer | 0 | 0 | 0 |
| **Core + stretch total** | **15** | 16 | **19** |

Per-lesson block counts, core layer: 13, 13, 14, 14, 15, 17.

**Observed block sequences**, which show how much the middle of the page varies between families:

- *The particle model* (MODEL): hook, check, explainer, figure, check, check, misconception, figure,
  explainer, keyword, check, check, quiz, summary
- *Solids, liquids and gases* (CONTRAST): hook, check, explainer, misconception, check, practical,
  check, figure, keyword, practical, check, quiz, summary
- *Changes of state* (PROCESS): hook, check, misconception, figure, explainer, practical, figure,
  keyword, check, worked-example, check, check, misconception, check, check, quiz, summary
- *Gas pressure* (MODEL): hook, check, explainer, figure, misconception, keyword, check,
  misconception, practical, check, figure, check, quiz, summary
- *Diffusion* (MODEL): hook, check, explainer, practical, check, misconception, figure, keyword,
  check, figure, check, quiz, summary
- *Testing the model* (INVESTIGATION): hook, check, explainer, figure, practical, misconception,
  figure, keyword, check, check, misconception, check, practical, quiz, summary

Every lesson opens `hook` then `check`, and ends `quiz` then `summary`. Everything between differs.

### Block-type frequency *(from 6 lessons, all layers, 98 blocks total)*

| Block type | Total | Most in one lesson |
|---|---|---|
| `check` | 33 | 7 |
| `explainer` | 13 | 3 |
| `figure` | 11 | 2 |
| `misconception` | 9 | 2 |
| `practical` | 7 | 2 |
| `hook` | 6 | 1 |
| `keyword` | 6 | 1 |
| `quiz` | 6 | 1 |
| `summary` | 6 | 1 |
| `worked-example` | **1** | 1 |

### Other per-lesson ranges *(from 6 lessons)*

| Measure | Minimum | Median | Maximum | Values |
|---|---|---|---|---|
| Activities | **7** | 8 | **11** | 7, 7, 8, 8, 9, 11 |
| Vocabulary terms | **2** | 3 | **6** | 2, 3, 3, 3, 4, 6 |
| Misconceptions declared | **2** | 2 | **3** | 2, 2, 2, 2, 2, 3 |
| Figures | **1** | 2 | **2** | 1, 2, 2, 2, 2, 2 |
| Statutory statements owned | 1 | 1 | 2 | 1, 1, 1, 1, 2, 2 |
| Scientific-skill strands tagged | 1 | 2 | 3 | 1, 1, 2, 2, 2, 3 |
| Prerequisite lessons | 0 | 1 | 4 | 0, 1, 1, 1, 1, 4 |
| GCSE forward links | 1 | 1 | 1 | all 1 |
| Cross-discipline references | 0 | 0 | 1 | one lesson has one |
| Nominal lesson length, minutes | 35 | 40 | 45 | 35, 40, 40, 40, 45, 45 |
| Mastery-ladder rungs | **4** | 4 | **4** | always exactly four |
| Answer buttons per activity question | **2** | — | **3** | never more than 3 |
| Answer buttons per ladder question | **4** | 4 | **4** | always exactly four, on rungs ① and ② only |
| Ladder question length, characters | **19** | ~95 | **169** | the widest text range of any single component |
| Cards per card grid | **3** | 3 | **6** | 3, 3, 6, 4, 3 |
| Key-note length, characters | **156** | ~208 | **247** | 156, 171, 198, 217, 227, 247 |

### Text extremes

**Lesson titles** *(all 183 slots)*:

- Shortest: **"Speed"** — 5 characters (unit P3)
- Also short: "Joints" (6), "Density" (7)
- Longest: **"Life processes and what living things are made of"** — 49 characters (unit B1)
- Also long: "Temperature, particle motion and internal energy" (48), "Transverse waves,
  reflection and superposition" (46)

A title component must therefore sit comfortably at both 5 and 49 characters, in the page heading,
in a breadcrumb, in an index row and in a browser tab title.

**Big questions** — the one-sentence framing question under the lesson title. Present on **only the
6 written lessons**; the other 177 slots have none. All six, sorted by length:

| Characters | Lesson | Text |
|---|---|---|
| 27 | *The particle model* | "What is everything made of?" |
| 36 | *Changes of state* | "Where does the ice go when it melts?" |
| 43 | *Testing the model* | "Is the particle model true, or just useful?" |
| 50 | *Diffusion* | "How does a smell get across the room with no wind?" |
| 52 | *Gas pressure* | "What is actually pushing on the inside of a balloon?" |
| 53 | *Solids, liquids and gases* | "Why does a solid keep its shape but a liquid doesn't?" |

Shortest 27 characters, longest 53. Always exactly one sentence, always a question.

### Other content-level facts

- **All 11 figures in existence are placeholders.** No artwork has been drawn.
- **No lesson has support content.** The slot exists and is required, and is empty everywhere.
- **All six lessons carry the draft marker.** None is frozen.
- **Units range from 3 to 9 lessons.** Only one of 33 units has an introduction paragraph.
- Five units carry a written justification for being split out of a larger curriculum heading. That
  text is stored but **deliberately not rendered** — see section 8.

---

## 8. Hard constraints a design must honour

These are not preferences. Each is either enforced by an automatic build check or is a written
ruling that a page violating it is a defect.

### 8.1 Reduced motion

Anyone who has asked their operating system for reduced motion must get a **complete experience,
never a degraded one**. Specifically:

- Reveals swap instantly instead of fading and sliding.
- Flip cards swap instantly; the colour transition is removed.
- **Particle simulations do not animate at all.** Instead, the simulation is advanced internally to
  a settled state, one representative frame is drawn, and the readout states the result in words.
  Every control change re-settles from scratch so the frame always matches the sliders.
- Smooth scrolling is switched off site-wide.

The design rule that follows: **no information may exist only in motion.** Every animated
simulation has a written readout that says the same thing, and that readout is not optional
decoration — for a reduced-motion visitor it *is* the experience. A build check verifies a
reduced-motion fallback is present in the stylesheet.

### 8.2 Keyboard operability

- **Every interactive control is a real `<button>`, `<input>` or `<select>`.** No clickable
  `<div>`s. A build check enforces this.
- Every control has a visible focus ring — a 3-pixel accent outline with a 2-pixel offset. A build
  check verifies focus styles are present.
- State is carried in standard accessibility attributes, and the visual class is only ever a
  consequence: `aria-pressed` on prediction buttons, `aria-expanded` on flip cards.
- Lists that have their bullets removed restate their list role, because otherwise some
  screen-reader and browser combinations drop list semantics.
- "Retry my misses" moves keyboard focus to the first re-opened question.
- Live regions announce the score summary, each rung's feedback, the simulation readout, and any
  reveal that unhides — a sighted user sees new content appear, and a screen-reader user must be
  told.
- The simulation canvas carries a long written description of what the animation does, because a
  canvas is an empty rectangle to assistive technology. "Particle simulation" would be technically
  alt text and practically nothing.

### 8.3 The four-rung ladder

**Every lesson ends with exactly four rungs, always in this order:**

| Rung | Demand | Form at KS3 |
|---|---|---|
| ① | **Recall** | Retrieval and vocabulary. Fast and confidence-building. |
| ② | **Apply** | Use the idea on a new case; calculate; deduce. |
| ③ | **Explain** | Build a causal explanation from parts. |
| ④ | **Produce / transfer** | Write an answer and self-mark against a plain-English checklist; or predict a genuinely new situation; or design an investigation. |

Four is not a maximum or a target — it is the structure. In all existing content rungs ① and ② are
four-option multiple choice and rungs ③ and ④ are written answers with a self-marking checklist and
no buttons at all — two visually distinct rung shapes on every page. Rung ④ is marked against plain-English
success criteria, **never** mark-scheme tariffs, because there is no exam board to award marks and
pretending otherwise teaches a false model of assessment.

### 8.4 Law 1 — hook first

**Every lesson opens with something observed, never something defined.** A demonstration, a
photograph, a surprising result, a question about the everyday world. The definition arrives after
the student wants it. A lesson that opens at the abstract layer is a defect.

Design consequence: the top of a lesson page is a **phenomenon**, and it ends in a commitment. The
`hook` block is always first and always contains a prompt plus a commitment line. Nothing —
navigation, a definition, a summary, a contents list — may take that slot.

### 8.5 Law 4 — predict before reveal

**No interactive shows a verdict the student has not wagered on.** Every stateful reveal is gated
by a committed prediction. At this age this is not engagement decoration: an unspoken wrong belief
is invisible to its holder, and committing is what drags it into the open.

In practice:

- A reveal panel ships `hidden` in the HTML and unhides only on a button press.
- A simulation ships frozen behind a veil and runs only after a button press.
- A card back ships `hidden` in the HTML — **no hover reveal and no automatic flip** — and one tap
  flips only that card.
- **As amended 7 August 2026:** a card grid discharges the law through a **declared** prediction
  (the block asks the student in words to say the answer before tapping) rather than a recorded one,
  because a vocabulary recall has one right answer and nothing to bet on. The renderer's obligation
  is undiminished, and a build check fails if a card grid ships without a commitment prompt above
  it.

### 8.6 Law 9 — motion is meaning

**Any transfer, movement or state change is animated as visible movement, never a frame swap.** A
particle moving from A to B travels; it does not disappear and reappear. Reduced-motion visitors get
the instant swap, per 8.1.

The corollary is stricter than it sounds: motion that carries no meaning is not covered by this law
and does not earn its place. Decorative animation is not what Law 9 asks for.

### 8.7 The interactive budget, as amended 7 August 2026

The base rule: **one flagship instrument, one mid-size instrument, micro-widgets as needed, plus the
ladder.** Lower than the GCSE pages' ceiling, because the page is shorter and the learner is
younger.

The 7 August amendment settles what counts:

> **The budget counts stateful instruments only.**

An instrument holds state — it has a before and an after, it can be got wrong, it can be abandoned
half-finished, and it competes for the student's working memory with the idea the page is teaching.
That is what the budget rations.

- A **worked example plus its do-it-yourself counterpart is exempt.** A worked example holds no
  state: it does not respond, cannot be got wrong, and cannot be left in a bad state. Its
  counterpart is the student doing the same thing on paper. Neither is charged against the budget.
- **The exemption is about state, not about the label.** An "interactive worked example" that
  remembers where the student is, marks their entry, or gates a reveal *is* an instrument, and it
  counts.
- **What is untouched:** a worked example still never ships without its do-it-yourself counterpart.
  The pair is exempt from the budget, not from that pairing rule.

Design consequence: **at most two heavyweight interactive components per lesson page**, and the page
must be able to carry a modelled calculation alongside them without the layout feeling overloaded.

### 8.8 The platform does not explain itself on the page

Ruled 7 August 2026. **Student-facing pages must not carry explanatory text about how the platform
works.** The trigger was a full-width callout at the top of all 75 browse pages beginning *"This is
the MrBadmusAI default sequence…"* — written to a teacher, on pages read almost entirely by
students, answering a question nobody had asked, occupying the prime slot above the cards the page
exists to show.

The rule is deliberately a test, not a banned-phrase list:

> **Is this text telling the reader what to do with the thing in front of them — or is it the
> platform explaining its own reasoning to someone who did not ask?**

The first stays. The second goes. Three pieces of copy were removed under it, and they are worth
knowing about because a designer might reasonably want to add them back:

- The browse-layer explanation of how the teaching order was derived — **removed**.
- "Why this is its own unit: …" on unit pages — **removed**. The reasoning is still stored in the
  data; it just is not printed.
- The family gloss ("One idea explains a whole class of behaviour") on coming-soon pages —
  **removed**. The seven families are real and still govern the build; they are not page copy.

What was **kept**, and must stay:

- The cross-reference pointer that says where a lesson lives.
- The draft marker, the "Draft" badge and the "Coming soon" tag — these protect a student from
  unreviewed science.
- The "Prefer to browse by subject?" invitation, because two routes are visible and the reader is
  genuinely holding that question.
- The Key Stage 3 / GCSE chooser helper line, because it resolves the exact choice the page asks
  the reader to make.

Where a note genuinely earns its place — legal, data protection, safeguarding — it stays, but
**small, at the bottom edge, never as a callout.** The single exception that outranks that is the
draft marker, which must stay visible enough to do its job.

A build check verifies the removed browse-layer callout has not returned.

### 8.9 Never punish

No streaks. No guilt wording. No points or experience bars. No timers. A low score gets a diagnosis
and a route to a real lesson that would help, never "try again".

### 8.10 No exam-course furniture

These exist on the GCSE pages and **must not appear on a KS3 page**:

| Not allowed | Why | What replaces it |
|---|---|---|
| Examiner tips | No exam board, no examiner | A "say it like a scientist" framing — how to word an explanation |
| Specification code pills (e.g. "5.2.1.2") | No specification | Statutory-coverage indicator and topic-thread chips |
| Tier badges (Higher / Foundation) | No tiers at KS3 | Nothing. Depth is the opt-in stretch and support layers |
| ⭐ Higher and 🔬 Triple markers | Meaningless at KS3 | Nothing |
| Mark-scheme tariffs | No board awards marks | Plain-English success criteria |

### 8.11 Brand and shell constraints

- KS3 pages are public-facing, so they take the **orange chevron logo plus "MrBadmusAI"** brand mark
  in the navigation bar — not the plain-text brand used on internal dashboards.
- Every KS3 page body carries **both** `class="rd"` and `data-mode="ks3"`. A build check enforces
  this, because the KS3 colour and radius dials only apply when both are present.
- KS3 needs nothing beyond the existing shared token set. Anything additional is an addition to the
  KS3 block of the shared token file, **never a new stylesheet and never a raw colour value in the
  KS3 stylesheet**.
- The content column is capped at 44rem.
- Accessible-contrast note carried over from the current build: the KS3 accent colour **fails
  WCAG AA at body-text size** on most of the cream page grounds. It is used for large text, rules,
  fills, borders and focus rings; a separate darker accent token exists for body-size text. Any new
  accent-coloured text must use that darker token.

---

## 9. Things that do not exist yet

Added because the purpose of this manifest is that nothing is discovered missing at integration.
These are gaps in the current build, not design instructions.

| Gap | Detail |
|---|---|
| **No frozen lessons** | Every written lesson is a draft carrying the under-review marker. The "no marker" state has never been rendered. |
| **No real artwork** | All 11 declared figures are placeholders. The "figure with an image" state has never been rendered. |
| **No support-layer content** | The "Need a hand?" section has never been rendered. |
| **177 of 183 lessons unwritten** | Three of seven families — SYSTEM, QUANTITATIVE, CLASSIFY, 64 lessons between them — have no authored example at all. |
| **One calculation only** | The Formula / Insert / Fix / Answer layout has shipped once. Seventeen QUANTITATIVE lessons, thirteen of them Physics, will need it. |
| **No end matter** | The architecture specifies a closing block with score-plus-delta, the AI tutor and previous/next navigation. What the generator actually writes is a static "Stuck? Ask Mr Badmus AI" heading and one line of text — **the tutor is not wired up on KS3 pages, and there are no previous/next links.** |
| **No stepper rendering** | A stepped presentation is permitted where a family calls for it, especially PROCESS lessons. None is implemented; PROCESS content currently renders as ordinary stacked blocks. |
| **Components named but not built** | The architecture names several inherited components for future use — sorting and matching interactions, an explanation-chain builder, a write-then-self-mark component. None is wired into the KS3 generator. Rung ③ and rung ④ currently render as an ordinary question and a self-marking checklist. |
| **Simulation control gap** | Of the four legal simulation controls, no shipped simulation uses all four; the widest panel is three sliders. The `volume` slider only has a visible effect in the gas-pressure simulation. |
| **`answer` unused outside the ladder** | Activities record which option is correct, but activity buttons never mark right or wrong. Only the ladder does. |
| **Ladder score tops out at 2** | Rungs ③ and ④ carry no buttons, so the score line reads "You got 2 of 2" on a fully-completed four-rung ladder. See the warning in section 5. |

---

## 10. AUTHORITATIVE REGISTRY — the rows `verify_ks3.py` reads

⚠️ **Sections 0–9 above are descriptive. This section is not.** `verify_ks3.py` parses
the two tables below and **fails the build** against them. MRB-203, ruled after Design
sign-off on 11 August 2026:

> The parity gate cannot see a component that was never registered. Layer C measures
> registered components to ±1px and layer B checks structural rules. Neither can see a
> component that is not in the reference set at all.

Absence-of-selector already fails. This section makes **absence-of-registration** fail too,
which is the hole that let B1 ship with no progress rail, smaller type and a flat uniform
stack while the gate reported green over 116 assertions across 40 components.

Do not edit a row here to make a build pass. A row is a claim that Design has **drawn**
the thing. If the drawing does not exist, the correct action is to get it drawn.

### 10.1 Architecture family → the reference screen that defines it

A lesson may only be authored in a family that has an approved reference screen. Author a
lesson in a family with no row here, or with a row pointing at a file that does not exist,
and the build fails naming the family.

| Family | Slots | Reference screen | Approved |
|---|---|---|---|
| MODEL | 50 | `docs/ks3/design-reference/b1/b1-03-animal-and-plant-cells.dc.html` | Mide, 12 Aug 2026 |
| PROCESS | 34 | `docs/ks3/design-reference/KS3 Reference Set (offline).html` | Mide, 8 Aug 2026 |
| SYSTEM | 32 | `docs/ks3/design-reference/b1/b1-04-specialised-cells.dc.html` | Mide, 12 Aug 2026 |
| INVESTIGATION | 18 | `docs/ks3/design-reference/b1/b1-02-using-a-microscope.dc.html` | Mide, 12 Aug 2026 |
| CONTRAST | 18 | `docs/ks3/design-reference/b1/b1-06-unicellular-organisms.dc.html` | Mide, 12 Aug 2026 |
| CLASSIFY | 15 | `docs/ks3/design-reference/b1/b1-01-life-processes.dc.html` | Mide, 12 Aug 2026 |
| QUANTITATIVE | 17 | `docs/ks3/design-reference/b2/b2-04-biomechanics-forces-in-the-body.dc.html` | Design delivered 15 Aug 2026 · **awaiting Mide** |

⊕ **QUANTITATIVE rowed 16 Aug 2026 (MRB-220). It was the last unrowed family.** Design's B2/C1/C2
delivery includes two QUANTITATIVE pages — `b2-04 biomechanics-forces-in-the-body` and
`c2-06 conservation-of-mass` — so the drawing now exists, which is the only thing §10.1 asks for.

`b2-04` is named as the screen because it is the **product** case, and products are the majority
shape across the seventeen slots (speed, density, pressure, moments). It carries the MRB-204
four-part treatment in full: the formula alone in its own block, the drawn triangle, the
staged-reveal worked example, and the student filling the same steps before any independent
question.

`c2-06` is the **sum** case and is the second screen for the family, not a competitor to the first:

| Relationship | Drawn as | Screen |
|---|---|---|
| product — `A = B × C` | triangle | `b2-04` |
| sum / conservation — `before = after` | balance beam + part–whole bar | `c2-06` |

Under **MRB-204 as amended 15 Aug 2026**, that split is the ruling rather than a divergence from
it: a triangle encodes one quantity as the product or quotient of two others, and *everything
before = everything after* is neither, so drawing it as a triangle would teach a false
relationship to make a rule fit. Measured on the page, `c2-06` contains the word "triangle" **zero
times**; it draws a level beam with two pans, and a part–whole bar whose parts sum to the whole to
the pixel (296 + 8 gap + 146 = 450). Design flagged this as an open question (NOTES-C2 flag 14);
the amendment answers it and the page is already compliant. **No redraw is needed.**

The **Approved** column is deliberately not "Mide, 16 Aug 2026". Design has drawn it and the
family is unblocked for authoring, but the science on both pages is `draft` and Mide has not
reviewed either. The row records who drew it and when, and that his gate is still ahead.

Before the B1 delivery, SYSTEM and CLASSIFY were unrowed too — 32 + 15 = **47 of the 183
slots**, every one of which would have inherited whatever Code invented. Design's approved
B1 pages are what closed them; this delivery closes the last 17, and **every one of the seven
families now has a screen.**

### 10.2 Block type → the registered components that gate it

Every block type the generator can emit must map to at least one component registered in
`ks3_parity.COMPONENTS`. Render a block type with no row, or name a component in a row that
`ks3_parity` does not define, and the build fails naming the block type.

> **The `quiz` and `check` answered-state names were reconciled on 2026-08-13, and the
> registry is what caught it.** MRB-202 was worked twice on the night of 11–12 August by two
> sessions that never saw each other (MRB-211). Both registered every answered option state;
> they chose different names for them. This table was written against one set of names and
> the surviving `ks3_parity.COMPONENTS` uses the other, so on the first run after the rebase
> the registry failed with *"the registry claims cover that does not exist"* for both block
> types — twelve component names that no longer resolved. It named the block type and every
> missing component, which is precisely the job §10.2 was built for: a stale row here is a
> block type gated by nothing, and before this section existed it would have passed green.

| Block type | Registered components |
|---|---|
| hook | `hook is ink-dark, accent shadow`, `hook art sits on its own night ground`, `Motion control clears the 44px tap target` |
| explainer | `body prose (type row 4)`, `page ground + body type` |
| figure | `figure frame`, `figure caption`, `figure pending slot`, `drawn figure takes the photograph's frame`, `drawn figure scrolls rather than shrinking`, `drawn figure carries the page ground`, `thread label is accent-TEXT, never accent`, `thread badge is a drawn ring, not a tint`, `base-pair width guide is accent-TEXT`, `the drawn figure frame holds on b10-03 too`, `B11 moth pair · the pale moth is the band fill, not a dropped paint`, `B11 moth pair · the dark moth is the ink fill, not a dropped paint`, `B11 moth pair · the lichen bark is the band ground`, `B11 moth pair · the soot bark is the ink ground` |
| keyword | `vocabulary card`, `card term type` |
| quiz | `ladder shell`, `ladder heading`, `page-marked rung is accent`, `page-marked rung heading`, `self-marked rung is violet`, `ladder option CHOSEN-CORRECT`, `ladder option CHOSEN-CORRECT badge`, `ladder option CHOSEN-WRONG`, `ladder option CHOSEN-WRONG badge`, `ladder option SPENT`, `ladder option SPENT badge`, `ladder feedback CORRECT`, `ladder feedback WRONG` |
| summary | `key note is ink-dark`, `key note type drops to 700` |
| misconception | `misconception is amber`, `second confrontation is divided in amber`, `scorecard figure is mono 32px, not a heading` |
| check | `activity option resting`, `activity option CHOSEN`, `activity option CHOSEN badge`, `board lamp is a column, not an option row`, `board lamp badge is a 28px display square`, `board verdict is ink-dark`, `board tally is mono 24px`, `sorter row is a card on a hairline, not an option`, `sorter chip is 16px, narrower than a segment`, `self-check options are a plain grid`, `settles-it feature is a panel, not a row`, `settles-it choice is 16px on the ground`, `settles-it why is ONE tone (MRB-196)`, `case verdict is ink-dark with an alert label`, `bench cell picker is a full-width ROW, not a segment`, `tuning dial is a fixed 74px mono chip`, `zoom slider clears the 44px tap target`, `zoom gain label is accent-text mono`, `awkward row is unmarked until opened`, `cell-bench part row carries a numbered badge`, `cell-bench readout name is display 800 at 25px`, `pair row is the sorter's sibling, not the sorter`, `fit-parts installs as a wrapping row of pills`, `a fit chip is a pill on the dark block, not a light option row`, `the fit job panel is the dark nested panel, not a cream inset`, `the fit results card re-declares ink on its own cream ground`, `critique step is a full-width tappable row`, `critique verdict is indented under its badge`, `FIFA field is a real text input at tap size`, `model line is mono, so it reads as working` |
| worked-example | `R8 answer box`, `R8 check-my-answer button` |
| practical | `sim canvas`, `sim live figure is mono`, `sabotage chain's first link is the cell itself`, `removal outcome lands on a LIGHT panel`, `B10 variation-plotter · the characteristic label is muted mono`, `B10 variation-plotter · the chosen characteristic is the alert ground`, `B10 variation-plotter · an unchosen characteristic stays on the panel ground`, `B10 variation-plotter · the bench sits on the nested dark panel`, `B10 variation-plotter · the characteristic name is on-dark at 20px`, `B10 variation-plotter · the predict ask is on-dark, not muted`, `B10 variation-plotter · a predict button clears the tap target`, `B10 variation-plotter · the plot button is dimmed until a shape is committed`, `B10 variation-plotter · the plot button is inverted on ink`, `B10 variation-plotter · the chosen prediction takes the alert ground`, `B10 variation-plotter · the bars are drawn to the derived gap`, `B10 variation-plotter · the bar is the alert fill`, `B10 variation-plotter · the chart sits in a translucent well`, `B10 variation-plotter · the bin count is muted mono at 12px`, `B10 variation-plotter · the bin label is muted mono at 11px`, `B10 variation-plotter · the axis caption is muted mono, uppercase`, `B10 variation-plotter · the verdict is the page ground on an ink block`, `B10 variation-plotter · the verdict tag is accent-TEXT mono, never accent`, `B10 variation-plotter · the kind line is display 800 at 22px`, `B10 variation-plotter · the shape answer reads in ink body`, `B10 variation-plotter · the cause answer is divided off by a rule`, `B10 variation-plotter · the spent plot button dims`, `B10 zoom-bench · the ladder sits on the nested dark panel`, `B10 zoom-bench · an unreached level dims and takes no outline`, `B10 zoom-bench · an unreached level's name is muted`, `B10 zoom-bench · a reached level's name is on-dark headline`, `B10 zoom-bench · the scale figure is alert mono on every row`, `B10 zoom-bench · the level just reached takes the alert outline`, `B10 zoom-bench · a reached level's number is the alert chip`, `B10 zoom-bench · an unreached number is a muted outline`, `B10 zoom-bench · a revealed level body reads in on-dark body`, `B10 zoom-bench · the zoom button is inverted on ink`, `B10 zoom-bench · the back-out button is inverted on ink`, `B10 zoom-bench · the say-it-back panel is a well on the ink block`, `B10 zoom-bench · the say-it-back label is muted mono, uppercase`, `B10 zoom-bench · the chosen question is the alert ground`, `B10 zoom-bench · an unchosen question stays on the panel ground`, `B10 zoom-bench · the answer reads in on-dark body`, `B10 zoom-bench · the spent zoom button dims`, `B10 zoom-bench · the close is the page ground on an ink block`, `B10 zoom-bench · the last level is the one lit at the bottom`, `B10 model-builder · the dial name is muted mono, uppercase`, `B10 model-builder · the chosen dial is the alert ground`, `B10 model-builder · an unchosen dial stays on the panel ground`, `B10 model-builder · the bench sits on the nested dark panel`, `B10 model-builder · the model line is on-dark at 20px`, `B10 model-builder · an evidence card sits in a translucent well`, `B10 model-builder · a failing card takes the alert outline`, `B10 model-builder · a failing card's verdict is alert mono`, `B10 model-builder · the evidence name is on-dark at 18px`, `B10 model-builder · what the evidence IS reads in on-dark body`, `B10 model-builder · the elimination line is amber`, `B10 model-builder · the verdict is the page ground on an ink block`, `B10 model-builder · the verdict tag is accent-TEXT mono, never accent`, `B10 model-builder · the verdict body reads in ink body`, `B10 model-builder · a passing card takes the green outline`, `B10 model-builder · a passing card's verdict is green mono`, `B10 pea-cross · the parent name is muted mono, uppercase`, `B10 pea-cross · the chosen genotype is the alert ground`, `B10 pea-cross · an unchosen genotype stays on the panel ground`, `B10 pea-cross · the plot sits on the nested dark panel`, `B10 pea-cross · the cross line is on-dark at 20px`, `B10 pea-cross · the note reads in on-dark body on a well`, `B10 pea-cross · the grow buttons are inverted on ink`, `B10 pea-cross · the clear button is inverted on ink`, `B10 pea-cross · the most-recent-seed card is a well`, `B10 pea-cross · the seed label is muted mono, uppercase`, `B10 pea-cross · the seed line reads in on-dark body`, `B10 pea-cross · the tally name is on-dark at 17px`, `B10 pea-cross · the tally figure is muted mono`, `B10 pea-cross · the purple bar is the alert fill`, `B10 pea-cross · the white bar is the muted fill, not a second alert`, `B10 pea-cross · the bars sit in a translucent well`, `B10 pea-cross · the ratio line is alert mono`, `B10 species-cases · the case label is muted mono, uppercase`, `B10 species-cases · the chosen case is the alert ground`, `B10 species-cases · the bench sits on the nested dark panel`, `B10 species-cases · the case title is display 800 at 25px`, `B10 species-cases · the facts read in on-dark body`, `B10 species-cases · a verdict is a full-width row, not a segment`, `B10 species-cases · the verdict letter is a drawn ring, not a tint`, `B10 species-cases · the check button is dimmed until a verdict is chosen`, `B10 species-cases · the tally beside it is muted mono`, `B10 species-cases · the chosen verdict takes the alert outline`, `B10 species-cases · a spent unchosen verdict dims and takes no mark`, `B10 species-cases · the outcome is the page ground on an ink block`, `B10 species-cases · the outcome tag is accent-TEXT mono, never accent`, `B10 species-cases · the answer is display 800 at 22px`, `B10 species-cases · the reasoning reads in ink body`, `B10 species-cases · the spent check button dims`, `B11 advantage-bench · the conditions label is muted mono`, `B11 advantage-bench · the chosen condition is the alert ground`, `B11 advantage-bench · an unchosen condition stays on the block ground`, `B11 advantage-bench · the bench sits on the nested dark panel`, `B11 advantage-bench · the condition headline is on-dark at 20px`, `B11 advantage-bench · what the condition does is muted, not body`, `B11 advantage-bench · the variation's name is on-dark at 18px`, `B11 advantage-bench · the survival bar runs in a drawn track`, `B11 advantage-bench · the column's best is green and says so`, `B11 advantage-bench · the column's worst is amber and says so`, `B11 advantage-bench · an unranked figure is muted mono`, `B11 advantage-bench · an unranked bar is the muted fill`, `B11 advantage-bench · the reason under the bar reads in on-dark body`, `B11 advantage-bench · the verdict is the page ground on an ink block`, `B11 advantage-bench · the tied column marks nothing best`, `B11 advantage-bench · the tied column's figures are all muted`, `B11 selection-runner · the bark label is muted mono`, `B11 selection-runner · the chosen bark is the alert ground`, `B11 selection-runner · an unchosen bark stays on the block ground`, `B11 selection-runner · the bench sits on the nested dark panel`, `B11 selection-runner · what the bark IS reads muted, not body`, `B11 selection-runner · the generations sit in a fixed well`, `B11 selection-runner · a generation column shares the well`, `B11 selection-runner · the pale stack is the muted fill`, `B11 selection-runner · the dark stack is the alert fill`, `B11 selection-runner · the axis caption is muted mono, uppercase`, `B11 selection-runner · the pale figure matches the pale stack`, `B11 selection-runner · the dark figure matches the dark stack`, `B11 selection-runner · the note reads in on-dark body on a well`, `B11 selection-runner · the run buttons are inverted on ink`, `B11 selection-runner · the reset is inverted on ink too`, `B11 selection-runner · a run fills the well with columns`, `B11 pressure-bench · an axis label is muted mono`, `B11 pressure-bench · the chosen species is the alert ground`, `B11 pressure-bench · the chosen pressure is the alert ground too`, `B11 pressure-bench · an unchosen tab stays on the block ground`, `B11 pressure-bench · the bench sits on the nested dark panel`, `B11 pressure-bench · the species name is on-dark at 21px`, `B11 pressure-bench · a trait reads in on-dark body`, `B11 pressure-bench · a trait's name is muted mono at 13px`, `B11 pressure-bench · a rule divides the species from the pressure`, `B11 pressure-bench · the pressure headline is on-dark at 19px`, `B11 pressure-bench · what the pressure does reads muted`, `B11 pressure-bench · the outcome ask is on-dark at 17px`, `B11 pressure-bench · the outcome bar runs in a drawn track`, `B11 pressure-bench · a bottom-band outcome is amber and says so`, `B11 pressure-bench · a bottom-band bar is the amber fill`, `B11 pressure-bench · the outcome text is the page ground on ink`, `B11 pressure-bench · a top-band outcome is green`, `B11 pressure-bench · a top-band bar is the green fill`, `B11 blight-bench · the field label is muted mono`, `B11 blight-bench · the chosen field is the alert ground`, `B11 blight-bench · an unchosen field stays on the block ground`, `B11 blight-bench · the bench sits on the nested dark panel`, `B11 blight-bench · the field name is on-dark at 20px`, `B11 blight-bench · what was planted reads muted, not body`, `B11 blight-bench · a bar's name is on-dark at 17px`, `B11 blight-bench · a bar runs in a drawn track`, `B11 blight-bench · the variation bar is the muted fill`, `B11 blight-bench · the yield bar is amber, as the cost`, `B11 blight-bench · the unblighted field is a full green bar`, `B11 blight-bench · the release button is inverted on ink`, `B11 blight-bench · the clear button is inverted on ink`, `B11 blight-bench · a zero harvest is amber and says so`, `B11 blight-bench · the zero-survivor bar is the amber fill`, `B11 blight-bench · the verdict is the page ground on an ink block`, `B11 blight-bench · the spent release button dims` |
| key-fact | `KEY FACT box is band on an ACCENT shadow`, `KEY FACT label is mono accent-text`, `KEY FACT statement is display 700` |
| rule | `statement panel is band on a 3px ink border`, `statement is display 800 at the ruled clamp`, `statement cards take the option border`, `badged card is one column of full-width rows, not the auto grid`, `badged card is a two-column grid`, `initials badge is a 44px accent square`, `badged card's name is display 800 at 22px`, `badged card's role is accent-TEXT mono under the name`, `card limit is muted prose, not the mono example line` |
| formula | `formula panel is centred`, `formula statement takes the FORMULA clamp, not the rule's`, `formula triangle is drawn, not typed`, `triangle cover is ink and starts invisible` |
| comparison | `comparison rows are flex, not grid`, `comparison label stacks below 820`, `comparison content cells shrink to zero` |

⊕ **The four rows above are B1 round two's (13 Aug 2026).** Each block type is a
distinct SHELL, and every component registered against it pins the property that
makes it distinct rather than the properties it shares with everything else:

- `key-fact`'s shadow is **accent**, where a `.ks3-block`'s is ink. That single
  value is what stops the box reading as one more card. It is also why the box
  carries no badge, letter or mark — `--ks3-band` is the ground a chosen-WRONG
  ladder option takes (MRB-202), so anything mark-like here reads as a verdict
  on a line that is simply true.
- `rule`'s border is **3px with no shadow**, and its statement takes drift 3's
  **ruled** clamp rather than any one page's own.
- `formula`'s statement is **centred with `max-width: none`**. That is the
  entire difference between it and `rule`, whose statement is left-aligned at
  20ch; the two shells are otherwise identical and a future tidy-up will try to
  merge them. The pair exists to make that merge fail.
- `comparison` is **flex and never grid**, because a grid cannot produce the
  820px stack without a second query (MRB-210).


## Provenance

Every figure in this document was measured on 8 August 2026 against the working branch
`feat/ks3-entry`, at commit `a5754b66c`, by running the real content data through the real
generator. Sources read: `docs/ks3/architecture.md` (2,530 lines), `build_ks3.py` (1,341 lines),
`shared/ks3.js` (609 lines), `shared/ks3.css` (809 lines), `verify_ks3.py`, and the `ks3_data/`
content modules.

**Note on branches.** The `main` branch is behind: it has no browse layer, no flip cards, no
particle simulations, and its architecture document predates the 7 August rulings in sections 8.5,
8.7 and 8.8. This manifest describes `feat/ks3-entry`, which is the current state of the KS3 build.
