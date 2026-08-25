# Chemistry audit — morning summary — 25 Aug 2026

Morning Mide. Yesterday ten auditors went through all 57 chemistry lessons on
the live site, twice each — once reading as a Year 7/8 student on a phone,
once reading as an AQA examiner. They pressed every button, ran every
simulation, and answered questions wrong on purpose. Here is what it comes to.

## The verdict

**Chemistry is not September-ready today — but it is genuinely close.** One
sitting of decisions from you, a few days of fixes from Code, and a small
batch of redrawn diagrams gets it there. Nothing needs rebuilding. In fact
the auditors kept saying the same thing independently: the teaching writing
and the interactive experiments are the best they have seen at this level.
C5 (types of reaction) and C10 (Earth and atmosphere) came back nearly
spotless.

We found 106 issues in total. Most are small — a wrong word, a mislabel, a
missing sentence. The ones that matter:

## The handful that genuinely matter

1. **The catalysts lesson teaches an experiment that isn't true.** The
   "fifth flask" says dilute acid speeds up hydrogen peroxide breaking down.
   It doesn't — acid actually slows it. Any teacher who runs this for real
   gets the opposite of what the page says, and two quiz-bank questions
   repeat it as fact. This is the biggest single item.
2. **A reactivity series is printed in the wrong order.** In the metals unit,
   lesson 2's list puts carbon below iron — contradicting lesson 1's correct
   list, and undermining lesson 3, which depends on carbon sitting above iron
   (that is why we can smelt iron at all).
3. **An endothermic lesson claims a kitchen experiment can freeze a beaker
   to the bench.** The reaction it names can't get anywhere near freezing —
   and it's one students can and will try at home.
4. **Three diagrams draw the very misconception their lesson exists to
   kill** — solids drawn with gaps under text saying "all touching"; atoms
   silently vanishing in the iron-and-sulfur dish; a filtration picture whose
   own label says salt is nearly as big as the paper's holes. Students trust
   pictures over words, so these go to Design to redraw.
5. **"Next in this unit" lies on about 23 pages.** The link under that
   heading often goes backwards, into another unit, or even into two biology
   lessons. One mechanical fix cleans up all of them.
6. **A few small bugs hide good teaching**: on the groups-and-periods page,
   the progress rail can never reach 5/5, and a whole misconception-busting
   panel is built into the page but never shown to anyone. Two one-line
   fixes.
7. **On two metals pages, word equations show up as raw computer code** —
   brackets and quote marks on screen instead of "zinc + copper sulfate →
   zinc sulfate + copper". Quick fix, embarrassing until then.

## What needs your eyes (nobody else can decide these)

- **About 18 science rulings** — the catalysts flask and the freezing demo
  above, plus things like: the "smell crosses a room in two minutes by
  diffusion" claim, "ten metres of atmosphere", sugar's melting point, and
  whether the course credits **tasting** samples (four lessons credit it;
  one lesson explicitly teaches "nothing in a laboratory is tasted" — the
  course currently contradicts itself and you decide which side wins).
- **About 20 quick nods** — Code has drafted one-sentence corrections for
  clear errors (seawater called acidic when it's alkaline, "a hundred
  thousand times" that should be "a thousand", etc.). These just need your
  yes.
- **The safety wording pile** — every safety note across the ten units is
  listed for your sign-off, unchanged. One page (burning magnesium and
  sulfur) has no safety line at all and needs you to write one.
- **Two of your past rulings, revisited with evidence**: flat formulae erase
  the very big-vs-small-number distinction two quiz questions are testing;
  and the 60-character "Complete" gate left a student's
  correct 55-character answer with a dead button and no explanation.

## What happens next

The moment you've ruled, Code starts fixing under standing authority:
science errors first, then bugs, then polish — one unit of work, one commit,
one push, verified live each time. Design gets a written brief for the
diagram batch. Realistically: one decision session from you, about five
working sessions from Code, and chemistry is ready for the first week of
September.

Full detail, every finding with evidence and a proposed fix:
`docs/ks3/audits/2026-08-25-chem-audit/REPORT.md`.
