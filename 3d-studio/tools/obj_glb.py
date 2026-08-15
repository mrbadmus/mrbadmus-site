#!/usr/bin/env python3
"""3D Studio — read Wavefront .obj, write multi-part GLB.

Why this exists
---------------
prepare_specimen.py's non-glTF branch needs Blender, which is not installed.
For .obj that requirement was never real: .obj is a plain text list of vertices
and faces, and the GLB writer below is the one already proven in
tools/make_test_specimen.py. Reading one and emitting the other is a hundred
lines of stdlib, so .obj now converts here and hands the result to the same
Node worker every other format goes through. Blender remains the route for
.blend/.fbx/.dae/.stl/.ply, which are binary or need a real scene graph.

This module is a library plus a small CLI. prepare_specimen.py imports it;
nothing here knows about specimens, gates or the studio.

Two shapes of input
-------------------
ONE .obj                  → parts come from its own `o` / `g` statements, or
                            the file becomes a single part named after itself.

AN ASSEMBLY RECIPE (.json) → many .obj files composed into one specimen, each
                            named part listing the source files that make it.
                            This is what an anatomical source needs: the meshes
                            arrive one-structure-per-file, and a specimen is a
                            named selection of them. See RECIPE below.

Recipe format — "specimen-assembly/v1"
--------------------------------------
    {
      "recipe": "specimen-assembly/v1",
      "name": "heart",
      "source": { ...free-form provenance, copied into the report... },
      "transform": {
         "axes": "LPS-to-glTF",     # or "none"
         "recentre": "bounds",      # or "none"
         "scaleTo": 1.0             # longest bounding-box edge becomes this
      },
      "parts": [
        { "name": "right-atrium", "files": ["FJ2424", "FJ2439"] },
        { "name": "ventricular-myocardium", "files": ["FJ2428.clean100"],
          "tree": "isa", "preserve": true },
        ...
      ]
    }

`files` are resolved against --obj-dir, with `.obj` appended when absent. A
part may name several files: they are concatenated into one mesh under one
node, which is what "the right atrium" means when the source ships its wall
and its cavity as separate meshes.

`tree` (optional) names WHICH source directory a part's files come from, for a
specimen assembled from more than one release of the same database. Directories
are supplied as `--obj-dir name=path`, and a part with no `tree` takes the
unnamed `--obj-dir`. MRB-222 is why this exists: BodyParts3D ships a partof and
an isa tree, and the heart's ventricular myocardium is present only in the isa
one. The two trees share element ids AND coordinate frame — all 1,258 elements
common to both are byte-identical below their header comments — so parts drawn
from either compose without reconciliation. That is a property of these two
archives, checked, not a general guarantee about multi-tree assembly.

`preserve` (optional, default false) marks a part the simplifier must NOT
touch. This module never simplifies anything, so the flag is carried rather
than acted on here: build_from_recipe records it on the part, prepare_specimen
hands the names to tools/specimen_pipeline.mjs, and the decimation is scoped
there. Preservation is not free — the triangle budget the rest of the specimen
gets is what remains after the preserved parts have taken their share.

Axis conventions
----------------
"LPS-to-glTF" converts the medical-imaging convention (+x anatomical LEFT,
+y POSTERIOR, +z SUPERIOR — what BodyParts3D uses) to glTF's (+y UP,
+z toward the viewer, +x to the viewer's right):

    gltf = (x, z, -y)

Determinant +1, so winding order and surface normals survive unchanged — no
face flip, no inside-out geometry. The result is the conventional anterior
view: the patient's left appears on the viewer's right, as in every textbook
plate and every dissection photograph.

Stdlib only, deliberately
-------------------------
trimesh and pygltflib both do this well, and either would have been a
reasonable answer. Neither is installed, and the whole Python side of this
project is stdlib-only so that `python3 tools/...` works on a fresh machine
with nothing to set up — the same property that makes prepare_specimen.py
useful. Adding a numpy/scipy dependency chain to parse a text format and
re-emit a container this repo already writes elsewhere would trade that away
for nothing. The GLB writer is lifted from make_test_specimen.py, where it has
been producing files that pass validate_specimen_glb.py since Stage 0.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import struct
import sys

# ── .obj reading ──────────────────────────────────────────────────────────


def read_obj(path, default_name=None):
    """Parse one .obj into [{name, verts, faces}].

    Handles the parts of the format that matter here and ignores the rest:

      v x y z [w]     vertex; a 4th value is a weight, not a coordinate
      f a b c ...     face, as v / v/vt / v//vn / v/vt/vn; n-gons are fanned
                      into triangles, which is exact for the convex faces
                      every exporter emits
      o name / g name start a new part

    Indices may be negative, meaning "counted back from here" — resolved
    against the vertex count at the point the face is read, per the spec.

    Vertex normals in the file are ignored: normals are recomputed from the
    geometry on write, so a file with absent, stale or non-normalised normals
    cannot produce shading that disagrees with its own triangles.
    """
    verts = []
    parts = []
    current = None

    def open_part(name):
        nonlocal current
        current = {"name": name, "faces": []}
        parts.append(current)

    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not line or line[0] == "#":
                continue
            tag, _, rest = line.partition(" ")
            if tag == "v":
                bits = rest.split()
                if len(bits) < 3:
                    continue
                verts.append((float(bits[0]), float(bits[1]), float(bits[2])))
            elif tag == "f":
                if current is None:
                    open_part(default_name
                              or os.path.splitext(os.path.basename(path))[0])
                corners = []
                for token in rest.split():
                    head = token.split("/", 1)[0]
                    if not head:
                        continue
                    i = int(head)
                    corners.append(i - 1 if i > 0 else len(verts) + i)
                for k in range(1, len(corners) - 1):
                    current["faces"].append(
                        (corners[0], corners[k], corners[k + 1]))
            elif tag in ("o", "g"):
                name = rest.strip()
                if name:
                    open_part(name)

    # Faces index into one shared vertex list; give each part only the vertices
    # it uses, so parts are independent meshes rather than views onto a pool.
    out = []
    for part in parts:
        if not part["faces"]:
            continue
        remap = {}
        local_verts = []
        local_faces = []
        for face in part["faces"]:
            tri = []
            for index in face:
                if index not in remap:
                    remap[index] = len(local_verts)
                    local_verts.append(verts[index])
                tri.append(remap[index])
            local_faces.append(tuple(tri))
        out.append({"name": part["name"], "verts": local_verts,
                    "faces": local_faces})
    return out


def merge_parts(parts, name):
    """Concatenate several meshes into one named part, rebasing indices."""
    verts, faces = [], []
    for part in parts:
        base = len(verts)
        verts.extend(part["verts"])
        faces.extend((a + base, b + base, c + base)
                     for a, b, c in part["faces"])
    return {"name": name, "verts": verts, "faces": faces}


# ── transforms ────────────────────────────────────────────────────────────

def bounds(parts):
    lo = [math.inf] * 3
    hi = [-math.inf] * 3
    for part in parts:
        for v in part["verts"]:
            for i in range(3):
                if v[i] < lo[i]:
                    lo[i] = v[i]
                if v[i] > hi[i]:
                    hi[i] = v[i]
    return lo, hi


def apply_transform(parts, spec):
    """Re-orient, recentre and rescale every part together.

    Together matters: each part is moved by the SAME transform, derived from
    the bounds of all of them. Normalising parts individually would stack them
    on top of each other and destroy the specimen.
    """
    axes = (spec or {}).get("axes", "none")
    if axes == "LPS-to-glTF":
        for part in parts:
            part["verts"] = [(x, z, -y) for (x, y, z) in part["verts"]]
    elif axes not in ("none", None):
        raise ValueError(f"unknown axes conversion: {axes!r}")

    lo, hi = bounds(parts)
    span = [hi[i] - lo[i] for i in range(3)]

    scale = 1.0
    target = (spec or {}).get("scaleTo")
    if target:
        longest = max(span) or 1.0
        scale = float(target) / longest

    offset = [0.0, 0.0, 0.0]
    if (spec or {}).get("recentre", "none") == "bounds":
        offset = [-(lo[i] + hi[i]) / 2.0 for i in range(3)]

    if scale != 1.0 or any(offset):
        for part in parts:
            part["verts"] = [
                ((x + offset[0]) * scale,
                 (y + offset[1]) * scale,
                 (z + offset[2]) * scale)
                for (x, y, z) in part["verts"]
            ]
    return parts


# ── geometry helpers (shared with make_test_specimen.py) ──────────────────

def compute_normals(verts, faces):
    """Area-weighted vertex normals. A degenerate triangle contributes a zero
    cross product and so weights itself out rather than poisoning the average;
    a vertex touched only by degenerate faces falls back to +Y."""
    acc = [[0.0, 0.0, 0.0] for _ in verts]
    for a, b, c in faces:
        va, vb, vc = verts[a], verts[b], verts[c]
        e1 = (vb[0] - va[0], vb[1] - va[1], vb[2] - va[2])
        e2 = (vc[0] - va[0], vc[1] - va[1], vc[2] - va[2])
        n = (e1[1] * e2[2] - e1[2] * e2[1],
             e1[2] * e2[0] - e1[0] * e2[2],
             e1[0] * e2[1] - e1[1] * e2[0])
        for index in (a, b, c):
            acc[index][0] += n[0]
            acc[index][1] += n[1]
            acc[index][2] += n[2]
    out = []
    for n in acc:
        length = math.sqrt(n[0] * n[0] + n[1] * n[1] + n[2] * n[2])
        out.append((0.0, 1.0, 0.0) if length < 1e-20
                   else (n[0] / length, n[1] / length, n[2] / length))
    return out


def bbox(verts):
    lo = [math.inf] * 3
    hi = [-math.inf] * 3
    for v in verts:
        for i in range(3):
            if v[i] < lo[i]:
                lo[i] = v[i]
            if v[i] > hi[i]:
                hi[i] = v[i]
    return lo, hi


# ── GLB writing ───────────────────────────────────────────────────────────

JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942
ARRAY_BUFFER = 34962
ELEMENT_ARRAY_BUFFER = 34963
FLOAT = 5126
UNSIGNED_INT = 5125

# A neutral tissue colour. The studio's own materials and lighting dress the
# specimen (renderer/mesh/tiers.ts); this is only what a bare viewer shows, and
# it must not pretend to be an authored palette.
DEFAULT_COLOUR = [0.86, 0.72, 0.68, 1.0]
DEFAULT_ROUGHNESS = 0.72


def write_glb(path, parts, generator, scene_name):
    """Assemble an uncompressed GLB: 12-byte header, JSON chunk padded with
    spaces, BIN chunk padded with zeros, every chunk length a multiple of four
    and the header length covering the lot.

    One node per part, named. That naming is the whole point — the studio's
    isolate and layers tools read node names, and a flattened export (every
    triangle in one unnamed mesh) is the failure this pipeline exists to
    prevent."""
    blob = bytearray()
    buffer_views, accessors, meshes, nodes, materials = [], [], [], [], []

    def add_view(payload, target):
        while len(blob) % 4:
            blob.append(0)
        offset = len(blob)
        blob.extend(payload)
        buffer_views.append({"buffer": 0, "byteOffset": offset,
                             "byteLength": len(payload), "target": target})
        return len(buffer_views) - 1

    for part in parts:
        verts, faces = part["verts"], part["faces"]
        normals = compute_normals(verts, faces)

        flat = [i for face in faces for i in face]
        idx_view = add_view(struct.pack(f"<{len(flat)}I", *flat),
                            ELEMENT_ARRAY_BUFFER)
        pos_view = add_view(
            b"".join(struct.pack("<3f", *v) for v in verts), ARRAY_BUFFER)
        nrm_view = add_view(
            b"".join(struct.pack("<3f", *n) for n in normals), ARRAY_BUFFER)

        lo, hi = bbox(verts)
        accessors.append({"bufferView": idx_view,
                          "componentType": UNSIGNED_INT,
                          "count": len(flat), "type": "SCALAR"})
        idx_acc = len(accessors) - 1
        accessors.append({"bufferView": pos_view, "componentType": FLOAT,
                          "count": len(verts), "type": "VEC3",
                          "min": list(lo), "max": list(hi)})
        pos_acc = len(accessors) - 1
        accessors.append({"bufferView": nrm_view, "componentType": FLOAT,
                          "count": len(normals), "type": "VEC3"})
        nrm_acc = len(accessors) - 1

        materials.append({
            "name": f"{part['name']}-material",
            "pbrMetallicRoughness": {
                "baseColorFactor": part.get("colour", DEFAULT_COLOUR),
                "metallicFactor": 0.0,
                "roughnessFactor": part.get("roughness", DEFAULT_ROUGHNESS),
            },
            "doubleSided": False,
        })
        meshes.append({"name": part["name"], "primitives": [{
            "attributes": {"POSITION": pos_acc, "NORMAL": nrm_acc},
            "indices": idx_acc, "material": len(materials) - 1, "mode": 4}]})
        nodes.append({"name": part["name"], "mesh": len(meshes) - 1})

    gltf = {
        "asset": {"version": "2.0", "generator": generator},
        "scene": 0,
        "scenes": [{"name": scene_name, "nodes": list(range(len(nodes)))}],
        "nodes": nodes,
        "meshes": meshes,
        "materials": materials,
        "accessors": accessors,
        "bufferViews": buffer_views,
        "buffers": [{"byteLength": len(blob)}],
    }

    json_bytes = json.dumps(gltf, separators=(",", ":")).encode("utf-8")
    json_bytes += b" " * (-len(json_bytes) % 4)
    bin_bytes = bytes(blob) + b"\x00" * (-len(blob) % 4)
    total = 12 + 8 + len(json_bytes) + 8 + len(bin_bytes)

    with open(path, "wb") as fh:
        fh.write(b"glTF")
        fh.write(struct.pack("<II", 2, total))
        fh.write(struct.pack("<II", len(json_bytes), JSON_CHUNK))
        fh.write(json_bytes)
        fh.write(struct.pack("<II", len(bin_bytes), BIN_CHUNK))
        fh.write(bin_bytes)
    return total


# ── assembly ──────────────────────────────────────────────────────────────

RECIPE_VERSION = "specimen-assembly/v1"


def load_recipe(path):
    with open(path, "r", encoding="utf-8") as fh:
        recipe = json.load(fh)
    if recipe.get("recipe") != RECIPE_VERSION:
        raise ValueError(
            f"{path}: not a {RECIPE_VERSION} recipe "
            f"(found {recipe.get('recipe')!r})")
    if not recipe.get("parts"):
        raise ValueError(f"{path}: recipe declares no parts")
    return recipe


def resolve_source(obj_dir, ref, tree=None):
    """Locate one element file.

    `obj_dir` is either a single directory (the original, still what
    inspect_source_mesh.py and the single-tree path pass) or a mapping of tree
    name to directory, where the unnamed tree is keyed None. A part that asks
    for a tree the caller did not supply is an error rather than a silent fall
    back to the default directory: the two BodyParts3D trees share element ids,
    so a mis-resolved ref would quietly load a DIFFERENT structure that exists
    under the same name, and nothing downstream could see it happen.
    """
    dirs = obj_dir if isinstance(obj_dir, dict) else {None: obj_dir}
    if tree not in dirs:
        known = ", ".join(sorted(str(k) for k in dirs)) or "none"
        raise ValueError(
            f"{ref}: recipe asks for source tree {tree!r} but no directory was "
            f"given for it (have: {known}). Pass --obj-dir {tree}=<path>.")
    candidate = ref if ref.lower().endswith(".obj") else ref + ".obj"
    path = candidate if os.path.isabs(candidate) \
        else os.path.join(dirs[tree], candidate)
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    return path


def build_from_recipe(recipe, obj_dir):
    """Turn a recipe into the part list write_glb wants.

    Every declared file must exist. A recipe that silently drops a missing
    source would produce a specimen with a structure quietly absent from it,
    and nothing downstream could tell that from a structure the source never
    had."""
    parts = []
    for entry in recipe["parts"]:
        name = entry["name"]
        tree = entry.get("tree")
        pieces = []
        for ref in entry["files"]:
            pieces.extend(read_obj(resolve_source(obj_dir, ref, tree)))
        if not pieces:
            raise ValueError(f"part {name!r}: sources contain no geometry")
        part = merge_parts(pieces, name)
        if "colour" in entry:
            part["colour"] = entry["colour"]
        if "roughness" in entry:
            part["roughness"] = entry["roughness"]
        if entry.get("preserve"):
            part["preserve"] = True
        parts.append(part)
    return apply_transform(parts, recipe.get("transform"))


def parse_obj_dirs(values):
    """`["path"]` or `["isa=path", "path"]` → the mapping resolve_source wants.

    A bare path is the unnamed tree (key None); `name=path` is a named one. A
    single string is accepted too, so every existing caller keeps working.
    """
    if values is None:
        return {}
    if isinstance(values, dict):
        return values
    if isinstance(values, str):
        values = [values]
    dirs = {}
    for value in values:
        name, sep, path = value.partition("=")
        dirs[name if sep else None] = os.path.abspath(
            os.path.expanduser(path if sep else value))
    return dirs


def convert(source, out, obj_dir=None, name=None):
    """Single entry point for both shapes of input. Returns the part list that
    was written, so a caller can report on it."""
    if source.lower().endswith(".json"):
        recipe = load_recipe(source)
        dirs = parse_obj_dirs(obj_dir)
        if None not in dirs:
            dirs[None] = os.path.dirname(os.path.abspath(source))
        parts = build_from_recipe(recipe, dirs)
        scene = recipe.get("name") or name or "specimen"
        generator = (f"MrBadmusAI 3D Studio — tools/obj_glb.py "
                     f"({RECIPE_VERSION}, {os.path.basename(source)})")
    else:
        parts = read_obj(source, default_name=name)
        if not parts:
            raise ValueError(f"{source}: no triangle geometry found")
        parts = apply_transform(parts, {"axes": "none", "recentre": "none"})
        scene = name or os.path.splitext(os.path.basename(source))[0]
        generator = "MrBadmusAI 3D Studio — tools/obj_glb.py (.obj)"
    write_glb(out, parts, generator, scene)
    return parts


# ── CLI ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="obj_glb.py",
        description="Convert a Wavefront .obj, or an assembly recipe naming "
                    "many of them, into a multi-part GLB.")
    parser.add_argument("source", help=".obj file or .json assembly recipe")
    parser.add_argument("out", help="output .glb path")
    parser.add_argument("--obj-dir", default=None, action="append",
                        help="where a recipe's source files live (default: "
                             "beside the recipe). Repeat as --obj-dir "
                             "name=path to supply a named source tree.")
    parser.add_argument("--name", default=None, help="scene / part name")
    args = parser.parse_args()

    try:
        parts = convert(args.source, args.out, parse_obj_dirs(args.obj_dir),
                        args.name)
    except (OSError, ValueError) as error:
        print(f"❌ {error}")
        return 1

    total = sum(len(p["faces"]) for p in parts)
    print(f"wrote {args.out} — {len(parts)} part(s), {total:,} triangles")
    for part in parts:
        print(f"  {part['name']:24} {len(part['faces']):7,} triangles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
