#!/usr/bin/env python3

import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

def parse_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    frontmatter = match.group(1)
    metadata = {}

    title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip('"\'')

    date_match = re.search(r'^date:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    if date_match:
        metadata['date'] = date_match.group(1).strip('"\'')

    tags_match = re.search(r'^tags:\s*\[(.*?)\]', frontmatter, re.MULTILINE)
    if tags_match:
        tags_str = tags_match.group(1)
        tags = [tag.strip().strip('"\'') for tag in tags_str.split(',')]
        metadata['tags'] = [tag for tag in tags if tag]
    
    return metadata

def format_date(date_str):
    if not date_str:
        return ""
    
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime("%b %-d, %Y")
    except:
        return date_str

def generate_tags_html(tags):
    if not tags:
        return ""
    
    tag_elements = []
    for tag in tags:
        tag_elements.append(f'    <span class="tag">#{tag}</span>')
    
    return '\n'.join(tag_elements)

def sanitize_filename(title):
    sanitized = re.sub(r'[^a-zA-Z0-9 ]', '', title)
    sanitized = re.sub(r'\s+', '-', sanitized)
    return sanitized

def extract_metadata_from_built_page(md_file_path):
    md_path = Path(md_file_path)
    filename_stem = md_path.stem
    built_html = Path('public') / filename_stem / 'index.html'
    
    if not built_html.exists():
        print(f"  Warning: Built page not found at {built_html}")
        return None, None
    
    try:
        with open(built_html, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata_match = re.search(r'(\d+)\s+words\s+•\s+(\d+)\s+mins', content)
        if metadata_match:
            word_count = metadata_match.group(1)
            read_time = metadata_match.group(2)
            return word_count, read_time
        
    except Exception as e:
        print(f"  Error reading built page: {e}")
    
    return None, None

def generate_og_image(md_file, template_path, output_dir):
    print(f"Processing: {md_file}")
    
    metadata = parse_frontmatter(md_file)
    
    if 'title' not in metadata:
        print(f"  Skipping: No title found")
        return
    
    title = metadata['title']
    print(f"  Creating thumbnail for: {title}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    formatted_date = format_date(metadata.get('date', ''))
    tags_html = generate_tags_html(metadata.get('tags', []))
    word_count, read_time = extract_metadata_from_built_page(md_file)
    if word_count is None:
        word_count = '0'
        read_time = '0'
    
    html = html.replace('{title}', title)
    html = html.replace('{date}', formatted_date)
    html = html.replace('{tags}', tags_html)
    html = html.replace('{word_count}', str(word_count))
    html = html.replace('{read_time}', str(read_time))

    temp_html = 'temp_og_image.html'
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html)

    try:
        subprocess.run([
            'google-chrome-stable',
            '--headless',
            '--screenshot',
            '--window-size=1200,630',
            '--virtual-time-budget=5000',
            temp_html
        ], check=True)
        
        sanitized_title = sanitize_filename(title)
        output_file = os.path.join(output_dir, f"{sanitized_title}.png")
        
        if os.path.exists('screenshot.png'):
            os.makedirs(output_dir, exist_ok=True)
            os.rename('screenshot.png', output_file)
            print(f"  Created: {sanitized_title}.png")
        
    except subprocess.CalledProcessError as e:
        print(f"  Error generating screenshot: {e}")
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)

def main():
    content_dir = 'content/posts'
    template_path = 'og_image_template.html'
    output_dir = 'static/images'
    
    md_files = Path(content_dir).rglob('*.md')
    
    for md_file in md_files:
        if md_file.name == '_index.md':
            continue
        
        generate_og_image(md_file, template_path, output_dir)

if __name__ == '__main__':
    main()