#!/usr/bin/env python3
"""Validate the GronkSpeak manifest and optional release archive."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import zipfile


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "manifest.json"
EXPECTED_NAME = "mcpviews-gronk-speak"
EXPECTED_VERSION = "0.3.0"
EXPECTED_RULE_VERSIONS = {"GronkSpeak": "5", "PlainProse": "2"}
EXPECTED_QUESTIONS = {
    "enable_gronk_speak": "GronkSpeak",
    "enable_plain_prose": "PlainProse",
}
EXPECTED_ARCHIVE_FILES = {
    "manifest.json",
    "README.md",
    "RELEASE_NOTES.md",
    "THIRD_PARTY_NOTICES.md",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path)
    return parser.parse_args()


def load_manifest(errors: list[str]) -> dict[str, object]:
    try:
        value = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"manifest.json is not valid readable JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append("manifest.json must contain a JSON object")
        return {}
    return value


def validate_manifest(manifest: dict[str, object], errors: list[str]) -> None:
    require(manifest.get("name") == EXPECTED_NAME, f"name must be {EXPECTED_NAME}", errors)
    require(manifest.get("version") == EXPECTED_VERSION, f"version must be {EXPECTED_VERSION}", errors)
    expected_url = (
        "https://github.com/DeeJanuz/mcpviews-gronk-speak-plugin/releases/"
        f"download/v{EXPECTED_VERSION}/mcpviews-gronk-speak.zip"
    )
    require(manifest.get("download_url") == expected_url, "download_url must match manifest version", errors)

    questions = manifest.get("setup_questions")
    rules = manifest.get("startup_rules")
    require(isinstance(questions, list), "setup_questions must be a list", errors)
    require(isinstance(rules, list), "startup_rules must be a list", errors)
    if not isinstance(questions, list) or not isinstance(rules, list):
        return

    question_ids = [
        item.get("id")
        for item in questions
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    ]
    rule_ids = [
        item.get("id")
        for item in rules
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    ]
    require(len(question_ids) == len(questions), "every setup question needs a string ID", errors)
    require(len(rule_ids) == len(rules), "every startup rule needs a string ID", errors)
    require(len(question_ids) == len(set(question_ids)), "setup question IDs must be unique", errors)
    require(len(rule_ids) == len(set(rule_ids)), "startup rule IDs must be unique", errors)
    require(set(question_ids) == set(EXPECTED_QUESTIONS), "setup question IDs changed", errors)
    require(set(rule_ids) == set(EXPECTED_RULE_VERSIONS), "startup rule IDs changed", errors)

    question_map = {
        item["id"]: item
        for item in questions
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    for rule in rules:
        if not isinstance(rule, dict):
            errors.append("each startup rule must be an object")
            continue
        rule_id = rule.get("id")
        if not isinstance(rule_id, str):
            errors.append("each startup rule needs a string ID")
            continue
        require(
            rule.get("version") == EXPECTED_RULE_VERSIONS.get(rule_id),
            f"{rule_id} has the wrong rule version",
            errors,
        )
        source = rule.get("source")
        require(isinstance(source, dict), f"{rule_id} must have a source object", errors)
        if not isinstance(source, dict):
            continue
        question_id = source.get("question_id")
        require(source.get("type") == "setup_question", f"{rule_id} must use a setup question", errors)
        if not isinstance(question_id, str):
            errors.append(f"{rule_id} must reference a string question_id")
            continue
        require(question_id in question_map, f"{rule_id} references a missing question", errors)
        skip_values = source.get("skip_install_values")
        require(isinstance(skip_values, list), f"{rule_id} skip_install_values must be a list", errors)
        require(isinstance(skip_values, list) and "off" in skip_values, f"{rule_id} Off must suppress installation", errors)
        question = question_map.get(question_id)
        if not isinstance(question, dict):
            continue
        require(
            question.get("persist_as_rule_name") == EXPECTED_QUESTIONS.get(question_id),
            f"{question_id} persist_as_rule_name changed",
            errors,
        )
        options = question.get("options")
        require(isinstance(options, list), f"{question_id} options must be a list", errors)
        if not isinstance(options, list):
            continue
        option_values = [
            item.get("value")
            for item in options
            if isinstance(item, dict) and isinstance(item.get("value"), str)
        ]
        require(len(option_values) == len(options), f"{question_id} options need string values", errors)
        require(len(option_values) == len(set(option_values)), f"{question_id} option values must be unique", errors)
        option_map = {
            item["value"]: item
            for item in options
            if isinstance(item, dict) and isinstance(item.get("value"), str)
        }
        enabled = option_map.get("enabled")
        off = option_map.get("off")
        require(isinstance(enabled, dict), f"{question_id} needs an enabled option", errors)
        require(isinstance(off, dict), f"{question_id} needs an Off option", errors)
        if isinstance(off, dict):
            require(nonempty_string(off.get("persisted_rule")), f"{question_id} Off rule must be nonempty", errors)
        if not isinstance(enabled, dict):
            continue
        text = enabled.get("persisted_rule")
        require(nonempty_string(text), f"{question_id} enabled rule must be nonempty", errors)
        if not isinstance(text, str):
            continue
        for heading in ("Scope:", "Writing baseline:", "Protected content:", "Self-audit:", "Precedence:"):
            require(heading in text, f"{rule_id} is missing {heading}", errors)
        for behavior in (
            "puffery",
            "chatbot phrases",
            "named source",
            "forced groups of three",
            "active voice",
            "em dashes",
            "machine-generated" if rule_id == "PlainProse" else "AI-flavored vocabulary",
        ):
            require(behavior in text, f"{rule_id} lacks independent Unslop behavior: {behavior}", errors)
        for protected in (
            "code",
            "commands",
            "file paths",
            "identifiers",
            "schemas",
            "API names",
            "errors",
            "citations",
            "exact values",
            "direct quotations",
        ):
            require(protected in text, f"{rule_id} does not protect {protected}", errors)
        require("User instructions" in text, f"{rule_id} lacks precedence behavior", errors)


def validate_archive(path: Path, errors: list[str]) -> None:
    require(path.is_file(), f"release archive does not exist: {path}", errors)
    if not path.is_file():
        return
    try:
        with zipfile.ZipFile(path) as archive:
            raw_names = archive.namelist()
            names = set(raw_names)
            require(names == EXPECTED_ARCHIVE_FILES, "release ZIP file set is not exact", errors)
            require(len(raw_names) == len(EXPECTED_ARCHIVE_FILES), "release ZIP contains duplicate entries", errors)
            for name in EXPECTED_ARCHIVE_FILES & names:
                source = (ROOT / name).read_bytes()
                require(archive.read(name) == source, f"release ZIP {name} differs from working tree", errors)
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(f"release archive is invalid: {exc}")


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    manifest = load_manifest(errors)
    if manifest:
        validate_manifest(manifest, errors)
    if args.archive is not None:
        validate_archive(args.archive.resolve(), errors)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    suffix = f" and {args.archive}" if args.archive is not None else ""
    print(f"Validation passed: manifest{suffix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
