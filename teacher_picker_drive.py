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

    5. IT WRITES NOTHING. Every request the page makes is recorded, and a
       whole cycle of presses — plus a reset, plus marking somebody absent
       — must add not one. Storage is checked the same way: `localStorage`
       and `sessionStorage` are empty before and after.

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
          % len(WIDTHS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
