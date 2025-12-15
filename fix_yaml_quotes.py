#!/usr/bin/env python3
"""
Fix YAML frontmatter quotes - change single quotes to double quotes for titles with apostrophes
"""

import glob
import re
from pathlib import Path

def fix_yaml_title_quotes(content):
    """
    Fix title fields that have apostrophes inside single quotes
    Change from: title: 'I'm a title'
    To: title: "I'm a title"
    """
    # Pattern to match title with single quotes that contain apostrophes
    pattern = r"^title: '([^']*'[^']*)'$"

    lines = content.split('\n')
    fixed = False

    for i, line in enumerate(lines):
        match = re.match(pattern, line)
        if match:
            # Extract the title content
            title_content = match.group(1)
            # Replace with double quotes
            lines[i] = f'title: "{title_content}"'
            fixed = True

    if fixed:
        return '\n'.join(lines)
    return content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        content = fix_yaml_title_quotes(content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main execution function"""
    post_dir = Path('/Users/buraglio/Documents/Dev/nickburaglio.com/content/post')

    if not post_dir.exists():
        print(f"Error: Directory not found: {post_dir}")
        return

    markdown_files = list(post_dir.glob('*.md'))
    total_files = len(markdown_files)
    modified_files = 0

    print("Fixing YAML frontmatter quotes...")
    print("=" * 60)

    for filepath in markdown_files:
        if process_file(filepath):
            modified_files += 1
            print(f"Fixed: {filepath.name}")

    print("=" * 60)
    print(f"Complete!")
    print(f"Total files: {total_files}")
    print(f"Files modified: {modified_files}")

if __name__ == '__main__':
    main()
