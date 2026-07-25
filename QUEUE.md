# QUEUE — lane: content/ks3

**Worktree:** `~/Documents/GitHub/mrbadmus-worktrees/ks3`
**Branch:** `content/ks3` (cut from `main` @ `14d9d405d`, 25 Jul 2026)
**Purpose:** build KS3 Science — Years 7 to 9, all three disciplines.

> **Updated 25 Jul 2026, 19:30.** `docs/ks3/architecture.md` has landed and is committed here
> (`07da73795`). Linear is now authenticated. Both facts changed this queue — an earlier version told
> you to stop if the architecture was missing. It is no longer missing. Read on.

---

## Standing rules for this lane

1. **Work only inside this worktree.** Never edit, stage, or read-modify files in
   `~/Documents/GitHub/mrbadmus-site` or in any other worktree under
   `~/Documents/GitHub/mrbadmus-worktrees/`. Reading `main` for reference is fine; writing to it is not.
2. **One session per worktree.** If another Code session is already open here, do not start a second.
3. **Commit freely.** You do not need permission to commit.
4. **NEVER push.** Mide pushes via GitHub Desktop, always.
5. **Follow the AUTONOMY CONTRACT** at the top of `CLAUDE.md` — act, don't ask.
6. **Science accuracy is Mide's gate, not yours.** Whether a KS3 explanation is correct, and whether
   it lands right for Year 7 vs Year 9, is his call. Draft it; flag what you are unsure of.
7. **`docs/ks3/architecture.md` is law** (its own §12: "Changing it changes what gets built").
   Amendments go **in that file with a dated log line**, never as a local decision in a build session.
8. **Deviations go in the final report, one line each** — not mid-run.

---

## Read these first, in this order

1. **`docs/ks3/architecture.md`** — 71KB, sha256 `cf3448b56685a997`. Authoritative and self-contained.
   Read it in full before touching anything. It is now committed on `main` (`490bacb14`) and merged
   into this branch, so there is one canonical copy and no sync question to worry about.
2. **`docs/redesign/architecture_v2.md`** — the bonding v2 doctrine. Inherited *in spirit* and
   explicitly overridden where KS4 assumptions don't serve 11–14 year olds. Every override is named
   in architecture.md §3. Do not apply v2 laws to KS3 without checking §3 first.
3. The statutory programme of study (*National curriculum in England: science, Key Stage 3*, DfE 2014)
   outranks both documents. It is the spine.

---

## ⚠️ Read this before you plan your work

The original brief for this lane said "build one topic end to end". **The architecture says you cannot
start there**, and the architecture wins (it is law; the brief predates it). Specifically:

- **§10.1 puts Phase 0 before Phase 1.** Phase 0 is the statutory register, and it carries its own
  Mide gate: *"Mide confirms the register is a faithful transcription of the statutory document."*
  Phase 1 — the C1 slice — comes after that gate.
- **§11 decision 6 (statutory ID scheme) explicitly "needs explicit blessing before Phase 0."**
  §4.4 invents the `KS3.C.PNM.02` form, and once lessons reference those IDs they are permanent.
- **§11 lists ten open decisions that are Mide's calls**, several of which shape Phase 0/1 output.

So the honest state is: **the C1 slice is gated, but there is real unattended work ahead of it.**
Tasks 1 and 2 below are that work. Task 3 is the gate. Do not jump to task 3.

---

## Task 1 — MRB-103 reconciliation *(now unblocked — do this first)*

Architecture.md §0 flags this as an **open action**, and §11 ranks it decision #1: "blocking-ish,
cheap to resolve." The whole document was reasoned from the statutory spine **without sight of
MRB-103**, the previously ratified KS3 architecture, because Linear was unauthenticated when it was
written. **Linear is authenticated now.** You should have Linear MCP tools available.

1. Read **MRB-103** in Linear, in full, including comments.
2. Diff it against `docs/ks3/architecture.md` — structure, topic map, content model, naming, sequence.
3. Record the delta **in §11 of architecture.md**, under decision 1, with a dated line per §12.

**Treat every conflict as a genuine open question, not a settled reversal.** §0 is explicit:
"Anything in MRB-103 that this document contradicts was contradicted *without having seen it*."
Where they disagree, write up both positions and what each would cost. Do not silently rewrite the
architecture to match MRB-103, and do not dismiss MRB-103 because the newer document is more detailed.
Mide decides.

If MRB-103 turns out not to exist, or to be a stub, say so plainly — that resolves the decision too.

---

## Task 2 — Phase 0: the statutory register

Per §10.1, Phase 0 produces:

- **`docs/ks3/statutory-register.md`** — every statutory bullet from the DfE KS3 programme of study,
  ID'd per §4.4, with each statement **owned exactly once** (the single-source rule).
- **`docs/ks3/misconception-register.md`** — created empty, ready to fill during authoring.

This is transcription and structuring, not invention, so it is genuinely doable unattended. Two things
to be careful about:

- **The ID scheme is not blessed yet** (§11 decision 6). Build the register using §4.4's scheme as
  specified — the recommendation is "adopt as specified" — but generate the IDs so they can be
  **mechanically reissued** if Mide rules differently. Do not hand-scatter IDs in prose you would have
  to rewrite by hand.
- **Faithful transcription is the gate.** Do not paraphrase, merge, or "tidy" statutory bullets.
  Mide is checking it against the source document.

Chemistry at minimum (§9 requires C1's statements owned). All three disciplines is better if the
transcription goes cleanly.

---

## Task 3 — the C1 vertical slice ⛔ GATED — do not start unattended

§9 names it: **Unit C1 — *Particles and their behaviour***. Six lessons, one unit index, full plumbing.
The seven reasons it beats the P4 *Forces* runner-up are in §9; read them, because they tell you what
the slice is meant to prove.

**Do not start this until both hold:**
- Mide has confirmed the Phase 0 register (§10.1 gate), **and**
- Mide has ruled on §11's open decisions — at minimum #6 (ID scheme), and ideally #2, #4 and #8,
  which change what a lesson contains and how many you build.

When it is unblocked, §9's done-list is the acceptance criteria — all of it, including: six lessons
examiner-reviewed at `review_state: frozen`; the prerequisite graph acyclic with the generator failing
loudly on a cycle; the P11 cross-reference rendering a graceful pending state *before* P11 exists;
`ks4_links` resolving to the bonding v2 states-of-matter page; a school reordering the default sequence
**by data change only, proven by doing it**; determinism double-run (two generator runs → byte-identical
output); and **zero KS4 pages changed**.

Then **stop and review before unit two.** §9: "The slice exists to find what is wrong with this document."

---

## When you are done

Report: the MRB-103 delta and where you recorded it, the state of the register, which §11 decisions
are blocking, and any one-line deviations. Leave the work committed on `content/ks3`. **Do not push.**
