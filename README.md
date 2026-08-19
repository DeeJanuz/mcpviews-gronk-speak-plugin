# MCPViews Gronk Speak Plugin

Independent MCPViews startup rules for terse GronkSpeak and clear Plain Prose. Each enabled rule includes an adapted Unslop baseline for specific, natural writing.

This plugin contributes two independent setup-gated startup rules: `GronkSpeak` and `PlainProse`. It does not provide renderers, MCP tools, auth, or a backend service. During setup, MCPViews asks whether to enable each style and shows examples of where it applies. Enabled choices become separate harness-native project rules so they are available from the first assistant message in a new session.

`GronkSpeak` keeps its existing nonpublic scope and compression rules. It now cuts machine-like filler, vague claims, canned phrasing, and robotic repetition. `PlainProse` governs clarity and word choice across chat, messages, docs, PR text, reports, and other public or private prose without enabling GronkSpeak compression. Either rule works alone. When both apply, Plain Prose governs wording while GronkSpeak may govern fragments and compression only within its existing scope.

Each enabled rule contains its own scope, concrete-writing baseline, protected technical content, punctuation guidance, self-audit, and precedence rules. Agents install each choice as its own native project rule. Choosing Off suppresses that rule's fresh install without changing the other choice. No third Unslop question is added.

The adapted writing baseline favors named sources, observed facts, plain verbs, readable sentences, and audience-aware human voice. It rejects promotional claims, chatbot phrases, excessive hedging, forced symmetry, generic conclusions, and invented opinions. Code, commands, paths, identifiers, schemas, API names, errors, citations, exact values, and quotations remain exact.

## Install

Install through the MCPViews plugin manager once the plugin is listed in the registry, or install a release ZIP manually:

```bash
mcpviews-cli plugin install-zip release/mcpviews-gronk-speak.zip
```

## Build

```bash
bash build.sh
```

The build runs deterministic validation before and after packaging. It writes `release/mcpviews-gronk-speak.zip` with `manifest.json`, `README.md`, `RELEASE_NOTES.md`, and `THIRD_PARTY_NOTICES.md` at the ZIP root.

Run validation without packaging:

```bash
python3 scripts/validate.py
```

## Release

1. Update `manifest.json` `version`.
2. Add notes under `RELEASE_NOTES.md`.
3. Run `bash build.sh`.
4. Commit and push `master`.

The GitHub workflow creates a release named `v<version>` and uploads `mcpviews-gronk-speak.zip`.

## Attribution

The writing baseline adapts ideas from pstack's Unslop skill at pinned commit `60c641e4fad674784b30abcf9f8915dea39df38d`. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
