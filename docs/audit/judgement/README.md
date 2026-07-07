# Judgement-layer audit (AI-read, for human spot-check)

The mechanical audit (`audit_content.py` → `../phase1_*.csv`) checks the countable rules. This layer covers the three things a script can't judge, per content standards §6: distractor quality, exam register, and whether Higher/Triple genuinely demand more. Each subject was read by an independent AI reader over a stratified sample, with count/duplication claims verified programmatically over the full corpus.

- [physics.md](physics.md)
- [chemistry.md](chemistry.md) — includes Bonding pilot specifics
- [biology.md](biology.md)

## The one conclusion all three readers reached independently

**The writing is exam-grade; the volume and tier differentiation are not.** Distractor quality and command-word register are genuine strengths across all three subjects — wrong options encode real misconceptions and classic working errors, and calculation stems read like AQA items. What fails, site-wide, is (1) question count (~2 per page vs a floor of 5), and (2) tier integrity (Higher/Triple quizzes are byte-identical to Foundation/Combined).

**Implication for Phase 2:** remediation is *generate more questions and author Higher/Triple as genuinely harder*, not *rewrite existing questions*. Existing items are mostly worth keeping and building on. Per §7, all Higher/Triple calculation content and all FIFA sets still go to Mide's full-review pile regardless — but the drafting starts from a good base, not a rewrite.

The only genuine per-item editorial defects found (a short, cheap cleanup list) are the handful of filler distractors and lookup-style stems tabulated in each subject file — notably chemistry's `atom-economy` / `percentage-yield` filler options and the `bonding/states-of-matter` + `bonding/polymers` lookup stems in the pilot unit.
