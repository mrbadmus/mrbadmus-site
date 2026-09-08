# MRB-336 / MRB-337 — five minutes on your phone

Everything below is on the live site. If any step does not do what it says,
stop there and tell me which number — I would rather fix it than have you work
around it.

---

## 1. Papers on a triple class (10 seconds)
Open a triple class — **11h/Ph1** — and tap **Set work**.
✅ You should see **Paper 1 · Paper 2 · Both** chips, the same as a combined class.
This is the "simple fix" — it was one line that said triple classes get no papers.
Tap **Paper 2** and you should see Space; tap Paper 1 and it should be gone.

## 2. Your three assignments from this morning
Open **8r/Sc1** as a pupil, or check the class page.
✅ All three of your sets are **live now**, not waiting for 14 September.
They were stored with a release time of midnight on the 14th because the
school hold was overriding what you chose. That is gone.
⚠️ They were also **filed under next week**, which is why releasing them alone
would not have been enough — the pupil's page only lists the current week's
work. Both were repaired.

## 3. Set work and see it arrive (2 minutes) — the main event
On **8r/Sc1** → **Set work** → pick anything → **Release now** → set it.
✅ Your test pupil sees it **immediately**, even though the hold still says
14 September.
✅ The **bell** on their page shows **1**. Tap it: the message says **New work**.
✅ The class page shows it as **its own card**, with its own "N of M in" and its
own **Remind all** — not folded into a "+2 more" line.

## 4. The hold still works where it should
The 14 September hold is untouched and still stands. What changed is what it
governs: it now holds back only the **automatic weekly** assignments. Work you
set by hand goes when you say it goes.
✅ Nothing you do in step 3 makes automatic work appear early.

## 5. Edit it
On that assignment's row, tap **Edit**.
✅ It opens with everything filled in. Change the due date. **Save**.
✅ Toast reads `<title> · Saved` and the row updates without a reload.
Note: because it is already released, you can change the **title and due date
only**. Before release you can change everything, including the questions —
that split is deliberate, so a pupil who has started never has the questions
change underneath them.

## 6. Delete it
On the same row, tap **Delete**. The controls become **Delete · Cancel**.
Tap **Delete** again.
✅ Row goes. Toast reads `<title> · Deleted`.
✅ Your test pupil no longer sees it — not on their page, not in the bell, not
in the banner.
Marks and submissions are kept. Automatic weekly work shows no Edit or Delete
at all, on purpose.

## 7. Scheduled work reads as Scheduled
Set one more with **Release later**, a date in the future.
✅ The Assignments table says **Scheduled**, not Open, and the **Set** column
shows the release time it will actually go live at.
This was the wrong bit in your screenshot: three assignments no pupil could see
were all showing as OPEN.

---

## Two things I want to flag, not bury

**Someone else can delete your work.** Any teacher on a class — plus school
admins — can delete or edit work set by a colleague on that class. Every delete
is recorded in the audit log with who did it and how many pupils had submitted.
I did not restrict it to the person who set it, because on a co-taught class
that would block the cover teacher. Say if you want it narrowed.

**A pupil mid-attempt when you delete.** If you delete work while a child has it
open, their next answer fails rather than showing "your teacher withdrew this".
Answers already saved are kept. Building a proper withdrawn state is a small
piece of design, not a bug fix, so I have left it for you to decide.
