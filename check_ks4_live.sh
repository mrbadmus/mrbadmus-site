#!/bin/bash
# Post-push check for the KS4 and root pages (MRB-290, modelled on
# check_ks3_live.sh — read that file's header for why the stamps are DERIVED
# from the local build and never typed).
#
#   ./check_ks4_live.sh                       # the standard sample
#   ./check_ks4_live.sh combined/foundation/physics/energy.html …   # named pages
#
# Run AFTER the push and after Cloudflare Pages reports the deploy done.
#
# Per page it asserts, on the FINAL response after Cloudflare's 308s:
#   200 · every /shared/*?v= reference the LOCAL build stamped into that
#         page appears byte-identical in the live body.
#
# That second assertion is the whole point: a 200 carrying stale assets is
# the failure mode that looks like success, and it is what broke a session
# on KS3 before stamping landed there. Comparing the live body's stamped
# references against the local build's proves the live page IS this build.

set -uo pipefail
cd "$(dirname "$0")" || exit 1

OUT=mrbadmus_site
BASE=https://mrbadmus.com

[ -d "$OUT" ] || { echo "no local build at $OUT — run python3 build_all.py first"; exit 1; }

# The sample: every root page plus one topic page per pathway/tier/subject —
# broad enough that a stamping regression in any emitter shows, small enough
# to run in seconds. Named arguments override it.
if [ $# -gt 0 ]; then
  PAGES="$*"
else
  PAGES="index.html ks4.html auth.html leaderboard.html weekly-challenge.html
         my-challenges.html past-papers.html profile-setup.html revision.html
         teacher-profile.html"
  for tree in combined/foundation combined/higher triple/foundation triple/higher; do
    for subj in biology chemistry physics; do
      p=$(find "$OUT/$tree/$subj" -maxdepth 1 -name '*.html' ! -name 'index.html' 2>/dev/null | sort | head -1)
      [ -n "$p" ] && PAGES="$PAGES ${p#"$OUT"/}"
    done
  done
fi

FAIL=0; N=0
printf '  %-64s %-9s %s\n' PAGE HTTP STAMPS

for rel in $PAGES; do
  f="$OUT/$rel"
  [ -f "$f" ] || { printf '  %-64s %s\n' "$rel" "no local build ❌"; FAIL=1; continue; }

  # The stamped references THIS build wrote into this page.
  refs=$(grep -o '/shared/[A-Za-z0-9._-]*?v=[0-9a-f]*' "$f" | sort -u)

  url="$BASE/$rel"
  body=$(curl -sL --max-time 30 "$url" 2>/dev/null)
  code=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 30 "$url")
  N=$((N+1))

  [ "$code" = "200" ] && c="200 ✅" || { c="$code ❌"; FAIL=1; }

  s="✅"
  missing=""
  while IFS= read -r ref; do
    [ -n "$ref" ] || continue
    grep -qF "$ref" <<<"$body" || missing="$missing $ref"
  done <<<"$refs"
  if [ -n "$missing" ]; then s="❌ stale:$missing"; FAIL=1; fi
  [ -z "$refs" ] && s="⚠️ page stamps nothing"

  printf '  %-64s %-9s %s\n' "$rel" "$c" "$s"
done

echo
echo "checked $N page(s)"
if [ $FAIL -eq 0 ] && [ $N -gt 0 ]; then
  echo "✅ all live on THIS build's assets"
else
  echo "❌ something is off above."
  echo "   'stale' almost always means Cloudflare has not finished deploying"
  echo "   yet — give it a few minutes and re-run before investigating."
  exit 1
fi
