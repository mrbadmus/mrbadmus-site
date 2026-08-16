#!/bin/bash
# Post-push check for the B1 replay (15 Aug 2026) — now a thin wrapper.
#
#   ./check_b1_live.sh
#
# ⊕ SUPERSEDED BY check_ks3_live.sh, 16 Aug 2026 (MRB-220). The entry point is
# kept because it is the name written into MRB-218's deploy notes, but the logic
# has moved.
#
# This script used to hard-code the stamps it expected:
#
#     CSS=dbd1f2f2
#     JS=b9cf7a3f
#
# Those were correct on the day B1 shipped and wrong for every build after it.
# Any edit to shared/ks3.css or shared/ks3.js moves both, and the script would
# then report six perfectly healthy lessons as "stale" — a false alarm on a green
# deploy, which is the fastest way to teach someone to ignore a checker.
# MRB-220 changed both files, so this would have fired on its very next run.
#
# check_ks3_live.sh reads the expected stamps out of the local build instead, so
# the stamp it compares against is always the stamp you just built, and it takes
# unit codes so B1 is no longer a special case.

exec "$(dirname "$0")/check_ks3_live.sh" B1
