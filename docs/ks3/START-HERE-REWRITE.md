# KS3 "Start here" rewrite — every live lesson onto the two-option guess

**Run:** 9–10 Oct 2026, unattended. Branch `feat/ks3-start-here`, worktree
`mrbadmus-worktrees/ks3-start-here`, cut from `origin/main` at `b9a9f5488`.
**Rule:** Mide's rule of 2 Oct 2026, written for KS4 and applied here unchanged:
"Start here" is "If you had to guess, …?" with exactly two options, in simple
everyday wording any Year 7 pupil can answer, not patronising for a strong Year 9,
the answer not given away in the title, the scene or the big question above it, and
a friendly reply to each option that leads into the teaching.

## How KS3 openers work (step 1, from the code)

| What | Where |
|---|---|
| The opener's data | each lesson's `phenomenon` dict in `ks3_data/<unit>/lesson_NN_*.py`: `title`, `prompt` (the scene), `commit` (the question), `options`, `reveal`, plus `art`/`tiles`/`figures` for the media column and, on 70 lessons, an `answer` index. The big question is the lesson's `big_question`, shown in the header above the hook and on the year index cards. |
| How it renders | `r_hook()` in `build_ks3.py` (the `"hook"` block renderer): `#s-hook`, ink-dark, `data-activity="hook"`. Options come from `r_activity_options()` (`ks3_art/kit.py`) as lettered `.ks3-option` buttons, and one shared `.ks3-reveal` opens on any pick (`wirePredictions` in `shared/ks3.js`). No unit module overrides the hook. |
| Which build | `build_ks3.py` (step 2 of `build_all.py`), mirrored to `ks3/` and `mrbadmus_site/ks3/`. |
| Which gates watch it | `verify_ks3` (a hook exists, `#s-hook` resolves, the rail), `ks3_parity` (style rows on the hook, and the c1-06 keyed-commit rows), `answer_lengths` (hook options when an `answer` index exists), `ks3_rail_manifest`. |
| Frozen content? | **No.** `frozen_window_guard` reads only the KS4 question bank's frozen window; no KS3 opener text is frozen. It stayed green. |
| Lessons | **185** live (authored) KS3 lessons: 184 opened on four options, 1 (`life-processes`) on three. **None** had a two-option guess, so none was left alone. |

### The route taken

KS3 had no two-option block, so per the ruling the KS4 `Ks4Guess` behaviour is
ported into KS3's own system. It needed **no new component at all**: KS3 already
has `keyed-commit` (c1-03 `#s-bubble`, c1-06 `#s-verdict`), a set of `.ks3-option`
buttons whose panel shows the reply for the option pressed, then closing paragraphs
everyone reads. `shared/ks3.js`'s `wireKeyedCommit` drives it and `shared/ks3.css`
already paints it for ink-dark blocks. So the guess is the hook with that markup:

- `#s-hook` gains `data-keyedblock`; its commit line is the "If you had to guess,
  …?" question; two lettered `.ks3-option` buttons (KS3's house look, not KS4's
  "This / Or this"); one `.ks3-keyed-reply` per option, opening with **Good
  guess.** or **Fair guess.** as `Ks4Guess` does; then the bridge as a
  `.ks3-keyed-static` paragraph.
- Under KS3's R3 the options are never marked and stay re-choosable (`Ks4Guess`
  disables after one pick). A pupil can press the other option and read its reply.
- **No shared code changed.** `shared/ks3.js`, `shared/ks3.css` and every other
  shared asset are byte-identical to main, so no other page's cache-bust stamp
  moved: KS4, the class pages, the student work list and B2C are untouched, and
  every KS3 page whose opener did not change is byte-identical to main.

| File | Change |
|---|---|
| `ks3_data/start_here.py` | **New.** Every opener as data: question, two (option, reply) pairs, the correct index, the bridge, and a new title / scene / big question only where the old one gave the answer away. `validate()` refuses a malformed entry. |
| `ks3_data/__init__.py` | `build_units()` merges each entry over its lesson's `phenomenon` (and `big_question`), so the generator and every gate see the same opener; refuses an entry for a lesson that is not authored. The lesson modules themselves, Design's transcriptions, are untouched. |
| `build_ks3.py` | `r_hook()` renders a guess with the keyed-commit markup (`_hook_guess`). A hook with no entry renders exactly as before. |
| `ks3_parity.py` | The c1-06 keyed-commit rows and their drive are scoped to `#s-verdict`. With the hook keyed too, a bare `[data-keyed]` would have silently started measuring the hook instead, which sits above it. A tightening, not a weakening. |

### How each opener was written and checked

Sonnet writers drafted each batch from the whole lesson file (its explainer, key
facts, activities, ladder and misconceptions), against the KS4 batch 4–6 openers
as the model. A fresh Opus reviewer per two batches then read every lesson in full
and checked each opener against the four tests, the science, the title / scene /
big question for give-aways, any later text on the page that refers back to the
hook (rail labels, "at the top of this lesson"), and any later prediction it might
answer in advance, fixing what failed. A mechanical lint refused any entry whose
correct option was visibly longer, any em dash in new text, and any reply carrying
its own "Good guess". Each batch was then built, every changed page was driven in
headless Chrome (two options, the right reply per pick, the bridge, the rail stop
ticks, no console errors), every other KS3 page was compared with main byte for
byte, and the fast gates were run before the commit.

## The openers (10 of 185 lessons)

| Year | Lesson | Old opener | New question and two options | Correct option, and why | Pushed / waiting |
|---|---|---|---|---|---|
| 7 | life-processes (B1) | Is a candle flame alive?<br>3 options: Yes — it does everything a living thing does / No — but I could not say what is missing / No — and I know what is missing | If you had to guess, is a candle flame alive?<br>**A:** Yes, it is alive<br>**B:** No, it is not alive<br>*also changed: big question* | **No, it is not alive.** A flame moves, grows, feeds and makes waste, and it is still not alive. What it is missing is cells. | batch 1: committed, not pushed |
| 7 | using-a-microscope (B1) | Which objective would you turn in first to find the cells?<br>4 options: The ×4 — the widest view / The ×10 / The ×40 — the most detail / It makes no difference which | If you had to guess, which lens should you start with to find the cells?<br>**A:** The weakest lens<br>**B:** The strongest lens<br>*also changed: big question* | **The weakest lens.** That is the right start. Find the cells on the weakest lens first, then move up to a stronger one. | batch 1: committed, not pushed |
| 7 | animal-and-plant-cells (B1) | Which one is in an animal cell but not in a plant cell?<br>4 options: The nucleus / The mitochondria / The cytoplasm / None of them | If you had to guess, does the cheek cell have any of these seven parts that the oak leaf cell lacks?<br>**A:** Yes, at least one<br>**B:** No, not one<br>*also changed: title, scene, big question* | **No, not one.** Every part in your cheek cell is in the leaf cell too. The leaf cell just has some extra parts of its own. | batch 1: committed, not pushed |
| 7 | specialised-cells (B1) | Something must be worth all that. What does losing the nucleus buy the cell?<br>4 options: It can fit through narrower vessels / Room — space for the cargo it carries / It saves energy by not using the nucleus / Nothing. It is a mistake in the process | If you had to guess, what does the red blood cell gain by throwing its nucleus away?<br>**A:** More room inside<br>**B:** A faster trip | **More room inside.** Room is the gain. The space the nucleus leaves is packed with haemoglobin, the red stuff that carries oxygen. | batch 1: committed, not pushed |
| 7 | levels-of-organisation (B1) | Nothing is missing from the dish. So what has the stomach got?<br>4 options: More cells / The cells arranged into layers that work together / Different kinds of cell / Nothing — the dish just needs more time | If you had to guess, what lets a real stomach do what the dish of cells cannot?<br>**A:** Many more cells<br>**B:** Cells arranged in layers<br>*also changed: title, scene* | **Cells arranged in layers.** Layers, each with its own job: muscle to churn the food, a lining to make acid and enzymes. They only work as a team. | batch 1: committed, not pushed |
| 7 | unicellular-organisms (B1) | One is an organism. One is part of one. What settles it?<br>4 options: It can move on its own / It has more structures inside it / It carries out all seven life processes by itself / It lives in water instead of inside a body | If you had to guess, what makes the Paramecium a whole living thing and not just a piece of one?<br>**A:** It does every job itself<br>**B:** It can swim about | **It does every job itself.** A Paramecium has nobody to feed it or clean up after it. It has to feed, grow, move and reproduce all on its own. | batch 1: committed, not pushed |
| 7 | what-the-skeleton-does (B2) | What actually decides how serious a broken bone is?<br>4 options: How big the bone is / How much it hurts / What job that bone was doing, and what depended on it / How long it takes to heal | If you had to guess, what matters most for how bad a broken bone is?<br>**A:** What relies on the bone<br>**B:** How big the bone is<br>*also changed: big question* | **What relies on the bone.** A finger bone has little relying on it. A femur holds up your whole body, so far more fails when it breaks. | batch 1: committed, not pushed |
| 7 | joints (B2) | Why is the shoulder the one that gives way?<br>4 options: Shoulder muscles are weaker than elbow muscles / It moves in far more directions, so far more directions can push it out / People use their shoulders more / The bones there are softer | If you had to guess, why does the shoulder come out of place so much more than the elbow?<br>**A:** It moves in more directions<br>**B:** Its muscles are weaker<br>*also changed: title, big question* | **It moves in more directions.** Every direction a joint can move in is a direction it cannot hold against. The shoulder swings almost anywhere, so almost anything can push it out. | batch 1: committed, not pushed |
| 7 | antagonistic-muscle-pairs (B2) | You push a door open, straightening your arm. What straightens it?<br>4 options: The biceps pushes the forearm out / The biceps gets longer on its own / A different muscle, behind the arm, pulls / Nothing does — the arm falls straight | If you had to guess, when you push a door open, where is the muscle that straightens your arm?<br>**A:** On the front of your upper arm<br>**B:** On the back of your upper arm | **On the back of your upper arm.** A muscle on the back of the upper arm, the triceps, pulls on the bone behind your elbow and swings the forearm straight. | batch 1: committed, not pushed |
| 7 | biomechanics-forces-in-the-body (B2) | Something about that arrangement is doing the damage. What?<br>4 options: Muscles are simply weak for their size / The two distances from the elbow are very different / The bag is heavier than it looks / The forearm bones get in the way of the pull | If you had to guess, why does your biceps have to pull so much harder than the bag weighs?<br>**A:** Some of its pull is wasted<br>**B:** It is attached near the elbow<br>*also changed: title, scene* | **It is attached near the elbow.** The bag sits far out along your forearm, but the muscle pulls close to the elbow. A pull that close in has to be much bigger to hold the bag up. | batch 1: committed, not pushed |


