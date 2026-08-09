#!/usr/bin/env python3
"""3D Studio — specimen GLB purchase-gate validator (spec v1 §4, MRB-185).

Run it:

    python3 3d-studio/validate_specimen_glb.py path/to/specimen.glb

Written before the heart asset exists, so it can run the moment Mide acquires
a candidate. It checks the mechanical purchase gates and reports honestly on
the ones a script cannot decide.

Gates checked mechanically (PASS / FAIL / UNKNOWN):

  1. Triangle count       — under 60,000
  2. Texture dimensions   — 1024 × 1024 maximum
  3. File size            — under 3 MB (3,145,728 bytes)
  4. Draco compression    — KHR_draco_mesh_compression must be present
  5. Watertight manifold  — every edge shared by exactly two faces, with
                            consistent winding, after welding coincident
                            vertices (tolerance 1e-6 of the mesh's largest
                            bounding-box dimension)

Reported as SIGNALS ONLY, never pass/fail:

  6. Interior geometry    — the hard purchase gate. This script computes
     indicative signals (shell count, shells nested inside other shells via
     ray-parity containment, interior-surface ray probe) but a script CANNOT
     confirm that interior structure is anatomically meaningful chambers and
     valves rather than junk geometry. A human must open the model and cut a
     cross-section before purchase — instructions are printed with the
     signals.

  Gate 7 of the spec (anatomically correct at teaching fidelity, matching AQA
  diagram conventions) is entirely human judgement — Mide's examiner eye —
  and is out of this tool's scope by design.

Dependencies:
  - numpy (required — present on this machine)
  - DracoPy (optional; REQUIRED to run the geometry gates on a
    Draco-compressed file: `pip install DracoPy`. Triangle count, textures,
    size and Draco-presence still work without it, because glTF accessors
    declare the decompressed counts in the JSON.)

Triangle counts are read from the glTF accessor declarations, which the glTF
spec requires to describe the decompressed geometry — so the count gate is
exact even when the geometry itself cannot be decoded.

Exit code 0 = every mechanical gate passed. 1 = at least one FAIL.
2 = a gate is UNKNOWN (could not be verified — treat as not yet cleared).
"""

import base64
import json
import os
import struct
import sys

import numpy as np

try:
    import DracoPy
    HAVE_DRACO = True
except ImportError:
    HAVE_DRACO = False

TRIANGLE_LIMIT = 60_000
TEXTURE_LIMIT = 1024
SIZE_LIMIT = 3 * 1024 * 1024
WELD_DECIMALS_REL = 1e-6

COMPONENT_DTYPES = {
    5120: np.int8, 5121: np.uint8, 5122: np.int16,
    5123: np.uint16, 5125: np.uint32, 5126: np.float32,
}
TYPE_COMPONENT_COUNTS = {
    "SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4,
    "MAT2": 4, "MAT3": 9, "MAT4": 16,
}


# ── GLB container ─────────────────────────────────────────────────────────

def parse_glb(path):
    """Return (gltf_json, bin_chunk_bytes)."""
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) < 12 or data[:4] != b"glTF":
        raise ValueError("not a GLB file (missing 'glTF' magic)")
    version, length = struct.unpack_from("<II", data, 4)
    if version != 2:
        raise ValueError(f"GLB version {version} — this tool expects 2")
    offset, gltf, bin_chunk = 12, None, b""
    while offset + 8 <= len(data):
        chunk_len, chunk_type = struct.unpack_from("<II", data, offset)
        chunk = data[offset + 8: offset + 8 + chunk_len]
        if chunk_type == 0x4E4F534A:        # 'JSON'
            gltf = json.loads(chunk.decode("utf-8"))
        elif chunk_type == 0x004E4942:      # 'BIN'
            bin_chunk = chunk
        offset += 8 + chunk_len + (-chunk_len % 4 if chunk_len % 4 else 0)
    if gltf is None:
        raise ValueError("GLB has no JSON chunk")
    return gltf, bin_chunk


def buffer_view_bytes(gltf, bin_chunk, bv_index, glb_dir):
    bv = gltf["bufferViews"][bv_index]
    buf = gltf["buffers"][bv["buffer"]]
    uri = buf.get("uri")
    if uri is None:
        src = bin_chunk
    elif uri.startswith("data:"):
        src = base64.b64decode(uri.split(",", 1)[1])
    else:
        with open(os.path.join(glb_dir, uri), "rb") as fh:
            src = fh.read()
    start = bv.get("byteOffset", 0)
    return src, start, bv.get("byteLength", len(src) - start), bv.get("byteStride")


def read_accessor(gltf, bin_chunk, acc_index, glb_dir):
    """Decode a non-sparse accessor into an (count, ncomp) numpy array.
    Returns None when the accessor has no bufferView (Draco-only payload)."""
    acc = gltf["accessors"][acc_index]
    if "sparse" in acc:
        raise ValueError("sparse accessors not supported by this tool")
    if "bufferView" not in acc:
        return None
    dtype = COMPONENT_DTYPES[acc["componentType"]]
    ncomp = TYPE_COMPONENT_COUNTS[acc["type"]]
    count = acc["count"]
    src, bv_start, _bv_len, stride = buffer_view_bytes(
        gltf, bin_chunk, acc["bufferView"], glb_dir)
    start = bv_start + acc.get("byteOffset", 0)
    itemsize = np.dtype(dtype).itemsize
    packed = itemsize * ncomp
    if stride is None or stride == packed:
        arr = np.frombuffer(src, dtype=dtype, count=count * ncomp,
                            offset=start)
        return arr.reshape(count, ncomp)
    rows = []
    for i in range(count):
        off = start + i * stride
        rows.append(np.frombuffer(src, dtype=dtype, count=ncomp, offset=off))
    return np.stack(rows)


# ── image header parsing (PNG / JPEG / WebP) ──────────────────────────────

def image_dimensions(blob):
    """Return (width, height, format) or (None, None, reason)."""
    if blob[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack_from(">II", blob, 16)
        return w, h, "png"
    if blob[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(blob):
            if blob[i] != 0xFF:
                i += 1
                continue
            marker = blob[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            seg_len = struct.unpack_from(">H", blob, i + 2)[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack_from(">HH", blob, i + 5)
                return w, h, "jpeg"
            i += 2 + seg_len
        return None, None, "jpeg (no SOF found)"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
        fmt = blob[12:16]
        if fmt == b"VP8X":
            w = int.from_bytes(blob[24:27], "little") + 1
            h = int.from_bytes(blob[27:30], "little") + 1
            return w, h, "webp"
        if fmt == b"VP8L":
            bits = int.from_bytes(blob[21:25], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1, "webp"
        if fmt == b"VP8 ":
            w, h = struct.unpack_from("<HH", blob, 26)
            return (w & 0x3FFF), (h & 0x3FFF), "webp"
    return None, None, "unrecognised image format"


# ── geometry extraction ───────────────────────────────────────────────────

def primitive_triangle_count(gltf, prim):
    mode = prim.get("mode", 4)
    if "indices" in prim:
        n = gltf["accessors"][prim["indices"]]["count"]
    else:
        n = gltf["accessors"][prim["attributes"]["POSITION"]]["count"]
    if mode == 4:
        return n // 3
    if mode in (5, 6):                      # strip / fan
        return max(n - 2, 0)
    return 0                                # points / lines contribute none


def extract_geometry(gltf, bin_chunk, glb_dir):
    """Return (positions (n,3) float array, faces (m,3) int array,
    notes list). Concatenates every triangle primitive of every mesh.
    Raises RuntimeError when geometry exists but cannot be decoded."""
    all_pos, all_faces, notes = [], [], []
    base = 0
    for mesh in gltf.get("meshes", []):
        for prim in mesh.get("primitives", []):
            if prim.get("mode", 4) != 4:
                notes.append("non-triangle primitive skipped "
                             f"(mode {prim.get('mode')})")
                continue
            draco = prim.get("extensions", {}).get(
                "KHR_draco_mesh_compression")
            if draco is not None:
                if not HAVE_DRACO:
                    raise RuntimeError(
                        "geometry is Draco-compressed and DracoPy is not "
                        "installed — run `pip install DracoPy` to enable the "
                        "watertight/manifold and interior-signal checks")
                src, start, length, _ = buffer_view_bytes(
                    gltf, bin_chunk, draco["bufferView"], glb_dir)
                decoded = DracoPy.decode(bytes(src[start:start + length]))
                pos = np.asarray(decoded.points, dtype=np.float64)
                faces = np.asarray(decoded.faces, dtype=np.int64)
            else:
                pos_arr = read_accessor(
                    gltf, bin_chunk, prim["attributes"]["POSITION"], glb_dir)
                if pos_arr is None:
                    raise RuntimeError("POSITION accessor has no bufferView "
                                       "and no Draco payload")
                pos = pos_arr.astype(np.float64)
                if "indices" in prim:
                    idx = read_accessor(gltf, bin_chunk, prim["indices"],
                                        glb_dir)
                    faces = idx.reshape(-1, 3).astype(np.int64)
                else:
                    faces = np.arange(len(pos), dtype=np.int64).reshape(-1, 3)
            all_pos.append(pos)
            all_faces.append(faces + base)
            base += len(pos)
    if not all_pos:
        raise RuntimeError("no triangle geometry found")
    return np.vstack(all_pos), np.vstack(all_faces), notes


def weld(positions, faces):
    """Merge vertices coincident within a relative tolerance so seams do not
    read as boundary edges. Returns (welded_positions, remapped_faces)."""
    extent = float(np.max(positions.max(axis=0) - positions.min(axis=0)))
    tol = max(extent, 1e-12) * WELD_DECIMALS_REL
    quantised = np.round(positions / tol).astype(np.int64)
    _, first_index, inverse = np.unique(
        quantised, axis=0, return_index=True, return_inverse=True)
    welded = positions[first_index]
    remapped = inverse[faces]
    keep = ~((remapped[:, 0] == remapped[:, 1])
             | (remapped[:, 1] == remapped[:, 2])
             | (remapped[:, 0] == remapped[:, 2]))
    return welded, remapped[keep], int((~keep).sum())


def edge_analysis(faces):
    """Return (boundary_edge_count, overshared_edge_count,
    misoriented_edge_count). Watertight manifold = all three are zero."""
    a, b, c = faces[:, 0], faces[:, 1], faces[:, 2]
    directed = np.concatenate([
        np.stack([a, b], 1), np.stack([b, c], 1), np.stack([c, a], 1)])
    undirected = np.sort(directed, axis=1)
    _, und_counts = np.unique(undirected, axis=0, return_counts=True)
    boundary = int((und_counts == 1).sum())
    overshared = int((und_counts > 2).sum())
    _, dir_counts = np.unique(directed, axis=0, return_counts=True)
    misoriented = int((dir_counts > 1).sum())
    return boundary, overshared, misoriented


def connected_components(n_vertices, faces):
    """Union-find over face-connected vertices → per-face component labels."""
    parent = np.arange(n_vertices)

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    for f in faces:
        r0, r1, r2 = find(f[0]), find(f[1]), find(f[2])
        parent[r1] = r0
        parent[r2] = r0
    roots = np.array([find(v) for v in faces[:, 0]])
    labels = {r: i for i, r in enumerate(dict.fromkeys(roots.tolist()))}
    return np.array([labels[r] for r in roots]), len(labels)


def ray_hit_count(origin, direction, v0, v1, v2, eps=1e-12):
    """Möller–Trumbore, vectorised over triangles; returns the number of
    distinct surface crossings. Hits are deduplicated by intersection
    distance, because a ray crossing the shared edge of two triangles
    registers on both — one wall must count once."""
    e1, e2 = v1 - v0, v2 - v0
    h = np.cross(direction, e2)
    a = np.einsum("ij,ij->i", e1, h)
    mask = np.abs(a) > eps
    f = np.zeros_like(a)
    f[mask] = 1.0 / a[mask]
    s = origin - v0
    u = f * np.einsum("ij,ij->i", s, h)
    q = np.cross(s, e1)
    v = f * (q @ direction)
    t = f * np.einsum("ij,ij->i", e2, q)
    hits = mask & (u >= 0) & (v >= 0) & (u + v <= 1) & (t > 1e-9)
    if not hits.any():
        return 0
    return int(np.unique(np.round(t[hits], 6)).size)


def interior_signals(positions, faces, face_labels, n_components):
    """Indicative-only signals for interior geometry."""
    signals = []
    tris = positions[faces]
    signals.append(f"shell/component count: {n_components}")

    # nested shells: is component i's centroid inside component j's surface?
    # Directions are deliberately asymmetric so rays do not run along the
    # symmetry planes and shared edges that typical modelled geometry has.
    if n_components > 1:
        nested = []
        rng_dirs = np.array([
            [0.276, 0.583, 0.764], [-0.831, 0.322, 0.454],
            [0.447, -0.795, 0.410], [0.638, 0.221, -0.738],
            [-0.353, -0.606, 0.713]])
        for i in range(n_components):
            ci = positions[np.unique(faces[face_labels == i])].mean(axis=0)
            for j in range(n_components):
                if i == j:
                    continue
                tj = tris[face_labels == j]
                votes = sum(
                    ray_hit_count(ci, d / np.linalg.norm(d),
                                  tj[:, 0], tj[:, 1], tj[:, 2]) % 2
                    for d in rng_dirs)
                if votes >= 3:      # majority of 5 rays says inside
                    nested.append((i, j))
        if nested:
            for i, j in nested:
                signals.append(
                    f"component {i} lies INSIDE component {j} "
                    f"(ray-parity majority) — consistent with modelled "
                    f"interior structure")
        else:
            signals.append("no component nests inside another — multiple "
                           "shells sit side by side")

    # interior-surface probe: from the bounding-box centre, count surface
    # crossings along fixed rays. From inside one hollow shell every ray
    # crosses once (odd, =1); counts of 3+ mean surfaces exist between the
    # centre and the outer wall — i.e. interior geometry of SOME kind.
    centre = (positions.min(axis=0) + positions.max(axis=0)) / 2.0
    golden = np.pi * (3.0 - np.sqrt(5.0))
    counts = []
    for k in range(24):
        y = 1.0 - (k / 23.0) * 2.0
        r = np.sqrt(max(0.0, 1.0 - y * y))
        d = np.array([np.cos(golden * k) * r, y, np.sin(golden * k) * r])
        counts.append(ray_hit_count(centre, d, tris[:, 0], tris[:, 1],
                                    tris[:, 2]))
    counts = np.array(counts)
    signals.append(
        f"bbox-centre ray probe (24 rays): crossings min {counts.min()} / "
        f"median {int(np.median(counts))} / max {counts.max()} — "
        f"{int((counts >= 3).sum())}/24 rays cross 3+ surfaces")
    return signals


# ── report ────────────────────────────────────────────────────────────────

def gate_line(name, status, detail):
    mark = {"PASS": "✅", "FAIL": "❌", "UNKNOWN": "⚠️ "}[status]
    print(f"  {mark} {name:<22} {status:<8} {detail}")
    return status


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"❌ file not found: {path}")
        return 2
    glb_dir = os.path.dirname(os.path.abspath(path))

    print(f"3D Studio GLB purchase gates — {path}\n")
    statuses = []

    # gate 3: file size
    size = os.path.getsize(path)
    statuses.append(gate_line(
        "File size", "PASS" if size < SIZE_LIMIT else "FAIL",
        f"{size:,} bytes ({size / (1024 * 1024):.2f} MiB), limit "
        f"{SIZE_LIMIT:,} (3 MiB)"))

    try:
        gltf, bin_chunk = parse_glb(path)
    except (ValueError, OSError) as e:
        print(f"\n❌ cannot parse GLB: {e}")
        return 1

    # gate 4: Draco
    exts = set(gltf.get("extensionsRequired", [])) \
        | set(gltf.get("extensionsUsed", []))
    has_draco = "KHR_draco_mesh_compression" in exts
    statuses.append(gate_line(
        "Draco compression", "PASS" if has_draco else "FAIL",
        "KHR_draco_mesh_compression "
        + ("present" if has_draco else "ABSENT — gate requires Draco")))

    # gate 1: triangle count (exact from accessor declarations)
    tri_total = 0
    for mesh in gltf.get("meshes", []):
        for prim in mesh.get("primitives", []):
            tri_total += primitive_triangle_count(gltf, prim)
    statuses.append(gate_line(
        "Triangle count", "PASS" if tri_total < TRIANGLE_LIMIT else "FAIL",
        f"{tri_total:,} triangles, limit {TRIANGLE_LIMIT:,}"))

    # gate 2: texture dimensions
    images = gltf.get("images", [])
    if not images:
        statuses.append(gate_line("Textures", "PASS",
                                  "no images embedded or referenced"))
    else:
        worst, details = "PASS", []
        for i, img in enumerate(images):
            if "bufferView" in img:
                src, start, length, _ = buffer_view_bytes(
                    gltf, bin_chunk, img["bufferView"], glb_dir)
                blob = bytes(src[start:start + length])
            elif img.get("uri", "").startswith("data:"):
                blob = base64.b64decode(img["uri"].split(",", 1)[1])
            elif "uri" in img:
                try:
                    with open(os.path.join(glb_dir, img["uri"]), "rb") as fh:
                        blob = fh.read()
                except OSError:
                    details.append(f"img{i}: external file missing")
                    worst = "UNKNOWN" if worst == "PASS" else worst
                    continue
            else:
                details.append(f"img{i}: no data")
                worst = "UNKNOWN" if worst == "PASS" else worst
                continue
            w, h, fmt = image_dimensions(blob)
            if w is None:
                details.append(f"img{i}: {fmt}")
                worst = "UNKNOWN" if worst == "PASS" else worst
            else:
                details.append(f"img{i}: {w}×{h} {fmt}")
                if w > TEXTURE_LIMIT or h > TEXTURE_LIMIT:
                    worst = "FAIL"
        statuses.append(gate_line(
            "Textures", worst,
            f"limit {TEXTURE_LIMIT}×{TEXTURE_LIMIT} — " + "; ".join(details)))

    # gate 5: watertight manifold (+ interior signals from the same geometry)
    geometry_err = None
    try:
        positions, faces, notes = extract_geometry(gltf, bin_chunk, glb_dir)
        positions_w, faces_w, dropped = weld(positions, faces)
        boundary, overshared, misoriented = edge_analysis(faces_w)
        ok = boundary == 0 and overshared == 0 and misoriented == 0
        detail = (f"boundary edges {boundary}, edges shared by 3+ faces "
                  f"{overshared}, misoriented edge pairs {misoriented}"
                  + (f", degenerate faces dropped {dropped}" if dropped else "")
                  + (f" [{'; '.join(notes)}]" if notes else ""))
        statuses.append(gate_line(
            "Watertight manifold", "PASS" if ok else "FAIL", detail))
    except RuntimeError as e:
        geometry_err = str(e)
        statuses.append(gate_line("Watertight manifold", "UNKNOWN",
                                  geometry_err))

    # interior geometry — signals only, never a verdict
    print("\n  🔬 Interior geometry — the hard purchase gate (signals only):")
    if geometry_err:
        print(f"     cannot compute signals: {geometry_err}")
    else:
        face_labels, n_components = connected_components(
            len(positions_w), faces_w)
        for s in interior_signals(positions_w, faces_w, face_labels,
                                  n_components):
            print(f"     • {s}")
    print("""
     HONEST LIMIT: this script can show that surfaces exist inside the
     outer shell; it CANNOT confirm they are anatomically meaningful
     chambers, valves and lumens rather than junk geometry, and a clever
     hollow shell with a stray inner plane would fool every heuristic
     above. Before purchase a human must:
       1. open the GLB in a viewer with a clipping plane
          (Blender, or https://gltf-viewer.donmccurdy.com + Blender cut)
       2. drag the section plane through the specimen
       3. confirm the internal structure students must name is modelled,
          not painted on — for the heart: chambers, valves, vessel lumens
     Anatomical correctness at teaching fidelity (spec gate 6) is Mide's
     examiner judgement, out of scope for this tool.""")

    fails = statuses.count("FAIL")
    unknowns = statuses.count("UNKNOWN")
    print(f"\nMechanical gates: {statuses.count('PASS')} pass, {fails} fail, "
          f"{unknowns} unverified. Interior geometry: HUMAN CHECK REQUIRED.")
    return 1 if fails else (2 if unknowns else 0)


if __name__ == "__main__":
    sys.exit(main())
