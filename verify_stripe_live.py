#!/usr/bin/env python3
"""verify_stripe_live.py — can a parent on production actually reach Stripe
Checkout? Slow gate, stdlib only, no browser, no credential.

⊕ Live checkout incident, 9 Oct 2026. The first real parent on mrbadmus.com
pressed "Add a card and start the free week" three times and was told "The
payment page didn't open." Production's STRIPE_SECRET_KEY was the text of a
shell command, pasted where the key belonged, so every Stripe call answered
401 — while /api/health reported Stripe "configured", because all it checked
was that the variable was set. Every checkout test and drive in the estate
ran on a TEST key, so nothing had ever exercised the live-mode path.

The backend now dry-runs the checkout route's own Stripe calls with the key
it actually holds (consumer/stripe.js liveCheck: prices, the customer lookup,
the list calls, and a customer write and a Checkout create aimed at a
customer that cannot exist — Stripe checks permission first, so "No such
customer" proves the real call would be allowed; nothing is created). The
result rides on /api/health as `stripe.live_check`. This gate reads it and
fails unless every step passed on a LIVE key.

It only applies while launch.json says the consumer product is launched:
with signup off there is no parent who could press the button, and a test
key on production is then legitimate. A backend too old to carry the live
check is a FAIL, never a skip — "could not measure" is not "fine".

    python3 verify_stripe_live.py
    python3 verify_stripe_live.py --base http://localhost:3000   # any backend
"""
import json
import subprocess
import sys
import time

BASE = "https://mrbadmus-backend.onrender.com"


def launched():
    with open("launch.json") as f:
        return bool(json.load(f).get("consumer_signup_enabled"))


def health(base):
    # curl, not urllib: the python.org Python on the Mac ships no CA bundle,
    # and a certificate error would read as "backend unreachable".
    out = subprocess.run(["curl", "-sS", "--max-time", "60", "-H", "Cache-Control: no-cache",
                          base + "/api/health"], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or f"curl exit {out.returncode}")
    return json.loads(out.stdout)


def main(argv):
    base = BASE
    if "--base" in argv:
        base = argv[argv.index("--base") + 1].rstrip("/")
    if not launched():
        print("stripe_live_checkout: consumer signup is OFF in launch.json — nothing to check. PASS")
        return 0
    deadline = time.time() + 120
    while True:
        try:
            h = health(base)
        except Exception as e:  # a cold Render instance can take a minute
            if time.time() > deadline:
                print(f"FAIL — {base}/api/health unreachable: {e}")
                return 1
            time.sleep(10)
            continue
        st = h.get("stripe")
        if st is None:
            print("FAIL — the backend reports no Stripe module")
            return 1
        if "live_check" not in st:
            print(f"FAIL — backend build {h.get('build')} predates the live check")
            return 1
        lc = st["live_check"]
        if lc is None:
            print("FAIL — Stripe is not configured on the backend (no key or no prices)")
            return 1
        if lc.get("pending"):
            if time.time() > deadline:
                print("FAIL — the live check never finished")
                return 1
            time.sleep(5)
            continue
        break
    print(f"backend {h.get('build')}  key {lc.get('mode')}  checked {lc.get('checked_at')}")
    for s in lc.get("steps", []):
        extra = s.get("note", "") if s.get("ok") else json.dumps(s.get("error") or s.get("note"))
        print(f"  {'✅' if s.get('ok') else '❌'} {s.get('step', '?'):<18} {extra}")
    live = lc.get("mode") in ("live", "live_restricted")
    if not live:
        print(f"  ❌ key mode is {lc.get('mode')!r} — consumer signup is launched, so the key must be live")
    ok = bool(lc.get("ok")) and live
    print("PASS — checkout's Stripe path works in live mode" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
