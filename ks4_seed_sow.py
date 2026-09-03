"""ks4_seed_sow.py — generate the KS4 scheme-of-work seed SQL.

Run it:

    python3 ks4_seed_sow.py

Writes one file, generated, never hand-edited:

    supabase/seeds/20260902001000_ks4_default_sequence.sql
        → public.scheme_of_work_entries — the GLOBAL table. One row per KS4
          subtopic PAGE, per (pathway, tier, subject) block.

**Why generate rather than write.** The KS4 site already knows its own
curriculum: `generate_site_v5.PATHWAY_TOPIC_MAP` says which topics a pathway
and tier teach and in what order, and the twelve `all_subtopics_*.py` modules
say which pages sit inside each topic. A hand-written scheme of work would be a
second description of the same thing, and two descriptions drift. A drifted
row is a teacher's sequence pointing at a page that does not exist — which
fails silently, because nothing joins on it. So this file is a projection of
the site's own data, and it re-checks every href against `mrbadmus_site/`
before it will write anything.

**Ordering authority.** `PATHWAY_TOPIC_MAP` is imported, not copied. Importing
`generate_site_v5` is safe: everything past its data tables is behind
`if __name__ == "__main__"`, so an import reads the module and builds nothing.
Topic display titles come from `generate_site_v5.SITE_DATA[subject]["topics"]`,
each entry of which carries `id` and `title` — the same title the built topic
page shows, so a teacher reading a scheme row and a student reading the page
see the same words.

**⚠️ FIVE BLOCKS DO NOT FIT, AND ROWS ARE OMITTED.**

`scheme_of_work_entries.academic_week` carries
`CHECK (academic_week BETWEEN 1 AND 39)`, and the base unique key is
`(key_stage, year_group, tier, pathway, subject_id, exam_board,
academic_week)`. That is a hard ceiling of 39 rows per year and therefore 78
per (pathway, tier, subject) block across Years 10 and 11. Five KS4 blocks are
larger than that — triple/foundation biology (87) and chemistry (83),
triple/higher biology (89), chemistry (93) and physics (82) — and the
year-split can push a smaller block's half over 39 too, because the split
lands on a TOPIC boundary rather than mid-topic.

Where a year's slice exceeds the ceiling it is TRUNCATED, and every dropped
subtopic is listed by name in a `-- ⚠️ OMITTED` block in the generated SQL and
printed to stdout. Nothing disappears quietly; the loss is written into the
artefact that causes it.

**The fix is a migration, not a generator change.** Raise the KS4 ceiling on
`academic_week` — to at least 47, which is what the largest year slice here
needs — and re-run this generator, and all 865 rows are emitted with no
truncation at all. Until that migration exists, this seed is deliberately
incomplete and says so in its own header.

**The year split.** A block is cut into Year 10 and Year 11 at a topic
boundary, never through the middle of a topic: half of Bonding in Year 10 and
half in Year 11 is not a thing anyone teaches. The boundary chosen is the one
whose cumulative subtopic count sits closest to half the block, ties going to
the earlier boundary so the result is deterministic rather than
dictionary-order dependent.

**What the columns carry.** `topic` is the topic's human title, `subtopic` is
the page slug, and `notes` is the page href — so a row is resolvable to the
page it describes without anyone reconstructing the path convention by hand.
`half_term` is NULL on every row: `scheme_of_work_entries_half_term_is_ks3_only`
forbids it outside KS3, because a half-term map is a KS3 sequencing artefact
and KS4 has no equivalent ruling.
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_site_v5 import PATHWAY_TOPIC_MAP, SITE_DATA

SEED_DIR = os.path.join("supabase", "seeds")
SEED_FILE = "20260902001000_ks4_default_sequence.sql"

# Where the built pages live. Every href this generator emits is checked
# against this tree before the file is written — see check_hrefs().
SITE_DIR = "mrbadmus_site"

# The hard ceiling from the table definition. It was 39 (the KS3 rule, one
# school year of teaching order) until migration 20260902001200-era
# `mrb310_ks4_scheme_week_ceiling` widened KS4 to 52: a Triple Higher
# Chemistry year needs 48 slots. Raising this constant alone changes nothing —
# the CHECK is in the database, and the migration has to move first.
MAX_ACADEMIC_WEEK = 52

YEARS = (10, 11)

SUBJECTS = ("biology", "chemistry", "physics")

SUBJECT_TITLES = {
    "biology": "Biology",
    "chemistry": "Chemistry",
    "physics": "Physics",
}

# (pathway, tier) → the suffix on the all_subtopics_<subject><suffix>.py
# module that holds that combination's pages. The four modules per subject are
# separate files rather than one filtered file, which is why this map exists at
# all; it mirrors what generate_site_v5 loads for the same combination.
MODULE_SUFFIX = {
    ("combined", "foundation"): "",
    ("combined", "higher"): "_higher",
    ("triple", "foundation"): "_triple_foundation",
    ("triple", "higher"): "_triple_higher",
}

# Emitted in the order a reader expects to review them, not in dict order.
BLOCKS = [(p, t, s)
          for p in ("combined", "triple")
          for t in ("foundation", "higher")
          for s in SUBJECTS]


def q(s):
    """A SQL string literal, or NULL. Single quotes doubled, per the standard."""
    if s is None:
        return "null"
    return "'%s'" % str(s).replace("'", "''")


def subject_id_sql(subject):
    """subject_id by NAME, never a hardcoded uuid.

    uuids differ between the test project and production, so a seed carrying
    one is a seed that works in exactly one place. Looking the row up by its
    natural key makes the file portable, and makes a missing subject row fail
    loudly on the NOT NULL rather than silently on the wrong id.
    """
    return ("(select id from public.subjects where name = %s)"
            % q(SUBJECT_TITLES[subject]))


# ── the source data ──────────────────────────────────────────────────────

def topic_titles(subject):
    """topic id → human title, from SITE_DATA — the same title the page shows.

    Title-casing the slug would be the obvious fallback and the wrong answer:
    it turns `rates-equilibrium` into "Rates Equilibrium" where AQA and the
    built page both say "Rate and Extent of Chemical Change".
    """
    return {t["id"]: t["title"] for t in SITE_DATA[subject]["topics"]}


def subtopics_for(pathway, tier, subject):
    """The block's pages as (topic_id, topic_title, subtopic_id) in teaching order.

    Topic order comes from PATHWAY_TOPIC_MAP, which is the ordering authority;
    subtopic order is the authored order inside the module's list, which is the
    order the topic page itself renders them in.
    """
    module = importlib.import_module(
        "all_subtopics_%s%s" % (subject, MODULE_SUFFIX[(pathway, tier)]))
    pages = getattr(module, "%s_SUBTOPICS_ALL" % subject.upper())
    titles = topic_titles(subject)

    out = []
    for topic_id in PATHWAY_TOPIC_MAP[(pathway, tier)][subject]:
        if topic_id not in pages:
            # A topic the pathway teaches but the module has no pages for is a
            # real gap in the content, not something to skip past quietly.
            raise KeyError(
                "ks4_seed_sow: %s/%s %s teaches topic '%s' but "
                "all_subtopics_%s%s.py has no subtopics for it."
                % (pathway, tier, subject, topic_id, subject,
                   MODULE_SUFFIX[(pathway, tier)]))
        for st in pages[topic_id]:
            out.append((topic_id, titles.get(topic_id, topic_id), st["id"]))
    return out


def href(pathway, tier, subject, topic_id, subtopic_id):
    """The built page's path. Verified on disk, never assumed — see check_hrefs."""
    return "/%s/%s/%s/%s/%s.html" % (pathway, tier, subject, topic_id,
                                     subtopic_id)


# ── the split, and the ceiling ───────────────────────────────────────────

def split_index(rows):
    """Where Year 10 ends and Year 11 begins, as an index into `rows`.

    The cut lands on a TOPIC boundary, always. Splitting a topic across two
    academic years describes a sequence nobody teaches — half of Bonding in
    Year 10 and half in Year 11 — and a scheme of work is a description of
    teaching, so it has to be one a teacher could recognise.

    Among the topic boundaries, the one nearest half the block wins. Ties go to
    the earlier boundary: an arbitrary but fixed choice, so re-running the
    generator on unchanged data produces an unchanged file.
    """
    target = len(rows) / 2.0
    boundaries = []
    for i in range(1, len(rows)):
        if rows[i][0] != rows[i - 1][0]:
            boundaries.append(i)
    if not boundaries:
        # A single-topic block cannot be split at a topic boundary at all, so
        # it is taught whole in Year 10.
        return len(rows)
    return min(boundaries, key=lambda i: (abs(i - target), i))


def build_block(pathway, tier, subject):
    """One (pathway, tier, subject) block, laid out as rows plus its omissions.

    Returns (rows, omitted). Each row carries its year, academic week and the
    href it describes. `omitted` holds everything the 39-week ceiling pushed
    off the end of a year, in the order it would have been taught.
    """
    pages = subtopics_for(pathway, tier, subject)
    cut = split_index(pages)
    slices = [(10, pages[:cut]), (11, pages[cut:])]

    rows, omitted = [], []
    for year, slice_pages in slices:
        for n, (topic_id, topic_title, subtopic_id) in enumerate(slice_pages,
                                                                 start=1):
            entry = {
                "pathway": pathway,
                "tier": tier,
                "subject": subject,
                "year_group": year,
                "academic_week": n,
                "topic_id": topic_id,
                "topic": topic_title,
                "subtopic": subtopic_id,
                "notes": href(pathway, tier, subject, topic_id, subtopic_id),
            }
            # TRUNCATE rather than renumber or spill into the next year. Both
            # alternatives lie: renumbering would put two lessons in one week,
            # and spilling would claim Year 11 teaches content Year 10 owns.
            # Dropping the row and NAMING it is the only option that leaves the
            # loss visible.
            if n > MAX_ACADEMIC_WEEK:
                omitted.append(entry)
            else:
                rows.append(entry)
    return rows, omitted


def check_hrefs(all_rows, all_omitted):
    """Every href — kept AND omitted — must resolve to a built page.

    The omitted ones are checked too, because they are named in the SQL as
    content this seed knows about and did not place. A name in that list that
    points at nothing is a worse artefact than no list at all.

    Raises. A missing page means the generator's path convention and the
    generator that writes the pages have diverged, and a seed full of dead
    hrefs would apply cleanly and be wrong.
    """
    missing = []
    for entry in list(all_rows) + list(all_omitted):
        path = os.path.join(SITE_DIR, entry["notes"].lstrip("/"))
        if not os.path.isfile(path):
            missing.append(entry["notes"])
    if missing:
        raise FileNotFoundError(
            "ks4_seed_sow: %d emitted href(s) do not exist under %s/ — the "
            "seed would describe pages that are not built. First 20:\n  %s"
            % (len(missing), SITE_DIR, "\n  ".join(missing[:20])))


# ── rendering ────────────────────────────────────────────────────────────

def header(path, counts, omitted_by_block, peak_week):
    total = sum(counts.values())
    dropped = sum(len(v) for v in omitted_by_block.values())

    lines = []
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("-- KS4 — AQA default sequence, as scheme-of-work rows.")
    lines.append("--")
    lines.append("-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.")
    lines.append("--    Regenerate with:  python3 ks4_seed_sow.py")
    lines.append("--    Source of truth:  generate_site_v5.py (PATHWAY_TOPIC_MAP, SITE_DATA)")
    lines.append("--                      all_subtopics_{biology,chemistry,physics}*.py")
    lines.append("--    Written to:       %s" % path)
    lines.append("--    Target table:     public.scheme_of_work_entries (GLOBAL — no school_id)")
    lines.append("--")
    lines.append("-- Hand-editing this file makes it disagree with the site's own curriculum")
    lines.append("-- data, and a scheme row that disagrees with the built pages is a teacher")
    lines.append("-- pointing at a page that does not exist. Change the Python, re-run the")
    lines.append("-- generator. Every href below was checked against mrbadmus_site/ at")
    lines.append("-- generation time.")
    lines.append("--")
    lines.append("-- Idempotent: every KS4 row is deleted and rewritten, inside one")
    lines.append("-- transaction. Re-running is safe and is the intended way to apply a change.")
    lines.append("--")
    lines.append("-- KS4 rows carry exam_board = 'AQA', a tier and a pathway on every row —")
    lines.append("-- the same subtopic is taught in up to four blocks and the three columns")
    lines.append("-- are what tells them apart. half_term is NULL throughout: the constraint")
    lines.append("-- scheme_of_work_entries_half_term_is_ks3_only forbids it outside KS3.")
    lines.append("--")
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("-- ⚠️ THIS SEED IS DELIBERATELY INCOMPLETE — %d OF %d ROWS ARE OMITTED."
                 % (dropped, total + dropped))
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("--")
    lines.append("-- academic_week carries CHECK (academic_week BETWEEN 1 AND %d), and the"
                 % MAX_ACADEMIC_WEEK)
    lines.append("-- base unique key (key_stage, year_group, tier, pathway, subject_id,")
    lines.append("-- exam_board, academic_week) allows one row per week. That caps a")
    lines.append("-- (pathway, tier, subject) block at %d rows across Years 10 and 11."
                 % (MAX_ACADEMIC_WEEK * 2))
    lines.append("--")
    lines.append("-- Five KS4 blocks are larger than that cap. Where a year's slice runs")
    lines.append("-- past week %d the remainder is dropped, and every dropped subtopic is"
                 % MAX_ACADEMIC_WEEK)
    lines.append("-- named in the OMITTED block at the foot of this file. Nothing vanishes")
    lines.append("-- silently.")
    lines.append("--")
    lines.append("-- ➤ THE FIX IS A MIGRATION, NOT A GENERATOR CHANGE. Raise the KS4 ceiling")
    lines.append("--   on academic_week to at least %d — the largest year slice this"
                 % peak_week)
    lines.append("--   curriculum needs — and re-run `python3 ks4_seed_sow.py`. All %d rows"
                 % (total + dropped))
    lines.append("--   are then emitted with no truncation whatsoever. Until that migration")
    lines.append("--   lands, %d subtopic pages have no scheme-of-work row." % dropped)
    lines.append("--")
    lines.append("-- Rows emitted per block, generated:")
    lines.append("--")
    for pathway, tier, subject in BLOCKS:
        key = (pathway, tier, subject)
        kept = counts[key]
        lost = len(omitted_by_block[key])
        note = "" if not lost else "   (%d omitted of %d)" % (lost, kept + lost)
        lines.append("--   %-9s %-10s %-9s %3d%s"
                     % (pathway, tier, SUBJECT_TITLES[subject], kept, note))
    lines.append("--")
    lines.append("--   %d rows emitted, %d omitted, %d total pages in the curriculum."
                 % (total, dropped, total + dropped))
    lines.append("--")
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("")
    lines.append("")
    return "\n".join(lines)


def render(rows_by_block, omitted_by_block, peak_week):
    counts = {k: len(v) for k, v in rows_by_block.items()}
    out = [header(os.path.join(SEED_DIR, SEED_FILE), counts, omitted_by_block,
                  peak_week)]

    out.append("begin;\n")
    out.append("""
-- Preconditions. Failing here with a sentence beats failing later with a
-- NOT NULL violation on a subselect that quietly returned NULL.
do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS4 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;

-- Idempotency: this file owns every KS4 row in the global table.
delete from public.scheme_of_work_entries where key_stage = 'KS4';
""")

    for pathway, tier, subject in BLOCKS:
        rows = rows_by_block[(pathway, tier, subject)]
        for year in YEARS:
            year_rows = [r for r in rows if r["year_group"] == year]
            if not year_rows:
                continue
            out.append(
                "\n-- ── %s · %s · %s · Year %d — %d lessons "
                "─────────────────────\n"
                % (pathway.title(), tier.title(), SUBJECT_TITLES[subject],
                   year, len(year_rows)))
            out.append(
                "insert into public.scheme_of_work_entries\n"
                "  (key_stage, year_group, tier, pathway, subject_id, "
                "exam_board, academic_week, half_term, topic, subtopic, notes, "
                "active)\n"
                "values\n")
            vals = []
            topic = None
            for r in year_rows:
                if r["topic_id"] != topic:
                    topic = r["topic_id"]
                    vals.append("  -- %s — %s" % (topic, r["topic"]))
                vals.append(
                    "  ('KS4', %d, %s, %s, %s, 'AQA', %d, null, %s, %s, %s, "
                    "true)"
                    % (r["year_group"], q(tier), q(pathway),
                       subject_id_sql(subject), r["academic_week"],
                       q(r["topic"]), q(r["subtopic"]), q(r["notes"])))
            out.append(_join_values(vals) + ";\n")

    out.append("\ncommit;\n")
    out.append(omitted_comment(omitted_by_block, peak_week))
    return "".join(out)


def omitted_comment(omitted_by_block, peak_week):
    """Every dropped subtopic, named, at the foot of the file.

    It sits AFTER the commit deliberately. It is not something the database
    does; it is the record of what this seed could not say, kept next to what
    it did say so the two cannot be separated.
    """
    dropped = sum(len(v) for v in omitted_by_block.values())
    lines = ["", ""]
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("-- ⚠️ OMITTED — %d subtopic pages with no scheme-of-work row." % dropped)
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    lines.append("--")
    if not dropped:
        lines.append("-- None. Every subtopic in the curriculum has a row above.")
        lines.append("--")
        return "\n".join(lines) + "\n"
    lines.append("-- These pages exist and are taught. They are absent from the table only")
    lines.append("-- because their year's slice ran past academic_week %d, which the table"
                 % MAX_ACADEMIC_WEEK)
    lines.append("-- CHECK forbids. Raise the KS4 ceiling to %d and re-run the generator;"
                 % peak_week)
    lines.append("-- every name below then gets a row and this block empties itself.")
    lines.append("--")
    lines.append("-- Summary, one line per affected block:")
    lines.append("--")
    for pathway, tier, subject in BLOCKS:
        lost = omitted_by_block[(pathway, tier, subject)]
        if not lost:
            continue
        years = sorted({e["year_group"] for e in lost})
        lines.append("--   %-9s %-10s %-9s  %d omitted (Year %s)"
                     % (pathway, tier, SUBJECT_TITLES[subject], len(lost),
                        ", ".join(str(y) for y in years)))
    lines.append("--")
    lines.append("-- Full list:")
    for pathway, tier, subject in BLOCKS:
        lost = omitted_by_block[(pathway, tier, subject)]
        if not lost:
            continue
        lines.append("--")
        lines.append("--   ── %s / %s / %s — %d omitted ──"
                     % (pathway, tier, SUBJECT_TITLES[subject], len(lost)))
        topic = None
        for e in lost:
            if e["topic_id"] != topic:
                topic = e["topic_id"]
                lines.append("--     %s" % e["topic"])
            lines.append("--       Y%d  %s   %s"
                         % (e["year_group"], e["subtopic"], e["notes"]))
    lines.append("--")
    lines.append("-- ═══════════════════════════════════════════════════════════════════════")
    return "\n".join(lines) + "\n"


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
    print("\nks4_seed_sow — generating the KS4 scheme-of-work seed\n" + "=" * 68)

    os.makedirs(SEED_DIR, exist_ok=True)

    rows_by_block, omitted_by_block = {}, {}
    for pathway, tier, subject in BLOCKS:
        rows, omitted = build_block(pathway, tier, subject)
        rows_by_block[(pathway, tier, subject)] = rows
        omitted_by_block[(pathway, tier, subject)] = omitted

    all_rows = [r for v in rows_by_block.values() for r in v]
    all_omitted = [r for v in omitted_by_block.values() for r in v]
    check_hrefs(all_rows, all_omitted)

    # The ceiling the migration would have to reach for nothing to be dropped:
    # the largest single-year slice across every block.
    peak_week = 0
    for (pathway, tier, subject) in BLOCKS:
        pages = subtopics_for(pathway, tier, subject)
        cut = split_index(pages)
        peak_week = max(peak_week, cut, len(pages) - cut)

    path = os.path.join(SEED_DIR, SEED_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(rows_by_block, omitted_by_block, peak_week))

    _report(path, rows_by_block, omitted_by_block, peak_week)
    return 0


def _report(path, rows_by_block, omitted_by_block, peak_week):
    total = sum(len(v) for v in rows_by_block.values())
    dropped = sum(len(v) for v in omitted_by_block.values())

    print("\n  written → %s\n" % path)
    print("  %-9s %-10s %-9s  %5s %5s %5s   %s"
          % ("pathway", "tier", "subject", "Y10", "Y11", "rows", "omitted"))
    for pathway, tier, subject in BLOCKS:
        key = (pathway, tier, subject)
        rows = rows_by_block[key]
        y10 = sum(1 for r in rows if r["year_group"] == 10)
        y11 = sum(1 for r in rows if r["year_group"] == 11)
        lost = len(omitted_by_block[key])
        print("  %-9s %-10s %-9s  %5d %5d %5d   %s"
              % (pathway, tier, SUBJECT_TITLES[subject], y10, y11, len(rows),
                 ("%d" % lost) if lost else "-"))

    print("\n  %d rows emitted · %d omitted · %d pages in the curriculum"
          % (total, dropped, total + dropped))
    print("  ceiling %d per year (table CHECK). Largest year slice needed: %d."
          % (MAX_ACADEMIC_WEEK, peak_week))

    if dropped:
        print("\n  ⚠️ OMITTED, per block:")
        for pathway, tier, subject in BLOCKS:
            lost = omitted_by_block[(pathway, tier, subject)]
            if not lost:
                continue
            years = sorted({e["year_group"] for e in lost})
            print("     %-9s %-10s %-9s  %d (Year %s)"
                  % (pathway, tier, SUBJECT_TITLES[subject], len(lost),
                     ", ".join(str(y) for y in years)))
        print("\n  Raise academic_week's KS4 ceiling to %d and re-run to emit "
              "all %d rows." % (peak_week, total + dropped))


if __name__ == "__main__":
    raise SystemExit(main())
