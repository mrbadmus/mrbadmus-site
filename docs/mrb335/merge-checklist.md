# MRB-335 — merge checklist

Run in order. Every step is a thing to OBSERVE, not a thing to assume; where a
step can pass for the wrong reason, the wrong reason is named.

PLAN §6 step 7 is the source of the ordering. Backend first, because the site's
sheet calls routes that must already answer; a site deployed first would give
every teacher a sheet whose every request 404s.

---

## 0 · Before anything

```bash
df -h /System/Volumes/Data          # under 700 MB free → stop
cd <site worktree>     && git status --short   # nothing of yours modified
cd <backend worktree>  && git status --short
```

⚠️ **Gate receipts bind to a TREE, not to a branch.** Run the slow gates ONCE,
on the final tree, after the last commit (RISKS E5). A single late byte —
including a `?v=` restamp — invalidates every receipt taken before it.

---

## 1 · Backend → Render

```bash
cd <backend worktree>
node test_set_work_v2.js            # the pure half; expect 0 failed
git push origin feat/set-work-v2    # (or merge to main per the merge plan)
```

Wait for Render to say **Live**. Then:

### 1a · `prod_401_unauth` — the five routes refuse an unauthenticated caller

⚠️ **THIS IS THE STEP MOST LIKELY TO PASS FOR THE WRONG REASON.** A route that
does not exist answers **404**, and a 404 is not a 401 — but read quickly, both
are "not 200" and both look like a refusal. A deploy that silently did not
carry the new routes would produce five 404s and a tick. So the check is on the
**exact status**, and a 404 means the deploy did not land rather than that the
route is safe.

```bash
API=https://mrbadmus-backend.onrender.com

for R in \
  "GET  /api/teacher/set-work/scope?class_id=00000000-0000-0000-0000-000000000000" \
  "GET  /api/teacher/set-work/preview?class_id=00000000-0000-0000-0000-000000000000&tier=foundation&scope_kind=topic&scope_ref=ecology" \
  "GET  /api/teacher/set-work/swap?class_id=00000000-0000-0000-0000-000000000000&tier=foundation&scope_kind=topic&scope_ref=ecology" \
  "POST /api/teacher/set-work" \
  "POST /api/admin/class-tier" ; do
  M=${R%% *}; P=${R#* }; P=${P##* }
  printf '%-4s %-92s ' "$M" "${P:0:92}"
  if [ "$M" = POST ]; then
    curl -s -o /dev/null -w '%{http_code}\n' -X POST -H 'Content-Type: application/json' \
      -d '{}' "$API$P"
  else
    curl -s -o /dev/null -w '%{http_code}\n' "$API$P"
  fi
done
```

**Expected: `401` five times.**

| What you see | What it means |
|---|---|
| `401` | Correct. The route exists and refuses an anonymous caller. |
| `404` | ⚠️ The deploy did NOT carry these routes. Do not proceed. |
| `400` | ⚠️ The route is answering on the BODY before checking the caller — a validation error is being disclosed to someone who is not signed in. Stop and report. |
| `500` | ⚠️ Usually a missing `SUPABASE_ANON_KEY` on Render: the standing check runs the caller's own JWT through `auth_user_has_scope` and cannot without it. |
| `200` | Stop everything. |

And the negative control, so a run of five 401s is not a firewall being clever:

```bash
curl -s -o /dev/null -w 'health %{http_code}\n' "$API/api/health"    # expect 200
```

A 401 on `/api/health` too means something in front of the app is refusing
everything, and the five 401s above said nothing about the routes.

---

## 2 · Migrations, one at a time, on PRODUCTION

⚠️ **Only at merge.** "Additive and unread" is not a reason to apply early —
MRB-322 put an RLS hole on production for an hour on that reasoning, and both
its excuses were true at the time.

```
20260907211144_mrb335_assignments_scope.sql
20260907211350_mrb335_classes_tier_rule.sql
```

Apply the first, read the row counts it prints, then the second. Each has a
rollback pair in `supabase/rollbacks/`.

After the second, the backfill's own numbers are the thing to record:

```sql
select tier_pathway_source, count(*) from classes
 where key_stage = 'KS4' group by 1 order by 1;
```

⚠️ Rainford has 38 KS4 classes and **36 of them carry no tier and no pathway**
(MRB-332). Expect a large `null` bucket. That is the roster, not a failed
backfill — the trigger fills on INSERT and these rows already exist.

---

## 3 · Content load on production, then checksum

```bash
python3 tools/export_ks4_questions.py --verify
python3 -m ks3_data.question_bank            # its own _cap_test
python3 set_work_scope_check.py --db         # against PROD once loaded
```

⚠️ `set_work_scope_check --db` reads `MRB_BACKEND_ENV`'s `.env`, which points
at TEST by default. Point it at production deliberately, and only for a read.

Record the smallest cell per key stage and the floor result in the report.

### 3a · anon cannot read either bank (RISKS D9)

```bash
curl -s -H "apikey: $PROD_ANON" \
  "$PROD_URL/rest/v1/ks4_assignment_bank?select=id&limit=1"
curl -s -H "apikey: $PROD_ANON" \
  "$PROD_URL/rest/v1/ks3_assignment_bank?select=id&limit=1"
```

Expect `[]` — both tables are `authenticated`-SELECT only. A row coming back is
the whole question bank readable by anyone with the page source.

---

## 4 · Site → Cloudflare Pages

```bash
cd <site worktree>
python3 build_all.py                # NOT generate_site_v5.py — it skips five generators
git status --short                  # the restamps must be committed
git push origin feat/set-work-v2
```

### 4a · the stamp, proved with `cmp` and not with `grep`

⚠️ **Read the page map FIRST, then the asset with a nonce.** Polling a stamped
URL *before* its deploy pins the stale bytes for a year under `_headers`'
`immutable`, and every later fetch — yours and every student's — is served the
wrong file from cache with a 200.

```bash
curl -sL https://mrbadmus.com/teacher/class-detail.html -o /tmp/cd.html
V=$(grep -o '"set-work\.js":"[0-9a-f]*"' /tmp/cd.html | head -1 | cut -d'"' -f4)
echo "live stamp: $V"
curl -sL "https://mrbadmus.com/shared/set-work.js?v=$V&nonce=$RANDOM" -o /tmp/live.js
cmp /tmp/live.js mrbadmus_site/shared/set-work.js && echo "byte-identical"
```

`curl -sL`, not `curl -s`: Pages answers `.html` with a 308.

---

## 5 · Re-read production as a person

- Open a real class's Set work sheet at 390px. Tier chip on the class's tier;
  counts beside every topic; a topic taps without the list jumping.
- Set one small piece of work to one class. Check the toast, then the class
  card, then the child's page.
- **Delete it again.** A merge-check assignment left on a real class is
  homework a real child sees.

---

## 6 · What to write down

- the five statuses from 1a, and `/api/health`;
- the backfill's `tier_pathway_source` counts;
- the checksum from 3, and the smallest cell per key stage;
- the live stamp and the `cmp` result;
- the id of anything set on a real class in step 5, **and its deletion**.
