#!/usr/bin/env python3
"""
Fix WordPress image paths and remove Twitter digest posts
"""

import glob
import re
import os
from pathlib import Path

def fix_wordpress_image_paths(content):
    """
    Fix WordPress image paths to use Hugo static directory
    Converts: http://www.nickburaglio.com/wp-content/uploads/...
    To: /wp-content/uploads/...
    """
    # Pattern to match WordPress image URLs
    patterns = [
        (r'http://www\.nickburaglio\.com/wp-content/', '/wp-content/'),
        (r'https://www\.nickburaglio\.com/wp-content/', '/wp-content/'),
        (r'http://nickburaglio\.com/wp-content/', '/wp-content/'),
        (r'https://nickburaglio\.com/wp-content/', '/wp-content/'),
    ]

    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)

    return content

def is_twitter_digest_post(filepath):
    """
    Identify Twitter digest posts by reading the content
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Twitter Tools signature
        has_twitter_tools = 'Powered by [Twitter Tools]' in content or 'Twitter Tools' in content

        # Check title for "Twitter Updates"
        title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
        if title_match:
            title = title_match.group(1)
            has_twitter_title = 'Twitter Updates for' in title or 'Twitter updates for' in title
        else:
            has_twitter_title = False

        return has_twitter_tools or has_twitter_title
    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return False

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Apply image path fixes
        content = fix_wordpress_image_paths(content)

        # Only write if changes were made
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

    # Get all markdown files
    markdown_files = list(post_dir.glob('*.md'))
    total_files = len(markdown_files)

    # First pass: Fix image paths
    print("=" * 60)
    print("PHASE 1: Fixing WordPress image paths")
    print("=" * 60)
    modified_files = 0

    for i, filepath in enumerate(markdown_files, 1):
        if process_file(filepath):
            modified_files += 1

        if i % 50 == 0:
            print(f"Processed {i}/{total_files} files...")

    print(f"\nImage path fixes complete!")
    print(f"Files modified: {modified_files}")

    # Second pass: Identify and remove Twitter digest posts
    print("\n" + "=" * 60)
    print("PHASE 2: Removing Twitter digest posts")
    print("=" * 60)

    twitter_posts = []
    for filepath in markdown_files:
        if is_twitter_digest_post(filepath):
            twitter_posts.append(filepath)

    print(f"Found {len(twitter_posts)} Twitter digest posts")

    if twitter_posts:
        print("\nRemoving Twitter digest posts...")
        for filepath in twitter_posts:
            try:
                os.remove(filepath)
                print(f"Removed: {filepath.name}")
            except Exception as e:
                print(f"Error removing {filepath.name}: {e}")

        print(f"\nRemoved {len(twitter_posts)} Twitter digest posts")

    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)

if __name__ == '__main__':
    main()
