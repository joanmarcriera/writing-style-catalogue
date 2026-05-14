#!/usr/bin/env python3
"""
Generate INDEX.md from markdown files in the repository.
Reads YAML front matter and creates an indexed list of all content files.
"""

import os
import re
from pathlib import Path

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
    if frontmatter and 'description' in frontmatter:
        return frontmatter['description']
    return ''

def generate_section(folder, folder_name):
    """Generate index section for a folder."""
    folder_path = Path(folder)
    if not folder_path.exists():
        return ''

    markdown_files = sorted(folder_path.glob('*.md'))
    if not markdown_files:
        return ''

    lines = [f'## {folder_name}\n']
    for filepath in markdown_files:
        frontmatter = parse_frontmatter(filepath)
        title = get_title(filepath, frontmatter)
        description = get_description(frontmatter)
        relative_path = f'{folder}/{filepath.name}'

        if description:
            lines.append(f'- [{title}]({relative_path}) — {description}')
        else:
            lines.append(f'- [{title}]({relative_path})')

    lines.append('')
    return '\n'.join(lines)

def main():
    """Generate INDEX.md."""
    base_path = Path(__file__).parent.parent

    sections = [
        ('styles', 'Styles'),
        ('prompt-templates', 'Prompt Templates'),
        ('skills', 'Skills'),
        ('examples', 'Examples'),
        ('checklists', 'Checklists'),
        ('reference', 'Reference'),
        ('personal-workflows', 'Personal Workflows'),
    ]

    content = """# Index (Auto-Generated)

This index is generated automatically by `scripts/generate_index.py`.

Run `python scripts/generate_index.py` after adding new files to update this index.

---

"""

    for folder, name in sections:
        section = generate_section(base_path / folder, name)
        content += section

    content += """---

**Note**: This index was auto-generated. Run `python scripts/generate_index.py` to regenerate after adding new files.
"""

    # Write to INDEX.md
    index_path = base_path / 'INDEX.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Generated {index_path}")

if __name__ == '__main__':
    main()
