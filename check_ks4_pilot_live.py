#!/usr/bin/env python3
"""check_ks4_pilot_live.py — THIN WRAPPER around check_ks4_live.py's
generalised `--batch` form (docs/ks4/batch-engine.md, 1 Oct 2026). Kept
under its original name/invocation so nothing that already calls it by
name breaks; the real implementation (the manifest-driven live-vs-build
sha256 + asset-stamp proof) now lives in check_ks4_live.py and covers
every registered batch, not only the pilot.

    python3 check_ks4_pilot_live.py            # every pilot page
    python3 check_ks4_pilot_live.py --sample   # one page per route (5)
"""
import sys

import check_ks4_live


def main():
    sys.argv = [sys.argv[0], "--batch", "pilot"] + sys.argv[1:]
    return check_ks4_live.main()


if __name__ == "__main__":
    sys.exit(main())
