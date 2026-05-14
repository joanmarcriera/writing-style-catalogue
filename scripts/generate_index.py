#!/usr/bin/env python3
"""
Generate INDEX.md from markdown files in the repository.
Reads YAML front matter and creates an indexed list of all content files.
"""

import re
from pathlib import Path

MAX_DESCRIPTION_LENGTH = 180


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match YAML frontmatter
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            return None

        frontmatter = {}
        for line in match.group(1).split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def get_title(filepath, frontmatter):
    """Get title from frontmatter or filename."""
    if frontmatter and 'title' in frontmatter:
        return frontmatter['title']
    # Fallback: convert filename to title
    return filepath.stem.replace('-', ' ').title()

def get_description(frontmatter):
    """Get description from frontmatter."""
    if not frontmatter:
        return ''

    for key in ('description', 'use_case', 'output', 'best_for'):
        if key in frontmatter and frontmatter[key]:
            description = frontmatter[key]
            if len(description) > MAX_DESCRIPTION_LENGTH:
                return description[:MAX_DESCRIPTION_LENGTH].rstrip() + '…'
            return description
    return ''

def format_index_line(filepath, relative_path):
    """Format one Markdown file as an index bullet."""
    frontmatter = parse_frontmatter(filepath)
    title = get_title(filepath, frontmatter)
    description = get_description(frontmatter)

    if description:
        return f'- [{title}]({relative_path}) — {description}'
    return f'- [{title}]({relative_path})'


def generate_root_section(base_path, files):
    """Generate index section for selected root navigation files."""
    lines = ['## Navigation', '']
    for filename in files:
        filepath = base_path / filename
        if filepath.exists():
            lines.append(format_index_line(filepath, filename))
    lines.append('')
    return '\n'.join(lines) + '\n'


def generate_section(base_path, folder, folder_name):
    """Generate index section for a folder."""
    folder_path = base_path / folder
    if not folder_path.exists():
        return ''

    markdown_files = sorted(folder_path.glob('*.md'))
    if not markdown_files:
        return ''

    lines = [f'## {folder_name}', '']
    for filepath in markdown_files:
        relative_path = filepath.relative_to(base_path).as_posix()
        lines.append(format_index_line(filepath, relative_path))

    lines.append('')
    return '\n'.join(lines) + '\n'

def main():
    """Generate INDEX.md."""
    base_path = Path(__file__).parent.parent

    root_files = [
        'START-HERE.md',
        'CHEATSHEET.md',
        'STYLE-SELECTION-GUIDE.md',
        'REPO-MAP.md',
        'QUICKSTART.md',
        'README.md',
        'CONTRIBUTING.md',
    ]

    sections = [
        ('styles', 'Styles'),
        ('patterns', 'Patterns'),
        ('prompt-templates', 'Prompt Templates'),
        ('meta-prompts', 'Meta Prompts'),
        ('skills', 'Skills'),
        ('examples', 'Examples'),
        ('checklists', 'Checklists'),
        ('rubrics', 'Rubrics'),
        ('reference', 'Reference'),
        ('personal-workflows', 'Personal Workflows'),
    ]

    content = """# Index (Auto-Generated)

This index is generated automatically by `scripts/generate_index.py`.

Run `python3 scripts/generate_index.py` after adding new files to update this index.

---

"""

    content += generate_root_section(base_path, root_files)

    for folder, name in sections:
        section = generate_section(base_path, folder, name)
        content += section

    content += """---

**Note**: This index was auto-generated. Run `python3 scripts/generate_index.py` to regenerate after adding new files.
"""

    # Write to INDEX.md
    index_path = base_path / 'INDEX.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Generated {index_path}")

if __name__ == '__main__':
    main()
