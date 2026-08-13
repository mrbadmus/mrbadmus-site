#!/usr/bin/env python3
"""3D Studio — derive hotspot position3d from the specimen's own geometry.

Run it:

    python3 tools/derive_anchors.py heart              # report only
    python3 tools/derive_anchors.py heart --write      # patch content/heart.json

Why a tool and not a spreadsheet
--------------------------------
`position3d` is not authored content. It is a fact about the mesh, and the mesh
is the thing that changes when a specimen is re-acquired or re-decimated. Doing
it by hand means fourteen numbers a human guessed against a model they were
rotating by eye, which nobody can check and which silently rots the next time
the GLB is rebuilt. This reads the shipped GLB and derives the numbers, so they
can always be regenerated and always agree with what actually renders.

It never touches a science string. Labels, detail, accepted answers and spec
points are Mide's under the science gate; this writes `position3d` and nothing
else.

The rule
--------
**A hotspot's anchor is the nearest point on the specimen's outer surface,
over that structure, THAT A CAMERA CAN ACTUALLY SEE.**

Not the centroid. The centroid of a chamber is inside the chamber, and
renderer/mesh/project.ts tests occlusion with a real raycast — an anchor buried
under the heart wall is occluded from every angle, so its dot would never draw
and the structure could never be asked about.

Not the nearest outer-surface point either, which is the version this tool
shipped first and which was wrong in a way worth recording. Every candidate it
chose was genuinely on the outer surface, and seven of the heart's fourteen
anchors were still invisible from all sixteen views sampled. A heart is deeply
concave: the crevices between the atria, the great vessels and the draped
coronary tree are outer surface in the strict sense and are enclosed from
almost every direction. Raising the surface lift ten-fold barely moved the
number, because the anchor was not sitting too low — it was sitting in a slot.

So candidates are put to the renderer's own occlusion test, and have to pass
it TWICE.

First, from the one direction the FRAMING MOVE will use. renderer/mesh/
framing.ts turns the camera to `target + normalise(anchor - target) * distance`
when a retrieval question is presented, and now also when a student picks a
structure from the panel. An anchor that direction cannot see is an anchor the
studio turns towards and still shows nothing — which is what happened to the
pulmonary artery, whose trunk sits under the aortic arch, until this became a
gate rather than a preference.

Then, from the arc a student can actually orbit through by hand, and the
best-scoring of the framing-clean candidates wins. Both halves are needed: an
earlier version that took simply the NEAREST framing-clean candidate left the
left ventricle visible from 1 of 36 camera positions and the coronary arteries
from none. A dot only a button can reveal is half a dot.

The dot still sits over its structure, and the report prints how far out it had
to go and how many views can see it — the numbers to look at if one lands
somewhere surprising.

For a surface structure — the coronary arteries, the aorta — the anchor lands
on the structure itself. For a buried one — the valves — it lands on the wall
over the valve, which is the compromise already ruled for the sino-atrial node:
a hotspot needs a coordinate, not its own mesh part.

Structures with no mesh part of their own (the septum, the sino-atrial node)
are anchored from a `derivedFrom` rule in tools/recipes/<name>.anchors.json,
which names the parts whose geometry locates them. Those rules are anatomy, so
they are written down and reviewable rather than computed from nothing.

How the outer surface is found
------------------------------
Rays are cast INWARD, from well outside the specimen towards the structure's
centroid, in many directions spread evenly over the sphere; the FIRST surface
each ray meets is the outer boundary as seen from that direction. Casting
outward from the centroid and taking the last exit is NOT the same thing on a
specimen made of separate closed parts, and finds the face pointing at a
neighbour rather than the face pointing at the world.

Needs numpy and DracoPy, exactly as validate_specimen_glb.py does, and reuses
its GLB parsing so both read the shipped file the same way.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
sys.path.insert(0, STUDIO)

from validate_specimen_glb import (  # noqa: E402
    HAVE_DRACO, parse_glb, buffer_view_bytes, read_accessor,
)

if HAVE_DRACO:
    import DracoPy  # noqa: E402

# Matches SURFACE_LIFT in src/renderer/mesh/anchors.ts. The renderer applies
# this itself only to its stand-in anchors; an authored position is used raw,
# so an authored one has to arrive already lifted or the surface it sits on
# reads as the thing occluding it.
SURFACE_LIFT = 0.006

# DEPTH_TOLERANCE in renderer/mesh/project.ts: how much nearer than the anchor
# a hit must be before it counts as occluding. Mirrored here so the scoring
# below asks exactly the question the renderer will ask at run time.
OCCLUSION_TOLERANCE = 0.02

# Directions sampled when looking for the outer surface. 1024 spreads to
# about 3.5° apart, which is finer than the features being resolved.
SPHERE_SAMPLES = 1024

# How many of those, nearest first, are scored for visibility. It has to be
# generous: a structure can be wholly buried where it is thickest and only
# reachable along a limb of itself. The pulmonary artery is the case that set
# this number — its trunk sits under the aortic arch, so no candidate within
# the nearest hundred cleared the radial line the framing move uses, and the
# first that did was out on the left pulmonary artery.
CANDIDATES = 384

# How many framing-clean candidates are collected before the full visibility
# score picks between them. Enough choice to find open surface, few enough that
# the scoring pass stays under a second per structure.
FRAMED_POOL = 24

# How many candidates are scored when NONE of them frames cleanly. Only the
# fallback path pays this, and only for a structure that has no clear radial
# line at all.
FALLBACK_CANDIDATES = 64

# Camera positions per elevation band, and how far out they sit as a multiple
# of the bounding radius. FRAMING_MARGIN in renderer/mesh/anchors.ts puts the
# real camera at about this distance.
CAMERA_AZIMUTHS = 12
CAMERA_DISTANCE = 2.6


# ── geometry, per named part ──────────────────────────────────────────────

def part_geometry(path):
    """{node name: (positions, faces)} from a GLB, keeping parts separate.

    validate_specimen_glb.extract_geometry concatenates every primitive,
    because a watertight check does not care which part a triangle came from.
    Here the part IS the question."""
    gltf, bin_chunk = parse_glb(path)
    glb_dir = os.path.dirname(os.path.abspath(path))
    out = {}
    for node in gltf.get("nodes", []):
        if "mesh" not in node:
            continue
        name = node.get("name") or f"mesh{node['mesh']}"
        chunks_v, chunks_f, base = [], [], 0
        for prim in gltf["meshes"][node["mesh"]].get("primitives", []):
            if prim.get("mode", 4) != 4:
                continue
            draco = prim.get("extensions", {}).get(
                "KHR_draco_mesh_compression")
            if draco is not None:
                if not HAVE_DRACO:
                    raise RuntimeError(
                        "the specimen is Draco-compressed and DracoPy is not "
                        "installed — run `pip install DracoPy`")
                src, start, length, _ = buffer_view_bytes(
                    gltf, bin_chunk, draco["bufferView"], glb_dir)
                decoded = DracoPy.decode(bytes(src[start:start + length]))
                pos = np.asarray(decoded.points, dtype=np.float64)
                faces = np.asarray(decoded.faces, dtype=np.int64)
            else:
                pos = read_accessor(
                    gltf, bin_chunk, prim["attributes"]["POSITION"],
                    glb_dir).astype(np.float64)
                faces = read_accessor(
                    gltf, bin_chunk, prim["indices"], glb_dir
                ).reshape(-1, 3).astype(np.int64)
            chunks_v.append(pos)
            chunks_f.append(faces + base)
            base += len(pos)
        if chunks_v:
            out[name] = (np.vstack(chunks_v), np.vstack(chunks_f))
    return out


def slug(name):
    """A GLB part name reduced to the form a hotspot id uses after its
    specimen prefix: "Right atrium" → "right-atrium".

    The parts are named for the class, not for this script — the isolate tool
    shows a part's name verbatim, and the renderer contract says it must be
    the asset's own word. Binding them to hotspots therefore needs this one
    reduction, and validate_content.py holds both sides to it."""
    out = []
    for ch in name.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    return "".join(out).strip("-")


def area_centroid(positions, faces):
    """Area-weighted centroid. Unweighted vertex mean would be dragged towards
    whichever region the decimator happened to leave densest."""
    a, b, c = positions[faces[:, 0]], positions[faces[:, 1]], positions[faces[:, 2]]
    areas = 0.5 * np.linalg.norm(np.cross(b - a, c - a), axis=1)
    mids = (a + b + c) / 3.0
    total = areas.sum()
    if total <= 0:
        return positions.mean(axis=0)
    return (mids * areas[:, None]).sum(axis=0) / total


def fibonacci_directions(n):
    """n roughly-even directions on the sphere."""
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    theta = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.sin(phi) * np.cos(theta),
                     np.sin(phi) * np.sin(theta),
                     np.cos(phi)], axis=1)


def inward_first_hits(centroid, directions, v0, v1, v2, start_distance):
    """Distance from `centroid` to the specimen's OUTER surface along each
    direction, by casting INWARD from well outside and taking the FIRST
    surface met. inf where a direction meets nothing.

    Inward-from-outside, not outward-from-inside. Casting outward and taking
    the last exit finds the nearest surface, which is not the same thing and
    was wrong here: the specimen is twelve separate closed parts, not one
    solid, so the nearest surface to a structure wedged between its
    neighbours is the face pointing AT a neighbour. Anchors derived that way
    landed in the gaps between the chambers — geometrically just outside their
    own part, and inside the heart, so occluded from every camera angle. Seven
    of the heart's fourteen were invisible from all sixteen views sampled, and
    raising the surface lift ten-fold barely moved it, because the anchor was
    not near the outside at all.

    The first surface a ray meets on its way in is the outer boundary as seen
    from that direction, by definition. Anchoring there means a camera looking
    along that direction can always see the dot. It is also what
    renderer/mesh/anchors.ts does for its own stand-in anchors — "the raycast
    that places them starts outside the form and stops at the first surface it
    meets" — so the two now agree about what "on the surface" means.

    Möller–Trumbore, vectorised over triangles, chunked over directions so
    memory stays bounded whatever the triangle count."""
    e1, e2 = v1 - v0, v2 - v0
    out = np.full(len(directions), np.inf)

    # h is (K,T,3), so K is chunked to keep that array in the tens of MB.
    chunk = max(1, 4_000_000 // max(len(v0), 1))
    for start in range(0, len(directions), chunk):
        dirs = directions[start:start + chunk]
        origins = centroid + dirs * start_distance
        rays = -dirs
        h = np.cross(rays[:, None, :], e2[None, :, :])
        a = np.einsum('tj,ktj->kt', e1, h)
        ok = np.abs(a) > 1e-12
        f = np.zeros_like(a)
        np.divide(1.0, a, out=f, where=ok)
        s = origins[:, None, :] - v0[None, :, :]
        u = f * np.einsum('ktj,ktj->kt', s, h)
        q = np.cross(s, e1[None, :, :])
        v = f * np.einsum('kj,ktj->kt', rays, q)
        t = f * np.einsum('tj,ktj->kt', e2, q)
        hit = (ok & (u >= -1e-9) & (v >= -1e-9)
               & (u + v <= 1 + 1e-9) & (t > 1e-9))
        # FIRST hit: the smallest t along the inward ray. Reported as a
        # distance from the centroid, not from the ray's origin.
        out[start:start + len(dirs)] = (
            start_distance - np.where(hit, t, np.inf).min(axis=1))
    return out


def blocked(origin, direction, max_t, v0, v1, v2):
    """True when any triangle lies between `origin` and `max_t` along the ray.
    The same question renderer/mesh/project.ts asks of the camera."""
    e1, e2 = v1 - v0, v2 - v0
    h = np.cross(direction, e2)
    a = np.einsum('tj,tj->t', e1, h)
    ok = np.abs(a) > 1e-12
    f = np.zeros_like(a)
    np.divide(1.0, a, out=f, where=ok)
    s = origin - v0
    u = f * np.einsum('tj,tj->t', s, h)
    q = np.cross(s, e1)
    v = f * (q @ direction)
    t = f * np.einsum('tj,tj->t', e2, q)
    return bool(np.any(ok & (u >= -1e-9) & (v >= -1e-9)
                       & (u + v <= 1 + 1e-9) & (t > 1e-9) & (t < max_t)))


def camera_directions(n):
    """Where a student actually looks from. The controls orbit in azimuth with
    a modest elevation, so visibility is scored over that band rather than the
    whole sphere — an anchor only a bird could see is no use in a lesson."""
    out = []
    for elevation in (-0.25, 0.15, 0.55):
        for k in range(n):
            angle = 2 * np.pi * k / n
            d = np.array([np.sin(angle), elevation, np.cos(angle)])
            out.append(d / np.linalg.norm(d))
    return np.stack(out)


def visible_from(point, centre, radius, cameras, v0, v1, v2, tolerance):
    """How many of `cameras` can see `point`, by the renderer's own test."""
    seen = 0
    for direction in cameras:
        eye = centre + direction * radius * CAMERA_DISTANCE
        to_point = point - eye
        distance = float(np.linalg.norm(to_point))
        if distance <= tolerance:
            continue
        if not blocked(eye, to_point / distance, distance - tolerance,
                       v0, v1, v2):
            seen += 1
    return seen


def best_anchor(centroid, all_v0, all_v1, all_v2, directions, start_distance,
                centre, radius, cameras, lift, tolerance):
    """The outer-surface point over this structure that a camera can actually
    see, preferring the nearest such point.

    NEAREST ALONE IS NOT ENOUGH, which cost a rebuild to learn. Every
    candidate here is on the outer surface by construction, so nearest-first
    looked right — and put seven of the heart's fourteen anchors where no
    camera could see them. A heart is deeply concave: the crevices between the
    atria, the great vessels and the draped coronary tree are outer surface in
    the strict sense, visible from one narrow cone and enclosed from every
    other. Raising the surface lift ten-fold barely moved it, because the
    anchor was not sitting too low, it was sitting in a slot.

    So the candidates are SCORED by the renderer's own occlusion test, over
    the arc a student can actually orbit through, and the winner is the
    closest candidate among the best-scoring ones. The dot still sits over its
    structure — the distance is reported, and a structure whose only visible
    surface is far from it is exactly the thing worth seeing in the report.
    """
    dists = inward_first_hits(centroid, directions, all_v0, all_v1, all_v2,
                              start_distance)
    finite = np.isfinite(dists)
    if not finite.any():
        return None, None, None, 0

    # Nearest by MAGNITUDE. A negative distance is not a mistake: it means the
    # surface facing that direction lies behind the centroid, which happens
    # whenever the centroid is not inside its own structure — the coronary
    # arteries' centroid sits in the space the vessels wrap around, and the
    # septum's rule puts its point between two chamber cavities.
    magnitude = np.where(finite, np.abs(dists), np.inf)
    order = np.argsort(magnitude)[:CANDIDATES]

    # THE FRAMED VIEW HAS TO WORK, and it is one specific direction.
    #
    # renderer/mesh/framing.ts puts the camera at
    # `target + normalise(anchor - target) * distance` — the radial line from
    # the orbit target through the anchor. That is where the camera goes when a
    # retrieval question is presented, and now also when a student picks a
    # structure from the panel. An anchor visible from eleven of thirty-six
    # sampled views but NOT from its own radial one is an anchor the framing
    # move turns towards and still cannot see: exactly what happened to the
    # pulmonary artery, whose trunk sits under the aortic arch.
    #
    # It is therefore the FIRST question asked of each candidate, and it costs
    # one ray. Scoring all 36 camera views for every candidate before the cheap
    # gate made the pass over 384 candidates take longer than the whole rest of
    # the pipeline; this way the full score is computed once, for the winner.
    everything, framing_clean = [], []
    for index in order:
        if not np.isfinite(magnitude[index]):
            break
        direction = directions[index]
        point = centroid + direction * dists[index] + direction * lift
        radial = point - centre
        length = float(np.linalg.norm(radial))
        candidate = (point, float(magnitude[index]), direction)
        everything.append(candidate)
        if length > 1e-9 and visible_from(
                point, centre, radius, (radial / length)[None, :],
                all_v0, all_v1, all_v2, tolerance) == 1:
            framing_clean.append(candidate)
            if len(framing_clean) >= FRAMED_POOL:
                break

    if not everything:
        return None, None, None, (0, 0)

    # BOTH THINGS MATTER, so both are asked, in the order that costs least.
    #
    # Taking simply the nearest candidate that frames cleanly was the first
    # version and it was not good enough: framing worked for all fourteen, but
    # free rotation showed almost nothing — the left ventricle was visible from
    # 1 of 36 camera positions and the coronary arteries from none. A dot only
    # a button can reveal is half a dot; a student turning the specimen by hand
    # must be able to find it.
    #
    # So the cheap gate collects a POOL of framing-clean candidates, and the
    # full 36-view score picks the winner from inside that pool. `order` is
    # sorted by distance, so max() breaking ties on the first entry keeps the
    # nearest of equals.
    pool = framing_clean or everything[:FALLBACK_CANDIDATES]
    scored = [(visible_from(c[0], centre, radius, cameras,
                            all_v0, all_v1, all_v2, tolerance), -i, c)
              for i, c in enumerate(pool)]
    score, _, (point, distance, direction) = max(scored)
    return point, distance, direction, (1 if framing_clean else 0, score)


# ── entry ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="derive_anchors.py",
        description="Derive hotspot position3d from a specimen's own GLB.")
    parser.add_argument("specimen", help="specimen id, e.g. heart")
    parser.add_argument("--write", action="store_true",
                        help="patch position3d into the content record")
    args = parser.parse_args()

    record_path = os.path.join(STUDIO, "content", f"{args.specimen}.json")
    with open(record_path, encoding="utf-8") as fh:
        record = json.load(fh)
    glb = os.path.join(STUDIO, "public", "assets", f"{args.specimen}.glb")
    if not os.path.isfile(glb):
        print(f"❌ no mesh on disk: {glb}")
        return 2

    rules_path = os.path.join(HERE, "recipes", f"{args.specimen}.anchors.json")
    rules = {}
    if os.path.isfile(rules_path):
        with open(rules_path, encoding="utf-8") as fh:
            rules = {r["hotspot"]: r for r in json.load(fh)["anchors"]}

    parts = {slug(name): geom for name, geom in part_geometry(glb).items()}
    every_v = np.vstack([p[0] for p in parts.values()])
    faces_all, base = [], 0
    for positions, faces in parts.values():
        faces_all.append(faces + base)
        base += len(positions)
    every_f = np.vstack(faces_all)
    v0, v1, v2 = every_v[every_f[:, 0]], every_v[every_f[:, 1]], every_v[every_f[:, 2]]

    lo, hi = every_v.min(axis=0), every_v.max(axis=0)
    radius = float(np.linalg.norm(hi - lo) / 2)
    lift = radius * SURFACE_LIFT
    # The band renderer/mesh/project.ts ignores when it asks what is in front
    # of an anchor. An anchor has to clear this to be seen past its own
    # surface, and it is the number the scoring below must agree with.
    tolerance = max(radius * OCCLUSION_TOLERANCE, 1e-4)
    directions = fibonacci_directions(SPHERE_SAMPLES)
    cameras = camera_directions(CAMERA_AZIMUTHS)
    centre = (lo + hi) / 2.0

    print(f"3D Studio — deriving anchors for '{args.specimen}'")
    print(f"  {len(parts)} mesh part(s), bounding radius {radius:.4f}, "
          f"surface lift {lift:.5f}, {len(cameras)} camera views\n")

    derived, unresolved, unframed = {}, [], []
    for hotspot in record["hotspots"]:
        key = hotspot["id"].split(".", 1)[1]
        rule = rules.get(hotspot["id"])
        if key in parts:
            source = [key]
        elif rule and rule.get("derivedFrom"):
            source = [s for s in rule["derivedFrom"] if s in parts]
        else:
            source = []

        if not source:
            unresolved.append(hotspot["id"])
            print(f"  ⚠️  {hotspot['id']:26} no mesh part and no anchor rule "
                  f"— left unauthored")
            continue

        weights = (rule or {}).get("weights")
        centroids = np.stack([area_centroid(*parts[s]) for s in source])
        if weights and len(weights) == len(source):
            w = np.asarray(weights, dtype=np.float64)
            centroid = (centroids * w[:, None]).sum(axis=0) / w.sum()
        else:
            centroid = centroids.mean(axis=0)
        if (rule or {}).get("offset"):
            centroid = centroid + np.asarray(rule["offset"]) * radius

        point, distance, normal, rank = best_anchor(
            centroid, v0, v1, v2, directions, radius * 3.0,
            centre, radius, cameras, lift, tolerance)
        if point is None:
            unresolved.append(hotspot["id"])
            print(f"  ⚠️  {hotspot['id']:26} no outer surface found — left "
                  f"unauthored")
            continue
        derived[hotspot["id"]] = [round(float(c), 5) for c in point]
        via = "own part" if key in parts else "rule: " + "+".join(source)
        framed, score = rank
        mark = "✅" if framed and score else "⚠️ "
        print(f"  {mark} {hotspot['id']:26} {np.round(point, 4)}  "
              f"{distance / radius * 100:3.0f}% out · seen from "
              f"{score}/{len(cameras)} views · framed view "
              f"{'OK' if framed else 'BLOCKED'}  [{via}]")
        if not framed:
            unframed.append(hotspot["id"])

    orphans = sorted(set(parts) - {h["id"].split(".", 1)[1]
                                   for h in record["hotspots"]})
    if orphans:
        print(f"\n  ⚠️  mesh parts with no hotspot: {', '.join(orphans)}")

    print(f"\n  {len(derived)} derived, {len(unresolved)} unresolved"
          + (f" ({', '.join(unresolved)})" if unresolved else ""))
    if unframed:
        print(f"  ⚠️  the framing move cannot reveal: {', '.join(unframed)} — "
              f"selecting one of these from the panel, or being asked about it "
              f"in a round, will turn the camera and still show nothing")

    if args.write:
        for hotspot in record["hotspots"]:
            if hotspot["id"] in derived:
                hotspot["position3d"] = derived[hotspot["id"]]
        with open(record_path, "w", encoding="utf-8") as fh:
            json.dump(record, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"  wrote position3d for {len(derived)} hotspot(s) "
              f"into content/{args.specimen}.json")
    else:
        print("  (report only — pass --write to patch the content record)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
