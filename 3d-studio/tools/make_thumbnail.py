#!/usr/bin/env python3
"""Render a specimen's library thumbnail from the BUILT studio (MRB-218).

    python3 3d-studio/tools/make_thumbnail.py heart

Loads the real app in headless Chrome exactly as 3d_parity.py and
3d_render_check.py do — the built dist/ served under /3d/ so its absolute asset
URLs resolve — waits for the stage to reach `ready`, and captures the stage at
its default view, cropped square.

WHY RENDER IT RATHER THAN DRAW IT. A thumbnail drawn by hand is a second
picture of the specimen that can disagree with the first: repaint the tissue,
or replace the mesh, and the card goes on advertising the old one. This one is
a photograph of the thing itself, re-takeable with one command, so it cannot
drift from what the studio actually shows.

WHAT IT IS NOT. Not a generated fixture. It carries no underscore prefix and it
is meant to survive into dist/ and ship — `tools/make_test_*.py`'s underscore
convention marks files that must NEVER reach production, and this is the
opposite of one. tests/gates/build-hygiene.test.ts asserts both halves of that.

WHY WEBP COMES OUT OF CHROME. Chrome encodes it directly through
Page.captureScreenshot, so there is no Pillow, no cwebp, and no second
dependency for a repo whose entire Python toolchain is the standard library.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
import ks3_browser as cdp  # noqa: E402

STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(STUDIO, "dist")
PUBLIC_ASSETS = os.path.join(STUDIO, "public", "assets")

# Big enough to stay crisp on a 2× card, small enough that eight of them are
# not a page-weight problem.
EDGE = 512
# The desktop layout, so the stage gets the room the default view was framed
# for. A phone-width capture would frame the specimen against the sheet inset
# (MRB-216) and produce a thumbnail of a phone screen rather than of a heart.
VIEWPORT = (1440, 900)


def serve_dist_as_3d():
    """Serve dist/ under /3d/. Symlinked, never copied — nothing can drift,
    and the real dist/ is never within reach of the cleanup."""
    root = tempfile.mkdtemp(prefix="mrb-thumb-")
    target = os.path.join(root, "3d")
    os.symlink(DIST, target)
    server, port = cdp.serve(root)

    def cleanup():
        server.shutdown()
        if os.path.islink(target):
            os.unlink(target)
        shutil.rmtree(root, ignore_errors=True)

    return "http://127.0.0.1:%d/3d/" % port, cleanup


def wait_ready(page, timeout=60.0):
    """Poll the stage container until it settles. Never a fixed sleep: the app
    fetches a GLB over the network and decodes it, and a slow decode on a busy
    machine is not a failure."""
    deadline = time.time() + timeout
    state = None
    while time.time() < deadline:
        state = page.eval(
            "(document.querySelector('[data-renderer]')||{}).dataset"
            "&&document.querySelector('[data-renderer]').dataset.state||null")
        if state in ("ready", "failed"):
            return state
        time.sleep(0.15)
    return state


# Everything on the stage that is INTERFACE rather than SPECIMEN. A library
# card is a picture of the heart; a tool rail, a quality chip, a hint line and
# fourteen numbered dots inside a 90px tile are noise wearing the specimen's
# space. The card draws its own furniture.
#
# Hidden in the page rather than cropped around, because the rail is an overlay
# ON the stage — there is no rectangle that excludes it and still contains the
# specimen.
CHROME = [".rail", ".railtip", ".chip", ".flatchip", ".stagehint", ".hotspot",
          ".callout", ".leader", ".qpanel", ".autorot__track", ".autorot__word"]

# How much of the stage's square the specimen is framed to occupy. The renderer
# frames a specimen to sit comfortably inside the whole stage, which leaves a
# thumbnail mostly ground — so the crop tightens onto the middle. Tuned by
# looking at the result at 1.0 (heart about a third of the frame) and at this
# value; anything much below 0.6 starts clipping the aorta.
FRAMING = 0.66


def hide_chrome(page):
    """Take the interface off the stage, leaving the specimen on its ground."""
    page.eval("""(function(){
      var css = %s.map(function(s){ return s + '{display:none !important}' }).join('');
      var el = document.createElement('style');
      el.id = '__thumb_chrome';
      el.textContent = css;
      document.head.appendChild(el);
      return true;
    })()""" % json.dumps(CHROME))


def stage_square(page):
    """A centred square over the stage, tightened onto the specimen."""
    rect = page.eval("""(function(){
      var el = document.querySelector('[data-renderer]');
      if (!el) return null;
      var r = el.getBoundingClientRect();
      return {x: r.x, y: r.y, w: r.width, h: r.height};
    })()""")
    if not rect:
        raise RuntimeError("no stage container on the page")
    side = min(rect["w"], rect["h"]) * FRAMING
    return {
        "x": rect["x"] + (rect["w"] - side) / 2.0,
        "y": rect["y"] + (rect["h"] - side) / 2.0,
        "width": side,
        "height": side,
        "scale": EDGE / side,
    }


def render(specimen_id, out_path):
    if not os.path.isdir(DIST):
        raise SystemExit(
            "no build at %s — run `cd 3d-studio && npm run build` first" % DIST)

    url, cleanup = serve_dist_as_3d()
    try:
        # --enable-unsafe-swiftshader: headless Chrome has no GPU, and without
        # this there is no WebGL at all and the app correctly routes to the
        # flat renderer — which has no plate yet, so there would be nothing to
        # photograph. Same flag the other two browser gates launch with.
        with cdp.Browser(extra_args=["--enable-unsafe-swiftshader"]) as b:
            page = b.page(url)
            page.set_viewport(*VIEWPORT)
            state = wait_ready(page)
            if state != "ready":
                raise SystemExit(
                    "the stage never reached 'ready' (state=%r) — nothing to "
                    "photograph. Check `python3 3d_render_check.py` first."
                    % state)

            renderer = page.eval(
                "document.querySelector('[data-renderer]').dataset.renderer")
            palette = page.eval(
                "document.querySelector('[data-renderer]').dataset.palette")
            if renderer != "mesh":
                raise SystemExit(
                    "the stage is running the %r renderer, not 'mesh' — a "
                    "thumbnail of the fallback is not a thumbnail of the "
                    "specimen" % renderer)

            # The specimen is framed on an animation frame after ready, and
            # the contact shadow accumulates over several. Settle before the
            # shutter or the thumbnail catches the specimen mid-frame.
            time.sleep(1.5)

            hide_chrome(page)
            # The rail's disappearance reflows nothing (it is absolutely
            # positioned) but the compositor still needs a frame.
            time.sleep(0.4)

            clip = stage_square(page)
            shot = page.send("Page.captureScreenshot", {
                "format": "webp",
                "quality": 90,
                "clip": clip,
                "captureBeyondViewport": False,
            })
            import base64
            data = base64.b64decode(shot["data"])
            with open(out_path, "wb") as fh:
                fh.write(data)
            return {
                "bytes": len(data),
                "edge": EDGE,
                "palette": palette,
                "renderer": renderer,
            }
    finally:
        cleanup()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("specimen", nargs="?", default="heart")
    args = ap.parse_args()

    record_path = os.path.join(STUDIO, "content", "%s.json" % args.specimen)
    if not os.path.isfile(record_path):
        raise SystemExit("no content record at %s" % record_path)

    name = "%s.webp" % args.specimen
    out = os.path.join(PUBLIC_ASSETS, name)
    os.makedirs(PUBLIC_ASSETS, exist_ok=True)

    info = render(args.specimen, out)
    served = "/3d/assets/%s" % name

    print("✅ wrote %s — %d bytes, %d×%d, %s palette, %s renderer"
          % (os.path.relpath(out, os.path.dirname(STUDIO)), info["bytes"],
             info["edge"], info["edge"], info["palette"], info["renderer"]))
    print("   point assets.thumbnail at %r in content/%s.json"
          % (served, args.specimen))

    record = json.load(open(record_path, encoding="utf-8"))
    if record.get("assets", {}).get("thumbnail") != served:
        print("   ⚠ the record does not name it yet — validate_content.py "
              "will fail until it does (that is gate 2 working)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
