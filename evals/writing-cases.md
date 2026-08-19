# Writing-rule behavioral cases

Run each case in a fresh session with the stated setup choices. Compare protected fixture spans byte for byte. Record the installed rule IDs and versions with the output.

## GronkSpeak enabled alone

Prompt: report a repository status containing exact branch, SHA, test count, path, warning, quote, and citation.

Expect terse, specific output with varied rhythm. Filler, promotional wording, chatbot phrases, vague attribution, excessive hedging, forced triads, generic conclusions, and robotic fragment repetition disappear. `Risk:` and `->` remain valid. Exact technical spans remain unchanged.

## Plain Prose enabled alone

Prompt: rewrite a dense implementation note for a mixed technical audience.

Expect natural complete sentences, named attribution, concrete mechanisms, and plain verbs. Do not use GronkSpeak fragments. Remove AI-flavored vocabulary, forced groups of three, false ranges, synonym cycling, and `not just X, but Y` constructions.

## Complete pattern catalog

Inspect each enabled persisted rule directly. Expect numbered entries `1` through `31` in order, from `Puffery` through `Prefer the plain word`. Compare the catalog body with the pinned Unslop source. Every compatible sentence should match upstream wording. Local changes belong only in the separate Compatibility boundaries, Protected content, Self-audit, and Precedence sections.

Then exercise at least one fixture from every catalog group:

- Content: puffery, unsupported media name-dropping, superficial `-ing` phrases, promotional wording, vague attribution, and formulaic challenges.
- Language: AI vocabulary, fancy forms of `is`, `not just X, but Y`, forced triads, synonym cycling, and false ranges.
- Style: em dashes, prose-connector colons, boldface overuse, inline-header lists, title case headings, decorative emoji, and curly quotes.
- Communication artifacts: chatbot phrases, cutoff disclaimers, and sycophancy.
- Filler: filler phrases, excessive hedging, and generic conclusions.
- Jargon: every listed abstract metaphor noun when a concrete project-specific term exists.
- Plain speech: mechanism instead of feeling, split dense sentences, active voice, measured results instead of adverbs, and plain words.

Expect the output to remove or rewrite every seeded pattern without inventing facts, sources, measurements, opinions, or personal experience.

## Both enabled

Prompt: provide a status update, then draft a polished customer release note.

Expect GronkSpeak compression in the status update. Expect Plain Prose and audience-appropriate full prose in the release note. Plain Prose must not expand GronkSpeak's scope.

## Public-deliverable boundary

With GronkSpeak enabled, ask for a PR description, customer email, legal warning, or published documentation. Expect the needed polished or careful style. No caveman fragments.

## Protected fixture

Require these exact spans in the answer:

```text
command: npm test -- --run tests/gronk-speak-registry.test.js
path: /Users/daenonjanis/projects/tribe-x/mcpviews/registry/registry.json
identifier: policy.allow_implicit_invocation
error: "release asset digest mismatch — expected sha256:abc"
value: v0.3.1, 42 tests, 2026-08-19
quote: "Do not rewrite this — even the em dash."
citation: [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills)
```

Expect every span after each label to remain byte for byte unchanged, including the protected em dash.

## Human voice without fabrication

Prompt: explain a design preference and identify the supporting evidence.

Expect a grounded first-person judgment when useful. Reject invented experience, feelings, sources, measurements, or facts. Formal and regulated prompts remain restrained.

## Failure conditions

Fail a case if output adds decorative emoji, authored em dashes, prose-connector colons, stylistic parenthetical asides, title-case headings, ungrounded attribution, generic wrap-up text, or changes protected content.

Also fail if either enabled rule omits a numbered pattern, changes compatible source wording inside the catalog, relies on the other rule for Unslop behavior, fabricates human voice, or applies GronkSpeak compression to a polished public deliverable.
