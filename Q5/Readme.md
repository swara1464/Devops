# Lab Question 5: ML Environment Setup

## 📝 Problem Statement
**Set up a simple ML project environment by creating a `requirements.txt` file, installing packages, and verifying environment setup. Document the steps in a Jupyter Notebook and commit it to the Git repository.**

---

## ✅ Solution Steps

Follow these steps to complete the task.

### Step 1: Create requirements.txt
Create a file named `requirements.txt` listing the necessary Python packages for a basic ML project.

**File Content:** [`requirements.txt`](requirements.txt)
```text
numpy
pandas
scikit-learn
matplotlib
jupyter
```

### Step 2: Install Packages
Open your terminal in this directory (`Q5`) and install the packages using pip.

```bash
pip install -r requirements.txt
```

### Step 3: Document and Verify in Jupyter Notebook
We have provided a Jupyter Notebook that documents these steps and includes a code cell to verify the installation.

1.  **Open the Notebook:**
    ```bash
    jupyter notebook setup_guide.ipynb
    ```
2.  **Run the Cells:** Execute the cells in the notebook to read the documentation and run the verification script (checking package versions).

**File:** [`setup_guide.ipynb`](setup_guide.ipynb)

### Step 4: Commit to Git
Once you have created the files and verified the setup, commit everything to your Git repository.

```bash
# 1. Check status
git status

# 2. Add files
git add requirements.txt setup_guide.ipynb

# 3. Commit
git commit -m "Setup ML project environment and documentation"
```
