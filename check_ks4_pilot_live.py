#!/usr/bin/env python3
"""check_ks4_pilot_live.py — prove the 54 KS4 pilot pages live on mrbadmus.com
ARE this build, byte for byte.

    python3 check_ks4_pilot_live.py            # every page in ks4_pilot_manifest.json
    python3 check_ks4_pilot_live.py --sample   # one page per route (5)

Run AFTER the push and after Cloudflare Pages reports the deploy done.

Two proofs per page, in this order (the order matters — see the immutable
cache trap below):

  1. THE PAGE. Fetch the live URL (following Cloudflare's 308 to the
     extensionless path) and compare the body's sha256 with the one
     `build_ks4.py` recorded in `ks4_pilot_manifest.json`. Equal means the
     live page is this build, not "a 200" — a 200 carrying last week's page
     is the failure mode that looks like success.
  2. THE ASSETS THAT PAGE NAMES. Only once the live page has been proved,
     read every `/shared/ks4-*?v=<stamp>` reference out of THAT live body
     and fetch each; the md5[:8] of the bytes must equal the stamp. Assets
     are fetched at the URL the live page names, never at a stamp read off
     the local tree, so a stale deploy cannot make us pin a stale asset in
     Cloudflare's immutable cache (memory: immutable cache trap).

Nothing here is typed by hand: the page list, the hashes and the stamps
all come from the manifest and the live body.
"""
import hashlib
import json
import re
import sys
import subprocess

BASE = "https://mrbadmus.com"
MANIFEST = "ks4_pilot_manifest.json"
STAMP_RE = re.compile(r'/shared/(ks4-[a-z-]+\.(?:js|css))\?v=([a-f0-9]{8})')


def fetch(url):
    # curl, not urllib: the framework Python on this Mac ships no CA bundle
    # (CERTIFICATE_VERIFY_FAILED on every https fetch), and check_ks4_live.sh
    # already proves live pages through curl. -L follows Cloudflare's 308.
    out = subprocess.run(
        ["curl", "-sSL", "-H", "Cache-Control: no-cache", "-H", "Pragma: no-cache",
         "-A", "check_ks4_pilot_live/1", "-w", "\n%{http_code} %{url_effective}", url],
        capture_output=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.decode("utf-8", "replace").strip() or "curl failed")
    body, _, trailer = out.stdout.rpartition(b"\n")
    status, _, final = trailer.decode().partition(" ")
    return int(status), final, body


def main():
    sample = "--sample" in sys.argv
    m = json.load(open(MANIFEST))
    pages = sorted(m["pages"].items())
    if sample:
        seen, picked = set(), []
        for path, sha in pages:
            route = "/".join(path.split("/")[1:3])
            if route not in seen:
                seen.add(route); picked.append((path, sha))
        pages = picked + [p for p in pages if p[0].endswith("nanoparticles.html")][:1]
    bad = 0
    asset_cache = {}
    for path, sha in pages:
        url = BASE + "/" + path.split("mrbadmus_site/", 1)[1]
        try:
            status, final, body = fetch(url)
        except Exception as e:  # noqa: BLE001
            print("FAIL %s — %s" % (url, e)); bad += 1; continue
        live_sha = hashlib.sha256(body).hexdigest()
        if status != 200 or live_sha != sha:
            print("FAIL %s — status %s, live sha256 %s… != build %s…" % (
                url, status, live_sha[:12], sha[:12])); bad += 1; continue
        refs = STAMP_RE.findall(body.decode("utf-8", "replace"))
        if not refs:
            print("FAIL %s — page carries no /shared/ks4-*?v= reference" % url)
            bad += 1; continue
        stale = []
        for name, stamp in sorted(set(refs)):
            key = (name, stamp)
            if key not in asset_cache:
                try:
                    _, _, abody = fetch("%s/shared/%s?v=%s" % (BASE, name, stamp))
                    asset_cache[key] = hashlib.md5(abody).hexdigest()[:8]
                except Exception as e:  # noqa: BLE001
                    asset_cache[key] = "ERR:%s" % e
            if asset_cache[key] != stamp:
                stale.append("%s?v=%s -> %s" % (name, stamp, asset_cache[key]))
        if stale:
            print("FAIL %s — asset bytes do not match their stamp: %s" % (url, "; ".join(stale)))
            bad += 1; continue
        print("OK   %s  sha256 %s…  assets %d" % (url, sha[:12], len(set(refs))))
    print()
    if bad:
        print("❌ %d of %d page(s) are NOT this build live" % (bad, len(pages)))
        return 1
    print("✅ %d page(s) live are this build byte for byte, and every asset they name matches its stamp" % len(pages))
    return 0


if __name__ == "__main__":
    sys.exit(main())
