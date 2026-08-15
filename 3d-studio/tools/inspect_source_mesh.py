#!/usr/bin/env python3
"""3D Studio — interrogate a source mesh BEFORE it becomes a specimen.

Run it:

    python3 tools/inspect_source_mesh.py report  <obj-dir> FJ2428 FJ2422
    python3 tools/inspect_source_mesh.py probe   <obj-dir> --wall FJ2428 --cavity FJ2422
    python3 tools/inspect_source_mesh.py clean   <obj-dir> FJ2428 out.obj
    python3 tools/inspect_source_mesh.py section <obj-dir> FJ2428 out.svg

Why this exists
---------------
validate_specimen_glb.py gates a FINISHED GLB, and on the one gate that matters
most — is the interior really modelled? — it can only print HUMAN CHECK
REQUIRED. That check happens far too late: by then the mesh has been assembled,
transformed, Draco-compressed and named, and if the interior turns out to be
solid the whole assembly was wasted.

This tool asks the question at the other end, of the raw source files, before a
recipe is written. It was built during the MRB-218 investigation into whether
BodyParts3D could show the left ventricle wall being thicker than the right, and
every one of its four commands earned its place by answering something that
naming alone got wrong:

  report   A name is not geometry. `wall of right ventricle` sounds like a
           shell; its volume and bounding box said "three small lumps". Volume,
           watertightness, shell count and bbox tell you what a file IS.

  probe    The decisive one. Fire rays from inside a cavity mesh outward and
           count how many directions meet the candidate wall. An enclosing
           shell covers ~90%+ of directions; scattered muscle stubs cover 3–10%.
           No naming convention can fake angular coverage. It also reports the
           wall thickness along each ray, which is the number a teaching model
           lives or dies by.

  clean    Anatomical releases ship stray zero-volume sliver components that
           carry all of a mesh's topology errors and fail the watertight gate
           for no anatomical reason. This drops components below a volume
           threshold and reports how much volume went with them, so the claim
           "nothing anatomical was removed" is checkable rather than trusted.
           It deletes components; it never adds, moves or thickens geometry.

  section  Writes a true cross-section as SVG — the plane/mesh intersection,
           filled by the even-odd rule. This is the cut the validator tells a
           human to make, produced automatically, for any specimen. It also
           reports whether the intersection forms closed loops: if it does not,
           the fill is unreliable and the picture should not be trusted.

Dependencies: numpy, which validate_specimen_glb.py already requires. The SVG
is written with stdlib string formatting, so nothing new is needed to draw.
Geometry reading is tools/obj_glb.py, the module the specimen pipeline already
uses, so this tool and the pipeline can never disagree about what a file says.

Coordinates are whatever the source uses. BodyParts3D is millimetres in an LPS
whole-body frame, so its numbers come out as millimetres directly; no transform
is applied here, deliberately, because a measurement is worth more in the frame
the source author used than in a renormalised one.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import obj_glb  # noqa: E402  (needs the path line above)

WELD_REL = 1e-6


# ── loading and topology ──────────────────────────────────────────────────

def load(obj_dir, refs):
    """Merge one or more element files into a single (verts, faces) pair."""
    pieces = []
    for ref in refs:
        pieces.extend(obj_glb.read_obj(obj_glb.resolve_source(obj_dir, ref)))
    if not pieces:
        raise ValueError(f"{refs}: no triangle geometry found")
    merged = obj_glb.merge_parts(pieces, "merged")
    return (np.asarray(merged["verts"], dtype=np.float64),
            np.asarray(merged["faces"], dtype=np.int64))


def weld(verts, faces):
    """Merge coincident vertices so shared seams stop reading as open edges.

    The same tolerance rule validate_specimen_glb.py uses, so a mesh that looks
    watertight here looks watertight to the gate.
    """
    extent = float(np.max(verts.max(axis=0) - verts.min(axis=0)))
    tol = max(extent, 1e-12) * WELD_REL
    quantised = np.round(verts / tol).astype(np.int64)
    _, first, inverse = np.unique(quantised, axis=0, return_index=True,
                                  return_inverse=True)
    welded = verts[first]
    remapped = inverse[faces]
    keep = ~((remapped[:, 0] == remapped[:, 1])
             | (remapped[:, 1] == remapped[:, 2])
             | (remapped[:, 0] == remapped[:, 2]))
    return welded, remapped[keep], int((~keep).sum())


def edge_counts(faces):
    """(boundary, over-shared, misoriented). All zero = watertight manifold."""
    a, b, c = faces[:, 0], faces[:, 1], faces[:, 2]
    directed = np.concatenate([np.stack([a, b], 1), np.stack([b, c], 1),
                               np.stack([c, a], 1)])
    undirected = np.sort(directed, axis=1)
    _, und = np.unique(undirected, axis=0, return_counts=True)
    _, dir_ = np.unique(directed, axis=0, return_counts=True)
    return int((und == 1).sum()), int((und > 2).sum()), int((dir_ > 1).sum())


def signed_volume(verts, faces):
    """Divergence theorem. A closed surface with outward winding gives the
    enclosed volume; a shell gives the volume of its material, not its hollow."""
    a, b, c = verts[faces[:, 0]], verts[faces[:, 1]], verts[faces[:, 2]]
    return float(np.einsum("ij,ij->i", a, np.cross(b, c)).sum() / 6.0)


def surface_area(verts, faces):
    a, b, c = verts[faces[:, 0]], verts[faces[:, 1]], verts[faces[:, 2]]
    return float(np.linalg.norm(np.cross(b - a, c - a), axis=1).sum() / 2.0)


def components(n_vertices, faces):
    """Union-find over face-connected vertices → per-face component label."""
    parent = np.arange(n_vertices)

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    for tri in faces:
        r0, r1, r2 = find(tri[0]), find(tri[1]), find(tri[2])
        parent[r1] = r0
        parent[r2] = r0
    roots = np.array([find(v) for v in faces[:, 0]])
    order = {r: i for i, r in enumerate(dict.fromkeys(roots.tolist()))}
    return np.array([order[r] for r in roots]), len(order)


def sub_mesh(verts, faces, mask):
    sel = faces[mask]
    used = np.unique(sel)
    remap = {u: k for k, u in enumerate(used.tolist())}
    return verts[used], np.array([[remap[i] for i in tri] for tri in sel])


# ── ray casting ───────────────────────────────────────────────────────────

def ray_hits(origin, direction, tris, eps=1e-12):
    """Sorted distances at which a ray crosses a surface (Möller–Trumbore).

    Deduplicated by distance: a ray through the shared edge of two triangles
    registers on both, and one wall must count once.
    """
    v0, v1, v2 = tris[:, 0], tris[:, 1], tris[:, 2]
    e1, e2 = v1 - v0, v2 - v0
    h = np.cross(direction, e2)
    a = np.einsum("ij,ij->i", e1, h)
    live = np.abs(a) > eps
    f = np.zeros_like(a)
    f[live] = 1.0 / a[live]
    s = origin - v0
    u = f * np.einsum("ij,ij->i", s, h)
    q = np.cross(s, e1)
    v = f * (q @ direction)
    t = f * np.einsum("ij,ij->i", e2, q)
    hit = (live & (u >= -1e-9) & (v >= -1e-9)
           & (u + v <= 1 + 1e-9) & (t > 1e-6))
    if not hit.any():
        return np.empty(0)
    return np.unique(np.round(t[hit], 4))


def fibonacci_directions(n):
    """Near-uniform directions on the sphere, deliberately not axis-aligned so
    rays do not run along the symmetry planes modelled geometry tends to have."""
    k = np.arange(n)
    y = 1.0 - (k / max(n - 1, 1)) * 2.0
    r = np.sqrt(np.maximum(0.0, 1.0 - y * y))
    golden = math.pi * (3.0 - math.sqrt(5.0))
    return np.stack([np.cos(golden * k) * r, y, np.sin(golden * k) * r], 1)


# ── plane section ─────────────────────────────────────────────────────────

def plane_segments(verts, faces, axis, level):
    """Every segment where the mesh crosses the plane `axis = level`.

    Returns segments in the plane's own 2-D coordinates, plus the names of the
    two axes retained, so a caller can label the drawing honestly.
    """
    keep = [i for i in range(3) if i != axis]
    tris = verts[faces]
    d = tris[:, :, axis] - level
    positive = d > 0
    n_pos = positive.sum(axis=1)
    crossing = (n_pos == 1) | (n_pos == 2)
    tris, d, positive = tris[crossing], d[crossing], positive[crossing]

    segs = []
    for tri, dd, pp in zip(tris, d, positive):
        pts = []
        for i in range(3):
            j = (i + 1) % 3
            if pp[i] != pp[j]:
                w = dd[i] / (dd[i] - dd[j])
                p = tri[i] + w * (tri[j] - tri[i])
                pts.append((p[keep[0]], p[keep[1]]))
        if len(pts) == 2:
            segs.append(pts)
    return segs, keep


def loops_closed(segs, tol=1e-4):
    """Do the segments form closed loops? Returns the count of open ends.

    Zero means an even-odd fill is trustworthy. Anything else means the section
    has open ends and a filled picture would be inventing a boundary.
    """
    ends = defaultdict(int)
    for a, b in segs:
        ends[(round(a[0] / tol), round(a[1] / tol))] += 1
        ends[(round(b[0] / tol), round(b[1] / tol))] += 1
    return sum(1 for v in ends.values() if v % 2 == 1)


def write_svg(path, segs, axis_names, level, title, size=900, pad=0.06):
    """Draw the section: filled by even-odd, outlined so the fill is checkable."""
    pts = np.array([p for seg in segs for p in seg], dtype=np.float64)
    lo, hi = pts.min(axis=0), pts.max(axis=0)
    span = float((hi - lo).max()) * (1 + pad * 2) or 1.0
    centre = (lo + hi) / 2
    scale = size / span

    def px(p):
        return ((p[0] - centre[0]) * scale + size / 2,
                size / 2 - (p[1] - centre[1]) * scale)

    # Chain segments into paths so the even-odd fill has real subpaths.
    adjacency = defaultdict(list)
    key = lambda p: (round(p[0], 4), round(p[1], 4))          # noqa: E731
    for a, b in segs:
        adjacency[key(a)].append((key(b), b))
        adjacency[key(b)].append((key(a), a))
    seen, paths = set(), []
    for a, b in segs:
        start = key(a)
        if start in seen:
            continue
        chain, current, point = [a], start, a
        seen.add(start)
        while True:
            nxt = None
            for k, p in adjacency[current]:
                if k not in seen:
                    nxt = (k, p)
                    break
            if nxt is None:
                break
            seen.add(nxt[0])
            chain.append(nxt[1])
            current, point = nxt
        if len(chain) > 2:
            paths.append(chain)

    # Every loop is a SUBPATH of one path, not a path of its own. The even-odd
    # rule only cancels within a single path element, and that cancellation is
    # the whole point: it is what turns an enclosed lumen into a hole instead
    # of a second filled blob sitting on top of the wall.
    subpaths = []
    for chain in paths:
        pts = " L ".join(f"{px(p)[0]:.2f},{px(p)[1]:.2f}" for p in chain)
        subpaths.append(f"M {pts} Z")
    body = f'<path fill-rule="evenodd" d="{" ".join(subpaths)}"/>'

    header = (f'{title} — section at {axis_names[0]} = {level:.1f}, '
              f'{len(segs)} segments, {len(paths)} loops')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size + 34}" viewBox="0 0 {size} {size + 34}">
<rect width="100%" height="100%" fill="#faf8f5"/>
<text x="12" y="21" font-family="-apple-system,sans-serif" font-size="13" fill="#201e22">{header}</text>
<g transform="translate(0,34)" fill="#C4685F" stroke="#8d3f38" stroke-width="1.1">
{body}
</g>
</svg>
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return len(paths)


# ── commands ──────────────────────────────────────────────────────────────

def cmd_report(args):
    print(f"{'element':10} {'tris':>8} {'verts':>8} {'shells':>7} "
          f"{'watertight':>16} {'volume':>14} {'area':>12}  bbox span")
    print("─" * 120)
    for ref in args.refs:
        try:
            v, f = load(args.obj_dir, [ref])
        except FileNotFoundError as error:
            print(f"{ref:10} NOT FOUND — no such file: {error}")
            continue
        except ValueError as error:
            print(f"{ref:10} UNREADABLE — {error}")
            continue
        vw, fw, degenerate = weld(v, f)
        b, o, m = edge_counts(fw)
        _, n_shells = components(len(vw), fw)
        span = vw.max(axis=0) - vw.min(axis=0)
        flag = "YES" if (b == 0 and o == 0 and m == 0) else f"no b{b}/o{o}/m{m}"
        print(f"{ref:10} {len(fw):8,} {len(vw):8,} {n_shells:7} {flag:>16} "
              f"{signed_volume(vw, fw):14,.0f} {surface_area(vw, fw):12,.0f}  "
              f"{span[0]:.1f}×{span[1]:.1f}×{span[2]:.1f}"
              + (f"   [{degenerate} degenerate dropped]" if degenerate else ""))
    print("\nVolume is of the MATERIAL, not the hollow: a shell reports the "
          "volume of\nits wall, a solid cast reports the volume it fills. That "
          "difference is\nusually the fastest way to tell which one you have.")
    return 0


def cmd_probe(args):
    wall_v, wall_f = load(args.obj_dir, args.wall)
    cav_v, cav_f = load(args.obj_dir, args.cavity)
    wall_tris, cav_tris = wall_v[wall_f], cav_v[cav_f]
    origin = cav_v.mean(axis=0)

    exits, covered, thickness, gaps = 0, 0, [], []
    for d in fibonacci_directions(args.rays):
        cav = ray_hits(origin, d, cav_tris)
        if len(cav) == 0:
            continue
        exits += 1
        r_endo = cav[-1]
        beyond = ray_hits(origin, d, wall_tris)
        beyond = beyond[beyond > r_endo - args.tolerance]
        if len(beyond) >= 2:
            covered += 1
            thickness.append(beyond[1] - beyond[0])   # FIRST segment only
            gaps.append(beyond[0] - r_endo)

    coverage = 100.0 * covered / max(exits, 1)
    print(f"wall    {'+'.join(args.wall)}")
    print(f"cavity  {'+'.join(args.cavity)}")
    print(f"\n  rays leaving the cavity      {exits}/{args.rays}")
    print(f"  ANGULAR COVERAGE by the wall {coverage:.1f}%  "
          f"({covered} of {exits} directions meet wall outside the cavity)")
    if thickness:
        t, g = np.array(thickness), np.array(gaps)
        print(f"  wall thickness               median {np.median(t):.2f}   "
              f"IQR {np.percentile(t, 25):.2f}–{np.percentile(t, 75):.2f}")
        print(f"  gap, cavity skin to wall     median {np.median(g):.2f}  "
              f"(≈0 means the wall hugs the lumen)")
    verdict = ("ENCLOSING SHELL — a real wall around a real void"
               if coverage > 75 else
               "PARTIAL COVER — a wall over part of the chamber only"
               if coverage > 25 else
               "SCATTERED LUMPS — this is not a wall, whatever it is called")
    print(f"\n  → {verdict}")
    return 0


def cmd_clean(args):
    v, f = load(args.obj_dir, [args.ref])
    vw, fw, _ = weld(v, f)
    volume_in = signed_volume(vw, fw)
    labels, n = components(len(vw), fw)

    keep, dropped_volume, dropped_tris = [], 0.0, 0
    for i in range(n):
        mask = labels == i
        sv, sf = sub_mesh(vw, fw, mask)
        volume = signed_volume(sv, sf)
        if abs(volume) >= args.min_volume:
            keep.append(fw[mask])
        else:
            dropped_volume += abs(volume)
            dropped_tris += int(mask.sum())

    if not keep:
        print(f"❌ every component is below {args.min_volume} — nothing to keep.")
        return 1

    faces = np.vstack(keep)
    used = np.unique(faces)
    remap = {u: k for k, u in enumerate(used.tolist())}
    verts = vw[used]
    faces = np.array([[remap[i] for i in tri] for tri in faces])
    b, o, m = edge_counts(faces)

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(f"# {args.ref}: components under {args.min_volume} removed.\n")
        fh.write("# Mesh repair only — components deleted, nothing added, "
                 "moved or thickened.\n")
        fh.write(f"o {args.ref}\n")
        for x, y, z in verts:
            fh.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for tri in faces:
            fh.write(f"f {tri[0]+1} {tri[1]+1} {tri[2]+1}\n")

    share = 100 * dropped_volume / abs(volume_in) if volume_in else 0.0
    print(f"  in       {len(fw):,} triangles, volume {volume_in:,.1f}")
    print(f"  dropped  {dropped_tris:,} triangles, volume {dropped_volume:,.3f} "
          f"({share:.4f}% of the volume)")
    print(f"  out      {len(faces):,} triangles, volume "
          f"{signed_volume(verts, faces):,.1f}")
    print(f"  watertight now: "
          f"{'YES' if (b == 0 and o == 0 and m == 0) else f'no b{b}/o{o}/m{m}'}")
    print(f"  wrote    {args.out}")
    if share > 0.5:
        print("\n  ⚠️  More than half a percent of the volume went. That is too "
              "much to\n      call junk — inspect the dropped components before "
              "trusting this.")
    return 0


def cmd_section(args):
    v, f = load(args.obj_dir, [args.ref])
    vw, fw, _ = weld(v, f)
    axis = {"x": 0, "y": 1, "z": 2}[args.axis]
    lo, hi = float(vw[:, axis].min()), float(vw[:, axis].max())
    level = args.level if args.level is not None else lo + (hi - lo) * args.at

    segs, keep = plane_segments(vw, fw, axis, level)
    if not segs:
        print(f"❌ the plane {args.axis} = {level:.2f} misses the mesh "
              f"({args.axis} runs {lo:.1f} to {hi:.1f}).")
        return 1
    open_ends = loops_closed(segs)
    names = ["x", "y", "z"]
    print(f"  {args.ref} spans {args.axis} {lo:.1f} → {hi:.1f}")
    print(f"  section at {args.axis} = {level:.2f}: {len(segs)} segments, "
          f"{open_ends} open ends")
    if open_ends:
        print("  ⚠️  Open ends: the intersection is not closed loops, so the "
              "filled\n      region is not reliable. Trust the outline, not the "
              "fill.")
    n_paths = write_svg(args.out, segs, (args.axis, names[keep[0]]), level,
                        args.ref)
    print(f"  wrote {args.out} — {n_paths} closed path(s)")
    print("\n  Open it in a browser. Filled = material; holes = genuine voids "
          "in the\n  mesh. This is the cross-section validate_specimen_glb.py "
          "asks a human\n  to make, and it is the evidence for its interior "
          "gate.")
    return 0


# ── entry ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="inspect_source_mesh.py",
        description="Ask what a source mesh actually is, before it becomes a "
                    "specimen.")
    subs = parser.add_subparsers(dest="command", required=True)

    p = subs.add_parser("report", help="triangles, shells, watertightness, "
                                       "volume and bounds per element")
    p.add_argument("obj_dir")
    p.add_argument("refs", nargs="+")
    p.set_defaults(func=cmd_report)

    p = subs.add_parser("probe", help="does a candidate wall enclose a cavity, "
                                      "and how thick is it?")
    p.add_argument("obj_dir")
    p.add_argument("--wall", nargs="+", required=True)
    p.add_argument("--cavity", nargs="+", required=True)
    p.add_argument("--rays", type=int, default=300)
    p.add_argument("--tolerance", type=float, default=1.0,
                   help="how far inside the cavity skin still counts as wall "
                        "(source units, default 1.0)")
    p.set_defaults(func=cmd_probe)

    p = subs.add_parser("clean", help="drop zero-volume junk components")
    p.add_argument("obj_dir")
    p.add_argument("ref")
    p.add_argument("out")
    p.add_argument("--min-volume", type=float, default=100.0,
                   help="components below this volume are dropped "
                        "(source units cubed, default 100)")
    p.set_defaults(func=cmd_clean)

    p = subs.add_parser("section", help="write a true cross-section as SVG")
    p.add_argument("obj_dir")
    p.add_argument("ref")
    p.add_argument("out")
    p.add_argument("--axis", choices=["x", "y", "z"], default="z")
    p.add_argument("--at", type=float, default=0.5,
                   help="fraction along the axis, 0 to 1 (default 0.5)")
    p.add_argument("--level", type=float, default=None,
                   help="absolute coordinate; overrides --at")
    p.set_defaults(func=cmd_section)

    args = parser.parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError) as error:
        print(f"❌ {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
