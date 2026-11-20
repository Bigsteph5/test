#!/usr/bin/env bash
# Builds a deployable folder for one lead: leads/dist/<slug>/ with index.html (live form on) and media.
set -euo pipefail
cd "$(dirname "$0")"
slug="$1"; out="dist/$slug"
rm -rf "$out" && mkdir -p "$out"
{
  printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="form-live" content="1">\n'
  sed 's#="../../media/#="media/#g' "$slug/index.html"
  printf '\n</html>\n'
} > "$out/index.html"
cp -r ../media "$out/media"
echo "$out"
