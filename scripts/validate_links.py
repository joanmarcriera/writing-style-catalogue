#!/usr/bin/env python3
"""
Validate internal links.

Checks that every relative [text](path) link and ![alt](path) image in the
Markdown files, and every relative href/src in index.html, points to an
existing file or directory. Fragments such as page.md#section or #section
are checked against the headings (and explicit id/name anchors) of the
target Markdown file.
"""

import re
from pathlib import Path

LINK_PATTERN = re.compile(r'!?\[([^\]]+)\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
HTML_ATTR_PATTERN = re.compile(r'(?:href|src)="([^"]+)"')
SCHEME_PATTERN = re.compile(r'^[a-z][a-z0-9+.-]*:', re.IGNORECASE)
HTML_FILES = ('index.html',)


def find_markdown_links(content):
    """Extract all relative markdown links and images from content."""
    links = []
    for text, path in LINK_PATTERN.findall(content):
        path = path.strip()
        if SCHEME_PATTERN.match(path):
            continue
        links.append((text, path))
    return links


def find_html_links(content):
    """Extract relative href and src values from an HTML page."""
    return [
        (value, value)
        for value in HTML_ATTR_PATTERN.findall(content)
        if not SCHEME_PATTERN.match(value) and not value.startswith('//')
    ]


def heading_slug(heading):
    """Approximate GitHub's heading anchor algorithm."""
    heading = re.sub(r'`([^`]*)`', r'\1', heading)
    heading = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', heading)
    heading = re.sub(r'[^\w\- ]', '', heading.strip().lower())
    return heading.replace(' ', '-')


_anchor_cache = {}


def file_anchors(path):
    """Return the set of anchors a Markdown or HTML file exposes."""
    if path in _anchor_cache:
        return _anchor_cache[path]
    text = path.read_text(encoding='utf-8')
    anchors = set(re.findall(r'\b(?:id|name)="([^"]+)"', text))
    if path.suffix == '.md':
        seen = {}
        in_fence = False
        for line in text.splitlines():
            if line.lstrip().startswith('```'):
                in_fence = not in_fence
                continue
            match = None if in_fence else re.match(r'^#{1,6}\s+(.*?)\s*#*\s*$', line)
            if match:
                slug = heading_slug(match.group(1))
                count = seen.get(slug, 0)
                seen[slug] = count + 1
                anchors.add(slug if count == 0 else f'{slug}-{count}')
    _anchor_cache[path] = anchors
    return anchors


def validate_link(base_path, current_file, link_path):
    """Validate a single link, including any #fragment."""
    target, _, fragment = link_path.partition('#')
    target_path = (current_file.parent / target).resolve() if target else current_file

    if not target_path.exists():
        return False, str(target_path)
    if fragment and target_path.is_file() and target_path.suffix in ('.md', '.html'):
        if fragment not in file_anchors(target_path):
            return False, f'{target_path}#{fragment} (no such anchor)'
    return True, None


def main():
    """Validate all internal links."""
    base_path = Path(__file__).parent.parent
    all_markdown = [
        path for path in base_path.rglob('*.md')
        if '.git' not in path.parts
        and '.claude' not in path.parts
        and path.name != 'AGENTS.md'
    ]
    html_files = [base_path / name for name in HTML_FILES if (base_path / name).is_file()]

    broken_links = []
    checked = 0

    for filepath in all_markdown + html_files:
        try:
            content = filepath.read_text(encoding='utf-8')
            if filepath.suffix == '.html':
                links = find_html_links(content)
            else:
                links = find_markdown_links(content)
            for text, link_path in links:
                checked += 1
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
        print(
            f"✓ All internal links are valid ({checked} links in "
            f"{len(all_markdown) + len(html_files)} files checked)"
        )
        return 0

if __name__ == '__main__':
    exit(main())
