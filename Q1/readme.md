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

**Project Files:**
- [regestration.html](regestration.html): The initial registration form **without** the Department field.
- [updated-form.html](updated-form.html): The updated registration form **with** the Department field.

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

### Step 5: Create and Switch to a New Branch
Create a new branch named `update-form` to work on the new feature (adding the Department field).

```bash
# Create and switch to the new branch
git branch update-form
git checkout update-form

# Alternatively, you can do both in one command:
# git checkout -b update-form
```

### Step 6: Modify the Registration Form
Open `regestration.html` and add the new "Department" field.

1.  **Add HTML Input:** Add a new input field for "Department" after the phone number field.
2.  **Update JavaScript:** Add validation logic for the new field and ensure it's included in the form submission.

*(Use the code from `updated-form.html` in this folder as the improved version with the Department field)*

### Step 7: Commit Changes to the Branch
Stage and commit your changes to the `update-form` branch.

```bash
git add regestration.html
git commit -m "Add Department field to registration form"
```

### Step 8: Merge Branch into Main
Switch back to the `main` branch and merge the changes from `update-form`.

```bash
# Switch back to main
git checkout main

# Merge the update-form branch
git merge update-form
```

### Step 9: Push Changes to GitHub
Push the updated `main` branch to the remote repository.

```bash
git push origin main
```
