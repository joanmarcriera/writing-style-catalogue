#!/usr/bin/env python3
"""Generate static catalogue data for the GitHub Pages UI."""

import json
import re
from pathlib import Path

from bundle_contract import load_bundles


BASE_PATH = Path(__file__).parent.parent
OUTPUT_PATH = BASE_PATH / "assets" / "catalogue-data.js"

SECTIONS = [
    ("styles", "Styles", "style"),
    ("patterns", "Patterns", "pattern"),
    ("prompt-templates", "Prompt Templates", "template"),
    ("meta-prompts", "Meta Prompts", "meta-prompt"),
    ("skills", "Skills", "skill"),
    ("personal-workflows", "Personal Workflows", "workflow"),
    ("examples", "Examples", "example"),
    ("checklists", "Checklists", "checklist"),
    ("rubrics", "Rubrics", "rubric"),
    ("reference", "Reference", "reference"),
]


def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}, text

    data = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')

    return data, text[match.end():]


def title_from_path(path):
    return path.stem.replace("-", " ").title()


def markdown_excerpt(body, limit=220):
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    body = re.sub(r"`([^`]+)`", r"\1", body)
    body = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", body)
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"^#+\s*", "", body, flags=re.MULTILINE)
    body = re.sub(r"[*_>#|-]", " ", body)
    body = re.sub(r"\s+", " ", body).strip()
    if len(body) <= limit:
        return body
    return body[:limit].rsplit(" ", 1)[0] + "..."


def description(frontmatter, body):
    for key in ("description", "use_case", "output", "best_for"):
        value = frontmatter.get(key)
        if value:
            if len(value) > 220:
                return value[:220].rsplit(" ", 1)[0] + "..."
            return value
    return markdown_excerpt(body)


def build_item(path, section_name, kind):
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    rel = path.relative_to(BASE_PATH).as_posix()
    return {
        "title": frontmatter.get("title") or title_from_path(path),
        "path": rel,
        "section": section_name,
        "kind": kind,
        "description": description(frontmatter, body),
        "category": frontmatter.get("category", ""),
        "audience": frontmatter.get("audience", ""),
        "templateType": frontmatter.get("template_type", ""),
    }


def main():
    sections = []
    items = []

    for folder, label, kind in SECTIONS:
        folder_path = BASE_PATH / folder
        files = sorted(folder_path.glob("*.md")) if folder_path.exists() else []
        section_items = [build_item(path, label, kind) for path in files]
        sections.append(
            {
                "folder": folder,
                "label": label,
                "kind": kind,
                "count": len(section_items),
            }
        )
        items.extend(section_items)

    payload = {
        "generatedFrom": "scripts/generate_site_data.py",
        "sections": sections,
        "items": items,
        "bundles": load_bundles(BASE_PATH),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        "window.CATALOGUE_DATA = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Generated {OUTPUT_PATH.relative_to(BASE_PATH)}")


if __name__ == "__main__":
    main()
