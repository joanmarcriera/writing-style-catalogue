#!/usr/bin/env python3
"""
Validate internal markdown links.
Checks that all [text](path) links point to existing files.
"""

import re
from pathlib import Path

def find_markdown_links(content):
    """Extract all markdown links from content."""
    # Match [text](path) pattern
    pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    matches = re.findall(pattern, content)
    return [(text, path) for text, path in matches if path.endswith('.md')]

def validate_link(base_path, current_file, link_path):
    """Validate a single link."""
    # Resolve relative path from current file
    current_dir = current_file.parent
    target_path = current_dir / link_path
    target_path = target_path.resolve()

    # Check if file exists
    if target_path.exists() and target_path.is_file():
        return True, None
    else:
        return False, str(target_path)

def main():
    """Validate all internal links."""
    base_path = Path(__file__).parent.parent
    all_markdown = list(base_path.rglob('*.md'))

    broken_links = []

    for filepath in all_markdown:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            links = find_markdown_links(content)
            for text, link_path in links:
                valid, resolved_path = validate_link(base_path, filepath, link_path)
                if not valid:
                    broken_links.append({
                        'file': filepath.relative_to(base_path),
                        'link': link_path,
                        'text': text,
                        'resolved': resolved_path
                    })
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    if broken_links:
        print(f"\n✗ Found {len(broken_links)} broken link(s):\n")
        for item in broken_links:
            print(f"File: {item['file']}")
            print(f"  Link: [{item['text']}]({item['link']})")
            print(f"  Resolved to: {item['resolved']}")
            print()
        return 1
    else:
        print(f"✓ All internal links are valid ({len(all_markdown)} files checked)")
        return 0

if __name__ == '__main__':
    exit(main())
