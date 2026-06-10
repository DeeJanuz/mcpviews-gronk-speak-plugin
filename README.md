# MCPViews Gronk Speak Plugin

Optional MCPViews startup rule for GronkSpeak, a terse nonpublic Codex output style.

This plugin contributes one setup-gated startup rule named `GronkSpeak`. It does not provide renderers, MCP tools, auth, or a backend service. During setup, MCPViews asks whether to enable GronkSpeak and shows examples of where it applies. If enabled, MCPViews asks the agent to seed the one `GronkSpeak` rule into the harness-native project rules so the style is available from the first assistant message in a new session.

The enabled rule text contains the full behavior contract: where GronkSpeak applies, where it must not apply, style constraints, precedence rules, and examples. Ordinary final answers, local summaries, findings, inventories, implementation notes, test summaries, and internal reports are in scope. Agents should install it as one native project rule rather than splitting mode/scope fragments across separate rule sections. Choosing Off suppresses fresh installs.

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
