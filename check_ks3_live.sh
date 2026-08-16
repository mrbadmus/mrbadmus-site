#!/bin/bash
# Post-push check for any authored KS3 unit (MRB-220, generalising check_b1_live.sh).
#
#   ./check_ks3_live.sh                 # every authored lesson the local build has
#   ./check_ks3_live.sh B2 C1 C2        # named units only
#
# Run AFTER the push and after Cloudflare Pages reports the deploy done.
#
# Cloudflare 308-redirects /x.html -> /x, so this follows redirects and asserts on
# the FINAL response. Per lesson it checks four things:
#   200 · the ks3.css stamp · the ks3.js stamp · absence of the revoked marker
#
# ⊕ MRB-221 (16 Aug 2026) — the third column used to REQUIRE the under-review
# marker. Architecture §5.10.1 is revoked and the build no longer emits it, so
# the assertion is inverted rather than dropped: a marker reappearing live is now
# the failure. Both halves moved in the same commit as the emission, deliberately.
#
# ── Why the stamps are derived and never typed ──────────────────────────────
#
# A 200 carrying stale assets is the failure mode that looks like success: the
# page is there, the styles and behaviour are last week's. So the stamps matter
# more than the status code.
#
# check_b1_live.sh hard-codes CSS=dbd1f2f2 / JS=b9cf7a3f — correct on the day it
# was written, and wrong for every build after it. Any change to shared/ks3.css
# or shared/ks3.js moves both, and the script then reports six healthy lessons as
# "stale". A checker that cries wolf after one deploy gets switched off, so this
# one reads the expected stamps out of the LOCAL build it is checking against.
# The stamp you compare with is the stamp you just built, always.
#
# It also derives the LESSON LIST from the local build rather than hard-coding
# slugs: a lesson that is still a "coming soon" placeholder locally is skipped
# rather than failed, because an unauthored slot serving a placeholder is the
# architecture working (structure-first, §8.8), not a defect.

set -uo pipefail
cd "$(dirname "$0")" || exit 1

OUT=mrbadmus_site/ks3
BASE=https://mrbadmus.com/ks3

[ -d "$OUT" ] || { echo "no local build at $OUT — run python3 generate_site_v5.py first"; exit 1; }

# The stamps THIS build produced, read from any built lesson.
probe=$(find "$OUT" -name '*.html' -print -quit)
CSS=$(grep -o 'ks3\.css?v=[0-9a-f]*' "$probe" | head -1 | cut -d= -f2)
JS=$(grep -o 'ks3\.js?v=[0-9a-f]*'  "$probe" | head -1 | cut -d= -f2)
[ -n "$CSS" ] && [ -n "$JS" ] || { echo "could not read asset stamps from $probe"; exit 1; }

echo "expecting  ks3.css?v=$CSS   ks3.js?v=$JS"
echo

FAIL=0; N=0; SKIP=0
printf '  %-52s %-9s %-9s %-9s %s\n' LESSON HTTP CSS JS NOMARK

# Which unit folders to check. Unit code -> discipline/slug comes from
# structure.py, so a new unit needs no edit here and a renamed one cannot go
# quietly unchecked.
if [ $# -gt 0 ]; then
  PREFIXES=$(python3 - "$@" <<'PY'
import sys
sys.path.insert(0, ".")
from ks3_data import structure
want = {a.upper() for a in sys.argv[1:]}
for unit in structure.UNITS:
    code, slug, _title, discipline = unit[0], unit[1], unit[2], unit[3]
    if code.upper() in want:
        print("%s/%s/" % (discipline, slug))
PY
)
  [ -n "$PREFIXES" ] || { echo "no unit matched: $*"; exit 1; }
fi

for f in $(find "$OUT" -name '*.html' ! -name 'index.html' | sort); do
  rel=${f#"$OUT"/}

  if [ $# -gt 0 ]; then
    keep=0
    for p in $PREFIXES; do
      case "$rel" in "$p"*) keep=1 ;; esac
    done
    [ $keep -eq 1 ] || continue
  fi

  # An unauthored slot is a placeholder by design — skip, never fail.
  if grep -q 'Coming soon' "$f"; then SKIP=$((SKIP+1)); continue; fi

  url="$BASE/${rel%.html}.html"
  body=$(curl -sL --max-time 30 "$url" 2>/dev/null)
  code=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 30 "$url")
  N=$((N+1))

  [ "$code" = "200" ] && c="200 ✅" || { c="$code ❌"; FAIL=1; }
  grep -q "ks3.css?v=$CSS" <<<"$body" && a="✅" || { a="❌ stale"; FAIL=1; }
  grep -q "ks3.js?v=$JS"   <<<"$body" && j="✅" || { j="❌ stale"; FAIL=1; }
  grep -q 'Coming soon'    <<<"$body" && { c="$c(soon)"; FAIL=1; }
  # ⊕ MRB-221 — the under-review marker is revoked, so this asserts its ABSENCE.
  # The old line passed only when it FOUND the string; leaving it in place after
  # the build stopped emitting it would have turned all 30 live lessons red.
  grep -q 'science-reviewed' <<<"$body" && { m="❌ marker"; FAIL=1; } || m="✅"

  printf '  %-52s %-9s %-9s %-9s %s\n' "${rel%.html}" "$c" "$a" "$j" "$m"
done

echo
echo "checked $N authored lesson(s); skipped $SKIP still-placeholder slot(s)"
if [ $FAIL -eq 0 ] && [ $N -gt 0 ]; then
  echo "✅ all live, clean of the revoked marker, on THIS build's assets"
elif [ $N -eq 0 ]; then
  echo "⚠️  nothing matched — check the unit codes you passed"; exit 1
else
  echo "❌ something is off above."
  echo "   'stale' or '(soon)' almost always means Cloudflare has not finished"
  echo "   deploying yet — give it a few minutes and re-run before investigating."
  exit 1
fi
