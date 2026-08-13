#!/usr/bin/env python3
"""3D Studio — build-time content validation (spec v1 §3.2 and §10, MRB-185).

Run it:

    python3 3d-studio/validate_content.py

Standalone by design — stdlib only, runnable before any app exists. When the
Vite app lands this becomes a build gate (a failing record must fail the
build); until then it is the Stage 0 harness.

It iterates every specimen record in 3d-studio/content/ and asserts:

  1. every declared field is present and non-empty
  2. every referenced asset file exists on disk
     (source of truth: 3d-studio/public/, where /3d/<p> maps to public/<p>)
  3. every lessonUrl resolves to a real file under mrbadmus_site/
  4. every hotspot has both position3d ([x,y,z]) and position2d ([x,y])
  5. sidebar label, stage caption and panel heading derive from one field:
     the record carries exactly `name` and no alias key anywhere at top level
     (unknown keys are failures — the three-independent-lookups defect is
     designed against by making a second name field impossible to add)

Plus the binding naming rule: the word "organ" must not appear in any content
filename or in any key at any depth.

Placeholder convention (Stage 8 checklist): a string value beginning with
"TODO" passes the presence check but is COUNTED and listed separately, and its
semantic check is deferred — a TODO lessonUrl is not resolved, and while
assets.acquired is a TODO the missing asset files are reported as "pending
acquisition" rather than failing. A hotspot position of all zeros likewise
passes presence but is listed as not yet authored. The two optional
per-hotspot fields added by MRB-193 are listed the same way: a hotspot with no
'accept' array grades on its label alone until Mide authors the alternatives,
and a hotspot with no 'specPoints' inherits the specimen's — both are legal,
both are on the checklist. Everything on that list must be cleared, and
science-gated text signed off by Mide, before Stage 8 closes.

Exit code 0 = every record valid. Exit code 1 = at least one failure.
"""

import json
import os
import sys

STUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(STUDIO_DIR)
CONTENT_DIR = os.path.join(STUDIO_DIR, "content")
PUBLIC_DIR = os.path.join(STUDIO_DIR, "public")
SITE_DIR = os.path.join(REPO_ROOT, "mrbadmus_site")

TOP_LEVEL_KEYS = [
    "id", "renderer", "name", "epithet", "system", "keyStages", "assets",
    "description", "keyFacts", "callouts", "lessonUrl", "specPoints",
    "hotspots",
]
ASSET_KEYS = ["mesh", "fallback", "thumbnail", "licence", "source", "acquired"]
CALLOUT_KEYS = ["importance", "didYouKnow"]
HOTSPOT_KEYS = ["id", "label", "detail", "position3d", "position2d", "tiers",
                "retrievable"]
# Optional per-hotspot fields (MRB-193). Allowed by the unknown-field check but
# NOT required — they are deliberately kept out of HOTSPOT_KEYS, which doubles
# as the required-presence list.
HOTSPOT_OPTIONAL_KEYS = ["specPoints", "accept"]
# Aliases that would reintroduce independent name lookups. Their absence is
# already implied by the unknown-key check; naming them keeps the failure
# message specific when someone tries.
NAME_ALIASES = {"sidebarLabel", "stageCaption", "panelHeading", "caption",
                "heading", "displayName", "title"}
FORBIDDEN_KEY_SUBSTRING = "organ"


def is_placeholder(value):
    return isinstance(value, str) and value.startswith("TODO")


def non_empty(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return value is not None


def walk_keys(node, path=""):
    """Yield (dotted_path, key) for every dict key at every depth."""
    if isinstance(node, dict):
        for k, v in node.items():
            here = f"{path}.{k}" if path else k
            yield here, k
            yield from walk_keys(v, here)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_keys(v, f"{path}[{i}]")


def walk_strings(node, path=""):
    """Yield (dotted_path, value) for every string value at every depth."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def served_path_to_source(served):
    """Map a served asset path (/3d/assets/x) to its source file under
    3d-studio/public/ (Vite serves public/ at the app base, which is /3d/)."""
    if not served.startswith("/3d/"):
        return None
    return os.path.join(PUBLIC_DIR, served[len("/3d/"):])


def require(record, keys, ctx, fail):
    """Presence + non-emptiness for a fixed key set; returns present keys."""
    present = []
    for k in keys:
        if k not in record:
            fail(f"{ctx}: missing field '{k}'")
        elif not non_empty(record[k]):
            fail(f"{ctx}: field '{k}' is empty")
        else:
            present.append(k)
    return present


def validate_record(fname, record, failures, placeholders):
    ctx = fname

    def fail(msg):
        failures.append(msg)

    if not isinstance(record, dict):
        fail(f"{ctx}: record is not a JSON object")
        return

    # ── naming discipline: no forbidden key at any depth, nor in the filename
    if FORBIDDEN_KEY_SUBSTRING in fname.lower():
        fail(f"{ctx}: filename contains '{FORBIDDEN_KEY_SUBSTRING}' — naming "
             f"discipline is specimen/item")
    for keypath, key in walk_keys(record):
        if FORBIDDEN_KEY_SUBSTRING in key.lower():
            fail(f"{ctx}: key '{keypath}' contains "
                 f"'{FORBIDDEN_KEY_SUBSTRING}' — naming discipline is "
                 f"specimen/item")

    # ── gate 5: one name field, no aliases, no unknown top-level keys
    for k in record:
        if k in NAME_ALIASES:
            fail(f"{ctx}: alias field '{k}' — sidebar label, stage caption "
                 f"and panel heading must all derive from 'name'")
        elif k not in TOP_LEVEL_KEYS:
            fail(f"{ctx}: unknown top-level field '{k}'")

    # ── gate 1: every declared field present and non-empty
    require(record, TOP_LEVEL_KEYS, ctx, fail)

    if isinstance(record.get("assets"), dict):
        require(record["assets"], ASSET_KEYS, f"{ctx}: assets", fail)
    if isinstance(record.get("callouts"), dict):
        require(record["callouts"], CALLOUT_KEYS, f"{ctx}: callouts", fail)
    for i, kf in enumerate(record.get("keyFacts") or []):
        if isinstance(kf, dict):
            require(kf, ["label", "value"], f"{ctx}: keyFacts[{i}]", fail)
        else:
            fail(f"{ctx}: keyFacts[{i}] is not an object")

    # expected id ↔ filename agreement (one source of record)
    expected_id = os.path.splitext(fname)[0]
    if record.get("id") and record["id"] != expected_id:
        fail(f"{ctx}: id '{record['id']}' does not match filename "
             f"'{expected_id}'")

    # ── gate 2: referenced asset files exist on disk
    assets = record.get("assets") or {}
    acquired_pending = is_placeholder(assets.get("acquired", ""))
    for k in ("mesh", "fallback", "thumbnail"):
        served = assets.get(k)
        if not isinstance(served, str) or not served:
            continue  # absence already failed gate 1
        if is_placeholder(served):
            continue  # counted by the placeholder sweep below
        src = served_path_to_source(served)
        if src is None:
            fail(f"{ctx}: assets.{k} '{served}' is not under /3d/")
        elif not os.path.isfile(src):
            if acquired_pending:
                placeholders.append(
                    f"{ctx}: assets.{k} → {served} (pending acquisition — "
                    f"file not on disk yet, enforced once assets.acquired is "
                    f"a real date)")
            else:
                fail(f"{ctx}: assets.{k} '{served}' does not exist at {src}")

    # ── gate 3: lessonUrl resolves to a real generated page
    lesson = record.get("lessonUrl")
    if isinstance(lesson, str) and lesson and not is_placeholder(lesson):
        target = os.path.join(SITE_DIR, lesson.lstrip("/"))
        if not os.path.isfile(target):
            fail(f"{ctx}: lessonUrl '{lesson}' does not resolve to a file "
                 f"under mrbadmus_site/")

    # ── gate 4: every hotspot carries both coordinate systems
    for i, h in enumerate(record.get("hotspots") or []):
        hctx = f"{ctx}: hotspots[{i}]"
        if not isinstance(h, dict):
            fail(f"{hctx} is not an object")
            continue
        for k in h:
            if k not in HOTSPOT_KEYS and k not in HOTSPOT_OPTIONAL_KEYS:
                fail(f"{hctx}: unknown field '{k}'")
        for k in HOTSPOT_KEYS:
            if k == "retrievable":
                if not isinstance(h.get(k), bool):
                    fail(f"{hctx}: 'retrievable' must be true or false")
                continue
            if k not in h:
                fail(f"{hctx}: missing field '{k}'")
            elif not non_empty(h[k]):
                fail(f"{hctx}: field '{k}' is empty")
        p3, p2 = h.get("position3d"), h.get("position2d")
        if not (isinstance(p3, list) and len(p3) == 3
                and all(isinstance(v, (int, float)) for v in p3)):
            fail(f"{hctx}: position3d must be [x, y, z] numbers")
        elif p3 == [0, 0, 0]:
            placeholders.append(f"{hctx}: position3d not yet authored "
                                f"(all-zero)")
        if not (isinstance(p2, list) and len(p2) == 2
                and all(isinstance(v, (int, float)) for v in p2)):
            fail(f"{hctx}: position2d must be [x, y] numbers")
        elif p2 == [0, 0]:
            placeholders.append(f"{hctx}: position2d not yet authored "
                                f"(all-zero)")
        tiers = h.get("tiers")
        if isinstance(tiers, list) and not all(
                t in ("foundation", "higher") for t in tiers):
            fail(f"{hctx}: tiers must contain only 'foundation'/'higher'")

        # ── the two optional fields (MRB-193): absent is legal, and listed.
        # A field that is PRESENT but holds a TODO string is not listed here —
        # the walk_strings sweep below already catches it, and counting it
        # twice would overstate the checklist.
        if "accept" not in h:
            placeholders.append(f"{hctx}: accept not yet authored "
                                f"(exact-match on the label only until Mide "
                                f"authors alternatives)")
        elif not (isinstance(h["accept"], list) and h["accept"] and all(
                isinstance(a, str) and a.strip() for a in h["accept"])):
            fail(f"{hctx}: accept must be a non-empty list of authored "
                 f"alternatives")
        if "specPoints" not in h:
            placeholders.append(f"{hctx}: specPoints not declared — inherits "
                                f"the specimen's")
        elif not (isinstance(h["specPoints"], list) and h["specPoints"] and all(
                isinstance(sp, str) and sp.strip() for sp in h["specPoints"])):
            fail(f"{hctx}: specPoints must be a non-empty list of statement "
                 f"IDs")

    # ── Stage 8 checklist: every TODO string, wherever it sits
    for path, value in walk_strings(record):
        if is_placeholder(value):
            placeholders.append(f"{ctx}: {path} = {value!r}")


def main():
    if not os.path.isdir(CONTENT_DIR):
        print(f"❌ content directory not found: {CONTENT_DIR}")
        return 1

    files = sorted(f for f in os.listdir(CONTENT_DIR)
                   if f.endswith(".json") and not f.endswith(".schema.json"))
    if not files:
        print(f"❌ no specimen records in {CONTENT_DIR}")
        return 1

    failures, placeholders = [], []
    for fname in files:
        path = os.path.join(CONTENT_DIR, fname)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                record = json.load(fh)
        except json.JSONDecodeError as e:
            failures.append(f"{fname}: invalid JSON — {e}")
            continue
        validate_record(fname, record, failures, placeholders)

    print(f"3D Studio content validation — {len(files)} specimen record(s): "
          f"{', '.join(files)}\n")

    if failures:
        print(f"❌ {len(failures)} failure(s):")
        for f in failures:
            print(f"   ✗ {f}")
    else:
        print("✅ all records valid — presence, assets, lesson URLs, hotspot "
              "parity, single-name binding, naming discipline")

    if placeholders:
        print(f"\n📋 Stage 8 checklist — {len(placeholders)} item(s) still "
              f"placeholder (pass now, must clear before Stage 8):")
        for p in placeholders:
            print(f"   • {p}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
