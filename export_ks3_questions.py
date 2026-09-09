#!/usr/bin/env python3
"""export_ks3_questions.py — mirror the KS3 question pools into Postgres.

    python3 export_ks3_questions.py            # write SQL under build/ks3-questions/
    python3 export_ks3_questions.py --json     # write bank/ladder/cards.json for the RPC
    python3 export_ks3_questions.py --stdout   # one statement per line, to stdout
    python3 export_ks3_questions.py --check    # counts only, write nothing
    python3 export_ks3_questions.py --verify   # ⭐ THE GATE: does the database still
                                               #   match Python, row for row?
    python3 export_ks3_questions.py --verify --project test    # …on TEST instead

── Why this exists ──────────────────────────────────────────────────────

`compose_assignment()` and the 70 question modules are Python, in this repo.
The thing that has to CALL them — the on-demand assignment producer — lives in
the Node backend, in a different repo. There are three ways to bridge that and
only one of them keeps a question written in exactly one place:

  1. Re-implement the bank in Node.          70 files of content, duplicated.
  2. Vendor a JSON copy into the backend.    Still a copy. Still drifts.
  3. Mirror it into the database. ← this.

The tables are a BUILD ARTEFACT, the way `mrbadmus_site/` is. Python is the
source; this script is the only writer; the export is idempotent, so running it
twice changes nothing and running it after an edit changes exactly what was
edited. Nothing here authors a question and nothing here may be hand-edited in
the database.

It also buys something the wiring needed anyway: with the pools in Postgres the
assignment page can read a question's text, its four options, their letters and
the per-distractor `why` in one query — instead of fetching the lesson's built
HTML page and scraping `.ks3-option[data-correct]` out of the DOM, which is what
`student/assignment.html:96` has had to do, and which breaks the moment the
lesson template changes a class name.

── The three pools are not the same shape ───────────────────────────────

**The bank** (`ks3_data/<unit>/questions_*.py`) is AT LEAST twelve questions per
lesson and at least four per band, each option carrying a `why` for every wrong
answer. It is what a weekly assignment is drawn from — and, since MRB-335, what
Set work lets a teacher choose from by hand.

⊕ It used to be EXACTLY twelve, and the difference is load-bearing rather than
cosmetic. `bank_position` 0–11 still hold the original four per band, in the
order they have always had, because that window is all AUTO composition reads
(`compose_assignment` here, `bankFor()` in the backend). Everything a top-up
adds lands at position ≥ 12, where only Set work can see it. That is what makes
growing the bank safe: an assignment auto-composed before a top-up and one
composed after it are the same fifteen questions.

**The ladder** (`LESSON["ladder"]`) is the four rungs at the foot of each lesson
page. Only `recall` and `apply` are exported: they are multiple choice and have
a right answer. `explain` and `produce` are marked BY THE STUDENT against
success criteria — nothing can score them, so nothing can put them in a recall
round.

**The cards** (`LESSON["vocabulary"]`, and the `equation` records nested in
`LESSON["core"]`) are the flashcard deck. Two kinds ship, and both are pairs
somebody already AUTHORED as a question and its answer:

  * `definition` — one per vocabulary entry. 573 of them, in all 107 lessons.
  * `equation`   — one per authored word equation. 9 of them, in 7 lessons.

`key_fact` is a KIND THE SCHEMA ACCEPTS AND THIS EXPORTER NEVER EMITS. A key
fact is a STATEMENT, not a pair: `key_facts[].text` would be the back and
nothing in the record is the front. `big_question` is the obvious candidate and
is unusable — a median of 148 characters, 87 of the 107 over 120 — so a front
would have to be WRITTEN, and writing a science prompt for 107 lessons is
Mide's gate, not an export. The slot is in the schema so that the day those
fronts are authored, the migration does not move.

⚠️ **The right-answer feedback slot is left CLOSED.** A ladder authors three
feedback strings, one for each wrong option. The correct option has none, and
this exporter writes `why: null` for it rather than inventing a fourth. That is
the standing ruling and it is what `student_parity.py` layer H is watching for:
a generic "Correct!" is not teaching, and a reused string is worse than silence.
"""

import argparse
import importlib
import json
import os
import pkgutil
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

OUT_DIR = os.path.join("build", "ks3-questions")

# ⚠️ SMALL ON PURPOSE. Each row is a question, four options and four feedback
# strings — around a kilobyte of JSON — so 40 rows is roughly 38 kB per
# statement. A first attempt used 120 and the load stalled part-way through;
# whatever the ceiling is, it is not worth finding by binary search on a
# production table. 28 small statements apply in well under a minute and any
# one of them can be re-run on its own, because they are upserts.
ROWS_PER_STATEMENT = 250

LETTERS = ("A", "B", "C", "D")

# Ladder keys that are not rungs. `retry_note` and `sub` are authoring notes
# that live alongside the rungs in the same dict.
NOT_A_RUNG = {"retry_note", "sub"}
MARKED_RUNGS = ("recall", "apply")


def checksum(rows, columns):
    """One SHA-256 over a whole pool, computed identically on both sides.

    ⊕ MRB-335 (7 Sep 2026). KS4's exporter has had this since MRB-332; KS3's
    had only the row-by-row comparison. The comparison is still the check —
    it names the rows and the fields that differ. The checksum is the thing you
    can WRITE DOWN: one value a report, a commit message or a person three
    months from now can hold against another run without re-reading 2,220
    rows. It matters most on the run that FAILS, because it is what tells you
    whether you are looking at the same wrong database or a different one.

    ⚠️ It only earns that by being canonical about CONTENT rather than about
    transport:

      · rows sorted by their key, so page order cannot change the answer;
      · every column including the key, so a renamed question checksums
        differently even with identical wording;
      · `bank_position` included — the whole of RISKS D7 is a statement about
        position, so a row that moved must not checksum the same;
      · `options` walked IN ORDER and never sorted, because the correct answer
        is identified by its place in that sequence;
      · every scalar through `str()` and None through a single sentinel,
        because PostgREST hands back JSON types where Python holds native
        ones, and a checksum that changed with the wire format would be a
        checksum of the wire format.
    """
    import hashlib
    key = columns[0]
    h = hashlib.sha256()
    for r in sorted(rows, key=lambda r: str(r[key])):
        for f in columns:
            v = r.get(f)
            if isinstance(v, list):
                v = "\u001f".join(
                    json.dumps(o, sort_keys=True, ensure_ascii=False)
                    if isinstance(o, dict) else str(o)
                    for o in v)
            elif v is None:
                v = "null"
            elif isinstance(v, bool):
                v = "1" if v else "0"
            h.update(("%s=%s" % (f, v)).encode("utf-8"))
        h.update(b"\x02")
    return h.hexdigest()


def sql_str(v):
    """A Postgres string literal, or NULL."""
    if v is None:
        return "null"
    return "'" + str(v).replace("'", "''") + "'"


def sql_json(v):
    return sql_str(json.dumps(v, ensure_ascii=False, separators=(",", ":"))) + "::jsonb"


# ── the bank ─────────────────────────────────────────────────────────────

def bank_rows():
    """Every bank question, in bank order.

    `bank_position` is the question's index inside its own module. That
    ordering is what makes `compose_assignment` deterministic — it takes
    questions in bank order — so it has to survive the trip into the database
    or the producer would compose a different assignment from the same inputs.

    ⊕ MRB-335 — A LESSON MAY NOW BE ANY LENGTH, AND POSITION BECAME LOAD-
    BEARING RATHER THAN MERELY DETERMINISTIC. `enumerate` already exported
    every row at whatever index it sat at, so nothing here had to change to
    carry a top-up; what changed is what a position MEANS. `bank_position < 12`
    is the auto-composition window in both mirrors — `compose_assignment` here
    and `bankFor()` in the Node backend — and Set work reads every position.
    So the shape of the first twelve is now checked ON THE WAY OUT as well as
    by the gate: the database must never be able to hold a bank the gate would
    have refused, because the database is what a class is actually served
    from and it outlives any one run of `verify_questions.py`.
    """
    import ks3_data.question_bank as qb

    rows = []
    by_lesson = qb.bank_by_lesson()

    bad = []
    for record in qb.load_bank():
        for check, qid, message in qb.validate_lesson(record):
            bad.append("%s%s: %s"
                       % (record["module"],
                          " [%s]" % qid if qid else "", message))
    if bad:
        raise SystemExit(
            "export_ks3_questions: the bank does not satisfy "
            "question_bank.validate_lesson, so it must not be mirrored:\n"
            + "\n".join("  · " + b for b in bad[:20])
            + ("\n  … and %d more" % (len(bad) - 20) if len(bad) > 20 else "")
            + "\n\nRun `python3 -m ks3_data.question_bank` for the full list.")

    for (unit_code, lesson_slug) in sorted(by_lesson):
        for pos, q in enumerate(by_lesson[(unit_code, lesson_slug)]):
            opts = q.get("options") or []
            if len(opts) != 4:
                raise SystemExit(
                    "export_ks3_questions: %s has %d option(s), expected 4"
                    % (q.get("id"), len(opts)))
            if sum(1 for o in opts if o.get("correct")) != 1:
                raise SystemExit(
                    "export_ks3_questions: %s does not have exactly one "
                    "correct option" % q.get("id"))
            rows.append(dict(
                id=q["id"],
                unit_code=unit_code,
                lesson_slug=lesson_slug,
                band=q["band"],
                bank_position=pos,
                text=q["text"],
                figure=q.get("figure"),
                options=[
                    dict(text=o["text"],
                         correct=bool(o.get("correct")),
                         # The correct option carries no `why` in the bank
                         # either — the field is the misconception behind a
                         # DISTRACTOR. Kept null rather than absent so the
                         # shape is the same for all four.
                         why=o.get("why"))
                    for o in opts
                ],
            ))
    return rows


# ── the ladder ───────────────────────────────────────────────────────────

def lesson_modules():
    """Every authored lesson module, as (unit_code, module)."""
    import ks3_data

    found = []
    for unit in sorted(m.name for m in pkgutil.iter_modules(ks3_data.__path__)
                       if m.ispkg):
        pkg_dir = os.path.join(REPO, "ks3_data", unit)
        for fname in sorted(os.listdir(pkg_dir)):
            if not (fname.startswith("lesson_") and fname.endswith(".py")):
                continue
            mod = importlib.import_module("ks3_data.%s.%s" % (unit, fname[:-3]))
            if getattr(mod, "LESSON", None) is not None:
                found.append((unit.upper(), mod))
    return found


def ladder_rows():
    rows = []
    for unit_code, mod in lesson_modules():
        lesson = mod.LESSON
        slug = lesson.get("slug")
        ladder = lesson.get("ladder") or {}
        if not slug:
            raise SystemExit(
                "export_ks3_questions: %s has a ladder but no slug" % mod.__name__)
        for rung in MARKED_RUNGS:
            r = ladder.get(rung)
            if r is None:
                continue
            opts = r.get("options") or []
            if len(opts) != 4:
                raise SystemExit(
                    "export_ks3_questions: %s#%s has %d option(s), expected 4"
                    % (slug, rung, len(opts)))
            answer = r.get("answer")
            if not isinstance(answer, int) or not (0 <= answer < 4):
                raise SystemExit(
                    "export_ks3_questions: %s#%s has answer=%r, expected an "
                    "index 0-3" % (slug, rung, answer))
            # `feedback` is keyed by the index of the WRONG option it corrects.
            # Authored files use int keys; be tolerant of str keys too.
            fb = r.get("feedback") or {}
            fb = {int(k): v for k, v in fb.items()}
            missing = [i for i in range(4) if i != answer and i not in fb]
            if missing:
                raise SystemExit(
                    "export_ks3_questions: %s#%s has no feedback for wrong "
                    "option(s) %s — every distractor must name the "
                    "misconception it represents"
                    % (slug, rung, ", ".join(LETTERS[i] for i in missing)))
            rows.append(dict(
                question_ref="%s#%s" % (slug, rung),
                unit_code=unit_code,
                lesson_slug=slug,
                rung=rung,
                text=r["q"],
                answer_letter=LETTERS[answer],
                options=[
                    dict(letter=LETTERS[i],
                         text=opts[i],
                         correct=(i == answer),
                         # ⚠️ THE RIGHT-ANSWER SLOT IS CLOSED. Null, not a
                         # generic line. See the module docstring.
                         why=(None if i == answer else fb[i]))
                    for i in range(4)
                ],
            ))
    return rows


# ── the cards ────────────────────────────────────────────────────────────

# `key_fact` is accepted by the table and emitted by nothing. See the module
# docstring: a key fact is a statement, and deriving a front for one would mean
# authoring science prompts, which is Mide's gate.
CARD_KINDS = ("definition", "equation", "key_fact")

# The one place a KS3 unit's human title is written down.
def unit_titles():
    from ks3_data.structure import unit_index
    return {code: u["title"] for code, u in unit_index().items()}


# ⚠️ NO MARKUP MAY REACH A CARD FACE, and this asserts it rather than cleaning
# it up. Lesson content DOES carry `<strong>` and `<em>` — `close`, `gloss` and
# `key_facts[].text` are full of it — but the five fields a card is built from
# (`term`, `definition`, `note`, and an equation's two sides) carry none today,
# measured across all 107 lessons.
#
# Both ways of "handling" markup here are defects. Escaping it ships a literal
# `<em>` to a child. Stripping it silently discards emphasis an author chose to
# put there, and the author never learns. So neither: the export FAILS, and
# whoever typed the tag decides — either it comes out, or the card surface
# grows a way to render it and this guard is widened deliberately.
_MARKUP = ("<", "&lt;", "&amp;", "&#")


def _no_markup(where, value):
    for probe in _MARKUP:
        if probe in value:
            raise SystemExit(
                "export_ks3_questions: %s contains markup (%r) — a card face is "
                "plain text and there is nothing on the card that renders a "
                "tag. Take the tag out of the source, or widen the card surface "
                "first and this guard with it: %r"
                % (where, probe, value[:90]))
    return value


def _anchor(text):
    """The id fragment for a card, taken from the words its FRONT asks about.

    ⚠️ THIS IS THE WHOLE POINT OF THE ID SCHEME, so it is worth saying plainly.
    A card's id is `<lesson_slug>#<def|eq>#<anchor>`, and the anchor comes from
    the TERM (a definition) or the LEFT-HAND SIDE (an equation) — never from the
    card's position in the file.

    A positional id survives re-authoring in the sense that nothing is orphaned,
    and fails in the sense that matters: insert one new term at the top of a
    lesson's vocabulary and every id below it now names a DIFFERENT card, so any
    per-card state a student has built up — seen, starred, got-it-wrong —
    silently slides onto the wrong questions. Anchoring on the front means
    reordering moves nothing, rewriting a DEFINITION moves nothing, and the id
    changes only when the question itself changes, which is when it should.
    """
    out = []
    for ch in text.lower():
        if ch.isascii() and (ch.isalnum()):
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    slug = "".join(out).strip("-")
    if not slug:
        raise SystemExit(
            "export_ks3_questions: %r has no id-able characters in it" % text)
    return slug


def _equations(node, path):
    """Every authored `equation`, wherever it nests, in document order.

    They do not all live in one place and they are not all one shape. Measured
    across the 107 lessons there are three, all of them under `core`:

      * `{reactants, arrow, products}` + either `condition` or the
        `condition_over` / `condition_under` pair — 5 lessons, on a `rule`
        block (b7-01, b8-01, b8-03, c6-03, c6-04);
      * `{left, right}` — 1, nested two deep inside `control-tubes.summary`
        (c5-03, the rusting equation);
      * a bare STRING, `"starch → glucose"` — 3, one per enzyme inside the
        `enzyme-run` bench (b3-06).

    So this walks rather than reaching, and raises on a fourth shape instead of
    skipping it: an equation a new lesson nests somewhere new should stop the
    export, not quietly fail to become a card.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "equation":
                yield path + "." + k, v
            else:
                yield from _equations(v, path + "." + str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _equations(v, "%s[%d]" % (path, i))


def _equation_parts(where, eq):
    """One authored equation, normalised to (left, arrow_word, right, conds).

    ⚠️ THE ARROW IS NEVER A CHARACTER — that is the standing ruling in b7-01,
    b8-01 and b8-03, whose comments say there is deliberately no field a U+2192
    could be typed into, because the shipped font subsets carry no glyph for it
    and Design draws the arrow as an SVG. `arrow` holds the WORD the drawn arrow
    means ("gives", "makes"), which is also the component's accessible name.

    b3-06 is the exception that proves it: its three equations ARE strings with
    a literal `→` in them, because they sit in an instrument's config rather
    than in the equation component. Split here, so the arrow character stops at
    the edge of the mirror and no card face ever carries one.
    """
    if isinstance(eq, str):
        if eq.count("→") != 1:
            raise SystemExit(
                "export_ks3_questions: %s is a string equation with %d arrow(s) "
                "— expected exactly one to split on: %r"
                % (where, eq.count("→"), eq))
        left, right = (p.strip() for p in eq.split("→"))
        return left, None, right, {}

    if not isinstance(eq, dict):
        raise SystemExit("export_ks3_questions: %s is a %s, not an equation"
                         % (where, type(eq).__name__))

    if "reactants" in eq:
        left, arrow, right = eq["reactants"], eq.get("arrow"), eq["products"]
    elif "left" in eq:
        # c5-03's rusting equation. Drawn, never spoken: `control-tubes`
        # authors no arrow WORD, so this card has none and the surface has to
        # draw the arrow. Inventing "gives" here to fill the column would be
        # putting a word in the author's mouth on a science page.
        left, arrow, right = eq["left"], None, eq["right"]
    else:
        raise SystemExit(
            "export_ks3_questions: %s is an equation shape this exporter does "
            "not know: keys %s. Teach `_equation_parts` about it rather than "
            "letting it fall out of the deck silently."
            % (where, sorted(eq)))

    conds = {k: eq[k] for k in ("condition", "condition_over", "condition_under")
             if eq.get(k)}
    for k in eq:
        if k not in ("reactants", "arrow", "products", "left", "right",
                     "condition", "condition_over", "condition_under"):
            raise SystemExit(
                "export_ks3_questions: %s has an unexported equation field %r"
                % (where, k))
    return left, arrow, right, conds


def card_rows():
    """The flashcard deck, one lesson at a time.

    ── The front wording, because it is read by children ─────────────────

    A definition's front is `Define: <term>`, and the term ships EXACTLY as it
    was authored.

    Design's sample deck writes `Define diffusion.` — the term as the object of
    a sentence. That works for Design's six sample cards and breaks on the real
    corpus in two ways. 212 of the 573 terms are authored with a capital first
    letter, and it is a per-unit house style rather than a property of the word:
    the whole of B2, C2, C3, C6, C7, C8 and C9 capitalise, and the whole of B1,
    B3, B4, B5 and B11 do not. Design's frame would print `Define Skeleton.`
    next to `Define cell.` in one deck. And 143 of them are PHRASES, not nouns
    — `concentration difference`, `sacrificial protection` — which read as a
    sentence fragment when a verb is put in front of them.

    Down-casing the first letter to fix it was the obvious alternative and is
    rejected: `DNA` and `X-ray diffraction` are both real terms in this corpus,
    both would be damaged by the rule, and a heuristic that mangles two terms in
    573 is worse than a frame that needs no heuristic. This exporter normalises
    NOTHING; the authored bytes are the shipped bytes, as everywhere else here.

    The colon does that work. It makes the term a LABEL rather than a
    grammatical object, so an authored capital is not an error and a phrase is
    not a fragment — which is exactly how the term already appears in the
    lesson's own vocabulary list. There is no full stop, because a label is not
    a sentence.

    An equation's front is `Complete the word equation: <left-hand side>`, and
    its back is the right-hand side. The alternative was Design's own framing,
    `Write the word equation for <X>`, and there is no honest `<X>` in the data:
    the lesson title fits two of the seven, prints `Write the word equation for
    Acid + metal.` on a third, and on c5-03 would say `for oxidation` over an
    equation that is specifically RUSTING — a science-accuracy error, which is
    the one thing this is not allowed to invent. Giving the left-hand side asks
    for the products, which is what all seven lessons actually teach, and it
    composes no words at all.

    ── `note` ───────────────────────────────────────────────────────────

    502 of the 573 entries carry a `note` (421 non-empty, median 64 characters).
    It is extra teaching detail, and it is NOT part of the definition: `Lower it
    slowly, at an angle.` is a method warning; `The seven are movement,
    respiration, …` is a list the definition deliberately does not give.

    It is neither dropped nor glued onto the back. It ships in its own column,
    `back_note`, for one reason: the back of this card is the ANSWER to
    `Define: X`, and a student self-marks by comparing what they said to what is
    there. Append three more sentences and they cannot tell which part they were
    supposed to produce, so a card they knew reads as a card they half-knew. In
    its own column the surface can reveal it under the definition as an aside,
    and can do that later without a re-export.

    ⚑ For whoever builds that surface: four of the 421 notes lean on the lesson
    page around them — `Sam's method`, `the dials on the bench` — and will read
    as a dangling reference on a card. Small, and worth a pass before they are
    shown.
    """
    titles = unit_titles()
    rows = []
    for unit_code, mod in lesson_modules():
        lesson = mod.LESSON
        slug = lesson.get("slug")
        if not slug:
            raise SystemExit(
                "export_ks3_questions: %s has no slug" % mod.__name__)
        if unit_code not in titles:
            raise SystemExit(
                "export_ks3_questions: unit %s is not in ks3_data.structure — "
                "there is no topic to put on its cards" % unit_code)
        topic = titles[unit_code]
        seen = set()
        pos = 0

        def add(kind, anchor, front, back, back_note=None, eq=None):
            nonlocal pos
            key = (kind, anchor)
            if key in seen:
                raise SystemExit(
                    "export_ks3_questions: %s has two %s cards anchored on %r "
                    "— the id would collide and one would overwrite the other"
                    % (slug, kind, anchor))
            seen.add(key)
            eq = eq or {}
            rows.append(dict(
                id="%s#%s#%s" % (slug, "def" if kind == "definition" else "eq",
                                 anchor),
                unit_code=unit_code,
                lesson_slug=slug,
                kind=kind,
                card_position=pos,
                # ⚠️ THE UNIT'S TITLE, not the lesson's, and VERBATIM.
                #
                # Design shows a topic on both faces of every card, and her
                # sample values — GAS EXCHANGE, PRESSURE, CHEMICAL REACTIONS,
                # PARTICLE MODEL — are KS3 UNIT titles, uppercased. That is the
                # only real grouping the data has: a deck spans every lesson a
                # class has covered, so the label's job is to say which unit a
                # card came from. The lesson title would be near-redundant with
                # the front (`DIFFUSION` over `Define: diffusion`).
                #
                # Stored in the case `ks3_data/structure.py` writes it.
                # Uppercasing is presentation and is reversible; doing it here
                # is not, and the day a unit title carries `pH` or `DNA` the
                # mirror would be the thing that broke it.
                topic=topic,
                front=_no_markup("%s front" % slug, front),
                back=_no_markup("%s back" % slug, back),
                back_note=(None if not back_note
                           else _no_markup("%s note" % slug, back_note)),
                equation_left=eq.get("left"),
                equation_arrow=eq.get("arrow"),
                equation_right=eq.get("right"),
                equation_condition=eq.get("condition"),
                equation_condition_over=eq.get("condition_over"),
                equation_condition_under=eq.get("condition_under"),
            ))
            pos += 1

        for entry in lesson.get("vocabulary") or []:
            term = (entry.get("term") or "").strip()
            definition = (entry.get("definition") or "").strip()
            if not term or not definition:
                raise SystemExit(
                    "export_ks3_questions: %s has a vocabulary entry with no "
                    "term or no definition: %r" % (slug, entry))
            add("definition", _anchor(term),
                "Define: " + term, definition,
                back_note=(entry.get("note") or "").strip() or None)

        for where, eq in _equations(lesson, slug):
            left, arrow, right, conds = _equation_parts(where, eq)
            for part in (left, right, arrow) + tuple(conds.values()):
                if part is not None:
                    _no_markup("%s equation" % slug, part)
                if part is not None and "→" in part:
                    raise SystemExit(
                        "export_ks3_questions: %s carries a typed arrow — the "
                        "parts are stored, never the glyph: %r" % (where, part))
            add("equation", _anchor(left),
                "Complete the word equation: " + left, right,
                eq=dict(left=left, arrow=arrow, right=right, **conds))

    return rows


# ── emitting ─────────────────────────────────────────────────────────────

def upsert_statements(table, columns, rows, conflict_key):
    """Idempotent multi-row upserts, chunked."""
    out = []
    for start in range(0, len(rows), ROWS_PER_STATEMENT):
        chunk = rows[start:start + ROWS_PER_STATEMENT]
        values = []
        for r in chunk:
            cells = []
            for col in columns:
                v = r[col]
                if isinstance(v, (list, dict)):
                    cells.append(sql_json(v))
                elif isinstance(v, int) and not isinstance(v, bool):
                    cells.append(str(v))
                else:
                    cells.append(sql_str(v))
            values.append("(" + ", ".join(cells) + ")")
        updates = ", ".join(
            "%s = excluded.%s" % (c, c) for c in columns if c != conflict_key)
        out.append(
            "insert into public.%s (%s) values\n%s\non conflict (%s) do update "
            "set %s, updated_at = now();"
            % (table, ", ".join(columns), ",\n".join(values), conflict_key,
               updates))
    return out


BANK_COLUMNS = ["id", "unit_code", "lesson_slug", "band", "bank_position",
                "text", "figure", "options"]
LADDER_COLUMNS = ["question_ref", "unit_code", "lesson_slug", "rung", "text",
                  "answer_letter", "options"]
CARD_COLUMNS = ["id", "unit_code", "lesson_slug", "kind", "card_position",
                "topic", "front", "back", "back_note", "equation_left",
                "equation_arrow", "equation_right", "equation_condition",
                "equation_condition_over", "equation_condition_under"]


# ── ⊕ MRB-338, 9 Sep 2026 — THE LOAD PATH THIS EXPORTER DID NOT HAVE ────
#
# KS4's exporter has had `--load {test,prod}` since MRB-332; this one emitted
# SQL and stopped, because `ks3_pools_ingest(pool, payload)` was meant to be
# the fast path. On night 1 of MRB-338 that path turned out to be unusable
# unattended, and the reason is worth keeping rather than rediscovering:
#
#   ⚠️ `ks3_pools_ingest` guards on
#      `auth.jwt() ->> 'email' = 'midebolabadmus@gmail.com'`.
#      That is deliberate — its own comment says it exists so a pool refresh
#      needs no service-role key on the machine doing the export, and an
#      ordinary student holding a valid JWT must not be able to rewrite the
#      bank. But a SERVICE-ROLE key carries no `email` claim at all, so an
#      unattended run is refused: HTTP 400, P0001,
#      "ks3_pools_ingest: not permitted". Verified with an empty payload, so
#      nothing could have been written either way.
#
#   The generated SQL is the documented alternative, and at 5.2 MB across 24
#   statements it cannot go through an MCP round trip either.
#
# So this mirrors KS4's loader exactly — same three guards, same header, same
# chunking — and leaves `ks3_pools_ingest` in place for Mide, who is the
# operator it was written for.


def _jwt_ref(token):
    """The Supabase project ref a JWT was issued for, or None.

    Decodes the payload only. It does NOT verify the signature and must never
    be used to decide whether a token is authentic — that is the server's job,
    and here the token is our own. What it answers is the one question a
    signature cannot: WHICH PROJECT this key opens.

    ⚠️ This matters more here than it looks. On 9 Sep 2026 TEST and PRODUCTION
    both held exactly 5,142 KS3 rows and 3,417 KS4 rows, so no count, and no
    glance at a table, could have told the two apart. The ref claim could.

    Returns None rather than raising on anything unreadable, so the caller
    reports "the project could not be established" and refuses, instead of a
    traceback three frames from a production write.
    """
    import base64
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        claims = json.loads(base64.urlsafe_b64decode(payload).decode("utf-8"))
    except Exception:
        return None
    ref = claims.get("ref")
    return ref if isinstance(ref, str) and ref else None


def load_rows(project, pools, bank, ladder, cards):
    """Upsert the named pools into TEST or PRODUCTION over PostgREST.

    Guarded the three independent ways `export_ks4_questions.py --load` is,
    because they fail for different reasons and one guard is one thing to get
    wrong:

      1. THE VALUE IS TYPED IN FULL. The raw argv must carry the exact token
         `prod`; no abbreviation, no default, no environment variable.
      2. THE KEY COMES FROM ~/.mrbadmus/prod.env AND NOWHERE ELSE — not this
         repo, not the backend .env, not the environment. It is never printed:
         not in a success line, not in an error, not in a traceback.
      3. THE TARGET IS PROVED FROM THE KEY, NOT STATED BESIDE IT. A URL in a
         file is somebody's note about where a key belongs; the key's own
         `ref` claim is what the credential actually opens. ~/.mrbadmus/prod.env
         carries the key alone and no URL, so on the prod path this is not a
         convenience — it is the only thing that knows where the load is going,
         and the URL is DERIVED from it.

    ⚠️ BANK ONLY BY DEFAULT. MRB-338 changed the bank and nothing else, and a
    load that quietly rewrote `ks3_ladder_questions` and `ks3_cards` as well
    would be touching two pools nobody had reviewed that night — with the
    ladder mirror in particular being what the class page's practice round
    serves. `--pools` must name them explicitly.
    """
    # Imported here rather than at module scope, matching `verify()` below:
    # every other entry point in this file runs without touching the network.
    import ssl
    import urllib.error
    import urllib.request

    if project == "prod":
        if "prod" not in sys.argv:
            print("\n     ⛔ --load prod: the literal token `prod` is not in "
                  "the command line.\n        Production is never reached by "
                  "an abbreviation. Refusing.")
            return 3
        env = os.path.expanduser("~/.mrbadmus/prod.env")
        expect_ref = "urklkrwevjtlfbwnipjn"
        label = "PRODUCTION"
    else:
        env = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
        expect_ref = "qeppkiswvclkkwbxmlok"
        label = "TEST"

    conf = {}
    try:
        with open(env, encoding="utf-8") as fh:
            for line in fh:
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    conf[k.strip()] = v.strip()
    except OSError as exc:
        if project == "prod":
            print("\n     ⛔ --load prod: %s is not readable (%s)." % (env, exc))
            print("        This is the ONLY place the production service key "
                  "is read from, on purpose.")
            print("        Exit 4 — apply build/ks3-questions/*.sql by hand "
                  "instead, or call")
            print("        ks3_pools_ingest signed in as the content owner. Do "
                  "not put a production key anywhere in this repo.\n")
            return 4
        print("\n     ⛔ --load cannot read %s (%s)" % (env, exc))
        return 3

    url = conf.get("SUPABASE_URL", "")
    key = conf.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not key:
        print("\n     ⛔ --load %s: %s sets no SUPABASE_SERVICE_ROLE_KEY."
              % (project, env))
        return 3

    key_ref = _jwt_ref(key)
    if key_ref is None:
        print("\n     ⛔ --load %s: the SUPABASE_SERVICE_ROLE_KEY in %s is not "
              "a readable JWT,\n        so the project it belongs to cannot be "
              "established. Refusing." % (project, env))
        return 3
    if key_ref != expect_ref:
        print("\n     ⛔ --load %s: that key belongs to project %r, not the %s "
              "project %r.\n        Refusing — this is exactly the mix-up the "
              "guard exists for." % (project, key_ref, label, expect_ref))
        return 3
    if url and expect_ref not in url:
        print("\n     ⛔ --load %s: %s sets a SUPABASE_URL that does not match "
              "its own key.\n        Key says %r; URL says %s. Refusing."
              % (project, env, key_ref, url))
        return 3
    url = url or ("https://%s.supabase.co" % key_ref)

    TABLES = [("bank", "ks3_assignment_bank", BANK_COLUMNS, bank)]
    if "ladder" in pools:
        TABLES.append(("ladder", "ks3_ladder_questions", LADDER_COLUMNS, ladder))
    if "cards" in pools:
        TABLES.append(("cards", "ks3_cards", CARD_COLUMNS, cards))

    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    BATCH = 250
    print("\n     target project proved from the key's own ref claim: %s (%s)"
          % (key_ref, label))
    for name, table, columns, rows in TABLES:
        endpoint = url.rstrip("/") + "/rest/v1/" + table
        sent = 0
        print("     loading %d %s row(s) into %s…" % (len(rows), name, label))
        for i in range(0, len(rows), BATCH):
            chunk = [{c: r[c] for c in columns} for r in rows[i:i + BATCH]]
            rq = urllib.request.Request(
                endpoint, data=json.dumps(chunk, ensure_ascii=False).encode("utf-8"),
                method="POST")
            rq.add_header("apikey", key)
            rq.add_header("Authorization", "Bearer " + key)
            rq.add_header("Content-Type", "application/json")
            # merge-duplicates makes this the same upsert the SQL files are.
            rq.add_header("Prefer", "resolution=merge-duplicates,return=minimal")
            try:
                with urllib.request.urlopen(rq, context=ctx, timeout=120) as r:
                    r.read()
            except urllib.error.HTTPError as e:
                print("\n     ⛔ --load failed on %s rows %d-%d: HTTP %s\n        %s"
                      % (name, i, i + len(chunk) - 1, e.code,
                         e.read().decode("utf-8", "replace")[:400]))
                return 1
            sent += len(chunk)
            print("        %d / %d" % (sent, len(rows)))
        print("     ✅ %d %s row(s) upserted into %s." % (sent, name, label))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true",
                    help="print the statements instead of writing files")
    ap.add_argument("--check", action="store_true",
                    help="validate and count; write nothing")
    ap.add_argument("--json", action="store_true",
                    help="write bank.json / ladder.json / cards.json for ks3_pools_ingest")
    ap.add_argument("--verify", action="store_true",
                    help="compare the live tables against Python, row for row")
    # ⊕ MRB-335. The project used to be a hardcoded production URL, which made
    # `--verify` unusable for a TEST rehearsal — the one thing you want to do
    # BEFORE loading production. Default unchanged, so every existing caller
    # and the gate registry keep pointing where they did.
    ap.add_argument("--project", choices=("prod", "test"), default="prod",
                    help="which Supabase project --verify reads (default prod)")
    # ⊕ MRB-338. See load_rows() for why the ingest RPC could not be used
    # unattended, and for the three guards on the prod path.
    ap.add_argument("--load", choices=("test", "prod"), default=None,
                    help="apply the rows straight to the database over "
                         "PostgREST (bank only unless --pools says otherwise)")
    ap.add_argument("--pools", default="bank",
                    help="comma-separated pools to --load: bank,ladder,cards "
                         "(default bank — MRB-338 changed the bank alone)")
    args = ap.parse_args()

    bank = bank_rows()
    ladder = ladder_rows()
    cards = card_rows()

    # ⚠️ THE LESSON SLUG MUST BE GLOBALLY UNIQUE, and this is where that is
    # enforced rather than hoped for.
    #
    # Python keys the bank by (unit_code, lesson_slug). The producer in the Node
    # backend cannot: it reads `ks3_assignment_bank` filtered by `lesson_slug`
    # alone, because the scheme of work stores a subtopic SLUG and no unit code.
    # The two agree only while no slug appears in two units. If one ever does,
    # the producer silently merges both lessons' questions into one pool and
    # composes an assignment Python would never compose — and nothing about the
    # page would look wrong.
    #
    # It is true today across all 77 lessons. It is not guaranteed by anything
    # else, so it is asserted here, on the way out, where a new unit will trip
    # it the first time it is exported.
    #
    # ⊕ WIDENED to the cards, which are read the same way — the deck is built
    # for the lessons a class has covered, and the scheme of work names them by
    # slug alone. The cards also reach 107 lessons where the bank reaches 77, so
    # this now sees 30 lessons it could not see before.
    by_slug = {}
    for r in bank + cards:
        by_slug.setdefault(r["lesson_slug"], set()).add(r["unit_code"])
    collisions = {s: sorted(u) for s, u in by_slug.items() if len(u) > 1}
    if collisions:
        raise SystemExit(
            "export_ks3_questions: lesson slug(s) used by more than one unit — "
            "%s. The backend's producer looks a lesson up by slug alone (the "
            "scheme of work has no unit code), so it would merge them. Rename "
            "one of them before exporting."
            % "; ".join("%r in %s" % (s, u) for s, u in sorted(collisions.items())))

    lessons_banked = len({(r["unit_code"], r["lesson_slug"]) for r in bank})
    lessons_laddered = len({r["lesson_slug"] for r in ladder})
    lessons_carded = len({r["lesson_slug"] for r in cards})
    by_kind = {k: sum(1 for r in cards if r["kind"] == k) for k in CARD_KINDS}

    print("\n📚  export_ks3_questions — the pools, out of Python\n")
    print("     bank    %4d question(s) across %d lesson(s)"
          % (len(bank), lessons_banked))
    print("     ladder  %4d question(s) across %d lesson(s)  (recall + apply "
          "only)" % (len(ladder), lessons_laddered))
    print("     cards   %4d card(s) across %d lesson(s)  (%s)"
          % (len(cards), lessons_carded,
             ", ".join("%d %s" % (by_kind[k], k) for k in CARD_KINDS)))

    # ⊕ MRB-335 — printed on EVERY run, not only on --verify, so the value in
    # a report and the value on the machine that made it are the same
    # sentence. `topped` is the count of lessons that have grown past the
    # original twelve; it is the one number that says whether a top-up landed.
    topped = len({(r["unit_code"], r["lesson_slug"]) for r in bank
                  if r["bank_position"] >= 12})
    print("\n     bank sha256  %s" % checksum(bank, BANK_COLUMNS))
    print("     %d of %d lesson(s) topped up beyond bank_position 11; auto "
          "composition still reads 0–11 only" % (topped, lessons_banked))

    if args.check:
        print("\n     --check: nothing written.\n")
        return

    if args.verify:
        sys.exit(verify(bank, ladder, cards, args.project))

    if args.json:
        os.makedirs(OUT_DIR, exist_ok=True)
        for name, rows in (("bank", bank), ("ladder", ladder),
                           ("cards", cards)):
            path = os.path.join(OUT_DIR, name + ".json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(rows, fh, ensure_ascii=False)
            print("     ✅ %-12s %8d bytes  → %s"
                  % (name + ".json", os.path.getsize(path), path))
        print("\n     Apply with ks3_pools_ingest(pool, payload). See the "
              "migration for the guard.\n")
        return

    if args.load:
        pools = {p.strip() for p in args.pools.split(",") if p.strip()}
        unknown = pools - {"bank", "ladder", "cards"}
        if unknown:
            raise SystemExit("export_ks3_questions: unknown pool(s) %s"
                             % ", ".join(sorted(unknown)))
        if "bank" not in pools:
            raise SystemExit("export_ks3_questions: --pools must include bank")
        sys.exit(load_rows(args.load, pools, bank, ladder, cards))

    stmts = (upsert_statements("ks3_assignment_bank", BANK_COLUMNS, bank, "id")
             + upsert_statements("ks3_ladder_questions", LADDER_COLUMNS,
                                 ladder, "question_ref")
             + upsert_statements("ks3_cards", CARD_COLUMNS, cards, "id"))

    if args.stdout:
        for s in stmts:
            print(s)
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    for old in os.listdir(OUT_DIR):
        if old.endswith(".sql"):
            os.remove(os.path.join(OUT_DIR, old))
    for i, s in enumerate(stmts):
        path = os.path.join(OUT_DIR, "%02d.sql" % i)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(s + "\n")
    print("\n     ✅ %d statement(s) → %s/" % (len(stmts), OUT_DIR))
    print("\n     These are upserts. Applying them twice is applying them "
          "once.\n")


# ── the gate ─────────────────────────────────────────────────────────────

# ⊕ MRB-335. Both projects, named rather than typed at the one call site, so
# `--project test` is a rehearsal and `--project prod` is the gate. The anon
# key for whichever is chosen is still resolved out of shared/config.js by
# matching the key's own `ref` claim — see below.
PROJECTS = {
    "prod": "https://urklkrwevjtlfbwnipjn.supabase.co",
    "test": "https://qeppkiswvclkkwbxmlok.supabase.co",
}


def verify(bank, ladder, cards, project="prod"):
    """Does the database still match Python, row for row?

    The tables are a mirror. A mirror nobody checks is just a second copy, and
    the failure it hides is the quiet one: a question edited in Python, the
    export not re-run, and every class served the old wording for a term while
    the repo says otherwise.

    Reads over PostgREST with a real session rather than a service key, because
    the pools are readable by any signed-in user and this only needs to READ.
    SKIPS LOUDLY when there are no credentials — a gate that passes because it
    could not run is worse than no gate.
    """
    import ssl
    import urllib.error
    import urllib.request

    pw = os.environ.get("MRB_TEST_STUDENT_PASSWORD")
    if not pw:
        print("\n     ⏭️  --verify SKIPPED (%s): MRB_TEST_STUDENT_PASSWORD is"
              " not set," % project)
        print("        so the live tables cannot be read. This is the only check")
        print("        that the database still matches these files.\n")
        # ⊕ MRB-282. This used to `return 0`, three lines under a docstring
        # that says "a gate that passes because it could not run is worse than
        # no gate". Exit 3 — distinct from 1, which means measured drift — so
        # that a caller can tell "the mirror agrees" from "nobody looked".
        # gate_registry marks this gate `needs_env`, so the pre-push guard
        # reports the missing password as a SKIP by name and never sees a 3.
        return 3

    url = PROJECTS[project]

    # ⊕ 1 Sep 2026 (MRB-306 WS-0). The key used to be scraped out of
    # leaderboard.html. MRB-290 made that page GENERATED and derive-everything,
    # and its inline anon key left with the hand-written original — so this
    # gate would have died on `.group(0)` of None the moment somebody set
    # MRB_TEST_STUDENT_PASSWORD, i.e. exactly when it was finally asked to run.
    # It never surfaced because the skip above returns first without the env
    # var. shared/config.js carries BOTH projects, so take the key whose own
    # `ref` claim matches the project this verify is pointed at.
    import base64
    import re
    ref = url.split("//", 1)[1].split(".", 1)[0]
    src = open(os.path.join(REPO, "shared", "config.js"), encoding="utf-8").read()
    key = None
    for tok in re.findall(
            r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
            src):
        payload = tok.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        if ('"ref":"%s"' % ref) in base64.urlsafe_b64decode(payload).decode():
            key = tok
            break
    if key is None:
        raise SystemExit(
            "export_ks3_questions --verify: shared/config.js carries no anon "
            "key for project %r." % ref)
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

    def api(path, headers, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            url + path, data=data, method=("POST" if data else "GET"),
            headers=dict({"Content-Type": "application/json"}, **headers))
        with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
            return json.loads(r.read().decode())

    # ⊕ MRB-335 — the account is overridable. On TEST the production owner's
    # address may not exist, and a rehearsal that cannot sign in is a
    # rehearsal that proves nothing.
    email = os.environ.get("MRB_VERIFY_EMAIL", "midebolabadmus@gmail.com")
    tok = api("/auth/v1/token?grant_type=password", {"apikey": key},
              {"email": email, "password": pw})
    del pw
    auth = {"apikey": key, "Authorization": "Bearer " + tok["access_token"]}

    def fetch(table, cols):
        out, step = [], 1000
        while True:
            page = api("/rest/v1/%s?select=%s&order=%s&limit=%d&offset=%d"
                       % (table, cols, cols.split(",")[0], step, len(out)), auth)
            out.extend(page)
            if len(page) < step:
                return out

    problems = []

    def compare(name, want, got, keyfield, fields):
        w = {r[keyfield]: r for r in want}
        g = {r[keyfield]: r for r in got}
        missing = sorted(set(w) - set(g))
        extra = sorted(set(g) - set(w))
        if missing:
            problems.append("%s: %d row(s) in Python and NOT in the database — "
                            "the export has not been applied: %s"
                            % (name, len(missing), ", ".join(missing[:5])))
        if extra:
            problems.append("%s: %d row(s) in the database that Python does not "
                            "have — a retired question is still being served: %s"
                            % (name, len(extra), ", ".join(extra[:5])))
        differing = []
        for k in sorted(set(w) & set(g)):
            for f in fields:
                a, b_ = w[k][f], g[k][f]
                if f == "options":
                    a = json.dumps(a, sort_keys=True, ensure_ascii=False)
                    b_ = json.dumps(b_, sort_keys=True, ensure_ascii=False)
                if a != b_:
                    differing.append("%s.%s" % (k, f))
                    break
        if differing:
            problems.append("%s: %d row(s) differ between Python and the "
                            "database: %s" % (name, len(differing),
                                              ", ".join(differing[:5])))
        print("     %s %-8s %4d in Python, %4d live, %d missing, %d extra, %d differing"
              % ("❌" if (missing or extra or differing) else "✅", name,
                 len(w), len(g), len(missing), len(extra), len(differing)))

    print("\n     comparing %s against Python\n" % url)
    live_bank = fetch("ks3_assignment_bank",
                      "id,unit_code,lesson_slug,band,bank_position,text,figure,options")
    compare("bank",
            bank,
            live_bank,
            "id",
            ["unit_code", "lesson_slug", "band", "bank_position", "text",
             "figure", "options"])

    # ⚠️ Printed whether or not the comparison passed. A checksum is most
    # useful on the run that FAILS — it is what tells you, next time, whether
    # you are looking at the same wrong database or a different one. And if
    # these two ever disagree with the row-by-row verdict above, one of the
    # two is not reading what it claims to; say so rather than pick a winner.
    py_sum = checksum(bank, BANK_COLUMNS)
    db_sum = checksum(live_bank, BANK_COLUMNS)
    print("        bank python   sha256 %s" % py_sum)
    print("        bank database sha256 %s   %s"
          % (db_sum, "✅ equal" if py_sum == db_sum else "❌ DIFFERENT"))
    bank_clean = not problems
    if (py_sum == db_sum) != bank_clean:
        problems.append(
            "the bank's row-by-row comparison and its checksum DISAGREE. One "
            "of them is not reading what it says it is — do not trust either "
            "until that is explained.")
    compare("ladder",
            ladder,
            fetch("ks3_ladder_questions",
                  "question_ref,unit_code,lesson_slug,rung,text,answer_letter,options"),
            "question_ref",
            ["unit_code", "lesson_slug", "rung", "text", "answer_letter",
             "options"])
    compare("cards",
            cards,
            fetch("ks3_cards", ",".join(CARD_COLUMNS)),
            "id",
            [c for c in CARD_COLUMNS if c != "id"])

    print()
    if problems:
        for p in problems:
            print("        · " + p)
        print("\n     Re-run:  python3 export_ks3_questions.py --json  and apply "
              "it.\n")
        return 1
    print("     ✅ the database is exactly what these files say it is.\n")
    return 0


if __name__ == "__main__":
    main()
