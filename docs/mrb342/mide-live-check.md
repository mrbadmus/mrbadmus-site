# MRB-342 — the five-minute check, for Mide

⚠️ **Do this only after the site half is merged and live.** The backend is
already on production; the sheet is not. Until then the `Download` control does
not exist on the page.

Sign in as yourself. Open **teacher → Classes → 8r/Sc1 → Set work**.

---

### 1 · Pick a topic (about 1 minute)
Choose a topic, a tier, and let it pick the questions. You land on **Detail**.

**Look for:** the questions listed, count chips beside each, a `Swap` on each
row. Nothing should have moved on the page when you tapped a chip — if the list
jumps back to the top, tell me, because that scroll-jump is the exact bug the
sheet is built outside the compiled runtime to avoid.

### 2 · Add a second topic (about 1 minute)
Tap **`Add topic`**. You go back to the Topic step.

**Look for:**
- the **tier is locked** to the one you already chose — you should not be able
  to pick Foundation questions into a Higher set;
- only topics from **this class's own curriculum** are offered;
- back on Detail, the two topics appear as **separate sections**, each with its
  own count and its own rows.

### 3 · Download a PDF — WITHOUT setting the work (about 1 minute)
Tap **`Download`**, choose **`PDF`**.

**Look for:**
- a PDF in your Downloads;
- the header: title, **8r/Sc1**, the tier, today's date;
- questions numbered, options **A–D**;
- **no question split across a page break**;
- a final **`Answers`** page — number and letter, plus the answer text, and
  **no explanations**;
- the footer: **MrBadmusAI** and a page number;
- ⚠️ **`CO₂` should have a proper small 2** at KS3. If you see `CO2` on a KS3
  question, or a blank box or a strange glyph, tell me — that is the bundled
  font not doing its job. **On a KS4 worksheet flat `CO2` is CORRECT and
  deliberate**, because there `N2` means Newton's second law.

**Then check nothing was set:** go back to the class's assignment list. **There
should be no new assignment.** A download is not a set, and that is the single
most important thing on this page to get right.

### 4 · Word (about 30 seconds)
Tap `Download` again, choose **`Word`**. It should open in Word with the same
content. ⚠️ It will be about **390 KB even for a short worksheet** — the font
travels inside the file. That is expected, not a fault.

### 5 · Now actually set it, and download from the row (about 1 minute)
Set the work. On the assignment row that appears, tap **`Download`**.

**Look for:**
- the row turns into `PDF / Word / Cancel`, and **only that row does**;
- `Cancel` puts it back;
- the same file comes out;
- the row says **`Set by <your first name>`**.
  ⚠️ On a **colleague's** assignment that line will be **absent**, not blank and
  not a long code. That is deliberate — a teacher has no permission to read a
  colleague's profile, and showing nothing is better than showing a raw id.
  Tell me if you would rather it said something.

---

## If anything is wrong
Tell me **which step**, and what you saw instead. The two that matter most:
**a download that creates an assignment**, and **an answers page on a worksheet
you meant to hand out**. Either of those, stop and tell me before using it with
a class.
