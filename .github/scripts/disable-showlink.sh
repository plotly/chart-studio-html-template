#!/bin/bash

# Modify Plotly chart HTML files to disable showLink

cd charts

for file in *.html; do
    # Skip index.html
    if [ "$file" = "index.html" ]; then
        continue
    fi

    # Check if file exists and is not empty
    if [ ! -f "$file" ] || [ ! -s "$file" ]; then
        continue
    fi

    # Check if modification hasn't already been done
    if grep -q '"showLink"\s*:\s*false' "$file"; then
        echo "$file already has showLink disabled, skipping"
        continue
    fi

    # Replace "showLink": true with "showLink": false
    sed -i.bak 's/"showLink"[[:space:]]*:[[:space:]]*true/"showLink": false/g' "$file"

    # Remove backup file
    rm -f "${file}.bak"

    echo "Disabled showLink in $file"
done
