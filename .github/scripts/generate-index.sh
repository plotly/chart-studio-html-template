#!/bin/bash

# Generate index.html with links to all charts

cd charts

cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chart Gallery</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        h1 {
            color: #119dff;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .plotly-logo {
            font-weight: 700;
            color: #119dff;
        }

        .subtitle {
            color: #7f8c8d;
            font-size: 1.1rem;
        }

        .powered-by {
            margin-top: 1rem;
            font-size: 0.9rem;
            color: #95a5a6;
        }

        .powered-by a {
            color: #119dff;
            text-decoration: none;
        }

        .powered-by a:hover {
            text-decoration: underline;
        }

        .chart-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .chart-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .chart-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .chart-card a {
            text-decoration: none;
            color: #119dff;
            font-size: 1.1rem;
            font-weight: 500;
            display: block;
        }

        .chart-card a:hover {
            color: #0d7ec9;
        }

        .chart-name {
            margin-top: 0.5rem;
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        .copy-button {
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            background: #119dff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.2s;
        }

        .copy-button:hover {
            background: #0d7ec9;
        }

        .copy-button.copied {
            background: #27ae60;
        }

        .empty-state {
            background: white;
            border-radius: 8px;
            padding: 3rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .empty-state h2 {
            color: #7f8c8d;
            margin-bottom: 1rem;
        }

        .empty-state p {
            color: #95a5a6;
        }
    </style>
    <script>
        function copyEmbedCode(filename) {
            // Get the base URL dynamically from the current page
            const baseUrl = window.location.href.replace(/\/[^\/]*$/, '');
            const url = baseUrl + '/' + filename;
            const embedCode = '<iframe src="' + url + '" width="100%" height="600" frameborder="0"></iframe>';

            navigator.clipboard.writeText(embedCode).then(function() {
                const button = event.target;
                const originalText = button.textContent;
                button.textContent = 'Copied!';
                button.classList.add('copied');

                setTimeout(function() {
                    button.textContent = originalText;
                    button.classList.remove('copied');
                }, 2000);
            }).catch(function(err) {
                alert('Failed to copy: ' + err);
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <header>
            <h1><span class="plotly-logo">Plotly</span> Chart Gallery</h1>
            <p class="subtitle">Charts previously hosted on Plotly Chart Studio</p>
        </header>

        <div class="chart-grid">
EOF

# Find all HTML files except index.html and add them to the page
html_files=$(find . -maxdepth 1 -name "*.html" ! -name "index.html" | sort)

if [ -z "$html_files" ]; then
    cat >> index.html << 'EOF'
        </div>
        <div class="empty-state">
            <h2>No Plotly charts yet</h2>
            <p>Export your charts from Chart Studio as HTML and add them to the charts/ folder.</p>
        </div>
EOF
else
    for file in $html_files; do
        filename=$(basename "$file")
        # Convert filename to readable title (remove .html, replace hyphens/underscores with spaces, capitalize)
        title=$(echo "$filename" | sed 's/.html$//' | sed 's/[-_]/ /g' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')

        cat >> index.html << EOF
            <div class="chart-card">
                <a href="$filename">$title</a>
                <div class="chart-name">$filename</div>
                <button class="copy-button" onclick="copyEmbedCode('$filename')">Copy Embed Code</button>
            </div>
EOF
    done

    cat >> index.html << 'EOF'
        </div>
EOF
fi

cat >> index.html << 'EOF'
    </div>
</body>
</html>
EOF

echo "Generated index.html with $(echo "$html_files" | wc -l | tr -d ' ') charts"
