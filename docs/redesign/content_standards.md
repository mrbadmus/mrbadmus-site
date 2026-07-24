# MrBadmusAI Content Standards

**Status:** law. Every page, existing or new, is audited against this document. Design and Code briefs both reference it. No block ships that fails it.

**Why this exists:** the redesign templates were built from screenshots of the old site, so they inherited its content patterns: thin question counts, one-size-fits-all difficulty, malformed callouts. The visual system is good. The content bar was never written down. This is it.

---

## 1. Test Yourself

**Counts.**
- Default: **10 questions** per page.
- Genuinely light pages (small factual topics, e.g. state symbols): 6 to 7.
- Absolute floor: **5**. No page ships below 5. A Higher page with 3 questions is a defect, full stop.

**Style: AQA exam register, not pub quiz.**
- Every stem uses a real AQA command word where one fits: state, describe, explain, compare, calculate, predict, evaluate, suggest.
- MCQ format is accepted for now (free-text marking is a different problem), but the stem and options must read like an exam item, not a definition lookup.
- Distractors are **diagnostic**: each wrong option encodes a real student misconception or a plausible working error, not filler. A distractor nobody would pick is a wasted option.
- **Length parity**: the correct option and its distractors sit at the same level of detail and length — no option is conspicuously longer or shorter than the others, so a student cannot score by picking the longest line without reading. Where the key must be precise, at least one distractor is equally precise but wrong. (Audited by rule `1-length-parity`: flags a question where the correct option is the longest and exceeds the longest distractor by ≥4 words or ≥1.4×.)
- Calculation questions: distractors are the answers you get from the classic wrong moves (forgot to convert units, rearranged wrongly, used the wrong equation), so a student who picks one learns which error they made.
- Feedback on every option: why it's right, or which specific error produced it.

**Difficulty mix per page (guide, not straitjacket).**
- Foundation pages: roughly 60% recall/apply, 40% apply-in-context. Include at least one simple calculation where the topic has maths.
- Higher pages: no more than 30% straight recall. The rest: multi-step application, calculations with unit conversions, "explain why" reasoning, data or graph interpretation.
- Triple pages: as Higher, plus at least 2 questions touching Triple-only depth.
- **A Higher page whose questions are all "which symbol is this" is a defect.** (Current example: Standard Circuit Symbols, Higher, three trivial questions. That page fails on count, style, and tier.)

## 2. FIFA worked examples (Formula, Insert, Fine-tune, Answer)

The step-reveal FIFA pattern is confirmed as a core archetype. Requirements:

- **Worked examples: minimum 3 per FIFA block**, escalating in difficulty. One is not a pattern, it's an anecdote.
- **Then interactive practice:** the student does FIFA themselves. Each step is an input or a choice (pick the formula, insert the values, fine-tune/rearrange, state the answer with unit), checked step by step, with feedback tied to the step they got wrong. A "couple" of these per FIFA page, scaled to the topic.
- **Tier differentiation is mandatory, not cosmetic:**
  - Foundation: values in the right units, formula given or heavily cued, single-step substitution.
  - Higher: unit conversions in most examples (kJ to J, g to kg, cm³ to m³, minutes to seconds), **rearrangement required** rather than plug-and-chug, and at least one two-formula chain where the topic allows.
  - Triple: as Higher plus Triple-only quantities and contexts.
- The same three examples appearing on Foundation and Higher variants of a page is a defect. If the numbers and demands are identical across tiers, the differentiation is fake.

## 3. Common Mistake blocks

**Format is fixed, three beats:**
1. **The mistake, stated as the mistake.** What students actually write or think, quoted or paraphrased. ("Students often connect the voltmeter in series because they think it needs the current through it.")
2. **Why it's wrong** (short).
3. **The correct version.**

A block that only states correct information under a "Common Mistake" headline is a defect. If there's no named mistake in the first sentence, it isn't a Common Mistake block, it's a Key Note wearing the wrong hat, and it should be converted or cut.

**Optionality:** Common Mistake appears only where a genuine, well-known misconception exists for that topic. Forcing one onto every page produces fake mistakes, which is worse than none. Same principle as interactives: presence is a per-page decision.

## 4. Template blocks are a menu, not a mandate

The page shell (hero, explainers, callouts, matching, Test Yourself, etc.) is a **menu**. Per page, each optional block is chosen deliberately: FIFA only where there's maths, Required Practical only where AQA names one, Higher Tier box only where Higher content genuinely diverges, Matching only where term-matching is the right retrieval mode. Two adjacent pages with identical block lineups should be a coincidence of need, not a default.

## 5. Tier and pathway integrity

- Foundation Combined remains the base content. Higher content flagged `higher`, Triple flagged `triple_only`, generator filters as now.
- The standard above applies **per variant**: the Higher variant of a page is audited as a Higher page. "Same page, harder badge" is a defect.

## 6. The audit (Code's job, site-wide)

Because nobody is reading 317 pages by hand, Code runs a structured audit of the generated site against this document and outputs a **defect table**: page, tier, block, rule violated, severity. Rules 1 to 5 are written to be mechanically checkable in the main:

- Question count per page and per tier variant (rule 1 counts).
- Distractor quality and command-word usage (flag for AI review, then human spot-check).
- FIFA blocks: example count, presence of interactive practice, cross-tier duplication of numbers (string-compare the values across variants; identical means fake differentiation).
- Common Mistake blocks: does the first sentence state a mistake (pattern check plus AI read), or is it a mislabelled note.
- Block lineup fingerprints: pages whose optional-block lineup is identical to many siblings get flagged for a deliberateness check.

Output order: worst-first (Higher/Triple pages failing multiple rules at the top), so fixing starts where the damage to credibility is greatest.

## 7. Authoring and review at scale

Ten exam-grade questions across 317 pages is roughly 3,000 items, plus FIFA sets. The confirmed approach is the MRB-105 hybrid: **AI drafts to this spec, Mide reviews as the qualified AQA teacher.** But you cannot review 3,000 items either, so review is tiered:

- **Full review:** all Higher and Triple calculation content, all FIFA sets (highest risk of subtle wrongness).
- **Spot-check:** recall and comprehension MCQs, sampled per unit (e.g. 2 pages per unit in full).
- **Auto-accept with flagging:** anything the drafting pass itself marks low-confidence goes to the full-review pile regardless of category.

Drafting happens unit by unit alongside the redesign port, not as a separate later pass, so a page is never reskinned while carrying failing content.

## 8. Examiner Tip

**Locked standard: one Examiner Tip per page.** Every page carries exactly one. Unlike the Common Mistake block (§3), which is optional and appears only where a real misconception exists, the Examiner Tip is the one block that is *not* part of the §4 menu — it is mandatory on every page, every subject.

**What a good tip is:** exam technique, grounded in AQA marking. It tells the student what to write — or what not to write — to secure the marks on *this page's* spec point. It is built from the page's own material: the phrasing the mark scheme rewards, the AQA command word the topic tests, or the correction inside its Common Mistake. It is short (one or two sentences) and never invents a rule ("examiners always…"); it points at how the marks are actually awarded for this content.

**Rollout:** the audit tracks coverage at **info** severity (rule `8-examiner-tip`) — a page with no Examiner Tip is reported for tracking, not failed, so coverage grows page-by-page alongside the port without drowning real defects.
