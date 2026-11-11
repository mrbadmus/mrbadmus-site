#!/usr/bin/env python3
"""teacher_picker_drive.py — the name picker's PROMISES, driven and checked.

    python3 teacher_picker_drive.py
    python3 teacher_picker_drive.py --shots DIR    # also write screenshots

⊕ MRB-323, 5 Sep 2026.

── WHY THIS EXISTS AND THE TWO GATES BESIDE IT DO NOT COVER IT ──────────

`teacher_behaviour.py` already presses the picker's entry button by name
(`AMENDED_ADDITIONS['pick-open']`) and sweeps every control the overlay
draws, and `teacher_reach.py` already hit-tests all of them at 390px and
360px. Between them they prove the picker MOUNTS, that nothing in it is
dead, and that a teacher on a phone can reach every part of it.

⚠️ NEITHER OF THEM KNOWS WHAT A PICKER IS FOR. "The press changed
something" is satisfied by a picker that shows the same child eleven times
in a row, by one that calls on a student who is off sick, and by a
no-repeats mode that repeats — every one of those changes the page.

This gate asserts the four claims the feature actually makes:

    1. NO REPEATS MEANS NO REPEATS. Press Pick M times on a class of M and
       you get M DISTINCT names, and the count line agrees with the number
       of presses at every step.
    2. RESET PUTS THE POOL BACK. After it, the count is 0 of M again and
       the cycle can run a second time.
    3. ABSENT MEANS ABSENT. A student marked away this lesson is not
       returned by any of M presses — checked against the WHOLE cycle, not
       against one draw, because a single draw missing one name proves
       nothing at all.
    4. RANDOM IS RANDOM, AND IS NOT THE CYCLE. With repeats allowed, many
       presses over a small pool produce a repeat — which is the property
       that tells the two modes apart, and the one a toggle wired to
       nothing would fail.

And one thing that is not a promise about picking:

    5. IT WRITES NOTHING BY DEFAULT. Every request the page makes is
       recorded, and a whole cycle of presses — plus a reset, plus marking
       somebody absent — must add not one. Storage is checked the same way:
       `localStorage` and `sessionStorage` are empty before and after, for
       every run in which the teacher's "Save for this class" switch stays
       OFF.

And the settings panel and the timer (the second half of this file):

    6. WEIGHTS ARE TICKETS. A pupil with five tickets is drawn about five
       times as often as one with one (Random), and comes up exactly w times
       in one No-repeats cycle with the count line agreeing at every step.
    7. PICK NEXT LANDS ONCE. Marked in the panel, the next Pick runs the
       ordinary reveal (`aria-busy` goes up) and lands on that pupil; then it
       is gone and the picks are random again. It is never drawn on the board.
    8. SAVE IS THE ONLY KEEP, AND IT IS OPT-IN. Off: a reload leaves weights
       at 1 and `localStorage` empty. On: exactly one key for this class,
       holding weights and nothing else, restored after a reload; turning it
       off removes the key.
    9. THE TIMER counts, pauses, resets, adds time, flips to its last-ten-
       seconds state and to done; Space toggles it in the full view; and it
       writes and requests nothing.

⚠️ IT DRIVES THE FIXTURE, like every other gate on this port. A live
teacher page starts with `requireTeacherRole`, so driving one needs a
credential and a waking Render. What this proves is everything between the
roster arriving and the name on the wall.

⚠️ AND IT PRESSES THROUGH THE REAL DOM, never through `MrBadmusPicker`'s
own internals. Calling `open()` and reading `STATE` would be this file
agreeing with itself; every step below finds a button by its
`data-mrb-added` marker and clicks it, which is what a teacher does.
"""

import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))

FIXTURE = "teacher_fixtures/class-detail-fixture.html"

# The widths the picker has to work at: a projector-shaped board and a real
# phone. 1460 is the class screen's own `max-width`; 390 is the width
# `teacher_reach` uses and the one an iPhone actually has.
WIDTHS = ((1460, 940), (390, 844))


# ── the drive, in the page ───────────────────────────────────────────────
#
# ⚠️ ONE `await frame()` AFTER EVERY PRESS, AND A LONGER WAIT AFTER A PICK.
# The reveal animation is ~700ms of shuffling names before it settles on the
# real one, so reading the name straight after the click reads a DECOY —
# which would make this gate report repeats that never happened, at random,
# on a correct picker. `settle()` waits for the name to stop changing.
DRIVE = r"""
(async () => {
  const host = document.querySelector('#mrb-teacher');
  if (!host) { return JSON.stringify({error: 'no #mrb-teacher host'}); }

  const frame = () => new Promise(r => requestAnimationFrame(
                        () => requestAnimationFrame(r)));
  const wait  = (ms) => new Promise(r => setTimeout(r, ms));

  const q = (m) => host.querySelector('[data-mrb-added="' + m + '"]');
  const all = (m) => Array.prototype.slice.call(
                       host.querySelectorAll('[data-mrb-added="' + m + '"]'));
  const nameNow = () => {
    const n = host.querySelector('[data-mrb-name]');
    return n ? (n.textContent || '').trim() : '';
  };
  const countNow = () => {
    const f = host.querySelector('[data-mrb-picker]');
    if (!f) { return ''; }
    const c = f.querySelectorAll('div');
    for (let i = 0; i < c.length; i++) {
      const t = (c[i].textContent || '').trim();
      if (/^(Picked \d+ of \d+|\d+ in the pool|Nobody in the pool)$/.test(t)) {
        return t;
      }
    }
    return '';
  };

  /* The name after the shuffle has finished — ASKED, NOT GUESSED.
     ⚠️ THE FIRST VERSION OF THIS POLLED UNTIL THE TEXT STOPPED CHANGING,
     and it was wrong in the worst available way: the reveal's last frames
     are 140ms apart and the poll was 60, so two consecutive reads landed on
     the same DECOY and this gate reported repeats that a correct picker had
     not made. `shared/teacher-picker.js` holds `aria-busy` on the name slot
     for exactly as long as the names are still moving. */
  async function settle() {
    const n = () => host.querySelector('[data-mrb-name]');
    for (let i = 0; i < 60; i++) {
      const el = n();
      if (el && !el.hasAttribute('aria-busy')) { return (el.textContent || '').trim(); }
      await wait(40);
    }
    return nameNow();
  }

  /* ⚠️ A DISABLED CONTROL IS NOT A PRESS. `pick-go` stays in the DOM with
     its marker when the cycle is spent — it is `aria-disabled`, which is
     also how `teacher_behaviour.disabledLooking()` reads it — and clicking
     it does nothing. Treated as a press, the name on screen would be read a
     second time and reported as a REPEAT the picker never made. */
  const press = async (m) => {
    const el = q(m);
    if (!el || el.getAttribute('aria-disabled') === 'true') { return false; }
    el.click();
    await frame();
    return true;
  };

  const out = {steps: [], problems: []};
  const fail = (s) => out.problems.push(s);

  // ── 0. the entry button, and the overlay it opens ──────────────────
  const entry = q('pick-open');
  if (!entry) { return JSON.stringify({error: 'no pick-open on the page'}); }
  out.entryLabel = (entry.innerText || '').trim();
  entry.click();
  await frame();
  const overlay = host.querySelector('[data-mrb-picker]');
  if (!overlay) { return JSON.stringify({error: 'pick-open opened nothing'}); }

  /* BOARD MODE IS THE REVEAL, not a second toggle — so the thing to check
     is that the overlay really is full-viewport and really is drawn at the
     display scale, rather than that some "board" button exists. */
  const box = overlay.getBoundingClientRect();
  out.overlay = {w: Math.round(box.width), h: Math.round(box.height),
                 vw: window.innerWidth, vh: window.innerHeight,
                 pos: getComputedStyle(overlay).position};

  const M = (function () {
    const t = countNow();
    const m = t.match(/^Picked \d+ of (\d+)$/);
    return m ? Number(m[1]) : 0;
  })();
  out.M = M;
  out.count0 = countNow();
  if (M < 2) { fail('the fixture class has ' + M + ' student(s) — nothing to cycle'); }

  // ── 1. no repeats means no repeats ─────────────────────────────────
  const cycle = [], counts = [];
  for (let i = 0; i < M; i++) {
    if (!await press('pick-go')) { fail('Pick vanished after ' + i + ' press(es)'); break; }
    cycle.push(await settle());
    counts.push(countNow());
  }
  out.cycle = cycle;
  out.counts = counts;
  out.nameSize = (function () {
    const n = host.querySelector('[data-mrb-name]');
    return n ? Math.round(parseFloat(getComputedStyle(n).fontSize)) : 0;
  })();

  const uniq = {};
  cycle.forEach(n => { uniq[n] = (uniq[n] || 0) + 1; });
  const dupes = Object.keys(uniq).filter(k => uniq[k] > 1);
  if (dupes.length) {
    fail('no-repeats repeated: ' + dupes.map(d => d + ' x' + uniq[d]).join(', '));
  }
  if (cycle.length !== M) { fail('cycle produced ' + cycle.length + ' of ' + M); }
  counts.forEach((c, i) => {
    const want = 'Picked ' + (i + 1) + ' of ' + M;
    if (c !== want) { fail('count line after press ' + (i + 1) + ' read ' + JSON.stringify(c) + ', wanted ' + JSON.stringify(want)); }
  });
  /* Exhausted, the primary must stop offering a pick it cannot make. */
  const spent = q('pick-go');
  out.exhausted = spent ? spent.getAttribute('aria-disabled') : 'gone';
  if (out.exhausted !== 'true') { fail('every name is spent and Pick is still live'); }

  // ── 2. reset puts the pool back ────────────────────────────────────
  if (!await press('pick-reset')) { fail('no Start again control after a full cycle'); }
  out.countAfterReset = countNow();
  if (out.countAfterReset !== 'Picked 0 of ' + M) {
    fail('after Start again the count read ' + JSON.stringify(out.countAfterReset));
  }
  if (!await press('pick-go')) { fail('Pick did not come back after Start again'); }
  out.afterReset = await settle();
  if (!out.afterReset) { fail('Start again left the picker unable to pick'); }

  // ── 3. absent means absent ─────────────────────────────────────────
  await press('pick-reset');
  await press('pick-absent');                       // open the list
  const chips = all('pick-absent-row');
  out.chips = chips.length;
  if (chips.length !== M) { fail('the absent list holds ' + chips.length + ' of ' + M + ' names'); }
  const away = (chips[0].innerText || '').trim();
  out.away = away;
  chips[0].click();
  await frame();
  out.countAway = countNow();
  if (out.countAway !== 'Picked 0 of ' + (M - 1)) {
    fail('one student away and the count read ' + JSON.stringify(out.countAway));
  }
  const second = [];
  for (let i = 0; i < M - 1; i++) {
    if (!await press('pick-go')) { break; }
    second.push(await settle());
  }
  out.withoutAway = second;
  if (second.indexOf(away) !== -1) {
    fail('a student marked absent was picked: ' + JSON.stringify(away));
  }
  if (second.length !== M - 1) { fail('absent cycle produced ' + second.length + ' of ' + (M - 1)); }

  // ── 4. random is random, and is not the cycle ──────────────────────
  //
  // A repeat over 3M presses of a pool of M is what tells "with
  // replacement" from "the cycle with a different label". The chance of
  // seeing none is (M-1)!/(M^(M-1)) scale — vanishing for any real class,
  // and the pool is checked to be at least 2 above.
  if (!await press('pick-mode-random')) { fail('no Random toggle'); }
  out.countRandom = countNow();
  if (!/ in the pool$/.test(out.countRandom)) {
    fail('Random mode still showed a cycle count: ' + JSON.stringify(out.countRandom));
  }
  const rolls = [];
  for (let i = 0; i < M * 3; i++) {
    if (!await press('pick-go')) { break; }
    rolls.push(await settle());
  }
  out.rolls = rolls.length;
  const seenR = {};
  let repeated = false;
  rolls.forEach(n => { if (seenR[n]) { repeated = true; } seenR[n] = 1; });
  if (!repeated) { fail('Random never repeated over ' + rolls.length + ' presses of ' + M + ' — it is behaving as the cycle'); }
  if (rolls.indexOf(away) !== -1) { fail('Random picked a student marked absent'); }

  // back to no-repeats, and close
  await press('pick-mode-cycle');
  out.countBack = countNow();
  await press('pick-close');
  await frame();
  out.closed = !host.querySelector('[data-mrb-picker]');
  if (!out.closed) { fail('the close control left the overlay on the page'); }

  out.storage = {
    local: Object.keys(window.localStorage || {}).length,
    session: Object.keys(window.sessionStorage || {}).length
  };
  return JSON.stringify(out);
})()
"""

# ── the animation, checked ONCE and then emulated away ───────────────────
#
# ⚑ WHY THE BULK RUN DOES NOT WATCH IT. The cycle below makes about five
# presses per student and waits out the reveal on every one, which for a
# class of sixteen is well over a minute of pure decoration — and
# `ks3_browser`'s socket gives up at sixty seconds, which is how the first
# version of this gate died looking exactly like a Chrome crash. So the
# reveal is proved HERE, once, on its own, and the rest of the run sets
# `prefers-reduced-motion: reduce` through `Emulation.setEmulatedMedia`.
#
# ⚠️ THAT IS COVERAGE, NOT A DODGE, AND IN BOTH DIRECTIONS. The reduced
# branch of `reveal()` is a real code path a real teacher with a real
# accessibility setting takes, and running the whole cycle on it is the only
# thing in the estate that exercises it. The animated branch is proved right
# here: `aria-busy` goes up, names actually move while it is up, it comes
# down, and the name it comes down on is the one the picker chose — which is
# the promise that matters, because the winner is decided before the shuffle
# and the shuffle must not be able to change it.
MOTION = r"""
(async () => {
  const host = document.querySelector('#mrb-teacher');
  const frame = () => new Promise(r => requestAnimationFrame(
                        () => requestAnimationFrame(r)));
  const wait  = (ms) => new Promise(r => setTimeout(r, ms));
  const q = (m) => host.querySelector('[data-mrb-added="' + m + '"]');
  const nm = () => host.querySelector('[data-mrb-name]');

  q('pick-open').click();
  await frame();
  q('pick-go').click();
  await frame();

  const out = {busySeen: false, moved: 0, ms: 0};
  let seen = {}, t0 = Date.now(), last = null;
  for (let i = 0; i < 60; i++) {
    const el = nm();
    if (!el) { break; }
    if (el.hasAttribute('aria-busy')) {
      out.busySeen = true;
      const t = (el.textContent || '').trim();
      if (t && t !== last) { out.moved += 1; seen[t] = 1; }
      last = t;
    } else if (out.busySeen) {
      out.ms = Date.now() - t0;
      out.landed = (el.textContent || '').trim();
      break;
    }
    await wait(25);
  }
  out.distinct = Object.keys(seen).length;
  /* ⚠️ PUT THE CYCLE BACK BEFORE LEAVING. The session deliberately survives
     a close — that is what makes "no repeats" mean anything across a lesson
     — so this check's one pick would otherwise start the run below one name
     down, and every count line after it would read one too high. Found by
     this gate on its own first green run, which is the right place. */
  const r = q('pick-reset');
  if (r) { r.click(); await frame(); }
  q('pick-close').click();
  await frame();
  return JSON.stringify(out);
})()
"""


# Reopen and re-press, to prove the session state survives a close — the
# property that makes "no repeats" mean anything across a lesson.
REOPEN = r"""
(async () => {
  const host = document.querySelector('#mrb-teacher');
  const frame = () => new Promise(r => requestAnimationFrame(
                        () => requestAnimationFrame(r)));
  const q = (m) => host.querySelector('[data-mrb-added="' + m + '"]');
  q('pick-open').click();
  await frame();
  const f = host.querySelector('[data-mrb-picker]');
  const c = f ? f.querySelectorAll('div') : [];
  let line = '';
  for (let i = 0; i < c.length; i++) {
    const t = (c[i].textContent || '').trim();
    if (/^(Picked \d+ of \d+|\d+ in the pool|Nobody in the pool)$/.test(t)) { line = t; break; }
  }
  return JSON.stringify({line: line});
})()
"""


# ══ THE SECOND HALF: settings panel, weights, pick next, save, timer ═════
#
# Same rules as the first half: everything is pressed through the real DOM by
# its `data-mrb-added` marker, one fresh page per scenario so no scenario
# inherits another's cycle, and the request recorder is injected again after
# every load. The bulk draws run with `prefers-reduced-motion: reduce` (the
# reveal's real, second code path), and the one scenario that needs the
# animation — pick next landing through the ordinary reveal — runs with it on.

def wrap(pre, body):
    """Declarations live INSIDE the async function: `Runtime.evaluate` runs a
    top-level `const` in the page's global scope, so a second script that
    re-declared `host` would die with "Identifier has already been declared"
    — and the first script's `host` would still be there to mislead."""
    return "(async () => {\n" + pre + "\n" + body + "\n})()"


PRE = r"""
const host = document.querySelector('#mrb-teacher');
const frame = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
const wait  = (ms) => new Promise(r => setTimeout(r, ms));
const q   = (m, root) => (root || host).querySelector('[data-mrb-added="' + m + '"]');
const all = (m, root) => Array.prototype.slice.call((root || host).querySelectorAll('[data-mrb-added="' + m + '"]'));
const nameNow = () => { const n = host.querySelector('[data-mrb-name]'); return n ? (n.textContent || '').trim() : ''; };
const countNow = () => {
  const f = host.querySelector('[data-mrb-picker]');
  if (!f) { return ''; }
  const c = f.querySelectorAll('div');
  for (let i = 0; i < c.length; i++) {
    const t = (c[i].textContent || '').trim();
    if (/^(Picked \d+ of \d+|\d+ in the pool|Nobody in the pool)$/.test(t)) { return t; }
  }
  return '';
};
const click = async (m) => { const e = q(m); if (!e || e.getAttribute('aria-disabled') === 'true') { return false; } e.click(); await frame(); return true; };
const openPicker = async () => { q('pick-open').click(); await frame(); };
const rows = () => all('pick-set-row');
const rowName = (r) => (q('pick-set-name', r).firstChild.textContent || '').trim();
const rowCount = (r) => Number((q('pick-set-count', r).textContent || '0').trim());
const plusRow = async (i, n) => { for (let k = 0; k < n; k++) { q('pick-set-plus', rows()[i]).click(); await frame(); } };
const out = {problems: []};
const fail = (m) => out.problems.push(m);
const lsKeys = () => Object.keys(window.localStorage || {});
"""

WEIGHT_RANDOM = wrap(PRE, r"""
  await openPicker();
  if (!await click('pick-settings')) { return JSON.stringify({error: 'no settings cog'}); }
  const rs = rows(), M = rs.length;
  out.M = M;
  const heavy = rowName(rs[0]);
  await plusRow(0, 4);
  out.heavyCount = rowCount(rows()[0]);
  out.minusEnabled = q('pick-set-minus', rows()[0]).getAttribute('aria-disabled');
  out.minusOnOne = q('pick-set-minus', rows()[1]).getAttribute('aria-disabled');
  await click('pick-settings');                       // close the panel
  await click('pick-mode-random');
  const N = 1500, tally = {};
  for (let i = 0; i < N; i++) {
    const g = q('pick-go');
    g.click();
    const n = nameNow();
    tally[n] = (tally[n] || 0) + 1;
  }
  const others = Object.keys(tally).filter(k => k !== heavy);
  const sumO = others.reduce((a, k) => a + tally[k], 0);
  out.heavy = heavy;
  out.heavyHits = tally[heavy] || 0;
  out.avgOther = sumO / Math.max(1, M - 1);
  out.ratio = out.heavyHits / Math.max(0.0001, out.avgOther);
  out.distinct = Object.keys(tally).length;
  out.count = countNow();
  out.ls = lsKeys().length;
  await click('pick-close');
  out.requests = (window.__REQ__ || []).length;
  return JSON.stringify(out);
""")

WEIGHT_CYCLE = wrap(PRE, r"""
  await openPicker();
  await click('pick-settings');
  const rs = rows(), M = rs.length;
  const a = rowName(rs[0]), b = rowName(rs[1]);
  await plusRow(0, 2);          // a: 3
  await plusRow(1, 1);          // b: 2
  await click('pick-settings');
  await click('pick-mode-cycle');
  if (q('pick-reset')) { await click('pick-reset'); }
  const T = M + 3;              // tickets in the hat
  out.T = T;
  out.count0 = countNow();
  if (out.count0 !== 'Picked 0 of ' + T) { fail('count before the cycle read ' + JSON.stringify(out.count0) + ', wanted Picked 0 of ' + T); }
  const names = [], counts = [];
  for (let i = 0; i < T + 3; i++) {
    const g = q('pick-go');
    if (!g || g.getAttribute('aria-disabled') === 'true') { break; }
    g.click();
    names.push(nameNow());
    counts.push(countNow());
  }
  out.presses = names.length;
  const tally = {};
  names.forEach(n => { tally[n] = (tally[n] || 0) + 1; });
  out.tallyA = tally[a]; out.tallyB = tally[b];
  const rest = Object.keys(tally).filter(k => k !== a && k !== b);
  out.restAllOne = rest.every(k => tally[k] === 1);
  out.restN = rest.length;
  counts.forEach((c, i) => { if (c !== 'Picked ' + (i + 1) + ' of ' + T) { fail('count after press ' + (i + 1) + ' read ' + JSON.stringify(c)); } });
  out.finalLabel = (q('pick-go').textContent || '').trim();
  out.finalDisabled = q('pick-go').getAttribute('aria-disabled');
  /* Lowering a weight after the draws must keep N <= M. */
  await click('pick-settings');
  q('pick-set-minus', rows()[0]).click(); await frame();
  q('pick-set-minus', rows()[0]).click(); await frame();      // a back to 1
  await click('pick-settings');
  out.afterLower = countNow();
  const mm = out.afterLower.match(/^Picked (\d+) of (\d+)$/);
  out.honest = !!mm && Number(mm[1]) <= Number(mm[2]) && Number(mm[2]) === T - 2 && Number(mm[1]) === T - 2;
  await click('pick-close');
  return JSON.stringify(out);
""")

# Pick next, with MOTION ON: the reveal must be the ordinary one.
PICK_NEXT = wrap(PRE, r"""
  await openPicker();
  await click('pick-settings');
  let rs = rows();
  out.M = rs.length;
  const t = rowName(rs[3]), u = rowName(rs[4]);
  out.target = t;
  q('pick-set-name', rs[3]).click(); await frame();
  out.marks1 = all('pick-set-next').length;
  q('pick-set-name', rows()[4]).click(); await frame();            // moves it
  out.marks2 = all('pick-set-next').length;
  out.markOnU = !!q('pick-set-next', rows()[4]);
  q('pick-set-name', rows()[4]).click(); await frame();            // unmarks
  out.marks3 = all('pick-set-next').length;
  q('pick-set-name', rows()[3]).click(); await frame();            // back on t
  out.resetEnabled = q('pick-set-reset').getAttribute('aria-disabled');
  await click('pick-settings');
  out.boardMarks = all('pick-set-next').length + (host.querySelector('[data-mrb-picker]').textContent.indexOf('Next') !== -1 ? 1 : 0);
  out.count0 = countNow();

  q('pick-go').click(); await frame();
  let busy = false, moved = 0, last = null;
  for (let i = 0; i < 80; i++) {
    const n = host.querySelector('[data-mrb-name]');
    if (n.hasAttribute('aria-busy')) { busy = true; const x = (n.textContent || '').trim(); if (x !== last) { moved++; last = x; } }
    else if (busy) { break; }
    await wait(25);
  }
  out.busy = busy; out.moved = moved;
  out.landed = nameNow();
  out.count1 = countNow();

  await click('pick-settings');
  out.marksAfter = all('pick-set-next').length;
  out.resetNow = q('pick-set-reset').getAttribute('aria-disabled');
  await click('pick-settings');

  /* Teacher's choice wins even when the pupil has no ticket left; picked
     must not rise above the weight. */
  await click('pick-settings');
  q('pick-set-name', rows()[3]).click(); await frame();
  await click('pick-settings');
  q('pick-go').click(); await frame();
  for (let i = 0; i < 80 && host.querySelector('[data-mrb-name]').hasAttribute('aria-busy'); i++) { await wait(25); }
  out.landed2 = nameNow();
  out.count2 = countNow();

  /* Marking the pupil absent clears pick next; an absent pupil cannot be
     chosen as next. */
  await click('pick-settings');
  q('pick-set-name', rows()[5]).click(); await frame();
  out.markBeforeAbsent = all('pick-set-next').length;
  await click('pick-settings');
  await click('pick-absent');
  const chip = all('pick-absent-row')[5];
  chip.click(); await frame();
  await click('pick-absent');
  await click('pick-settings');
  out.markAfterAbsent = all('pick-set-next').length;
  out.absentNameDisabled = q('pick-set-name', rows()[5]).getAttribute('aria-disabled');
  q('pick-set-name', rows()[5]).click(); await frame();
  out.stillNone = all('pick-set-next').length;
  await click('pick-settings');
  out.ls = lsKeys().length;
  out.requests = (window.__REQ__ || []).length;
  return JSON.stringify(out);
""")

# …and the picks after it, with motion reduced: random again.
RANDOM_AFTER = wrap(PRE, r"""
  await click('pick-mode-random');
  const tally = {};
  for (let i = 0; i < 30; i++) { q('pick-go').click(); const n = nameNow(); tally[n] = (tally[n] || 0) + 1; }
  out.distinct = Object.keys(tally).length;
  out.maxShare = Math.max.apply(null, Object.keys(tally).map(k => tally[k])) / 30;
  await click('pick-settings');
  out.marks = all('pick-set-next').length;
  await click('pick-settings');
  await click('pick-close');
  return JSON.stringify(out);
""")

SAVE_OFF_SET = wrap(PRE, r"""
  await openPicker();
  out.classId = host.querySelector('[data-mrb-picker]').getAttribute('data-mrb-picker');
  await click('pick-settings');
  out.switch0 = q('pick-set-save').getAttribute('aria-checked');
  await plusRow(0, 2);
  q('pick-set-name', rows()[1]).click(); await frame();     // pick next, never saved
  await click('pick-settings');
  await click('pick-absent');
  all('pick-absent-row')[2].click(); await frame();         // absent, never saved
  out.ls = lsKeys();
  await click('pick-close');
  out.lsAfterClose = lsKeys();
  return JSON.stringify(out);
""")

SAVE_READ = wrap(PRE, r"""
  await openPicker();
  await click('pick-settings');
  out.switch = q('pick-set-save').getAttribute('aria-checked');
  out.counts = rows().map(rowCount);
  out.marks = all('pick-set-next').length;
  out.ls = lsKeys();
  out.help = (q('pick-set-help').textContent || '').trim();
  return JSON.stringify(out);
""")

SAVE_ON_SET = wrap(PRE, r"""
  await openPicker();
  out.classId = host.querySelector('[data-mrb-picker]').getAttribute('data-mrb-picker');
  await click('pick-settings');
  q('pick-set-save').click(); await frame();
  out.switch1 = q('pick-set-save').getAttribute('aria-checked');
  out.keysOn = lsKeys();
  out.valOn0 = window.localStorage.getItem(out.keysOn[0] || 'none');
  await plusRow(0, 2);          // 3
  await plusRow(1, 1);          // 2
  q('pick-set-name', rows()[2]).click(); await frame();       // pick next: not saved
  await click('pick-settings');
  await click('pick-absent');
  all('pick-absent-row')[3].click(); await frame();           // absent: not saved
  out.keys = lsKeys();
  out.raw = window.localStorage.getItem(out.keys[0] || 'none');
  out.sess = Object.keys(window.sessionStorage || {}).length;
  out.cookie = document.cookie;
  await click('pick-absent');
  await click('pick-settings');
  q('pick-set-minus', rows()[1]).click(); await frame();      // weight change rewrites
  out.rawAfterMinus = window.localStorage.getItem(out.keys[0] || 'none');
  q('pick-set-plus', rows()[1]).click(); await frame();
  /* Reset keeps the key (the switch stays on) but empties it. */
  q('pick-set-reset').click(); await frame();
  out.rawAfterReset = window.localStorage.getItem(out.keys[0] || 'none');
  out.switchAfterReset = q('pick-set-save').getAttribute('aria-checked');
  await plusRow(0, 2); await plusRow(1, 1);                   // 3 and 2 again
  return JSON.stringify(out);
""")

SAVE_OFF_AGAIN = wrap(PRE, r"""
  q('pick-set-save').click(); await frame();
  out.switch = q('pick-set-save').getAttribute('aria-checked');
  out.ls = lsKeys();
  out.countsKept = rows().map(rowCount).slice(0, 3);
  await click('pick-settings');
  await click('pick-close');
  await openPicker();
  await click('pick-settings');
  out.countsAfterClose = rows().map(rowCount).slice(0, 3);
  await click('pick-close');
  out.requests = (window.__REQ__ || []).length;
  return JSON.stringify(out);
""")

# ── the timer ────────────────────────────────────────────────────────────

TIMER_PRE = PRE + r"""
const tm = () => document.querySelector('[data-tm="overlay"]');
const tq = (m) => { const t = tm(); return t ? t.querySelector('[data-mrb-added="' + m + '"]') : null; };
const tclick = async (m) => { const e = tq(m); if (!e || e.getAttribute('aria-disabled') === 'true') { return false; } e.click(); await frame(); return true; };
const reading = () => { const t = tm(); return t ? t.getAttribute('data-tm-reading') : null; };
const state = () => { const t = tm(); return t ? t.getAttribute('data-tm-state') : null; };
const view = () => { const t = tm(); return t ? t.getAttribute('data-tm-view') : null; };
const secOf = (r) => { const p = String(r).split(':').map(Number); return p.length === 3 ? p[0]*3600+p[1]*60+p[2] : p[0]*60+p[1]; };
const waitFor = async (fn, ms) => { const t0 = Date.now(); while (Date.now() - t0 < ms) { if (fn()) { return true; } await wait(50); } return false; };
const key = (target, k, code) => { const e = new KeyboardEvent('keydown', {key: k, code: code || k, bubbles: true, cancelable: true}); target.dispatchEvent(e); return e.defaultPrevented; };
"""

TIMER_MAIN = wrap(TIMER_PRE, r"""
  // ── entry: the class screen's Timer opens the FULL view ──────────────
  const entry = q('timer-open');
  if (!entry) { return JSON.stringify({error: 'no timer-open entry on the class screen'}); }
  out.entryLabel = (entry.innerText || '').trim();
  entry.click(); await frame();
  out.opened = !!tm();
  out.view0 = view();
  const t = tm();
  const cs = getComputedStyle(t);
  out.full = {pos: cs.position, z: Number(cs.zIndex), bg: cs.backgroundColor,
              w: Math.round(t.getBoundingClientRect().width), h: Math.round(t.getBoundingClientRect().height),
              vw: innerWidth, vh: innerHeight, parentIsBody: t.parentNode === document.body,
              insideHost: host.contains(t)};
  out.digitPx = Math.round(parseFloat(getComputedStyle(t.querySelector('[data-tm-digits]')).fontSize));
  out.digitsHidden = t.querySelector('[data-tm-digits]').getAttribute('aria-hidden');
  out.live = (() => { const l = tq('tm-live'); return l ? {role: l.getAttribute('role'), live: l.getAttribute('aria-live')} : null; })();
  out.dialog = {role: t.getAttribute('role'), label: t.getAttribute('aria-label'), modal: t.getAttribute('aria-modal')};
  out.minH = Math.round(Math.min.apply(null, Array.prototype.slice.call(t.querySelectorAll('button')).map(b => b.getBoundingClientRect().height)));

  // ── a custom 12 s countdown ──────────────────────────────────────────
  tq('tm-custom-min').value = '0';
  tq('tm-custom-sec').value = '12';
  await tclick('tm-custom-set');
  out.set12 = reading();
  out.resetDisabledAtRest = tq('tm-reset').getAttribute('aria-disabled');
  out.addHiddenIdle = !tq('tm-add-30');
  await tclick('tm-toggle');                                     // Start
  out.stateStart = state();
  out.liveStart = (tq('tm-live').textContent || '').trim();
  out.addShown = !!tq('tm-add-30') && !!tq('tm-add-60');
  out.warnSeen = await waitFor(() => state() === 'warn', 4500);
  out.readingWarn = reading();
  out.warnColour = getComputedStyle(t.querySelector('[data-tm-digits]')).color;
  const calm = (() => { return null; })();
  // pause holds the reading
  await tclick('tm-toggle');
  const pr = reading(); await wait(700);
  out.pausedHolds = (reading() === pr) && state() !== 'running';
  out.livePause = (tq('tm-live').textContent || '').trim();
  // +30 s and +1 min add to the reading
  const before = secOf(reading());
  await tclick('tm-add-30');
  const a30 = secOf(reading());
  await tclick('tm-add-60');
  const a60 = secOf(reading());
  out.adds = [before, a30, a60];
  out.stateAfterAdd = state();
  // reset puts it back
  await tclick('tm-reset');
  out.afterReset = reading(); out.stateReset = state();
  // run to the end: warn then done
  await tclick('tm-toggle');
  out.done = await waitFor(() => state() === 'done', 14500);
  out.doneText = (t.textContent || '').indexOf("Time's up") !== -1;
  out.doneReading = reading();
  out.beeps = Number(tm().getAttribute('data-tm-beeps'));
  out.liveDone = (tq('tm-live').textContent || '').trim();
  // Again restarts a fresh countdown
  await tclick('tm-toggle');
  out.againState = state();
  await tclick('tm-reset');

  // ── muted: a short countdown ends silently ───────────────────────────
  await tclick('tm-mute');
  out.muted = tm().getAttribute('data-tm-muted');
  tq('tm-custom-min').value = '0'; tq('tm-custom-sec').value = '3';
  await tclick('tm-custom-set');
  await tclick('tm-toggle');
  await waitFor(() => state() === 'done', 5000);
  out.beepsMuted = Number(tm().getAttribute('data-tm-beeps'));
  await tclick('tm-mute');                                      // unmute

  // ── stopwatch counts up ──────────────────────────────────────────────
  await tclick('tm-mode-up');
  out.swStart = reading();
  await tclick('tm-toggle');
  await wait(2300);
  out.swReading = reading();
  await tclick('tm-toggle');
  const sp = reading(); await wait(600);
  out.swHolds = reading() === sp;
  out.swStateAfter = state();
  await tclick('tm-reset');
  out.swReset = reading();
  await tclick('tm-mode-down');
  await tclick('tm-preset-300');                                 // 5 min: out of the warn band

  // ── Space toggles in the full view; not elsewhere ────────────────────
  out.spaceFullPrevented = key(document.body, ' ', 'Space');    // start
  await frame(); out.spaceStart = state();
  key(document.body, ' ', 'Space'); await frame();
  out.spacePause = state();
  await tclick('tm-reset');

  // ── float: corner, above the page, and Space only with focus inside ──
  await tclick('tm-view');
  out.view1 = view();
  const fr = tm().getBoundingClientRect(), fcs = getComputedStyle(tm());
  out.float = {pos: fcs.position, z: Number(fcs.zIndex), right: Math.round(innerWidth - fr.right),
               bottom: Math.round(innerHeight - fr.bottom), w: Math.round(fr.width), h: Math.round(fr.height),
               vw: innerWidth, vh: innerHeight};
  out.floatMinH = Math.round(Math.min.apply(null, Array.prototype.slice.call(tm().querySelectorAll('button')).map(b => b.getBoundingClientRect().height)));
  document.activeElement && document.activeElement.blur && document.activeElement.blur();
  out.spaceOutsidePrevented = key(document.body, ' ', 'Space');
  await frame(); out.spaceOutside = state();
  const fb = tq('tm-toggle'); fb.focus();
  out.spaceInsidePrevented = key(fb, ' ', 'Space');
  await frame(); out.spaceInside = state();
  await tclick('tm-toggle');                                     // pause again
  await tclick('tm-reset');

  // ── the picker on top: the timer button floats it, Escape order ──────
  await tclick('tm-close');
  out.closedGone = !tm();
  await openPicker();
  const pt = q('pick-timer');
  out.pickTimerPressed0 = pt.getAttribute('aria-pressed');
  pt.click(); await frame();
  out.pickView = view();
  out.pickPressed1 = q('pick-timer').getAttribute('aria-pressed');
  out.pickerStillOpen = !!host.querySelector('[data-mrb-picker]');
  const fr2 = tm().getBoundingClientRect();
  out.footerCovered = ['pick-mode-cycle', 'pick-mode-random', 'pick-absent', 'pick-go'].filter(m => {
    const r = q(m).getBoundingClientRect();
    return !(r.right <= fr2.left || r.left >= fr2.right || r.bottom <= fr2.top || r.top >= fr2.bottom);
  });
  const pz = Number(getComputedStyle(host.querySelector('[data-mrb-picker]')).zIndex);
  out.zAbovePicker = Number(getComputedStyle(tm()).zIndex) > pz;
  out.floatCoversNothingTop = tm().getBoundingClientRect().top > innerHeight * 0.3;
  // a running float survives the picker closing
  await tclick('tm-toggle');
  await click('pick-close');
  out.survivesPickerClose = !!tm() && state() === 'running';
  // reopen the picker, promote to full from its button, then Escape order
  await openPicker();
  q('pick-timer').click(); await frame();
  out.promoted = view();
  const prevented = key(document, 'Escape');
  await frame();
  out.escView = view();
  out.escPickerOpen = !!host.querySelector('[data-mrb-picker]');
  out.escPrevented = prevented;
  key(document, 'Escape'); await frame();                        // now the picker's own
  out.escSecondPicker = !!host.querySelector('[data-mrb-picker]');
  out.escSecondTimer = !!tm();
  await tclick('tm-close');
  out.storage = {local: lsKeys().length, session: Object.keys(window.sessionStorage || {}).length};
  out.requests = (window.__REQ__ || []).length;
  return JSON.stringify(out);
""")




# the request recorder, as a constant so every fresh page gets it again
REC = """
  window.__REQ__ = [];
  (function () {
    var f = window.fetch;
    window.fetch = function () {
      window.__REQ__.push(['fetch', String(arguments[0])]);
      return f.apply(this, arguments);
    };
    var o = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (m, u) {
      window.__REQ__.push([m, String(u)]);
      return o.apply(this, arguments);
    };
    var b = navigator.sendBeacon;
    if (b) { navigator.sendBeacon = function (u) {
      window.__REQ__.push(['beacon', String(u)]);
      return b.apply(navigator, arguments); }; }
  }());
  1
"""


def _motion(page, reduce):
    page.send("Emulation.setEmulatedMedia",
              {"features": [{"name": "prefers-reduced-motion",
                             "value": "reduce" if reduce else "no-preference"}]})


def _fresh(br, port, width, height, reduce=True, clear=True):
    page = br.page("http://127.0.0.1:%d/%s" % (port, FIXTURE))
    page.set_viewport(width, height)
    _motion(page, reduce)
    if clear:
        page.eval("window.localStorage.clear(); window.sessionStorage.clear(); 1")
    page.eval(REC)
    return page


def _reload(page, port, width, height, reduce=True):
    page.goto("http://127.0.0.1:%d/%s" % (port, FIXTURE))
    page.set_viewport(width, height)
    _motion(page, reduce)
    page.eval(REC)


def features(cdp, port, width, height):
    """The second half. Returns a list of problem strings; every one is
    prefixed with the width so a red points at the layout it happened in."""
    P = []

    def bad(msg):
        P.append("%dpx: %s" % (width, msg))

    def run(page, js, timeout=120):
        got = json.loads(page.eval(js, timeout=timeout))
        if got.get("error"):
            bad(got["error"])
        for m in got.get("problems", []):
            bad(m)
        return got

    summary = {}
    with cdp.Browser() as br:
        # ── 6a. weight 5, Random: about five times the average pupil ──
        page = _fresh(br, port, width, height)
        g = run(page, WEIGHT_RANDOM)
        summary["ratio"] = round(g.get("ratio") or 0, 2)
        if g.get("heavyCount") != 5:
            bad("four presses of + on a weight-1 pupil read %r, wanted 5"
                % g.get("heavyCount"))
        if g.get("minusEnabled") == "true":
            bad("− is disabled on a pupil whose weight is 5")
        if g.get("minusOnOne") != "true":
            bad("− is not disabled at weight 1 (min is 1)")
        if not (3.5 <= (g.get("ratio") or 0) <= 6.5):
            bad("weight 5 was drawn %.2fx as often as the average weight-1 "
                "pupil over %d picks (%s hit(s) against an average of %.1f) "
                "— wanted between 3.5x and 6.5x"
                % (g.get("ratio") or 0, 1500, g.get("heavyHits"),
                   g.get("avgOther") or 0))
        if g.get("distinct", 0) < (g.get("M") or 0):
            bad("Random over 1500 picks never showed %d of %d pupils"
                % ((g.get("M") or 0) - g.get("distinct", 0), g.get("M") or 0))
        if g.get("ls"):
            bad("weighting without Save wrote %d localStorage key(s)" % g["ls"])
        if g.get("requests"):
            bad("weighting made %d request(s)" % g["requests"])

        # ── 6b. weight in the cycle: exactly w times, count line agrees ─
        _reload(page, port, width, height)
        g = run(page, WEIGHT_CYCLE)
        if g.get("tallyA") != 3 or g.get("tallyB") != 2:
            bad("in one cycle the weight-3 pupil came up %r time(s) and the "
                "weight-2 pupil %r (wanted 3 and 2)"
                % (g.get("tallyA"), g.get("tallyB")))
        if not g.get("restAllOne"):
            bad("a weight-1 pupil did not come up exactly once in the cycle")
        if g.get("presses") != g.get("T"):
            bad("the cycle took %r presses for %r tickets"
                % (g.get("presses"), g.get("T")))
        if g.get("finalDisabled") != "true":
            bad("every ticket is drawn and Pick is still live")
        if not g.get("honest"):
            bad("lowering a weight after its draws left the count line "
                "reading %r — N must never exceed M" % g.get("afterLower"))

        # ── 7. pick next: the ordinary reveal, lands once, then random ──
        _reload(page, port, width, height, reduce=False)
        g = run(page, PICK_NEXT)
        if (g.get("marks1"), g.get("marks2"), g.get("marks3")) != (1, 1, 0):
            bad("pick-next marks across three taps read %r — only one pupil "
                "may be next, and a second tap on the same name unmarks"
                % ((g.get("marks1"), g.get("marks2"), g.get("marks3")),))
        if not g.get("markOnU"):
            bad("tapping a second name did not move the marker to it")
        if g.get("resetEnabled") == "true":
            bad("Reset is disabled while a pick-next mark exists")
        if g.get("boardMarks"):
            bad("the pick-next marker (or the word Next) is visible on the "
                "board — it belongs in the panel only")
        if not g.get("busy") or g.get("moved", 0) < 2:
            bad("pick next did not run the reveal (aria-busy %r, %r frame(s))"
                % (g.get("busy"), g.get("moved")))
        if g.get("landed") != g.get("target"):
            bad("pick next landed on %r, wanted %r"
                % (g.get("landed"), g.get("target")))
        if g.get("count1") != "Picked 1 of %d" % (g.get("M") or 0):
            bad("pick next in the cycle read %r, wanted it to spend one ticket"
                % g.get("count1"))
        if g.get("marksAfter"):
            bad("the pick-next marker survived the pick that used it")
        if g.get("resetNow") != "true":
            bad("Reset is live with nothing to reset")
        if g.get("landed2") != g.get("target") or \
                g.get("count2") != g.get("count1"):
            bad("pick next on a pupil with no ticket left read %r / %r — "
                "the teacher's choice wins and the count must not rise"
                % (g.get("landed2"), g.get("count2")))
        if g.get("markBeforeAbsent") != 1 or g.get("markAfterAbsent"):
            bad("marking the next pupil absent did not clear pick next "
                "(%r then %r)" % (g.get("markBeforeAbsent"),
                                  g.get("markAfterAbsent")))
        if g.get("absentNameDisabled") != "true" or g.get("stillNone"):
            bad("an absent pupil can be chosen as next")
        _motion(page, True)
        g = run(page, RANDOM_AFTER)
        if g.get("distinct", 0) < 2 or g.get("maxShare", 1) > 0.9:
            bad("after pick next the picks are not random again "
                "(%r distinct over 30)" % g.get("distinct"))
        if g.get("marks"):
            bad("a pick-next marker came back by itself")

        # ── 8. Save ───────────────────────────────────────────────────
        # OFF: a reload forgets the weights and nothing was stored
        page = _fresh(br, port, width, height)
        g = run(page, SAVE_OFF_SET)
        if g.get("switch0") != "false":
            bad("Save for this class is not OFF by default")
        if g.get("ls") or g.get("lsAfterClose"):
            bad("with Save OFF, weights/next/absent left localStorage key(s): "
                "%r then %r" % (g.get("ls"), g.get("lsAfterClose")))
        _reload(page, port, width, height)
        g = run(page, SAVE_READ)
        if set(g.get("counts") or [0]) != {1} or g.get("switch") != "false":
            bad("with Save OFF a reload brought weights back: %r (switch %r)"
                % (g.get("counts"), g.get("switch")))
        if g.get("ls"):
            bad("with Save OFF, localStorage holds %r" % g["ls"])

        # ON: one key, weights only, restored after a reload
        page = _fresh(br, port, width, height)
        g = run(page, SAVE_ON_SET)
        keys = g.get("keys") or []
        want = "mrb.picker.weights.v1." + str(g.get("classId"))
        if g.get("switch1") != "true":
            bad("the Save switch did not turn on")
        if keys != [want]:
            bad("Save ON wrote %r, wanted exactly [%r]" % (keys, want))
        try:
            raw = json.loads(g.get("raw") or "null")
        except ValueError:
            raw = None
        if not isinstance(raw, dict) or list(raw.keys()) != ["weights"] or \
                sorted((raw.get("weights") or {}).values()) != [2, 3]:
            bad("the saved value is %r — wanted {\"weights\": {id: 3, id: 2}} "
                "and nothing else (not pick next, not absent)" % g.get("raw"))
        if json.loads(g.get("valOn0") or "{}") != {"weights": {}}:
            bad("turning Save on wrote %r, wanted an empty weights object"
                % g.get("valOn0"))
        if g.get("sess") or g.get("cookie"):
            bad("Save ON touched sessionStorage (%r) or a cookie (%r)"
                % (g.get("sess"), g.get("cookie")))
        try:
            after_minus = json.loads(g.get("rawAfterMinus") or "null")
        except ValueError:
            after_minus = None
        if not after_minus or sorted(after_minus["weights"].values()) != [3]:
            bad("a weight change did not rewrite the key: %r" % g.get("rawAfterMinus"))
        if json.loads(g.get("rawAfterReset") or "null") != {"weights": {}} \
                or g.get("switchAfterReset") != "true":
            bad("Reset with Save on left %r / switch %r — wanted an empty "
                "weights object and the switch still on"
                % (g.get("rawAfterReset"), g.get("switchAfterReset")))
        _reload(page, port, width, height)
        g = run(page, SAVE_READ)
        if g.get("switch") != "true" or (g.get("counts") or [])[:3] != [3, 2, 1]:
            bad("after a reload with Save ON the panel read switch %r, "
                "weights %r — wanted ON and 3, 2, 1"
                % (g.get("switch"), (g.get("counts") or [])[:3]))
        if g.get("marks"):
            bad("pick next was restored after a reload")
        if len(g.get("ls") or []) != 1:
            bad("a reload left %r key(s)" % g.get("ls"))
        g = run(page, SAVE_OFF_AGAIN)
        if g.get("switch") != "false" or g.get("ls"):
            bad("turning Save off left %r (switch %r)"
                % (g.get("ls"), g.get("switch")))
        if g.get("countsKept") != [3, 2, 1] or \
                g.get("countsAfterClose") != [1, 1, 1]:
            bad("Save off: weights should stay until close (%r) and then go "
                "back to 1 (%r)" % (g.get("countsKept"),
                                    g.get("countsAfterClose")))
        if g.get("requests"):
            bad("Save made %d request(s)" % g["requests"])

        # ── 9. the timer ──────────────────────────────────────────────
        page = _fresh(br, port, width, height)
        g = run(page, TIMER_MAIN, timeout=150)
        if not g.get("error"):
            full = g.get("full") or {}
            if g.get("view0") != "full":
                bad("the class screen's Timer opened %r, wanted the full view"
                    % g.get("view0"))
            if full.get("pos") != "fixed" or full.get("w", 0) < full.get("vw", 1) \
                    or full.get("h", 0) < full.get("vh", 1):
                bad("the full timer is not full-viewport: %r" % full)
            if full.get("z", 0) <= 90:
                bad("the timer's z-index (%r) is not above the picker's 90"
                    % full.get("z"))
            if not full.get("parentIsBody") or full.get("insideHost"):
                bad("the timer is not mounted on document.body outside "
                    "#mrb-teacher: %r" % full)
            bg = full.get("bg") or ""
            if bg in ("", "transparent", "rgba(0, 0, 0, 0)") or \
                    bg.startswith("rgba") and not bg.endswith(", 1)"):
                bad("the full timer is not opaque (background %r)" % bg)
            if g.get("digitPx", 0) < (min(width * 0.2, 90)):
                bad("full-screen digits are %spx at %dpx wide — too small "
                    "for the back of a room" % (g.get("digitPx"), width))
            if g.get("digitsHidden") != "true":
                bad("the big digits are not aria-hidden")
            if (g.get("live") or {}).get("role") != "status" or \
                    (g.get("live") or {}).get("live") != "polite":
                bad("no polite status live region: %r" % g.get("live"))
            if (g.get("dialog") or {}).get("role") != "dialog" or \
                    not (g.get("dialog") or {}).get("label"):
                bad("the full timer is not a labelled dialog: %r" % g.get("dialog"))
            if g.get("minH", 0) < 40:
                bad("a full-view timer control is %spx tall (floor 40)"
                    % g.get("minH"))
            if g.get("set12") != "0:12":
                bad("custom 0 min 12 sec read %r" % g.get("set12"))
            if g.get("resetDisabledAtRest") != "true":
                bad("Reset is live with nothing to reset")
            if not g.get("addHiddenIdle") or not g.get("addShown"):
                bad("+30 s / +1 min should appear only once it is running")
            if g.get("stateStart") != "running":
                bad("Start left the timer %r" % g.get("stateStart"))
            if "started" not in (g.get("liveStart") or "").lower():
                bad("starting was not announced: %r" % g.get("liveStart"))
            if not g.get("warnSeen"):
                bad("the last-ten-seconds state never came")
            elif secs_of(g.get("readingWarn")) > 10:
                bad("the warn state began at %r, wanted 0:10 or less"
                    % g.get("readingWarn"))
            if g.get("warnColour") in (None, ""):
                bad("no colour read for the warn digits")
            if not g.get("pausedHolds"):
                bad("Pause did not hold the reading")
            if "paused" not in (g.get("livePause") or "").lower():
                bad("pausing was not announced: %r" % g.get("livePause"))
            ad = g.get("adds") or [0, 0, 0]
            if ad[1] - ad[0] < 29 or ad[2] - ad[1] < 59:
                bad("+30 s / +1 min moved the reading %r — wanted +30 then +60"
                    % (ad,))
            if g.get("stateAfterAdd") == "warn":
                bad("adding time left the timer in the last-ten-seconds state")
            if g.get("afterReset") != "0:12" or g.get("stateReset") != "idle":
                bad("Reset read %r / %r, wanted 0:12 idle"
                    % (g.get("afterReset"), g.get("stateReset")))
            if not g.get("done") or g.get("doneReading") != "0:00" or \
                    not g.get("doneText"):
                bad("the countdown never reached its done state "
                    "(%r, reading %r)" % (g.get("done"), g.get("doneReading")))
            if (g.get("beeps") or 0) < 1:
                bad("the countdown ended without a sound")
            if "up" not in (g.get("liveDone") or "").lower():
                bad("finishing was not announced: %r" % g.get("liveDone"))
            if g.get("againState") != "running":
                bad("Again did not restart the countdown (%r)" % g.get("againState"))
            if g.get("muted") != "1" or g.get("beepsMuted") != g.get("beeps"):
                bad("muted, the countdown still beeped (%r -> %r)"
                    % (g.get("beeps"), g.get("beepsMuted")))
            if g.get("swStart") != "0:00" or secs_of(g.get("swReading")) < 2:
                bad("the stopwatch read %r then %r after 2.3s"
                    % (g.get("swStart"), g.get("swReading")))
            if not g.get("swHolds") or g.get("swStateAfter") != "paused":
                bad("the stopwatch did not hold when paused")
            if g.get("swReset") != "0:00":
                bad("stopwatch Reset read %r" % g.get("swReset"))
            if not g.get("spaceFullPrevented") or g.get("spaceStart") != "running" \
                    or g.get("spacePause") != "paused":
                bad("Space in the full view: start %r pause %r (prevented %r)"
                    % (g.get("spaceStart"), g.get("spacePause"),
                       g.get("spaceFullPrevented")))
            if g.get("view1") != "float":
                bad("the shrink control left the view %r" % g.get("view1"))
            fl = g.get("float") or {}
            if fl.get("pos") != "fixed" or fl.get("right", 99) > 24 or \
                    fl.get("bottom", 99) > 24 or fl.get("w", 999) > 360 or \
                    fl.get("z", 0) <= 90:
                bad("the floating timer is not a small fixed corner card "
                    "above the picker: %r" % fl)
            if g.get("floatMinH", 0) < 40:
                bad("a floating-timer control is %spx tall (floor 40)"
                    % g.get("floatMinH"))
            if g.get("spaceOutsidePrevented") or g.get("spaceOutside") == "running":
                bad("Space was taken from outside the floating timer")
            if not g.get("spaceInsidePrevented") or g.get("spaceInside") != "running":
                bad("Space did not toggle with focus inside the float (%r)"
                    % g.get("spaceInside"))
            if not g.get("closedGone"):
                bad("the timer's close control left it on the page")
            if g.get("pickView") != "float" or g.get("pickPressed1") != "true" \
                    or g.get("pickTimerPressed0") != "false":
                bad("the picker's Timer button: view %r, aria-pressed %r -> %r "
                    "(wanted float, false -> true)"
                    % (g.get("pickView"), g.get("pickTimerPressed0"),
                       g.get("pickPressed1")))
            if g.get("footerCovered"):
                bad("the floating timer covers the picker's own control(s) %r"
                    % g.get("footerCovered"))
            if not g.get("pickerStillOpen") or not g.get("zAbovePicker"):
                bad("the floating timer is not over a still-open picker")
            if not g.get("survivesPickerClose"):
                bad("a running timer did not survive the picker closing")
            if g.get("promoted") != "full":
                bad("the picker's Timer button did not bring the open timer "
                    "to full (%r)" % g.get("promoted"))
            if g.get("escPrevented") is not True or not g.get("escPickerOpen") \
                    or g.get("escView") != "float":
                bad("Escape over a running full timer: view %r, picker open "
                    "%r — it must shrink the timer and leave the picker alone"
                    % (g.get("escView"), g.get("escPickerOpen")))
            if g.get("escSecondPicker") or not g.get("escSecondTimer"):
                bad("the next Escape should close the picker and leave the "
                    "floating timer (%r / %r)"
                    % (g.get("escSecondPicker"), g.get("escSecondTimer")))
            st = g.get("storage") or {}
            if st.get("local") or st.get("session"):
                bad("the timer wrote storage: %r" % st)
            if g.get("requests"):
                bad("the timer made %d request(s)" % g["requests"])
        _reload(page, port, width, height)
        res = json.loads(page.eval(wrap(TIMER_PRE, """
          await openPicker();
          window.MrBadmusTimer.open({view: 'full'}); await frame();
          key(document, 'Escape'); await frame();
          out.timerGone = !tm();
          out.pickerOpen = !!host.querySelector('[data-mrb-picker]');
          key(document, 'Escape'); await frame();
          out.pickerGone = !host.querySelector('[data-mrb-picker]');
          return JSON.stringify(out);""")))
        if not (res.get("timerGone") and res.get("pickerOpen")
                and res.get("pickerGone")):
            bad("Escape over an idle full timer should close only the timer, "
                "then the picker: %r" % res)

    print("     %-6s settings/timer: weight ratio %s" % ("%dpx" % width,
                                                          summary.get("ratio")))
    return P


def secs_of(r):
    try:
        parts = [int(x) for x in str(r).split(":")]
    except ValueError:
        return 0
    t = 0
    for x in parts:
        t = t * 60 + x
    return t


def main(argv):
    shots = None
    if "--shots" in argv:
        shots = argv[argv.index("--shots") + 1]
        os.makedirs(shots, exist_ok=True)

    sys.path.insert(0, REPO)
    import ks3_browser as cdp

    if not os.path.exists(os.path.join(REPO, FIXTURE)):
        print("\nteacher_picker_drive.py: not built — %s\n"
              "  Run `python3 build_teacher_port.py` first." % FIXTURE)
        return 1

    print("\n🎲  teacher_picker_drive — the name picker's promises, driven\n")

    server, port = cdp.serve(REPO)
    problems, rows = [], []
    try:
        for width, height in WIDTHS:
            with cdp.Browser() as br:
                page = br.page("http://127.0.0.1:%d/%s" % (port, FIXTURE))
                page.set_viewport(width, height)

                # ⚑ EVERY REQUEST, RECORDED FROM BEFORE THE FIRST PRESS.
                # The claim is "zero writes", and the only honest way to
                # make it from a driven page is to count what left it.
                page.eval("""
                  window.__REQ__ = [];
                  (function () {
                    var f = window.fetch;
                    window.fetch = function () {
                      window.__REQ__.push(['fetch', String(arguments[0])]);
                      return f.apply(this, arguments);
                    };
                    var o = XMLHttpRequest.prototype.open;
                    XMLHttpRequest.prototype.open = function (m, u) {
                      window.__REQ__.push([m, String(u)]);
                      return o.apply(this, arguments);
                    };
                    var b = navigator.sendBeacon;
                    if (b) { navigator.sendBeacon = function (u) {
                      window.__REQ__.push(['beacon', String(u)]);
                      return b.apply(navigator, arguments); }; }
                  }());
                  Object.keys(window.localStorage).length +
                  ':' + Object.keys(window.sessionStorage).length
                """)

                # ── the reveal, proved once, with motion allowed ───────
                mo = json.loads(page.eval(MOTION))
                if not mo.get("busySeen"):
                    problems.append(
                        "%dpx: pressing Pick never raised `aria-busy` on the "
                        "name. The reveal is the whole animation and it is "
                        "also how any drive knows which name was PICKED "
                        "rather than shuffled past." % width)
                elif mo.get("distinct", 0) < 2:
                    problems.append(
                        "%dpx: `aria-busy` was up but the name never moved "
                        "(%d distinct frame(s)) — the shuffle is not "
                        "shuffling." % (width, mo.get("distinct")))
                elif not mo.get("landed"):
                    problems.append(
                        "%dpx: the reveal cleared `aria-busy` with no name "
                        "on the wall." % width)
                elif mo.get("ms", 0) > 2000:
                    problems.append(
                        "%dpx: the reveal took %dms. \"Brief\" is the brief; "
                        "a teacher is waiting in front of a class."
                        % (width, mo.get("ms")))

                # ⚠️ AND NOW THE MOTION GOES AWAY — see the note on `MOTION`.
                # `ks3_browser`'s socket gives up at 60s and the cycle below
                # would spend longer than that on animation alone.
                page.send("Emulation.setEmulatedMedia",
                          {"features": [{"name": "prefers-reduced-motion",
                                         "value": "reduce"}]})

                got = json.loads(page.eval(DRIVE, timeout=300))
                if got.get("error"):
                    problems.append("%dpx: %s" % (width, got["error"]))
                    continue

                if shots:
                    # Board mode, EARLY in a cycle, with a name on the wall
                    # and a live Pick button. ⚠️ The reset is not cosmetic:
                    # the run above leaves the cycle spent, and a photograph
                    # of the exhausted state is a photograph of the one state
                    # the feature is not usually in.
                    page.eval("""(async () => {
                      const h = document.querySelector('#mrb-teacher');
                      const q = m => h.querySelector('[data-mrb-added="' + m + '"]');
                      const f = () => new Promise(r => requestAnimationFrame(r));
                      q('pick-open').click(); await f();
                      if (q('pick-reset')) { q('pick-reset').click(); await f(); }
                      q('pick-go').click(); await f();
                      q('pick-go').click();
                      await new Promise(r => setTimeout(r, 900));
                      return 1; })()""")
                    page.screenshot(
                        os.path.join(shots, "picker-board-%d.png" % width),
                        width=width, height=height, full_page=False)
                    page.eval("""(async () => {
                      const h = document.querySelector('#mrb-teacher');
                      h.querySelector('[data-mrb-added="pick-absent"]').click();
                      await new Promise(r => requestAnimationFrame(r));
                      return 1; })()""")
                    page.screenshot(
                        os.path.join(shots, "picker-absent-%d.png" % width),
                        width=width, height=height, full_page=False)
                    page.eval("""document.querySelector('#mrb-teacher')
                        .querySelector('[data-mrb-added="pick-close"]').click()""")

                back = json.loads(page.eval(REOPEN))
                reqs = json.loads(page.eval("JSON.stringify(window.__REQ__)"))

                problems.extend("%dpx: %s" % (width, p)
                                for p in got.get("problems", []))

                if reqs:
                    problems.append(
                        "%dpx: the picker made %d request(s) — %s. It is "
                        "read-only by design and a request is a write path "
                        "nobody ruled." % (width, len(reqs),
                                           "; ".join(" ".join(r) for r in reqs[:4])))
                st = got.get("storage") or {}
                if st.get("local") or st.get("session"):
                    problems.append(
                        "%dpx: the picker left %d localStorage and %d "
                        "sessionStorage key(s). Absences are this lesson's "
                        "business and are not written down."
                        % (width, st.get("local"), st.get("session")))

                ov = got.get("overlay") or {}
                if ov.get("pos") != "fixed" or ov.get("w", 0) < ov.get("vw", 1) \
                        or ov.get("h", 0) < ov.get("vh", 1):
                    problems.append(
                        "%dpx: the reveal is not full-viewport (%sx%s in a "
                        "%sx%s window, position %s) — board mode IS the "
                        "overlay, so a panel is the whole feature missing."
                        % (width, ov.get("w"), ov.get("h"), ov.get("vw"),
                           ov.get("vh"), ov.get("pos")))

                # The name has to be big. 38px is the clamp's floor and the
                # smallest this is allowed to be anywhere.
                if got.get("nameSize", 0) < 38:
                    problems.append(
                        "%dpx: the picked name renders at %spx. The floor is "
                        "38 and the point of the surface is the back of a "
                        "classroom." % (width, got.get("nameSize")))

                want_back = "Picked 0 of %d" % (got.get("M") or 0)
                if back.get("line") == want_back:
                    problems.append(
                        "%dpx: closing and reopening reset the cycle — it "
                        "read %r. The session is the lesson, not the "
                        "overlay." % (width, back.get("line")))

                rows.append((width, got, back, len(reqs)))
                problems.extend(features(cdp, port, width, height))
                here = [p for p in problems if p.startswith("%dpx:" % width)]
                print("     %-6s %s  %d in the pool · cycle of %d · %s away "
                      "· %d random roll(s) · %d request(s)"
                      % ("%dpx" % width, "❌" if here else "✅",
                         got.get("M"), len(got.get("cycle") or []),
                         json.dumps(got.get("away")), got.get("rolls"),
                         len(reqs)))
    finally:
        server.shutdown()

    print()
    if problems:
        print("  FAIL  %d problem(s):\n" % len(problems))
        for p in problems:
            print("     · %s" % p)
        print()
        return 1
    print("  PASS  %d width(s). No-repeats never repeated, the count line "
          "agreed with\n        every press, Start again restored the pool, a "
          "student marked away was\n        never picked in a whole cycle, "
          "Random repeated where the cycle could not,\n        the reveal "
          "filled the viewport at the display scale, and the whole run\n"
          "        made ZERO requests and wrote ZERO storage keys.\n"
          "        Weights drew tickets (about 5x in Random, exactly w per "
          "cycle), pick next\n        landed once through the ordinary "
          "reveal, Save kept one per-class key and\n        nothing else, "
          "and the timer counted, warned, finished and wrote nothing.\n"
          % len(WIDTHS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
