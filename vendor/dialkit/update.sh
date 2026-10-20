#!/bin/sh
# Rebuilds the vendored DialKit vanilla bundle from https://github.com/joshpuckett/dialkit.
# Usage: sh vendor/dialkit/update.sh [git-ref]   (default: main), then run python3 build.py.
set -e
REF=${1:-main}
TMP=$(mktemp -d)
git clone --depth 1 --branch "$REF" https://github.com/joshpuckett/dialkit "$TMP/dialkit"
(cd "$TMP/dialkit" && npm ci --no-audit --no-fund && npx tsup)
DIR=$(dirname "$0")
cp "$TMP/dialkit/dist/vanilla/browser.global.js" "$TMP/dialkit/dist/vanilla/styles.css" "$TMP/dialkit/LICENSE" "$DIR/"
echo "dialkit $(git -C "$TMP/dialkit" rev-parse --short HEAD)" > "$DIR/VERSION"
rm -rf "$TMP"
