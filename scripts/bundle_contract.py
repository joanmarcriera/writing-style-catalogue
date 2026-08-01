"""Parse and validate professional prompt bundles stored as Markdown examples."""

from __future__ import annotations

import re
from pathlib import Path


REQUIRED_FRONTMATTER = (
    "bundle_id",
    "artefact",
    "audience",
    "scenario",
    "style_path",
    "pattern_path",
    "prompt_path",
    "rubric_path",
)

REQUIRED_SECTIONS = (
    "Professional context",
    "Source packet",
    "Completed prompt",
    "Output excerpt",
    "Review scorecard",
    "Human review before use",
    "Reuse this bundle",
)

ALLOWED_SCENARIOS = {"labelled-composite", "verified-public-project"}
ALLOWED_GATES = {"Pass", "Revise", "Human check"}
EXPECTED_BUNDLE_COUNT = 12


class BundleContractError(ValueError):
    """Raised when a worked example does not meet the bundle contract."""


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise BundleContractError("missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields, text[match.end():]


def extract_section(body: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^##\s|\Z)"
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def strip_single_fence(value: str) -> str:
    match = re.fullmatch(r"```(?:text|markdown)?\n(.*?)\n```", value.strip(), re.DOTALL)
    return match.group(1).strip() if match else value.strip()


def parse_scorecard(section: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] in {"Criterion", "---"}:
            continue
        if set(cells[0]) == {"-"}:
            continue
        try:
            score = int(cells[1])
        except ValueError as error:
            raise BundleContractError(f"invalid score {cells[1]!r}") from error
        rows.append(
            {
                "criterion": cells[0],
                "score": score,
                "evidence": cells[2],
                "gate": cells[3],
            }
        )
    return rows


def build_bundle(path: Path, base_path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    errors: list[str] = []

    for key in REQUIRED_FRONTMATTER:
        if not fields.get(key):
            errors.append(f"missing frontmatter field {key}")

    if fields.get("scenario") not in ALLOWED_SCENARIOS:
        errors.append("scenario must be labelled-composite or verified-public-project")

    sections = {heading: extract_section(body, heading) for heading in REQUIRED_SECTIONS}
    for heading, content in sections.items():
        if not content:
            errors.append(f"missing or empty section {heading!r}")

    path_keys = ("style_path", "pattern_path", "prompt_path", "rubric_path", "skill_path")
    for key in path_keys:
        relative = fields.get(key)
        if relative and not (base_path / relative).is_file():
            errors.append(f"{key} does not resolve: {relative}")

    prompt = strip_single_fence(sections["Completed prompt"])
    if prompt and len(prompt) < 600:
        errors.append("completed prompt must contain at least 600 characters")
    for phrase in ("MISSING INFORMATION", "Do not invent", "British English"):
        if prompt and phrase not in prompt:
            errors.append(f"completed prompt must include {phrase!r}")

    scorecard = parse_scorecard(sections["Review scorecard"]) if sections["Review scorecard"] else []
    if len(scorecard) < 4:
        errors.append("review scorecard must contain at least four criteria")
    for row in scorecard:
        if row["score"] not in range(1, 6):
            errors.append(f"score outside 1-5 range for {row['criterion']}")
        if row["gate"] not in ALLOWED_GATES:
            errors.append(f"invalid gate for {row['criterion']}: {row['gate']}")
        if row["score"] < 3 and row["gate"] == "Pass":
            errors.append(f"score below 3 cannot pass: {row['criterion']}")

    if errors:
        relative_path = path.relative_to(base_path).as_posix()
        raise BundleContractError(f"{relative_path}: " + "; ".join(errors))

    links = [
        {"kind": "style", "label": "Style", "path": fields["style_path"]},
        {"kind": "pattern", "label": "Pattern", "path": fields["pattern_path"]},
        {"kind": "template", "label": "Prompt", "path": fields["prompt_path"]},
    ]
    if fields.get("skill_path"):
        links.append({"kind": "skill", "label": "Skill", "path": fields["skill_path"]})
    links.extend(
        [
            {"kind": "example", "label": "Example", "path": path.relative_to(base_path).as_posix()},
            {"kind": "rubric", "label": "Rubric", "path": fields["rubric_path"]},
        ]
    )

    return {
        "id": fields["bundle_id"],
        "title": fields.get("title", fields["artefact"]),
        "artefact": fields["artefact"],
        "audience": fields["audience"],
        "scenario": fields["scenario"],
        "description": fields.get("description", ""),
        "sourcePath": path.relative_to(base_path).as_posix(),
        "links": links,
        "context": sections["Professional context"],
        "sourcePacket": strip_single_fence(sections["Source packet"]),
        "prompt": prompt,
        "output": strip_single_fence(sections["Output excerpt"]),
        "scorecard": scorecard,
        "humanReview": sections["Human review before use"],
    }


def load_bundles(base_path: Path) -> list[dict[str, object]]:
    examples = sorted((base_path / "examples").glob("*.md"))
    bundles = [build_bundle(path, base_path) for path in examples]
    ids = [bundle["id"] for bundle in bundles]
    duplicates = sorted({bundle_id for bundle_id in ids if ids.count(bundle_id) > 1})
    if duplicates:
        raise BundleContractError(f"duplicate bundle ids: {', '.join(duplicates)}")
    if len(bundles) != EXPECTED_BUNDLE_COUNT:
        raise BundleContractError(
            f"expected {EXPECTED_BUNDLE_COUNT} bundles, found {len(bundles)}"
        )
    return bundles
