# MCPViews Gronk Speak Plugin

Optional MCPViews startup rules for GronkSpeak compression and clear Plain Prose.

This plugin contributes two independent setup-gated startup rules: `GronkSpeak` and `PlainProse`. It does not provide renderers, MCP tools, auth, or a backend service. During setup, MCPViews asks whether to enable each style and shows examples of where it applies. Enabled choices become separate harness-native project rules so they are available from the first assistant message in a new session.

`GronkSpeak` keeps its existing nonpublic scope and compression rules. `PlainProse` governs clarity and word choice across chat, messages, docs, PR text, reports, and other public or private prose without enabling GronkSpeak compression. Either rule can be enabled without the other. When both apply, Plain Prose governs wording while GronkSpeak may govern fragments and compression only within its existing scope.

Each enabled rule text contains its full behavior contract, protected technical content, and precedence rules. Agents should install each choice as its own native project rule. Choosing Off suppresses that rule's fresh install without changing the other choice.

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
