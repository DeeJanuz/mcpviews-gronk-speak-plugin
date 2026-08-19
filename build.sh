#!/usr/bin/env bash
set -euo pipefail

PLUGIN_NAME="mcpviews-gronk-speak"
REPO_SLUG="DeeJanuz/mcpviews-gronk-speak-plugin"
ZIP_NAME="${PLUGIN_NAME}.zip"
RELEASE_DIR="release"

echo "Building ${ZIP_NAME}..."

VERSION=$(python3 -c "import json; print(json.load(open('manifest.json'))['version'])")
DOWNLOAD_URL="https://github.com/${REPO_SLUG}/releases/download/v${VERSION}/${ZIP_NAME}"

echo "  Version: ${VERSION}"
echo "  Download URL: ${DOWNLOAD_URL}"

python3 scripts/validate.py

rm -rf "${RELEASE_DIR:?}"
mkdir -p "${RELEASE_DIR}"

zip -q -j "${RELEASE_DIR}/${ZIP_NAME}" manifest.json README.md RELEASE_NOTES.md THIRD_PARTY_NOTICES.md

python3 scripts/validate.py --archive "${RELEASE_DIR}/${ZIP_NAME}"

echo "Built ${RELEASE_DIR}/${ZIP_NAME} ($(du -h "${RELEASE_DIR}/${ZIP_NAME}" | cut -f1))"
