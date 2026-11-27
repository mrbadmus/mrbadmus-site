# Sandbox class moved — every live check repointed and guarded (27 Nov 2026)

8r/Sc1 (`d9740ab8-c4e3-4c22-bce9-629b650782c5`) became Mide's real Year 8
class on 16 Nov 2026. The production sandbox is now **"Test class (Mr Badmus)"**
(`e8eb5833-fa52-4d01-9ff6-678145ee48c7`). This run made sure no script can
write to 8r/Sc1 again, and that every live check uses the new class.

## What changed

| file | change |
|---|---|
| `sandbox_class.py` (new) | The ONE place the sandbox id is named, plus the guard. `assert_writable()` refuses the retired 8r/Sc1 id on any project. On production it also refuses any class that cannot prove, from the database, that it has at least one pupil, only the two test pupils, and no teacher but Mr Badmus. It fails closed: no key, or an unreadable read, means refused. `guard_request()` applies the check to every class a write names. |
| `student_submit_drive.py`, `student_api_drive.py` | Defaulted to the old 8r/Sc1 id. Now default to `sandbox_class.SANDBOX_CLASS_ID` and run `assert_writable()` before anything else. |
| `tools/mrb351_acceptance.py` | The shared client that 16 live tools use. `Client._req` now runs `guard_request()` on every write. |
| `sandbox_class_check.py` + `gate_registry.py` | New fast gate, `sandbox_class` (run on every push). |
| `CLAUDE.md` (both repos) | New section, "The production sandbox class". |
| `docs/golive/dry-run.md`, `docs/golive/monday.md`, `docs/mrb335/mide-live-check.md`, `docs/mrb342/mide-live-check.md` | Mide's own runbooks told him to set work on 8r/Sc1 on production. Every such step now names the test class, under a dated banner. |
| `docs/ks3/pending-cleanup.md`, `docs/wrapped/PLAN.md`, `docs/experience/REPORT.md` | Dated note: 8r/Sc1 is no longer the sandbox. The Wrapped preview note now excludes all of 8r/Sc1's real pupils and teachers. |

## Every reference, and why the rest are harmless

- **Code that held the class id:** only the two drives above, now repointed. No
  tracked script outside `sandbox_class.py` spells either id, and the gate
  keeps it that way.
- **Drives that pick a class by name or take the first one:** none of them
  write to production. `mrb348_teacher_equiv.py`'s "first class" case is a
  read-only page check against the TEST seed (class 8X1). The `tools/*_live.py`
  scripts look up a *subject* by name, build their own throwaway class on TEST,
  and refuse any key that isn't TEST.
- **`tools/mrb351_set_from_class_live.py`, `flashcard_progress_drive.py`,
  `set_work_drive.py`:** these already use fixture classes on TEST. The first
  one's comment ("Production's sandbox 8r/Sc1 does not exist on TEST") is out of
  date but harmless. All three are covered by the shared guard or the gate.
- **"8r/Sc1" as a display label:** in Design's templates, `student_rulings.py`,
  `build_student_port.py`, the teacher fixtures, `today_drive.py`,
  `week_truth_fixture.py`, `week_scope_check.js` and `admin_view_drive.py`. These
  all use fixture ids (`cccccccc-…`, `f3530000-…`) or no id at all. They never
  touch a database, and no check compares them with live data. Left alone.
- **Supabase migrations and data-ops SQL:** historical, already applied. Left alone.
- **Backend:** three `server.js` comments describe old measurements. No backend
  script writes to a class by id.
- **8r/Sc1's real timetable or co-teacher:** no drive depends on either. The
  co-teacher and timetable cases in `today_drive.py` and
  `teacher_admin_foreign_class_drive.py` are made-up fixtures.

## Proof

**On TEST (Supabase project `qeppkiswvclkkwbxmlok`).** I created three
throwaway classes: one sandbox-shaped (only the test pupil), one with the test
pupil plus a non-test pupil, and one empty. I read them with the guard's own
membership query (`sandbox_class.membership_sql`) and fed the rows to
`decide()`. Output: `docs/sandbox/test-proof-output.txt`.

- sandbox-shaped class → **ALLOWED**
- class with a non-test pupil → **REFUSED**, with the class named
- empty class → **REFUSED**
- the 8r/Sc1 id → **REFUSED** (retired)

Everything was then deleted, including a temporary TEST profile row the test
pupil needed in order to join a class. A follow-up count showed nothing left
behind.

**Production, read-only, nothing written.** Membership read on 27 Nov 2026:

- 8r/Sc1: 30 pupils, none of them test accounts; teachers Mr Badmus and
  V. Ellingham; 0 assignments. The guard → **REFUSED**.
- Test class (Mr Badmus): exactly the two test pupils; Mr Badmus only;
  11 assignments. The guard → **ALLOWED**.

**The gate.** `sandbox_class` passes 6,734 checks. A deliberate break of each
kind turns it red: removing the guard call from a drive, and a probe file
spelling the retired id.

## Not done in this run

- No live drive was run against production, and nothing on production changed.
- The guard's HTTP read, `fetch_membership`, was not run live. This container
  has no service key for either project. The same read was run as SQL through
  the connector instead, and the gate checks that the two versions apply the
  same filters.
