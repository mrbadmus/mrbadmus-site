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

Optional 'keyStages' is the exception, and deliberately so. It is NOT on the
checklist when absent: a hotspot without it inherits the specimen's key stages,
which is the finished, correct answer for the great majority of structures.
Listing every one of them would be asking Mide to clear an item that has
nothing wrong with it. Where the field IS present its values are checked.

'cutMaterial' (MRB-217) and 'appearance' (MRB-218) are exceptions on exactly
the same terms and for the same reason. Both resolve hotspot → specimen →
renderer fallback, so absence is an inherit rather than an unauthored blank,
and neither produces a checklist line. The heart's septum and sino-atrial node
declare no 'appearance' at all: they have no part in the GLB and are anchored
by coordinate alone, so there is no surface of theirs to paint. Where either
field IS present its value is checked against its enum.

Exit code 0 = every record valid. Exit code 1 = at least one failure.
"""

import json
import os
import sys

STUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(STUDIO_DIR)
# MRB_CONTENT_DIR points the record sweep somewhere else. A TEST SEAM, and the
# only reason it exists: gate 4 proves the validator REJECTS a bad value by
# handing it a copy of content/ with one planted in, and a validator nobody has
# watched reject something is a spell-check that is switched off. Everything
# else — public/assets, mrbadmus_site — still resolves from the repo, so the
# copy is validated against the real world rather than against a stub.
CONTENT_DIR = os.environ.get("MRB_CONTENT_DIR") or os.path.join(STUDIO_DIR, "content")
PUBLIC_DIR = os.path.join(STUDIO_DIR, "public")
SITE_DIR = os.path.join(REPO_ROOT, "mrbadmus_site")

TOP_LEVEL_KEYS = [
    "id", "renderer", "name", "epithet", "system", "keyStages", "assets",
    "description", "keyFacts", "callouts", "lessonUrl", "specPoints",
    "hotspots",
]
# Optional top-level fields. Kept OUT of TOP_LEVEL_KEYS deliberately, which
# doubles as the required-presence list — the same split HOTSPOT_OPTIONAL_KEYS
# makes for the same reason.
TOP_LEVEL_OPTIONAL_KEYS = ["cutMaterial", "appearance", "structuralParts"]
ASSET_KEYS = ["mesh", "fallback", "thumbnail", "licence", "source", "acquired"]

# Which file extension each asset is served as. Used to ask the same question
# vite.config.ts asks — is an acquired file of this kind on disk — so the
# record and the build agree about what has actually been acquired.
ASSET_EXTENSIONS = {"mesh": ".glb", "fallback": ".svg", "thumbnail": ".webp"}


def slugify(name):
    """"Right atrium" → "right-atrium". The one reduction that binds a GLB's
    part names to the record's hotspot ids. Mirrored in
    tools/derive_anchors.py, which resolves anchors across the same join."""
    out = []
    for ch in name.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    return "".join(out).strip("-")


def glb_part_names(path):
    """Every named node with a mesh, straight out of a GLB's JSON chunk.

    Stdlib only and no geometry decoding: the names live in the JSON chunk, so
    this reads them without numpy or DracoPy and keeps this validator runnable
    on a machine with nothing installed."""
    import struct

    with open(path, "rb") as fh:
        header = fh.read(12)
        if len(header) < 12 or header[:4] != b"glTF":
            raise ValueError("not a GLB")
        chunk_header = fh.read(8)
        if len(chunk_header) < 8:
            raise ValueError("truncated GLB")
        length, kind = struct.unpack("<II", chunk_header)
        if kind != 0x4E4F534A:
            raise ValueError("first chunk is not JSON")
        gltf = json.loads(fh.read(length).decode("utf-8"))
    return [node["name"] for node in gltf.get("nodes", [])
            if "mesh" in node and node.get("name")]


def acquired_asset(extension):
    """The first acquired file of that kind in public/assets, or None.
    Underscore-prefixed files are generated test fixtures and do not count —
    the same rule vite.config.ts's standInFor() applies."""
    directory = os.path.join(PUBLIC_DIR, "assets")
    if not os.path.isdir(directory):
        return None
    for name in sorted(os.listdir(directory)):
        if name.endswith(extension) and not name.startswith("_"):
            return name
    return None
CALLOUT_KEYS = ["importance", "didYouKnow"]
HOTSPOT_KEYS = ["id", "label", "detail", "position3d", "position2d", "tiers",
                "retrievable"]
# Optional per-hotspot fields (MRB-193). Allowed by the unknown-field check but
# NOT required — they are deliberately kept out of HOTSPOT_KEYS, which doubles
# as the required-presence list.
HOTSPOT_OPTIONAL_KEYS = ["specPoints", "accept", "keyStages", "cutMaterial",
                         "appearance"]
# What a cut face may be made of (MRB-217). Optional at BOTH levels — hotspot
# first, then the specimen's, then the renderer's depth heuristic — so absence
# is an inherit exactly as keyStages' is, and produces no placeholder line.
CUT_MATERIALS = ("wall", "cavity")
# What an OUTER SURFACE may be (MRB-218). Optional at BOTH levels on exactly
# the same terms, so absence is an inherit and produces no placeholder line.
#
# These are SEMANTIC TOKENS, not colours. The renderer owns the mapping from
# token to colour and finish, which is what lets two palettes — 'realistic'
# (the default) and 'schematic' (the AQA diagram convention) — stand over one
# identical record. A SEVENTH token is a RULING, not an edit here: every palette
# must cover every token, and the renderer's gate asserts that both do.
#
# 'muscle' is the sixth, ruled by Mide for MRB-222 and added with the geometry
# that needed it — before the ventricular myocardium was assembled from
# BodyParts3D's isa tree there was no muscle on the heart to paint, only
# blood-volume casts of the chambers.
APPEARANCES = ("blood-oxygenated", "blood-deoxygenated", "vessel-oxygenated",
               "vessel-deoxygenated", "valve", "muscle")
KEY_STAGES = ("KS3", "KS4")
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
        elif k not in TOP_LEVEL_KEYS and k not in TOP_LEVEL_OPTIONAL_KEYS:
            fail(f"{ctx}: unknown top-level field '{k}'")

    # ── gate 5b: the specimen-wide cut material, where one is declared
    if "cutMaterial" in record and record["cutMaterial"] not in CUT_MATERIALS:
        fail(f"{ctx}: cutMaterial {record['cutMaterial']!r} is not one of "
             f"{list(CUT_MATERIALS)} — the cut face is wall or cavity, and a "
             f"third value would have no colour to be drawn in")

    # ── gate 5c: the specimen-wide outer surface, where one is declared
    if "appearance" in record and record["appearance"] not in APPEARANCES:
        fail(f"{ctx}: appearance {record['appearance']!r} is not one of "
             f"{list(APPEARANCES)} — a sixth token is a ruling, not an edit, "
             f"because every palette must cover every token and an unlisted "
             f"one would have no colour in either palette")

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
    #
    # The three assets are acquired SEPARATELY. The heart's mesh landed on
    # 2026-08-13 while its 2D plate and thumbnail had not been drawn, so a
    # single `acquired` date cannot speak for all three: read as "everything
    # arrived" it demands files nobody has made, and read as "nothing has"
    # it stops enforcing the one that did. Each asset therefore answers for
    # itself — a real path must exist on disk, a TODO path is pending — and
    # `acquired` keeps the old bundled behaviour only while it is itself a
    # TODO, which is the pre-acquisition state it was written for.
    #
    # The inverse matters just as much. vite.config.ts substitutes a generated
    # stand-in only while NO acquired file of that kind is on disk, so a record
    # still saying TODO after one lands would send the renderer to fetch the
    # literal string "TODO: …". Both directions are checked, against the same
    # test the build makes, so the record and the build cannot disagree.
    assets = record.get("assets") or {}
    acquired_pending = is_placeholder(assets.get("acquired", ""))
    for k in ("mesh", "fallback", "thumbnail"):
        served = assets.get(k)
        if not isinstance(served, str) or not served:
            continue  # absence already failed gate 1
        if is_placeholder(served):
            on_disk = acquired_asset(ASSET_EXTENSIONS[k])
            if on_disk:
                fail(f"{ctx}: assets.{k} is still a placeholder, but "
                     f"{on_disk} is on disk — the build has stopped "
                     f"substituting a stand-in, so the record must name the "
                     f"acquired file")
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

    # ── gate 2b: the mesh's named parts bind to hotspots
    #
    # The pipeline already proves a GLB kept its part names through decimation
    # (specimen_pipeline.mjs, namesPreserved) — that catches a flattened
    # export. It cannot catch the other half: names that survived intact but
    # name nothing the record knows about. The isolate tool shows a part's name
    # to the class verbatim ("Isolated: Right atrium"), so a part the record
    # cannot account for is a structure a student can select and the panel has
    # nothing to say about.
    #
    # Binding is by slug, because the two are written for different readers: a
    # part is named for the class, a hotspot id is written for code.
    #
    # The reverse is NOT an error. A hotspot may legitimately have no part of
    # its own and be anchored by coordinate alone — the heart's septum and
    # sino-atrial node are, because BodyParts3D models neither as separately
    # addressable geometry. Those are listed, not failed, so the split between
    # "has a part" and "coordinates only" stays visible rather than silently
    # becoming whatever the last acquisition happened to contain.
    mesh = assets.get("mesh")
    if isinstance(mesh, str) and mesh and not is_placeholder(mesh):
        mesh_src = served_path_to_source(mesh)
        if mesh_src and os.path.isfile(mesh_src):
            try:
                part_names = glb_part_names(mesh_src)
            except (OSError, ValueError) as error:
                fail(f"{ctx}: cannot read part names from {mesh}: {error}")
                part_names = []
            ids = {h.get("id") for h in record.get("hotspots") or []
                   if isinstance(h, dict)}
            prefix = record.get("id", "")
            # A part may be declared STRUCTURAL: geometry the specimen needs in
            # order to be the right shape, which the record does not (yet) name
            # as a teaching structure. MRB-222 forced this — the heart's
            # ventricular myocardium and its two atrial walls are real parts
            # carrying the wall-thickness comparison, and writing a hotspot for
            # them means writing student-facing prose, which is authored
            # anatomy under the science gate rather than a build step.
            #
            # This does NOT bless the gap, and the gate above keeps all its
            # force against an ACCIDENTALLY unnamed part. A structural part
            # must be named here on purpose, it must actually exist in the mesh
            # (so the list cannot rot into a blanket exemption), and every one
            # of them is booked into the Stage 8 checklist below — because the
            # defect this gate guards against is real for them too: the isolate
            # tool will show the part's name to a class and the panel has
            # nothing to say. Tracked, not waived.
            structural = record.get("structuralParts") or []
            if not isinstance(structural, list):
                fail(f"{ctx}: structuralParts must be a list of part names")
                structural = []
            declared = {n for n in structural if isinstance(n, str)}
            for name in sorted(declared - set(part_names)):
                fail(f"{ctx}: structuralParts names {name!r}, which the mesh "
                     f"does not declare as a part — remove it, or fix the "
                     f"spelling to match the GLB exactly")
            for name in part_names:
                if name in declared:
                    placeholders.append(
                        f"{ctx}: part {name!r} is declared structural and has "
                        f"no hotspot — a class can isolate it and the panel "
                        f"has nothing to say; needs authored content")
                elif f"{prefix}.{slugify(name)}" not in ids:
                    fail(f"{ctx}: the mesh declares a part {name!r} that no "
                         f"hotspot claims — expected a hotspot with id "
                         f"'{prefix}.{slugify(name)}', or declare it in "
                         f"structuralParts if it carries no teaching content")
            bound = {f"{prefix}.{slugify(n)}" for n in part_names}
            for hotspot_id in sorted(ids - bound):
                placeholders.append(
                    f"{ctx}: {hotspot_id} has no mesh part — anchored by "
                    f"coordinate alone")

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
        if "cutMaterial" in h and h["cutMaterial"] not in CUT_MATERIALS:
            fail(f"{hctx}: cutMaterial {h['cutMaterial']!r} is not one of "
                 f"{list(CUT_MATERIALS)} — the cut face is wall or cavity, and "
                 f"a third value would have no colour to be drawn in")
        if "appearance" in h and h["appearance"] not in APPEARANCES:
            fail(f"{hctx}: appearance {h['appearance']!r} is not one of "
                 f"{list(APPEARANCES)} — a sixth token is a ruling, not an "
                 f"edit, because every palette must cover every token and an "
                 f"unlisted one would have no colour in either palette")
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

        # ── optional keyStages: absence is an INHERIT, not a placeholder.
        # Unlike specPoints above it produces no checklist line — a structure
        # taught at every key stage its specimen is offered at is finished
        # content, and putting it on Mide's Stage 8 list would be asking him to
        # clear an item with nothing wrong with it. Only a declared-but-broken
        # value is a failure.
        if "keyStages" in h and not (
                isinstance(h["keyStages"], list) and h["keyStages"]
                and all(ks in KEY_STAGES for ks in h["keyStages"])
                and len(set(h["keyStages"])) == len(h["keyStages"])):
            fail(f"{hctx}: keyStages must be a non-empty list of unique "
                 f"'KS3'/'KS4' values")

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
