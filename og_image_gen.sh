#!/bin/bash

convert_date() {
    local input_date="$1"
    if [[ -n "$input_date" ]]; then
        date -d "$input_date" "+%b %-d, %Y" 2>/dev/null || echo "$input_date"
    fi
}

format_tags() {
    local tags_line="$1"
    local tags_content=$(echo "$tags_line" | sed -n 's/.*\[\(.*\)\].*/\1/p')
    
    if [[ -n "$tags_content" ]]; then
        # split by comma, trim whitespace, remove quotes, add # prefix
        echo "$tags_content" | sed 's/[",]/ /g' | tr -s ' ' | sed 's/^ *//;s/ *$//' | sed 's/ /, #/g' | sed 's/^/#/'
    fi
}

find content/ -name "*.md" -type f ! -name "_index.md" | while read -r file; do
    echo "Processing: $file"
    
    title=""
    date=""
    tags=""
    
    in_frontmatter=false
    while IFS= read -r line; do
        if [[ "$line" =~ ^---$ ]]; then
            if [[ "$in_frontmatter" == false ]]; then
                in_frontmatter=true
                continue
            else
                break
            fi
        fi
        
        if [[ "$in_frontmatter" == true ]]; then
            if [[ "$line" =~ ^title:[[:space:]]*\"(.*)\"$ ]]; then
                title="${BASH_REMATCH[1]}"
            elif [[ "$line" =~ ^title:[[:space:]]*(.*)$ ]]; then
                title="${BASH_REMATCH[1]}"
                title=$(echo "$title" | sed 's/^"//;s/"$//')
            fi
            
            if [[ "$line" =~ ^date:[[:space:]]*(.*)$ ]]; then
                date="${BASH_REMATCH[1]}"
                date=$(echo "$date" | sed 's/^"//;s/"$//')
            fi
            
            if [[ "$line" =~ ^tags:[[:space:]]*\[(.*)\]$ ]]; then
                tags="${BASH_REMATCH[1]}"
            fi
        fi
    done < "$file"
    
    if [[ -n "$title" ]]; then
        echo "Creating thumbnail for: $title"
        
        cp og_image_template.html copied.html
        
        formatted_date=""
        if [[ -n "$date" ]]; then
            formatted_date=$(convert_date "$date")
        fi
        
        formatted_tags=""
        if [[ -n "$tags" ]]; then
            formatted_tags=$(format_tags "tags: [$tags]")
        fi
        
        sed -i "s/title/$title/g" copied.html
        sed -i "s/date/$formatted_date/g" copied.html
        sed -i "s/tags/$formatted_tags/g" copied.html
        
        google-chrome-stable --headless --screenshot --window-size=1200,630 --virtual-time-budget=5000 copied.html
        
        sanitized_title=$(echo "$title" | sed 's/[^a-zA-Z0-9 ]//g' | sed 's/ /-/g')
        if [[ -f "screenshot.png" ]]; then
            mv screenshot.png static/images/"${sanitized_title}.png"
            echo "Created: ${sanitized_title}.png"
        fi
        
        rm -f copied.html
    fi
done