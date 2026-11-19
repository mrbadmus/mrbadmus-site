#!/usr/bin/env python3
"""check_ks4_live.py — prove a KS4 BATCH's pages live on mrbadmus.com ARE
this build, byte for byte. The generalised form of check_ks4_pilot_live.py
(docs/ks4/batch-engine.md) — that script is now a thin wrapper around this
one with `--batch pilot` pinned, kept so nothing that calls it by name
breaks.

    python3 check_ks4_live.py --batch pilot            # every pilot page
    python3 check_ks4_live.py --batch batch-2          # every batch-2 page
    python3 check_ks4_live.py --batch pilot --sample   # one page per route

Run AFTER the push. The script itself now waits for Cloudflare Pages to report the deploy done
(GitHub check run), for a live page to name this build's asset stamps, and 90 s more, and checks
each asset under a throwaway query first: no stamped asset URL is fetched before that (18 Nov 2026).

Two proofs per page, in this order (the order matters — see the immutable
cache trap below):

  1. THE PAGE. Fetch the live URL (following Cloudflare's 308 to the
     extensionless path) and compare the body's sha256 with the one
     `build_ks4.py` recorded in the batch's manifest
     (`ks4_pilot_manifest.json` for the pilot, `ks4_<batch>_manifest.json`
     otherwise). Equal means the live page is this build, not "a 200" — a
     200 carrying last week's page is the failure mode that looks like
     success.
  2. THE ASSETS THAT PAGE NAMES. Only once the live page has been proved,
     read every `/shared/ks4-*?v=<stamp>` reference out of THAT live body
     and fetch each; the md5[:8] of the bytes must equal the stamp. Assets
     are fetched at the URL the live page names, never at a stamp read off
     the local tree, so a stale deploy cannot make us pin a stale asset in
     Cloudflare's immutable cache (memory: immutable cache trap). This
     naturally covers a batch's OWN `ks4-source-<batch>.js` / `ks4-lesson-
     <batch>.css` / `ks4-ext-<batch>.js` too — they match the same
     `/shared/ks4-*?v=` pattern as the pilot's shared assets.

Nothing here is typed by hand: the page list, the hashes and the stamps
all come from the manifest and the live body.
"""
import argparse
import hashlib
import json
import re
import sys
import random
import subprocess
import time

BASE = "https://mrbadmus.com"
STAMP_RE = re.compile(r'/shared/(ks4-[a-z0-9-]+\.(?:js|css))\?v=([a-f0-9]{8})')


def manifest_path_for(batch):
    return "ks4_pilot_manifest.json" if batch == "pilot" else "ks4_%s_manifest.json" % batch


def fetch(url):
    # curl, not urllib: the framework Python on this Mac ships no CA bundle
    # (CERTIFICATE_VERIFY_FAILED on every https fetch), and check_ks4_live.sh
    # already proves live pages through curl. -L follows Cloudflare's 308.
    out = subprocess.run(
        ["curl", "-sSL", "-H", "Cache-Control: no-cache", "-H", "Pragma: no-cache",
         "-A", "check_ks4_live/1", "-w", "\n%{http_code} %{url_effective}", url],
        capture_output=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.decode("utf-8", "replace").strip() or "curl failed")
    body, _, trailer = out.stdout.rpartition(b"\n")
    status, _, final = trailer.decode().partition(" ")
    return int(status), final, body


REPO_SLUG = "mrbadmus/mrbadmus-site"
SETTLE_S = 90          # after the page flips: an edge can still route assets to the old deploy


def _head():
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def wait_for_deploy(sha, timeout=1800, poll=20):
    """Block until GitHub shows Cloudflare Pages' check run for `sha` completed. Fail closed:
    no gh, no run, a failed run or a timeout all refuse, because every asset fetch before the
    deploy lands can pin last deploy's bytes under the new stamp for a year (immutable)."""
    t_end = time.time() + timeout
    while True:
        out = subprocess.run(
            ["gh", "api", "repos/%s/commits/%s/check-runs" % (REPO_SLUG, sha),
             "--jq", '.check_runs[] | select(.name == "Cloudflare Pages") | [.status, (.conclusion // ""), (.completed_at // "")] | @tsv'],
            capture_output=True, text=True)
        if out.returncode != 0:
            raise SystemExit("check_ks4_live: cannot read Cloudflare's deploy status for %s from GitHub "
                             "(gh: %s). Refusing to fetch any stamped asset before the deploy is known "
                             "to be finished." % (sha[:10], out.stderr.strip()[:200]))
        rows = [r.split("\t") for r in out.stdout.strip().splitlines() if r.strip()]
        done = [r for r in rows if r[0] == "completed"]
        if done:
            if all(r[1] == "success" for r in done):
                print("deploy: Cloudflare Pages finished %s for %s" % (done[-1][2], sha[:10]))
                return
            raise SystemExit("check_ks4_live: Cloudflare Pages reports %s for %s: not live."
                             % (done[-1][1], sha[:10]))
        if time.time() > t_end:
            raise SystemExit("check_ks4_live: no finished Cloudflare Pages deploy for %s after %d s "
                             "(is it pushed?)." % (sha[:10], timeout))
        print("deploy: waiting for Cloudflare Pages on %s (%s)…" % (sha[:10], rows[0][0] if rows else "no run yet"))
        time.sleep(poll)


def wait_for_stamps(url, want, timeout=900, poll=15):
    """Block until the live page at `url` names every asset stamp in `want` ({name: stamp})."""
    t_end = time.time() + timeout
    while True:
        try:
            status, _, body = fetch(url)
            have = dict(STAMP_RE.findall(body.decode("utf-8", "replace")))
        except Exception as e:  # noqa: BLE001
            status, have = "ERR %s" % e, {}
        missing = {n: s for n, s in want.items() if have.get(n) != s}
        if status == 200 and not missing:
            return
        if time.time() > t_end:
            raise SystemExit("check_ks4_live: %s still does not name this build's assets: %s"
                             % (url, ", ".join("%s?v=%s" % kv for kv in sorted(missing.items()))))
        time.sleep(poll)


def nonce_ok(name, stamp):
    """md5 of the asset fetched under a throwaway query, so the real cache key is never touched."""
    _, _, abody = fetch("%s/shared/%s?v=%s&nonce=%d" % (BASE, name, stamp, random.randrange(10**9)))
    return hashlib.md5(abody).hexdigest()[:8] == stamp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", default="pilot",
                     help="'pilot' (default) or another registered batch name")
    ap.add_argument("--sample", action="store_true",
                     help="one page per route instead of every page")
    args = ap.parse_args()

    manifest_path = manifest_path_for(args.batch)
    try:
        m = json.load(open(manifest_path))
    except FileNotFoundError:
        raise SystemExit("check_ks4_live: %s does not exist — build batch "
                          "%r first." % (manifest_path, args.batch))
    pages = sorted(m["pages"].items())
    if args.sample:
        seen, picked = set(), []
        for path, sha in pages:
            route = "/".join(path.split("/")[1:3])
            if route not in seen:
                seen.add(route); picked.append((path, sha))
        pages = picked

    # ⊕ 18 Nov 2026 (supervising ruling): THE DEPLOY-FINISHED RULE. Fetching a stamped asset before
    # Cloudflare has published can pin last deploy's bytes under the new stamp for a year
    # (immutable), and a flipped page is not proof enough (an edge can still route the asset to the
    # old deploy for a moment). So, before ANY asset is fetched at its real URL:
    #   1. GitHub's "Cloudflare Pages" check run for this commit is completed and successful;
    #   2. a live page names every asset stamp this build wrote;
    #   3. SETTLE_S more seconds;
    #   4. each asset, fetched under a throwaway &nonce=, already hashes to its stamp.
    # Any failure stops here, with the real cache keys untouched. There is no flag to skip it.
    sha = _head()
    wait_for_deploy(sha)
    want, probe = {}, None
    for path, _sha in pages:
        local = dict(STAMP_RE.findall(open(path, encoding="utf-8").read()))
        want.update(local)
        probe = probe or (path, local)
    probe_url = BASE + "/" + probe[0].split("mrbadmus_site/", 1)[1]
    wait_for_stamps(probe_url, probe[1])
    print("deploy: %s names this build's assets; settling %d s" % (probe_url, SETTLE_S))
    time.sleep(SETTLE_S)
    unready = sorted("%s?v=%s" % kv for kv in want.items() if not nonce_ok(*kv))
    if unready:
        print("❌ the origin is not serving these assets' new bytes yet (checked under a throwaway "
              "query; the real URLs were NOT fetched): %s" % ", ".join(unready))
        return 1

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
        print("❌ %d of %d page(s) [%s] are NOT this build live" % (bad, len(pages), args.batch))
        return 1
    print("✅ %d page(s) [%s] live are this build byte for byte, and every "
          "asset they name matches its stamp" % (len(pages), args.batch))
    return 0


if __name__ == "__main__":
    sys.exit(main())
