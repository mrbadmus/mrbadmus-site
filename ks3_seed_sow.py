"""ks3_seed_sow.py — generate the KS3 scheme-of-work seed SQL.

Run it:

    python3 ks3_seed_sow.py

Writes two files, both generated, neither hand-edited:

    supabase/seeds/20260726181000_ks3_default_sequence.sql
        → public.scheme_of_work_entries — the GLOBAL table. One row per lesson
          slot in the platform's published default sequence (architecture.md
          §7, ruled 2026-07-26). exam_board / tier / pathway all NULL.

    supabase/seeds/20260726182000_ks3_school_schemes.sql
        → public.scheme_of_work_overrides — the PER-SCHOOL table. One block per
          school in ``ks3_data/school_schemes.py``. These are seed data and
          reference evidence, never the default.

**Why generate rather than write.** These two files and ``ks3_data/`` describe
the same curriculum, so hand-writing them guarantees they drift — and a drifted
scheme-of-work row is a school pointing at a lesson that does not exist, which
fails silently. Generating both from the Python data makes drift structurally
impossible: there is one source, and the SQL is a projection of it.

**Row rule.** One row per lesson SLOT declared in ``ks3_data/structure.py``,
including referenced slots (§4.6). A referenced slot generates no page — the
owning unit renders it — but a teacher *does* teach that slot in that week, and
a scheme of work describes teaching, not pages. Those rows carry the
cross-reference in ``notes`` so nobody reads them as a duplicate.

Within one ``(year_group, subject)`` block, rows are ordered by unit order then
lesson order, and ``academic_week`` runs 1..n. That is a teaching *order*, not a
calendar: week 1 is the first lesson of that subject in that year, whenever the
school actually starts it.

**Half terms, and the one behavioural change they brought (MRB-176 ruling 2).**
Default-sequence rows now also carry ``half_term`` (1–6), derived by
``ks3_data/half_terms.py``. The change worth stating is not the extra column,
it is that **the DEFAULT block's unit order — and therefore its
``academic_week`` numbering — now follows ``half_terms.INTRA_YEAR_UNIT_ORDER``
rather than raw ``structure.py`` declaration order.** In practice that moves one
thing: Year 8 physics teaches P5 Pressure before P1 Energy, because Year 8
biology meets breathing in half term 1 and breathing requires pressure. Half
term and academic week have to agree about teaching order or the row contradicts
itself, so they are numbered from the same list.

**School-scheme rows are untouched by all of that.** They carry no
``half_term``, and their ``academic_week`` still comes from declaration order.
``build_rows`` takes an explicit ``with_half_terms`` flag rather than inferring
it, because a school's sequence puts different units in different years and the
default's half-term map simply does not describe it. The generated
``20260726182000_ks3_school_schemes.sql`` is byte-identical to what it was
before half terms existed.

**The 39-week ceiling.** ``academic_week`` carries
``CHECK (academic_week BETWEEN 1 AND 39)``. Every block is asserted against it
here, for the default and for every school scheme, so a curriculum that will not
fit an academic year is caught in Python rather than by a constraint violation
halfway through a seed.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ks3_data import half_terms, structure
from ks3_data.default_sequence import DEFAULT_SEQUENCE_V1
from ks3_data.school_schemes import SCHOOL_SCHEMES, effective_sequence

SEED_DIR = os.path.join("supabase", "seeds")

DEFAULT_SEED = "20260726181000_ks3_default_sequence.sql"
SCHOOLS_SEED = "20260726182000_ks3_school_schemes.sql"

# The hard ceiling from the table definition, restated here so the assertion
# reads as the rule rather than as a magic number.
MAX_ACADEMIC_WEEK = 39

YEARS = (7, 8, 9)


def q(s):
    """A SQL string literal, or NULL. Single quotes doubled, per the standard."""
    if s is None:
        return "null"
    return "'%s'" % str(s).replace("'", "''")


def subject_id_sql(discipline):
    """subject_id by NAME, never a hardcoded uuid.

    uuids differ between the test project and production, so a seed carrying
    one is a seed that works in exactly one place. Looking the row up by its
    natural key makes the file portable, and makes a missing subject row fail
    loudly on the NOT NULL rather than silently on the wrong id.
    """
    return ("(select id from public.subjects where name = %s)"
            % q(structure.DISCIPLINE_TITLES[discipline]))


def school_id_sql(slug):
    """school_id by slug — same reasoning as subject_id_sql."""
    return "(select id from public.schools where slug = %s)" % q(slug)


# ── the rows ─────────────────────────────────────────────────────────────

def unit_order(sequence, with_half_terms):
    """The order units are laid out in, as a flat list of unit codes.

    Two orders, and which one applies is a caller's decision rather than
    something guessed from the shape of `sequence`:

    * **Declaration order** (`with_half_terms=False`) — `structure.py`'s own
      order, filtered to the units this sequence places. §7's tables are
      written in teaching order, so declaration order IS a teaching order, and
      it is the only one available for a school whose year map we did not
      derive anything from.
    * **`half_terms.INTRA_YEAR_UNIT_ORDER`** (`with_half_terms=True`) — the
      same order with the ruled prerequisite deviations applied. Rows numbered
      any other way would disagree with the half term stamped on them.
    """
    if not with_half_terms:
        return [u[0] for u in structure.UNITS if sequence.get(u[0]) is not None]

    # INTRA_YEAR_UNIT_ORDER is derived from the published default and describes
    # only the published default. Applying it to a school's sequence would put
    # units in years that school does not teach them in — silently, because
    # both are just dicts of unit code → year. Refuse loudly instead.
    if dict(sequence) != dict(DEFAULT_SEQUENCE_V1):
        differ = sorted(c for c in set(sequence) | set(DEFAULT_SEQUENCE_V1)
                        if sequence.get(c) != DEFAULT_SEQUENCE_V1.get(c))
        raise ValueError(
            "ks3_seed_sow: with_half_terms=True is only meaningful for the "
            "published default sequence, and this sequence diverges from it on "
            "%d unit(s): %s. Half terms are derived from the default's own "
            "intra-year order (ks3_data/half_terms.py); a school that teaches "
            "different units in different years needs its own derivation, not "
            "this one." % (len(differ), ", ".join(differ)))

    out = []
    for key in sorted(half_terms.INTRA_YEAR_UNIT_ORDER):
        out.extend(half_terms.INTRA_YEAR_UNIT_ORDER[key])
    return out


def build_rows(sequence, unit_notes=None, with_half_terms=False):
    """Lesson slots laid out as scheme-of-work rows for one sequence.

    `sequence` is unit code → year. `unit_notes` is an optional unit code →
    note, used for school schemes so a school's own commentary rides on that
    school's rows and nowhere else.

    `with_half_terms` says whether these rows carry a half term — see
    `unit_order` for why it is a parameter and not something inferred. It is
    True for exactly one caller: the platform default.

    Returns {(year_group, discipline): [row, ...]}, each row a dict ready to
    render, with academic_week already assigned 1..n in teaching order.
    """
    idx = structure.unit_index()
    unit_notes = unit_notes or {}
    blocks = {}

    # Iterating a unit list rather than the sequence dict keeps this
    # deterministic — dict order would make the output depend on how the map
    # was written.
    for code in unit_order(sequence, with_half_terms):
        year = sequence[code]
        title = idx[code]["title"]
        disc = idx[code]["discipline"]
        rows = blocks.setdefault((year, disc), [])
        for n, slot in enumerate(idx[code]["lesson_slots"]):
            notes = []
            owner = slot.get("owned_by")
            if owner:
                # §4.6 single source: the slot is taught here, but the lesson
                # belongs to another discipline's unit and is written there.
                notes.append(
                    "Cross-reference (architecture.md §4.6): this lesson is "
                    "owned by %s %s (%s) and is taught from there. Listed here "
                    "because %s teaches the slot, not because the content is "
                    "duplicated."
                    % (owner, idx[owner]["title"],
                       structure.DISCIPLINE_TITLES[idx[owner]["discipline"]],
                       title))
            # A school note is about the UNIT, not the lesson, so it rides on
            # the unit's first row only. Repeating it on all eight lessons of
            # P1 would make it read as a property of each lesson, which it is
            # not, and would put a school's commentary in eight places to
            # correct instead of one.
            if n == 0 and code in unit_notes:
                notes.append(unit_notes[code])
            row = {
                "year_group": year,
                "discipline": disc,
                "unit_code": code,
                "topic": title,
                "subtopic": slot["slug"],
                "notes": " · ".join(notes) if notes else None,
            }
            if with_half_terms:
                # By (unit, slug), never by slug alone: `energy-in-food` is
                # declared in two units — B3's §4.6 reference slot and P2's own
                # lesson — and they are taught two years apart.
                row["half_term"] = half_terms.half_term_of(slot["slug"], code)
            rows.append(row)

    for rows in blocks.values():
        for i, row in enumerate(rows, start=1):
            row["academic_week"] = i

    return blocks


def check_ceiling(blocks, label):
    """Every (year, subject) block must fit an academic year. §8.7 / table CHECK.

    Raises rather than truncating. A block over 39 is a real finding about the
    curriculum — either the year is overloaded or the sequence is wrong — and
    papering over it would hide that behind a constraint violation at apply
    time, in a different repo, on somebody else's afternoon.
    """
    busts = [(k, len(v)) for k, v in sorted(blocks.items()) if len(v) > MAX_ACADEMIC_WEEK]
    if busts:
        raise ValueError(
            "%s: %d (year, subject) block(s) exceed the %d-week ceiling on "
            "academic_week — %s. This is a curriculum problem, not a generator "
            "problem: the sequence does not fit an academic year." % (
                label, len(busts), MAX_ACADEMIC_WEEK,
                "; ".join("Y%d %s = %d lessons"
                          % (y, structure.DISCIPLINE_TITLES[d], n)
                          for (y, d), n in busts)))


# ── rendering ────────────────────────────────────────────────────────────

def header(path, what, tables, extra=""):
    return """-- ═══════════════════════════════════════════════════════════════════════
-- %(what)s
--
-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.
--    Regenerate with:  python3 ks3_seed_sow.py
--    Source of truth:  ks3_data/structure.py, ks3_data/default_sequence.py,
--                      ks3_data/school_schemes.py
--    Written to:       %(path)s
--    Target table:     %(tables)s
--
-- Hand-editing this file makes it disagree with ks3_data/, and a scheme row
-- that disagrees with the lesson registry is a school pointing at a lesson
-- that does not exist. Change the Python, re-run the generator.
--
-- Requires migrations 20260726120000_ks3_scheme_of_work_entries.sql and
-- 20260727081530_ks3_scheme_of_work_overrides.sql (architecture.md §8.7):
-- without them KS3 rows either cannot be inserted or can be duplicated.
--
-- Idempotent: every KS3 row in scope is deleted and rewritten, inside one
-- transaction. Re-running is safe and is the intended way to apply a change.
%(extra)s-- ═══════════════════════════════════════════════════════════════════════

""" % {"what": what, "path": path, "tables": tables, "extra": extra}


def block_comment(blocks):
    """The per-(year, subject) row counts, stated in the file itself."""
    lines = ["-- Row counts, generated:", "--"]
    for year in YEARS:
        parts = []
        for disc in structure.DISCIPLINES:
            rows = blocks.get((year, disc))
            if rows:
                parts.append("%s %d" % (structure.DISCIPLINE_TITLES[disc],
                                        len(rows)))
        if parts:
            lines.append("--   Y%d  %s" % (year, " · ".join(parts)))
    lines.append("--   %d rows total, max academic_week %d (ceiling %d)"
                 % (sum(len(v) for v in blocks.values()),
                    max((len(v) for v in blocks.values()), default=0),
                    MAX_ACADEMIC_WEEK))
    lines.append("--")
    return "\n".join(lines) + "\n"


def half_term_comment(blocks):
    """Lessons per half term, stated in the file rather than inferrable from it.

    The distribution is the whole point of the column, and it is the first
    thing anyone reviewing this seed wants to see. Reading it off 185 INSERT
    tuples is not review, it is arithmetic.
    """
    lines = ["-- Lessons per half term (HT1 … HT6), generated:", "--"]
    for year in YEARS:
        year_counts = [0] * 6
        for disc in structure.DISCIPLINES:
            rows = blocks.get((year, disc))
            if not rows:
                continue
            counts = [0] * 6
            for r in rows:
                counts[r["half_term"] - 1] += 1
            for i, n in enumerate(counts):
                year_counts[i] += n
            lines.append("--   Y%d %-10s %s   (%d)"
                         % (year, structure.DISCIPLINE_TITLES[disc],
                            " ".join("%2d" % n for n in counts), sum(counts)))
        if any(year_counts):
            lines.append("--   Y%d %-10s %s   (%d)"
                         % (year, "ALL",
                            " ".join("%2d" % n for n in year_counts),
                            sum(year_counts)))
    lines.append("--")
    lines.append("-- Every discipline appears in every half term of every year "
                 "— that is")
    lines.append("-- asserted in ks3_data/half_terms.py, not hoped for here.")
    lines.append("--")
    return "\n".join(lines) + "\n"


def render_default(blocks):
    out = [header(
        os.path.join(SEED_DIR, DEFAULT_SEED),
        "KS3 — MrBadmusAI default sequence v1, as scheme-of-work rows.",
        "public.scheme_of_work_entries (GLOBAL — no school_id)",
        extra="--\n"
              "-- This is the PLATFORM DEFAULT: what a school with nothing\n"
              "-- configured gets. It is derived from the statutory spine and the\n"
              "-- prerequisite graph, not from any school's timetable\n"
              "-- (architecture.md §7, ruled 2026-07-26). A school overrides it by\n"
              "-- writing scheme_of_work_overrides rows — see the companion seed.\n"
              "--\n"
              "-- KS3 has no exam board, no tier and no pathway: all three are NULL\n"
              "-- on every row here, which the §8.7 migration both permits and\n"
              "-- requires.\n"
              "--\n"
              "-- half_term (1-6) is where in the year the lesson falls. It is\n"
              "-- METADATA under §4.5 exactly as year_group is, derived by\n"
              "-- ks3_data/half_terms.py from this same default sequence, and it\n"
              "-- reaches no URL and no page byte. Requires migration\n"
              "-- 20260806230345_ks3_scheme_of_work_half_term.sql.\n"
              "--\n" + block_comment(blocks) + half_term_comment(blocks))]

    out.append("begin;\n")
    out.append("""
-- Preconditions. Failing here with a sentence beats failing later with a
-- NOT NULL violation on a subselect that quietly returned NULL.
do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS3 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;

-- Idempotency: this file owns every KS3 row in the global table.
delete from public.scheme_of_work_entries where key_stage = 'KS3';
""")

    for year in YEARS:
        for disc in structure.DISCIPLINES:
            rows = blocks.get((year, disc))
            if not rows:
                continue
            out.append(
                "\n-- ── Year %d · %s — %d lessons ─────────────────────────\n"
                % (year, structure.DISCIPLINE_TITLES[disc], len(rows)))
            out.append(
                "insert into public.scheme_of_work_entries\n"
                "  (key_stage, year_group, tier, pathway, subject_id, "
                "exam_board, academic_week, half_term, topic, subtopic, notes, "
                "active)\n"
                "values\n")
            vals = []
            unit = None
            for r in rows:
                if r["unit_code"] != unit:
                    unit = r["unit_code"]
                    vals.append("  -- %s %s" % (unit, r["topic"]))
                vals.append(
                    "  ('KS3', %d, null, null, %s, null, %d, %d, %s, %s, %s, "
                    "true)"
                    % (r["year_group"], subject_id_sql(disc),
                       r["academic_week"], r["half_term"], q(r["topic"]),
                       q(r["subtopic"]), q(r["notes"])))
            out.append(_join_values(vals) + ";\n")

    out.append("\ncommit;\n")
    return "".join(out)


def render_schools(all_blocks):
    total = sum(len(v) for b in all_blocks.values() for v in b.values())
    out = [header(
        os.path.join(SEED_DIR, SCHOOLS_SEED),
        "KS3 — real schools' configured sequences, as override rows.",
        "public.scheme_of_work_overrides (PER-SCHOOL — has school_id)",
        extra="--\n"
              "-- SEED DATA and reference evidence. **Never the default, never a\n"
              "-- template.** These rows describe what one named school teaches and\n"
              "-- when; the platform default lives in the companion seed against\n"
              "-- scheme_of_work_entries.\n"
              "--\n"
              "-- Each block below is one school laying its own order over the\n"
              "-- default — which is the whole of what architecture.md §4.5 asks a\n"
              "-- reorder to cost: rows in this table, and nothing else. No page\n"
              "-- path and no page byte depends on any of it.\n"
              "--\n"
              "-- %d school%s, %d rows.\n--\n"
              % (len(all_blocks), "" if len(all_blocks) == 1 else "s", total))]

    out.append("begin;\n")
    out.append("""
do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS3 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;
""")

    for slug, blocks in all_blocks.items():
        sch = SCHOOL_SCHEMES[slug]
        out.append("""

-- ═══════════════════════════════════════════════════════════════════════
-- %(name)s  (schools.slug = '%(slug)s')
--
-- Source: %(source)s
--
%(counts)s-- ═══════════════════════════════════════════════════════════════════════

do $$
begin
  if not exists (select 1 from public.schools where slug = %(qslug)s) then
    raise exception 'KS3 seed: no school with slug %%. Insert the school row '
                    'before seeding its scheme of work.', %(qslug)s;
  end if;
end $$;

-- Idempotency: this block owns every KS3 override row for this school.
delete from public.scheme_of_work_overrides
 where key_stage = 'KS3'
   and school_id = %(school)s;
""" % {"name": sch["name"], "slug": slug, "source": sch["source"],
       "qslug": q(slug), "school": school_id_sql(slug),
       "counts": block_comment(blocks)})

        for year in YEARS:
            for disc in structure.DISCIPLINES:
                rows = blocks.get((year, disc))
                if not rows:
                    continue
                out.append(
                    "\n-- ── Year %d · %s — %d lessons ─────────────────────────\n"
                    % (year, structure.DISCIPLINE_TITLES[disc], len(rows)))
                out.append(
                    "insert into public.scheme_of_work_overrides\n"
                    "  (school_id, key_stage, year_group, tier, pathway, "
                    "subject_id, academic_week, topic, subtopic, notes)\n"
                    "values\n")
                vals = []
                unit = None
                for r in rows:
                    if r["unit_code"] != unit:
                        unit = r["unit_code"]
                        vals.append("  -- %s %s" % (unit, r["topic"]))
                    vals.append(
                        "  (%s, 'KS3', %d, null, null, %s, %d, %s, %s, %s)"
                        % (school_id_sql(slug), r["year_group"],
                           subject_id_sql(disc), r["academic_week"],
                           q(r["topic"]), q(r["subtopic"]), q(r["notes"])))
                out.append(_join_values(vals) + ";\n")

    out.append("\ncommit;\n")
    return "".join(out)


def _join_values(lines):
    """Comma-separate the value tuples, leaving comment lines uncommaed."""
    out = []
    idxs = [i for i, l in enumerate(lines) if not l.lstrip().startswith("--")]
    last = idxs[-1] if idxs else None
    for i, l in enumerate(lines):
        if l.lstrip().startswith("--") or i == last:
            out.append(l)
        else:
            out.append(l + ",")
    return "\n".join(out)


# ── run ──────────────────────────────────────────────────────────────────

def main():
    print("\nks3_seed_sow — generating scheme-of-work seeds\n" + "=" * 60)

    os.makedirs(SEED_DIR, exist_ok=True)

    default_blocks = build_rows(DEFAULT_SEQUENCE_V1, with_half_terms=True)
    check_ceiling(default_blocks, "MrBadmusAI default sequence v1")

    # School rows deliberately carry no half term — see the module docstring.
    school_blocks = {}
    for slug in SCHOOL_SCHEMES:
        sch = SCHOOL_SCHEMES[slug]
        blocks = build_rows(effective_sequence(slug), unit_notes=sch["notes"],
                            with_half_terms=False)
        check_ceiling(blocks, "%s (%s)" % (sch["name"], slug))
        school_blocks[slug] = blocks

    p1 = os.path.join(SEED_DIR, DEFAULT_SEED)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(render_default(default_blocks))
    _report("default sequence", p1, default_blocks)

    p2 = os.path.join(SEED_DIR, SCHOOLS_SEED)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(render_schools(school_blocks))
    for slug, blocks in school_blocks.items():
        _report(SCHOOL_SCHEMES[slug]["name"], p2, blocks)

    return 0


def _report(label, path, blocks):
    total = sum(len(v) for v in blocks.values())
    peak = max((len(v) for v in blocks.values()), default=0)
    print("\n  %s → %s" % (label, path))
    for year in YEARS:
        parts = []
        for disc in structure.DISCIPLINES:
            rows = blocks.get((year, disc))
            if rows:
                parts.append("%-9s %2d" % (structure.DISCIPLINE_TITLES[disc],
                                           len(rows)))
        if parts:
            print("    Y%d  %s" % (year, "   ".join(parts)))
    print("    %d rows · max academic_week %d (ceiling %d)"
          % (total, peak, MAX_ACADEMIC_WEEK))

    if any("half_term" in r for rows in blocks.values() for r in rows):
        print("    lessons per half term (HT1…HT6):")
        for year in YEARS:
            counts = [0] * 6
            for disc in structure.DISCIPLINES:
                for r in blocks.get((year, disc)) or []:
                    counts[r["half_term"] - 1] += 1
            if any(counts):
                print("      Y%d  %s   (%d)"
                      % (year, " ".join("%2d" % n for n in counts),
                         sum(counts)))


if __name__ == "__main__":
    raise SystemExit(main())
