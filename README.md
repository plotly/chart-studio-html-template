# Plotly Chart Studio Dash App

A Dash web application for hosting and displaying your Plotly Chart Studio visualizations. Simply place your Chart Studio JSON exports in the `json/` directory, and the app will automatically create an interactive gallery of your charts.

## Features

- **Automatic Chart Loading**: Reads all JSON files from the `json/` directory and subdirectories
- **Interactive Gallery**: Beautiful index page listing all your charts
- **Individual Chart Pages**: Each chart gets its own dedicated page with full interactivity
- **Responsive Design**: Works on desktop and mobile devices
- **Easy Deployment**: Deploy to Render, Heroku, or any platform that supports Python web apps

## Publishing and Embedding

### Deploy to Plotly Cloud

1. **Clone or download this repository**

2. **Add your Chart Studio JSON files** to the `json/` directory. For example:
   ```
   json/
   ├── 01/
   │   └── example-chart.json
   ├── 02/
   │   └── another-chart.json
   └── my-chart.json
   ```

3. **Create a Plotly Cloud account** at [cloud.plotly.com](https://cloud.plotly.com)

4. **Drag + drop to deploy**: Drag and drop your files into Plotly Cloud.

5. **Embed**: Use the Cloud URL to embed your charts.

Note: You'll need a **Pro** account on Plotly Cloud for apps to be hosted for more than 7 days before stopping automatically.

### Local Development

1. **Clone this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Chart Studio JSON files** to the `json/` directory. For example:
   ```
   json/
   ├── 01/
   │   └── example-chart.json
   ├── 02/
   │   └── another-chart.json
   └── my-chart.json
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open your browser** to `http://localhost:8050`
