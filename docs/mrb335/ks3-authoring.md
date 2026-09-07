# KS3 bank top-up — the authoring brief and the load path (MRB-335)

For the three KS3 content lanes. Everything a lane needs is here; nothing here
needs `build_all.py`.

---

## 1. The brief

1. **What you are adding.** New MCQ rows to `ks3_data/<unit>/questions_<nn>_<slug>.py`.
   Nothing else in the file changes. **Append to `QUESTIONS`. Never insert.**
2. **Why append.** A row's index in that list becomes its `bank_position`.
   Positions 0–11 are all that AUTO composition reads, in both mirrors
   (`compose_assignment` in Python, `bankFor()` in the backend). Inserting into
   the first twelve changes every weekly assignment the lesson has ever
   produced; appending changes nothing (RISKS D7). The validator refuses an
   insert.
3. **Ids.** `<unit lowercased>-<lesson nn>-<e|s|h><nn>`, e.g. `b1-01-e05`.
   Continue from `05` — each band's numbers must run `01, 02, 03 …` with no gap
   and no repeat. **Ids are never reused or renumbered.**
4. **Band is the rung of DEMAND, not the topic.** `easier` = Easy = recall and
   direct recognition. `standard` = Medium = applying the lesson's idea to a
   situation it covered. `harder` = Hard = an unfamiliar context, or two of the
   lesson's ideas joined. A hard question about an easy topic is `harder`.
5. **Quota.** Each `(unit, band)` needs **50 − 4 × lessons** more rows, spread
   evenly across the unit's lessons. B1 has 6 lessons → 26 more per band → 4 or
   5 per lesson per band (78 new rows for the unit). §3 below has every unit.
6. **Shape.** Four options, exactly one `"correct": True`, and a `"why"` on
   **every** distractor that names the misconception and corrects it — same
   voice as the rows already in the file. The correct option carries **no**
   `why`. `"figure": None` unless you are pointing at a figure that already
   exists in that lesson and is drawn.
7. **Content standards.** AQA / KS3 National Curriculum wording. UK spellings
   (metre, sulfur, colour, analyse). Self-contained stems — **no reference to a
   diagram, a page or "the picture above"**; a bank question is read on the
   assignment page, away from the lesson.
8. **No duplicate stems inside a lesson**, and no two questions sharing both
   their four options *and* the correct one. (Sharing an option pool with a
   different answer is fine and deliberate — see `p4-09-e01` / `e02`.)
9. **Formulae.** Write the character the child should see. ⚠️ Contrary to
   MRB-302's "both question pools stay FLAT": bank text is **not** run through
   `ks3_art.kit.formulae()` — `student-runtime.js` builds it with
   `document.createTextNode` — so `CO₂` must be written `CO₂` and `CO2` stays
   `CO2`. **Never `<sub>`**: markup is shown to the child literally, brackets
   and all. The validator refuses any tag.
10. **Nothing may restate a ladder rung** — the bank is additional depth, not a
    copy of the lesson's four rungs.
11. **Before you commit**, from the repo root:

    ```bash
    python3 -m ks3_data.question_bank   # fast: shape, positions, ids, duplicates
    python3 verify_questions.py         # the full gate, incl. figures and ladders
    ```

    Both must print OK. A red gate is a finding, not an obstacle to route around.

---

## 2. Loading the pool onto TEST

The database is a **mirror**. Python is the source; `export_ks3_questions.py`
is the only writer; every statement is an upsert, so applying twice is applying
once.

```bash
cd /Users/midebadmus/Documents/GitHub/mrbadmus-site      # or your worktree

# 1. Validate. The exporter REFUSES to mirror a bank the gate would reject.
python3 export_ks3_questions.py --check
#    → prints counts and `bank sha256 <hex>`. Write that value down.

# 2. Build the payloads.
python3 export_ks3_questions.py --json
#    → build/ks3-questions/{bank,ladder,cards}.json   (gitignored)

# 3. Apply. `ks3_pools_ingest(pool, payload)` is SECURITY DEFINER and guarded
#    by `auth.jwt() ->> 'email' = 'midebolabadmus@gmail.com'`, so it needs a
#    signed-in session as Mide — an anon key alone is refused.
#    TEST project ref: qeppkiswvclkkwbxmlok
#    Anon keys for BOTH projects are in shared/config.js (public by design);
#    take the one whose own `ref` claim matches the project you are pointing at.
export SB=https://qeppkiswvclkkwbxmlok.supabase.co
export ANON=<the qeppk… key from shared/config.js>
ACCESS=$(curl -s "$SB/auth/v1/token?grant_type=password" \
  -H "apikey: $ANON" -H 'Content-Type: application/json' \
  -d "{\"email\":\"midebolabadmus@gmail.com\",\"password\":\"$MRB_TEST_STUDENT_PASSWORD\"}" \
  | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')
curl -s "$SB/rest/v1/rpc/ks3_pools_ingest" \
  -H "apikey: $ANON" -H "Authorization: Bearer $ACCESS" \
  -H 'Content-Type: application/json' \
  -d "$(python3 -c 'import json;print(json.dumps({"pool":"bank","payload":json.load(open("build/ks3-questions/bank.json"))}))')"
#    → returns the row count written.

# 4. Prove the mirror. THIS IS THE GATE.
MRB_TEST_STUDENT_PASSWORD=<password> \
  python3 export_ks3_questions.py --verify --project test
#    → row-by-row comparison plus `bank python sha256` / `bank database sha256`.
#      They must be equal AND the comparison must be clean; if the two verdicts
#      disagree the script says so and fails, because one of them is not
#      reading what it claims to.
```

`MRB_TEST_STUDENT_PASSWORD` is the account password, held by Mide — it is not
in the repo and must never be committed. Without it `--verify` exits **3**
(“nobody looked”), which is distinct from **1** (“measured drift”).

⚠️ **Two things that will bite.**

- `--project` **defaults to `prod`.** `--verify` alone reads production. Pass
  `--project test` for a rehearsal. Nothing here ever *writes* to production;
  the prod load is a merge-time step and Mide's call.
- If the TEST project has no `midebolabadmus@gmail.com` account, `ks3_pools_ingest`
  will refuse and the load has to go in as **service role** instead (a plain
  PostgREST upsert into `ks3_assignment_bank`, bypassing the RPC). That key is
  Mide's; an executor cannot obtain it. Ask rather than improvise.
  `MRB_VERIFY_EMAIL` overrides the address `--verify` signs in with.

---

## 3. Quota per unit — `50 − 4 × lessons` per band

`new rows` is the whole unit across all three bands. Total across KS3: **2,730**
new rows on top of today's 2,220.

| unit | lessons | more per band | per lesson per band | new rows |
|---|---|---|---|---|
| B1 | 6 | 26 | 4–5 | 78 |
| B2 | 4 | 34 | 8–9 | 102 |
| B3 | 8 | 18 | 2–3 | 54 |
| B4 | 5 | 30 | 6 | 90 |
| B5 | 8 | 18 | 2–3 | 54 |
| B6 | 3 | 38 | 12–13 | 114 |
| B7 | 4 | 34 | 8–9 | 102 |
| B8 | 5 | 30 | 6 | 90 |
| B9 | 6 | 26 | 4–5 | 78 |
| B10 | 5 | 30 | 6 | 90 |
| B11 | 4 | 34 | 8–9 | 102 |
| C1 | 6 | 26 | 4–5 | 78 |
| C2 | 6 | 26 | 4–5 | 78 |
| C3 | 7 | 22 | 3–4 | 66 |
| C4 | 5 | 30 | 6 | 90 |
| C5 | 5 | 30 | 6 | 90 |
| C6 | 7 | 22 | 3–4 | 66 |
| C7 | 4 | 34 | 8–9 | 102 |
| C8 | 7 | 22 | 3–4 | 66 |
| C9 | 4 | 34 | 8–9 | 102 |
| C10 | 6 | 26 | 4–5 | 78 |
| P1 | 8 | 18 | 2–3 | 54 |
| P2 | 5 | 30 | 6 | 90 |
| P3 | 3 | 38 | 12–13 | 114 |
| P4 | 9 | 14 | 1–2 | 42 |
| P5 | 4 | 34 | 8–9 | 102 |
| P6 | 9 | 14 | 1–2 | 42 |
| P7 | 7 | 22 | 3–4 | 66 |
| P8 | 7 | 22 | 3–4 | 66 |
| P9 | 3 | 38 | 12–13 | 114 |
| P10 | 5 | 30 | 6 | 90 |
| P11 | 4 | 34 | 8–9 | 102 |
| P12 | 6 | 26 | 4–5 | 78 |

Regenerate this table at any time:

```bash
python3 -c "
import sys,collections; sys.path.insert(0,'.')
from ks3_data import question_bank as qb
c=collections.Counter(r['unit'] for r in qb.load_bank())
for u in sorted(c):
    n=c[u]; need=50-4*n
    print('%-4s %d lessons  %3d more per band  %d new rows'%(u,n,need,need*3))"
```

---

## 4. The cap, named for the backend lane

| side | function | semantics |
|---|---|---|
| Python | `ks3_data.question_bank.auto_pool(questions)` | `questions[:12]` — the slice `compose_assignment` draws from |
| Node | `bankFor()` in `server.js` / `assignment-compose.js` | must add `.lt('bank_position', 12)` to the `ks3_assignment_bank` read |

The constant is `ks3_data.question_bank.AUTO_POSITIONS = 12`. **Set work does
not go through either** — it reads every position, on purpose. The Python side
is proved by `_cap_test()` in `question_bank.py` (a synthetic 60-row lesson
composes exactly what its 12-row self composes, at all three bands); the same
test removed the cap and watched it fail before it was believed.

---

## 5. What actually happened ⊕ 8 Sep 2026

Three lanes ran this brief across the 33 units. **2,922 rows were added** to
the 2,220 that were there, so `ks3_assignment_bank` now holds **5,142** across
185 lessons.

| subject | lessons | new rows | total |
|---|---:|---:|---:|
| biology (B1–B11) | 58 | 1,020 | 1,716 |
| chemistry (C1–C10) | 57 | 870 | 1,554 |
| physics (P1–P12) | 70 | 1,032 | 1,872 |
| **total** | **185** | **2,922** | **5,142** |

More than §3's 2,730, and deliberately: `50 − 4 × lessons` rarely divides
evenly across a unit's lessons, and every lane rounded UP to a whole number per
lesson per band rather than leaving one lesson short. Nothing is below quota.

### The three traps the lanes hit

1. **A scoped `git add` still committed another lane's work.** Every commit ran
   `git add ks3_data/p5/ docs/…` and then a bare `git commit -m` — and a bare
   commit commits **the whole index**, not the paths just added. In a shared
   worktree the index is shared, so a co-tenant lane that had staged its own
   files had them swept into someone else's commit. ⚠️ **Commit with pathspecs**
   — `git commit <paths> -m …` commits exactly those paths and ignores
   everything else staged. Never `git add -A`, never a bare `git commit -m`, in
   a worktree with more than one lane in it.
2. **`verify_questions.py` check 8 goes red the moment ANY unit is topped up,
   and it is the gate that is wrong, not the content.** `_check_composition()`
   hardcodes `r["unit"] == "B1"` as its fixture and derives its expected id
   sequences from the WHOLE lesson rather than from `auto_pool()`. So it pins
   the first twelve while reading all of them. The two findings it emits —
   `compose_assignment/nearest-first` and `compose_assignment/thin-week` — are
   the KNOWN pair; a lane must check its run reports **exactly those two and
   nothing else**, because a real defect would otherwise hide behind a red that
   everybody has learned to expect. The fix is `auto_pool(bank.get(...))` in
   `own` and `nearest`.
3. **A paraphrase is a duplicate and no string check can see it.**
   `validate_lesson` refuses a repeated STRING; it cannot refuse a repeated
   QUESTION. Thirty-nine rows in the chemistry lane alone asked something their
   own unit already asked, in different words — `c9-02-e12` was `c9-02-s03`
   with lead swapped for copper. A thirty-line normalised-stem similarity sweep
   (≥ 0.90, within the unit) found them all. Run one over your own rows; §1.8's
   rule is only enforced for exact matches.

### One live answer was keyed backwards, and it was fixed

`c9-04-h02` marked "the concrete takes the pull and the steel spreads the load"
correct. That is the physics the other way round, and the row contradicted
itself: its own distractor was corrected with *"Concrete is strong in
compression and weak in tension"* while the key said the reverse. Fixed in
`ada785706` — **steel takes the pull**. It sits at `bank_position` 9, inside
the twelve this run was otherwise required to leave byte-identical; the id, the
position and the option ORDER are unchanged, so the auto window is untouched,
but a student drawn this row was being marked wrong for the right answer and
that outranks the freeze.

### ⚠️ OPEN for Mide — 274 rows in the frozen twelve are page-bound

Every lane independently reported the same thing: the self-containment rule
they were held to (§1.7 — a bank question is read on the assignment page, away
from the lesson) is broken by the **existing** rows at `bank_position` 0–11 —
the byte-frozen ones AUTO composition actually serves.

| subject | rows affected |
|---|---:|
| biology | 155 |
| chemistry | 68 |
| physics | 51 |
| **total** | **274** |

Most are mild — "the belief this lesson exists to break", inside a `why`. A
minority are **unanswerable away from the lesson page**, because they point at
an on-page instrument a child sitting an assignment cannot see: `b4-05-e04`
("the third bar is labelled…"), `b4-05-s02` ("you drag the light on the bench
down to zero"), `b4-03-h04` (its four options are "Requirement 1/2/3/4"). None
was touched. Rewriting them is a content decision inside the frozen window and
therefore Mide's, not a lane's.
