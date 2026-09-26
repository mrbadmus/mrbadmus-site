#!/usr/bin/env python3
"""ks4_lessons/blocks.py — the closed block-type registry (pilot-build-contract.md §1).

Two separate vocabularies, both closed:

  SECTION_TYPES  — what a lesson's own `<section>` (or a handful of
                   non-`<section>` content blocks Design used instead, like
                   the `<div data-key-fact>` card) IS. 14 inherited from KS3
                   + 4 new to KS4. `classify_section()` maps a compiled
                   template node to exactly one of these, and stamps it onto
                   the page as `data-block="…"`.

  COMPONENTS     — the 11 shared `.dc.html` blocks a lesson may `<dc-import
                   name="…">`. Closed because an unregistered import name is
                   almost always a typo or a Design delivery this build has
                   not been told about, and either way the right move is to
                   stop, not to silently mount nothing.

`classify_section()` is a HEURISTIC over id/class/eyebrow text — good enough
for the common shapes (hook, misconception, explainer, the fixed exam-tip
slot, key-fact, the 4 KS4-specific panels) but not psychic about a lesson's
bespoke content (L10's diamond/graphite comparison, L14's required-practical
panel). Where it cannot decide, it raises `SystemExit` naming the lesson and
the section's id/index — UNLESS `ks4_lessons.LESSONS[…]["block_map"]` already
answers for that id/index, in which case the override wins outright (no
heuristic runs at all for a mapped section). `build_ks4.py` builds every
lesson's `block_map` up front from the real compiled output, precisely
because a heuristic guessing at bespoke content is the wrong tool for it.
"""

# ── the 14 KS3 section types (docs/ks3/architecture.md's vocabulary) + 4 new ─
SECTION_TYPES = frozenset([
    # inherited from KS3
    "hook", "explainer", "figure", "worked-example", "check", "keyword",
    "practical", "misconception", "summary", "quiz", "key-fact", "rule",
    "formula", "comparison",
    # new at KS4 (pilot-build-contract.md §1)
    "required-practical", "equation", "extended-response", "exam-tip",
])

# ── the 11 shared block components a lesson may <dc-import> ───────────────
COMPONENTS = frozenset([
    "Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write", "Ks4Cfifa",
    "Ks4Ladder", "Ks4KeyNote", "Ks4QuizBank", "Ks4End", "Ks4Video",
])

# A section that is essentially a one-component wrapper takes that
# component's nearest SECTION_TYPES meaning. Ks4Chrome/Ks4Video/Ks4End are
# never wrapped in a lesson-authored <section> (they sit directly in
# `.ks3-lesson`), so they are not here — classify_section() never needs them.
IMPORT_TO_TYPE = {
    "Ks4Sort": "check",
    "Ks4Chain": "check",
    "Ks4Cfifa": "worked-example",
    "Ks4QuizBank": "quiz",
    "Ks4KeyNote": "summary",
    "Ks4Ladder": "check",
    "Ks4Write": "extended-response",
    # Ks4Choice alone means very little — it is the hook AND the
    # spot-the-flaw AND mid-lesson commit points. Never used as the sole
    # signal; see the id/class rules below, which run first.
}


def _class_of(node):
    a = (node.get("a") or {})
    cls = a.get("class")
    if cls is None:
        return ""
    if isinstance(cls, str):
        return cls
    # compiled attrs are either a bare string or {"parts": [...]}; a class
    # attribute is never interpolated on any pilot page, but stay defensive.
    if isinstance(cls, dict) and cls.get("parts"):
        return "".join(p for p in cls["parts"] if isinstance(p, str))
    return ""


def _id_of(node):
    a = (node.get("a") or {})
    v = a.get("id")
    if isinstance(v, str):
        return v
    return ""


def _text_of(node, limit=400):
    """First `limit` chars of a subtree's literal text, for eyebrow/heading
    sniffing. Interpolations (`{{ }}`) contribute nothing — the eyebrows this
    checks against are all literal strings in the pilot's markup."""
    out = []

    def walk(n):
        if len(" ".join(out)) > limit:
            return
        if n.get("t") == "#":
            v = n.get("v")
            if isinstance(v, str):
                out.append(v)
        for c in n.get("c") or []:
            walk(c)

    walk(node)
    return " ".join(out)


def _imports_in(node):
    """Every `dc-import` component name anywhere inside this subtree."""
    out = []

    def walk(n):
        if n.get("t") == "child":
            out.append(n.get("comp"))
        for c in n.get("c") or []:
            walk(c)

    walk(node)
    return out


def classify_section(node, lesson_slug, index, block_map):
    """Classify one top-level content node from a lesson's `.ks3-lesson`
    body. `index` is this node's 0-based position among ITS SIBLINGS at that
    level (stable across a build, used as the `block_map` key when the node
    has no `id`). Returns a SECTION_TYPES member, or raises `SystemExit`.
    """
    node_id = _id_of(node)
    key = node_id or str(index)
    if key in block_map:
        forced = block_map[key]
        if forced not in SECTION_TYPES:
            raise SystemExit(
                "ks4_lessons.blocks: %s block_map[%r] = %r is not a "
                "registered section type. Registered: %s"
                % (lesson_slug, key, forced, sorted(SECTION_TYPES)))
        return forced

    cls = _class_of(node)
    a = node.get("a") or {}
    text = _text_of(node)
    imports = _imports_in(node)

    # 1. the one non-<section> content block: the key-fact card.
    if "data-key-fact" in a:
        return "key-fact"

    # 2. id/class signals — these are Design's own naming and are the most
    #    reliable evidence, checked before any dc-import inference.
    if node_id.startswith("s-hook") or "ks3-hook" in cls:
        return "hook"
    if "ks3-misconception" in cls:
        return "misconception"
    if "ks3-explainer" in cls:
        return "explainer"
    if node_id.startswith("s-equation") or "Equations" in text[:40]:
        return "equation"
    if node_id.startswith("s-keynote"):
        return "summary"
    if node_id.startswith("s-ladder"):
        return "check"
    if "Examiner tip" in text[:60]:
        return "exam-tip"
    if "Required practical" in text[:80] or "required-practical" in cls:
        return "required-practical"
    if "Command words in this lesson" in text[:80]:
        return "keyword"

    # 3. a section that is essentially one component's wrapper.
    single_imports = set(imports)
    if len(single_imports) == 1:
        only = next(iter(single_imports))
        if only in IMPORT_TO_TYPE:
            return IMPORT_TO_TYPE[only]

    # 4. a bare figure card: no import, no eyebrow text beyond a caption,
    #    just an SVG-bearing div (a `{{ …Fig }}`/`{{ …fig }}`-named binding).
    if not imports and _has_fig_binding(node):
        return "figure"

    raise SystemExit(
        "ks4_lessons.blocks.classify_section: cannot infer a type for "
        "%s section %r (index %d, class=%r, imports=%r, text=%r…).\n"
        "  Add an entry to this lesson's block_map in ks4_lessons/__init__.py:"
        " block_map={%r: '<one of %s>'}"
        % (lesson_slug, node_id or "(no id)", index, cls, imports, text[:80],
           key, sorted(SECTION_TYPES)))


def _has_fig_binding(node):
    """True if this subtree contains a `{{ xFig }}`/`{{ xfig }}`-shaped
    single-expression interpolation — Design's naming convention for a
    `KS4.fig(...)`-produced figure marker (see shared/ks4-runtime.js)."""
    found = [False]

    def walk(n):
        if found[0]:
            return
        if n.get("t") == "#":
            v = n.get("v")
            if isinstance(v, dict) and v.get("parts") and len(v["parts"]) == 1:
                part = v["parts"][0]
                if isinstance(part, dict):
                    e = (part.get("e") or "").strip().lower()
                    if e.endswith("fig"):
                        found[0] = True
                        return
        for c in n.get("c") or []:
            walk(c)

    walk(node)
    return found[0]
