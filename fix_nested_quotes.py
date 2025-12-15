#!/usr/bin/env python3
"""
Fix YAML frontmatter with nested quotes
"""

import glob
import re
from pathlib import Path

def fix_nested_quotes(content):
    """
    Fix title fields that have nested double quotes
    Change from: title: "Text "quoted" text"
    To: title: 'Text "quoted" text'
    """
    lines = content.split('\n')
    fixed = False

    for i, line in enumerate(lines):
        # Match title with double quotes that contain other double quotes
        if re.match(r'^title: ".*".*"', line):
            # Extract the title value between first and last quote
            match = re.match(r'^title: "(.*)"', line)
            if match:
                title_content = match.group(1)
                # Change to single quotes to avoid escaping issues
                lines[i] = f"title: '{title_content}'"
                fixed = True
                print(f"Fixed nested quotes: {title_content[:50]}...")

    if fixed:
        return '\n'.join(lines)
    return content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        content = fix_nested_quotes(content)

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

    print("Fixing nested quotes in YAML frontmatter...")
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
