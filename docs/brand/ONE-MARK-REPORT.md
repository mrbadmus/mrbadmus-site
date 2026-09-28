# One mark — run report (27–28 Sep 2026)

**The ruling (Mide, 13 Sep 2026).** ONE mark everywhere: a forward double
chevron (front solid, back faded) + the wordmark **"MrBadmus"** — "AI"
dropped. Identical on every page (pupil, public, staff, consumer) and in every
email. The only variant is light-on-dark. Octopus and ⚗️ alembic retired.
Teacher worksheets (PDF/DOCX) keep the chevron alone.

**Outcome.** Every published page now wears one lockup, drawn by one module
(`brand.py`) from Design's kit. The gate `brand_one_mark` (fast, on every
push) makes a second mark impossible to ship. The rendered proof
(`brand_fingerprint.py`) counts **1 distinct mark across 39 page families**,
light and dark, 360 px and 1280 px — locally and on the live site (§6).

---

## 1. Before → after, per page family

Measured on the live site before the swap (`brand_fingerprint.py --base
https://mrbadmus.com`, light, 1280) — **12 distinct fingerprints**, which read
as nine real marks (the staff rows differ only because a text-only wordmark
sat beside the theme control's icons, and two signed-in pages redirected to
auth.html):

| family | before | after |
|---|---|---|
| landing, GCSE hub, pathway, tier, subject hub, topic (KS4 chrome) | Design double chevron, **halves mirrored**, "MrBadmusAI" Bricolage 800 | one mark |
| KS4 classic lessons (~900), auth, leaderboard, past papers, weekly challenge, my challenges, revision, profile setup, reset password, 404 | gold-to-rust gradient chevron, "MrBadmusAI" Fraunces 600 (reset-password: a second hero variant) | one mark |
| KS3 hubs, units, lessons (297) | single **upward** chevron, "MrBadmusAI" Bricolage 800 | one mark |
| KS4 pilot lessons (54) | white chevron in an orange tile, "MrBadmusAI" 800 | one mark |
| student class page, 3D Studio | Design BrandMark, **halves mirrored**, "MrBadmusAI" 600 | one mark |
| student assignment | BrandMark on wide screens only | one mark on wide screens; none on phones, by ruling (§5) |
| teacher (generated + hand-written), student classes/settings/claim, teacher profile | plain-text "MrBadmusAI", no logo | one mark |
| consumer, parents, go | hand-copied chevron, **halves mirrored**, "MrBadmus" 800 | one mark |
| org, org sign-in, consumer admin consoles | "MrBadmus" wordmark, no chevron | one mark (cream, `on_dark`, on the dark admin consoles) |
| favicons | three data: URIs (KS3 upward chevron on 1,293 pages; two double-chevron variants) | the kit's `mrbadmus-favicon.svg` + app icon, every page |
| shared-link card | mirrored chevron, wordmark 800 | redrawn from the partial (`brand_cards.py`) |
| worksheets (PDF + DOCX) | chevron only, **halves mirrored** | chevron only, as the kit draws it (backend `7cce2d0`) |

After (local build, `--expect-one`, light/dark × 360/1280): **1 distinct mark
— `[8ecf26fc6d] "MrBadmus" Bricolage Grotesque 600; svg 0 0 22 22 ×2` — across
39 families**, wordmark ink on light grounds and cream on dark, ≥ 4.5:1
against the ground it actually sits on. `brand_one_mark`: 1,332 pages, 0
violations.

**Root cause worth knowing.** Four of the old marks were "byte-for-byte copies"
of one another, each made in good faith, and three of them had the solid and
faded chevrons swapped relative to Design's kit. The worksheet inherited the
mirror from one of them. That is why the mark now has exactly one drawing and
a gate that refuses any other.

## 2. The one source

| | |
|---|---|
| Design's kit (untouched originals + *Brand Mark* sheet) | `docs/brand/source/` |
| Published copies, `<metadata>` stripped (~8 KB → ~0.5 KB each) | `shared/brand/` |
| The partial | `brand.py` — `brand_lockup()`, `brand_head()`, `stamp_brand()`, writes `brand.js` |
| Styling | `shared/brand/brand.css` (21/19/5 phone, 23/21/6 ≥ 720 px; Bricolage 600) |
| JS-drawn headers | `shared/brand/brand.js` → `window.MrBadmusBrand.lockup()` (generated) |
| Compiled student/teacher ports | `brand_port.py` `replace_brand_run()` + `RULED_BRAND` in `student_rulings.py` / `teacher_rulings.py` |
| KS4 pilot | `ks4_rulings.py` R-BRAND |
| 3D Studio | `TopBar.tsx` renders `MrBadmusBrand.lockup()`; `vite.config.ts` stamps the brand links |
| Email lockup PNG, shared-link card | `brand_cards.py` (drawn from the partial in headless Chrome) |

Kit md5s (originals in `docs/brand/source/`):

```
be4cdd40dc6a009011dea95ad5186391  mrbadmus-app-icon-dark.svg
9b1ca5545668c53faa5fc683aff8e20d  mrbadmus-app-icon-light.svg
36f88510e005e51799983d275d3c29d6  mrbadmus-chevron.svg
65aba4776f456dc56fffd21a8d39f697  mrbadmus-favicon.svg
6e02e35fdb35eb3e4ffca6a1df4dfdb3  mrbadmus-lockup-dark.svg
ad0eab7842f33c639e0a1b9f48bfc0e2  mrbadmus-lockup-light.svg
2d8b7f78b83dc9bbc297bd0cc0b8c8eb  files/mrbadmus-icon-dark-512.png
cffd3cc4dc8ec287edb2a9145f0b6a32  files/mrbadmus-icon-light-512.png
bf21a2a52a3ca17e0a58841a1baad1b4  files/mrbadmus-logo.png (= mrbadmus-logo-light.png)
```

Shipped (stripped) copies: chevron `767412ae…`, favicon `414f7a61…`,
app-icon-light `16d94ead…`, app-icon-dark `2571104c…`, lockup-light
`0862e73c…`, lockup-dark `82ae485d…`; PNGs byte-identical to the kit.
`brand_one_mark` re-derives every stripped copy from its original on every push.

## 3. Emails

**Changed (in this repo):** `supabase/functions/account-claim-request/index.ts`
— sender "MrBadmus <noreply@mrbadmus.com>", subject and heading without "AI",
and the lockup image (`/shared/brand/mrbadmus-lockup-light-email.png`, live) at
the top. ⚠️ **Not deployed** — an edge function ships only with
`supabase functions deploy account-claim-request` against production, and this
run had no production credential (and was not to write to production). Until
someone runs it, that email keeps the old wording.

**Listed, not edited:**

1. **`consumer/email.js` in the backend repo (B2C lane).** Every consumer
   email (welcome, child login details, trial ending, payment failed,
   subscription cancelled, marked, new messages, account deletion, ops digest,
   digest). The header at ~line 257–259 is the plain word "MrBadmus" in a
   `<span>`. Change it to:
   ```html
   <img src="https://mrbadmus.com/shared/brand/mrbadmus-lockup-light-email.png" width="160" height="30" alt="MrBadmus" style="display:block;width:160px;height:auto;border:0;outline:none;text-decoration:none;">
   ```
   and rewrite the comment at lines 24–29, which says the wordmark is "the
   plain word MrBadmus, as text, with no image". `FROM` (line 31) is already
   "MrBadmus". The image is live, so this can ship any time.
2. **Supabase Auth email templates (dashboard, not in any repo)** — Supabase
   dashboard → project `urklkrwevjtlfbwnipjn` → Authentication → Email
   Templates: *Confirm signup*, *Invite user*, *Magic link*, *Change email
   address*, *Reset password*, *Reauthentication*. For each: replace any
   "MrBadmusAI"/"Mr Badmus AI" with "MrBadmus", and put the same `<img>` as
   above at the top of the body. Also Authentication → SMTP settings →
   *Sender name*: "MrBadmus". (Not inspected — this run had no dashboard
   access; check each rather than assume it names the brand.)

**Worksheets (backend, live):** `worksheet.js` — `MARK_FRONT` is now the
right-hand chevron (solid) and `MARK_BACK` the left (0.34), matching the kit;
back painted first. `test_worksheet.js` 731 passed / 0 failed. Pushed as
backend `7cce2d0`, confirmed by `/api/health` reporting that build.

## 4. Tutor-name labels left for Mide

These name the AI **tutor** as a feature, so they kept their wording (the
ruling covers the brand in chrome, titles and meta):

- `generate_site_v5.py` — chat button `title="Ask MrBadmus AI"` / text "Ask MrBadmusAI" (~951); chat header `<h3>Mr. Badmus AI</h3>` (~957); "Ask Mr Badmus AI" (~1712, 1716, 4012, 4016, 4358, 4361, 4556, 4560, 5034); "Ask Mr Badmus AI below for a worked FIFA example…" (~1960); "what Mr Badmus AI is here for" (~3900); "Stuck · ask Mr Badmus AI" (~5030); "Ask MrBadmusAI" (~5298).
- `build_ks3.py` — chat header `<h3>Mr. Badmus AI</h3>` (~408); placeholder "Ask Mr Badmus anything about this lesson" (~421); "Stuck? Ask Mr Badmus AI" (~4182). About 184 lesson-specific prompts in `ks3_data/` are content and untouched.
- KS4 pilot — Design's `Ks4End.dc.html:33` `<h2>Ask Mr Badmus AI</h2>`.
- `shared/mrbadmus.v2.js` — the tutor's system prompt ("You are Mr. Badmus AI…", lines 50, 67) and `aria-label "Ask Mr Badmus"` (330).
- `teacher/classes.html:67` (hidden empty state) "…want to explore Mr Badmus AI?"; `teacher_rulings.py:8305` "Not used by Mr Badmus AI".

Also left, because they are **body copy using the site's name**, not chrome —
your call whether they become "MrBadmus":
- `weekly-challenge.html:199` "You need a free MrBadmusAI account to compete."
- `profile-setup.html:396` "Welcome to MrBadmusAI"
- `student/settings.html:347` "Manage your MrBadmusAI account." and `:367` "Used MrBadmusAI before with a different email?"
- `build_ks3.py:4126` "Lesson content © MrBadmusAI." (a legal-ish line — left as legal text)
- Design's frozen KS4 pilot templates keep "· MrBadmusAI GCSE …" in a compiled `<title>` node that is never rendered (the page's real `<title>` is "… | MrBadmus"); changing it would break the content freeze hash.

## 5. Decisions I made

- **Wordmark weight 600, not 800.** Design's MANIFEST says "Bricolage 800"; her kit's lockup SVGs draw 600 and her *Brand Mark* sheet lists "Wordmark in anything but Bricolage Grotesque 600" as a don't. The kit wins.
- **The kit's orientation wins over every copy.** The kit's back (left) chevron is the faded one. Four in-repo copies and the worksheet had it the other way round; all now follow the kit.
- **Staff pages get the full mark.** The kit's sheet still says staff surfaces keep the wordmark-only rule; the 13 Sep ruling says identical on every page, staff included. The ruling wins.
- **The kit's lockup SVGs and logo PNG are shipped but not used on pages or in emails.** The lockup SVGs clip the final "s" of "MrBadmus" when Bricolage actually loads (the 120-unit viewBox is too narrow); the logo PNG is not set in Bricolage. Pages use the partial; the email PNG is drawn from the partial. **For Design:** widen the lockups' viewBox (~132) and re-export the PNG in Bricolage 600.
- **Head tags**: every page gets the kit favicon, the kit's light app icon as `apple-touch-icon`, and `og:site_name` "MrBadmus" where pages carry OG tags. No new OG *images* were added to school-side pages (none had one); the one existing card was redrawn.
- **Chat button icon** is a neutral speech bubble in the button's text colour, not the mark: the button fill is rust (light) / gold (dark), on which the orange chevron cannot read, and on phones the button is icon-only.
- **Student assignment page shows no mark below Design's wide breakpoint.** Design draws it as an exam task bar (back link, class, clock, HANDED IN); at 360 px the lockup would push the clock off-screen. No mark is not a second mark; `brand_fingerprint.py` reports it as "ruled", never as a pass. Reasoning beside `RULED_BRAND` in `student_rulings.py`.
- **KS4 pilot brand link** now goes to `/index.html` like every other page (it went to `/ks4.html`).
- **`/go/` and consumer `today.html`** had an unlinked brand; the lockup is always a link, so on those two child-facing pages it points at the page itself rather than out to the public site.
- **Consumer admin consoles** are dark in both themes, so they carry `on_dark` (cream wordmark).
- **Titles**: "… | MrBadmus" everywhere; KS3 "… | KS3 | MrBadmus"; KS4 pilot "… | GCSE Chemistry | MrBadmus".
- **Cache-busting**: `/shared/*` is served immutable for a year, so every brand asset link is `?v=md5[:8]`-stamped — including `brand.js` on hand-written pages and the 3D Studio (stamped in its own Vite build, because the generator must publish `3d-studio/dist` byte for byte).
- **Gates changed** (none weakened; each cites the ruling): `ks4_chrome_drive` (now also asserts which chevron is faded and the 600 weight), `night3_selfreview` (any chevron on a staff surface must be byte-for-byte `brand.MARK_SVG`, and org pages must carry it), `ks3_parity` (brand rows re-pointed to `.mrb-brand`), `3d_parity` + `3d_render_check` (brand rows re-pointed; serve `/shared/` like production), `student_behaviour` (the "AI" removal and the assignment label declared through its own divergence mechanisms).
- **Adjacent defect fixed:** `parents/public.css` — the sign-up rail stayed cream in dark theme, making the wordmark and step labels invisible.

## 6. Landing and live proof

**Commits.** Unit 1 (kit + partial + tools) `3a50ca3c2`, live 27 Sep 00:52.
Unit 2 (every page) `54f36956f` with lane merges, then three merges of
`origin/main` (the theme run kept landing: Set-from-class, dark-audit fixes,
re-check fixes, its report) — pushed as **`9e3396053`** on 28 Sep. Backend
worksheet fix `7cce2d0` (live, `/api/health`).

**Gates at the push** (`prepush_gate.py`, `MRB_BACKEND` pointed at a fresh
backend worktree; credentials exactly as `docs/mrb335/RISKS.md` E6 —
`MRB_SET_WORK_PASSWORD`, `MRB_THROWAWAY_PASSWORD`, `MRB_TEST_TEACHER_PASSWORD`;
`MRB_DRIVE_PASSWORD` / `MRB_TEST_STUDENT_PASSWORD` never set): 31 fast gates
ran fresh, 30 slow gates passed on receipts, 4 skipped by rule, 2 skipped for a
missing precondition (`student_controls_drive`, which needs the forbidden
credentials, and one other). Two red, both pre-existing and declared with
`GATE-OVERRIDE` in the tip commit: `3d_parity` (three token/border rows,
proved red on `origin/main`) and `set_work` (452/455; the three standing TEST
small-pool data checks, recorded red by the Set-from-class landing too).
`brand_one_mark` is registered as a fast gate and green.

**Live bytes.** 19 pages across every family fetched from mrbadmus.com are
**byte-identical** to the committed build (landing, KS3 hub, a KS4 lesson,
teacher today and all six generated teacher screens, parents, leaderboard, 3D,
auth, student class and assignment, consumer signup, org, go). Every brand
asset link is `?v=`-stamped from its own bytes — `brand.css?v=9c818614`,
`brand.js?v=a8b2a506`, `mrbadmus-favicon.svg?v=414f7a61`,
`mrbadmus-icon-light-512.png?v=cffd3cc4` — and the live files' md5s match.

**Live rendered proof** (`brand_fingerprint.py --base https://mrbadmus.com
--themes light,dark --widths 360,1280 --expect-one`): **1 distinct mark across
39 families**, exit 0; the wordmark ink on light and cream on dark, ≥ 4.5:1 on
its real ground; student assignment at 360 reported as ruled. Two honest
footnotes: the two generated teacher screens are measured on their fixtures,
which are not published — on the live run those rows had served the 404 page
(the script now refuses to count a 404), so their live proof is the byte
match above plus the local rendered run on identical bytes; and the consumer
admin console redirects a signed-out browser to its sign-in, so its `on_dark`
variant was verified locally by lane C.

**Screenshots:** `$MRB_SHOTS` = `~/tmp/one-mark-shots/` — `live/` (every
family, light/dark × 360/1280: `mark-*.png` crops and `page-*.png` viewports),
`before-live/` (the old marks), `after-local/`, `worksheet/` (PDF/DOCX
before/after).

## Deviations

- The theme run (Prompt J) landed on `main` without ever writing
  `docs/theme/REPORT.md`, which this run's instructions named as the signal.
  The watcher keyed to that file never fired; ~21 hours passed before the
  header work started. Deviation: waited for a report file → should have
  checked for the theme code itself → cost time, not correctness.
- `3d_parity` was already red on `main` (three token/border rows, none brand);
  proved by building `origin/main`'s studio and running `origin/main`'s gate.
  Shipped with a `GATE-OVERRIDE` line naming it.
- The main backend checkout is stale (missing `figures.json`,
  `@resvg/resvg-js`); gates were pointed at a fresh detached backend worktree
  via `MRB_BACKEND`/`MRB_BACKEND_DIR` instead.
- Pre-existing, not caused here: the nav on `student/classes`,
  `teacher/seating`, `teacher-profile` already overflows at 360 px (measured
  old vs new: 409 vs 416, 442 vs 441, 489 vs 496 px); `org/sign-in.html`'s
  floating theme control overlaps the "For organisations" chip at 360 px;
  3d-studio `tier-override.test.tsx` fails 3/3 on `main`.
