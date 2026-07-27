# KS3 Science — Canonical Architecture

**Status:** law for all KS3 builds. This document is authoritative and self-contained. If you are
opening it cold with no other context, you can build any KS3 topic from it.

**Scope:** Key Stage 3 science (Years 7–9), all three disciplines, on the MrBadmusAI platform.

**Authority order.** Where sources disagree:

1. **The statutory programme of study** — *National curriculum in England: science programmes of
   study, Key Stage 3* (DfE, 2014, still in force). This is the spine. Every lesson traces to it.
2. **This document.**
3. **`docs/redesign/architecture_v2.md`** (the bonding v2 doctrine) — inherited in spirit, and
   explicitly overridden where KS4 assumptions don't serve 11–14 year olds. Every override is
   named in §3.
4. Everything else — schemes of work, prior drafts, habit.

**What this document is not.** It contains no lesson content, no science, no code. It defines the
architecture that content and code must satisfy.

---

## 0. Provenance and known gaps

| Input | Status |
|---|---|
| Statutory KS3 programme of study (gov.uk, 2014) | **Read in full.** Primary source for §7. |
| `docs/redesign/architecture_v2.md` — bonding v2 doctrine | **Read in full.** Inherited per §3. |
| Existing generator, data-file pattern, design tokens, schools layer | **Surveyed.** See §8. |
| **Linear MRB-103 — previously ratified KS3 architecture** | **READ IN FULL, 2026-07-25.** Ticket body plus the 6 Jul 2026 ratification comment. Diffed against this document; delta recorded in §11 decision 1. |
| Rainford scheme of work | **Reference evidence and seed data — never a template** (§8.9). Whether a formal SoW document exists is still disputed (this document saw only folder structure; MRB-103 states Ayo ruled against "Rainford's actual SOW"), but the dispute is **no longer load-bearing**: since the 2026-07-26 reversal of §11 decision 5, nothing about the platform default depends on it. Rainford's map now lives in `ks3_data/school_schemes.py` as one school's configured sequence. |
| Westleigh scheme of work | **Outstanding — requested from Mide 2026-07-26.** The second school seed. Two divergent real schemes over identical lessons is the demonstration §4.5 exists for (§8.9). |

> ✅ **MRB-103 reconciliation: the diff is done** (2026-07-25), and the delta is in §11 decision 1.
> Nothing from MRB-103 has been applied to this document. Each conflict is written up as two
> positions with costs, per the rule below — Mide rules, then the amendment follows.
>
> ⚠️ Anything in MRB-103 that this document contradicts was contradicted *without having seen it* —
> those remain genuine open questions, not settled reversals.

**Convention used throughout:** ⊕ marks a design element that is the architect's addition beyond the
original brief, so a reviewer can see what was invented here versus what was asked for.

---

## 1. What KS3 is, and why it cannot be KS4 with easier words

KS4 on this platform is organised around an exam specification. AQA names the content, names the
tier, names the pathway, and — crucially — names the *reward*: marks, in a terminal exam, against
published mark schemes. The KS4 architecture is correct to be exam-shaped, because the student's
actual problem is an exam.

KS3 has none of that. There is no exam board, no specification, no tier, no pathway, no terminal
assessment. The statutory programme of study is 137 short bullet points of subject content (plus 18
Working Scientifically statements) for three years of three sciences — an order of magnitude less
prescriptive than AQA. That is not a gap to be filled by importing KS4 structure downward. It is a
different job.

*(Corrected 2026-07-25 from "roughly 120" once Phase 0 counted them —* `docs/ks3/statutory-register.md`.
*The exact figure matters: see §11 decision 11, where it collides with §7's lesson count.)*

**The KS3 job, stated plainly:** build the conceptual equipment that KS4 will later demand, in
students who are 11–14, many of whom have not yet decided whether science is for them.

Three consequences drive everything below.

**KS3 students are novices in the technical sense.** They have little domain knowledge to hang new
ideas on, so they cannot skim, cannot infer what matters, and cannot self-correct a wrong model.
Long continuous prose is not merely boring to them — it is close to useless, because they have no
schema to file it against. This is why the prose-blob architecture must not be reused, and it is a
stronger argument at KS3 than it ever was at KS4.

**The obstacle at KS3 is rarely the new idea. It is the old wrong idea.** Every KS3 topic collides
with a well-documented intuitive belief — heavier things fall faster, plants take food from the
soil, a moving object needs a continuous force, heat and temperature are the same thing, particles
themselves expand when heated. Teaching *around* a misconception leaves it intact; the student
learns the words and keeps the belief. KS3 content must confront these head-on, by name. This is
the single biggest content-architecture difference from KS4, and it is why §5.3 makes the
misconception a required, structured field rather than a prose aside.

**Sequence is a school's decision, not ours.** There is no statutory ordering of KS3 content, and
schools order it wildly differently — some spiral all three sciences every year, some teach
disciplinary blocks, some follow a published scheme. A platform serving many schools that hard-codes
one order is broken for most of them. Hence the invariant in §4.5: **year and sequence are soft,
overridable metadata and never appear in structure.**

---

## 2. Anti-goals ⊕

Stated explicitly so nobody rebuilds the thing we are moving away from.

| Anti-goal | Why |
|---|---|
| **The prose blob.** A page that is 1,200 words of theory with a quiz stapled on. | The named thing being moved away from. Fails novice learners hardest. |
| **Tier/pathway at KS3.** | There is no Foundation/Higher at KS3, and the database already forbids it (`profiles_tier_only_ks4_check`). Depth is handled by layers (§5.6), which is a different axis. |
| **Year baked into structure.** Folders named `year-7/`, URLs containing `/y8/`, content that branches on year. | Makes reordering a rebuild. Kills multi-school fit. |
| **A separate "Working Scientifically" unit.** | The statutory document is explicit that WS is taught *through* the content. A bolt-on unit gets skipped. See §5.7. |
| **Duplicating a lesson across two disciplines.** e.g. writing "diffusion" once for Chemistry and again for Physics. | Two copies drift. One owner, cross-referenced (§4.6). |
| **Gamification that punishes.** Streaks, guilt copy, XP, page leaderboards. | Inherited from bonding Law 8. Doubly important for 11-year-olds. |
| **Emoji doing content labour.** | Inherited from bonding Law 7. Drawn primitives carry meaning; emoji decorate at most. |
| **Building all three sciences at once.** | See the vertical slice, §9. |

---

## 3. Inheritance from bonding v2 — what carries, what changes

The bonding v2 doctrine is the best thinking this platform has produced about how a page should
teach. KS3 inherits its spirit wholesale. Five things change — the prose budget, the interactive
ceiling, the ladder's purpose, the frozen-field set, and the family list — and each change is
justified by the age of the learner or the absence of an exam board. Everything else carries.

| Bonding v2 | KS3 |
|---|---|
| Law 1 — demand-driven structure | **Inherited**, with a KS3 family set (§6): the demands differ across three sciences. |
| Law 2 — 150-word encode–act spine | **Tightened to ~90 words** (§5.2). Lower reading age, shorter attention. |
| Law 3 — three interactive scales at demand peaks | **Inherited**, ceiling lowered to one flagship + one mid + micros. |
| Law 4 — predict before reveal | **Inherited unchanged.** Serves novices *more* than experts: commitment is what makes a misconception visible to its owner. |
| Law 5 — watch/do duality | **Inherited unchanged.** |
| Law 6 — production-ending **exam** ladder | **Becomes the mastery ladder** (§5.8). Same four rungs, retuned: rung 4 is transfer and explanation, not AQA tariff. No exam board to tag against. |
| Law 7 — one design language | **Inherited unchanged**, with the KS3 accent already stubbed in the token layer. |
| Law 8 — persistence, never punish | **Inherited unchanged.** |
| Law 9 — motion is meaning | **Inherited unchanged.** |
| Law 10 — every activity exercises its claimed demand | **Inherited unchanged.** The sharpest review tool we have. |
| The 8 frozen science fields | **Replaced** by the KS3 review model (§5.10) — different fields, same discipline: science-bearing content is examiner-reviewed and then frozen; activities are built *from* frozen science. |
| Five architecture families | **Seven families** (§6). KS4 chemistry's set doesn't cover biological systems or investigation lessons. |

Everything not listed above — tokens, WCAG AA, full keyboard access, reduced-motion, vanilla JS, no
build step, generator determinism, the instrument-panel anatomy, tone tints, the end-matter ritual —
carries over unchanged. **KS3 is a new content architecture on the same design and delivery
system**, not a new platform.

---

## 4. The content model

### 4.1 The hierarchy

```
Discipline        biology | chemistry | physics          (3)
  └── Unit        a teachable sequence, 3–9 lessons      (33)
        └── Lesson  THE ATOM — one page, one idea        (185)
```

Three levels, deliberately. The statutory document has an inconsistent two-level structure
(Biology and Physics have area → sub-heading; Chemistry is flat). Normalising to Discipline → Unit →
Lesson makes all three disciplines the same shape. The statutory area is preserved as metadata on
the unit (`statutory_area`), not as a navigation level.

**Discipline is retained at KS3 even though most schools teach "Science".** Two reasons: the KS4
handoff is disciplinary, so the bridge edges (§4.7) need a disciplinary target; and content
ownership needs an unambiguous home. How this is *presented* to students is a separate, reversible
choice — see the open decision in §11.

### 4.2 The Lesson is the atom

**A lesson is one idea, one page, one sitting.** Target 25–40 minutes of student time, sized so a
teacher can set exactly one as homework, cover work, pre-teaching, or catch-up.

This is the most consequential sizing decision in the document, so the reasoning is explicit:

- **It matches how schools actually consume content.** The schedulable unit in a school is a lesson.
  A page that is half a lesson wastes a homework slot; a page that is three lessons cannot be set.
- **It matches novice working memory.** One idea per page means the page has one thing to be about,
  and the mastery ladder at the bottom can genuinely test *that idea* rather than sampling a blob.
- **It makes the prerequisite graph meaningful.** "Photosynthesis requires the particle model" is
  useless at page granularity if the page is the whole of chemistry.
- **It makes coverage auditable.** Statutory statements attach to lessons; coverage is then a
  computable property (§4.4), not a claim.

A lesson that cannot state its idea in one sentence is not a lesson; it is two.

### 4.3 Unit

A unit is the **release increment** and the **schedulable block**. Units are what a school's scheme
of work points at, what gets built and reviewed together, and what ships together.

A statutory strand may split into several units where it is too big to teach as one — "Chemical
reactions" is eight statutory bullets covering combustion, acids, pH, salts and catalysts, and
splits into three units. Splitting is a pedagogical judgement and must be recorded in the unit's
`split_rationale` field so it isn't silently re-litigated.

### 4.4 Statutory statement IDs ⊕ — the rigour mechanism

**Every statutory bullet gets a stable ID. Every lesson declares which statements it covers.**

This is the KS3 analogue of AQA spec points, and it is what makes the whole architecture defensible
rather than a matter of taste. Without it, "does our KS3 cover the national curriculum?" is a
question no one can answer.

**ID scheme:** `KS3.<D>.<STRAND>.<nn>`

- `<D>` — `B` | `C` | `P`
- `<STRAND>` — a short stable strand code (e.g. `PNM` = particulate nature of matter, `CR` =
  chemical reactions, `CELLS`, `FORCES`)
- `<nn>` — the bullet's ordinal within that strand **as printed in the 2014 document**, zero-padded

Example: `KS3.C.PNM.02` = the second bullet under Chemistry → The particulate nature of matter.

**Rules.**

1. IDs are **permanent**. Once assigned, an ID never changes meaning. If the statutory document is
   ever revised, new IDs are added and old ones marked `superseded`; they are never reused.
2. Every lesson has `covers: []` — the statements it is responsible for teaching — and may have
   `touches: []` for statements it supports but does not own.
3. **Every statement must be owned by exactly one lesson.** Zero owners is a coverage hole; two
   owners is duplicated content. Both are build-blocking defects.
4. The full enumeration lives in a companion file, **`docs/ks3/statutory-register.md`**, produced as
   the first task of the first build (§10.1). It is data; this document is architecture.

**What this buys us:** a coverage report per discipline; a defensible answer to a head of department
asking "what does this cover?"; safe reordering (statements move with lessons); and a rebuild path if
the statutory document is ever revised.

### 4.5 Invariant: year and sequence are metadata, never structure

**Binding rule. A violation is a defect, not a style choice.**

- A lesson carries `typical_year: 7 | 8 | 9` — **advisory only**. It seeds a sensible default order
  for a school that hasn't configured anything, and it may appear as a hint in authoring tools.
- `typical_year` **must never** determine a URL, a folder, a file name, a navigation structure, a
  content branch, or which lesson a student is served.
- Real ordering comes from the schools layer, which already exists and is already keyed on
  `(key_stage, year_group, …, academic_week)`. **Two tables, and they are not interchangeable:**
  `scheme_of_work_entries` is **global** — no `school_id` — and holds the platform default;
  `scheme_of_work_overrides` is **per-school** and holds what a real school actually does. **Both
  need constraint fixes before they can hold KS3 rows — see §8.7.** Until those land, this invariant
  is a promise the database cannot keep.
- Reordering a school's entire KS3 curriculum must require **zero content changes and zero
  regeneration** — it is a data change in that school's scheme of work.

The platform additionally publishes one **default sequence** (a named, versioned mapping of lessons
to year and week) so that a school with no scheme configured still gets a coherent journey. The
default sequence is *a* scheme of work stored the same way as any school's — not a privileged
structure.

> ⊕ **Where the default comes from, and where it must not come from. Ruled 2026-07-26.**
>
> **The default is derived from the statutory spine and the prerequisite graph — never from a
> school's timetable.** "MrBadmusAI default sequence v1" is §7's `typical_year` column, and it is
> the default *because* it was built that way: it follows what the programme of study says, ordered
> by what §4.9's `requires` edges make possible.
>
> ⚠️ **That second clause was asserted before it was checked, and it is very nearly true rather than
> true.** Checked 2026-07-26: **zero** forward references among authored lesson `requires` edges, and
> **exactly one** at unit level — see the defect recorded below. `verify_ks3.py` now enforces this
> property, with that single case as a named allowance, so a *new* forward reference fails the build.
>
> This was ruled the other way earlier the same day and **reversed** — see §11 decision 5. The
> reasoning behind the reversal is the reasoning behind this whole invariant. A default derived from
> one school's sequence is that school's product with a platform's name on it. Every other school
> then starts by disagreeing with us, and the divergence reads as *our* map being wrong rather than
> as the override mechanism working as designed. **The platform is school-agnostic. Real schemes are
> evidence and seed data (§8.9), never the template.**
>
> The strongest thing a real scheme can do for this invariant is *diverge* from the default and cost
> nothing to honour. That is what §9's reorder proof now tests, and it is why two divergent real
> schemes over identical lessons are worth more here than one adopted one.

> ⛔ **KNOWN DEFECT IN THE DEFAULT — one forward reference. Mide's call, not the build's.**
> *Found 2026-07-26 by the check described above, immediately after the default was ruled.*
>
> **`B3 Energy in food and what you need` (Biology, Y7) is a reference slot pointing at `P2 Energy at
> home` (Physics, Y9).** §7.4 fixes P2 as the owner of "energy in food, energy calculations", so
> under §4.6 B3's slot is a cross-link, not its own lesson. A Year 7 biology class therefore meets a
> slot whose content is not taught until Year 9 — **two years forward.** Structure-first means the
> page exists and nothing breaks; the problem is pedagogical, not technical.
>
> **This is not caused by the reversal, but the reversal widened it.** Under the superseded Rainford
> default the same edge ran Y7 → Y8, one year. Under §7's map it runs Y7 → Y9.
>
> **It is one of exactly two things, and which one is a decision, not a fix:**
>
> | Option | Change | Cost |
> |---|---|---|
> | **(a) Flip ownership to B3** | Amend §7.4: Biology owns "energy in food"; P2 references it. | Amends a table §7.4 calls *fixed*. But it is arguably the truer reading — B3's lesson is nutrition (*what you need*), P2's is an energy calculation, and §4.6 explicitly allows two lessons where the treatment genuinely differs. |
> | **(b) Move P2 earlier** | P2 → Y8. | Closes the gap to one year, does not eliminate it. P2 requires P1 *Energy* (Y8), so P2 cannot precede it, and **no placement of P2 removes the forward reference while B3 stays Y7.** |
> | **(c) Accept and render it** | Keep both; render the cross-link as an explicit forward pointer — *"you'll meet the full calculation in Year 9"*. | Zero structural change. Turns a silent forward reference into a deliberate one, which is the same move §4.7's `ks4_links` already makes across the key-stage boundary. |
>
> **Recommendation: (a) or (c), and (c) is cheaper.** (b) does not actually solve it. **Not acted on
> — this touches curriculum sequencing and ownership, which is Mide's gate.** Recorded here so it is
> a known, bounded, single case rather than something rediscovered during Year 7 authoring.

### 4.6 Cross-discipline lessons: single source, referenced ⊕

The statutory document deliberately teaches some ideas twice — the particle model appears under both
Chemistry ("The particulate nature of matter") and Physics ("Matter"); diffusion appears in
Chemistry and in Biology's cell transport; energy appears in Physics and in Biology's nutrition.

**Rule: one owning lesson, referenced from elsewhere. Never two copies.**

- Each lesson has exactly one `discipline` — its owner.
- Other units link to it via `references: [lesson_ids]`, which renders as a genuine cross-link in
  the unit page ("Physics: Matter — this unit uses *The particle model* from Chemistry").
- Where the second discipline needs a genuinely different *treatment* rather than the same content
  (Physics wants Brownian motion and internal energy; Chemistry wants states and changes of state),
  those are separate lessons owning separate statements — not duplicates.

Ownership decisions for the contested ideas are fixed in the topic map (§7) so this is not
re-argued per unit.

### 4.7 Threads and the KS4 bridge ⊕

Two more edge types on the lesson, both cheap to author and high value.

**Threads — the big ideas that run vertically.** Nine threads cross discipline and year:

`particles` · `energy` · `forces-and-fields` · `cells-and-systems` · `interdependence` ·
`substances-and-reactions` · `genes-and-evolution` · `earth-and-universe` · `structure-function`

> **Amended 2026-07-26 (§11 "also noted", ruled).** `structure-function` is the ninth thread, added
> on Mide's ruling. It is a genuine KS3 big idea named in the statutory preamble — *how a thing is
> built explains what it does* — and it runs from cell adaptations and leaf structure through alveoli
> and the digestive system to the reactivity of metals. This document originally named eight and
> missed it; MRB-103 caught it. **Working Scientifically is deliberately NOT a thread** — it is a
> separate axis, handled per §5.7 via `ws: []` tags.

Each lesson declares `threads: [{id, level}]` where level is `1 encounter` / `2 develop` /
`3 secure`. This expresses the spiral **without hard-coding years**: a school can reorder freely and
the thread structure still describes what is being built. It also drives a genuinely useful student
view — "everything you know about energy, in the order you met it".

**KS4 bridge.** Each lesson declares `ks4_links: [KS4 subtopic slugs]`. This is the on-ramp to the
site's existing strength. It gives KS3 a visible destination ("this becomes *States of matter* in
GCSE Chemistry"), gives Year 9 a real transition surface, and later enables KS4 pages to call back
("you met this in Year 8") without KS4 needing to know KS3's structure.

### 4.8 The lesson record — canonical field list

Authoritative. Fields not listed here do not exist without an amendment to this document.

```python
{
  # ---- identity -------------------------------------------------------
  "slug":            "particle-model",             # stable, kebab-case, unique within unit
  "title":           "The particle model",
  "discipline":      "chemistry",                  # biology | chemistry | physics
  "unit":            "particles-and-their-behaviour",
  "family":          "MODEL",                      # one of the seven, §6

  # ---- curriculum position -------------------------------------------
  "covers":          ["KS3.C.PNM.01", "KS3.C.PNM.02"],
  "touches":         ["KS3.P.PHYC.05"],
  "beyond_statutory": False,                       # ⊕ §7.6 — True ⇒ covers MUST be empty
                                                   #   and ks4_links MUST NOT be
  "threads":         [{"id": "particles", "level": 1}],
  "typical_year":    7,                            # ADVISORY ONLY — never routes (§4.5)
  "typical_minutes": 35,

  # ---- progression edges ---------------------------------------------
  "requires":        [],                           # hard prerequisites, lesson ids (§4.9)
  "assumes":         [],                           # softer knowledge deps, statement ids
  "references":      [],                           # cross-discipline reuse (§4.6)
  "ks4_links":       ["chemistry/bonding/states-of-matter"],

  # ---- the teaching payload ------------------------------------------
  "big_question":    "Why does a solid keep its shape but a liquid doesn't?",
  "phenomenon":      {...},                        # the opening hook, Law 1 (§5.1)
  "misconceptions":  [{"id", "statement", "confronted_by"}],   # required, §5.3
  "vocabulary":      [{"term", "definition", "note"}],          # required, §5.4
  "figures":         [{"id", "kind", "caption", "status"}],     # ⊕ §4.10, may be empty
  "core":            [...blocks...],               # every student
  "stretch":         [...blocks...],               # depth layer, §5.6
  "support":         [...blocks...],               # scaffold layer, §5.6
  "activities":      [...],                        # §5.5, families §6
  "ladder":          {...},                        # the four rungs, §5.8
  "key_note":        "...",                        # revision card, last

  # ---- working scientifically ----------------------------------------
  "ws":              ["analysis-and-evaluation"],  # §5.7

  # ---- governance ------------------------------------------------------
  "review_state":    "draft",                      # draft | examiner-reviewed | frozen (§5.10)
}
```

And the unit record that wraps them — one per module in `ks3_data/` (§8.3):

```python
UNIT = {
  "code":            "C1",
  "slug":            "particles-and-their-behaviour",
  "title":           "Particles and their behaviour",
  "discipline":      "chemistry",
  "statutory_area":  "The particulate nature of matter",
  "split_rationale": None,          # required if this unit is one of several from one strand (§4.3)
  "lessons":         [ ... ],       # lesson records, in default teaching order within the unit
}
```

### 4.9 How prerequisites are expressed

Prerequisites are **conceptual, not chronological**. They are a directed acyclic graph over lessons,
authored as edges on the dependent lesson.

- **`requires`** — hard edges. "You cannot understand this lesson without having understood that
  one." Use sparingly; a graph where everything requires everything is a graph with no information.
  Rule of thumb: 0–3 edges per lesson.
- **`assumes`** — soft edges to *statements*, not lessons. Knowledge the lesson leans on but could
  survive without.

**The graph must be acyclic.** A cycle is a build-blocking defect and the generator must fail on
one. ⊕

**What the graph is for** — four concrete uses, which is why it earns its authoring cost:

1. **Scheme-of-work validation.** When a school orders its KS3, the platform can warn: "You have
   placed *Photosynthesis* in week 4 but its prerequisite *Cells and organisation* in week 19."
   Warn, never block — the school may have taught it elsewhere.
2. **Student-facing prerequisites.** "Before this, make sure you're solid on …" with links.
3. **Recovery routes.** A student who fails the ladder is routed to the prerequisite that most
   plausibly explains the failure, not just told to reread.
4. **Safe reordering.** The graph, not the sequence, is the real structure — which is exactly what
   §4.5 requires.

Prerequisites may cross disciplines freely (Biology's *Breathing* requires Physics' *Pressure*) —
and the fact that the graph makes those crossings visible is one of its main benefits.

### 4.10 Figures and the diagram manifest ⊕

*Added 2026-07-26 (§11 conflict 1h, ruled ADOPT). This was a gap in this document that MRB-103
caught: the lesson record had nowhere to put a diagram, so a missing asset could only be discovered
at build time.*

Each lesson declares `figures: []`. A figure entry is:

```python
{"id":      "c1-particle-arrangement",   # stable, unique across KS3, permanent once referenced
 "kind":    "schematic",                 # schematic | graph | photo | apparatus
 "caption": "Particle arrangement in a solid, a liquid and a gas.",
 "status":  "needed"}                    # needed | drafted | final
```

- **`status` is the whole point.** A lesson may ship with figures at `needed` — it is not a build
  blocker — but the need is then **recorded and countable** rather than invisible.
- **Every entry appears in `docs/ks3/diagram-manifest.md`**, which is the sourcing worklist. The
  manifest is generated from the lesson data, so it cannot drift from what the lessons actually ask
  for.
- **`figures` may be empty**, and legitimately is for lessons carried entirely by interactives. Empty
  is a statement that none is needed, not an omission.

**Schematic, not photographic.** A Platform Backlog ticket already covers real-life photography
across all subjects. The KS3 diagram need is related but **distinct**: particle arrangements, ray
diagrams, circuit diagrams, field lines and labelled biological structures are *schematic* assets,
and a photograph does not substitute for one. The two sourcing efforts must not be merged — see the
manifest's own note.

---

## 5. How a KS3 lesson is composed

### 5.0 The ten laws

Every KS3 page is judged against these. A page that violates one is a defect, not a style choice.

**Law 1 — Phenomenon first.** ⊕
Every lesson opens with something *observed*, never something *defined*. A demonstration, a
photograph, a surprising result, a question about the everyday world. The definition arrives after
the student wants it. Novices have no reason to care about an abstraction they have not yet seen do
any work.

**Law 2 — The 90-word encode–act spine.**
Never more than ~90 words of continuous prose before the student must commit to something — a
prediction, a construction, a classification, a written answer. A lesson is a chain of encode→act
cycles ending in consolidation. (Bonding's 150 tightened for reading age and attention.) Any static
block whose content an interactive now teaches is deleted from the composition.

**Law 3 — Misconception-targeted.** ⊕
Every lesson names its target misconception(s) as structured data, and **at least one activity must
confront one head-on** — by eliciting it, making its wrongness visible, and replacing it. A lesson
with an empty `misconceptions` list must justify itself at review; almost none legitimately can.

**Law 4 — Predict before reveal.**
No interactive shows a verdict the student hasn't wagered on. Every stateful reveal is gated by a
committed prediction, and the reveal answers the prediction right/wrong in tone tokens. At KS3 this
is not just engagement: an unspoken wrong belief is invisible to its holder, and prediction is what
drags it into the open.

**Law 5 — Watch/do duality.**
A worked sequence is legitimate only when paired with a do-it-yourself counterpart producing the
same artifact. Neither ships alone.

**Law 6 — Concrete → representational → abstract.** ⊕
Within a lesson, ideas travel in that order: real phenomenon → model/diagram → symbol, word
equation, or formula. A lesson that opens at the abstract layer is a defect. A lesson that never
reaches the abstract layer has under-taught.

**Law 7 — Vocabulary is taught, not assumed.** ⊕
Technical terms are introduced explicitly, defined in student language, and recalled at least once
in the lesson. Body prose targets a reading age *below* chronological age; the technical terms are
the exception and get carried deliberately. KS3 science failure is very often a reading failure
wearing a science costume.

**Law 8 — Production-ending mastery ladder.**
Every lesson ends in the four-rung ladder (§5.8): recall → apply → explain → produce/transfer. With
per-question persistence and "retry my misses".

**Law 9 — Motion is meaning.**
Any transfer, movement or state change is animated as visible movement, never a frame swap.
Reduced-motion users get the instant swap.

**Law 10 — Every activity exercises the demand it claims.**
Name the intended cognitive demand first, then check the activity delivers it. The defect is an
activity whose surface features answer it. Every distractor encodes a named misconception and its
feedback corrects that specific misconception.

### 5.1 Anatomy of a lesson page

Block order is fixed at the ends and demand-driven in the middle — the same principle as bonding
Law 1.

#### 5.1.1 Segments are the vocabulary; families are the grammar ⊕

*Added 2026-07-26 — the ruled reconciliation of §11 conflict 1b. MRB-103 fixed the lesson as an
ordered deck of typed segments rendered as a stepper; this document made the middle demand-driven
and family-arranged. Neither wins outright.*

**The canonical block vocabulary** — adopted from MRB-103, and closed. A lesson is assembled from
these types and no others; a new type requires an amendment to this document.

| Segment | What it is |
|---|---|
| `hook` | The phenomenon. Law 1. Opens every lesson. |
| `explainer` | Body prose. Bounded by Law 2 (~90 words) and §5.2 (~450 total). |
| `figure` | A diagram or image, declared in `figures` (§4.10). |
| `worked-example` | A modelled sequence. Never ships without its `check` counterpart (Law 5). |
| `check` | A do-it-yourself counterpart producing the same artifact. |
| `keyword` | Vocabulary introduction or recall. Law 7. |
| `practical` | A hands-on or simulated investigation. |
| `misconception` | The confrontation activity. Law 3. Required. |
| `summary` | Consolidation. |
| `quiz` | The mastery ladder (§5.8) and micro-checks. |

**The grammar** — the seven families (§6) decide **which** segments a lesson uses, **how many**, and
**in what order** the middle runs. The families are unchanged.

**What this buys, and what each side gave up.** The renderer only ever has to know ten block types,
which is what made MRB-103's deck buildable — so the generator is finite and testable. But the
*lineup is not fixed*: a MODEL lesson and a PROCESS lesson draw different segments in a different
order, which is what keeps Law 1 and Law 10 alive and stops §6's warning ("two lessons with
identical block lineups should be a coincidence of need, never a default") from being violated by
construction.

**The stepper is a rendering choice, not the structure.** MRB-103's stepper may be used where a
family calls for a stepped sequence — PROCESS lessons especially — but it is not imposed on every
lesson. The order comes from the family; the stepper is one way to present it.

**Rule:** the fixed blocks below (1–3, n+1, n+2, n+3) are mandatory in every lesson and in this
order. Everything between them is drawn from the vocabulary above and arranged by the family.

| # | Block | Fixed? | Notes |
|---|---|---|---|
| 1 | **Big question** | Fixed | One sentence. The idea of the lesson, as a question. |
| 2 | **Phenomenon hook** | Fixed | Law 1. Visual or interactive. Ends in a commitment. |
| 3 | **First prediction** | Fixed | Within the first ~90 words. Law 2, Law 4. |
| 4–n | **Encode→act cycles** | **Demand-driven** | Arrangement set by the family (§6). Instruments at demand peaks, not parked at the top. |
| — | *Misconception confrontation* | Fixed *that* it appears, free *where* | Law 3. Placed at the moment the error is born. |
| — | *Vocabulary check* | Fixed *that*, free *where* | Law 7. |
| n+1 | **Mastery ladder** | Fixed | §5.8. Four rungs. |
| n+2 | **Key note** | Fixed | Photographable revision card. Static, last. |
| n+3 | **End matter** | Fixed | Score + delta, AI tutor, prev/next. Identical ritual to KS4. |

Interactive budget per lesson: **one flagship, one mid-size, micro-widgets ad lib**, plus the
ladder. (Lower than bonding's ceiling — shorter page, younger learner.)

### 5.2 The prose budget

~90 words of continuous prose maximum before a commitment. Whole-lesson body prose target: **under
450 words**, excluding activity copy, ladder questions and the key note. If a lesson needs more than
that to make its point, the point is two lessons.

### 5.3 The misconception register ⊕

Misconceptions are structured data, not prose asides, and they are **cross-referenced across the
whole key stage** in a companion file `docs/ks3/misconception-register.md`.

```python
{"id": "PART-03",
 "statement": "The particles themselves get bigger when a substance is heated.",
 "elicited_by": "predict-expansion",     # the activity that surfaces it
 "confronted_by": "expansion-lab",       # the activity that kills it
 "reappears_in": ["thermal-expansion", "gas-pressure", "density"]}
```

**Why a register rather than per-lesson prose:** the same wrong belief resurfaces across years and
disciplines. A register lets a later lesson say "this is the same wrong idea you met in Year 7" and
lets us check we are actually killing misconceptions rather than dodging them in twelve places.
It also gives the AI tutor something precise to work with.

Every distractor in every ladder question and quiz should map to a register entry or be a
non-diagnostic distractor by explicit choice.

### 5.4 Vocabulary and reading ⊕

Each lesson carries `vocabulary: [{term, definition, note}]`:

- **`definition`** — student-facing, plain, one sentence, no undefined technical terms inside it.
- **`note`** — optional: etymology, a near-miss word it's confused with, or a false friend
  ("*mass* is not *weight*"). Etymology is disproportionately effective at this age
  (*photo*-light, *synthesis*-making).

Rendering: terms are visibly marked on first use with a tap/hover definition, and the lesson
includes at least one vocabulary recall mechanic. Target body-prose reading age is below
chronological age; **technical vocabulary is the deliberate exception**, not something to write
around. We are teaching students to read science, not protecting them from it.

### 5.5 Activities

Same commit-and-reveal discipline as bonding. Micro-widgets weave into prose; mid-size activities
sit at demand peaks; the flagship carries the lesson's central idea.

Every activity record names its intended demand (`demand: recall | apply | explain | classify |
construct | investigate`), which is what Law 10 is checked against.

### 5.6 Depth layers: support / core / stretch ⊕ — the replacement for tier

KS3 has no tier and must not grow one. But KS3 classes are enormously mixed. The answer is a
different axis:

| Layer | Who sees it | Nature |
|---|---|---|
| **core** | Every student, always | The lesson. Non-optional, non-hidden. |
| **stretch** | Anyone who wants it | Depth and challenge. **Visible and opt-in to all** — never allocated by the teacher, never gated by prior attainment. |
| **support** | Anyone who wants it | Scaffolding on demand: worked example, sentence starters, vocabulary pre-teach, a simpler parallel question. Available in-place, never a separate lesser route. |

**Why this is not tier in disguise.** Tier is a syllabus split decided *for* a student in advance,
and it caps what they can be examined on. Layers are decided *by* the student, in the moment, per
lesson, and cap nothing. No student is ever routed away from core. Nothing is ever hidden because of
who the system thinks they are.

Support and stretch are **optional at authoring time** — core alone is a shippable lesson.

> **Ruled 2026-07-26 (§11 decision 4, now closed).** At launch, lessons are authored `core` +
> `stretch`; **`support` content is deferred, but the `support` slot is designed in from day one** and
> must be present (and schema-valid) on every lesson, even when empty. "Optional at authoring time"
> means *may be empty*, never *may be absent* — an absent slot is what forces a re-author later.

### 5.7 Working Scientifically ⊕

The statutory document is explicit that WS is taught *through* content. So:

1. **Every lesson may tag `ws: []`** with the strands it exercises — `scientific-attitudes`,
   `experimental-skills`, `analysis-and-evaluation`, `measurement`.
2. **Every unit must contain at least one genuine WS moment** — an activity where the WS skill is
   the thing being learned, not incidental.
3. **A small number of lessons are WS-primary** — family `INVESTIGATION` (§6), where the subject
   *is* variables, or graphing, or error. These live inside host units, never in a WS unit of their
   own, and are listed in §7.
4. WS coverage is auditable the same way statutory coverage is.

#### 5.7.1 RULE — an INVESTIGATION lesson anchors `covers` on the WS statement it teaches ⊕

**Every `INVESTIGATION` lesson declares `covers: []` as one or more `KS3.WS.*` statements — the
Working Scientifically statement the lesson actually teaches — and declares no subject statement it
does not genuinely own.** This is the general rule for all 18 of them (§7.5), not a per-lesson
judgement call.

Why the rule is needed. A WS-primary lesson teaches no new subject content by design: `Testing the
model` (C1 L6) tests the particle model built across L1–L5, and `Mendeleev` (C8) teaches how a
prediction earns trust. Yet §10.2 requires `covers` non-empty, and §4.4 requires exactly-once
ownership of subject statements. Without this rule the author has two bad options — invent a subject
statement the lesson does not teach, and break exactly-once ownership by duplicating a statement
another lesson already owns; or leave `covers` empty and fail the done-list.

Why anchoring on WS is the right answer rather than a loophole:

- It is **honest**. `Testing the model` covers `KS3.WS.ATT.02` — *theories develop as earlier
  explanations are modified to take account of new evidence* — because that is precisely and only
  what the lesson does.
- It is **legal**. WS statements are exempt from the exactly-once ownership rule (§5.7 above, and
  the note in `ks3_statutory.py`), because WS is taught *through* content and many lessons tap the
  same strand via `ws: []`.
- It keeps the **audit meaningful**. Subject coverage stays a true partition — every subject
  statement owned once, by the lesson that teaches it — and WS coverage becomes auditable at
  statement grain on exactly the lessons where WS *is* the content.

How to apply it, per INVESTIGATION lesson:

1. Name the WS statement the lesson teaches, at statement grain, and put it in `covers`.
2. Keep the broader `ws: []` strand tags as well — `covers` is the statement this lesson is
   *responsible for*; `ws` is every strand it *exercises*. They answer different questions.
3. Add a subject statement to `covers` only if the lesson genuinely owns it and no other lesson
   does. A WS-primary lesson usually owns none.
4. `covers` must still resolve against `statutory-register.md` (§10.2) — a WS ID is a real
   registered ID, so this check is unchanged.

*Provenance: discovered by the C1 vertical slice (§9) on `testing-the-model` and ruled 26 Jul 2026.
Recorded here as a rule so all 18 INVESTIGATION lessons follow one pattern rather than each author
re-deciding. This is the kind of finding §9 says the slice exists to produce.*

### 5.8 The mastery ladder — KS4's exam ladder, retuned

Four rungs, always, at the end of every lesson:

| Rung | Demand | KS3 form |
|---|---|---|
| ① | **Recall** | Retrieval and vocabulary. Fast, confidence-building, genuinely required. |
| ② | **Apply** | Use the idea on a new case; calculate; deduce. |
| ③ | **Explain** | Chain assembly — build a causal explanation from parts. The KS3 version of the 6-marker skill, without the tariff. |
| ④ | **Produce / transfer** | Write-then-self-mark against a plain-English success list; or predict a genuinely new situation; or design an investigation. |

**Why production still tops the ladder with no exam to pay for it:** writing a causal explanation is
the hardest and most transferable thing a KS3 scientist does, and it is precisely what KS4 will
demand. Rung ③ and ④ are where KS3 earns its keep.

Rung ④ marking is **plain-English success criteria**, not mark schemes — "did you say the particles
move faster? did you say they spread out?" — because there is no board to award marks and pretending
otherwise teaches a false model of assessment.

Persistence, "retry my misses", score + delta vs best: inherited unchanged. Never punish: no
streaks, no guilt copy, no XP, opt-in timers only. Low scores get a diagnosis and a route — and with
the prerequisite graph (§4.9), the route can be a real lesson rather than "try again".

### 5.9 The AI tutor at KS3

Same engine, different register. The tutor must know it is talking to an 11–14 year old and must be
told the lesson's misconceptions so it can recognise and correct them rather than validate them.
Concretely: KS3 pages pass a KS3 system prompt with the lesson's `big_question`, `vocabulary`,
`misconceptions` and `covers`; the FIFA method carries over wherever a calculation appears; the
Higher ⭐ / Triple 🔬 labelling has no meaning at KS3 and must not appear.

### 5.10 Science review and the freeze ⊕

KS4's eight frozen fields exist because examiner-approved content must not drift. KS3 needs the same
discipline over different fields.

**Science-bearing fields** — `big_question`, `vocabulary[].definition`, `misconceptions[].statement`,
all `core`/`stretch`/`support` explanation text, all ladder questions, answers and success criteria,
`key_note`.

- These require **Mide's examiner review** before publish. Science accuracy is his sole gate.
- Once reviewed, they are **frozen**: `review_state: frozen`. Interactives are built *from* frozen
  science.
- Any net-new science introduced while building an activity is flagged **⚑** for review, never
  quietly shipped.
- Non-science copy (button labels, encouragement, layout) is freely editable.

`review_state` transitions: `draft` → `examiner-reviewed` → `frozen`. Only frozen lessons publish —
**except during the pre-launch carve-out below.**

#### 5.10.1 CARVE-OUT — draft lessons may publish before real students return ⊕

**For the pre-launch period only, a lesson with `review_state: draft` MAY publish, provided the page
carries a visible marker saying the content is under review.**

Why. Right now the site has no real students on it — it is the summer break, and the only accounts
are test users Mide placed himself. The frozen-only rule exists to protect students from unreviewed
science; with no students to protect, it protects nothing and costs a great deal. Holding the whole
KS3 build behind a review queue would mean nothing is visible to review *in situ*, nothing can be
smoke-tested on a real device, and the review itself gets harder because Mide has to read data files
instead of pages. Publishing drafts makes the work reviewable. That is the entire justification, and
it evaporates the moment a student can land on the page.

The marker is mandatory, not advisory. A draft lesson renders
`<p class="ks3-review-flag">Draft — not yet science-reviewed.</p>` in the lesson header — emitted by
`build_ks3.py` for any lesson whose `review_state` is not `frozen`, and styled to be legible rather
than decorative. A draft page with no marker is a defect, not a draft.

What the carve-out does NOT change:

- **Mide is still the sole science gate.** Publishing a draft is not approval and never counts as it.
  `draft` → `examiner-reviewed` → `frozen` runs exactly as before.
- **Net-new science is still flagged ⚑** for review rather than quietly shipped.
- **The done-list (§10.2) still applies in full.** A draft lesson meets every automatable gate; the
  carve-out is about the science review, not about build quality.

**EXPIRY — this carve-out is time-limited and the limit is explicit.**

> **It expires when real students return: the first day of the autumn term, 1 September 2026.**
> On that date the frozen-only rule in §5.10 resumes with no further amendment needed, and any lesson
> still at `review_state: draft` must stop publishing — it reverts to a "coming soon" slot until it
> is frozen. Nothing about this carve-out survives the date. If the build is not ready by then, the
> answer is to freeze the reviewed lessons and hide the rest, **not** to extend the carve-out
> silently — extending it requires an explicit amendment logged in §12 with Mide's decision on the
> record.

*The 1 September 2026 date is the stated assumption for "real students return"; if Mide opens the
site to students earlier, the carve-out expires on that earlier date instead — the trigger is the
first real student, and the date is only the backstop.*

---

## 6. The seven architecture families

Each lesson belongs to exactly one family. The family fixes the lesson's skeletal rhythm; the
component catalogue fills in the instruments. Bonding's five are retuned and extended to two more,
because KS3 spans biological systems and investigation lessons that KS4 chemistry never had to
model.

**MODEL — "one idea explains a whole class of behaviour"**
*e.g. the particle model, the ray model, magnetic fields, the atom.*
Lead → flagship parameter instrument with predict-gates at each regime change → property blocks each
anchored back to the model → ladder. The model instrument is the centre of gravity; prose orbits it.

**PROCESS — "a mechanism unfolds in steps"**
*e.g. photosynthesis, digestion, the rock cycle, the menstrual cycle, breathing.*
Lead → worked stepper with predict-gates → do-mode construction of the same sequence → what follows
from the mechanism → ladder. The static block that narrates what the stepper shows is deleted.

**SYSTEM — "parts working together, and what happens when one fails"** ⊕
*e.g. the digestive system, gas exchange, circuits, ecosystems, the skeleton.*
KS4 chemistry never needed this; KS3 biology and electricity are full of it. Lead → the system
assembled part-by-part, each part earning its place → **perturbation as the flagship**: break or
change one part, predict the knock-on, reveal → ladder. The characteristic KS3 error is knowing the
parts and not the interaction, so the flagship must be perturbation, never labelling.

**CONTRAST — "two things, one discriminating difference"**
*e.g. mass vs weight, chemical vs physical change, series vs parallel, aerobic vs anaerobic.*
Lead → predict-gated A/B instrument → parallel compare-cards as static reference → explanation-chain
builders forcing the *linked* comparison → ladder. Contrast lessons carry the heaviest rung ③.

**CLASSIFY — "decide which category, fast, and know why"**
*e.g. acid/alkali, element/compound/mixture, metal/non-metal, living/non-living.*
Lead → decision instrument (commit a prediction, watch resolution) → the reference table →
classification drills at rising stakes → ladder. Ends with the rule stated in the student's words.

**QUANTITATIVE — "a calculation carries the concept"**
*e.g. speed, pressure = F/A, energy cost, density, food energy.*
Lead → the phenomenon behind the number → concept-calculation pair: a simulation feeding directly
into FIFA worked/practice (Law 5) → ladder with production. FIFA follows the sim immediately.
Units and their meaning are content, not formatting.

**INVESTIGATION — "the science skill is the subject"** ⊕
*e.g. variables and fair testing, measuring and uncertainty, tables and graphs, evaluating error,
sampling.*
Lead with a flawed or ambiguous investigation → **critique before construct**: judge someone else's
method, then build your own → run it in simulation, get messy data → analyse and evaluate → ladder
ending in a designed investigation. These lessons live inside host content units (§5.7).

**Family assignment is a design decision recorded per lesson in §7.** Two lessons with identical
block lineups should be a coincidence of need, never a default.

> **Amended 2026-07-26 (§11 conflict 1b, ruled).** The families are the **grammar**; the ten typed
> segments in §5.1.1 are the **vocabulary**. A family does not invent block types — it draws from the
> closed list and decides which, how many, and in what order. Read each family description above as
> a sentence written in that vocabulary: MODEL's "flagship parameter instrument with predict-gates"
> is `hook → explainer → practical → check → …`; PROCESS's "worked stepper then do-mode
> construction" is `worked-example → check`, which is Law 5 expressed as grammar. This is what makes
> the renderer finite while keeping the arrangement demand-driven.

---

## 7. The proposed topic map

Derived from the 2014 statutory programme of study, normalised to Discipline → Unit → Lesson.

> ✅ **Amended 2026-07-26 (second amendment — the first is REVERSED).** The `Y` column below **is
> "MrBadmusAI default sequence v1"**, and it ships in `ks3_data/default_sequence.py`.
>
> This reverses the amendment made earlier the same day, which had demoted this column to an
> advisory fallback and promoted MRB-103's locked Rainford year map to the published default. **Mide
> reversed that ruling** — see §11 decision 5 and conflict 1d, both of which now carry the reversal
> and its reasoning. **Rainford's map is reference evidence, never a template**; it now lives in
> `ks3_data/school_schemes.py` as one school's configured sequence (§8.9).
>
> The column earns the default because it was **derived from the statutory spine and the
> prerequisite graph**, not from one school's timetable. There is no "fallback" layer any more —
> the default and this column are the same object, asserted equal at import.

**How to read this.** `Y` = `typical_year`, the published default and still **data, never structure**
(§4.5) — it is what a school with no scheme configured gets, and any school may override it with a
data change. `F` = architecture family. Lesson counts are
indicative; the authoring team may merge or split within a unit provided statutory coverage stays
exactly-once (§4.4). Units marked **⇄** contain a lesson owned by another discipline (§4.6).

**Totals: 33 units, 185 lessons** (Biology 11/60, Chemistry 10/55, Physics 12/70).

**As a default sequence, that distributes as:**

| Year | Units | Lessons |
|---|---|---|
| Y7 | 9 | 55 |
| Y8 | 13 | 79 |
| Y9 | 11 | 51 |

Year 8 is the heavy year and that is stated rather than shaded — it carries four of the five
physics units a school would rather not meet in Year 7. A school that finds it heavy moves a unit,
which is a data change (§4.5). What matters for a *default* is that all three years are teachable
years; the map this replaced offered Year 9 three lessons.

That is a large authoring commitment — larger than anything attempted at KS4 so far — and it is
stated honestly rather than shaded down. Across three years and three sciences it works out at
roughly 60 lessons per year group, against the 100–120 science lessons a typical school actually
teaches per year, so it is a lean curriculum, not a bloated one. It is nonetheless the single
biggest number in this document and it drives the build-order question in §11 decision 8.

### 7.1 Biology — 11 units, 60 lessons

| Unit | Statutory area | Y | Lessons |
|---|---|---|---|
| **B1 Cells and organisation** | Structure and function of living organisms | 7 | Life processes and what living things are made of *(CLASSIFY)* · Using a microscope *(INVESTIGATION)* · Animal and plant cells *(MODEL)* · Specialised cells *(SYSTEM)* · Levels of organisation *(SYSTEM)* · Unicellular organisms *(CONTRAST)* · Stem cells and meristems *(PROCESS)* · Enzymes and what changes their rate *(MODEL)* |
| **B2 Movement: skeleton and muscles** | Structure and function | 7 | What the skeleton does *(SYSTEM)* · Joints *(MODEL)* · Antagonistic muscle pairs *(SYSTEM)* · Biomechanics: forces in the body *(QUANTITATIVE)* ⇄ *requires P4 Forces* |
| **B3 Nutrition and digestion** | Structure and function | 7 | A balanced diet *(CLASSIFY)* · Food tests *(INVESTIGATION)* · Energy in food and what you need *(QUANTITATIVE)* ⇄ *shares statements with P2* · When diet goes wrong *(CONTRAST)* · The digestive system *(SYSTEM)* · Enzymes in digestion *(PROCESS)* · Absorption and the small intestine *(MODEL)* · Bacteria in the gut *(SYSTEM)* |
| **B4 Breathing and gas exchange** | Structure and function | 8 | The gas exchange system *(SYSTEM)* · How breathing works *(MODEL)* ⇄ *requires P5 Pressure* · Alveoli: built for exchange *(MODEL)* · Exercise, asthma and smoking *(SYSTEM)* · Stomata and gas exchange in plants *(CONTRAST)* |
| **B5 Reproduction** | Structure and function | 8 | Human reproductive systems *(SYSTEM)* · Gametes and fertilisation *(PROCESS)* · The menstrual cycle *(PROCESS)* · Gestation, the placenta and birth *(PROCESS)* · Lifestyle and the developing foetus *(SYSTEM)* · Flowers and pollination *(SYSTEM)* · Fertilisation, seeds and fruit *(PROCESS)* · Seed dispersal *(CLASSIFY)* |
| **B6 Health and drugs** | Structure and function → Health | 9 | What drugs do to the body *(SYSTEM)* · Alcohol and smoking *(SYSTEM)* · Substance misuse and decisions *(INVESTIGATION — evaluating claims and evidence)* |
| **B7 Photosynthesis** | Material cycles and energy | 8 | The photosynthesis reaction *(PROCESS)* · Leaves built for the job *(MODEL)* · Testing a leaf for starch *(INVESTIGATION)* · Why almost all life depends on it *(SYSTEM)* |
| **B8 Respiration** | Material cycles and energy | 8 | Aerobic respiration *(PROCESS)* · Why every cell respires *(SYSTEM)* · Anaerobic respiration in humans *(PROCESS)* · Fermentation and what we use it for *(PROCESS)* · Aerobic vs anaerobic *(CONTRAST)* |
| **B9 Ecosystems and interdependence** | Interactions and interdependencies | 9 | Food chains and food webs *(SYSTEM)* · Predator and prey *(MODEL)* · Disturbing a food web *(SYSTEM)* · Pollinators and food security *(SYSTEM)* · Toxic build-up in a food chain *(PROCESS)* · Sampling an ecosystem *(INVESTIGATION)* |
| **B10 Inheritance and DNA** | Genetics and evolution | 9 | Variation: continuous and discontinuous *(INVESTIGATION — data and graphs)* · Chromosomes, genes and DNA *(MODEL)* · How we worked out DNA's structure *(INVESTIGATION — nature of science)* · Passing it on: heredity *(PROCESS)* · What makes a species *(CLASSIFY)* |
| **B11 Evolution, extinction and biodiversity** | Genetics and evolution | 9 | Variation and competitive success *(SYSTEM)* · Natural selection *(PROCESS)* · When the environment changes: extinction *(SYSTEM)* · Biodiversity and gene banks *(SYSTEM)* |

*B10/B11 split from one statutory heading — `split_rationale`: inheritance mechanism and evolutionary
consequence are separately assessable ideas and are almost universally taught apart.*

### 7.2 Chemistry — 10 units, 55 lessons

| Unit | Statutory area | Y | Lessons |
|---|---|---|---|
| **C1 Particles and their behaviour** | The particulate nature of matter | 7 | The particle model *(MODEL)* · Solids, liquids and gases *(CONTRAST)* · Changes of state *(PROCESS)* · Gas pressure *(MODEL)* · Diffusion *(MODEL)* · Testing the model: does it explain everything? *(INVESTIGATION)* |
| **C2 Atoms, elements and compounds** | Atoms, elements and compounds | 7 | The atom: Dalton's model *(MODEL)* · Elements *(CLASSIFY)* · Compounds *(CONTRAST)* · Chemical symbols *(CLASSIFY)* · Formulae *(MODEL)* · Conservation of mass *(QUANTITATIVE)* |
| **C3 Mixtures and separation** | Pure and impure substances | 7 | Pure or mixture? *(CLASSIFY)* · Dissolving and solutions *(MODEL)* · Filtration *(PROCESS)* · Evaporation and crystallisation *(PROCESS)* · Distillation *(PROCESS)* · Chromatography *(PROCESS)* · Proving something is pure *(INVESTIGATION)* |
| **C4 Chemical reactions** | Chemical reactions | 8 | Chemical change vs physical change *(CONTRAST)* ⇄ *shares statements with P11* · Reactions rearrange atoms *(MODEL)* · Word equations *(MODEL)* · Mass in a reaction *(QUANTITATIVE)* · Symbol equations and balancing *(MODEL — stretch-heavy)* |
| **C5 Types of reaction** | Chemical reactions | 8 | Combustion *(PROCESS)* · Thermal decomposition *(PROCESS)* · Oxidation *(PROCESS)* · Displacement *(PROCESS)* · Which reaction is this? *(CLASSIFY)* |
| **C6 Acids and alkalis** | Chemical reactions | 8 | Acids and alkalis *(CLASSIFY)* · The pH scale and indicators *(MODEL)* · Neutralisation *(PROCESS)* · Acid + metal *(PROCESS)* · Acid + alkali: making a salt *(PROCESS)* · Making a pure dry salt *(INVESTIGATION)* · Catalysts *(MODEL)* |
| **C7 Energy changes in reactions** | Energetics | 9 | Energy and changes of state *(MODEL)* ⇄ *requires C1* · Exothermic reactions *(PROCESS)* · Endothermic reactions *(CONTRAST)* · Measuring a temperature change *(INVESTIGATION)* |
| **C8 The periodic table** | The periodic table | 8 | Metals and non-metals *(CONTRAST)* · Mendeleev and the table that predicted *(INVESTIGATION — nature of science)* · Groups and periods *(MODEL)* · Patterns you can predict: Groups 1, 7 and 0 *(MODEL)* · Metal and non-metal oxides *(CONTRAST)* |
| **C9 Metals and materials** | Materials | 9 | The reactivity series *(CLASSIFY)* · Predicting displacement *(MODEL)* · Getting metals out of rocks *(PROCESS)* · Ceramics, polymers and composites *(CONTRAST)* |
| **C10 The Earth and its atmosphere** | Earth and atmosphere | 9 | Inside the Earth *(MODEL)* · Three ways to make a rock *(CLASSIFY)* · The rock cycle *(PROCESS)* · A planet with limits: resources and recycling *(SYSTEM)* · What's in the air *(MODEL)* · Carbon dioxide, humans and climate *(SYSTEM)* |

*C4/C5/C6 split from one statutory heading — `split_rationale`: eight statutory bullets spanning
representation, reaction types and acid chemistry; universally taught as separate units and too
large to schedule as one.*

### 7.3 Physics — 12 units, 70 lessons

| Unit | Statutory area | Y | Lessons |
|---|---|---|---|
| **P1 Energy transfers** | Energy | 8 | Energy stores *(CLASSIFY)* · Energy transfers: before and after *(MODEL)* · Conservation of energy *(MODEL)* · Heating and thermal equilibrium *(MODEL)* · Conduction *(PROCESS)* · Radiation *(PROCESS)* · Keeping energy in: insulation *(INVESTIGATION)* · Simple machines: force for distance *(QUANTITATIVE)* |
| **P2 Energy at home** | Energy | 9 | Energy in food *(QUANTITATIVE)* ⇄ *shares statements with B3* · Power ratings in watts *(QUANTITATIVE)* · Calculating energy transferred *(QUANTITATIVE)* · Reading a fuel bill *(QUANTITATIVE)* · Fuels and energy resources *(CLASSIFY)* |
| **P3 Describing motion** | Motion and forces | 7 | Speed *(QUANTITATIVE)* · Distance–time graphs *(INVESTIGATION)* · Relative motion *(MODEL)* |
| **P4 Forces** | Motion and forces | 7 | What a force is *(MODEL)* · Drawing and adding forces *(MODEL)* · Balanced and unbalanced *(CONTRAST)* · What forces do to motion *(MODEL)* · Friction *(PROCESS)* · Air and water resistance *(SYSTEM)* · Moments: the turning effect *(QUANTITATIVE)* · Springs and Hooke's law *(INVESTIGATION)* · Non-contact forces *(CLASSIFY)* |
| **P5 Pressure** | Motion and forces | 8 | Pressure = force ÷ area *(QUANTITATIVE)* · Pressure in liquids *(MODEL)* · Upthrust, floating and sinking *(MODEL)* · Atmospheric pressure *(SYSTEM)* |
| **P6 Waves and sound** | Waves | 8 | Waves on water: what a wave is *(MODEL)* · Transverse waves, reflection and superposition *(MODEL)* · How sound is made *(PROCESS)* · Sound is longitudinal *(CONTRAST)* · Frequency, pitch and loudness *(QUANTITATIVE)* · Sound needs a medium *(INVESTIGATION)* · Echoes, reflection and absorption *(PROCESS)* · Hearing and auditory range *(SYSTEM)* · Ultrasound at work *(SYSTEM)* |
| **P7 Light** | Waves | 8 | Light travels *(MODEL)* · Reflection: mirrors and scattering *(MODEL)* · Refraction *(PROCESS)* · Lenses and images *(MODEL)* · The eye and the camera *(SYSTEM)* · Colour and the spectrum *(MODEL)* · Why things look coloured *(CONTRAST)* |
| **P8 Electric circuits** | Electricity and electromagnetism | 8 | Current and circuits *(MODEL)* · Series and parallel *(CONTRAST)* · Current at a junction *(SYSTEM)* · Potential difference *(MODEL)* · Resistance *(QUANTITATIVE)* · Conductors and insulators *(CLASSIFY)* · Building and measuring a circuit *(INVESTIGATION)* |
| **P9 Static electricity** | Electricity and electromagnetism | 9 | Charging by rubbing *(PROCESS)* · Forces between charges *(MODEL)* · Electric fields *(MODEL)* |
| **P10 Magnetism and electromagnetism** | Electricity and electromagnetism | 9 | Magnets and poles *(CONTRAST)* · Magnetic fields *(INVESTIGATION)* · The Earth is a magnet *(SYSTEM)* · Electromagnets *(MODEL)* · How a motor works *(SYSTEM)* |
| **P11 Matter and the particle model** ⇄ | Matter | 7 | Density *(QUANTITATIVE)* · Brownian motion *(MODEL)* · Temperature, particle motion and internal energy *(MODEL)* · Why ice floats *(CONTRAST)* · *references C1 (particle model, changes of state, diffusion) and C4 (chemical vs physical change)* |
| **P12 Space** | Space physics | 9 | Gravity and weight *(QUANTITATIVE)* · Mass vs weight *(CONTRAST)* · Gravity between Earth, Moon and Sun *(MODEL)* · The Sun, stars and galaxies *(SYSTEM)* · Seasons and the tilt *(MODEL)* · How far is a light year? *(QUANTITATIVE)* |

*P11 is a **referencing unit**: it owns four lessons of its own and pulls the rest of its statutory
coverage from Chemistry C1 under the single-source rule (§4.6). It is the first real test of that
rule, which is why §10.1 schedules it as the opening physics unit.*

### 7.4 Cross-discipline ownership decisions (fixed)

| Idea | Owner | Referenced by |
|---|---|---|
| Particle model, states, changes of state, diffusion | **Chemistry C1** | Physics P11, Biology B3/B4 |
| Density, Brownian motion, internal energy, ice anomaly | **Physics P11** | Chemistry C1 |
| Chemical vs physical change | **Chemistry C4** | Physics P11 |
| Energy in food, energy calculations | **Physics P2** | Biology B3 |
| Pressure | **Physics P5** | Biology B4 (breathing) |
| Forces | **Physics P4** | Biology B2 (biomechanics) |

### 7.5 Working Scientifically distribution

WS-primary (`INVESTIGATION`) lessons are distributed so every year meets every WS strand. **There
are 18**, and each one anchors its `covers` on a WS statement per the rule in §5.7.1:
`Using a microscope` (B1) · `Food tests` (B3) · `Substance misuse and decisions` (B6) ·
`Testing a leaf for starch` (B7) · `Sampling an ecosystem` (B9) ·
`Variation: continuous and discontinuous` (B10) · `How we worked out DNA` (B10) ·
`Testing the model` (C1) · `Proving something is pure` (C3) · `Making a pure dry salt` (C6) ·
`Measuring a temperature change` (C7) · `Mendeleev` (C8) · `Insulation` (P1) ·
`Distance–time graphs` (P3) · `Springs and Hooke's law` (P4) · `Sound needs a medium` (P6) ·
`Building and measuring a circuit` (P8) · `Magnetic fields` (P10).

Coverage of the four WS strands is auditable per year and per discipline once `ws` tags are authored.

*Count corrected 26 Jul 2026: this list said 17 and omitted `Substance misuse and decisions` (B6),
which `ks3_data/structure.py` has carried as `INVESTIGATION` since Phase 1. The structure data was
right; the prose was one short.*

### 7.6 The Year 9 GCSE-bridge unit group ⊕ — design only, not yet authored

*Added 2026-07-26 on Mide's instruction, alongside the default-sequence reversal. This settles the
Phase 3 question left open by §11 conflict 1g — **whether** Year 9 gets a bridge group, and **what
is in it**. Authoring stays deferred; nothing here is in `ks3_data/structure.py`, and the 185-lesson
scope of §7 is unchanged by it.*

**The problem the default has to solve.** A published default sequence has to serve two real shapes
of school, and they want opposite things from Year 9:

| Shape | What the school does | What Year 9 needs from us |
|---|---|---|
| **A — full KS3** | Teaches KS3 across Years 7, 8 and 9, starts GCSE in Year 10. | The **remaining statutory content**: the 11 units and 51 lessons §7 places in Y9. |
| **B — early GCSE** | Starts GCSE in Year 9. Very common, and the reason Rainford's Y9 looked short. | An explicit **bridge set** — deliberate KS4-facing content that gets a KS3 student ready for a GCSE course starting now. |

Shape A is served by the default as published, with no extra work. Shape B is served by this unit
group. **Neither is the "real" default** — the default sequence covers Shape A because that is what
the statutory programme of study describes, and the bridge group is what a Shape-B school swaps in.

#### The exemption shape

Bridge lessons teach **nothing in the KS3 programme of study**, and the architecture must say so
loudly rather than let them leak into the coverage numbers. They take the same shape as the
Working Scientifically exemption ruled at decision 6 — *the rule is not quietly relaxed; the
exemption is declared, named, and countable*:

1. **Every bridge unit and every bridge lesson carries `beyond_statutory: True`.** No lesson is
   beyond-statutory by omission; it is beyond-statutory by declaration.
2. **`covers` MUST be empty.** Not "may be" — a bridge lesson that declares a `covers` entry is a
   **build failure**, not a warning. This is the operative half of conflict 1g's standing
   prohibition: *bridge content must never enter through the coverage register.*
3. **`ks4_links` MUST be non-empty.** The inverse gate, and the one that makes a bridge a bridge. A
   beyond-statutory lesson pointing nowhere is just off-spec content. `check_ks4_links()` already
   exists and already fails the build on an unresolvable edge — bridge lessons get it as a
   requirement rather than a courtesy.
4. **They never appear in `docs/ks3/statutory-register.md`.** Exactly-once (§4.4) is computed over
   statutory lessons only and is untouched by their existence.
5. **They are counted where they can be seen** — `docs/ks3/bridge-register.md`, generated from the
   lesson data exactly as the diagram manifest is (§4.10), so the beyond-statutory surface is a
   number anyone can read rather than something you have to grep for. *It does not exist yet and
   should not be created empty; it lands with the first authored bridge lesson.*

`typical_year: 9` on a bridge lesson is advisory in the ordinary way (§4.5). Its URL is
`/ks3/<discipline>/gcse-bridge-…/` — the path says bridge, because a teacher landing on one from a
search result must know immediately that it is not KS3 curriculum.

#### The proposed set — 3 units, 15 lessons

Three units, one per discipline, sized as an autumn term. MRB-103's four candidates are all in it
and are marked ⓶. The remaining eleven are proposed here: each is a KS4 idea that (a) sits directly
on a KS3 lesson already in §7, and (b) is a place students demonstrably stall on entry to GCSE.

**XB1 — *GCSE bridge: from cells to organisms*** (Biology, `gcse-bridge-organisms`)

| Lesson | F | Why it bridges | `ks4_links` target |
|---|---|---|---|
| The circulatory system ⓶ | SYSTEM | The organ system KS3 never teaches, and every GCSE organisation topic assumes. | the heart · blood vessels |
| Blood and what it carries | CLASSIFY | Follows directly; four components, one lesson. | blood |
| Exchange surfaces: surface area and volume | QUANTITATIVE | The single most common GCSE Biology stumble. Sits on B4 *Alveoli: built for exchange* and B1 *Animal and plant cells*, and asks for a ratio KS3 never asks for. | exchange surfaces |
| Enzymes: lock and key, and what denatures them | MODEL | B1 teaches enzyme rate descriptively; GCSE wants the model and the pH/temperature curve. | enzymes |
| Communicable disease and the immune response | SYSTEM | Sits on B6 *Health and drugs*, which is the one Y9 unit both shapes keep. | communicable diseases |

**XC1 — *GCSE bridge: atoms, bonding and rates*** (Chemistry, `gcse-bridge-atoms-and-rates`)

| Lesson | F | Why it bridges | `ks4_links` target |
|---|---|---|---|
| Inside the atom: the nuclear model | MODEL | **The biggest single KS3→KS4 chemistry step.** C2 stops at Dalton's indivisible sphere; GCSE opens on protons, neutrons and electrons. | the atom |
| Electron shells, and why the groups behave as they do | MODEL | C8 gives the group patterns descriptively; this supplies the explanation underneath them. | electronic structure |
| Ionic and covalent bonding: a first look | CONTRAST | **The strongest `ks4_links` in the set** — the bonding v2 pages already exist and are the platform's best content. | ionic bonding · covalent bonding |
| Collision theory | MODEL | The explanatory half of rate, and it sits squarely on C1's particle model — the bridge closes the loop the vertical slice opened. | collision theory |
| Rate of reaction: what changes it ⓶ | INVESTIGATION | MRB-103's candidate. Placed after collision theory so the investigation tests a model rather than collecting an unexplained pattern. | rate of reaction |

**XP1 — *GCSE bridge: energy, radiation and the universe*** (Physics, `gcse-bridge-energy-and-space`)

| Lesson | F | Why it bridges | `ks4_links` target |
|---|---|---|---|
| Efficiency: energy usefully transferred | QUANTITATIVE | P1 gives stores and transfers; GCSE wants the calculation within weeks. | efficiency |
| The electromagnetic spectrum | CLASSIFY | P7 covers visible light only. The spectrum is the frame GCSE waves hangs on. | electromagnetic spectrum |
| The nucleus and radioactive decay | MODEL | **Deliberately paired with XC1's *Inside the atom***: one model, two disciplines, two genuinely different treatments. This is §4.6 applied to bridge content, and it is why the two are not one lesson. | radioactive decay |
| Nuclear fusion in stars ⓶ | PROCESS | MRB-103's candidate. Sits on P12 *The Sun, stars and galaxies*. | nuclear fusion |
| The life cycle of a star ⓶ | PROCESS | MRB-103's candidate, and the natural close — the one place a KS3 student can see the whole periodic table get made. | life cycle of a star |

`ks4_links` targets above are **named, not slugged**. Real slugs get resolved at authoring time
against the live KS4 pages by the existing gate — writing guessed slugs into this document would
create exactly the silent drift §4.10 was added to prevent.

#### ⛔ Three of the 17 targets do not resolve — checked, not assumed

*All 17 targets were looked up against the live KS4 pages on 2026-07-26, before authoring rather
than during it. Fourteen resolve cleanly. Three do not, and two of those are MRB-103's own
candidates. **These are Mide's calls — the first is a science/AQA-coverage question and the second
is a KS4 content gap — so nothing has been changed in the set above.***

**`check_ks4_links()` resolves a link against `/combined/foundation/<link>.html`.** A page that
exists only under `triple/` therefore **fails** the gate — and §7.6 makes a resolving `ks4_links`
a hard requirement for a bridge lesson. So these are build failures, not cosmetic gaps.

| Target | State | What it means |
|---|---|---|
| **nuclear fusion** ⓶ | `physics/atomic-structure/nuclear-fusion` exists **under `triple/` only** | Not on the Combined pathway. |
| **life cycle of a star** ⓶ | `physics/space/stellar-evolution` exists **under `triple/` only** | Not on the Combined pathway. |
| **exchange surfaces / SA:V** | **No KS4 page anywhere** — not combined, not triple, not higher | A gap in KS4, not in KS3. |

**1. MRB-103's two physics candidates are Triple-only GCSE content.** Space physics and nuclear
fusion are not in AQA GCSE Combined Science. That is not a slug problem to be worked around by
pointing the gate at `triple/` — **it means those two lessons bridge only for students heading to
Triple Physics**, and roughly the majority of a cohort is not. A *default* bridge unit built on them
would spend two of its five physics lessons on content most of its students will never be examined
on. **⚑ Flagged for Mide as an AQA-coverage question** — this is his gate, and the whole set stands
until he rules.
> **Proposed fix, not applied:** keep both, but as **`stretch` within the physics bridge unit**
> rather than as core lessons, and promote two Combined-reachable ideas into the core slots. That is
> what §5.6's depth layers are for, and it is the move that does not smuggle a tier back into KS3
> (§2). The physics unit would then need two replacement core lessons proposed.

**2. `exchange surfaces / surface area to volume` has no KS4 counterpart at all.** AQA GCSE Biology
plainly covers it, so **this is a hole in the KS4 site**, found by designing the bridge — the bridge
pointing at KS4 turns out to be a way of auditing KS4. **It should become its own KS4 content
ticket**, not be solved by dropping the KS3 lesson: §7.6 names it "the single most common GCSE
Biology stumble", which is an argument for fixing KS4, not for looking away.

**This is the argument for designing the bridge before authoring it.** Fourteen targets are real and
the design is sound; three would have been discovered one at a time, mid-authoring, as build
failures with no obvious cause.

#### What this costs, stated plainly

- **+15 lessons, taking the full commitment from 185 to 200.** That is a real scope increase and it
  is recorded here rather than absorbed. It is also the smallest honest version: four candidates
  came from MRB-103 and eleven were needed to make three teachable units rather than three
  fragments.
- **It is the last thing authored, not the first.** Both Shape-A and Shape-B schools need Years 7
  and 8 first, and Shape B needs them *more* — an early-GCSE school compresses KS3 into two years,
  so Y7 and Y8 are its entire key stage.
- **One open audit, and it belongs to Phase 3:** *which Y9 statutory statements have no GCSE
  successor?* A Shape-B school skips §7's 51 Y9 lessons, and most of that content — ecosystems,
  inheritance, evolution, energetics, metals, Earth and atmosphere, static, magnetism, space — it
  meets again at GCSE depth. Most is not all. The register and the KS4 spec together can answer this
  exactly, and the answer is what a Shape-B school actually needs to know. **Do not assume the
  answer is "none".**

---

## 8. How KS3 plugs into the existing platform

KS3 is a **new content architecture on the existing delivery system**. Nothing below asks for new
infrastructure; it asks for a parallel path through infrastructure that already works.

### 8.1 What already exists (verified in the codebase)

| Thing | State |
|---|---|
| `generate_site_v5.py` (~5,225 lines, `build_site()` at ~L4901–5224) | Builds all topic pages. **Zero KS3 awareness.** |
| `all_subtopics_<subject>[_variant].py` × 12 | KS4 data modules, one per (subject × pathway × tier). |
| `bonding_redesign.py` + `BONDING_REDESIGN` | The v2 block vocabulary and per-page config. Branch at generator ~L4396. |
| `shared/tokens.css` | Loaded by **every** page. Contains a `[data-mode="ks3"]` block (~L157–165) — accent `#C4490F`, hover `#A63C12`, radii bumped to 12/18/26px. Described in-file as dials only, no styling. |
| `shared/quiz.js`, `shared/tap-match.js`, `shared/predict-wrapper.js`, `shared/heroes/theory-blocks.js` | Extracted, working, subject-agnostic. |
| `profiles.key_stage` + `profiles_tier_only_ks4_check` | KS3 profiles **already forbidden** from holding tier/pathway. The §2 anti-goal is enforced by the database. |
| `scheme_of_work_entries` (migration `20260501212106_schools_layer.sql`, L156–178) | Exists, keyed on `(key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week)`. **Unused by the frontend.** See §8.7 — it has two KS3 defects. |
| `subjects` table | Seeded with Biology / Chemistry / Physics, department `Science`. |

### 8.2 Generator integration

**Rule: KS3 gets its own build path. It must not be threaded through the KS4 loop.**

The KS4 pipeline is parameterised by `(pathway, tier, subject, topic, subtopic)` and driven by the
hardcoded `SITE_DATA` and `PATHWAY_TOPIC_MAP`. The tempting shortcut — give KS3 a synthetic pathway
and tier so it can ride the existing loop — **is forbidden.** It would reintroduce tier into KS3
through the back door and violate §2 within a week of shipping.

Instead:

- A new `build_ks3(output_dir)` function in its own module, `build_ks3.py`. **It is NOT called from
  `build_site()`** — see §8.2.1, which corrects an earlier version of this bullet.
- Its own registry (`ks3_data/`, §8.3). **Do not extend `SITE_DATA` or `PATHWAY_TOPIC_MAP`.**
- Its own page template — the KS4 subtopic template is prose-blob shaped and is the thing being
  moved away from. The bonding v2 branch (generator ~L4396) is the correct model to follow: a
  distinct renderer selected by data, emitting v2-grammar blocks.
- **Determinism holds:** iterate units and lessons in sorted order; two runs must produce
  byte-identical output. This is inherited, non-negotiable, and testable.
- **Zero KS4 drift:** a KS3 build must change zero bytes under the KS4 output paths. Verify by diff,
  every build.

#### 8.2.1 The two generators are independent, and their ORDER does not matter ⊕

*Corrects the bullet above, which said `build_ks3()` is "called from `build_site()`". It never was, and
it must not be. Recorded 27 Jul 2026 after the ordering hazard below shipped to `main`.*

**`build_ks3.py` is standalone. `build_site()` does not call it, and must not.** Wiring them together
would rebuild 300+ KS4 pages on every KS3 content change and make the "zero KS4 drift" gate directly
above impossible to demonstrate. Keeping them apart makes that gate provable by construction.

**The hazard that independence created, and how it is closed.** `build_site()` opens with
`shutil.rmtree(output_dir)` and rebuilds `mrbadmus_site/` from scratch. That is correct for
everything it generates and destructive for everything it does not — so whenever the KS4 generator
ran *second*, it silently deleted every page under `mrbadmus_site/ks3/`. Nothing failed: the KS4
build succeeded, exit code 0, and the deploy simply went out with no KS3 on it. A hazard that only
manifests as *missing output* and never as an error is the worst shape a build bug can take.

Documenting the order was not enough, because a document cannot be executed. Three changes, in
order of how much they actually protect:

1. **`build_site()` no longer destroys output trees it does not own.** A `FOREIGN_OUTPUT_DIRS` list
   (currently just `ks3`) is lifted out before the wipe and restored after it, before the
   copy-to-repo-root round-trip so the root mirror stays faithful. **Either order is now safe.**
2. **The cache-bust pass skips those trees too**, for the same reason. It was rewriting KS3 pages'
   `?v=` stamps whenever they happened to be present, so *whether* a KS3 page shipped stamped
   depended on which generator ran last — 221 pages of spurious diff. With this, the two orders are
   byte-identical, verified by a full `diff -r` of the served tree built both ways.
3. **`build_all.py` is the entrypoint** — one command, both generators, KS4 first because that is
   the order the deploy notes describe. Nobody needs to know any of the above to build the site.

**`verify_ks3.py` gates it.** It runs the KS4 generator *after* `build_ks3()` and asserts the KS3
output survived, count for count, plus that the repo-root mirror survived the round-trip. That is
the check which would have caught the original hazard, so it is the check that stops it returning.

**Anything not named in `FOREIGN_OUTPUT_DIRS` is still wiped** — that is the point of the list. Add
a name to it whenever another standalone generator starts writing into `mrbadmus_site/`.

*Known and deliberately left alone: KS3 pages link `/shared/tokens.css`, `styles.css` and `nav.css`
**unstamped**, which is how they have always shipped and is a small cache-staleness risk of its own.
Fixing that belongs in `build_ks3.py`, which owns those pages, not in the KS4 generator.*

### 8.3 Data files

KS4 uses twelve monolithic modules. **KS3 uses a package with one module per unit:**

```
ks3_data/
  __init__.py                     # builds KS3_UNITS by importing modules in sorted order
  chemistry_c1_particles.py       # exports UNIT = {...}
  chemistry_c2_atoms.py
  physics_p4_forces.py
  biology_b1_cells.py
  ...
```

Each module exports a single `UNIT` dict: `{code, slug, title, discipline, statutory_area,
split_rationale, lessons: [<lesson records per §4.8>]}`.

**Why not the KS4 pattern:** ~185 lessons across three files would be unreviewable, unmergeable, and
impossible to gate. One module per unit matches the release increment (§4.3) and the review gate
(§5.10) — a unit is authored, reviewed, frozen and shipped as one file.

### 8.4 URL and output taxonomy

```
/ks3/index.html                                     KS3 landing
/ks3/<discipline>/index.html                        discipline hub
/ks3/<discipline>/<unit-slug>/index.html            unit index
/ks3/<discipline>/<unit-slug>/<lesson-slug>.html    the lesson
```

Compare KS4: `/<pathway>/<tier>/<subject>/<topic>/<subtopic>.html`. KS3 is shallower because it has
no pathway and no tier — which is the point.

- **No year appears in any path**, ever (§4.5).
- Paths are **disciplinary even if navigation is integrated** (§11 decision 2). Presentation is
  reversible; URLs are not.
- **Slugs are permanent.** Renaming a lesson changes its title, never its slug — scheme-of-work rows,
  progress records and `requires` edges all point at slugs.
- Output lands in `mrbadmus_site/ks3/…`, which Cloudflare serves. Root-level hand-written pages and
  the `/teacher/` and `/student/` trees continue to be copied as they are today.

### 8.5 Tokens and the KS3 look

**KS3 pages carry both `class="rd"` and `data-mode="ks3"` on `<body>`.**

- `.rd` opts into the redesign locked token system (Space Grotesk / IBM Plex Sans / IBM Plex Mono,
  the panel/callout radii, `--rd-fs-scale: 1.25`). This is the platform's current design language and
  Law 7 says there is only one.
- `data-mode="ks3"` supplies the differentiating dials that already exist in `tokens.css`: a brighter
  accent and rounder corners. That is the entire visual difference at launch, and it is enough — KS3
  should read as *the same site, tuned younger*, not as a different product.
- Anything KS3 needs beyond those dials is **an addition to the `[data-mode="ks3"]` block in
  `tokens.css`**, never a new stylesheet.
- Subject identity colours (`--biology`, `--chemistry`, `--physics`) already exist and apply
  unchanged.
- ⚠️ **Verify at build:** the KS3 accent `#C4490F` has not been contrast-checked against the cream
  ground for body-text use. Check it against WCAG AA before it carries text, and adjust the token if
  it fails.
- Brand rule: KS3 pages are external/public, so they take the **orange chevron SVG + "MrBadmusAI"**
  nav brand per `CLAUDE.md`, not the dashboard text brand.
- Breadcrumbs: `nav_html(subject, pathway, tier)` is KS4-shaped. KS3 needs its own crumb builder
  rendering `KS3 › Chemistry › Particles and their behaviour`.

### 8.6 Component reuse — what KS3 inherits, and what doesn't transfer

**Inherit directly:**

| Component | Use at KS3 |
|---|---|
| `shared/quiz.js` | Ladder rungs ① and ②. |
| `shared/tap-match.js` | Classification and matching. Touch-safe; HTML5 drag-and-drop stays retired. |
| `shared/predict-wrapper.js` | Law 4. **Mandatory on every stateful reveal.** |
| `shared/heroes/theory-blocks.js` | Block renderer. |
| `bonding_redesign.py` block vocabulary | Starting library: `lead`, `feature-cards`, `compare-cards`, `step-sequence`, `example-callout`, `aside-callout`, `mistake-check`, `compare-reveal`. Subject-agnostic grammar. |
| ChainBuilder, WriteThenMark | Ladder rungs ③ and ④. |
| `shared/mrbadmus.v2.js` | AI tutor, with the KS3 prompt from §5.9. |

**Does not transfer — and must not appear on a KS3 page:**

| KS4 element | Why | KS3 replacement |
|---|---|---|
| `examiner-tip` block | No exam board, no examiner. | A "say it like a scientist" block — how to word an explanation. ⊕ |
| Spec pill (`5.2.1.2`) | No specification. | Statutory-coverage indicator + thread chips (§4.7). ⊕ |
| Tier pill (Higher / Foundation) | No tier at KS3. | Nothing. Depth is layers (§5.6), not a badge. |
| ⭐ Higher / 🔬 Triple labels | Meaningless at KS3. | Nothing. |
| Mark-scheme tariffs | No board awards marks. | Plain-English success criteria (§5.8). |

### 8.7 Supabase — three real defects to fix before the default sequence ships ⊕

**Two tables, and confusing them is the first mistake available here.** `scheme_of_work_entries` is
**global** — it has no `school_id` — and is therefore the right home for the *platform default*.
`scheme_of_work_overrides` is **per-school**, and is where a real school's real sequence goes. §4.5's
claim that the default "is *a* scheme of work stored the same way as any school's" is true of the
*shape* of the rows, not of the table: the default is global by definition, and a school's is not.

Both are currently **unused by the frontend**. Inspection shows three problems that are
build-blocking for KS3.

**On `scheme_of_work_entries` (the global default):**

1. **`exam_board` is `NOT NULL` with a CHECK restricted to real boards** (`'AQA'`, `'Edexcel'`,
   `'OCR'`, …). **KS3 has no exam board.** Every KS3 row would have to lie. Fix: a migration
   allowing `exam_board IS NULL` when `key_stage = 'KS3'`. A `'None'` sentinel is the wrong fix — it
   pollutes the domain and every consumer then has to special-case it.
2. **The unique constraint is ineffective for KS3.** It spans
   `(key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week)`, and `tier` and
   `pathway` are `NULL` on every KS3 row. Postgres treats NULLs as distinct in a unique index, so
   **duplicate KS3 scheme rows are currently allowed.** Fix: `NULLS NOT DISTINCT` (PG15+) or a
   partial unique index scoped to `key_stage = 'KS3'`.

**On `scheme_of_work_overrides` (per-school) — found 2026-07-26, when Rainford became seed data:**

3. **The same NULLS-DISTINCT hole, and no KS3 guard at all.** Its UNIQUE spans
   `(school_id, key_stage, year_group, tier, pathway, subject_id, academic_week)`, with `tier` and
   `pathway` NULL on every KS3 row — so **duplicate KS3 override rows are allowed**, exactly as in
   defect 2. It also has no constraint forcing `tier`/`pathway` NULL at KS3, and no shape constraint
   on `subtopic`. It has **no `exam_board` column**, so defect 1 does not apply to it.
   > ⚠️ **This was missed when defects 1 and 2 were written**, because the fix was scoped to the
   > table the default sequence lands in and the per-school table was not yet being written to.
   > Seeding one real school found it immediately — which is the argument for seeding real schemes
   > early rather than describing them. Fixed in
   > `supabase/migrations/20260726180000_ks3_scheme_of_work_overrides.sql`.

Also note:

- `topic` / `subtopic` are free text. KS3 rows should carry the **lesson slug** in `subtopic`, and
  ideally gain a real foreign key once a lesson registry table exists. Free text will drift.
- The `subjects` seed (Biology / Chemistry / Physics) supports disciplinary ownership (§4.1) with no
  change. A KS3 "Science" subject row is only needed if the product wants integrated *class
  assignment* — see §11 decision 2.
- Score persistence: bonding v2 uses `localStorage` (`quiz_best_<id>`, `lab_best_<id>`). KS3
  inherits that at minimum. Server-side progress is a Phase 5 question, not a Phase 1 blocker.

These are migration-time problems, not architecture problems — but they must be fixed before the
default sequence ships, or §4.5 is a promise the database cannot keep.

### 8.8 What a KS3 student can reach today: nothing

Verified current state:

- `profile-setup.html` — a KS3 student is shown a "you're all set" panel and correctly skipped past
  the pathway/tier wizard. There is **no onward destination**.
- `weekly-challenge.html` — shows "Weekly Challenges are coming soon for KS3".
- `leaderboard.html` — keyed on pathway and tier, so it is empty for KS3.
- The generator emits **no KS3 routes at all**.

A KS3 student who signs up today has nowhere to go. That is the strongest practical argument for the
vertical slice in §9: `/ks3/` plus one real unit is the first thing that gives them a destination.

### 8.9 Evidence from real schools ⊕ — and where their schemes live

> ✅ **Rewritten 2026-07-26, with the default-sequence reversal (§11 decision 5).** Real schools'
> schemes are **reference evidence and seed data. They are never a template, and never the default.**
> This section previously read as though Rainford's sequence had a claim on the platform's. It does
> not. **This is Mide's business, not any one school's**, and the platform is school-agnostic.

**What a real scheme is for.** Three things, none of which is "tell us how to order the curriculum":
it *validates* structural choices against practice; it *stress-tests* §4.5 by diverging from the
default and costing nothing; and it *seeds* the override mechanism with something real, so the
mechanism is demonstrated rather than described.

#### Observations that bear on this architecture

Rainford High School's KS3 materials were surveyed as reference evidence:

1. **Rainford's sequence differs materially from the default**, which is the useful part. MRB-103
   carries the locked year map, ruled by Ayo against Rainford's actual scheme: **Chemistry states of
   matter in Year 7**, with the *Physics* particle model in Year 8 as the second half of a
   deliberate deepening pair; reactions and materials in Year 7; electricity and magnetism in Year 7;
   Earth and atmosphere in Year 8; a short Year 9 that runs into a GCSE bridge.
   > **On the earlier dispute:** this section originally claimed Rainford taught states and particles
   > in Year 8, which conflicted with MRB-103. **MRB-103's reading is the record** — it is
   > self-consistent and Ayo had access this document's author did not. That settles *what Rainford
   > teaches*. It settles nothing about *what the platform defaults to*; the two questions were
   > briefly and wrongly treated as one (§11 decision 5).
   >
   > The *point* of the observation is unchanged, and is why it was included: a school reorders, and
   > **nothing rebuilds**. §9's reorder proof now runs Rainford's entire real scheme over the
   > default for exactly this reason.
2. **Rainford runs split science (separate Biology, Chemistry, Physics) across Years 7–9** — evidence
   supporting the disciplinary structure of §4.1, and a useful data point for §11 decision 2.
3. **Rainford differentiates with "LA"/"HA" variants of individual worksheets**, applied per-resource
   rather than as a tier. That is precisely the shape of the support/stretch layers in §5.6, and
   confirms the layer axis reflects real classroom practice rather than a platform invention.
4. **Rainford's Year 9 is short — explicitly "part-year, then GCSE bridge".** Read as a template that
   looked like a defect in the curriculum. Read as evidence, it is the observation that produced
   §7.6: many schools start GCSE in Year 9, and a default sequence has to serve that shape
   deliberately rather than by accident.

#### Where the schemes actually live

| Layer | Table | Contents |
|---|---|---|
| Platform default | `scheme_of_work_entries` (global) | §7's map — "MrBadmusAI default sequence v1", derived from the statutory spine and the prerequisite graph (§4.5). |
| A school's own scheme | `scheme_of_work_overrides` (per-school) | Rainford. Westleigh next. Any school after that. |

Both are generated from Python by `ks3_seed_sow.py`, so the SQL cannot drift from the maps:
`ks3_data/default_sequence.py` holds the default, and `ks3_data/school_schemes.py` holds the real
schemes, one entry per school. Adding a school is adding a dict key.

**Two divergent real schemes over identical lessons is the demonstration this architecture wants.**
One school's scheme can be mistaken for the shape of the curriculum. Two that disagree — over the
same 185 lessons, the same slugs, the same pages, with zero content difference between them — cannot
be. **Westleigh's map is the second seed and is outstanding from Mide** (requested 2026-07-26); the
slot for it is already in `school_schemes.py`.

**On whether a formal Rainford scheme-of-work document exists:** this document was written believing
none did, with the sequence implicit in folder structure; MRB-103 states Ayo ruled the year map
"against Rainford's actual SOW". §0 records this as disputed and it stays disputed — it no longer
matters much, because under the reversal nothing about the platform default depends on the answer.
Either way, **no scheme was copied into the default**, which is the claim that had to hold.

---

## 9. The vertical slice: build C1 first

**Recommendation: build Unit C1 — *Particles and their behaviour* — as the complete first slice, end
to end, before authoring anything else.** Six lessons, one unit index, full plumbing.

**Why C1 and not something else:**

1. **It is the most load-bearing idea in KS3.** The particle model underpins the whole of KS3
   chemistry, physics matter and energy, and reaches into biology via diffusion and gas exchange. If
   the architecture can carry C1 well, it can carry anything. If it can't, we want to know now.
2. **It is Year 7 in essentially every school**, so it is the first thing a pilot school would
   actually use, and the first thing that can be tested with real students.
3. **It is the densest misconception field in KS3** — particles expand when heated, there is air
   between particles, particles in a gas are "hot", a gas weighs nothing. This is the hardest test
   of Law 3, which is the newest and least proven law in this document.
4. **It has a proven KS4 counterpart.** The bonding v2 `states-of-matter` page already exists, which
   gives us a real `ks4_links` edge to prove the bridge, and existing components (parameter-sweep
   instruments, heating-curve-style labs) to reuse rather than invent.
5. **It exercises the cross-discipline model immediately.** C1 is the owner in the §7.4 table and
   P11 is its first referencer, so the single-source rule gets tested in the first slice instead of
   being discovered as a problem in month four.
6. **It spans four of the seven families** — MODEL, CONTRAST, PROCESS, INVESTIGATION — so the family
   system gets a real workout without needing three units.
7. **It is fast for Mide to examiner-check.** The science is unambiguous and he has taught it many
   times; the review gate won't bottleneck the first slice while the process is still being learned.

**Runner-up, and why it lost:** P4 *Forces* is the other candidate — equally misconception-rich, more
mathematically interesting. It loses on dependency (nine lessons, several requiring prior work) and
on breadth of downstream leverage: nothing outside physics depends on it, whereas half the key stage
depends on particles.

**What "done" means for the slice — the slice is not complete until all of these hold:**

- Six lessons authored, examiner-reviewed, `review_state: frozen`.
- `docs/ks3/statutory-register.md` exists, at least for Chemistry, with C1's statements owned
  exactly once.
- All ten laws demonstrably satisfied on every page, checked page by page.
- The prerequisite graph validates: acyclic, and the generator fails loudly on a cycle.
- Cross-reference to P11 renders correctly *before* P11 exists (graceful pending state).
- `ks4_links` to the bonding v2 states-of-matter page resolves.
- The default sequence contains C1 and a school can reorder it with a data change only — proven by
  actually doing it, not by assertion.
  > ⊕ **Strengthened 2026-07-26, with the default-sequence reversal.** The proof previously nudged
  > two units to different years, which is a synthetic reorder and a weak test. It now applies
  > **Rainford's entire real scheme** from `ks3_data/school_schemes.py` over the default and
  > rebuilds. That is a real school's real divergent sequence across all 33 units — the hardest
  > version of the claim §4.5 makes. The required result is **zero page paths changed and zero page
  > bytes changed.** Anything else is not a bug in the test; it is §4.5 having failed, and that is
  > the finding.
- Full verification pass, inherited from bonding: keyboard walk, touch model, reduced-motion, WCAG
  AA contrast on any new tints, determinism double-run (two generator runs → byte-identical output),
  and **zero KS4 pages changed**.

**Then stop and review before authoring unit two.** The slice exists to find what is wrong with this
document.

---

## 10. Build order and working method

### 10.1 Order

| Phase | Work | Gate |
|---|---|---|
| **0 — Register** | Produce `docs/ks3/statutory-register.md`: every statutory bullet, ID'd per §4.4. Produce the empty `misconception-register.md`. | Mide confirms the register is a faithful transcription of the statutory document. |
| **1 — Slice** | Build C1 end to end (§9): `build_ks3()`, KS3 page template, `ks3_data/` package, tokens, routing, `/ks3/` landing. Plus the `scheme_of_work_entries` migration from §8.7 — without it, §4.5 cannot be honoured. | Full §9 done-list. Mide reviews the science and two complete pages. |
| **2 — Chemistry** | C2, C3, then C4–C6 (the reactions block). | Per-unit examiner review. |
| **3 — Physics** | P11 (proves the reference model), then P3/P4/P5, then the rest. | Per-unit. |
| **4 — Biology** | B1 first (feeds most of biology), then the rest. | Per-unit. |
| **5 — Systems** | Progress tracking, scheme-of-work editor, coverage reporting, KS3 challenge/leaderboard if adopted (§11). | Product gate. |

Chemistry before physics before biology, because chemistry contains the most load-bearing shared
ideas and biology has the most lessons — we want the architecture proven before the biggest
authoring commitment.

> ⚠️ **Superseded 2026-07-26 (§11 decision 8, ruled FULL BUILD).** The phase table above sorts
> authoring by **discipline**. The scope ruling re-sorts it by **year first, discipline second**:
>
> | Phase | Work | Gate |
> |---|---|---|
> | **1 — Slice** | C1 end to end (§9). Unchanged. | Full §9 done-list. |
> | **2 — Year 7** | All remaining Year 7 units, all three disciplines, in the default sequence order. | Per-unit examiner review. |
> | **3 — Year 8** | All Year 8 units, all three disciplines. Confirm §11 decision 9 (P9). Run the §7.6 audit: which Y9 statutory statements have no GCSE successor? | Per-unit. |
> | **4 — Year 9** | All Year 9 units, all three disciplines (11 units, 51 lessons). **Then the §7.6 bridge group** — 3 units, 15 lessons, last because both school shapes need Years 7 and 8 first. | Per-unit, plus the `beyond_statutory` gates in §10.2. |
> | **5 — Systems** | Unchanged: progress tracking, scheme-of-work editor, coverage reporting, KS3 challenge (decision 3). | Product gate. |
>
> **Why:** the ruling keeps full scope but takes the Year-7-first cut's benefit — a pilot school gets
> a complete, usable year early. The original reasoning (chemistry's shared ideas first) is preserved
> *within* each year: C1 is still first overall, and chemistry still leads its year band.
>
> **Structure-first applies from Phase 1.** All 33 units and 185 lesson slots exist as routable
> structure from the slice onward; unauthored lessons render an honest "coming soon" state and are
> never broken links. The build order above is an **authoring** order, not a structure order.

### 10.2 Definition of done, per lesson ⊕

A lesson ships only when every line is true:

- [ ] One idea, statable in one sentence.
- [ ] `covers` non-empty; every listed statement owned by this lesson and no other.
- [ ] Opens with a phenomenon, not a definition (Law 1).
- [ ] First commitment within ~90 words (Law 2); total body prose under ~450 words.
- [ ] `misconceptions` non-empty and at least one confronted by an activity (Law 3).
- [ ] Every stateful reveal gated by a prediction (Law 4).
- [ ] Any worked sequence paired with a do-mode (Law 5).
- [ ] Concrete → representational → abstract, in that order (Law 6).
- [ ] `vocabulary` authored, marked on first use, recalled once (Law 7).
- [ ] Four-rung ladder with persistence and retry-my-misses (Law 8).
- [ ] Motion animated; reduced-motion fallback (Law 9).
- [ ] Each activity's claimed demand audited against what it actually requires (Law 10).
- [ ] `typical_year` present and used nowhere in structure (§4.5).
- [ ] `requires` edges authored; graph still acyclic.
- [ ] `ks4_links` authored or deliberately empty.
- [ ] Keyboard-complete, WCAG AA, touch-tested.
- [ ] Science examiner-reviewed; `review_state: frozen`; any net-new science flagged ⚑.

*Added 2026-07-26, from the ruled decisions:*

- [ ] **Body prose measures at reading age 9–10**, technical vocabulary excluded from the measure
      (§11 decision 7).
- [ ] **`support` key present and schema-valid**, even when empty (§11 decision 4). Empty is allowed;
      absent is a defect.
- [ ] **`figures` authored or deliberately empty**; every entry present in the diagram manifest
      (§4.10, §11 conflict 1h).
- [ ] **Blocks drawn only from the §5.1.1 segment vocabulary**, arranged by the lesson's family
      (§11 conflict 1b).
- [ ] **`covers` entries resolve** against `statutory-register.md` — parent IDs, or sub-IDs minted
      per §11 decision 11 — and no statement or clause is owned twice.

*Added 2026-07-26, with the §7.6 bridge-group design. These apply to every lesson, not only bridge
lessons — the point is that a lesson cannot end up beyond-statutory by accident:*

- [ ] **`beyond_statutory` present and explicit** (§7.6). Absent is a defect, exactly as with
      `support`.
- [ ] **If `beyond_statutory` is True: `covers` is empty and `ks4_links` is not.** Both halves are
      build failures, not warnings. A declared `covers` entry is conflict 1g's prohibition being
      breached; an empty `ks4_links` is off-spec content wearing a bridge's name.
- [ ] **If `beyond_statutory` is False: `covers` is non-empty**, which is the existing rule above,
      now stated as the other half of a pair.
- [ ] **Every `beyond_statutory` lesson appears in `docs/ks3/bridge-register.md`**, generated from
      the lesson data (§7.6), so the beyond-statutory surface is countable.

### 10.3 Review method

Inherited from bonding: **name the intended cognitive demand first, then check the activity delivers
it** (Law 10). At KS3 add one question to every review: *"which wrong idea does this lesson kill, and
would a student holding that idea be forced to notice?"* If the answer is no, the lesson is not
finished, however attractive it looks.

---

## 11. Open decisions — Mide's calls

> ✅ **ALL CLOSED, 2026-07-26.** Every decision below and every MRB-103 conflict has been ruled by
> Mide. Each carries its ruling inline, and each has a dated line in the §12 amendment log. **This
> section is now a decision record, not a queue.** Nothing here blocks the build.
>
> ⛔ **One ruling has since been REVERSED: decision 5 / conflict 1d, the default sequence.** Mide
> reversed his own ruling the same day. Both entries carry the superseded ruling, the reversal, and
> the reasoning for each. **Read the reversal, not the ruling.** Nothing else is disturbed.
>
> Two items are *scheduled* rather than undecided. Confirming decision 9 (P9 as its own unit) against
> authored physics is Phase 3. Conflict 1g's Year 9 bridge question is **answered in design** —
> §7.6 — with authoring deferred and one audit outstanding. Neither blocks Phase 1 or Phase 2.
>
> **Reopening any of these requires an amendment under §12**, not a build-session decision. The
> rulings are kept in place with their original reasoning above them so that the *cost* of each
> choice stays visible — a closed decision whose trade-offs were erased is one nobody can revisit
> intelligently. **That rule binds hardest on a reversal:** a superseded ruling is never deleted, and
> whose it was is recorded.

Ordered by how much downstream work they block.

**1. MRB-103 reconciliation.** *(Diff completed 2026-07-25. The action is closed; the conflicts it
surfaced are open and are Mide's calls.)*

Linear access was restored and MRB-103 was read in full. **It is not a stub.** The ticket body is a
scoping note, but it carries a substantial ratification comment — *"KS3 architecture ratified — year
map locked"*, 6 Jul 2026, by Ayo — recording two independent Opus 4.8 passes plus Ayo's own
sequencing ruling. That comment is the previously ratified architecture referred to in §0.

**Nothing below has been applied to this document.** §0 is explicit that anything MRB-103 says which
this document contradicts was contradicted *without having seen it*, so each conflict is written up
as two positions with costs. Mide decides; the amendment follows the decision.

**Where the two converge** (recorded so it is not re-litigated): year is soft overridable metadata,
never structure (`year_band` there, `typical_year` here); disciplinary/subject-first ownership;
tier and pathway null at KS3, enforced by `profiles_tier_only_ks4_check`; spiral carried by
prerequisite edges and thread tags rather than duplicated content; the KS4 prose blob explicitly
replaced; a `/ks3/*` generator path; a KS3 tutor persona; the `[data-mode="ks3"]` token variant;
reuse of `profiles`, `subjects` and a sequencing overlay; FIFA retained for calculations; and
AI-draft-then-Ayo-review as the authoring pipeline. On the architecture's spine, the two documents
agree.

**Conflict 1a — which unit is the vertical slice.** *Highest impact: it changes what gets built
next.* MRB-103 closes with "build Cells & Organisation (Bio 1, Y7) end-to-end as the demo vertical
slice". §9 of this document argues for C1 *Particles* on seven grounds and §10.1 makes it Phase 1.
**Cost either way:** B1 is what a Year 7 class meets first, so it is the more natural pilot opener —
but MRB-103 itself flags that B1 sits on an unresolved anatomical-diagram gap and is "on the critical
path". C1 has no such gap (the existing schematic library covers particles), has a proven KS4
counterpart to prove `ks4_links` against, and is the owner in the §7.4 cross-discipline table. Note
that MRB-103's own risk note is evidence *for* C1, not against it. **No recommendation offered — this
is a product-sequencing call and it is genuinely open.**

> ✅ **RULED by Mide, 2026-07-26. C1 *Particles*, not B1 *Cells*.**
>
> **This reverses MRB-103's ratified close, and the reversal is recorded deliberately rather than
> quietly.** MRB-103's 6 Jul 2026 ratification comment ends "build Cells & Organisation (Bio 1, Y7)
> end-to-end as the demo vertical slice". That is now overridden. Because MRB-103 was a *ratified*
> decision, the grounds are stated in full:
>
> 1. **It is reversed on MRB-103's own evidence.** MRB-103 itself flags B1 as sitting on an
>    unresolved anatomical-diagram gap and puts that gap on the critical path. Choosing B1 would mean
>    opening the build on the one unit its own author marked as blocked for assets.
> 2. **C1 has no asset gap** — the existing schematic library covers particles.
> 3. **C1 has a KS4 counterpart** (bonding v2 `states-of-matter`), so `ks4_links` gets proven against
>    something real in the first slice instead of being stubbed.
> 4. **C1 owns the §7.4 cross-discipline table**, so the single-source rule (§4.6) is tested on unit
>    one rather than discovered as a problem in month four.
>
> §9's seven grounds stand alongside these. **Nothing else in MRB-103's ratification is disturbed** —
> the year map from the same comment is *adopted* (conflict 1d), which is the clearest evidence this
> is a targeted reversal on evidence and not a preference for the newer document. **Conflict closed.**

**Conflict 1b — how a lesson is composed.** MRB-103 fixes the lesson as an *ordered deck of typed
segments* (hook, explainer, figure, worked-example, check, keyword, practical, misconception,
summary, quiz) *rendered as a stepper*. §5.1 and §6 of this document fix the block order only at the
ends and make the middle demand-driven, with the arrangement set by one of seven families — and §6
says outright that "two lessons with identical block lineups should be a coincidence of need, never a
default". **These are incompatible as written.** A uniform segment deck is exactly the uniform
lineup §6 rejects; conversely the family system is more expensive to author and to build a renderer
for. **Cost:** MRB-103's model ships a generator sooner and is far easier to author against;
this document's model is the one that carries Law 1 and Law 10, which are the reasons the prose blob
is being abandoned in the first place. A middle path exists — typed segments as the *vocabulary*,
families as the *grammar* that arranges them — and it is probably what both passes were reaching for.

> ✅ **RULED by Mide, 2026-07-26. The middle path — neither document wins outright.**
>
> **Typed segments are the VOCABULARY. The seven families are the GRAMMAR that arranges them.**
> MRB-103's segment type list is adopted as the **canonical block vocabulary**; §6's families are
> retained as the **arrangement rule**. The reconciliation is written into §5.1 and §6 rather than
> left here as a note — see the ⊕ blocks added to both, 2026-07-26.
>
> What each side gives up: MRB-103 gives up the *uniform stepper* — the deck is no longer a fixed
> lineup rendered in a fixed order. This document gives up the idea that the middle is *unconstrained*
> — blocks are now drawn from a closed, typed list rather than invented per lesson. What both keep is
> the thing each was protecting: MRB-103 keeps a buildable renderer with a finite set of block types,
> and this document keeps Law 1 and Law 10, because the *order* remains demand-driven.
> **Conflict closed.**

**Conflict 1c — misconceptions in v1 or v2.** MRB-103 ships a 6-type core first (hook, explainer,
figure, check, keyword, quiz) and defers `misconception` and `practical` to v2. Law 3 here makes
misconceptions a **required** field and at least one confrontation activity a **build gate** (§10.2).
**This is a direct contradiction and it matters more than its size suggests**, because §1 argues the
misconception is the whole reason KS3 content cannot be KS4 with easier words. **Cost:** deferring is
cheaper per lesson and gets the pipeline moving; but every lesson authored under the v1 cut would
need re-authoring, not just extending, since Law 3 changes what activities a lesson contains.

> ✅ **RULED by Mide, 2026-07-26. Misconceptions are v1, required, non-negotiable. Law 3 stands.**
>
> MRB-103's deferral to v2 is rejected on two grounds, both already on the table:
>
> 1. **Deferring costs more, not less.** Law 3 changes what *activities* a lesson contains, so
>    lessons authored without misconceptions would need **re-authoring, not extending** — 185 of
>    them. The apparent saving is a debt taken out at the worst possible interest rate.
> 2. **It is the stated reason KS3 is not KS4 with easier words** (§1). Deferring the misconception
>    layer defers the entire thesis of this document; what shipped in the meantime would be exactly
>    the thing §2 names as the anti-goal.
>
> `misconceptions` stays a **required** field and at least one confrontation activity stays a
> **build gate** (§10.2). A lesson with an empty `misconceptions` list must justify itself at review,
> and §10.3's review question — *"which wrong idea does this lesson kill, and would a student holding
> it be forced to notice?"* — is the test. **Conflict closed.** `practical`, the other type MRB-103
> deferred, is not covered by this ruling and remains a v2 candidate.

**Conflict 1d — the year map.** MRB-103 **locks** a year map to Rainford's actual placements, on
Ayo's explicit call to follow the pilot school. §7's `typical_year` column is a different map.
Material divergences: Chemistry reactions and materials/reactivity (Rainford Y7, here Y8/Y9); atoms
and the periodic table (Rainford Y8, here Y7/Y8); Earth and atmosphere (Rainford Y8, here Y9);
electricity and magnetism (Rainford Y7, here Y8/Y9); reproduction, ecosystems and genetics (Rainford
Y7/Y8, here Y8/Y9). Both documents also agree Energy is Y8. **Cost is genuinely low either way** —
this is precisely what §4.5 makes soft, and §11 decision 5 already frames it as data, not structure.
The real question is which map ships as "MrBadmusAI default sequence v1". **Recommendation: adopt
MRB-103's locked map as the published default**, because it is a real school's real sequence and
Ayo already ruled on it, and treat §7's column as the advisory fallback. If honouring it costs
anything beyond a data change, §4.5 has failed and we want to know on unit one.

> ⛔ **RULED, then REVERSED — both on 2026-07-26. Read the reversal, not the ruling.**
>
> **First ruling (superseded).** Recommendation adopted: MRB-103's locked Rainford map becomes
> "MrBadmusAI default sequence v1"; §7's `typical_year` column is the advisory fallback. Kept here
> per §11's own rule that a closed decision's reasoning stays visible.
>
> ✅ **REVERSED by Mide, 2026-07-26, jointly with decision 5. §7's map is the default. Rainford's is
> seed data.** Full reversal and reasoning recorded at decision 5 below — it is the same question and
> the same reversal. **Conflict closed on the reversed ruling.**
>
> The recommendation above was wrong in a specific and instructive way, and the error is worth
> naming rather than deleting: **it treated "a real school's real sequence" as automatically better
> evidence than a derived one.** For a *description* of practice that is right. For a *default* it is
> backwards — see decision 5.

**Conflict 1e — the KS4 relationship.** MRB-103: "Subject + topic are the shared spine with KS4."
§8.2 here forbids threading KS3 through the KS4 loop and §4.7 handles the relationship with explicit
`ks4_links` edges to a separate registry instead. **Cost:** a shared spine makes cross-key-stage
queries (coverage, progression, a student's whole journey) trivial and is the cheaper data model;
a separate registry is what keeps a synthetic tier or pathway from leaking back into KS3, which §2
names as an anti-goal and §8.2 calls a within-a-week failure. **Recommendation: keep them separate
as specified**, and treat "shared spine" as satisfied by the `ks4_links` edge rather than by shared
tables — but note this is the one place the two documents disagree about *infrastructure*, not
pedagogy, so it is the cheapest to get wrong and the most annoying to reverse.

> ✅ **RULED by Mide, 2026-07-26. Keep them separate.** Recommendation adopted: **`ks4_links` edges
> satisfy "shared spine"**; KS3 and KS4 do not share tables. The deciding risk is the one §2 names as
> an anti-goal and §8.2 calls a within-a-week failure — **a synthetic tier or pathway leaking back
> into KS3**. A shared spine is the cheaper data model right up until the moment KS4's
> `(subject, pathway, tier)` shape reaches into a key stage that has neither, and then it is very
> expensive. §4.7 and §8.2 stand unchanged. **Conflict closed.**

**Conflict 1f — progress persistence.** MRB-103 provisions a `content_progress` table (text
`content_id`, no FK, modelled on `weekly_scores`) as part of the v1 data model. §8.7 here puts
server-side progress in Phase 5 and starts on `localStorage`. **This is a timing disagreement, not a
direction one** — both end in the same place. **Recommendation:** follow §8.7 (localStorage first),
but create the table early if the pilot needs cross-device continuity, since adding it later costs
nothing already built.

> ✅ **RULED by Mide, 2026-07-26. localStorage first, per §8.7.** Server-side progress stays in
> Phase 5. **`content_progress` is created early only if the pilot needs cross-device continuity** —
> a real, observed need, not an anticipated one. Both documents agree on the destination, so nothing
> is lost by arriving at it later, and adding the table afterwards costs nothing already built.
> **Conflict closed.**

**Conflict 1g — scope beyond the statutory spine.** Phase 0 transcription (see
`docs/ks3/statutory-register.md`) settles three of these on the evidence. MRB-103's map includes
**circulation** (Y8 Bio), **rate of reaction** (Y9 Chem) and **fusion / star life cycle** (Y9 Phys).
**None of the three appears anywhere in the 2014 KS3 programme of study** — all are KS4 content. This
document omits all three, and per the authority order in §12 the statutory document wins, so the
omissions are correct *as statutory coverage*. **But MRB-103 may be right anyway** for a different
reason: its Y9 is explicitly "short, part-year then GCSE bridge", and deliberately teaching three
KS4-facing topics is a defensible bridge design. **Recommendation:** keep them out of statutory
coverage and out of `covers`, and decide separately whether Year 9 gets an explicit
beyond-statutory bridge unit. Do not let bridge content enter through the coverage register.

> ✅ **RULED by Mide, 2026-07-26.** Recommendation adopted in full. **Circulation, rate of reaction
> and fusion / star life cycle stay OUT of statutory coverage and OUT of `covers[]`.** None appears
> in the 2014 KS3 programme of study; per §12's authority order the statutory document wins.
>
> **Whether Year 9 gets an explicit GCSE-bridge unit is deferred to Phase 3.** The two questions are
> kept apart deliberately: a bridge unit is a legitimate design idea, but it must arrive as an
> *acknowledged* beyond-statutory addition, never by quietly widening what "covers" means.
> **Bridge content must not enter through the coverage register** — that is the operative
> prohibition, and it survives whatever Phase 3 decides. **Conflict closed, with a Phase 3 follow-up.**
>
> ⚠️ **Quantified 2026-07-26, when the locked map was encoded as `ks3_data/default_sequence.py`.**
> Mapping Rainford's locked map onto the 33 units gives Y7 16 units / 92 lessons, Y8 16 / 90, and
> **Y9 one unit — B6 *Health and drugs*, three lessons.** Rainford's Y9 names three topics and two of
> them (rate of reaction, fusion / star life cycle) are exactly the beyond-statutory content this
> conflict excludes. That is not an error in Rainford's scheme: their Y9 is explicitly "short,
> part-year then GCSE bridge", so a thin statutory Y9 faithfully reflects a real school's real year.
>
> **It was, however, decisive evidence that the map should not have been the platform default** —
> a default cannot silently assume every school starts GCSE in Year 9. That is one of the four
> grounds for the decision-5 reversal recorded above. Under the reversed default (§7's map), Year 9
> is **11 units and 51 lessons**, and the numbers above are now a fact about Rainford, not about the
> platform.

> ✅ **PHASE 3 FOLLOW-UP ANSWERED, 2026-07-26 — design only, authoring still deferred.** Mide
> instructed that the default must serve two shapes of school, and that the Year 9 bridge be designed
> now: schools running full KS3 to Year 9 get the remaining statutory content; schools starting GCSE
> early get an explicit bridge set. **The design is §7.6** — three units, 15 lessons, one per
> discipline, with all four MRB-103 candidates in it (circulation, rate of reaction, fusion, star
> life cycle) plus eleven proposed here.
>
> **This conflict's prohibition survives intact and is now mechanised**, which was the point of
> keeping the two questions apart. Bridge lessons carry `beyond_statutory: True`; `covers` **must**
> be empty and a declared entry is a build failure; `ks4_links` **must** be non-empty; they never
> enter `statutory-register.md`; and they are counted in a `bridge-register.md` of their own. The
> exemption has the same shape as the Working Scientifically exemption ruled at decision 6 — *named,
> declared and countable, never a quietly relaxed rule.*
>
> **What remains open is authoring, plus one real audit:** which Y9 statutory statements have no GCSE
> successor, and are therefore genuinely lost to a school that skips Year 9 KS3. §7.6 states it; the
> register and the KS4 spec can answer it exactly. **Do not assume the answer is "none".**

**Conflict 1h — figures and diagrams.** MRB-103 flags an **anatomical/structural diagram gap** and
proposes figure-slots plus a diagram manifest so the slice is not blocked. **The lesson record in
§4.8 has no figure or diagram field at all.** This is not a conflict — it is a gap in *this*
document that MRB-103 caught and this one missed. **Recommendation: adopt it.** Whichever unit is
built first, it needs somewhere to put a figure, and a manifest is the difference between a known
sourcing task and a silent blocker.

> ✅ **RULED by Mide, 2026-07-26. ADOPT.** This is recorded as **a gap in this document that MRB-103
> caught**, not as a conflict this document won or lost. Two changes, both applied 2026-07-26:
>
> 1. **§4.8 gains a `figures` field** — the lesson record can now declare the diagrams it needs.
> 2. **A diagram manifest exists**: `docs/ks3/diagram-manifest.md`. It turns every figure a lesson
>    declares into a tracked sourcing task with a status, so a missing asset is a known blocker
>    rather than a silent one discovered at build time.
>
> **Recorded in the manifest:** a Platform Backlog ticket already exists for **real-life photography
> across all subjects**. The KS3 diagram need is **related but distinct — schematic, not
> photographic**. The two must not be merged: a photograph of a beaker does not do the job of a
> particle diagram, and satisfying one ticket will not satisfy the other. **Conflict closed.**

**Also noted, minor.** MRB-103 names four threads (particle model, energy, structure↔function,
Working Scientifically); §4.7 names eight and handles WS on a separate axis (§5.7) rather than as a
thread. The eight are a superset except for **structure↔function**, which is a genuine KS3 big idea
named in the statutory preamble and is missing here — worth adding. Treating WS as an axis rather
than a thread is the better call and needs no change.

> ✅ **RULED by Mide, 2026-07-26.** **`structure↔function` is added as a ninth thread** (§4.7,
> amended 2026-07-26). It is a genuine KS3 big idea, named in the statutory preamble, and this
> document missed it — recorded as our gap, caught by MRB-103. **Working Scientifically stays an
> axis, not a thread** (§5.7), which was already the better call and needs no change. **Closed.**

**Two factual corrections to this document, arising from the diff.**

1. **§0 says no Rainford scheme of work exists as a document; MRB-103 says Ayo ruled the sequencing
   "against Rainford's actual SOW".** One of the two is wrong, and MRB-103 is the more likely to be
   right, since Ayo had access this document's author did not. **§8.9's evidence base is therefore
   weaker than it presents itself**, and its observation 1 — that Rainford teaches states and
   particles in Year 8 — conflicts with MRB-103's locked map, which puts Chemistry states of matter
   in Year 7 and the *Physics* particle model in Year 8. MRB-103's reading is self-consistent (it
   describes the two as a deliberate deepening pair) and should be preferred. **§8.9 observation 1
   and the part of §11 decision 5 that rests on it should be treated as unreliable until Mide
   confirms Rainford's actual order.**
   > ✅ **Settled 2026-07-26, in two steps.** MRB-103's reading is the record for **what Rainford
   > teaches** — that was the factual question and it is closed. The second sentence above is now
   > moot: after the decision-5 reversal, **no part of the platform default rests on it**. §8.9 is
   > rewritten accordingly. The correction was right that §8.9's evidence base was weaker than it
   > presented itself; it was wrong only in assuming the stronger evidence should therefore become
   > the default.
2. **§1 says the programme of study is "roughly 120 short bullet points".** The Phase 0 transcription
   counts **137 subject-content statements plus 18 Working Scientifically statements — 155 in all**.
   The understatement is material, because §7's lesson count is justified partly against it. See
   decision 11.

**2. Integrated or disciplinary presentation?** Most schools teach KS3 as "Science", not as three
subjects; the database models KS3 as a single Science subject; but content ownership and the KS4
bridge are disciplinary. **Recommendation:** disciplinary URLs and ownership (as specified in §4.1),
with navigation that can present either an integrated view or three subject views — a school
setting, defaulting to integrated. This is reversible; the underlying structure is not, which is why
the structure is disciplinary.

> ✅ **RULED by Mide, 2026-07-26 (Phase 0 gate).** Recommendation adopted: **disciplinary URLs and
> ownership**, with integrated navigation. The **integrated/disciplinary view as a school setting is
> deferred** — build the disciplinary structure now; the navigation toggle lands later. Nothing in
> Phase 0 or the C1 slice depends on the toggle existing, and §4.1 is unchanged by this ruling.
> **Decision closed.**

**3. Does KS3 get the weekly challenge and leaderboard?** The current system is built on
`(subject, pathway, tier)` and KS3 has neither pathway nor tier. A KS3 track would need its own
shape — probably `(discipline)` or a single mixed-science challenge. **Recommendation:** yes, but not
before Phase 5, and as a single mixed-science weekly challenge rather than three, because KS3
students mostly experience one Science.

> ✅ **RULED by Mide, 2026-07-26.** Recommendation adopted in full: **yes, at Phase 5, as a single
> mixed-science track.** Not before Phase 5 — the KS3 challenge waits on authored content to draw
> from. **Decision closed.**

**4. Does the `support` layer ship at launch?** It roughly doubles authoring effort on the parts of a
lesson that need most care. **Recommendation:** author `core` + `stretch` at launch; design the
support slots into the template from day one so they can be filled later without a re-author.

> ✅ **RULED by Mide, 2026-07-26 (Phase 0 gate).** Recommendation adopted: **all three depth-layer
> slots — `support`, `core`, `stretch` — are designed into the template now; `support` *content* is
> deferred.** A lesson ships with `core` + `stretch` authored and `support` present-but-empty, so
> filling it later is an addition, never a re-author.
>
> **No structural change is required by this ruling** — §4.8's lesson record already carries both
> `stretch` and `support` keys, and §5.6 already makes both optional at authoring time. What the
> ruling fixes is the *authoring* contract, so it belongs in the §10.2 build gates: `support` may be
> empty, but the key must be present and schema-valid on every lesson. **Do not let an authoring
> shortcut delete the slot** — a missing key is what forces a re-author later, which is the exact
> cost this decision was taken to avoid. **Decision closed.**

**5. The default sequence.** Someone must decide the platform's published default ordering. Rainford's
sequence is evidence of one school's choice, explicitly not a template — and it already diverges from
the §7 defaults (they teach reactions in Year 7 and particles in Year 8; this document suggests the
reverse). **Recommendation:** publish the §7 `typical_year` mapping as "MrBadmusAI default sequence
v1", and treat the Rainford divergence as the first live test of §4.5 rather than a reason to change
the default. If honouring their order costs anything more than a data change, the invariant has
failed and we want to find that out on unit one.

> ⚠️ **Superseded in part, 2026-07-25.** The parenthetical above ("they teach reactions in Year 7 and
> particles in Year 8") comes from §8.9 observation 1, which §11 decision 1 correction 1 marks
> unreliable. MRB-103 carries a **locked** year map ruled by Ayo against Rainford's actual scheme,
> which decision 1d recommends adopting as the published default instead of §7's column. **Decide 1d
> and this decision together** — they are the same question asked twice.

> ⛔ **First ruling, 2026-07-26 — SUPERSEDED. Kept for its reasoning; do not act on it.**
>
> > **RULED by Mide, 2026-07-26, jointly with conflict 1d.** MRB-103's locked Rainford year map is
> > adopted as "MrBadmusAI default sequence v1". Mide already ruled it against the school's real
> > scheme of work, and a real school's real sequence beats a desk-derived one as a *default*.
> > §7's `typical_year` column is demoted to advisory fallback. §8.9 observation 1 marked resolved
> > in MRB-103's favour.

---

> ✅ **REVERSED by Mide, 2026-07-26 (same day). §7's `typical_year` map IS "MrBadmusAI default
> sequence v1". Rainford's map is seed data.**
>
> **The earlier ruling was Mide's, and Mide has recorded that it was wrong.** It is written here in
> full, above, rather than deleted — §11's standing rule is that a decision whose trade-offs were
> erased is one nobody can revisit intelligently, and that applies with more force to a reversal than
> to anything else in this section.
>
> **Why it was wrong.**
>
> 1. **Rainford's SOW is reference evidence. It was never a template.** Mide supplied Rainford's map
>    *and* Westleigh's together, and the reason he supplied two was to demonstrate that schools
>    sequence the same curriculum differently. Adopting one of the two as the platform default
>    inverts the point of sending both.
> 2. **This is Mide's business, not Rainford's.** The platform must be school-agnostic. A default
>    derived from one school's timetable is that school's product with a platform's name on it —
>    every other school then opens by disagreeing with us, and the divergence reads as *our map being
>    wrong* rather than as the override mechanism working exactly as designed.
> 3. **"A real school's real sequence beats a desk-derived one" is the wrong test for a default.** It
>    is the right test for a *description of practice*. A default is not a description; it is what a
>    school with no information gets, and the only defensible basis for that is the **statutory spine
>    and the prerequisite graph** — what the programme of study says, ordered by what can actually be
>    taught before what. §7's column was built that way. Rainford's map was built around one school's
>    timetable, staffing and lab availability, none of which generalises.
> 4. **The first ruling made Year 9 unteachable in the published default.** Its own quantification
>    (recorded at conflict 1g) gave Y7 92 lessons, Y8 90, and **Y9 three**. That was read at the time
>    as a faithful reflection of a real school's real year — which it was. It is not a defensible
>    *default*, because it silently assumes every school starts GCSE in Year 9. §7's map gives
>    Y7 55 / Y8 79 / Y9 51, and §7.6 now serves the early-GCSE shape **explicitly** instead of by
>    accident.
>
> **What this ruling establishes.**
>
> - **§7's `typical_year` column is the published default**, shipped in
>   `ks3_data/default_sequence.py`. There is no "advisory fallback" layer any more — the default and
>   the column are one object, asserted equal at import so they cannot drift.
> - **Rainford's map moves to `ks3_data/school_schemes.py`** and is seeded into
>   `scheme_of_work_overrides` — one school's configured sequence, proving the override mechanism
>   works. **Westleigh is requested from Mide and becomes the second seed.** Two divergent real
>   schemes over identical lessons is the strongest available demonstration of §4.5.
> - **§8.9 is rewritten** around evidence-and-seed-data. Its observation 1 stays resolved in
>   MRB-103's favour **as a statement about what Rainford teaches** — that was a factual question and
>   MRB-103 answered it. What is reversed is the *consequence* drawn from it. The two were briefly
>   treated as one question; they are not.
> - **This still remains data, not structure (§4.5).** The reversal itself is the test: swapping the
>   published default from one whole map to another must cost a data change and nothing else. §9's
>   reorder proof was re-run against the new default for exactly this reason — see the amendment log.
>
> **Decision closed on the reversal, and conflict 1d closed with it.**

**6. Statutory ID scheme.** §4.4 invents `KS3.C.PNM.02`. Once lessons reference these IDs they are
effectively permanent. Needs explicit blessing before Phase 0. **Recommendation:** adopt as
specified.

> **Status, 2026-07-25.** Phase 0 ran ahead of this blessing, as the build queue directed, and
> `docs/ks3/statutory-register.md` now assigns all 155 IDs under the §4.4 scheme. **Nothing
> references them yet** — no lesson exists — so the cost of ruling differently is currently one
> command: IDs are minted in a single function (`statement_id()` in `ks3_statutory.py`) from one
> strand-code table, so the register regenerates wholesale. That window closes the moment C1 is
> authored. Two details Phase 0 had to settle, both flagged for the same ruling:
> **(i)** `<STRAND>` is read as *the heading that directly owns the bullets* — the only reading under
> which §4.4's own three examples (`PNM`, `CELLS`, `FORCES`) all resolve; the broader statutory area
> is kept separately as the unit's `statutory_area`. **(ii)** Working Scientifically statements are
> given `KS3.WS.<STRAND>.<nn>` ⊕, extending `<D>` beyond `B|C|P`, because §4.4 says *every* bullet
> gets an ID and §5.7.4 requires WS coverage to be auditable — but they are exempt from the
> exactly-once rule, since §5.7 taps them through `ws: []` tags on many lessons by design.
> Note also that §4.8's illustrative `KS3.P.MAT.05` does not resolve under (i); its intended target
> is `KS3.P.PHYC.05`, "the difference between chemical and physical changes".

> ✅ **RULED by Mide, 2026-07-26 (Phase 0 gate).** **The §4.4 ID scheme is adopted exactly as
> specified** — the `KS3.C.PNM.02` form. Both details Phase 0 flagged for the same ruling are
> blessed with it: **(i)** `<STRAND>` is the heading that directly owns the bullets, with the
> broader statutory area kept separately as the unit's `statutory_area`; **(ii)** Working
> Scientifically statements carry `KS3.WS.<STRAND>.<nn>`, extending `<D>` beyond `B|C|P`, and remain
> exempt from the exactly-once rule.
>
> **The 155 IDs in `docs/ks3/statutory-register.md` are therefore permanent from today.** §4.4 rule 1
> now binds: an ID never changes meaning, and a superseded ID is never reused. The reissue window
> described above is **closed by choice, not by expiry** — the mechanism (`statement_id()` in
> `ks3_statutory.py`) stays in place, but from here a re-mint is a breaking change, not a command.
>
> **Consequential fixes, applied 2026-07-26.** With the scheme blessed, every `KS3.*` ID cited
> anywhere in this document was validated against the register. Two in §4.8's illustrative lesson
> record did not resolve and have been corrected in place: `touches: ["KS3.P.MAT.05"]` →
> `["KS3.P.PHYC.05"]`, and `covers: [..., "KS3.C.PNM.03"]` → `[..., "KS3.C.PNM.02"]` (PNM has only
> two bullets, so `.03` never existed). Both were examples in prose, not references from a lesson,
> so nothing was broken by them — but an unresolvable ID in the worked example *of the ID system* is
> exactly the drift §4.4 exists to prevent. The only remaining non-resolving ID in this document is
> `KS3.P.ECT.02a` in decision 11, which is deliberate: it illustrates a sub-ID that has not been
> minted. **Decision closed.**

**7. Reading-age target.** §5.4 says "below chronological age" without a number. A specific target
(e.g. readability age 9–10 for body prose) makes it checkable. **Recommendation:** set 9–10 and
measure it, with technical vocabulary excluded from the measure.

> ✅ **RULED by Mide, 2026-07-26.** Recommendation adopted: **reading age 9–10 for body prose,
> measured, with technical vocabulary excluded from the measure.** "Measured" is the operative word —
> this is a checkable build property, not an aspiration, and it belongs in the §10.2 per-lesson
> done-list. Excluding technical vocabulary is what makes the target honest: Law 7 says the technical
> terms are carried deliberately, so counting them as difficulty would penalise doing Law 7 properly.
> **Decision closed.**

**8. Authoring capacity and scope.** **185 lessons** is a large commitment — larger than anything
attempted at KS4 so far — and §10.1 assumes it happens over many months. There is a real alternative:
build **Year 7 across all three disciplines** first (a "first year, whole curriculum" cut, roughly 60
lessons) rather than "all of chemistry". That gives a pilot school something completely usable for a
whole year group in a third of the time, at the cost of proving the architecture on a narrower range
of content. **Recommendation:** this is a product and commercial call, not an architecture one — the
architecture supports either. If schools are waiting, take the Year 7 cut. If the priority is getting
the architecture right, take the §10.1 order. Either way, C1 is still the first unit built (§9).

> ✅ **RULED by Mide, 2026-07-26. FULL BUILD.** All **33 units, 185 lessons**, three disciplines, the
> whole programme of study. The Year-7-first cut is **not** taken as a scope reduction — but its
> insight is kept, as an *authoring order*:
>
> - **Structure-first.** Every unit and every lesson slot exists from the start. The topic map in §7
>   is built out as real routable structure on day one, not accreted unit by unit.
> - **Unauthored lessons present honestly as "coming soon"** — never a broken link, never a 404,
>   never a silently missing entry. An unauthored lesson is a visible, deliberate placeholder.
> - **Authoring order prioritises Year 7 across all three sciences first**, so a pilot school gets a
>   complete, usable year early; then Year 8; then Year 9.
>
> This supersedes the either/or the decision was written as: scope is the full programme, sequencing
> takes the Year 7 cut's benefit. **Note this changes §10.1's phase order** — phases 2–4 were
> "chemistry, then physics, then biology"; the ruling makes the primary sort **year**, with
> discipline the secondary sort within a year. C1 remains the first unit built (§9) under both.
> **Decision closed.**

**9. Is P9 *Static electricity* its own unit?** It is only three lessons, and it could fold into P8
*Electric circuits* or into P10 *Magnetism and electromagnetism*. **Recommendation:** keep it
separate — static electricity is conceptually distinct from current electricity and merging them is
a known source of the "current is stored in the battery" confusion. But this is a physics-authoring
call, and either answer is architecturally fine. Decide it at Phase 3, not now.

> ✅ **RULED by Mide, 2026-07-26.** **P9 stays its own unit**, on the reasoning given — merging static
> into current electricity is a known source of the "current is stored in the battery" confusion.
> **To be confirmed at Phase 3** when the physics is actually authored and the merge question can be
> judged against real lessons rather than a lesson count. **Decision closed, with a Phase 3
> confirmation checkpoint.**

**10. AI tutor scope at KS3.** Should the tutor answer beyond the lesson, as it does at KS4? A Year 7
asking about radioactivity gets an answer that may confuse more than help. **Recommendation:** answer
anything, but anchor to KS3 language and flag when something is "something you'll meet at GCSE".

> ✅ **RULED by Mide, 2026-07-26.** Recommendation adopted: **the tutor answers anything**, anchored
> to KS3 language, and **flags "you'll meet this at GCSE"** when the answer runs ahead of the key
> stage. Curiosity is never refused; it is answered at the right altitude and signposted. This binds
> the KS3 system prompt in §5.9. **Decision closed.**

**11. There are not enough statutory statements to go round.** ⊕ *(Raised by Phase 0, 2026-07-25.
Build-blocking for the slice, because it decides what `covers` means on lesson one.)*

The transcription in `docs/ks3/statutory-register.md` counts **137 subject-content statements**. §7
specifies **185 lessons**. Two rules in this document then cannot both hold:

- **§4.4 rule 3** — every statement is owned by **exactly one** lesson.
- **§10.2** — every lesson has **`covers` non-empty**.

Under both, at least **48 lessons must own nothing**, which §10.2 forbids. The register's coverage
appendix shows this is not a rounding problem: **26 of 33 units** have more lessons than statements.
The extremes are C5 *Types of reaction* (5 lessons, 1 statement — the whole unit hangs off
`KS3.C.CR.03`), B5 *Reproduction* (8 lessons, 2 statements) and B6 *Health and drugs* (3 lessons,
1 statement). The cause is structural, not sloppy: the statutory bullets are **compound**.
`KS3.P.ECT.02` alone contains thermal equilibrium, conduction, radiation *and* insulators, which §7
quite reasonably teaches as four lessons.

Three ways out:

- **(a) Split compound bullets into clause-level sub-IDs** — `KS3.P.ECT.02a`, `.02b`, `.02c`. The
  parent ID and its verbatim text are untouched, so the transcription stays faithful and Mide's gate
  still works; exactly-once then bites at the grain lessons are actually written at. Cost: one
  careful pass over the compound bullets, and sub-IDs are permanent once referenced.
- **(b) Relax §10.2** so a lesson may own nothing provided it `touches` something. Cheapest, but it
  guts the coverage report — "what does this cover?" stops being answerable per lesson, which §4.4
  says is the whole point of the ID scheme.
- **(c) Cut §7 to ~137 lessons.** Restores the invariant exactly and shrinks the authoring
  commitment, but merges ideas that are genuinely separate sittings and pushes lessons back toward
  the blob §2 is moving away from.

**Recommendation: (a).** It is the only option that keeps both rules intact and the register
faithful, and the compound bullets are a fact about the source document rather than a problem with
§7. Do the split lazily — per unit, at authoring time, not as a big bang — so sub-IDs are only minted
where a real lesson needs one. **This needs Mide's ruling before Phase 1**, because C1's six lessons
own five statements and will hit it immediately.

> ✅ **RULED by Mide, 2026-07-26. Option (a) — clause-level sub-IDs.** Adopted with its lazy-minting
> discipline intact. The operative rules:
>
> 1. **The parent ID and its verbatim text are never touched.** A sub-ID is an additional, finer
>    handle on a clause *of* the parent, not a replacement for it. The transcription gate therefore
>    still works — `statutory-register.md` remains a faithful copy of the source document, and the
>    sub-IDs live alongside it rather than inside it.
> 2. **Exactly-once (§4.4 rule 3) bites at sub-ID grain.** Where a bullet is split, its *clauses* are
>    owned exactly once each; the parent is then covered exactly once by construction. Where a bullet
>    is not split, the parent is owned exactly once as before.
> 3. **Mint lazily — per unit, at authoring time. Never big-bang.** A sub-ID exists only because a
>    real lesson needed one. This keeps the permanent-ID surface as small as it can be.
> 4. **Sub-IDs are permanent once referenced**, exactly as parent IDs are (§4.4 rule 1, blessed under
>    decision 6). Lazy minting is about *when* an ID is created, never about whether it can later be
>    renumbered. It cannot.
>
> Form: `KS3.P.ECT.02a`, `.02b`, `.02c` — parent ID plus a lowercase letter, allocated in the clause
> order the bullet prints. **Decision closed.**

---

## 12. Change control

This document is law. Changing it changes what gets built.

- Amendments are made **here**, in this file, with a dated line in the log below — never by a local
  decision in a build session.
- Where a build discovers this document is wrong, the fix is an amendment plus a note of what the
  build actually did.
- Where this document and the bonding v2 doctrine conflict, §3 is the reconciliation record; add to
  it rather than improvising.
- Where this document and the statutory programme of study conflict, **the statutory document wins**
  and this one is wrong.
- ⊕ **Reversing a ruling, added 2026-07-26.** A reversal is an amendment like any other, with three
  extra obligations. **The superseded ruling is never deleted** — it stays in place, marked ⛔, above
  the reversal. **The reasoning for the reversal is recorded**, not just its outcome. **Whose ruling
  it was is stated plainly**, including when it was Mide's own. A decision record that quietly
  rewrites itself teaches nobody anything, and the *reason* a ruling was wrong is usually worth more
  than the ruling that replaced it.

### Amendment log

| Date | Change | By |
|---|---|---|
| 2026-07-25 | Initial architecture. Written from the statutory spine, the bonding v2 doctrine, and the existing platform. MRB-103 unavailable — see §0. | Claude (Fable 5) |
| 2026-07-25 | **MRB-103 reconciliation (§11 decision 1 rewritten).** Linear restored; MRB-103 read in full including its 6 Jul 2026 ratification comment. Delta recorded as eight conflicts (1a–1h) with two positions and costs each, plus convergences and two factual corrections. **No MRB-103 position applied** — all await Mide's ruling. §0 provenance table updated. | Claude (Opus 5) |
| 2026-07-25 | **Phase 0 register produced.** `docs/ks3/statutory-register.md` (155 statements, generated by `ks3_statutory.py`) and an empty `docs/ks3/misconception-register.md`. Awaiting the §10.1 gate. | Claude (Opus 5) |
| 2026-07-25 | **§1 corrected:** "roughly 120 short bullet points" → 137 subject-content statements plus 18 Working Scientifically. Counted in Phase 0; §12 makes the statutory document authoritative on its own contents. | Claude (Opus 5) |
| 2026-07-25 | **§8.9 observation 1 marked unreliable**, and the §0 Rainford row changed from "not available" to "disputed", per §11 decision 1 correction 1. Claim not deleted — Mide confirms which reading is right. | Claude (Opus 5) |
| 2026-07-25 | **§11 decision 11 added** (new, ⊕): 137 statutory statements cannot supply 185 lessons under §4.4 rule 3 + §10.2 simultaneously. Three options costed; clause-level sub-IDs recommended. Blocks Phase 1. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 6 RULED (closed).** Mide blessed the §4.4 ID scheme exactly as specified, including both Phase 0 details: strand = the heading that directly owns the bullets, and `KS3.WS.*` for Working Scientifically. **The register's 155 IDs are permanent from this date**; the reissue window is closed by choice. | Claude (Opus 5) |
| 2026-07-26 | **§4.8 illustrative IDs corrected** (consequence of decision 6): `KS3.P.MAT.05` → `KS3.P.PHYC.05` and `KS3.C.PNM.03` → `KS3.C.PNM.02`. All `KS3.*` IDs cited in this document were validated against the register; the only remaining non-resolving one is decision 11's deliberately unminted `KS3.P.ECT.02a`. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 2 RULED (closed).** Disciplinary URLs and ownership adopted per §4.1; integrated-vs-disciplinary navigation as a school setting **deferred**. No change to §4.1. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 4 RULED (closed).** `support`/`core`/`stretch` slots designed into the template now; `support` **content** deferred. §5.6 amended: the slot must be present and schema-valid even when empty. No structural change needed — §4.8 already carries both keys. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 8 (scope) explicitly left open** at the Phase 0 gate. Recorded as deliberate: Phase 0 is scope-independent, and C1 is the first unit under either cut, so it blocks Phase 2 rather than Phase 1. | Claude (Opus 5) |
| 2026-07-26 | **Phase 0 register independently verified** against the live DfE HTML: 155/155 bullets matched, 153 byte-identical, 2 differing only by collapsed double-spaces present in the published source. Per-discipline counts (B39/C36/P62/WS18) confirmed against the source. Verification method and the two whitespace normalisations recorded in the register. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 8 (scope) RULED: FULL BUILD.** All 33 units / 185 lessons / three disciplines. Structure-first — every unit and lesson slot exists from the start, unauthored lessons render an honest "coming soon", never a broken link. Authoring order prioritises Year 7 across all three sciences, then Y8, then Y9. **§10.1 phase table superseded**: primary sort is now year, secondary sort discipline. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 11 RULED: option (a), clause-level sub-IDs.** Parent ID and verbatim text untouched so the transcription gate still works; exactly-once bites at sub-ID grain; minted lazily per unit at authoring time; permanent once referenced. Form `KS3.P.ECT.02a`. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1a RULED: C1 *Particles*, not B1 *Cells*.** Explicitly reverses MRB-103's ratified close, on MRB-103's own evidence (it flags B1's anatomical-diagram gap as critical-path). Grounds recorded in full at 1a. No other part of MRB-103's ratification disturbed. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1b RULED: the middle path.** Typed segments are the vocabulary, the seven families are the grammar. MRB-103's segment list adopted as the canonical closed block vocabulary. **New §5.1.1** written as the reconciliation; §6 amended to read the families as grammar over that vocabulary. Stepper demoted to a rendering choice. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1c RULED: misconceptions are v1, required, non-negotiable.** Law 3 stands; MRB-103's v2 deferral rejected — deferring means re-authoring 185 lessons rather than extending them. `practical` remains a v2 candidate, uncovered by this ruling. | Claude (Opus 5) |
| 2026-07-26 | **§11 decision 5 + conflict 1d RULED jointly: MRB-103's locked Rainford year map becomes "MrBadmusAI default sequence v1".** §7's `Y` column demoted to advisory fallback. **§8.9 observation 1 marked RESOLVED** in MRB-103's favour (was: unreliable). | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1e RULED: keep KS3 and KS4 separate.** `ks4_links` edges satisfy "shared spine"; no shared tables, because that is the path by which tier/pathway leaks back into KS3 (§2 anti-goal). §4.7 and §8.2 unchanged. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1f RULED: localStorage first per §8.7.** `content_progress` created early only if the pilot needs cross-device continuity. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1g RULED: circulation, rate of reaction and fusion stay out of statutory coverage and out of `covers[]`.** Whether Year 9 gets an explicit GCSE-bridge unit deferred to Phase 3. Standing prohibition: bridge content must never enter through the coverage register. | Claude (Opus 5) |
| 2026-07-26 | **§11 conflict 1h RULED: ADOPT.** Recorded as a gap in this document that MRB-103 caught. **§4.8 gains `figures`; new §4.10** defines it; `docs/ks3/diagram-manifest.md` created, generated from lesson data. Manifest records that the existing Platform Backlog photography ticket is related but distinct — schematic ≠ photographic. | Claude (Opus 5) |
| 2026-07-26 | **Ninth thread added: `structure-function`** (§4.7). A genuine KS3 big idea named in the statutory preamble, missed here and caught by MRB-103. WS confirmed as an axis (§5.7), not a thread. | Claude (Opus 5) |
| 2026-07-26 | **§11 decisions 3, 7, 9, 10 RULED**, all adopting the stated recommendation: KS3 weekly challenge yes at Phase 5 as a single mixed-science track; reading age 9–10 measured with technical vocabulary excluded; P9 stays its own unit pending Phase 3 confirmation; tutor answers anything, anchored to KS3 language, flagging "you'll meet this at GCSE". | Claude (Opus 5) |
| 2026-07-26 | **§10.2 done-list extended** with the five checks the above rulings make testable: reading-age measure, `support` key present, `figures` in manifest, blocks from the §5.1.1 vocabulary, `covers` resolving against the register. | Claude (Opus 5) |
| 2026-07-26 | **§11 fully resolved.** All eleven decisions and all eight MRB-103 conflicts are closed. Open follow-ups are scheduled, not undecided: P9 confirmation and the Year 9 bridge-unit question, both at Phase 3. | Claude (Opus 5) |
| 2026-07-26 | **§5.7.1 added — RULE: an `INVESTIGATION` lesson anchors `covers` on the WS statement it teaches.** Discovered by the C1 slice on `testing-the-model`, where a WS-primary lesson owns no subject statement yet §10.2 requires `covers` non-empty. Recorded as a general rule for all 18 INVESTIGATION lessons rather than a per-lesson judgement, so the pattern is decided once. Subject coverage stays a true exactly-once partition; WS is exempt (§5.7) and so can carry the anchor honestly. | Claude (Opus 5) |
| 2026-07-26 | **§7.5 count corrected: 17 → 18 INVESTIGATION lessons.** `Substance misuse and decisions` (B6) was carried as `INVESTIGATION` in `ks3_data/structure.py` but omitted from the §7.5 prose list. The structure data was right. | Claude (Opus 5) |
| 2026-07-26 | **§5.10.1 added — CARVE-OUT: draft lessons may publish before real students return**, provided the page carries the visible under-review marker (`.ks3-review-flag`, already emitted by `build_ks3.py` for any non-frozen lesson). Rationale: with no real students on the site, frozen-only protects nobody and makes the build unreviewable in situ. **Expires 1 September 2026** — or earlier, on the first real student — after which §5.10's frozen-only rule resumes with no further amendment. Mide remains the sole science gate throughout; publishing a draft is not approval. Enforced, not merely documented: `verify_ks3.py` checks the marker on every published draft and FAILS once `CARVE_OUT_EXPIRY` passes while any draft still publishes, so the carve-out cannot lapse silently. Extending it requires an explicit amendment logged here. | Claude (Opus 5) |
| 2026-07-26 | **Misconception register: `PART-12`/`PART-13` RULED to stay as they are.** Both are nature-of-science misconceptions sitting in a particles family by accident of build order, but IDs are permanent (§5.3) and both are already referenced. A candidate `NOS` family is recorded, with the decision point set **before `B10 how-we-worked-out-dna` and `C8 mendeleev` are authored**; opening it would still not move these two. | Claude (Opus 5) |

| 2026-07-26 | ⛔ **§11 decision 5 + conflict 1d REVERSED — Mide reversed his own earlier ruling of the same day.** **§7's `typical_year` map is "MrBadmusAI default sequence v1"**, because it was derived from the statutory spine and the prerequisite graph rather than one school's timetable. MRB-103's locked Rainford map is **demoted from default to seed data**. Superseded ruling kept in place per the new reversal rule in §12. Four grounds recorded at decision 5: Rainford's SOW is reference evidence not a template; the platform is school-agnostic and this is Mide's business, not Rainford's; "real beats derived" is the right test for a description of practice and the wrong one for a default; and the old default gave Year 9 three lessons. §7 header amendment reversed; the advisory-fallback layer is **removed**, not re-pointed — default and column are now one object, asserted equal at import. | Claude (Opus 5) |
| 2026-07-26 | **§4.5 amended:** where the default may and may not come from, stated as part of the invariant. Also corrects the table split — `scheme_of_work_entries` is **global** and holds the default; `scheme_of_work_overrides` is **per-school**. The section previously named only the first for both jobs. | Claude (Opus 5) |
| 2026-07-26 | **§8.9 rewritten** as "Evidence from real schools — and where their schemes live". Rainford is reference evidence **and** seed data, never a template. Observation 1 stays resolved in MRB-103's favour **as a fact about Rainford**; the consequence drawn from it is reversed. New observation 4: Rainford's short Year 9 is the evidence that produced §7.6. **Westleigh requested from Mide** as the second seed; slot open in `school_schemes.py`. §0 provenance updated — the Rainford SoW dispute is recorded as no longer load-bearing, and a Westleigh row added. | Claude (Opus 5) |
| 2026-07-26 | **§8.7 gains defect 3:** `scheme_of_work_overrides` has the same NULLS-DISTINCT uniqueness hole as defect 2, no KS3 tier/pathway guard, and no `subtopic` shape constraint. Missed when defects 1–2 were written because the fix was scoped to the table the default lands in. **Found by seeding one real school** — the argument for seeding schemes early rather than describing them. Title changed from "two real defects" to "three". | Claude (Opus 5) |
| 2026-07-26 | **New §7.6 ⊕ — the Year 9 GCSE-bridge unit group, DESIGN ONLY.** Answers conflict 1g's deferred Phase 3 question. The default must serve two shapes: full KS3 to Y9 (gets §7's 11 Y9 units, 51 lessons) and early GCSE (gets the bridge set). **Three units, 15 lessons**, one per discipline, containing all four MRB-103 candidates plus eleven proposed here. Exemption shape mirrors the Working Scientifically exemption: `beyond_statutory: True` declared, `covers` **must** be empty (a declared entry is a build failure), `ks4_links` **must** be non-empty, never in `statutory-register.md`, counted in a new `bridge-register.md`. Scope cost stated: 185 → 200 lessons. **Not authored, and not in `structure.py`.** | Claude (Opus 5) |
| 2026-07-26 | **§4.8 gains `beyond_statutory`; §10.2 gains four gates** making it testable — present-and-explicit on every lesson, and the paired covers/ks4_links rules in both directions. | Claude (Opus 5) |
| 2026-07-26 | ⛔ **§7.6: three of the 17 proposed `ks4_links` targets do not resolve** — checked against live KS4 pages at design time. **Nuclear fusion and star life cycle (two of MRB-103's four candidates) exist under `triple/` only**, and `check_ks4_links()` resolves against `combined/foundation`, so both would fail §7.6's own hard gate. They are Triple-only AQA content, so they bridge only for future-Triple students. **⚑ Flagged for Mide as an AQA-coverage question; nothing changed.** Proposed fix recorded but not applied: demote both to `stretch` (§5.6) and propose two Combined-reachable core lessons. | Claude (Opus 5) |
| 2026-07-26 | ⛔ **KS4 content gap found by designing the bridge:** `exchange surfaces / surface area to volume` has **no KS4 page on any pathway or tier**, though AQA GCSE Biology covers it. Recorded as a KS4 ticket to raise, explicitly **not** to be solved by dropping the KS3 bridge lesson. | Claude (Opus 5) |
| 2026-07-26 | ⛔ **§4.5: one forward reference found in the new default** — `B3 energy-in-food` (Y7) is a §4.6 reference slot pointing at `P2` (Y9). Not caused by the reversal, but widened by it (was Y7→Y8 under the superseded default). Three options costed at §4.5; **not acted on — curriculum sequencing and §7.4 ownership are Mide's gate.** The §4.5 claim that the default is "ordered by what the prerequisite graph makes possible" is corrected from an assertion to a checked, very-nearly-true statement. | Claude (Opus 5) |
| 2026-07-26 | **`verify_ks3.py` gains a forward-reference gate** over the default sequence only (never over a school scheme — §4.5 makes a school's reorder their own business). The one known case is a **named allowance, not a suppression**: a new forward reference fails the build, and a stale allowance also fails, so the set can shrink only by a ruling. | Claude (Opus 5) |
| 2026-07-26 | **§9's reorder proof strengthened and re-run against the new default.** Previously nudged two units to different years — a synthetic reorder and a weak test. Now applies **Rainford's entire real scheme across all 33 units** and rebuilds. Required result: zero page paths changed, zero page bytes changed. | Claude (Opus 5) |
| 2026-07-26 | **§12 gains a reversal rule ⊕:** a superseded ruling is never deleted, the reasoning for the reversal is recorded, and whose ruling it was is stated plainly — including when it was Mide's own. | Claude (Opus 5) |
| 2026-07-27 | **§8.2 corrected + new §8.2.1 ⊕ — the two generators are independent and their order no longer matters.** §8.2 said `build_ks3()` is "called from `build_site()`"; it never was and must not be, or the zero-KS4-drift gate directly above it becomes undemonstrable. The independence had a sharp edge: `build_site()` rmtree's `mrbadmus_site/`, so a KS4 build running second silently deleted every KS3 page and still exited 0 — a bug that only ever showed up as missing output. Closed three ways: `build_site()` preserves `FOREIGN_OUTPUT_DIRS` (currently `ks3`) across the wipe and restores them before the root round-trip; the cache-bust pass skips those trees too, since it was rewriting KS3 `?v=` stamps depending on which generator ran last; and `build_all.py` is now the single ordered entrypoint. Both orders verified byte-identical by full `diff -r` of the served tree. `verify_ks3.py` gates it by running the KS4 generator after `build_ks3()` and asserting the KS3 output and root mirror both survive. | Claude (Opus 5) |
