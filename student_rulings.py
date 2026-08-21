#!/usr/bin/env python3
"""student_rulings.py — Mide's MRB-275 rulings, as source rather than as an edit.

⚠️ WHY THIS FILE EXISTS, AND WHAT IT IS RECOVERING FROM.

The three rulings of 21 Aug 2026 were applied on 20 Aug in commit 895f34766 —
correctly, carefully, and IN THE WRONG PLACE. That commit touched four files:

    mrbadmus_site/student/class-ported.html
    mrbadmus_site/student/assignment-ported.html
    student/class-ported.html
    student/assignment-ported.html

Every one of those is GENERATED OUTPUT. `build_student_port.py` writes all four
from `student_templates.json`, and its own banner says "GENERATED — do not
edit". So the rulings held for exactly as long as nobody re-ran the build. The
next run — this one — silently reverted all three, and the behaviour gate went
red in thirteen places naming a divergence that had been correct that morning.

That commit's own message diagnosed the neighbouring version of this mistake
("it drove last night's file and reported 28 healthy drives about code that no
longer existed") and then made this one, because `student/class-ported.html`
sits in the repo root and reads like source. It is not. It is the mirror.

So the rulings live HERE now, as transformations applied to Design's logic and
Design's template at build time, and a rebuild carries them rather than
destroying them. The content of every one is unchanged — each `new` below is
byte-for-byte what 895f34766 wrote, extracted from that commit rather than
retyped, and the build asserts that each `old` appears EXACTLY ONCE in Design's
delivery before touching it. If Design redraws that span, the build stops
rather than applying a ruling to a line that has moved.

── THE THREE RULINGS ─────────────────────────────────────────────────────

1a  The right answer's feedback line is dropped for v1, and the slot CLOSES
    rather than standing empty. (`assignment`, six replacements.)
1b  The leaderboard bar shows the TOTAL; the ON TIME / SCORE / RECALL split is
    omitted entirely, along with the leader's hero bar, the three-column
    figures and the static "40 / 40 / 20" legend. (`class view`, four
    replacements plus seven pruned template nodes.)

Both are also asserted from the other side, in `student_behaviour.py`'s
RULED_DIVERGENCE and in `student_parity.py`: present in Design's own delivery,
absent from the port. Those gates are what catch this file rotting.
"""

# ── template nodes the ruling removes, by `data-dc-tpl` index ────────────
#
# Each is the ROOT of a subtree; its descendants go with it. Measured against
# 895f34766, not guessed: pruning exactly these seven reproduces that commit's
# template node-for-node, and the build re-checks the count it removed.
#
#   275, 279   the leader's three-column ON TIME / SCORE / RECALL figures
#   297, 298   the leader's hero split bar
#   322 … 330  the static "ON TIME · 40 / SCORE · 40 / RECALL · 20" legend
PRUNE = {
    "class view": [275, 279, 297, 298, 322, 325, 328],
}

# ── the logic, transformed ───────────────────────────────────────────────
#
# (old, new). `old` must occur exactly once in Design's logic class, or the
# build stops — see `apply_rulings` in build_student_port.py. Order matters
# only in that each is applied to the result of the last.
LOGIC = {
    'class view': [
        (
            "        monoBorder: r.me ? 'var(--st-accent)' : 'var(--st-edge)',\n        barWidth: Math.round((r.pts / maxPts) * 100) + '%',",
            '        monoBorder: r.me ? \'var(--st-accent)\' : \'var(--st-edge)\',\n        /* ⊕ RULED 21 Aug 2026 — the bar shows the TOTAL, and the ON TIME /\n           SCORE / RECALL split is omitted entirely. `barWidth` is the total:\n           this student\'s points against the class maximum, which is a real\n           comparison and stays. The three sub-widths that used to fill it are\n           gone, along with the leader\'s hero bar, the leader\'s three-column\n           figures and the static "ON TIME · 40 / SCORE · 40 / RECALL · 20"\n           legend (template nodes 275-283, 295-298, 322-330).\n\n           ON TIME and SCORE are both computable — due_at against the submission\n           timestamp, and score against max_score. RECALL is not: nothing\n           anywhere records a recall round, `quiz_scores` carries neither a\n           class nor a teaching week, and `quiz_question_attempts` has no\n           question_ref to resolve an answer back to a rung. A bar showing two\n           of three components is a different lie from one showing three\n           fabricated ones, and it is still one.\n\n           What it would take to make the split honest is measured and costed on\n           MRB-275. Do not restore any of this until that lands — student_parity\n           layer F already fails the build if Design\'s 0.4 / 0.19 drawing\n           constants reappear. */\n        barWidth: Math.round((r.pts / maxPts) * 100) + \'%\',',
        ),
        (
            "        wOnTime: Math.round((r.onT / r.pts) * 100) + '%',\n        wScore: Math.round((r.sc / r.pts) * 100) + '%',\n        wRecall: Math.round((r.rec / r.pts) * 100) + '%',",
            '',
        ),
        (
            "      deltaText: top.me ? 'THAT IS YOU' : pad(top.pts - (table[1] ? table[1].pts : 0)) + ' POINTS CLEAR',\n      wOnTime: Math.round((top.onT / top.pts) * 100) + '%',\n      wScore: Math.round((top.sc / top.pts) * 100) + '%',\n      wRecall: Math.round((top.rec / top.pts) * 100) + '%',\n      parts: [{ label: 'ON TIME', value: top.onT }, { label: 'SCORE', value: top.sc }, { label: 'RECALL', value: top.rec }].map((p, i) => Object.assign(p, { edge: i < 2 ? '1px solid var(--st-room-line)' : 'none' }))",
            "      deltaText: top.me ? 'THAT IS YOU' : pad(top.pts - (table[1] ? table[1].pts : 0)) + ' POINTS CLEAR'\n      /* the leader's split bar and its three-column figures are gone — see the\n         ruling note on `barWidth` above. `leader.points` directly above them is\n         the total, so nothing is lost by removing the bar: at 100% of the\n         leader's own points it was always full and said nothing anyway. */",
        ),
        (
            "        barWidth: Math.round((r.pts / maxPts) * 100) + '%',\n\n        up: d.up, down: d.down, flat: d.flat",
            "        barWidth: Math.round((r.pts / maxPts) * 100) + '%',\n        up: d.up, down: d.down, flat: d.flat",
        ),
    ],
    'assignment': [
        (
            '    const n = Math.round(this.props.questionCount ?? 15);\n    return Math.max(6, Math.min(this.questions.length, n));',
            '    /* ⊕ RULED 22 Aug 2026 — THE FLOOR OF SIX IS THE BUG. THE CAP IS NOT.\n\n       Design\'s own assignment note requires the marker strip to read the real\n       length — "it does not assume fifteen" — and the floor of SIX broke that\n       in the direction that mattered: with four real questions this returned\n       6, the page then indexed `questions[4]` and `questions[5]`, found\n       undefined, and refused to open. The refusal was honest. The floor was\n       wrong. It drops to 1, which is the only number that is not an\n       assumption.\n\n       ⚠️ THE `?? 15` STAYS, and the first draft of this ruling removed it and\n       went red. It reads like an inert default — nothing passes\n       `questionCount`; the mount emits `props: {}` — but Design\'s own fixture\n       array is SIXTEEN questions long and Design renders fifteen, so the 15 is\n       a working CAP that `Math.min` applies, not a fallback that never fires.\n       Taking it out made the fixture render "16 QUESTIONS" and diverged nine\n       behaviour drives at the same character.\n\n       And 15 is the right cap, independently: `ASSIGNMENT_SIZE` in\n       `assignment-compose.js` is 15, so the producer never composes more. A\n       real assignment SHORTER than 15 now shows its real length, which is the\n       whole point; a longer one cannot exist. Proved at 4, 6, 12 and 15. */\n    const n = Math.round(this.props.questionCount ?? 15);\n    return Math.max(1, Math.min(this.questions.length, n));',
        ),
        (
            'class Component extends DCLogic {',
            "/* ⊕ RULED 22 Aug 2026 — WHERE A STUDENT'S WORK ACTUALLY GOES.\n\n   `window.__MRB_SINK__` is set by `shared/student-live.js` immediately before\n   it mounts, and by nothing else. It is a WRITER, not a data source: the page\n   still reads everything it renders through `MRB_DATA`, and the rule that the\n   production page has no code path to Design's example data is untouched.\n\n   It is read LAZILY, on every call, and never captured at script-evaluation\n   time — the logic script runs before `student-live.js` has loaded, so a\n   captured reference would be null forever and every answer would be silently\n   dropped. That is precisely the failure this whole unit exists to remove, and\n   it would have been invisible.\n\n   On the fixture page there is no sink, every call is a no-op returning null,\n   and Design's behaviour is exactly what it was. That is deliberate: the gates\n   drive the fixture, and a gate that had to reach a network would not be a\n   gate. */\nfunction _sink() {\n  return (typeof window !== 'undefined' && window.__MRB_SINK__) || null;\n}\nfunction _sinkCall(name, arg) {\n  var s = _sink();\n  if (!s || typeof s[name] !== 'function') { return null; }\n  /* A save that throws must never take the answer off the screen with it. The\n     student answered; what happens to the network afterwards is not their\n     problem and is not their feedback. */\n  try { return s[name](arg); } catch (e) { return null; }\n}\nclass Component extends DCLogic {",
        ),
        (
            '    const off = this.isOffline();\n    this.lastAct = Date.now();\n    this.setState((p) => {\n      const a = Object.assign({}, p.answers); a[p.idx] = oi;\n      const h = Object.assign({}, p.held); if (off) h[p.idx] = 1;\n      return { answers: a, held: h, resumed: false, paused: false };\n    }, () => this.saveLive());',
            "    const off = this.isOffline();\n    const at = s.idx;\n    this.lastAct = Date.now();\n    this.setState((p) => {\n      const a = Object.assign({}, p.answers); a[p.idx] = oi;\n      const h = Object.assign({}, p.held); if (off) h[p.idx] = 1;\n      return { answers: a, held: h, resumed: false, paused: false };\n    }, () => {\n      this.saveLive();\n      /* ⊕ RULED 22 Aug 2026 — W1. THE ANSWER GOES TO THE SERVER HERE, NOW.\n         Not batched, not held until the end: the submission row is created by\n         the first of these and the work is safe from question one. The call is\n         idempotent per (submission, question) at the database, so changing an\n         answer updates that row rather than adding a second — which is why\n         re-confirming is harmless and why no bookkeeping is needed here.\n         The offline queue lives in the sink, not in Design's logic; `held` and\n         `drain` stay exactly what Design drew them as, which is the UI telling\n         the student what it knows. */\n      _sinkCall('saveAnswer', { index: at, option: oi, offline: off });\n    });",
        ),
        (
            "  handIn = () => {\n    const stamp = this.state.late ? '20 SEP, 19:07' : '17 SEP, 20:41';\n    this.setState({ handing: true, handedAt: stamp, sheet: false, zoom: false }, () => this.saveLive());\n    clearTimeout(this.handT);\n    this.handT = setTimeout(() => this.setState({ handing: false, view: 'done' }, () => this.saveLive()), 1350);\n  };",
            "  /* ⊕ RULED 22 Aug 2026 — W3. THIS BUTTON MARKS THE WORK FINISHED.\n     IT DOES NOT SAVE IT. Saving already happened, one answer at a time.\n\n     ⛔ WHAT THIS REPLACES, because it is the worst defect the page had and the\n     reason the swap was refused twice:\n\n         const stamp = this.state.late ? '20 SEP, 19:07' : '17 SEP, 20:41';\n\n     A HARDCODED DATE, posted to NO ENDPOINT. A student pressing it was told\n     they handed in on 17 September, whatever today was, and their work never\n     reached their teacher. A false confirmation is worse than a visible\n     failure, because the student stops worrying about it.\n\n     Now the stamp comes back from the server or it does not appear at all.\n     `is_late` comes back with it — lateness is a fact about the clock decided\n     once, at the database, and never a guess made on the device. Nothing here\n     checks the due date, because nothing is locked by it (ruling 5).\n\n     Idempotent at both ends: this returns early if a completion is already in\n     flight or done, and the route returns the first press's row if it is not. */\n  handIn = () => {\n    if (this.state.handedAt || this.state.handing) return;\n    this.setState({ handing: true, sheet: false, zoom: false }, () => this.saveLive());\n    clearTimeout(this.handT);\n    const settle = (r) => {\n      this.setState((p) => ({\n        handing: false, view: 'done',\n        handedAt: (r && r.stamp) || '',\n        late: r && r.late != null ? !!r.late : p.late\n      }), () => this.saveLive());\n    };\n    const out = _sinkCall('complete', this.state.elapsed);\n    if (out && typeof out.then === 'function') {\n      /* The catch settles rather than rethrowing: a student who has finished\n         must reach the end screen even if the confirmation does not arrive.\n         Their answers are already saved, and the completion is retried by the\n         next visit, which reads its state from the server. */\n      out.then(settle, function () { settle(null); });\n      return;\n    }\n    this.handT = setTimeout(() => settle(out), 1350);\n  };",
        ),
        (
            "  loadLive() {\n    const empty = { answers: {}, sels: {}, held: {}, idx: 0, elapsed: 0, view: 'q', handedAt: null, resumed: false, late: false, sheet: false, zoom: false, handing: false, net: null };\n    try {",
            "  loadLive() {\n    const empty = { answers: {}, sels: {}, held: {}, idx: 0, elapsed: 0, view: 'q', handedAt: null, resumed: false, late: false, sheet: false, zoom: false, handing: false, net: null };\n    /* ⊕ RULED 22 Aug 2026 — W2. THE SERVER IS THE TRUTH; THE BROWSER IS A CACHE.\n       A student on the school computer on Monday and their phone on Thursday\n       must see the same state, and localStorage cannot do that — it is per\n       device and it is per browser profile. So when there is a sink, its\n       resume state wins outright and the local copy is not even consulted.\n       Without one (the fixture, and only the fixture) Design's localStorage\n       behaviour is exactly what it was. */\n    const fromServer = _sinkCall('resume', null);\n    if (fromServer) { return Object.assign(empty, fromServer); }\n    try {",
        ),
        (
            "  applyScenario(scn) {\n    const live = scn === 'Live, saved';",
            "  applyScenario(scn) {\n    /* ⊕ RULED 22 Aug 2026 — DEMO SCENARIOS ARE NOT REACHABLE IN PRODUCTION.\n       Design routes the scenario off the URL hash and falls back to 'Mid-way',\n       which pre-fills six answers with three deliberately wrong. On a real\n       student's assignment that is not a default, it is a lie — and worse, the\n       'Handed in' scenarios would show a child a completion that never\n       happened. A live page must not be able to reach any of them by hash.\n\n       When a sink is present there is exactly one scenario and it is the\n       student's own saved state. This replaces the `#live` history rewrite\n       `student-live.js` was doing from outside, which the last run recorded as\n       a workaround belonging in the page. It now is in the page. */\n    if (_sink()) { scn = 'Live, saved'; }\n    const live = scn === 'Live, saved';",
        ),
        (
            "      screenLabel: onDone ? (st.late ? 'Handed in late' : 'Handed in') : handed ? 'Review' : 'Question ' + pad(idx + 1),",
            "      /* ⊕ RULED 22 Aug 2026 — W5. “Complete” replaces the old wording everywhere.\n         The button marks the work finished; it does not transfer it, because\n         the transfer happened one answer at a time all week. Design's\n         typography and placement are untouched — only the words change. */\n      screenLabel: onDone ? (st.late ? 'Completed late' : 'Complete') : handed ? 'Review' : 'Question ' + pad(idx + 1),",
        ),
        (
            "      doneEyebrow: 'Handed in ' + (st.handedAt || '') + (st.late ? ' \\u00B7 2 days late' : ''),",
            '      /* The stamp is whatever the server said, and nothing when it said\n         nothing — never a manufactured date. The separator goes with it, so an\n         absent stamp leaves "Completed" rather than "Completed ·". */\n      doneEyebrow: \'Completed\' + (st.handedAt ? \' \' + st.handedAt : \'\') + (st.late ? \' \\u00B7 \' + MRB_DATA(\'lateText\') : \'\'),',
        ),
        (
            "      doneKicker: st.late ? 'Marked \\u00B7 handed in late' : 'Marked \\u00B7 week 04',",
            "      doneKicker: st.late ? 'Marked \\u00B7 completed late' : (MRB_DATA('weekLabel') ? 'Marked \\u00B7 ' + MRB_DATA('weekLabel').toLowerCase() : 'Marked'),",
        ),
        (
            "      headMeta: 'WEEK 04 \\u00B7 ' + total + ' QUESTIONS',\n      dueLead: 'CELLS & MICROSCOPY \\u00B7 ' + this.DUE,\n      dueFlag: st.late ? '\\u00B7 2 DAYS LATE' : '',",
            '      /* ⊕ RULED 22 Aug 2026 — three welded values in one line of Design\'s.\n         The week was 04 for every class in every week of every year; the topic\n         was one real class\'s; and "2 DAYS LATE" was a fixed number of days\n         printed over whatever the real overdue period happened to be.\n         `topicTitle` is already bound from the markup, so nothing new is\n         carried for it — the same key, upper-cased for this position. */\n      headMeta: (MRB_DATA(\'weekLabel\') ? MRB_DATA(\'weekLabel\') + \' \\u00B7 \' : \'\') + total + \' QUESTIONS\',\n      dueLead: MRB_DATA(\'topicTitle\').toUpperCase() + \' \\u00B7 \' + this.DUE,\n      dueFlag: st.late ? \'\\u00B7 \' + MRB_DATA(\'lateText\').toUpperCase() : \'\',',
        ),
        (
            'class Component extends DCLogic {',
            '\n/* One definition of "is this feedback line actually authored", used by both the\n   places a line surfaces: the option card while answering, and the review screen\n   at the end. See the ⊕ RULED 21 Aug note above `noteBlock` for why the right\n   answer\'s line is absent and why the slot must close rather than blank.\n   Returns \'\' — never undefined — so a missing line renders as the same closed\n   slot the idle and off states already produce, not as the string "undefined". */\nfunction _line(q, i) {\n  var s = q && q.f && q.f[i];\n  return (typeof s === \'string\' && s.trim()) ? s : \'\';\n}\nclass Component extends DCLogic {',
        ),
        (
            '    const sel = st.sels[idx];\n    const options = q.o.map((t, i) => {',
            '    const sel = st.sels[idx];\n    /* ⊕ RULED 21 Aug 2026 — the right answer\'s explanation line is DROPPED for v1,\n       and the slot must CLOSE rather than stand empty.\n\n       Design\'s §2 asks for four feedback strings per question so the pair reads\n       "why not that / why this". Measured across both content sources — 140 ladder\n       recall/apply rungs and 840 bank questions — the three that exist are always\n       the DISTRACTORS, and "why this" is authored nowhere. Authoring 980 pieces of\n       science prose is a term\'s work and it is Mide\'s gate, not the build\'s.\n\n       Ruled: v1 ships with three. The right answer is marked correct by the tick\n       and the word, with no line beneath it. The reasoning, recorded rather than\n       just obeyed: the teaching in a multiple-choice question lands on the MISTAKE.\n       A student who chose correctly does not need a paragraph confirming it, and\n       the lesson page is where the real explanation lives.\n\n       ⚠️ NOT a blanket suppression, and this is the one place the ruling is read\n       less than literally. `noteBlock` renders a line that IS authored and closes\n       the slot when one is not — because the same ruling says authored lines are\n       "content and welcome", and Design\'s own example data carries all four (its\n       right-answer lines open "Right. …"). Once the pages are wired to the real\n       content sources in phase 2, no correct option has a line anywhere, so both\n       readings ship exactly the same v1. This one just does not destroy the slot\n       on the way, and a fallback string appearing in 840 places is the thing\n       Design forbade — gated separately in student_parity.py.\n\n       Closing means dropping noteRule and noteColor too, not just blanking `note`.\n       Those carry the rule above the line and its padding; leaving them behind is\n       precisely the gap the ruling says must not appear. `idle` and `off` already\n       close it this way, which is the shape being matched. */\n    const noteBlock = (i, rule, color) => {\n      const s = _line(q, i);\n      return s ? { note: s, noteRule: rule, noteColor: color } : { note: \'\' };\n    };\n\n    const options = q.o.map((t, i) => {',
        ),
        (
            "        markColor: 'var(--ks3-ok-text)', status: 'RIGHT', statusColor: 'var(--ks3-ok-text)',\n        note: q.f[i], noteRule: 'var(--ok-border)', noteColor: 'var(--st-body)'\n      });",
            "        markColor: 'var(--ks3-ok-text)', status: 'RIGHT', statusColor: 'var(--ks3-ok-text)'\n      }, noteBlock(i, 'var(--ok-border)', 'var(--st-body)'));",
        ),
        (
            "        markColor: 'var(--err)', status: 'NOT THIS ONE', statusColor: 'var(--err)',\n        note: q.f[i], noteRule: 'var(--err-border)', noteColor: 'var(--st-body)'\n      });",
            "        markColor: 'var(--err)', status: 'NOT THIS ONE', statusColor: 'var(--err)'\n      }, noteBlock(i, 'var(--err-border)', 'var(--st-body)'));",
        ),
        (
            "        markColor: 'var(--ks3-ok)', status: 'THE ANSWER', statusColor: 'var(--ks3-ok-text)',\n        note: q.f[i], noteRule: 'var(--st-rule-soft)', noteColor: 'var(--st-muted)'\n      });",
            "        markColor: 'var(--ks3-ok)', status: 'THE ANSWER', statusColor: 'var(--ks3-ok-text)'\n      }, noteBlock(i, 'var(--st-rule-soft)', 'var(--st-muted)'));",
        ),
        (
            '        yourKey: keys[a], yourText: qq.o[a], yourNote: qq.f[a],\n        ansKey: keys[qq.a], ansText: qq.o[qq.a], ansNote: qq.f[qq.a],',
            "        yourKey: keys[a], yourText: qq.o[a], yourNote: _line(qq, a),\n        /* the correct option's line, closed when unauthored — see noteBlock above.\n           The review screen is the SECOND place it surfaces, and it was missed on\n           the first pass: closing it only on the question card would have left the\n           end-of-assignment review showing an empty rule under every right answer. */\n        ansKey: keys[qq.a], ansText: qq.o[qq.a], ansNote: _line(qq, qq.a),",
        ),
    ],
}
