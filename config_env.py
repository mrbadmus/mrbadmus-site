#!/usr/bin/env python3
"""config_env.py — shared/config.js's two worlds, for the Python scripts.

⊕ B2C unit 6 (Mide's ruling, 5 Oct 2026): a TEST run must never be able to
call production. `shared/config.js` is the ONE file that writes down the
production backend host and the production Supabase project, and the fast
gate `test_isolation` holds every shipped page AND every gate, drive and tool
script to that. A script that needs either world's endpoints — a drive
pointing at TEST, a tool refusing a key whose `ref` claim is production, a
console filter that demotes the live tutor's warm-up ping — reads them from
here, and this module reads them out of config.js. Nothing here spells either
world.

    import config_env
    config_env.TEST["SUPABASE_URL"]      # the TEST project
    config_env.TEST["SUPABASE_ANON_KEY"]
    config_env.TEST["BACKEND_URL"]       # the local backend config.js names
    config_env.TEST_REF / config_env.PROD_REF
    config_env.PROD_BACKEND_HOST         # for REFUSING or IGNORING it, only

`backend(default=None)` is the backend a TEST drive talks to: `MRB_API` when
set (the `?api=` override config.js honours on localhost), else the TEST
block's own BACKEND_URL. It never returns the production backend: a value
that resolves to the production host is refused.
"""

import os
import re
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_JS = os.path.join(ROOT, "shared", "config.js")


def _block(src, name):
    start = src.index("const %s = {" % name)
    return src[start:src.index("};", start)]


def _world(name):
    src = open(CONFIG_JS, encoding="utf-8").read()
    block = _block(src, name)

    def val(key):
        m = re.search(r"%s:\s*'([^']+)'" % key, block)
        if not m:
            raise SystemExit("config_env: shared/config.js %s block has no %s"
                             % (name, key))
        return m.group(1)

    url = val("SUPABASE_URL")
    ref = re.match(r"https://([a-z0-9]+)\.supabase\.co", url).group(1)
    backend = val("BACKEND_URL")
    return {
        "SUPABASE_URL": url,
        "SUPABASE_ANON_KEY": val("SUPABASE_ANON_KEY"),
        "BACKEND_URL": backend,
        "ref": ref,
        "backend_host": urlparse(backend).hostname or "",
        "AUTH_STORAGE_KEY": "sb-%s-auth-token" % ref,
    }


PROD = _world("PROD")
TEST = _world("TEST")
PROD_REF = PROD["ref"]
TEST_REF = TEST["ref"]
PROD_BACKEND_HOST = PROD["backend_host"]
# The platform the production backend is hosted on (its host minus the
# service name) — for a detector that must catch ANY host there, not only
# today's one.
PROD_BACKEND_PLATFORM = PROD_BACKEND_HOST.split(".", 1)[-1]


def is_prod_url(url):
    """True for any URL on the production backend's platform or project."""
    h = (urlparse(url).hostname or "").lower()
    return (h == PROD_BACKEND_HOST or h.endswith("." + PROD_BACKEND_PLATFORM)
            or h == (urlparse(PROD["SUPABASE_URL"]).hostname or ""))


def backend(default=None):
    """The backend a TEST drive talks to. Never production."""
    url = (os.environ.get("MRB_API") or default or TEST["BACKEND_URL"]).rstrip("/")
    if is_prod_url(url):
        raise SystemExit("config_env: refusing %s — a TEST drive must never "
                         "call the production backend." % urlparse(url).hostname)
    return url
