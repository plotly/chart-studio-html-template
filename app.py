#!/usr/bin/env python3
"""
Dash app for displaying Plotly Chart Studio charts from JSON files.
"""

import json
import os
from pathlib import Path
from dash import Dash, html, dcc, Input, Output, callback

# Initialize Dash app with Plotly.js 1.58.5 for Chart Studio compatibility
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_scripts=['https://cdn.plot.ly/plotly-1.58.5.min.js']
)
server = app.server

# Configure for deployment
app.title = "Plotly Chart Gallery"

def load_charts_from_json():
    """Load all chart JSON files from the json/ directory"""
    charts = []
    json_dir = Path("json")

    if not json_dir.exists():
        return charts

    # Walk through all subdirectories
    for json_file in json_dir.rglob("*.json"):
        try:
            with open(json_file, 'r') as f:
                chart_data = json.load(f)

            # Extract title from layout
            layout = chart_data.get('layout', {})
            title = layout.get('title', {})

            if isinstance(title, str):
                chart_title = title
            elif isinstance(title, dict) and 'text' in title:
                chart_title = title['text']
            else:
                chart_title = json_file.stem.replace('-', ' ').title()

            # Store chart info with raw data (Plotly.js 1.58.5 handles it)
            charts.append({
                'id': json_file.stem,
                'title': chart_title,
                'path': str(json_file),
                'data': chart_data.get('data', []),
                'layout': layout
            })
        except Exception as e:
            print(f"Error loading {json_file}: {e}")

    # Sort by title
    charts.sort(key=lambda x: x['title'])
    return charts

# Load all charts at startup
CHARTS = load_charts_from_json()

# Layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

def create_index_page():
    """Create the index page with all charts"""
    return html.Div([
        html.Div([
            html.Header([
                html.H1([
                    html.Span("Plotly", className="plotly-logo"),
                    " Chart Gallery"
                ]),
                html.P("Charts previously hosted on Plotly Chart Studio", className="subtitle")
            ], style={
                'background': 'white',
                'padding': '2rem',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'marginBottom': '2rem'
            }),

            html.Div([
                create_chart_card(chart) for chart in CHARTS
            ], className="chart-grid")
        ], className="container")
    ])

def create_chart_card(chart):
    """Create a card for a single chart"""
    return html.Div([
        html.A(chart['title'], href=f"/chart/{chart['id']}", className="chart-link"),
        html.Div(chart['id'], className="chart-name"),
        html.Div([
            html.A("View Chart", href=f"/chart/{chart['id']}", className="btn btn-primary")
        ], className="button-group")
    ], className="chart-card")

def create_chart_page(chart_id):
    """Create a page displaying a single chart using Plotly.js 1.58.5"""
    chart = next((c for c in CHARTS if c['id'] == chart_id), None)

    if not chart:
        return html.Div([
            html.H1("Chart Not Found"),
            html.A("Back to Gallery", href="/")
        ])

    # Embed chart data as a data attribute for clientside rendering
    chart_data_json = json.dumps({'data': chart['data'], 'layout': chart['layout']})

    return html.Div([
        html.Div(
            id='plotly-chart-container',
            **{'data-chart': chart_data_json},
            style={'height': '100%', 'width': '100%'}
        )
    ], style={'height': '100vh', 'width': '100vw', 'margin': 0, 'padding': 0})

@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """Route to the appropriate page"""
    if pathname == '/' or pathname is None:
        return create_index_page()
    elif pathname.startswith('/chart/'):
        chart_id = pathname.split('/chart/')[-1]
        return create_chart_page(chart_id)
    else:
        return html.Div([
            html.H1("404 - Page Not Found"),
            html.A("Back to Gallery", href="/")
        ])

# Clientside callback to render charts with Plotly.js 1.58.5
app.clientside_callback(
    """
    function(id) {
        var container = document.getElementById('plotly-chart-container');
        if (!container) {
            return window.dash_clientside.no_update;
        }

        var chartDataStr = container.getAttribute('data-chart');
        if (!chartDataStr) {
            return window.dash_clientside.no_update;
        }

        function renderChart() {
            if (typeof Plotly !== 'undefined') {
                var chartData = JSON.parse(chartDataStr);
                var layout = chartData.layout || {};

                // Force full viewport sizing
                layout.autosize = true;
                layout.width = undefined;
                layout.height = undefined;
                layout.margin = {l: 40, r: 40, t: 40, b: 40};

                Plotly.newPlot('plotly-chart-container', chartData.data, layout, {
                    responsive: true,
                    displayModeBar: false
                });

                // Resize on window resize
                window.addEventListener('resize', function() {
                    Plotly.Plots.resize('plotly-chart-container');
                });
            } else {
                setTimeout(renderChart, 100);
            }
        }

        setTimeout(renderChart, 100);
        return window.dash_clientside.no_update;
    }
    """,
    Output('plotly-chart-container', 'data-dummy'),
    Input('plotly-chart-container', 'id'),
    prevent_initial_call=False
)

# Add CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html, body {
                height: 100%;
                width: 100%;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                line-height: 1.6;
                color: #333;
                background: #f5f5f5;
            }

            /* Only hide overflow for chart pages */
            #plotly-chart-container {
                overflow: hidden;
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }

            .plotly-logo {
                font-weight: 700;
                color: #119dff;
            }

            .subtitle {
                color: #7f8c8d;
                font-size: 1.1rem;
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

            .chart-link {
                text-decoration: none;
                color: #119dff;
                font-size: 1.1rem;
                font-weight: 500;
                display: block;
            }

            .chart-link:hover {
                color: #0d7ec9;
            }

            .chart-name {
                margin-top: 0.5rem;
                color: #7f8c8d;
                font-size: 0.9rem;
            }

            .button-group {
                margin-top: 1rem;
                display: flex;
                gap: 0.5rem;
            }

            .btn {
                padding: 0.5rem 1rem;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
                transition: background 0.2s;
                text-decoration: none;
                display: inline-block;
                text-align: center;
            }

            .btn-primary {
                background: #119dff;
                color: white !important;
            }

            .btn-primary:hover {
                background: #0d7ec9;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
