# KS3 quiz batch 2: ready, held for the GCSE session's next production load

Stored options and keys can only change with a quiz-batch load. Editing them in Python alone
leaves production behind the site, so this batch rides in the GCSE session's next production
load (ruled by the supervising chat, 17 Nov 2026), not as a load of its own.

**Site branch:** `lean/ks3-quiz-batch-2` (81add0caa6 source, a099ea419d build and keys).
**Backend branch:** `lean/ks3-quiz-batch-2` (0d1268b, `knowledge-points.json`, two keys).
Table: `ks3_ladder_questions`, two rows: `moments#apply` and `distance-time-graphs#recall`.
No bank row changes, no question id changes, so no id map.

## The two rungs

### moments, Rung 2 (apply), key B (index 1)
Stem (lean overlay, unchanged): "Two people pull with exactly 50 N at right angles on the same
stiff bolt. One uses a 0.10 m spanner, the other a 0.40 m spanner. Which statement is right?"

| | Before | After |
|---|---|---|
| A | They give the same moment, because only how hard you pull decides the moment. | They both give 50 N m, because only how hard you pull matters. |
| B (key) | The long spanner gives 20 N m, while the short one gives 5 N m. | The long spanner gives 20 N m, because moment = force × distance. |
| C | The short spanner gives more, because the force acts closer to the bolt. | unchanged |
| D | The long spanner gives more, because a longer spanner weighs more. | The long spanner gives more, because you must pull harder on a longer handle. |

Feedback, lean record: A "50 N is the force, not the moment. Moment = force × distance, so 5 N m
and 20 N m." D "Both pull with 50 N. The longer handle adds distance, not force." The lesson
file's longer feedback says the same.

Mide's ruling (16 Nov) gave B a "because" and gave D its new reason. His B wording ran to 29 words
in one sentence, against the 15-word KS3 rule, and would have made B much the longest option.
B keeps the ruling's reason and its 20 N m in 11 words. A carries a number so B is not the only
option with one. Lengths: A 62, B 65, C 72, D 77, so the key is neither the longest nor the
shortest.

### distance-time graphs, Rung 1 (recall), key C (index 2)
The key "The object was stopped" becomes "It was standing still", in the same "It was" pattern
as the other three. Feedback unchanged.

## Already fixed by the 15 Nov batch (646a56ef1f)
The three other giveaways noted on 16 Nov were measured against the options as they stood before
that batch. Today none applies: moments Rung 1 and mass-vs-weight Rung 1 have no reasons on any
option, and the mass-vs-weight Rung 2 key is not the longest option (75 characters, against 71 to 83).

## Checks run
- Blind second pass (Sonnet) on both rungs: keys right, every distractor definitely wrong. Its
  one fix is taken ("verdict" is too hard a word, now "Your answer is right but the reason is
  wrong"). Not taken: rewording distance-time D (it says "moving", so zero speed is excluded) and
  removing the hyphen in "distance-time" (a compound, not a dash, and the site's term).
- `export_ks3_questions --check`, `lean_check`, `verify_answer_positions`,
  `verify_answer_lengths`, `option_labels_check`, `export_knowledge_points --check` and
  `--check-backend`, `frozen_window_guard`: all pass.
- `lesson_contract_check --unit P3 --drive` and `--unit P4 --drive`: both SAFE (saving, restoring and tags intact, live drive included).
- Old texts are in `ks3_data/option_history.json`, so saved answers restore.

## TEST rehearsal (qeppkiswvclkkwbxmlok, 18 Nov 2026)
1. `export_ks3_questions.py --load test --pools bank,ladder` from this branch: 16,946 bank and
   370 ladder rows upserted. Verify with the service key: bank, ladder and cards exactly equal.
2. Rollback: the same load from main (38b970e785). Verify equal to main. Checked against this
   branch, exactly two ladder rows differ, the two rungs above.
3. Reloaded this branch: equal again. Then TEST was restored to main, so it matches main until
   the real load.

## Load order for the GCSE session
1. Merge both branches into yours (they are local branches; nothing is pushed).
2. Push the backend first (`knowledge-points.json`).
3. TEST: `--load test --pools bank,ladder`, then verify.
4. Production (urklkrwevjtlfbwnipjn, ends in N): the KS3 `--load prod --pools bank,ladder` in
   the same load as yours, then `--verify --project prod`.
5. Site push, then `./check_ks3_live.sh P3` and `P4`.

Rollback: revert the two site commits and the backend commit, and reload production from the
reverted Python.
