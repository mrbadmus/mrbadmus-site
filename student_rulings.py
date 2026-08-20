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
