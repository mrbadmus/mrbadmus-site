# Pending demo-assignment / test-enrolment cleanup

**Destroyed before Sil's rosters are imported. Not before Mide says so.**

This list existed only as scattered notes (MORNING-2026-08-22 "say the word
and it goes", MORNING-2026-08-23 item 7) until MRB-288 required a single
place. Nothing on it is deleted by the run that adds to it — the 18 Aug
assignment is still the only worked example of a marked submission on the
platform, and destroying the only history is Mide's call.

## The list

All of it belongs to Mide's test identities (midebolabadmus@gmail.com,
anifabalo@gmail.com) on class `8r/Sc1` (`d9740ab8-c4e3-4c22-bce9-629b650782c5`).

| # | What | Why it goes |
|---|---|---|
| 1 | Assignment `282f2277-77ae-4931-93c0-356a5dee891e` — "Particle model — recall and apply", hand-seeded 18 Aug 2026 (MRB-238), 2 questions, **100% ladder-sourced (rung rows)** | ⊕ MRB-288: the proven cross-feed's ladder half. Its 2 `assignment_questions` rows are the ONLY rows violating `one_pool_per_assignment`. Deleting the assignment cascades them |
| 2 | Assignment `72a5b315-f8ef-4c04-9369-664c8d1a4b8e` — "Breathing and gas exchange · Pressure · Chemical reactions", auto-composed 20 Aug 2026, 4 questions, 100% bank-sourced | ⊕ MRB-288: the cross-feed's bank half — composed test data on a test class, week 1 of a year that hasn't started |
| 3 | Mide's own 3 `assignment_submissions` (+ attempts) against the above, `b0308282-5429-4050-827f-4707286a88aa` | test marks by the teacher's own account |
| 4 | Test enrolments / test members of `8r/Sc1` that are not real students | the class must hold only Sil's real roster when it arrives |

Until cleanup: **any surface meeting an unrecognised ref format shows a
blank, never a guess** (standing rule — already how `readAssignmentWithQuestions`
serves the rung rows: `retired: true`, and the page draws nothing for them).

## ⚠️ The dependency this cleanup unlocks

`one_pool_per_assignment` (migration `20260824214711`) is `NOT VALID` —
enforced on every NEW row, not yet validated against history, because item 1's
two rung rows violate it. **The same cleanup that deletes item 1 must run:**

```sql
alter table public.assignment_questions
  validate constraint one_pool_per_assignment;
```

— after which the constraint holds over all history and the `NOT VALID`
marker disappears. Rehearse on test first, as always.
