#!/bin/bash

# Inject CSS to hide Plotly Chart Studio links in all chart HTML files

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

    # Check if CSS hasn't already been injected
    if grep -q "hide-plotly-link-injection" "$file"; then
        continue
    fi

    # Inject CSS before the closing </head> tag to hide the Chart Studio link
    sed -i.bak '/<\/head>/i\
    <style class="hide-plotly-link-injection">\
        /* Hide Chart Studio export link */\
        a[href*="chart-studio.plotly.com"],\
        a[data-title*="chart-studio"],\
        .modebar-btn[data-title*="Produced with Plotly"],\
        .modebar-btn[data-title*="Edit chart"],\
        .js-plotly-plot .plotly a.modebar-btn[data-title="Produced with Plotly"] {\
            display: none !important;\
        }\
    </style>
' "$file"

    # Remove backup file
    rm -f "${file}.bak"

    echo "Injected CSS into $file"
done
