MRBADMUSAI · KS3 CLASS VIEW — AMENDMENTS
Delivery: 21 Aug 2026. Amendments to the live class-view file, not a redraw.

FILES
  ks3-class-view-bench-open.html   bench in its OPEN state (default view)
  ks3-class-view-bench-done.html   bench in its DONE state (default view)
      Both are the same surface, self-contained and offline: fonts, tokens
      and the design-system bundle are inlined. Every other state is
      reachable inside either file — the STATES bar (bottom right) toggles
      bench open/done, opens the flashcard stack, the recall round and the
      theme picker. The STATES bar is delivery-only: it carries
      data-port-ignore="1", drop it on port.
  README.txt   this file
  NOTES.txt    corrections, decisions and the work left to code
  source/      the editable component + design-system assets

CHANGED REGIONS  (data-port-region / data-port-change)
  bench                C1 theme · C3 done state
  bench-done           C3 new subtree
  bench-reward-slot    reserved, nothing drawn
  term-spine           C1 selected week tile
  sidebar-flashcards   C2 replaces the dark RECALL card
  flashcards-overlay   C2 new surface
  recall-round         C2b new surface, bench "Practise recall" lands here
  account-sheet        C1 the theme control lives here
  leaderboard          C1 card + week chips
  topbar               nav "Recall" item REMOVED
  data-port-ignore="1" STATES bar — delivery only

──────────────────────────────────────────────────────────────
1 · THE BENCH IS NO LONGER DARK
──────────────────────────────────────────────────────────────
The near-black ground is gone as a default, and no page chrome is
near-black any more. Page-chrome dark is now espresso #4A3728 (10.4:1 on
cream) — top rule, work-row and legend DONE dots. The week-selection
tile, the leaderboard card and its week chips take the bench theme, so
the whole page moves together.

PAGE TOKENS (unchanged KS3 set)
  ground #FBF3E6   card #FFFCF5   band #F4E9D8   inset #F7EFE1
  rule #E0D2B9     rule-strong #C3B191
  ink #221E1B 15.0:1   body #3B342E   muted #5F564F 5.9:1
  accent #E4572E graphic / 24px+   accent-text #A93411 6.0:1
  accent-hover #7F2408 8.8:1   tint #FCE7DE
  ok #12A150 (graphic)   ok-text #0A6B36   ok-tint #E4F7EB
  NEW  strong #4A3728 10.4:1

BENCH THEMES — switch is one attribute on the page root:
  data-bench-theme="harbour|clay|chalk|moss|damson|graphite"
  (absent = harbour). Token set per theme:
  --b-ground  --b-ink  --b-muted  --b-rule  --b-inset
  --b-ember (the accent at small size)  --b-cta  --b-cta-ink  --b-edge

  Contrast on that theme's ground: ink = body copy 18-20px,
  muted = small caps 11-12px, ember = small-caps accent.
  All AA or better; ink is AAA on every theme.

  HARBOUR — DEFAULT
    ground #20363F  ink #FBF3E6 11.48  muted #A9BFC6 6.60
    ember #F79E76 6.09  rule #37545F  inset #182B33
  CLAY
    ground #6B4A33  ink #FBF3E6 7.19   muted #E0CDB4 5.11
    ember #FFC4A6 5.16  rule #8A6849  inset #5B3D28
  CHALK (the light one)
    ground #EFE2CB  ink #221E1B 12.93  muted #6A5C4C 5.05
    ember #A93411 5.15  rule #D3BF9F  inset #E5D4B6
  MOSS
    ground #294036  ink #FBF3E6 10.14  muted #B4C6B6 6.22
    ember #F79E76 5.37  rule #42604F  inset #1F332B
  DAMSON
    ground #38243A  ink #FBF3E6 12.87  muted #C6AFC4 6.97
    ember #F79E76 6.82  rule #553855  inset #2C1B2E
  GRAPHITE (the old default, opt-in)
    ground #1A1512  ink #FBF3E6 16.44  muted #A99C8C 6.74
    ember #F0855C 7.08  rule #2F2823  inset #120E0C

ACCENT BEHAVIOUR ON A THEME (R1 held)
  #E4572E stays GRAPHIC only — the striped bench edge, the avatar ring,
  progress fills. It measures 2.6-4.9:1 on these grounds, so it never
  carries text and never sits behind small text.
  Small accent text uses --b-ember (5.1-7.1:1 on its own ground).
  Primary CTA: --b-cta #C0431C with #FFF7EC label = 4.69:1, plus a 1px
  --b-edge hairline so the button separates from the warm grounds.
  Chalk swaps the CTA fill to #A93411 (5.98:1).
  The docket stays paper #FFFCF5 + ink on every theme: the marking
  moment is deliberately theme-independent, so nothing competes with it.

WHERE THE CHOICE LIVES
  Account sheet — avatar or Settings in the top bar — section BENCH
  THEME: six swatches (each a miniature of the bench), one line of
  instruction, chosen one carries an ink outline and a drawn tick.
  No colour wheel, no free picker.
  Persistence contract for you to wire: student pref writes
  data-bench-theme on the page root. Nothing else changes.

──────────────────────────────────────────────────────────────
2 · FLASHCARDS  (replaced the dark sidebar Recall card)
──────────────────────────────────────────────────────────────
Sidebar card: stack-edged, themed, shows the CURRENT card's front and
NN / NN — so it doubles as a resume marker. Tapping opens the stack.
Overlay: 390px sheet, front 29px Bricolage readable with no scroll,
real flip (rotateY, 460ms; 1ms under prefers-reduced-motion),
Reveal / Hide + Next, progress pips, close.
Equation triangles are drawn as SVG. The word-equation arrow is SVG.
No meta-text explaining what flashcards are, anywhere.
"FROM YOUR WORK" chip renders on card.mine — the hook for the
wrong-answer targeting; it needs no redraw when that arrives.

──────────────────────────────────────────────────────────────
3 · THE BENCH'S DONE STATE
──────────────────────────────────────────────────────────────
Eyebrow THE WEEK'S WORK (no date). One line: "Good week, AY."
The checklist is resolved into one band on --b-inset: a single drawn
tick, OPENED · ANSWERED · COMPLETED, 3 / 3 — no ticked boxes staring
back at the student.
What it offers next: "Revisit this week's lessons" (primary, jumps to
the lessons panel) and "Practise recall" (secondary, opens the round).
Docket: SCORE / RIGHT / COMPLETED + "Read the feedback". The green
MARKED chip stays in the header band; the MARKED date row is gone.
Reward surface: data-port-region="bench-reward-slot", 64px, empty by
design — compositional room, nothing drawn.

──────────────────────────────────────────────────────────────
RECALL ROUND
──────────────────────────────────────────────────────────────
Reached from the bench "Practise recall" in BOTH bench states
(data-port-action="recall-round"). Rounds are unlimited: six questions,
then a round-end state offering "Another round"; nothing is handed in.
Flashcards and the recall round are separate products — the sidebar card
opens flashcards, the bench button opens the round, and the nav no
longer carries a Recall item (three doors became two).
States: unanswered / picked / checked-correct / checked-wrong / skipped
/ round complete. Marking always carries a word AND a drawn tick, never
colour alone (R2). The round takes --b-* like the bench, so it follows
the student's theme.

──────────────────────────────────────────────────────────────
TYPE, MARKS, BREAKPOINTS
──────────────────────────────────────────────────────────────
Display Bricolage Grotesque 700 (hero clamp 56-96px, bench title
clamp 38-60px, question clamp 30-44px). Body Instrument Sans 17-20px.
DM Mono 11-12px, .12-.15em tracking, for eyebrows, meta and numerals.
Minimum tap target 44px everywhere.
Ticks, chevrons, crosses, arrows and the equation triangle are inline
SVG: U+2713, U+2715 and U+2192 are never typed (the latin subsets do
not carry them).
No media queries for layout — flex-wrap plus minmax, so the port can be
embedded at any width. Reflow points: bench two-column -> stacked ~820px
(docket min 280px); work list / sidebar -> stacked ~980px; stat strip
wraps 4-2-1 from ~700px; spine tiles wrap freely; recall two-column ->
stacked ~900px. The flashcard sheet is a fixed 390px, full-bleed below.

STATE PLUMBING (for the porter)
  Every selected/active state is expressed as a data attribute that sets
  a CSS custom property the inline style reads:
    .wk[data-sel]        week tile      --wk-fill / --wk-edge / --wk-line
    .tab[data-on]        work filter    --tab-bg / --tab-ink / --tab-shadow
    .lbchip[data-on]     leaderboard    --lb-bg / --lb-edge / --lb-ink
    .pip[data-on]        progress pips  --pip-bg
    .sw[data-on]         theme swatch   --tick-o
    .opt[data-st]        recall option  --opt-bg / --opt-edge / --opt-mark-*
  Bind your data to the attribute; the styling follows.
