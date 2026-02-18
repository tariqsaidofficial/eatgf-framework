#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

# Scan all markdown files for broken links
broken_links = defaultdict(list)
link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

for md_file in Path('.').rglob('*.md'):
    if 'node_modules' in str(md_file) or '.git' in str(md_file):
        continue

    try:
        content = md_file.read_text()
        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_path = match.group(2)

            # Skip external URLs and anchors
            if link_path.startswith(('http://', 'https://', '#', 'mailto:')):
                continue

            # Remove fragment
            link_clean = link_path.split('#')[0]
            if not link_clean:
                continue

            # Convert relative path to absolute
            if link_clean.startswith('../'):
                target = (md_file.parent / link_clean).resolve()
            elif link_clean.startswith('/'):
                target = Path(link_clean)
            else:
                target = (md_file.parent / link_clean).resolve()

            # Check if target exists
            if not target.exists():
                broken_links[str(md_file)].append({
                    'text': link_text,
                    'path': link_path,
                    'target': str(target)
                })
    except Exception as e:
        pass

# Print summary
total = sum(len(v) for v in broken_links.values())
print(f"Total broken links found: {total}")
print(f"Files with broken links: {len(broken_links)}\n")

# Print first examples
count = 0
for file, links in sorted(broken_links.items())[:15]:
    print(f"{file}:")
    for link in links[:2]:
        print(f"  [{link['text']}]({link['path']})")
    if len(links) > 2:
        print(f"  ... and {len(links)-2} more")
    print()
