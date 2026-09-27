#!/usr/bin/env python3
"""brand_cards.py — redraw the brand's raster images from brand.py (one-mark run).

    python3 brand_cards.py

  · docs/b2c/social-card.png — the 1200×630 shared-link card. Its source,
    docs/b2c/social-card.html, is stamped with the one lockup first.
  · shared/brand/mrbadmus-lockup-light-email.png — the lockup for email
    headers (email clients do not render inline SVG), drawn from the same
    partial every page wears, at 3× so it stays sharp at 160 px wide.

Both are drawn in headless Chrome from the live partial and brand.css, so
they cannot drift from the header on the site.
"""
import base64
import time
from pathlib import Path

import brand
import ks3_browser as cdp

HERE = Path(__file__).resolve().parent
CARD_SRC = HERE / "docs/b2c/social-card.html"
CARD_PNG = HERE / "docs/b2c/social-card.png"
EMAIL_PNG = HERE / "shared/brand/mrbadmus-lockup-light-email.png"
_TMP = HERE / "_brand_email_render.html"


def _shot(page, clip, path):
    page.send("Emulation.setDefaultBackgroundColorOverride", {"color": {"r": 0, "g": 0, "b": 0, "a": 0}})
    res = page.send("Page.captureScreenshot", {"format": "png", "clip": dict(clip, scale=1)})
    Path(path).write_bytes(base64.b64decode(res["data"]))


def main():
    CARD_SRC.write_text(brand.stamp_brand(CARD_SRC.read_text(encoding="utf-8")), encoding="utf-8")
    _TMP.write_text(
        '<!doctype html><html data-theme="light"><head>'
        '<link rel="stylesheet" href="/shared/brand/brand.css">'
        '<style>html,body{margin:0;background:transparent}body{padding:6px 4px;display:inline-block;zoom:3}</style>'
        f'</head><body>{brand.brand_lockup("#")}</body></html>', encoding="utf-8")
    server, port = cdp.serve(str(HERE))
    try:
        with cdp.Browser() as b:
            p = b.page(f"http://127.0.0.1:{port}/docs/b2c/social-card.html")
            p.set_viewport(1200, 630)
            time.sleep(1.0)
            _shot(p, {"x": 0, "y": 0, "width": 1200, "height": 630}, CARD_PNG)
            p.goto(f"http://127.0.0.1:{port}/{_TMP.name}")
            p.set_viewport(1280, 400)
            time.sleep(1.0)
            x, y, w, h = p.eval("(()=>{const r=document.querySelector('.mrb-brand').getBoundingClientRect();"
                                "return [r.left,r.top,r.width,r.height]})()")
            _shot(p, {"x": x - 3, "y": y - 3, "width": round(w) + 6, "height": round(h) + 6}, EMAIL_PNG)
    finally:
        server.shutdown()
        _TMP.unlink(missing_ok=True)
    print("wrote", CARD_PNG.relative_to(HERE), "and", EMAIL_PNG.relative_to(HERE))


if __name__ == "__main__":
    main()
