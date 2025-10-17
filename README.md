# Chart Studio HTML Template

Host your HTML charts online for free using GitHub Pages. This template makes it easy to publish your visualizations and share them with a simple web link.

## What This Does

Upload your HTML chart files, and each one gets its own web address that you can share with anyone. For example:
- `my-chart.html` becomes `https://yourusername.github.io/your-project/my-chart.html`

## Step-by-Step Guide

### Step 1: Create Your Own Copy

1. At the top of this page on GitHub, click the green **"Use this template"** button
2. Give your project a name (like "my-charts")
3. Click **"Create repository"**

### Step 2: Turn On GitHub Pages

This is the most important step - your charts won't be published without it!

1. In your new repository, click **Settings** at the top
2. Look in the left sidebar and click **Pages**
3. Under "Build and deployment", find the **Source** dropdown
4. Select **GitHub Actions** (not "Deploy from a branch")
5. The page will refresh - you're all set!

### Step 3: Add Your Chart Files

You can add files directly on GitHub (easiest) or use GitHub Desktop:

**Option A: Upload on GitHub (Easiest)**
1. Click on the `charts` folder
2. Click **Add file** → **Upload files**
3. Drag and drop your `.html` files
4. Click **Commit changes** at the bottom

**Option B: Using GitHub Desktop**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Clone your repository to your computer
3. Copy your `.html` files into the `charts` folder
4. In GitHub Desktop, write a description and click **Commit to main**
5. Click **Push origin** to upload

### Step 4: Wait for Publishing

After uploading files:
1. Click the **Actions** tab at the top of your repository
2. You'll see a workflow running (yellow dot = in progress, green check = done)
3. This usually takes 30-60 seconds

### Step 5: View Your Charts Online

Your charts are now live! The web address follows this pattern:

```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/FILENAME.html
```

**Example:**
- If your GitHub username is `jane-smith`
- Your repository is named `my-charts`
- You uploaded `sales-report.html`
- Your chart is at: `https://jane-smith.github.io/my-charts/sales-report.html`

## Finding Your Chart URLs

Don't remember the exact address?

1. Go to **Settings** → **Pages**
2. At the top you'll see "Your site is live at [address]"
3. Add your filename to the end: `[address]/your-file.html`

## Adding More Charts

Just repeat Step 3! Every time you add a new `.html` file to the `charts` folder and commit it, GitHub will automatically publish it within about a minute.

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
