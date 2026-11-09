# The jobs only you can do (8 Nov 2026)

Everything below is on production (`urklkrwevjtlfbwnipjn`). None of it has been done for you. Do them in this order: C, then D, then E, then F. Each stands alone, so stopping between them is safe.

---

## C. Sign-in rate limit (about 10 minutes)

**Why:** every child signs in through the backend, so Supabase sees one address for every child. Junk logins could use up that shared allowance and lock real children out.

**Why this order is safe:** nothing changes for a child until step 5. Since tonight's backend, if the key in step 5 is wrong or revoked, a child's sign-in falls back to the old path and still works.

1. **Raise the limit first.** Supabase → your production project → **Authentication** → **Rate Limits** → "Token refreshes" (the `/token` limit): change **150 to 450** per 5 minutes → **Save**.
2. Leave "Token verifications" at 30 and "Sign-ups and sign-ins" at 30.
3. **Make the key.** **Project Settings** → **API Keys** → **Secret keys** → **Add new secret key** (`sb_secret_…`). Name it `backend-child-signin`. Copy it. Don't put it anywhere else.
4. **Switch on forwarding.** **Authentication** → **Rate Limits** → **IP Address Forwarding** → turn **on** → **Save**. Nothing changes yet: it only acts on requests that carry the new key.
5. **Give it to the backend.** Render → `mrbadmus-backend` → **Environment** → **Add Environment Variable** → key `SUPABASE_SECRET_KEY`, value the key → **Save, rebuild and deploy**. Wait for "Live".
6. **Check it.** Open <https://mrbadmus-backend.onrender.com/api/health>. It must say `"child_signin":"forwarded"`. If it says `"anon"`, the variable didn't take; nothing is broken, so check for a typo.
7. **Try it.** Sign in as Orion at <https://mrbadmus.com/go/>. Then in Render → **Logs**, search `child sign-in`. You want "secret key + sb-forwarded-for" and no "Auth refused". Then search `client-ip`: the line should end `agrees: yes`.
8. **Bring the limit back down.** Return to Rate Limits and change 450 to **300**.

**To undo:** Render → Environment → delete `SUPABASE_SECRET_KEY` → Save. Children go back to the old path straight away.

**Separately, only if you use custom email (Resend) for Supabase Auth:** set "Emails sent" to about 100 an hour. I couldn't confirm which sender is configured. On Supabase's built-in email the box is locked, so leave it.

---

## D. The `lesson_mark` constraint

**What it changes:** the list of allowed values on `ai_usage_events.kind` gains one word, `lesson_mark`. It is the only change. No data changes, and all 1,129 existing rows already fit.

**What depends on it today:** nothing that a child or parent sees. Marking and the daily cap both work without it. What is lost until then is the cost record of AI lesson marks: production has 2 AI-marked lesson answers with no cost row. The only database function reading this table is `ai_usage_counts`, and it isn't affected by a new value.

**Why it is yours:** it drops and re-adds a rule on an existing table, so it isn't additive. The whole thing takes well under a second.

**To apply:** Supabase → **SQL Editor** → **New query** → paste → **Run**. Check the project name at the top first.

```sql
alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check','lesson_mark']::text[]));
```

**Rollback** (this removes any lesson-marking cost rows written since, because they wouldn't fit the narrower rule):

```sql
delete from public.ai_usage_events where kind = 'lesson_mark';
alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check']::text[]));
```

---

## E. The 6 inflated lesson scores

"True" means the answers actually marked right. The difference is self-ticks counted as marks, which is how scores worked before 13 Oct.

| # | Whose | School or family | Date | Lesson | Stored | True | Row id |
|---|---|---|---|---|---|---|---|
| 1 | AY | **Rainford** (pupil account on a Gmail address) | 19 Aug | particle-model | 1/4 | **no answers stored, can't be checked** | `835f87d1-3d45-4063-aca6-497c497f6c8f` |
| 2 | AY | **Rainford** | 19 Aug | life-processes | 4/4 | 2/4 | `80b93ba8-77c3-4658-a40a-e180c141dff4` |
| 3 | AY | **Rainford** | 21 Aug | life-processes | 2/4 | 0/4 | `0b9e2588-c30f-4722-bf77-94831af45a09` |
| 4 | AY | **Rainford** | 21 Aug | particle-model | 3/4 | 1/4 | `fe355759-be78-4246-850e-885afdff0bb4` |
| 5 | Orion | **Family** | 9 Oct | specialised-cells | 4/4 | 2/4 | `d67ce6bf-f7c3-468c-911d-f335e553570c` |
| 6 | Ayomi | **Family** | 12 Oct | human-reproductive-systems | 4/4 | 2/4 | `296873e7-33ea-43ba-9795-09bce8b44a4d` |

Not inflated: Lydia's 2/4 (23 Sep), and Orion's two rows from 16 Oct, which were scored by the new rules.

**Please look at AY's account:** if it's your own test pupil, the four Rainford rows don't matter. School pupils' scores still count their own ticks. That is how school scoring works today, and your rule was not to change it. So rows 1–4 are "inflated" only by the family rule, and I'd leave them.

**What reads these rows:** Wrapped (`wrapped_pupil`, `wrapped_status`). Changing a row can change that pupil's Wrapped numbers. The parent view doesn't use them for answers: it reads the answer ledger.

**If you want the two family rows corrected** (my suggestion: yes, these two only). The second statement reverses it:

```sql
update public.quiz_scores set score = 2, percentage = 50
 where id in ('d67ce6bf-f7c3-468c-911d-f335e553570c', '296873e7-33ea-43ba-9795-09bce8b44a4d');

-- to undo:
-- update public.quiz_scores set score = 4, percentage = 100
--  where id in ('d67ce6bf-f7c3-468c-911d-f335e553570c', '296873e7-33ea-43ba-9795-09bce8b44a4d');
```

---

## F. Examiner and science calls (quoted from the run notes, §10, plus the plant-cell answer)

**The plant-cell answer**

- **Question:** "Down a school microscope you can see a leaf cell’s wall, its nucleus, its vacuole and its chloroplasts — but not its mitochondria and not its membrane. Explain why not."
- **Answer:** "A plant cell has a cell wall and a permanent vacuole, and leaf cells have chloroplasts, but an animal cell has none of these."
- **Mark scheme:**
  1. "Says both are still there — the microscope cannot show them, they are not absent."
  2. "Says a chloroplast is several times wider than a mitochondrion, which is why one shows and the other does not."
  3. "Says the membrane is thinner again — only a few molecules across."
  4. "Says turning the magnification up would not fix it, because the limit is what the microscope can separate, not how big it makes things."
- **Marker's feedback:** I can't give you this verbatim. It came from a throwaway TEST family on 16 Oct that was later deleted, and the transcript kept the mark but not the feedback. I couldn't re-mark it tonight either, because the model key on this Mac is invalid.
- **What you should know:** that answer was typed by a test script, not a child, and it answers a different question (animal against plant cells). 0/4 looks correct to me, but it's your call.

**Knowledge-point tags:** "all machine-drafted; please review, especially 'antitoxins ← lymphocytes' and 'IUD … stopping implantation'." Tonight added 1,295 more tags, drafted the same way, with no new points invented for the last 324. Whole grids went to one point because each cell's wording is only "?": Halogens `grid-nine`, Reactivity Series `bench-twelve`, Displacement `grid-sixteen`. Poor fits, placed as best guesses: Measuring a Temperature Change `plan-judge-4` and `rig-build-1`, Life Processes `seven-tests-3`, What the Skeleton Does `switch-off-chains-2`, and Exercise, Asthma and Smoking `locate-the-fault-3`. About 6 sit on items that show only bare options such as "A / B / C", so those are best guesses. Also guesses, because the activity's wording is thin: Extraction of Metals `pick`, Changes of State `ans`, Particle Motion `p3` and `p4`, Metal Hydroxides `forge`, Viral Diseases `clue`, Cell Specialisation `compared`, Titrations `rows`, Thermal Conductivity `tries`, Ionic Bonding `wa`, Internal Energy `picks`. Weaker, placed on wording alone: Enzymes `own` and `mean`, Decomposition `own` and `rate`, Food Security `picks`. Judgement calls: Microscopy `gate`, Carbon Cycle `labels`.

**The new marking rule:** "'a scheme point is credited in full or not at all'. Bundled points (e.g. 'bubbles AND the metal disappears') now earn nothing if half is missing ('bubbles… hydrogen' went 2/4 → 0/4); split such points if you want part credit."

**Levels:** "full marks at Level 3 with 4 of 5 indicative points (Ada's peas answer)."

**Possibly harsh:** "Ben's 0/4 for 'collide more often… denatured'."

**AI marker said** "'animal cells lack mitochondria' (wrong)."

**Tutor content:** "'water from respiration is part of why you sweat'; 'lit candle… actively burning' against the lesson's 'respiration is not slow burning'; 'energy lost as heat' against the lesson's 'heat is a pathway'; 'brain detects rising CO₂' for KS3; 'equivalence point', phenolphthalein for KS3."

**Prompt labels for Foundation:** "glucagon is now marked Higher-only in the tutor prompt (confirm AQA 4.5.3.2); the older 'Higher:' labels may be wrong (meiosis, monoclonal antibodies, terminal velocity, potential dividers, n=sin i/sin r), so for now they're taught to Foundation, flagged ⭐."

**Required-practical numbers:** "conflict across the site's own content (e.g. chemistry RP1 = chromatography in all_subtopics_chemistry.py vs making salts in the tutor's list). Tutor and marker now use names only; the numbers are your call."

**Wording:** "the tutor notice says 'parent **or tutor**'; say if you want 'parent' only." The new Ask-the-tutor sheet uses the same wording.

**Credentials claims (9 Oct false-claims rule):** "'Signed note from a qualified science teacher' (parents/home-education.html); 'Two exam answers a month marked by Mr Badmus himself', '2 human marks left', 'Mr Badmus can mark this one himself… three school days'."

**New tonight:** a balanced whole-number multiple on the KS3 equation balancer (e.g. 2H₂ + 2… all doubled) is saved as self-checked rather than wrong, because the page says balanced but gives no tick. Whether AQA credits a multiple is your call.

---

## Also yours, smaller

- **TEST clean-up:** on the TEST project, run `drop schema rh cascade;` (4 empty rehearsal tables).
- **Local model key:** `ANTHROPIC_API_KEY` in `mrbadmus---backend/.env` on this Mac is invalid. Production's is fine (the live tutor answered tonight). Local tagging and any real-marker test need a fresh one.
- **Connector:** `supabase-test` needs re-authorising via `/mcp`. ElevenLabs needs authorising in claude.ai connector settings.
