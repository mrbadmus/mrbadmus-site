#!/usr/bin/env python3
"""3D Studio — synthetic chambered test specimen generator (Stage 2, MRB-187).

Run it:

    python3 3d-studio/tools/make_test_specimen.py
    python3 3d-studio/tools/make_test_specimen.py --out somewhere/else.glb

Why this exists
---------------
The real specimen GLB has not been acquired yet, and the renderer cannot be
trusted against a sphere. A sphere is centred, convex and solid, so it hides
every bug worth catching: camera framing, bounds normalisation, per-part
materials, part picking, and — above all — the Stage 4 cross-section, which
has nothing to reveal when there is nothing inside.

So this writes geometry shaped like the real thing instead: one closed,
lumpy, deliberately off-centre outer shell with three closed chambers and one
closed tube modelled INSIDE it. Cutting it open is the whole point.

Naming discipline (binding on this project): parts carry neutral test names —
test-shell, test-chamber-01, test-tube-01 — never anatomy. This is a geometry
fixture, not a teaching asset, and it must never be mistaken for one.

How the geometry stays watertight
---------------------------------
Every closed surface here is either a star-shaped radial surface (a UV-sphere
grid whose radius is modulated by a smooth function of direction) or a torus.
Both are closed, orientable and — crucially — cannot self-intersect however
lumpy they get, because each direction carries exactly one surface point.
Manifoldness is a property of the construction, not a hope; the script then
proves it anyway before writing, with the same edge test the validator uses.

Output
------
An uncompressed binary glTF 2.0 (.glb): indexed triangles, POSITION (with the
spec-required min/max) and NORMAL, one node and one PBR material per part.
Deterministic — identical bytes on every run, no randomness anywhere.

Feed it to the purchase-gate validator:

    python3 3d-studio/validate_specimen_glb.py tools/build/_test-specimen.raw.glb

It should clear the watertight-manifold gate and report every interior part
nested inside the shell. It will correctly FAIL the Draco gate: this file is
the uncompressed intermediate. tools/compress_test_specimen.mjs produces the
Draco-compressed file the renderer actually loads.

Stdlib only — no numpy, no third-party anything.
"""

import argparse
import json
import math
import os
import struct
import sys

# ── specimen design constants ─────────────────────────────────────────────

TARGET_HEIGHT = 2.0                      # world units, tip to tip
TARGET_CENTRE = (0.42, -0.31, 0.58)      # deliberately NOT the origin
TRIANGLE_BUDGET = 60_000                 # validator gate 1

# clearance the self-check demands: no interior vertex may sit further than
# this fraction of the way from the shell's centre to the shell's surface.
MAX_CONTAINMENT_RATIO = 0.90

# The shell's anisotropic stretch, applied after the radial modulation.
SHELL_STRETCH = (0.92, 1.12, 0.86)


# ── small vector helpers ──────────────────────────────────────────────────

def f32(x):
    """Round a Python float to the nearest float32 value.

    Positions are rounded once, up front, so the accessor min/max we declare
    are the exact bytes we write. glTF requires POSITION min/max, and a
    validator that recomputes them from the buffer must agree with us.
    """
    return struct.unpack("<f", struct.pack("<f", x))[0]


def rotation_matrix(ax, ay, az):
    """Intrinsic X-then-Y-then-Z rotation. A proper rotation (determinant
    +1), so it preserves triangle winding — an improper one would silently
    turn every normal inward."""
    ca, sa = math.cos(ax), math.sin(ax)
    cb, sb = math.cos(ay), math.sin(ay)
    cc, sc = math.cos(az), math.sin(az)
    return (
        (cb * cc, sa * sb * cc - ca * sc, ca * sb * cc + sa * sc),
        (cb * sc, sa * sb * sc + ca * cc, ca * sb * sc - sa * cc),
        (-sb,     sa * cb,                ca * cb),
    )


def apply_matrix(m, v):
    return (
        m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2],
        m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2],
        m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2],
    )


def bbox(verts):
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    zs = [v[2] for v in verts]
    return (min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs))


# ── radius functions: the shapes themselves ───────────────────────────────
#
# r(theta, phi) modulates a unit sphere. theta is the polar angle from +Y
# (0 at the north pole, pi at the south), phi the azimuth about +Y.
#
# Every phi-dependent term carries a sin(theta) factor so it dies at the
# poles. Without that the radius would be multi-valued where phi is
# undefined, the pole fan would tear, and the mesh would stop being closed.

def shell_radius(theta, phi):
    """The outer shell: lumpy and organic, never spherical, never convex-
    looking, but still star-shaped so it cannot self-intersect."""
    s = math.sin(theta)
    return (1.0
            + 0.100 * s * math.sin(3.0 * phi + 0.70)
            + 0.060 * s * s * math.cos(2.0 * phi - 1.30)
            + 0.035 * s * s * s * math.sin(5.0 * phi + 2.10)
            + 0.075 * math.cos(2.0 * theta + 0.35)
            + 0.035 * math.cos(3.0 * theta - 0.80))


def chamber_radius_01(theta, phi):
    s = math.sin(theta)
    return (1.0
            + 0.130 * s * math.sin(2.0 * phi + 1.10)
            + 0.090 * math.cos(2.0 * theta - 0.50))


def chamber_radius_02(theta, phi):
    s = math.sin(theta)
    return (1.0
            + 0.100 * s * math.sin(3.0 * phi - 0.60)
            + 0.110 * math.cos(2.0 * theta + 1.20))


def chamber_radius_03(theta, phi):
    s = math.sin(theta)
    return (1.0
            + 0.120 * s * s * math.cos(2.0 * phi + 0.30)
            + 0.080 * math.cos(3.0 * theta))


# ── surface builders ──────────────────────────────────────────────────────

def build_radial_shell(radius_fn, stretch, centre, slices, stacks):
    """Closed surface with UV-sphere topology, radius driven by radius_fn.

    Vertex layout: north pole, then (stacks - 1) rings of `slices` vertices,
    then south pole. Rings share no duplicated seam column — column
    `slices - 1` wraps straight back to column 0 — so there is no seam to
    weld and no boundary edge anywhere.

    Winding: for a band between an upper row and a lower row the two
    triangles are (v00, v01, v11) and (v00, v11, v10). Taking the first edge
    along +phi and the second along +theta makes the face normal
    d/dphi x d/dtheta, which points outward for this parametrisation. The
    pole caps are that same rule with one row collapsed to a point, minus the
    degenerate triangle it produces.
    """
    verts = []
    verts.append((centre[0],
                  centre[1] + stretch[1] * radius_fn(0.0, 0.0),
                  centre[2]))
    for row in range(1, stacks):
        theta = math.pi * row / stacks
        st, ct = math.sin(theta), math.cos(theta)
        for col in range(slices):
            phi = 2.0 * math.pi * col / slices
            r = radius_fn(theta, phi)
            verts.append((
                centre[0] + stretch[0] * r * st * math.cos(phi),
                centre[1] + stretch[1] * r * ct,
                centre[2] + stretch[2] * r * st * math.sin(phi),
            ))
    south = len(verts)
    verts.append((centre[0],
                  centre[1] - stretch[1] * radius_fn(math.pi, 0.0),
                  centre[2]))

    def ring(row, col):
        return 1 + (row - 1) * slices + (col % slices)

    faces = []
    for col in range(slices):                       # north cap
        faces.append((0, ring(1, col + 1), ring(1, col)))
    for row in range(1, stacks - 1):                # body bands
        for col in range(slices):
            v00, v01 = ring(row, col), ring(row, col + 1)
            v10, v11 = ring(row + 1, col), ring(row + 1, col + 1)
            faces.append((v00, v01, v11))
            faces.append((v00, v11, v10))
    for col in range(slices):                       # south cap
        faces.append((ring(stacks - 1, col),
                      ring(stacks - 1, col + 1), south))
    return verts, faces


def build_torus(major, minor, centre, rot, major_segments, minor_segments):
    """Closed tube. Genus 1 rather than genus 0, which is exactly why it
    earns its place: it proves the pipeline is not quietly assuming every
    part is sphere-like.

    Winding follows d/dv x d/du (minor before major), which is the outward
    direction for this parametrisation.
    """
    verts = []
    for i in range(major_segments):
        u = 2.0 * math.pi * i / major_segments
        cu, su = math.cos(u), math.sin(u)
        for j in range(minor_segments):
            v = 2.0 * math.pi * j / minor_segments
            radial = major + minor * math.cos(v)
            local = (radial * cu, minor * math.sin(v), radial * su)
            p = apply_matrix(rot, local)
            verts.append((centre[0] + p[0], centre[1] + p[1],
                          centre[2] + p[2]))

    def idx(i, j):
        return (i % major_segments) * minor_segments + (j % minor_segments)

    faces = []
    for i in range(major_segments):
        for j in range(minor_segments):
            a, b = idx(i, j), idx(i, j + 1)
            c, d = idx(i + 1, j + 1), idx(i + 1, j)
            faces.append((a, b, c))
            faces.append((a, c, d))
    return verts, faces


# ── normals ───────────────────────────────────────────────────────────────

def compute_normals(verts, faces):
    """Area-weighted vertex normals from consistently wound faces, so they
    inherit the winding's outward direction rather than guessing at it."""
    acc = [[0.0, 0.0, 0.0] for _ in verts]
    for i, j, k in faces:
        a, b, c = verts[i], verts[j], verts[k]
        ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
        vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
        nx = uy * vz - uz * vy
        ny = uz * vx - ux * vz
        nz = ux * vy - uy * vx
        for t in (i, j, k):
            acc[t][0] += nx
            acc[t][1] += ny
            acc[t][2] += nz
    out = []
    for n in acc:
        length = math.sqrt(n[0] * n[0] + n[1] * n[1] + n[2] * n[2])
        if length < 1e-20:
            out.append((0.0, 1.0, 0.0))
        else:
            out.append((n[0] / length, n[1] / length, n[2] / length))
    return out


# ── self-checks: prove it before writing it ───────────────────────────────

def edge_report(faces):
    """Mirror of the validator's edge_analysis, in stdlib. Returns
    (boundary, overshared, misoriented) — all zero means watertight,
    manifold and consistently wound."""
    undirected = {}
    directed = {}
    for i, j, k in faces:
        for a, b in ((i, j), (j, k), (k, i)):
            key = (a, b) if a < b else (b, a)
            undirected[key] = undirected.get(key, 0) + 1
            directed[(a, b)] = directed.get((a, b), 0) + 1
    boundary = sum(1 for n in undirected.values() if n == 1)
    overshared = sum(1 for n in undirected.values() if n > 2)
    misoriented = sum(1 for n in directed.values() if n > 1)
    return boundary, overshared, misoriented


def degenerate_face_count(verts, faces):
    n = 0
    for i, j, k in faces:
        if i == j or j == k or i == k:
            n += 1
            continue
        a, b, c = verts[i], verts[j], verts[k]
        ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
        vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
        nx = uy * vz - uz * vy
        ny = uz * vx - ux * vz
        nz = ux * vy - uy * vx
        if nx * nx + ny * ny + nz * nz < 1e-30:
            n += 1
    return n


def signed_volume(verts, faces):
    """Divergence-theorem volume. Positive means the winding is outward;
    negative means every normal on this part points into the solid."""
    total = 0.0
    for i, j, k in faces:
        a, b, c = verts[i], verts[j], verts[k]
        total += (a[0] * (b[1] * c[2] - b[2] * c[1])
                  - a[1] * (b[0] * c[2] - b[2] * c[0])
                  + a[2] * (b[0] * c[1] - b[1] * c[0]))
    return total / 6.0


def containment_ratio(point):
    """How far a point sits from the shell's centre as a fraction of the
    shell's surface distance in that same direction. Below 1.0 is inside.

    The shell is star-shaped about the origin in model space, so undoing the
    anisotropic stretch turns "inside the lumpy blob" into the plain
    comparison |q| < r(direction of q).
    """
    q = (point[0] / SHELL_STRETCH[0],
         point[1] / SHELL_STRETCH[1],
         point[2] / SHELL_STRETCH[2])
    length = math.sqrt(q[0] * q[0] + q[1] * q[1] + q[2] * q[2])
    if length < 1e-12:
        return 0.0
    theta = math.acos(max(-1.0, min(1.0, q[1] / length)))
    phi = math.atan2(q[2], q[0])
    return length / shell_radius(theta, phi)


def aabbs_overlap(box_a, box_b):
    (a0, a1), (b0, b1) = box_a, box_b
    return all(a0[i] <= b1[i] and b0[i] <= a1[i] for i in range(3))


# ── the specimen layout ───────────────────────────────────────────────────

def build_parts():
    """Build every part in model space, where the shell is centred on the
    origin. A single similarity transform moves the lot into world space
    afterwards, so the interior maths above stays simple."""
    parts = []

    verts, faces = build_radial_shell(
        shell_radius, SHELL_STRETCH, (0.0, 0.0, 0.0),
        slices=96, stacks=56)
    parts.append({
        "name": "test-shell",
        "verts": verts, "faces": faces, "interior": False,
        "colour": [0.784, 0.545, 0.451, 1.0], "roughness": 0.62,
    })

    verts, faces = build_radial_shell(
        chamber_radius_01, (0.27, 0.30, 0.25), (-0.28, 0.29, -0.10),
        slices=48, stacks=32)
    parts.append({
        "name": "test-chamber-01",
        "verts": verts, "faces": faces, "interior": True,
        "colour": [0.624, 0.333, 0.290, 1.0], "roughness": 0.58,
    })

    verts, faces = build_radial_shell(
        chamber_radius_02, (0.27, 0.29, 0.25), (0.34, 0.29, 0.15),
        slices=44, stacks=28)
    parts.append({
        "name": "test-chamber-02",
        "verts": verts, "faces": faces, "interior": True,
        "colour": [0.702, 0.471, 0.298, 1.0], "roughness": 0.66,
    })

    verts, faces = build_radial_shell(
        chamber_radius_03, (0.28, 0.24, 0.26), (-0.10, -0.34, 0.34),
        slices=40, stacks=26)
    parts.append({
        "name": "test-chamber-03",
        "verts": verts, "faces": faces, "interior": True,
        "colour": [0.549, 0.400, 0.341, 1.0], "roughness": 0.60,
    })

    verts, faces = build_torus(
        major=0.175, minor=0.060, centre=(0.19, -0.32, -0.20),
        rot=rotation_matrix(0.62, 0.41, -0.35),
        major_segments=56, minor_segments=20)
    parts.append({
        "name": "test-tube-01",
        "verts": verts, "faces": faces, "interior": True,
        "colour": [0.659, 0.561, 0.420, 1.0], "roughness": 0.55,
    })

    return parts


def transform_to_world(parts):
    """Scale the model so the shell is TARGET_HEIGHT tall, then slide it so
    the shell's centre lands on TARGET_CENTRE. Uniform scale plus
    translation: winding, manifoldness and containment all survive it."""
    lo, hi = bbox(parts[0]["verts"])
    height = hi[1] - lo[1]
    scale = TARGET_HEIGHT / height
    centre = [(lo[i] + hi[i]) / 2.0 for i in range(3)]
    offset = [TARGET_CENTRE[i] - scale * centre[i] for i in range(3)]
    for part in parts:
        part["verts"] = [
            (f32(scale * v[0] + offset[0]),
             f32(scale * v[1] + offset[1]),
             f32(scale * v[2] + offset[2]))
            for v in part["verts"]]
    return scale


def run_self_checks(parts):
    """Everything the validator will test, tested here first, plus the two
    things it cannot test: that the interior parts really are interior, and
    that they do not intersect each other."""
    problems = []
    lines = []

    for part in parts:
        b, o, m = edge_report(part["faces"])
        deg = degenerate_face_count(part["verts"], part["faces"])
        vol = signed_volume(part["verts"], part["faces"])
        if b or o or m:
            problems.append(f"{part['name']}: boundary {b}, overshared {o}, "
                            f"misoriented {m}")
        if deg:
            problems.append(f"{part['name']}: {deg} degenerate faces")
        if vol <= 0.0:
            problems.append(f"{part['name']}: signed volume {vol:+.5f} — "
                            f"winding is inward")
        lines.append(f"    {part['name']:<18} closed, manifold, outward "
                     f"(volume {vol:+.4f})")

    # every interior part must sit genuinely inside the shell
    for part in parts:
        if not part["interior"]:
            continue
        worst = max(containment_ratio(v) for v in part["_model"])
        if worst >= MAX_CONTAINMENT_RATIO:
            problems.append(f"{part['name']}: reaches {worst:.3f} of the way "
                            f"to the shell surface (limit "
                            f"{MAX_CONTAINMENT_RATIO})")
        lines.append(f"    {part['name']:<18} deepest vertex sits at "
                     f"{worst:.3f} of the shell radius")

    # interior parts must not touch each other. Disjoint axis-aligned boxes
    # is a stricter test than non-intersection, and it is exact.
    interior = [p for p in parts if p["interior"]]
    collisions = 0
    for i in range(len(interior)):
        for j in range(i + 1, len(interior)):
            if aabbs_overlap(bbox(interior[i]["_model"]),
                             bbox(interior[j]["_model"])):
                collisions += 1
                problems.append(f"{interior[i]['name']} and "
                                f"{interior[j]['name']} have overlapping "
                                f"bounding boxes")
    if not collisions:
        lines.append(f"    {'interior spacing':<18} {len(interior)} interior "
                     f"parts, every bounding box disjoint")

    return lines, problems


# ── GLB writer ────────────────────────────────────────────────────────────

JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942
ARRAY_BUFFER = 34962
ELEMENT_ARRAY_BUFFER = 34963
FLOAT = 5126
UNSIGNED_INT = 5125


def write_glb(path, parts):
    """Assemble an uncompressed GLB: 12-byte header, JSON chunk padded with
    spaces, BIN chunk padded with zeros, every chunk length a multiple of
    four and the header length covering the lot."""
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
        accessors.append({"bufferView": idx_view, "componentType":
                          UNSIGNED_INT, "count": len(flat), "type": "SCALAR"})
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
                "baseColorFactor": part["colour"],
                "metallicFactor": 0.0,
                "roughnessFactor": part["roughness"],
            },
            "doubleSided": False,
        })
        meshes.append({"name": part["name"], "primitives": [{
            "attributes": {"POSITION": pos_acc, "NORMAL": nrm_acc},
            "indices": idx_acc, "material": len(materials) - 1, "mode": 4}]})
        nodes.append({"name": part["name"], "mesh": len(meshes) - 1})

    gltf = {
        "asset": {"version": "2.0",
                  "generator": "MrBadmusAI 3D Studio — "
                               "tools/make_test_specimen.py (MRB-187)"},
        "scene": 0,
        "scenes": [{"name": "test-specimen",
                    "nodes": list(range(len(nodes)))}],
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


# ── entry point ───────────────────────────────────────────────────────────

STUDIO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join("tools", "build", "_test-specimen.raw.glb")


def main():
    parser = argparse.ArgumentParser(
        description="Write the synthetic chambered test specimen GLB.")
    parser.add_argument(
        "--out", default=None,
        help="output path. Default: tools/build/_test-specimen.raw.glb "
             "relative to the 3d-studio/ directory. An explicit path is "
             "taken as given (relative paths resolve against the current "
             "working directory).")
    args = parser.parse_args()
    out = args.out if args.out else os.path.join(STUDIO_DIR, DEFAULT_OUT)
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    print("3D Studio — synthetic chambered test specimen\n")

    parts = build_parts()
    for part in parts:
        part["_model"] = part["verts"]
    scale = transform_to_world(parts)

    print("  Self-checks (run before a single byte is written):")
    lines, problems = run_self_checks(parts)
    for line in lines:
        if line:
            print(line)
    if problems:
        print("\n  ❌ geometry is not fit to write:")
        for p in problems:
            print(f"     • {p}")
        return 1

    tri_total = sum(len(p["faces"]) for p in parts)
    vert_total = sum(len(p["verts"]) for p in parts)
    if tri_total >= TRIANGLE_BUDGET:
        print(f"\n  ❌ {tri_total:,} triangles exceeds the "
              f"{TRIANGLE_BUDGET:,} budget")
        return 1

    size = write_glb(out, parts)

    print("\n  Parts:")
    for part in parts:
        lo, hi = bbox(part["verts"])
        dims = " × ".join(f"{hi[i] - lo[i]:.3f}" for i in range(3))
        print(f"    {part['name']:<18} {len(part['verts']):>6,} vertices  "
              f"{len(part['faces']):>6,} triangles   {dims}")

    lo, hi = bbox([v for p in parts for v in p["verts"]])
    print(f"\n  Totals:     {len(parts)} parts, {vert_total:,} vertices, "
          f"{tri_total:,} triangles (budget {TRIANGLE_BUDGET:,})")
    print(f"  Bounds:     min ({lo[0]:+.3f}, {lo[1]:+.3f}, {lo[2]:+.3f})  "
          f"max ({hi[0]:+.3f}, {hi[1]:+.3f}, {hi[2]:+.3f})")
    print(f"  Size:       {hi[0] - lo[0]:.3f} × {hi[1] - lo[1]:.3f} × "
          f"{hi[2] - lo[2]:.3f} units, centred "
          f"({(lo[0] + hi[0]) / 2:+.3f}, {(lo[1] + hi[1]) / 2:+.3f}, "
          f"{(lo[2] + hi[2]) / 2:+.3f}) — off-origin on purpose")
    print(f"  Model scale applied: ×{scale:.5f}")
    print(f"\n  ✅ wrote {out}")
    print(f"     {size:,} bytes, uncompressed — "
          f"tools/compress_test_specimen.mjs makes the Draco one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
