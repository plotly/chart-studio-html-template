#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import json
import os
import sys

def convert_json_to_html(json_path, output_path):
    """Convert a Chart Studio JSON export to standalone HTML"""
    with open(json_path, 'r') as f:
        chart_data = json.load(f)

    # Extract data and layout from the JSON
    data_json = json.dumps(chart_data.get('data', []))
    layout_json = json.dumps(chart_data.get('layout', {}))

    # Generate standalone HTML with Plotly.js 1.58.5
    html_template = f"""<html>
    <head><meta charset="utf-8" /></head>
    <body>
        <div id="plotly-div"></div>
        <script src="https://cdn.plot.ly/plotly-1.58.5.min.js"></script>
        <script>
            var data = {data_json};
            var layout = {layout_json};
            Plotly.newPlot('plotly-div', data, layout);
        </script>
    </body>
</html>"""

    with open(output_path, 'w') as f:
        f.write(html_template)

    return output_path

def main():
    # Convert all JSON files in the json/ directory
    json_dir = "json"
    charts_dir = "charts"

    if not os.path.exists(json_dir):
        print(f"❌ Directory '{json_dir}' does not exist")
        sys.exit(1)

    os.makedirs(charts_dir, exist_ok=True)

    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    if not json_files:
        print(f"No JSON files found in '{json_dir}' directory")
        return

    print(f"Found {len(json_files)} JSON file(s) to convert")

    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)
        html_filename = json_file.replace('.json', '.html')
        html_path = os.path.join(charts_dir, html_filename)

        try:
            convert_json_to_html(json_path, html_path)
            print(f"✅ Converted {json_file} → {html_filename}")
        except Exception as e:
            print(f"❌ Failed to convert {json_file}: {e}")

if __name__ == "__main__":
    main()
