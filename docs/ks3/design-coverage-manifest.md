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
| **Draft / under review** | Lesson's review state is anything other than "frozen" | A visible marker paragraph `ks3-review-flag` reading **"Draft — not yet science-reviewed."** in the lesson header. Currently on **all six** written lessons. It is mandatory: a draft page without it is a defect. It must stay legible and prominent — the one thing on a page more important than the science is protecting a student from unreviewed science. |
| **Reviewed and frozen** | Review state is "frozen" | No marker. **Zero lessons are in this state today.** |
| **Coming-soon lesson slot** | The lesson has no authored content | An entirely different, much shorter page: header with unit name and family label, then one section `ks3-block ks3-coming-soon` containing a small "Coming soon" tag, the single sentence *"This lesson has not been written yet."*, and a link back to the unit. **176 of 183 pages are in this state today.** |
| **Cross-reference slot** | The slot points at another discipline's unit | **No page at all.** It appears only as a row on index pages, styled `ks3-lesson-row is-ref`, carrying a badge naming the owning unit and a pointer paragraph: *"Taught in Chemistry — Particles and their behaviour. You'll meet the full lesson there."* There is exactly **one** of these in the whole course. |

### Figure states

| State | Signal | What renders |
|---|---|---|
| **Artwork exists** | Figure status is "drafted" or "final" | A normal `<figure>` with an image and a caption. **Zero figures are in this state today.** |
| **Figure declared but pending** | Figure status is "needed" | An honest placeholder: a dashed-border box with a "Diagram coming soon" tag, plus the real caption underneath, and the caption also serves as the accessible description. **All 11 figures in existence are in this state.** |

Every figure a lesson declares is also written into a generated sourcing worklist,
`docs/ks3/diagram-manifest.md`. Of the 11: 6 are schematic diagrams, 4 are apparatus diagrams, 1 is
a graph. A fourth kind, "photo", is legal but unused. These are **schematic** assets — a photograph
of a beaker does not substitute for a particle diagram.

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
| QUANTITATIVE | 17 | — NONE — | ✗ NOT DRAWN |

**QUANTITATIVE is deliberately unrowed.** Seventeen slots, no approved screen, no authored
lesson. The first person to author one will be stopped by this table rather than by Mide
finding it at sign-off. That is the whole point of the section.

Before the B1 delivery, SYSTEM and CLASSIFY were unrowed too — 32 + 15 = **47 of the 184
slots**, every one of which would have inherited whatever Code invented. Design's approved
B1 pages are what closed them.

### 10.2 Block type → the registered components that gate it

Every block type the generator can emit must map to at least one component registered in
`ks3_parity.COMPONENTS`. Render a block type with no row, or name a component in a row that
`ks3_parity` does not define, and the build fails naming the block type.

| Block type | Registered components |
|---|---|
| hook | `hook is ink-dark, accent shadow` |
| explainer | `body prose (type row 4)`, `page ground + body type` |
| figure | `figure frame`, `figure caption`, `figure pending slot` |
| keyword | `vocabulary card`, `card term type` |
| quiz | `ladder shell`, `ladder heading`, `page-marked rung is accent`, `page-marked rung heading`, `self-marked rung is violet`, `ladder option chosen-correct`, `ladder correct badge is green, not accent`, `ladder option chosen-wrong`, `ladder wrong badge is ink, not amber`, `ladder option spent`, `ladder feedback, correct`, `ladder feedback, wrong` |
| summary | `key note is ink-dark`, `key note type drops to 700` |
| misconception | `misconception is amber` |
| check | `activity option resting`, `activity option chosen shows accent, marks nothing` |
| worked-example | `R8 answer box`, `R8 check-my-answer button` |
| practical | `sim canvas`, `sim live figure is mono` |


## Provenance

Every figure in this document was measured on 8 August 2026 against the working branch
`feat/ks3-entry`, at commit `a5754b66c`, by running the real content data through the real
generator. Sources read: `docs/ks3/architecture.md` (2,530 lines), `build_ks3.py` (1,341 lines),
`shared/ks3.js` (609 lines), `shared/ks3.css` (809 lines), `verify_ks3.py`, and the `ks3_data/`
content modules.

**Note on branches.** The `main` branch is behind: it has no browse layer, no flip cards, no
particle simulations, and its architecture document predates the 7 August rulings in sections 8.5,
8.7 and 8.8. This manifest describes `feat/ks3-entry`, which is the current state of the KS3 build.
