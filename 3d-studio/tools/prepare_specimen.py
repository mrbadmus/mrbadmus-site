#!/usr/bin/env python3
"""3D Studio — take a downloaded 3D model and turn it into a studio specimen.

Run it:

    python3 3d-studio/tools/prepare_specimen.py ~/Downloads/heart.glb
    python3 3d-studio/tools/prepare_specimen.py ~/Downloads/heart.glb --name heart
    python3 3d-studio/tools/prepare_specimen.py ~/Downloads/heart.glb --out /tmp/try.glb

One command, downloaded file to verdict. It runs the glTF work (Node does that,
in tools/specimen_pipeline.mjs) and then runs validate_specimen_glb.py on the
result, so the purchase gates are always applied to the file that was actually
written — never to an earlier draft, never skipped.

The plain-English walkthrough for Mide is docs/3d_studio_asset_pipeline.md at
the repo root. This docstring is the operator's version.

Formats
-------
.glb and .gltf run the whole pipeline today, on this machine, with nothing to
install. Those are glTF — the format the web renders natively, and the one the
studio loads.

.blend, .fbx, .obj, .dae, .stl and .ply are not glTF. Converting them needs
Blender, the free 3D program, which is NOT installed here. When it is missing
this script says so and stops with a non-zero exit code; it does not half-run
and leave something that looks converted. The Blender branch is written and
ready and starts working the moment Blender is installed — but it has never
executed, because there is no Blender on this machine to execute it. Treat it
as untested code until its first real run.

The way past that gap costs nothing: download the model as GLB. Sketchfab and
most model sites offer GLB directly in the download menu, and Blender itself
exports it (File ▸ Export ▸ glTF 2.0, format GLB). GLB avoids the converter
entirely.

Exit codes
----------
    0   the output was written and every mechanical purchase gate passed
    1   a purchase gate FAILED (validator's verdict)
    2   a purchase gate is UNVERIFIED, or bad usage / missing file
    3   the source format needs Blender and Blender is not installed
    4   Blender ran and the conversion to GLB failed
    5   the glTF pipeline failed (part names lost, Draco missing, unreadable)

Stdlib only. The glTF work lives in Node because the libraries that do it well
(@gltf-transform, meshoptimizer, sharp) live there; this script's job is to
sequence the steps and report honestly on what happened.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

# This script's own prints interleave with the output of the two subprocesses it
# runs, which write straight to the terminal. Without line buffering Python's
# lines arrive last, in a block, and the report reads as though the steps ran in
# the wrong order.
sys.stdout.reconfigure(line_buffering=True)

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
WORKER = os.path.join(HERE, "specimen_pipeline.mjs")
VALIDATOR = os.path.join(STUDIO, "validate_specimen_glb.py")
ASSETS = os.path.join(STUDIO, "public", "assets")

# Formats the Node pipeline reads directly.
GLTF_SUFFIXES = {".glb", ".gltf"}

# Formats that are not glTF and so need Blender to become glTF. The operator
# that reads each one lives in BLENDER_SCRIPT below, where Blender can see it.
BLENDER_SUFFIXES = {".blend", ".fbx", ".obj", ".dae", ".stl", ".ply"}

# Where a real, acquired specimen lives. vite.config.ts treats any .glb here
# whose name does NOT start with an underscore as an acquired asset, and stops
# substituting the generated test fixture on the next build.
DEFAULT_OUT_DIR = ASSETS


# ── Blender discovery ─────────────────────────────────────────────────────

def find_blender() -> str | None:
    """Blender's executable, or None. Checked at run time, every run, so the
    non-glTF branch begins working the moment Blender is installed — no edit
    to this file, no flag to set."""
    on_path = shutil.which("blender")
    if on_path:
        return on_path
    candidates = [
        "/Applications/Blender.app/Contents/MacOS/Blender",
        os.path.expanduser("~/Applications/Blender.app/Contents/MacOS/Blender"),
    ]
    # Versioned installs: /Applications/Blender 4.2.app, and the folder layout
    # some downloads use.
    candidates += sorted(glob.glob(
        "/Applications/Blender*.app/Contents/MacOS/Blender"))
    candidates += sorted(glob.glob(
        "/Applications/Blender*/Blender.app/Contents/MacOS/Blender"))
    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None


# The script Blender runs, headless. Kept as a string here rather than a file on
# disk because it is meaningless without this script, and because a stray .py in
# tools/ that only Blender can run would be a trap for the next reader.
#
# UNTESTED: no Blender on this machine. Written to be correct, not proven.
BLENDER_SCRIPT = r'''
import sys, os
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
src, dst = argv[0], argv[1]
suffix = os.path.splitext(src)[1].lower()

if suffix != ".blend":
    # Factory startup still ships the default cube, camera and light. They would
    # export as parts, and parts are what the studio's isolate tool lists, so a
    # stray "Cube" would show up in a lesson. Clear everything first.
    bpy.ops.wm.read_factory_settings(use_empty=True)

    IMPORTERS = {
        ".fbx": [("import_scene", "fbx")],
        # Blender 4.x moved OBJ/STL/PLY to the wm namespace and kept the old
        # operators only in 3.x. Try new, fall back to old.
        ".obj": [("wm", "obj_import"), ("import_scene", "obj")],
        ".dae": [("wm", "collada_import")],
        ".stl": [("wm", "stl_import"), ("import_mesh", "stl")],
        ".ply": [("wm", "ply_import"), ("import_mesh", "ply")],
    }
    imported = False
    for namespace, operator in IMPORTERS.get(suffix, []):
        group = getattr(bpy.ops, namespace, None)
        function = getattr(group, operator, None) if group else None
        if function is None:
            continue
        try:
            function(filepath=src)
            imported = True
            break
        except (AttributeError, RuntimeError, TypeError) as error:
            print("[prepare_specimen] %s.%s failed: %s"
                  % (namespace, operator, error))
    if not imported:
        print("[prepare_specimen] no importer succeeded for %s" % suffix)
        sys.exit(1)

meshes = [o for o in bpy.data.objects if o.type == "MESH"]
if not meshes:
    print("[prepare_specimen] the file contains no mesh objects")
    sys.exit(1)
print("[prepare_specimen] %d mesh object(s): %s"
      % (len(meshes), ", ".join(o.name for o in meshes)))

# export_apply bakes modifiers (subdivision, mirror) into real geometry, which
# is what the triangle gate is counting and what the renderer will draw.
# Object names become glTF node names, which is the whole point: Stage 3's
# isolate reads those names. Nothing here merges or flattens objects.
bpy.ops.export_scene.gltf(
    filepath=dst,
    export_format="GLB",
    use_selection=False,
    export_apply=True,
    export_yup=True,
    export_texture_dir="",
)
print("[prepare_specimen] exported %s" % dst)
'''


def convert_with_blender(blender: str, src: str, dst: str) -> bool:
    """Drive Blender headlessly to write `dst` as GLB. Returns success.

    UNTESTED — see the module docstring. There is no Blender on this machine, so
    this path has never run. It is written to the documented CLI contract:
    `--background` for no window, `--factory-startup` so a user's add-ons and
    preferences cannot change the result, and everything after `--` handed to
    the script rather than eaten by Blender."""
    handle, script_path = tempfile.mkstemp(suffix=".py", prefix="prepare_specimen_")
    with os.fdopen(handle, "w", encoding="utf-8") as fh:
        fh.write(BLENDER_SCRIPT)
    try:
        command = [blender, "--background", "--factory-startup"]
        if src.lower().endswith(".blend"):
            # A .blend is opened as the session file, not imported.
            command.append(src)
        command += ["--python", script_path, "--", src, dst]
        print(f"  running Blender: {' '.join(command)}\n")
        result = subprocess.run(command, check=False)
        return result.returncode == 0 and os.path.isfile(dst)
    finally:
        os.unlink(script_path)


def blender_missing_message(suffix: str) -> str:
    return f"""
  ❌ {suffix} files need Blender, and Blender is not installed on this machine.

     Blender is the free 3D modelling program — it is the only thing here that
     can read {suffix} and write the format the studio loads. Two ways forward,
     and the first is faster:

     1. DOWNLOAD THE MODEL AS GLB INSTEAD  (recommended, nothing to install)
        GLB is glTF binary — the 3D format browsers render natively, one file
        with the geometry and textures inside it. On Sketchfab the download
        menu offers "glTF (.glb)" alongside the other formats; most other model
        sites do the same. Pick that, and re-run this command on the .glb. The
        conversion step disappears entirely.

     2. INSTALL BLENDER  (free, ~1 GB)
        https://www.blender.org/download/ — download the macOS build, drag
        Blender to Applications, open it once so macOS clears the security
        prompt. This script finds it automatically after that, at
        /Applications/Blender.app, and re-running the same command will work.
        Fair warning: that conversion path has never been run on this machine
        for lack of Blender, so its first run should be checked rather than
        trusted.

        With Blender installed you could also convert by hand:
        File ▸ Open the model, then File ▸ Export ▸ glTF 2.0 (.glb/.gltf),
        set Format to "glTF Binary (.glb)", and run this script on the result.
"""


# ── steps ─────────────────────────────────────────────────────────────────

def run_pipeline(src: str, dst: str, name: str | None, report: str) -> int:
    node = shutil.which("node")
    if node is None:
        print("  ❌ Node.js is not installed or not on PATH.")
        print("     The glTF work runs in Node. Install it from https://nodejs.org")
        print("     then re-run this command.")
        return 5
    command = [node, WORKER, "--in", src, "--out", dst, "--report", report]
    if name:
        command += ["--name", name]
    # Not captured: the worker's report is the operator's report, and it should
    # appear as it happens rather than in a block at the end.
    return subprocess.run(command, check=False, cwd=STUDIO).returncode


def run_validator(path: str) -> int:
    print("\n" + "─" * 76)
    print("Purchase gates — validate_specimen_glb.py\n")
    return subprocess.run(
        [sys.executable, VALIDATOR, path], check=False, cwd=STUDIO).returncode


def summarise(report_path: str, validator_status: int) -> None:
    try:
        with open(report_path, encoding="utf-8") as fh:
            report = json.load(fh)
    except (OSError, ValueError):
        return
    print("\n" + "─" * 76)
    print("Summary\n")
    print(f"  wrote        {report['output']}")
    print(f"  triangles    {report['trianglesBefore']:,} → "
          f"{report['trianglesAfter']:,}")
    # A .gltf keeps its geometry and images in separate files beside it, so the
    # "before" figure is the small text file only. Saying so stops the summary
    # claiming an increase that did not happen.
    aside = ("  (before = the .gltf text file only; its separate data files are "
             "not counted)" if report["input"].lower().endswith(".gltf") else "")
    print(f"  size         {report['bytesBefore']:,} → {report['bytesAfter']:,} "
          f"bytes{aside}")
    print(f"  parts        {', '.join(report['parts'])}")
    print(f"  part names   {'preserved' if report['namesPreserved'] else 'CHANGED'}")
    verdict = {
        0: "every mechanical gate passed",
        1: "a gate FAILED — see the ❌ line above",
        2: "a gate could not be verified — treat it as not yet cleared",
    }.get(validator_status, f"validator exited {validator_status}")
    print(f"  gates        {verdict}")
    print("""
  Still to do by hand, whatever the gates said:
    • cut a cross-section and confirm the interior structure is really
      modelled (the validator prints this as HUMAN CHECK REQUIRED and can
      never decide it for you)
    • record the licence and the source URL in the specimen record —
      content/<specimen>.json, assets.licence / assets.source / assets.acquired
""")


# ── entry ─────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="prepare_specimen.py",
        description="Convert a downloaded 3D model into a studio specimen GLB "
                    "and run the purchase gates on it.")
    parser.add_argument("source", help="the downloaded model file")
    parser.add_argument("--out", default=None,
                        help="output .glb path (default: "
                             "public/assets/<name>.glb)")
    parser.add_argument("--name", default=None,
                        help="specimen id, e.g. heart (default: the source "
                             "file's name)")
    args = parser.parse_args()

    src = os.path.abspath(os.path.expanduser(args.source))
    if not os.path.isfile(src):
        print(f"❌ file not found: {src}")
        return 2

    suffix = os.path.splitext(src)[1].lower()
    name = args.name or os.path.splitext(os.path.basename(src))[0]
    out = (os.path.abspath(os.path.expanduser(args.out)) if args.out
           else os.path.join(DEFAULT_OUT_DIR, f"{name}.glb"))

    print(f"3D Studio — preparing {os.path.basename(src)} as specimen '{name}'\n")

    if suffix not in GLTF_SUFFIXES and suffix not in BLENDER_SUFFIXES:
        known = ", ".join(sorted(GLTF_SUFFIXES | BLENDER_SUFFIXES))
        print(f"❌ {suffix or 'that file'} is not a 3D model format this script "
              f"handles.")
        print(f"   Handled: {known}")
        print("   If the model site offers GLB, download that — it is the format")
        print("   the studio loads and it needs no conversion.")
        return 2

    workdir = tempfile.mkdtemp(prefix="prepare_specimen_")
    report = os.path.join(workdir, "report.json")
    try:
        pipeline_input = src

        if suffix in BLENDER_SUFFIXES:
            blender = find_blender()
            if blender is None:
                print(blender_missing_message(suffix))
                return 3
            print(f"  Blender found: {blender}")
            print("  ⚠️  This conversion path has never been exercised — it was")
            print("      written without a Blender to test it against. Check the")
            print("      part names in the report below against the model you")
            print("      downloaded before trusting the result.\n")
            pipeline_input = os.path.join(workdir, f"{name}.converted.glb")
            if not convert_with_blender(blender, src, pipeline_input):
                print(f"\n❌ Blender could not convert {os.path.basename(src)} "
                      f"to GLB.")
                print("   Its output is above. The reliable fallback is to open the")
                print("   file in Blender yourself and use File ▸ Export ▸ glTF 2.0")
                print("   with Format set to glTF Binary (.glb), then run this")
                print("   script on that .glb.")
                return 4
            print(f"\n  converted to GLB: {pipeline_input}\n")

        status = run_pipeline(pipeline_input, out, name, report)
        if status != 0:
            print("\n❌ the glTF pipeline did not produce a usable specimen "
                  "(see above).")
            print("   The purchase gates were NOT run — there is nothing fit to "
                  "gate.")
            return 5

        validator_status = run_validator(out)
        summarise(report, validator_status)
        return validator_status
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
