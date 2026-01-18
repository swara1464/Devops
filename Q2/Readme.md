# Lab Question 2: Jenkins CI for Student Portal

## 📝 Problem Statement
**Your college department is developing a small student portal website hosted on GitHub. As a DevOps engineer, you must set up Continuous Integration using Jenkins.**

**Task Requirements:**
1.  Configure a Jenkins Freestyle Job that automatically pulls the website code from GitHub.
2.  Enable Jenkins to build the project every time a change is pushed.
3.  Make a small update to the HTML page, push it to GitHub, and show that Jenkins automatically triggers a new build.

---

## ✅ Solution Steps

Follow these steps to set up the CI pipeline.

### Step 1: Prepare the GitHub Repository
1.  Initialize a Git repository for this folder (`Q2`) if you haven't already.
2.  Commit the `index.html` file.
3.  Create a new repository on GitHub (e.g., `student-portal`).
4.  Push your local code to the GitHub repository.

```bash
git init
git add index.html
git commit -m "Initial commit of Student Portal"
git remote add origin https://github.com/USERNAME/student-portal.git
git push -u origin main
```

### Step 2: Configure Jenkins
1.  **Open Jenkins:** Go to your Jenkins dashboard (usually `http://localhost:8080`).
2.  **Create New Job:**
    *   Click **"New Item"**.
    *   Enter a name (e.g., `StudentPortal-CI`).
    *   Select **"Freestyle project"** and click **OK**.
3.  **Source Code Management:**
    *   In the configuration page, scroll to **Source Code Management**.
    *   Select **Git**.
    *   Paste your GitHub Repository URL in **Repository URL**.
    *   Specify the branch to build (e.g., `*/main`).
4.  **Build Triggers:**
    *   Check **"GitHub hook trigger for GITScm polling"** (This requires a Webhook on GitHub).
    *   *Alternative for Localhost:* Check **"Poll SCM"** and enter `* * * * *` (polls every minute). This is easier if your Jenkins is not exposed to the internet.
5.  **Build Steps:**
    *   Scroll to **Build**.
    *   Click **Add build step** -> **Execute shell** (Mac/Linux) or **Execute Windows batch command** (Windows).
    *   Enter a simple command to verify the pull, e.g.:
        ```bash
        echo "Build successfully triggered! Deploying Student Portal..."
        dir  # Lists files to confirm download (Windows)
        ```
6.  **Save:** Click **Save**.

### Step 3: Trigger a Build
Now, verify the automation by making a change to your code.

1.  **Modify `index.html`:** Open the file (or use the one in this directory) and change the text. For example, change "Status: Active" to "Status: Maintenance Mode".
2.  **Push Changes:**
    ```bash
    git add index.html
    git commit -m "Update portal status to Maintenance"
    git push origin main
    ```

### Step 4: Verify in Jenkins
1.  Go back to your Jenkins Project dashboard.
2.  Wait a minute (if using polling) or check immediately (if using webhooks).
3.  You should see a new build appear in the **Build History** (e.g., `#1` or `#2`).
4.  Click the build number -> **Console Output** to see the success message and file listing.
