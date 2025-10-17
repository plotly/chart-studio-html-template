# Plotly Chart Studio HTML Template

Host your Plotly Chart Studio visualizations online for free using GitHub Pages. Export your charts from Chart Studio as HTML files and publish them with a simple web link.

## What This Does

Upload your Chart Studio HTML exports, and they'll be automatically published online:
- An **index page** listing all your Plotly charts is created at `https://yourusername.github.io/your-project/`
- Each chart gets its own web address: `https://yourusername.github.io/your-project/my-chart.html`

Perfect for sharing interactive Plotly visualizations with your team or embedding in presentations!

## Step-by-Step Guide

### Step 1: Create Your Own Copy

1. At the top of this page on GitHub, click the green **"Use this template"** button
2. Select **"Create a new repository"**
3. Give your project a name (like "my-plotly-charts")
4. Click **"Create repository"**

### Step 2: Export Your Charts from Chart Studio

1. Go to [Chart Studio](https://chart-studio.plotly.com/)
2. Open the chart you want to publish
3. Click **Export** and select **HTML**
4. Save the `.html` file to your computer
5. Repeat for any other charts you want to publish

### Step 3: Turn On GitHub Pages

This is the most important step - your charts won't be published without it!

1. In your new repository, click **Settings** at the top
2. Look in the left sidebar and click **Pages**
3. Under "Build and deployment", find the **Source** dropdown
4. Select **GitHub Actions** (not "Deploy from a branch")
5. The page will refresh - you're all set!

### Step 4: Upload Your Chart Studio HTML Files

You can add files directly on GitHub (easiest) or use GitHub Desktop:

**Option A: Upload on GitHub (Easiest)**
1. Click on the `charts` folder
2. Click **Add file** → **Upload files**
3. Drag and drop your Chart Studio `.html` files
4. Click **Commit changes** at the bottom

**Option B: Using GitHub Desktop**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Clone your repository to your computer
3. Copy your Chart Studio `.html` files into the `charts` folder
4. In GitHub Desktop, write a description and click **Commit to main**
5. Click **Push origin** to upload

### Step 5: Wait for Publishing

After uploading files:
1. Click the **Actions** tab at the top of your repository
2. You'll see a workflow running (yellow dot = in progress, green check = done)
3. This usually takes 30-60 seconds

### Step 6: View Your Plotly Charts Online

Your interactive Plotly charts are now live!

**View All Charts:**
Go to your main page to see a gallery of all your Plotly visualizations:
```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/
```

**View Individual Charts:**
Each Plotly chart has its own direct link:
```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/FILENAME.html
```

**Example:**
- If your GitHub username is `jane-smith`
- Your repository is named `my-plotly-charts`
- Your main gallery page is at: `https://jane-smith.github.io/my-plotly-charts/`
- A specific chart is at: `https://jane-smith.github.io/my-plotly-charts/sales-report.html`

## Finding Your Chart URLs

Don't remember the exact address?

1. Go to **Settings** → **Pages**
2. At the top you'll see "Your site is live at [address]"
3. Visit that address to see all your charts listed with clickable links
4. Or add a filename to the end for a specific chart: `[address]/your-file.html`

## Adding More Charts

Just repeat Step 4! Every time you export a new chart from Chart Studio and add the `.html` file to the `charts` folder:
- GitHub will automatically publish it within about a minute
- The index page will automatically update to include your new Plotly chart

## Troubleshooting

**My chart isn't showing up**
- Double-check that GitHub Pages is enabled (Settings → Pages → Source should say "GitHub Actions")
- Make sure your file is in the `charts` folder, not somewhere else
- Wait 1-2 minutes after uploading - it's not instant
- Check the Actions tab to see if there were any errors (red X icon)

**I see a 404 error**
- Make sure you're using the exact filename (including `.html`)
- Check that the file name doesn't have spaces - use dashes instead (`my-chart.html` not `my chart.html`)

**Need to remove a chart?**
- Go to the `charts` folder, click on the file, and click the trash icon
- Commit the change, and it will be removed from your site within a minute
