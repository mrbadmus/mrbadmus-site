#!/usr/bin/env python3
"""tools/ks4_extract_pack.py — writes one "checked science source" markdown
file per KS4 subtopic, in exactly the format of the pilot pack at
`Design Pack - Pilot/04-checked-science-source/` (14 files, reverse-
engineered byte-for-byte — see docs/ks4/packs/EXTRACT-PACK.md if that file
exists, or the script's own comments below for the reasoning).

    python3 tools/ks4_extract_pack.py --out docs/ks4/packs/<batch> slug1 slug2 ...
    python3 tools/ks4_extract_pack.py --out docs/ks4/packs/<batch> physics:resistors chemistry:polymers
    python3 tools/ks4_extract_pack.py --out docs/ks4/packs/<batch> --spec some-slug=6.2.3 some-slug

A bare slug is searched across biology/chemistry/physics; if it exists in
more than one subject, pass `subject:slug` instead (the script's error
message says which subjects collided). Subject and topic are both found
from the data — nothing about the lesson needs to be known up front beyond
its subtopic id.

⚠️ This script reads `all_subtopics_*.py` ONLY — never `ks4_data/` (the
question-pool package), per the same hard line `build_ks4.py`'s own
docstring states (KS4 pilot build contract §2). It also deliberately does
NOT import `build_ks4.py` or `ks4_lessons/`: those are being edited
concurrently by another executor on this branch, and this tool has no
business depending on their mid-edit state. Instead it MIRRORS the three
pieces of their logic this tool needs — `load_subtopics_by_route` (as
`_load_route_data`, generalised to scan every topic's list rather than
assume a fixed topic_id, since this tool is handed bare slugs with no
topic context), `find_subtopic`, and the route/field shape
`build_source_record` reads out of `all_subtopics_*.py`. If `build_ks4.py`'s
own `NONQUIZ_FIELDS` ever changes, update `NONQUIZ_FIELDS` below to match —
grep for both names to keep them honest.

Format notes worked out from reading the 14 pilot files side by side with
the data (see the per-section comments for the evidence):

- Header: `# <Title>  (<Subject>, AQA <spec>)` — TWO spaces before the
  `(`. <Title> and <spec> both come straight off the subtopic's own
  `title`/`spec` fields (canonical = the Triple Higher record).
- `**Appears on routes:**` — every route (of CF/CH/TF/TH, in that order)
  whose file actually contains this slug.
- `**Route copies that differ from Triple Higher:**` — of the NON-TH
  routes this lesson appears on, those where ANY field in
  `COPY_CHECK_ORDER` differs from the TH canonical value, in route order;
  `"none"` if no route differs.
- The SOURCE MATERIAL paragraph is fixed, byte-identical boilerplate
  across all 14 pilot files (verified: one md5 across all 14 copies).
- Main sections, in `MAIN_ORDER`, one per field that is TRUTHY on the
  canonical (TH) record. A string-valued field (`summary`,
  `common_mistake`, `examiner_tip`, `key_note`, `rp`, `higher` when it
  holds prose) renders as a plain paragraph under the header with one
  blank line on each side. Any other field (`theory`, `equations`,
  `fifas`, `variables`, `matching`, `quiz` — lists/dicts) renders as a
  &#96;&#96;&#96;json fence, `json.dumps(value, indent=2, sort_keys=True,
  ensure_ascii=False)` — `sort_keys=True` is why `opts`/`q`/
  `wrong_explanations` come out alphabetical in every quiz item, and
  `ensure_ascii=False` is why Ω/°/✓/– print raw rather than escaped.
- Then, for each non-TH route this lesson appears on (CF, CH, TF order),
  for each field in `COPY_CHECK_ORDER` (`["quiz", "higher"]` — NOT all of
  `NONQUIZ_FIELDS`; see that constant's own comment for why) that differs
  from canonical on that route, checked quiz-then-higher (this reproduces
  the pilot pack's own section order, e.g. a `quiz — Combined Foundation
  copy` block before a `higher — Combined Foundation copy` block for the
  same route, even though `higher` is drawn earlier than `quiz` in the
  MAIN section order above): a `## <field> — <Route label> copy (differs
  from the Triple Higher copy above)` section, rendered the same way as
  the main sections (so a route's `higher: None` renders as a fenced
  `null`, not as empty plain text — the renderer picks fenced-vs-plain by
  the VALUE's Python type, not by which field it is).
- Equality for the diff check round-trips both sides through
  `json.dumps`/`json.loads` first (`_normalize`), the same technique
  `build_ks4._json_normalize` uses, so a tuple-vs-list artefact of how
  `all_subtopics_*.py` is authored can never register as a false "differs".
- File name: `<subject>-<spec-for-filename>-<slug>.md`, subject lower-case.
  Where `spec` is a range (`"5.2.2.1–5.2.2.2"`, en dash), the filename uses
  only the FIRST number (`states-of-matter` → `chemistry-5.2.2.1-states-
  of-matter.md`) — verified against the real pilot filenames, which do
  this for every ranged spec in the set (states-of-matter, metals-alloys).
"""

import argparse
import importlib
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

SOURCE_MODULES = {
    "biology": {"CF": "all_subtopics_biology",
                "CH": "all_subtopics_biology_higher",
                "TF": "all_subtopics_biology_triple_foundation",
                "TH": "all_subtopics_biology_triple_higher"},
    "chemistry": {"CF": "all_subtopics_chemistry",
                  "CH": "all_subtopics_chemistry_higher",
                  "TF": "all_subtopics_chemistry_triple_foundation",
                  "TH": "all_subtopics_chemistry_triple_higher"},
    "physics": {"CF": "all_subtopics_physics",
                "CH": "all_subtopics_physics_higher",
                "TF": "all_subtopics_physics_triple_foundation",
                "TH": "all_subtopics_physics_triple_higher"},
}
SOURCE_ATTR = {"biology": "BIOLOGY_SUBTOPICS_ALL",
               "chemistry": "CHEMISTRY_SUBTOPICS_ALL",
               "physics": "PHYSICS_SUBTOPICS_ALL"}

ROUTE_ORDER = ["CF", "CH", "TF", "TH"]
ROUTE_LABELS = {
    "CF": "Combined Foundation", "CH": "Combined Higher",
    "TF": "Triple Foundation", "TH": "Triple Higher",
}

# Mirrors build_ks4.NONQUIZ_FIELDS exactly — keep these two lists in step.
NONQUIZ_FIELDS = ["summary", "theory", "common_mistake", "examiner_tip",
                  "key_note", "matching", "fifas", "equations", "rp",
                  "variables", "higher"]

# Presentation order for the MAIN sections — distinct from NONQUIZ_FIELDS
# (which is only the order build_ks4.py happens to build its dict in).
# Verified against the `## ` headings of all 14 pilot files: summary,
# theory, [higher], common_mistake, [examiner_tip], key_note, [equations],
# [fifas], [rp], [variables], matching, quiz — a field only appears when
# truthy, but whichever subset is present always appears in THIS order.
MAIN_ORDER = ["summary", "theory", "higher", "common_mistake",
              "examiner_tip", "key_note", "equations", "fifas", "rp",
              "variables", "matching", "quiz"]

# The fields CHECKED for a route-copy divergence — NOT all of
# NONQUIZ_FIELDS. `quiz` is build_ks4.build_source_record's one
# genuinely-per-route field; `higher` is the one NONQUIZ field that is
# BY DESIGN tier-gated (every "higher"-field comment in all_subtopics_*.py
# says the field is "never route-varying, like every other non-quiz field
# here" — i.e. every NONQUIZ field except `higher` is an asserted
# invariant across routes, not a candidate for a route-copy diff).
#
# Proof this is the real check, not NONQUIZ_FIELDS wholesale: the pilot's
# `chemistry-5.2.3.3-nanoparticles.md` shows NO `fifas — Triple Foundation
# copy` section, even though the TF record's `fifas` already differed from
# TH's at the pack's cut date (git blame: both versions landed together in
# commit ba4db059e, 13 Jul 2026 — over two months before the pack's 24 Sep
# 2026 cut date, so this isn't post-cut drift). The three regenerated
# packs that differ from the frozen pilot files all come from REAL
# `examiner_tip` content added to the TH data after the cut (the 27 Sep
# 2026 KS4 polish run) — see the executor's report for the slugs/diffs.
COPY_CHECK_ORDER = ["quiz", "higher"]

# Byte-identical across all 14 pilot files (checked: one md5 for all 14).
SOURCE_MATERIAL_PARAGRAPH = (
    "This is SOURCE MATERIAL: checked science to draw from. Quiz questions "
    "(with their wrong-answer explanations), the examiner tip, worked "
    "examples (FIFA), equations and required-practical data are kept "
    "VERBATIM. The theory text may be re-cut. The matching activity is to "
    "be REPLACED (it prints its own answers). It is not a page structure "
    "to copy.")

_MODULE_CACHE = {}


def _load_route_data(subject, route):
    """Mirrors build_ks4.load_subtopics_by_route for one (subject, route)
    — imported lazily and cached, so a CLI run touching one subject never
    imports the other two subjects' eight route modules."""
    key = (subject, route)
    if key not in _MODULE_CACHE:
        modname = SOURCE_MODULES[subject][route]
        mod = importlib.import_module(modname)
        _MODULE_CACHE[key] = getattr(mod, SOURCE_ATTR[subject])
    return _MODULE_CACHE[key]


def find_subtopic(subject, route, slug):
    """(topic_id, record) for `slug` in `subject`'s `route` file, or
    (None, None). Mirrors build_ks4.find_subtopic, but scans every topic's
    list rather than taking a topic_id as given — this tool is handed bare
    slugs with no topic context, unlike build_ks4.py's lesson table."""
    data = _load_route_data(subject, route)
    for topic_id, lst in data.items():
        for s in lst:
            if s.get("id") == slug:
                return topic_id, s
    return None, None


def subject_has_slug(subject, slug):
    for route in ROUTE_ORDER:
        if find_subtopic(subject, route, slug)[1] is not None:
            return True
    return False


def resolve_slug(token):
    """`token` is 'slug' or 'subject:slug'. Returns (subject, slug), or
    raises SystemExit with a clear message on unknown/ambiguous input."""
    if ":" in token:
        subject, slug = token.split(":", 1)
        subject = subject.strip().lower()
        slug = slug.strip()
        if subject not in SOURCE_MODULES:
            raise SystemExit(
                "ks4_extract_pack: unknown subject %r in %r (expected one "
                "of biology, chemistry, physics)" % (subject, token))
        if not subject_has_slug(subject, slug):
            raise SystemExit(
                "ks4_extract_pack: %r not found in KS4 %s data"
                % (slug, subject))
        return subject, slug

    slug = token.strip()
    matches = [s for s in ("biology", "chemistry", "physics")
               if subject_has_slug(s, slug)]
    if not matches:
        raise SystemExit(
            "ks4_extract_pack: unknown KS4 subtopic slug %r (no match in "
            "biology, chemistry or physics)" % slug)
    if len(matches) > 1:
        raise SystemExit(
            "ks4_extract_pack: %r is ambiguous — it exists in KS4 %s. "
            "Disambiguate with subject:slug, e.g. %s:%s"
            % (slug, " and ".join(matches), matches[0], slug))
    return matches[0], slug


def appears_on_routes(subject, slug):
    return [r for r in ROUTE_ORDER
            if find_subtopic(subject, r, slug)[1] is not None]


def canonical_record(subject, slug, routes):
    """The Triple Higher record — always present for every real pilot
    lesson (build_ks4.build_source_record makes the identical assumption
    and hard-fails if it isn't). Falls back to the first other route
    present and WARNS, rather than hard-failing, since this tool runs
    against the full KS4 corpus rather than the 14-lesson pilot set and a
    future subtopic missing a TH copy is a data finding, not a bug in this
    script."""
    for route in ["TH"] + [r for r in ROUTE_ORDER if r != "TH"]:
        if route in routes:
            _, rec = find_subtopic(subject, route, slug)
            if rec is not None:
                if route != "TH":
                    print("ks4_extract_pack: WARNING — %s:%s has no Triple "
                          "Higher record; using %s as the canonical copy "
                          "instead" % (subject, slug, ROUTE_LABELS[route]),
                          file=sys.stderr)
                return rec
    raise SystemExit("ks4_extract_pack: %s:%s has no record on any route"
                      % (subject, slug))


def _normalize(value):
    """Round-trips through JSON so a Python tuple (how every opts/pairs/
    steps list is authored in all_subtopics_*.py) compares equal to the
    JSON-equivalent list it serialises to — the same technique
    build_ks4._json_normalize uses, and for the same reason: without it,
    `[('a', True)] == [['a', True]]` is False in Python."""
    return json.loads(json.dumps(value, sort_keys=True))


def render_block(value):
    """A string renders as a plain paragraph; anything else (list/dict/
    None/number) renders as a ```json fence. The SAME rule is used for
    main sections and for route-copy sections — a route's `higher: None`
    therefore renders as a fenced `null`, matching every null copy in the
    14-file pilot pack."""
    if isinstance(value, str):
        return value
    return "```json\n" + json.dumps(value, indent=2, sort_keys=True,
                                     ensure_ascii=False) + "\n```"


def build_doc(subject, slug, spec_overrides):
    routes = appears_on_routes(subject, slug)
    if not routes:
        raise SystemExit("ks4_extract_pack: %s:%s appears on no route"
                          % (subject, slug))
    canon = canonical_record(subject, slug, routes)

    title = canon.get("title") or slug
    spec = canon.get("spec")
    if not spec:
        if slug in spec_overrides:
            spec = spec_overrides[slug]
        else:
            spec = "?"
            print("ks4_extract_pack: WARNING — %s:%s has no spec field in "
                  "the data and no --spec override was given; writing '?'"
                  % (subject, slug), file=sys.stderr)

    subject_title = subject.capitalize()

    non_th_routes = [r for r in routes if r != "TH"]
    route_recs = {r: find_subtopic(subject, r, slug)[1] for r in non_th_routes}
    diffs = {}
    for r in non_th_routes:
        rec = route_recs[r]
        fields = [f for f in COPY_CHECK_ORDER
                  if _normalize(rec.get(f)) != _normalize(canon.get(f))]
        if fields:
            diffs[r] = fields

    differ_routes = [r for r in non_th_routes if r in diffs]
    differ_text = (", ".join(ROUTE_LABELS[r] for r in differ_routes)
                   if differ_routes else "none")

    parts = []
    parts.append("# %s  (%s, AQA %s)\n" % (title, subject_title, spec))
    parts.append("\n")
    parts.append("**Appears on routes:** %s\n"
                 % ", ".join(ROUTE_LABELS[r] for r in routes))
    parts.append("**Route copies that differ from Triple Higher:** %s "
                 "(the route tags are to be set from the AQA spec's own HT "
                 "/ separate-science labels, not from these copies)\n"
                 % differ_text)
    parts.append("\n")
    parts.append(SOURCE_MATERIAL_PARAGRAPH + "\n")

    def section(heading, value):
        parts.append("\n## %s\n" % heading)
        if isinstance(value, str):
            parts.append("\n%s\n" % value)
        else:
            parts.append(render_block(value) + "\n")

    for field in MAIN_ORDER:
        value = canon.get(field)
        if value:
            section(field, value)

    for r in non_th_routes:
        for field in diffs.get(r, []):
            heading = "%s — %s copy (differs from the Triple Higher copy " \
                      "above)" % (field, ROUTE_LABELS[r])
            section(heading, route_recs[r].get(field))

    text = "".join(parts)

    spec_for_filename = "unknown" if spec == "?" else spec.split("–")[0]
    filename = "%s-%s-%s.md" % (subject, spec_for_filename, slug)
    return filename, text


def parse_spec_overrides(raw_list):
    out = {}
    for item in raw_list or []:
        if "=" not in item:
            raise SystemExit("ks4_extract_pack: --spec expects slug=value, "
                              "got %r" % item)
        slug, value = item.split("=", 1)
        out[slug.strip()] = value.strip()
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Write one checked-science-source markdown pack per "
                     "KS4 subtopic, in the pilot pack's exact format.")
    ap.add_argument("slugs", nargs="+",
                     help="subtopic ids, bare ('resistors') or "
                          "'subject:slug' ('physics:resistors') when a "
                          "bare slug is ambiguous across subjects")
    ap.add_argument("--out", required=True,
                     help="output directory; created if it doesn't exist")
    ap.add_argument("--spec", action="append", default=[],
                     metavar="slug=value",
                     help="spec-number override for a subtopic whose data "
                          "has no spec field; repeatable")
    args = ap.parse_args(argv)

    spec_overrides = parse_spec_overrides(args.spec)
    os.makedirs(args.out, exist_ok=True)

    written = []
    for token in args.slugs:
        subject, slug = resolve_slug(token)
        filename, text = build_doc(subject, slug, spec_overrides)
        path = os.path.join(args.out, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        written.append(path)
        print("wrote %s" % path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
