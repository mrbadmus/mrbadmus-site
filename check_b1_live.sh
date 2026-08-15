#!/bin/bash
# Post-push check for the B1 replay (15 Aug 2026).
# Run AFTER GitHub Desktop has pushed and Cloudflare Pages reports the deploy done.
#
#   ./check_b1_live.sh
#
# Cloudflare 308-redirects /x.html -> /x, so this follows redirects and asserts
# on the FINAL response. It checks three things per lesson:
#   200 · the draft marker · the ks3.css/ks3.js stamps THIS build produced.
# The stamps are the point: a 200 carrying stale assets is the failure mode that
# looks like success. Before this deploy these URLs served "Coming soon" on
# ks3.css?v=79df97e8; after it they must serve the lesson on ?v=dbd1f2f2.

CSS=dbd1f2f2
JS=b9cf7a3f
BASE=https://mrbadmus.com/ks3/biology/cells-and-organisation
FAIL=0

printf '  %-26s %-9s %-9s %-13s %s\n' LESSON HTTP DRAFT CSS JS
for s in life-processes using-a-microscope animal-and-plant-cells \
         specialised-cells levels-of-organisation unicellular-organisms; do
  url="$BASE/$s.html"
  body=$(curl -sL --max-time 30 "$url" 2>/dev/null)
  code=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 30 "$url")

  [ "$code" = "200" ] && c="200 ✅" || { c="$code ❌"; FAIL=1; }
  grep -q 'Draft — not yet science-reviewed' <<<"$body" && d="✅"       || { d="❌";       FAIL=1; }
  grep -q "ks3.css?v=$CSS"                   <<<"$body" && a="✅"       || { a="❌ stale"; FAIL=1; }
  grep -q "ks3.js?v=$JS"                     <<<"$body" && j="✅"       || { j="❌ stale"; FAIL=1; }
  grep -q 'Coming soon'                      <<<"$body" && { c="$c(soon)"; FAIL=1; }

  printf '  %-26s %-9s %-9s %-13s %s\n' "$s" "$c" "$d" "$a" "$j"
done

echo
if [ $FAIL -eq 0 ]; then
  echo "✅ all six B1 lessons live, carrying the draft marker, on this build's assets"
else
  echo "❌ something is off above."
  echo "   'stale' or '(soon)' almost always means Cloudflare has not finished"
  echo "   deploying yet — give it a few minutes and re-run before investigating."
fi
