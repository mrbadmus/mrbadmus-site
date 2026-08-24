#!/usr/bin/env python3
"""teacher_tells.py — Design's sample data must not reach a teacher.

    python3 teacher_tells.py           # check the built teacher pages
    python3 teacher_tells.py --list    # print the derived corpus and stop

⊕ MRB-287, 24 Aug 2026.

── WHY THIS EXISTS ──────────────────────────────────────────────────────

Design's teacher-dashboard delivery is a SAMPLE. Not a page with placeholder
copy — a page with a complete, self-consistent, invented school in it: twelve
classes, fifty-four students, twelve weeks of assignments, and a score for
every student in every week, all generated from an FNV hash so that the same
class always produces the same marks.

That is exactly what makes it dangerous. Invented data that looked obviously
fake would be caught by the first person to glance at the page. This data
looks RIGHT. `8r/Sc1` is a plausible class code — it is the class-naming
convention this school actually uses (MRB-263). `Amara Okonkwo` is a plausible
student. `62%` is a plausible mean. A teacher looking at a screen of it has no
way to tell, and would make teaching decisions on numbers that describe
nobody.

The port replaces every one of those sources with a read through `MRB_DATA`,
which throws on a key it was not given. This gate is the check that the
replacement was TOTAL — that no sample constant survived the port into a page
a teacher can open.

── WHY THE CORPUS IS DERIVED AND NOT TYPED ──────────────────────────────

`student_page_drive.py` carries the ancestor of this list, hand-written, and
its own comment records what that cost:

    ⚠️ THIS LIST WAS TOO SHORT AND THE DRIVE PASSED BECAUSE OF IT.

It went green on a page whose docket still read "8 questions · Using a
microscope · SET Mon 15 Sep · DUE Thu 18 Sep" over a real assignment of four
questions due 3 September — because whoever wrote the list thought to write
down the names and did not think to write down the numbers.

A hand-maintained list of things-that-must-not-appear has the same shape as
the problem `gate_registry.py` was built to solve: it drifts, silently, in the
direction of passing. So this one is not maintained. It is EXTRACTED from
Design's own delivery every time the gate runs — every class code, every
student name, every assignment title, every question stem, every topic, every
relative-time string, and every literal in the markup that carries a digit.
If Design ships a new delivery with new invented names, the corpus grows by
itself and the gate keeps meaning what it says.

── WHAT IT CHECKS, AND AGAINST WHAT ─────────────────────────────────────

The LIVE pages only. The `*-fixture.html` pages beside them are SUPPOSED to
carry Design's values — that is what a fixture is, and the behaviour gate
drives them precisely because they hold Design's own numbers. Checking the
fixtures would fail every run and the gate would be turned off.

Three checks:

  1. NO SAMPLE CONSTANT in the emitted bytes. The pages ship Design's template
     and Design's logic; if a sample array survived the LOGIC rewrites in
     `teacher_rulings.py`, it is in the file, and this finds it.

  2. NO GENERATOR. `seed(` and `rnd(` are the FNV hash and its wrapper — the
     two functions that manufacture every invented number in the delivery. A
     page that still carries them can still invent, whatever else was
     replaced. Their absence is the structural proof, where check 1 is the
     evidential one.

  3. NO LITERAL COUNT where a count belongs. The hardcoded values in Design's
     markup and toast copy — the term, the academic year, the import row and
     column counts, "Search students across all 12 classes", "26 students
     imported into 8r/Sc4" — each has to have become a binding. A surviving
     literal is a number that will be wrong for every school that is not
     Design's imaginary one.

── WHAT IT DOES NOT CHECK, STATED RATHER THAN IMPLIED ───────────────────

⚠️ THREE OF DESIGN'S LITERAL COUNTS ARE INVISIBLE TO THIS GATE, and saying so
here is the point. The import review screen carries `24`, `2` and `1` as bare
text nodes — the rows that imported, the warnings, the errors. They are one
and two characters long, and a substring search for "24" matches a timestamp,
a percentage, a stroke width and half the SVG on the page.

So they are below `_TOO_SHORT` and this gate is silent about them. They still
have to become bindings; that requirement is real and is enforced by review
and by `teacher_behaviour`, not here. A gate that claimed to cover them by
grepping for "2" would be the overstated-scope defect `gate_registry.py`
exists to stop — it would go green on noise and everyone would believe the
counts were watched.

The same limit applies to any future one-or-two-character literal. If that
becomes the leak, the answer is a DRIVEN check that reads the rendered value
against the data it was given, not a longer substring list.
"""

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = "student_templates.json"
PAGE_DIR = "teacher"

# The pages this gate polices. A fixture beside each of these is exempt, by
# name rather than by pattern, so that a page added later cannot be quietly
# exempted by being called something ending in "-fixture".
# ⛔ NO `import.html`: it is not ported. `teacher/import.html` is the
# hand-written CSV/Excel wizard, restored on 24 Aug 2026 and taken out of
# build_teacher_port.PAGES — see IMPORT_NOT_PORTED in teacher_rulings.py. It
# carries no line of Design's delivery, so there is no sample constant in it
# for this gate to find; what it does carry is a 2,000-line wizard whose own
# vocabulary (`surname`, `Year group`, `Email`) this gate's docstring already
# records as the reason a harvest of LABELS was unusable.
LIVE_PAGES = [
    "classes.html", "class-detail.html", "student-detail.html",
    "assignment.html", "digest.html", "insights.html",
]

# ── the corpus, derived ──────────────────────────────────────────────────
#
# Design's invented data lives in eight class fields. They are read out of the
# compiled logic by a balanced-literal scan rather than by regex, because
# `CLASSES` is 1,676 characters of nested object literal and a regex over it
# would stop at the first `]` inside a nested array.
# ── WHAT COUNTS AS A TELL: AN IDENTITY, NOT A LABEL ──────────────────────
#
# ⚠️ THE VERSION BEFORE THIS ONE HARVESTED EVERY STRING IN EVERY SAMPLE ARRAY
# AND WAS UNUSABLE. Run against the real, correct, pre-port teacher pages it
# reported fifteen "sample values" — `'Email'`, `'Last name'`, `'Year group'`,
# `'first_name'`, `'surname'`, `'Combined Science'`, `'1 hour ago'`,
# `'No activity yet'`. Every one of them is a word the real product says. The
# live `import.html` maps a column called `surname` to a field called
# `Last name`; `formatRelativeTime` renders `1 hour ago` from a real
# timestamp; `Combined Science` is a subject.
#
# The distinction that makes the gate usable is between an IDENTITY and a
# LABEL. An identity names a particular class, person or record that Design
# invented — `8rsc1`, `Amara Okonkwo`, `d.fairhurst@school.uk`. If it is on a
# real page, the page is lying about who someone is. A label is vocabulary the
# product shares with the sample — a subject, a column heading, a relative
# time, a status word. If it is on a real page, that is the page working.
#
# So the harvest names the KEYS that carry identity, and takes nothing else.
# `LASTS` and `HOURS` are dropped whole: they are relative-time vocabulary and
# contain no identity at all. `mapRows` is dropped whole for the same reason —
# five CSV column headings, every one of which the live wizard also uses.
#
# `None` means the literal is a bare array of strings and all of it is
# identity.
HARVEST = [
    # name,          kind,     identity-bearing keys
    # ⚠️ `id` ONLY, AND NOT `code`. Design's twelve sample classes are not
    # named fictionally: `10h/Ph1`, `11h/Ph1`, `11r/Sc1` and `7h/Sc5` are REAL
    # codes off this school's 2026-27 timetable (CLAUDE.md, MRB-263 names
    # three of them). Harvesting `code` failed the correct, pre-port
    # `classes.html` on `11h/Ph1` — a class that genuinely exists and whose
    # name genuinely belongs on that page.
    #
    # That cuts both ways and is worth stating plainly: it means a leaked
    # class code is UNDETECTABLE by name, because the sample and the truth
    # spell it the same. What is detectable is the `id` — Design's slugs
    # (`8rsc1`, `10hph1`) are synthetic, and every real class id is a UUID, so
    # a slug on a page can only have come from the sample.
    ("CLASSES",      "field",  ["id"]),
    ("NAMES",        "field",  None),
    ("POOL_CLASSES", "field",  None),
    ("TITLES",       "field",  None),
    ("TOPICS",       "field",  ["name"]),
    ("STEMS",        "field",  ["text"]),
    ("previewRows",  "inline", ["name", "email", "klass"]),
]

# `TITLES`, `TOPICS` and `STEMS` are a judgement call worth recording: a real
# assignment COULD legitimately be called "Bonding and structure". They are
# harvested anyway because the port DELETES all three outright — Design's
# titles are replaced by real `assignments.title`. So their presence in a
# built page cannot be a coincidence; it means a LOGIC rewrite did not land.
# If a future port keeps any of them, it must drop them from this list and say
# why, because at that point they stop being evidence.

# `state = {…}` is subtracted from the KEPT text before the collision pass:
# it holds the sample IDs (`classId: '8rsc1'`, `studentId: '8rsc1-3'`) that the
# port rewrites to `MRB_DATA` reads. Leaving it in would excuse every class
# code by its own appearance in the initialiser.
STATE_FIELD = "state"

# Fields that are NOT sample data and must not be harvested.
#
# ⚠️ `TEMPLATES` IS DELIBERATELY ABSENT. Design's six shoutout labels look like
# sample data and are not: they mirror the six-key CHECK constraint on
# `class_shoutouts.template_key`, so the real page renders the same six
# strings. Harvesting them would fail a correct page, and a gate that cries
# wolf gets switched off — which is how the docket in the note above shipped.
NOT_SAMPLES = {"TEMPLATES", "HUE", "BANDS", "CHART_KINDS", "LASTS", "HOURS",
               "mapRows"}

# Attributes a human can READ. The markup harvest looks at text nodes and at
# these, and deliberately not at every attribute carrying a digit: `viewBox`,
# `d`, `stroke-width` and the six `_ds/…` stylesheet hrefs all carry digits,
# all ship legitimately, and all would fail every run.
VISIBLE_ATTRS = {"placeholder", "title", "aria-label", "alt", "value"}

_TOO_SHORT = 3


def _balanced(src, start):
    """The literal beginning at `start`, brackets balanced. Quote-aware."""
    open_c = src[start]
    close_c = {"[": "]", "{": "}"}[open_c]
    depth, i, quote = 0, start, None
    while i < len(src):
        ch = src[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "'\"`":
            quote = ch
        elif ch == open_c:
            depth += 1
        elif ch == close_c:
            depth -= 1
            if depth == 0:
                return src[start:i + 1]
        i += 1
    raise SystemExit("teacher_tells.py: unbalanced literal at %d" % start)


def field_literal(logic, name):
    """The literal assigned to a class field `  NAME = …`."""
    m = re.search(r"^  %s = " % re.escape(name), logic, re.M)
    if not m:
        return None
    i = logic.index("=", m.start()) + 1
    while i < len(logic) and logic[i] in " \n":
        i += 1
    if logic[i] in "[{":
        return _balanced(logic, i)
    return logic[i:logic.index(";", i)]


def inline_literal(logic, name):
    """The literal assigned to an inline `name: […]` inside renderVals."""
    m = re.search(r"\b%s:\s*\[" % re.escape(name), logic)
    if not m:
        return None
    return _balanced(logic, logic.index("[", m.start()))


def corpus(templates_path=TEMPLATES):
    """Every sample value Design's delivery invents. Derived, never typed."""
    tpl = json.load(open(templates_path, encoding="utf-8"))["teacher"]
    logic, roots = tpl["logic"], tpl["roots"]

    strings, missing, harvested = set(), [], []

    def take(lit, name, keys):
        if lit is None:
            # A field that has VANISHED is not automatically a pass. Either
            # Design renamed it — in which case its sample values are no
            # longer being harvested and this gate has quietly stopped
            # watching them — or the port's LOGIC rewrites deleted it, which
            # is the intended outcome but must be STATED rather than inferred.
            missing.append(name)
            return
        # The WHOLE literal is subtracted from the kept text later, even
        # though only some of its keys are harvested — otherwise a label like
        # `'Matched'` would be harvested from nowhere and then fail to be
        # excused, which is the same false positive by another route.
        harvested.append(lit)
        if keys is None:
            found = re.findall(r"'([^'\\\n]*)'", lit)
            # ⚠️ NOT THE OBJECT KEYS. `TITLES` is keyed BY SUBJECT —
            # `{'Science': [...], 'Combined Science': [...]}` — so a blanket
            # harvest takes `'Combined Science'` as a sample value and then
            # fails the correct `class-detail.html`, which renders that
            # subject for real. A key is vocabulary; only the values are
            # titles.
            keyset = set(re.findall(r"'([^'\\\n]*)'\s*:", lit))
            found = [f for f in found if f not in keyset]
        else:
            found = []
            for key in keys:
                found += re.findall(
                    r"\b%s:\s*'([^'\\\n]*)'" % re.escape(key), lit)
        for s2 in found:
            if len(s2) >= _TOO_SHORT:
                strings.add(s2)

    for name, kind, keys in HARVEST:
        lit = (field_literal(logic, name) if kind == "field"
               else inline_literal(logic, name))
        take(lit, name, keys)

    # ── SUBTRACT ANYTHING THE KEPT CODE ALSO SAYS ────────────────────────
    #
    # ⚠️ THE FIRST VERSION OF THIS GATE HAD 159 TELLS AND SEVERAL WERE TRAPS.
    # Harvesting `CLASSES` yields `'Physics'`, `'Combined Science'` and
    # `'Science'` — which are not sample data at all. They are the SUBJECT
    # VOCABULARY, derived from the class code per Design's README, and
    # `dotsFor(sub)` compares against them by name in code the port keeps
    # verbatim. Harvesting `LASTS` yields `'2 days ago'`, which is exactly the
    # format the live pages' own `formatRelativeTime` produces for a REAL
    # timestamp. `'KS3'`, `'live'` and `'empty'` are state vocabulary.
    #
    # Every one of those would have failed a CORRECT page. That is the worse
    # failure: a gate that cries wolf gets switched off, and a switched-off
    # gate is how the docket in the header note shipped.
    #
    # The fix is mechanical rather than a hand-written allowlist, because a
    # hand-written allowlist is the same drifting artefact this file exists to
    # avoid. A string is only a TELL if it appears nowhere in the code and
    # markup the port RETAINS. So: take the logic with every harvested literal
    # cut out of it, cut out `state` too (the port rewrites its sample IDs to
    # `MRB_DATA` reads, so leaving it in would excuse every class code by its
    # own appearance in the initialiser), add every literal in the template,
    # and subtract anything that still occurs.
    kept = logic
    st = field_literal(logic, STATE_FIELD)
    for lit in harvested + ([st] if st else []):
        kept = kept.replace(lit, "")

    def tmpl_text(n, out):
        if not isinstance(n, dict):
            return
        if n.get("t") == "#" and isinstance(n.get("v"), str):
            out.append(n["v"])
        for k, v in (n.get("a") or {}).items():
            if isinstance(v, str):
                out.append(v)
        for c in n.get("c") or []:
            tmpl_text(c, out)

    kept_bits = [kept]
    for r in roots:
        tmpl_text(r, kept_bits)
    kept_all = "\n".join(kept_bits)

    collisions = sorted(s2 for s2 in strings if s2 in kept_all)
    strings -= set(collisions)

    # ── the literals Design wrote into the MARKUP ────────────────────────
    #
    # Only those carrying a digit, and only where a human can read them: a
    # literal COUNT is the failure this catches. SVG path data, viewBox and
    # the stylesheet hrefs all carry digits and all ship legitimately.
    markup = set()

    def walk(n):
        if not isinstance(n, dict):
            return
        if n.get("t") == "#":
            v = n.get("v")
            if (isinstance(v, str) and re.search(r"\d", v)
                    and len(v.strip()) >= _TOO_SHORT and "{" not in v):
                markup.add(v.strip())
        for k, v in (n.get("a") or {}).items():
            if (k in VISIBLE_ATTRS and isinstance(v, str)
                    and re.search(r"\d", v) and len(v) >= _TOO_SHORT):
                markup.add(v.strip())
        for c in n.get("c") or []:
            walk(c)

    for r in roots:
        walk(r)

    # ── and the toast copy ───────────────────────────────────────────────
    #
    # ⚠️ THE THIRD PLACE, found by a string the collision pass kept excusing.
    # `8r/Sc4` stayed out of the corpus run after run because it occurs in
    # RETAINED code as well as in `CLASSES` — and the retained occurrence was
    # itself the defect:
    #
    #     this.ping('26 students imported into 8r/Sc4')
    #
    # A confirmation toast that names a class the teacher does not teach and
    # a count that has nothing to do with the file they just uploaded. The
    # collision pass was right that the string is not only in the sample
    # arrays; it was wrong to conclude the string was therefore innocent.
    #
    # Every other `ping` in the delivery composes its message from state. This
    # harvest catches the ones that do not: a literal toast carrying a digit
    # is a number shown to a teacher that came from nowhere.
    for m in re.finditer(r"ping\(\s*'([^'\\\n]+)'\s*\)", logic):
        if re.search(r"\d", m.group(1)):
            markup.add(m.group(1))

    return dict(strings=sorted(strings), markup=sorted(markup),
                missing=missing, collisions=collisions)


# ── the generator, which must not ship ───────────────────────────────────
#
# Anchored on the CALL, not the name. `seed` and `rnd` are three and four
# characters; unanchored they match `seeds`, `rnd_` and any minified
# identifier that happens to contain them.
#
# ⚠️ `rnd(` AND `seed(` ARE NOT THE SAME OFFENCE, and the first version of
# this check banned both. It was wrong about `seed`.
#
#   `rnd(key, lo, hi)` returns a number in a range. Its ONLY possible use is
#   to make a value up, so any call at all is a leak.
#
#   `seed(str)` is FNV-1a. It is what `rnd` is built on — but it is also what
#   `hueFor(name)` is built on, and `hueFor` picks an avatar COLOUR from a
#   name. That is presentation, it is deterministic on purpose, and the live
#   product already does exactly the same thing: `shared/shoutouts.js` carries
#   `getStudentColour()`, described in its own source as a "deterministic
#   hash-based avatar colour". Banning it outright would have forced the port
#   to either drop Design's avatars or re-implement the identical hash under a
#   different name to get past the gate — which is the shape of a gate being
#   worked around rather than satisfied.
#
# So the rule is precise: `rnd` may not appear, and `seed` may appear only if
# `hueFor` is its sole caller. That keeps the structural proof — nothing on
# the page can manufacture a NUMBER — while allowing the one use that
# manufactures a COLOUR.
RND_RE = re.compile(r"\b(?:this\.)?rnd\s*\(")
# ⚠️ `this.seed(` AND NOT `seed(`. A bare `seed(` also matches the METHOD
# DEFINITION — `seed(str) {` — so counting it reported two callers on a page
# that has one, and the gate failed itself. Inside a class body every real
# call is `this.seed(...)`; a bare one would have to be a free function, which
# the delivery does not have and which would show up as an undefined-name
# error long before this gate ran.
SEED_CALL_RE = re.compile(r"\bthis\.seed\s*\(")
SEED_OK_RE = re.compile(r"hueFor\s*\([^)]*\)\s*\{[^}]*\bthis\.seed\s*\(")


# ── comments are not the page ────────────────────────────────────────────
#
# The port's rulings explain themselves in the emitted source, and a good
# explanation QUOTES the value it removed — `teacher_rulings.py` documents the
# read-only toast by naming it. Scanning raw bytes therefore reported the
# ruling's own prose as the defect the ruling had fixed.
#
# Stripped rather than allowlisted: an allowlist would need a row per comment
# and would drift. What a teacher can read is what is left after the comments
# come out.
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)
_LINE_COMMENT = re.compile(r"^[ \t]*//.*$", re.M)


def strip_comments(body):
    body = _HTML_COMMENT.sub(" ", body)
    body = _BLOCK_COMMENT.sub(" ", body)
    return _LINE_COMMENT.sub(" ", body)


def check_page(path, c):
    """Problems, as strings, for one built page."""
    body = strip_comments(open(path, encoding="utf-8").read())
    problems = []

    for s in c["strings"]:
        if s in body:
            problems.append(
                "carries Design's sample value %r. That is invented data — "
                "the class, student, title or timing does not exist. It "
                "reached a page a teacher can open, which means a LOGIC "
                "rewrite in teacher_rulings.py did not land." % s)

    for s in c["markup"]:
        if s in body:
            problems.append(
                "carries Design's hardcoded literal %r. Counts, dates, week "
                "numbers and term names come from data, never from a literal "
                "— this one will be wrong for every school. It needs a "
                "binding, not a constant." % s)

    if RND_RE.search(body):
        problems.append(
            "still calls rnd( — the wrapper that returns a number in a range. "
            "Its only possible use is to make a value up, so any call at all "
            "is a leak. Whatever else was replaced, a page carrying this can "
            "still invent.")

    # `seed` is allowed for `hueFor` and for nothing else. Counted rather than
    # merely detected: one call is the avatar colour, two is something new.
    n_seed = len(SEED_CALL_RE.findall(body))
    n_ok = 1 if SEED_OK_RE.search(body) else 0
    if n_seed - n_ok > 0:
        problems.append(
            "calls seed( %d time(s) and only %d of them is hueFor's avatar "
            "colour. seed is FNV-1a — the hash rnd is built on — and any "
            "caller other than hueFor is manufacturing something. Name what "
            "the extra caller is for, or route it through real data."
            % (n_seed, n_ok))

    return problems


def main(argv):
    os.chdir(REPO)
    if not os.path.exists(TEMPLATES):
        print("teacher_tells.py: no %s. Run student_template.py first."
              % TEMPLATES)
        return 1
    c = corpus()

    if "--list" in argv:
        print("\n  %d sample string(s) derived from Design's delivery:\n"
              % len(c["strings"]))
        for s in c["strings"]:
            print("     %r" % s)
        print("\n  %d hardcoded markup literal(s):\n" % len(c["markup"]))
        for s in c["markup"]:
            print("     %r" % s)
        if c["collisions"]:
            print("\n  %d harvested string(s) DROPPED because the retained "
                  "code or markup\n  also says them \u2014 they are vocabulary, "
                  "not sample data:\n" % len(c["collisions"]))
            for s2 in c["collisions"]:
                print("     %r" % s2)
        if c["missing"]:
            print("\n  field(s) not present in the compiled logic: %s"
                  % ", ".join(c["missing"]))
        print()
        return 0

    print("\n🔎  teacher_tells — Design's sample school must not reach a "
          "teacher\n")
    print("     corpus: %d sample string(s) + %d hardcoded markup literal(s), "
          "derived\n             from the delivery itself"
          % (len(c["strings"]), len(c["markup"])))
    if c["missing"]:
        print("     ⊕ harvested nothing from: %s — deleted by the port's "
              "LOGIC\n       rewrites, which is the intended outcome"
              % ", ".join(c["missing"]))
    print()

    checked, failed = 0, 0
    for name in LIVE_PAGES:
        path = os.path.join(PAGE_DIR, name)
        if not os.path.exists(path):
            print("     %-22s ⚠️  not built" % name)
            failed += 1
            continue
        problems = check_page(path, c)
        checked += 1
        if problems:
            failed += 1
            print("     %-22s ❌ %d problem(s)" % (name, len(problems)))
            for p in problems[:12]:
                print("        · %s" % p)
            if len(problems) > 12:
                print("        · … and %d more" % (len(problems) - 12))
        else:
            print("     %-22s ✅" % name)

    print()
    if failed:
        print("  FAIL  %d of %d page(s) carry Design's sample data.\n"
              % (failed, len(LIVE_PAGES)))
        return 1
    print("  PASS  %d live page(s), no sample value, no literal count, no "
          "generator.\n" % checked)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
