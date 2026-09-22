#!/usr/bin/env python3
"""
MRB-348 · Set a known password on the TEST drive fixtures.

The perf drives (teacher_perf_budget.py, mrb328_card_prefetch_drive.py, and the
new perf_waterfall.py) all sign in as the MRB-293 TEST fixtures and read their
password from $MRB_TEST_TEACHER_PASSWORD / $MRB_TEST_STUDENT_PASSWORD. Neither
is set in this environment, so every one of those drives would SKIP BY NAME and
this run would have no measurement at all.

These are fake accounts on the SANDBOX project that exist only to be driven.
Setting a password on them is the prerequisite, not a change to the product.

⚠️ REFUSES TO RUN AGAINST ANYTHING BUT TEST, and proves it from the credential
rather than from a label beside it: a service-role key is a JWT whose payload
carries {"ref": "<project>"}, so the ref is read out of the key itself and
checked against the TEST ref. That is CLAUDE.md item 8, and it is the check that
caught a script printing "the TEST database" while reading production.
"""
import base64
import json
import os
import re
import ssl
import sys
import urllib.request

TEST_REF = "qeppkiswvclkkwbxmlok"
PROD_REF = "urklkrwevjtlfbwnipjn"

# The repo's own scripts pin this CA file; the framework Python's default trust
# store does not resolve Supabase's issuer on this machine.
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

BACKEND_ENV = os.environ.get(
    "MRB_BACKEND", "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
) + "/.env"

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ⚠️ THE hz_* FIXTURES ARE NOT ENOUGH TO MEASURE WITH. hz_s1's only class has
# zero assignments and zero submissions, and hz_amy's has zero of both, so a
# waterfall driven from them would show a page with nothing to load — fast for
# the one reason that cannot be shipped. The Rainford TEST seed is the realistic
# world: 8X1 is a KS3 class with 4 assignments and 15 submissions (so the deck
# and ladder reads actually fire), 10A is KS4 with 17, and mide.badmus teaches
# 5 classes / 26 assignments / 79 submissions — which is the shape workstream 2
# is about. Both sets are fake accounts on the sandbox project.
# ⚠️ THE hz_* FIXTURES HAVE DOCUMENTED PASSWORDS AND GATES DEPEND ON THEM.
# `night3_selfreview.py` (the `consumer_flag_off` gate) hard-codes the defaults
# `mrb293-drive-only` for hz_amy and `Night3!Admin` for hz_admin. MRB-348 set a
# different password on hz_amy and hz_rich and turned that gate RED — three
# checks failing with "sign-in failed", which reads exactly like a product
# defect and was entirely self-inflicted. So this file no longer takes one
# password for everything: each fixture is restored to the value the gates
# already expect, and the Rainford accounts take the same standing value so a
# single MRB_TEST_TEACHER_PASSWORD still drives everything.
#
# ⚠️ hz_s1's documented default is the EMPTY STRING — `consumer_flag_off` skips
# its two student checks for want of a credential, by design. It is given the
# standing password here so the perf drives can use it; that cannot un-skip the
# gate, which reads its own env var and defaults to empty.
STANDING = "mrb293-drive-only"

FIXTURES = {
    "ee000000-0000-0000-0000-000000001002": ("hz_amy@test.mrbadmus", STANDING),
    "ee000000-0000-0000-0000-000000001001": ("hz_rich@test.mrbadmus", STANDING),
    "ee000000-0000-0000-0000-000000001101": ("hz_s1@test.mrbadmus", STANDING),
    "ee000000-0000-0000-0000-000000001005": ("hz_admin@test.mrbadmus", "Night3!Admin"),
    # The Rainford seed — the realistic world the perf waterfall measures.
    # hz_s1's only class holds zero assignments and zero submissions, so a
    # waterfall driven from it measures a page with nothing to load, which is
    # fast for the one reason that cannot be shipped.
    "29000000-0000-0000-0000-000000000001": ("aiden.cole@test-rainford.local", STANDING),
    "29000000-0000-0000-0000-000000000006": ("hannah.patel@test-rainford.local", STANDING),
    "28000000-0000-0000-0000-000000000001": ("mide.badmus@test-rainford.local", STANDING),
}


def read_env(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                out[k] = v.strip().strip('"').strip("'")
    return out


def jwt_ref(token):
    """Read the project ref out of the key's own payload. Never off a label."""
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(payload)).get("ref")


def post(url, body, headers, method="POST"):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), headers=headers, method=method
    )
    try:
        r = urllib.request.urlopen(req, timeout=30, context=CTX)
        raw = r.read().decode()
        return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:300]}


def main():
    # Kept as a confirmation switch rather than the source of the value: the
    # values live in FIXTURES above, because the gates already know them.
    if os.environ.get("MRB_TEST_FIXTURE_RESET") != "1":
        print("This restores the TEST fixtures to the passwords the gates expect.")
        print("Re-run with MRB_TEST_FIXTURE_RESET=1 to do it.")
        return 2

    env = read_env(BACKEND_ENV)
    url, srk = env.get("SUPABASE_URL", ""), env.get("SUPABASE_SERVICE_ROLE_KEY", "")
    ref = jwt_ref(srk)

    print("credential ref, proven from the key payload : %s" % ref)
    print("SUPABASE_URL (a label, not the proof)       : %s" % url)
    if ref == PROD_REF:
        print("REFUSING: that is the PRODUCTION ref. This script is TEST-only.")
        return 1
    if ref != TEST_REF:
        print("REFUSING: ref %r is neither TEST nor a ref this script knows." % ref)
        return 1
    if url.split("//")[-1].split(".")[0] != ref:
        print("REFUSING: the URL's ref and the key's ref disagree.")
        return 1
    print("=> TEST (%s). Proceeding.\n" % TEST_REF)

    hdr = {"apikey": srk, "Authorization": "Bearer " + srk,
           "Content-Type": "application/json"}
    for uid, (email, want) in FIXTURES.items():
        st, _ = post(url + "/auth/v1/admin/users/" + uid,
                     {"password": want, "email_confirm": True}, hdr, method="PUT")
        print("  set password  %-32s HTTP %s" % (email, st))

    # Prove the credential actually signs in — a set that does not produce a
    # usable session is a silent failure that would surface as a drive SKIP.
    # ⚠️ THE **TEST** ANON KEY, NOT THE FIRST ONE IN THE FILE. config.js carries
    # both projects' keys and production's comes first, so a naive first-match
    # read signs a TEST fixture's email into PRODUCTION and gets a 401 that
    # looks like a bad password. The repo's drives slice from `const TEST`;
    # this does the same, then proves the ref out of the key it picked.
    anon = None
    with open(os.path.join(SITE, "shared", "config.js"), encoding="utf-8") as fh:
        src = fh.read()
    m = re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                  src[src.index("const TEST"):])
    if m:
        anon = m.group(1)
        if jwt_ref(anon) != TEST_REF:
            print("REFUSING: the anon key picked is not TEST's.")
            return 1
    if not anon:
        print("\n  (could not read the anon key; skipping the sign-in proof)")
        return 0

    print()
    ok = True
    for email, want in FIXTURES.values():
        st, d = post(url + "/auth/v1/token?grant_type=password",
                     {"email": email, "password": want},
                     {"apikey": anon, "Content-Type": "application/json"})
        good = st == 200 and bool(d.get("access_token"))
        ok = ok and good
        print("  sign-in proof %-32s %s" % (email, "OK" if good else "FAILED %s" % st))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
