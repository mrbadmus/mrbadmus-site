#!/usr/bin/env python3
"""Signal harness for §5 of mrb327_safari_drive.js.

The checkout-return page only polls while OUR subscription row has not caught
up with Stripe. That is a REAL state (`status='none'`, before the webhook), so
the drive reproduces it rather than stubbing the endpoint: this watcher flips
the row to `none` when the drive says it is about to load the page, and back to
`trialing` when the drive says to settle it.
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mrb327_safari_drive as F

ENGINE = sys.argv[1]
S = F.SCRATCH
ids = json.load(open(F.STATE_FILE))
ORG = ids["org"]

poll_mode = os.path.join(S, "poll_mode_" + ENGINE)
poll_ready = os.path.join(S, "poll_ready_" + ENGINE)
settle = os.path.join(S, "settle_now_" + ENGINE)
for f in (poll_mode, poll_ready, settle):
    if os.path.exists(f):
        os.remove(f)

print("[watcher] waiting for poll_mode…", flush=True)
t0 = time.time()
while not os.path.exists(poll_mode):
    if time.time() - t0 > 900:
        print("[watcher] timed out waiting for poll_mode"); sys.exit(1)
    time.sleep(0.3)

st, d = F.sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + ORG,
                   {"status": "none", "trial_end": None})
print("[watcher] status → none (%s)" % st, flush=True)
open(poll_ready, "w").write("1")

print("[watcher] waiting for settle_now…", flush=True)
t0 = time.time()
while not os.path.exists(settle):
    if time.time() - t0 > 900:
        print("[watcher] timed out waiting for settle_now"); sys.exit(1)
    time.sleep(0.3)

st, d = F.sb_admin("PATCH", "/rest/v1/subscriptions?org_id=eq." + ORG,
                   {"status": "trialing", "trial_end": F.iso(6 * 86400)})
print("[watcher] status → trialing (%s)" % st, flush=True)
