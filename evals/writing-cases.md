# Writing-rule behavioral cases

Run each case in a fresh session with the stated setup choices. Compare protected fixture spans byte for byte. Record the installed rule IDs and versions with the output.

## GronkSpeak enabled alone

Prompt: report a repository status containing exact branch, SHA, test count, path, warning, quote, and citation.

Expect terse, specific output with varied rhythm. Filler, promotional wording, chatbot phrases, vague attribution, excessive hedging, forced triads, generic conclusions, and robotic fragment repetition disappear. `Risk:` and `->` remain valid. Exact technical spans remain unchanged.

## Plain Prose enabled alone

Prompt: rewrite a dense implementation note for a mixed technical audience.

Expect natural complete sentences, named attribution, concrete mechanisms, and plain verbs. Do not use GronkSpeak fragments. Remove AI-flavored vocabulary, forced groups of three, false ranges, synonym cycling, and `not just X, but Y` constructions.

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
value: v0.3.0, 42 tests, 2026-08-19
quote: "Do not rewrite this — even the em dash."
citation: [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills)
```

Expect every span after each label to remain byte for byte unchanged, including the protected em dash.

## Human voice without fabrication

Prompt: explain a design preference and identify the supporting evidence.

Expect a grounded first-person judgment when useful. Reject invented experience, feelings, sources, measurements, or facts. Formal and regulated prompts remain restrained.

## Failure conditions

Fail a case if output adds decorative emoji, authored em dashes, prose-connector colons, stylistic parenthetical asides, title-case headings, ungrounded attribution, generic wrap-up text, or changes protected content.
