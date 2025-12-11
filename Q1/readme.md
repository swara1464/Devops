# Lab Question 1: User Registration Form with Git

## 📝 Problem Statement
**Create a simple User Registration Form for an event with fields (Name, Email, Phone). Initialize a Git repository, commit the project files, and push them to GitHub using appropriate Git commands.**

---

## ✅ Solution Steps

Follow these steps to complete the task.

### Step 1: Create the Project and HTML File
Create a new directory and an HTML file (e.g., `index.html`) implementing the required fields: Name, Email, and Phone.

**Commands:**
```bash
mkdir event-registration
cd event-registration
# Create the file index.html
```

**Project File:**
[regestration.html](regestration.html)

### Step 2: Initialize Git Repository
Initialize a local Git repository in your project folder.

```bash
git init
```

### Step 3: Stage and Commit Files
Add the file to the staging area and commit it to the repository.

```bash
git add .
git commit -m "Initial commit: Add simple user registration form"
```

### Step 4: Push to GitHub
Link your local repository to a remote GitHub repository and push your changes.

```bash
# 1. Create a new repository on GitHub named 'event-registration' first.

# 2. Add the remote repository URL (Replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/event-registration.git

# 3. Rename branch to main (optional but recommended)
git branch -M main

# 4. Push the code
git push -u origin main
```