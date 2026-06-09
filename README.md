# MCPViews Gronk Speak Plugin

Optional MCPViews setup rules for Gronk Speak, a terse nonpublic agent output style.

This plugin contributes setup questions only. It does not provide renderers, MCP tools, auth, or a backend service. Installing it makes `mcpviews_setup` ask whether the user wants Gronk Speak mode and scope persisted into their agent rules. Users who do not install the plugin will not see those setup questions.

## Install

Install through the MCPViews plugin manager once the plugin is listed in the registry, or install a release ZIP manually:

```bash
mcpviews-cli plugin install-zip release/mcpviews-gronk-speak.zip
```

## Build

```bash
bash build.sh
```

This writes `release/mcpviews-gronk-speak.zip` with `manifest.json`, `README.md`, and `RELEASE_NOTES.md` at the ZIP root.

## Release

1. Update `manifest.json` `version`.
2. Add notes under `RELEASE_NOTES.md`.
3. Run `bash build.sh`.
4. Commit and push `master`.

The GitHub workflow creates a release named `v<version>` and uploads `mcpviews-gronk-speak.zip`.

