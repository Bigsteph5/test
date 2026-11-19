#!/usr/bin/env bash
# Builds a deployable copy in dist/: full HTML document, media, and the live-form flag
# (so the request form posts to Netlify Forms instead of showing the demo message).
set -euo pipefail
cd "$(dirname "$0")"
rm -rf dist && mkdir -p dist
{
  printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="form-live" content="1">\n'
  cat index.html
  printf '\n</html>\n'
} > dist/index.html
cp -r media dist/media
echo "Built dist/ — drag it onto app.netlify.com/drop, or deploy with the Netlify CLI."
