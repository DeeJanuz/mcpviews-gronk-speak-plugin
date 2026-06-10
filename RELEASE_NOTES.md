# Unreleased

## 0.1.4

- Tightened `GronkSpeak` scope so ordinary final answers, local summaries, directory summaries, repo reports, test summaries, and internal reports stay in GronkSpeak.
- Narrowed exclusions to explicitly public-facing or polished deliverables, plus clarity/safety exceptions.
- Added examples for project-directory summaries and repo state summaries.
- Restored setup consent: setup now asks whether to enable GronkSpeak, explains where it will be used, and shows examples before producing the one `GronkSpeak` startup rule. Choosing Off suppresses fresh installs.

## 0.1.3

- Rewrote the installed `GronkSpeak` startup rule to be self-contained and Caveman-style: terse rule body, persistence, protected-content boundaries, auto-clarity exceptions, and examples.
- Removed references to MCPViews init/session state from the rule text so the native startup rule can stand alone from the first assistant-visible response.
- Kept the plugin to one static startup rule with no setup questions and no mode/scope split.

## 0.1.2

- Replaced split mode/scope startup rules with one self-contained `GronkSpeak` startup rule.
- Removed setup-question-sourced startup behavior from the installed rule path so future installs seed one native project rule with scope, exclusions, precedence, and examples.
- Removed `init_session`-dependent wording from the installed GronkSpeak rule text.

## 0.1.1

- Added setup-answer-sourced `startup_rules` so MCPViews can prompt agents to install Gronk mode/scope into native harness rules before the next session starts.
- Hardened Gronk Speak persisted rules so enabled modes explicitly apply after persisted MCPViews rules or `init_session` are loaded.
- Clarified that chat/status scope includes commentary progress updates, setup acknowledgements, tool-use narration, exploration updates, corrections, and ordinary conversational final answers.
