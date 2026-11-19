#!/usr/bin/env bash
# Wraps index.html into a full HTML document in dist/ for deploying to Netlify or any static host.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist
{
  printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
  cat index.html
  printf '\n</html>\n'
} > dist/index.html
echo "Built dist/index.html"
