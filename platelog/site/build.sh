#!/usr/bin/env bash
# Builds the PlateLog presale site into dist/ for Netlify (drag dist/ onto app.netlify.com/drop,
# or deploy with the Netlify CLI). The founding-spot form uses Netlify Forms.
# Refuses to build while YOUR_PHONE / YOUR_EMAIL placeholders remain.
set -euo pipefail
cd "$(dirname "$0")"
if grep -n "YOUR_" index.html thanks.html; then
  echo "Replace the YOUR_ placeholders above with your real contact details, then rebuild." >&2
  exit 1
fi
rm -rf dist && mkdir -p dist
for f in index.html thanks.html; do
  {
    printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    cat "$f"
    printf '\n</html>\n'
  } > "dist/$f"
done
echo "Built dist/"
