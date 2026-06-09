#!/usr/bin/env bash
set -euo pipefail

PLUGIN_NAME="mcpviews-gronk-speak"
REPO_SLUG="DeeJanuz/mcpviews-gronk-speak-plugin"
ZIP_NAME="${PLUGIN_NAME}.zip"
RELEASE_DIR="release"

echo "Building ${ZIP_NAME}..."

rm -rf "${RELEASE_DIR}"
mkdir -p "${RELEASE_DIR}"

VERSION=$(python3 -c "import json; print(json.load(open('manifest.json'))['version'])")
DOWNLOAD_URL="https://github.com/${REPO_SLUG}/releases/download/v${VERSION}/${ZIP_NAME}"

python3 - <<PY
import json
from pathlib import Path

path = Path("manifest.json")
manifest = json.loads(path.read_text())
manifest["download_url"] = "${DOWNLOAD_URL}"
path.write_text(json.dumps(manifest, indent=2) + "\\n")
print("  Updated manifest.json download_url")
PY

echo "  Version: ${VERSION}"
echo "  Download URL: ${DOWNLOAD_URL}"

zip -r "${RELEASE_DIR}/${ZIP_NAME}" manifest.json README.md RELEASE_NOTES.md

echo "Built ${RELEASE_DIR}/${ZIP_NAME} ($(du -h "${RELEASE_DIR}/${ZIP_NAME}" | cut -f1))"

