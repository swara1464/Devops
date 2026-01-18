# Lab Question 7: Data Versioning with DVC

## 📝 Problem Statement
**Implement data ingestion, cleaning, and versioning using Data Version Control (DVC) by tracking raw and processed datasets, creating a reproducible pipeline with `dvc.yaml`, and validating reproducibility via `dvc repro`.**

---

## ✅ Solution Steps

Follow these steps to set up DVC and run the data pipeline.

### Prerequisites
Ensure you have DVC and pandas installed:
```bash
pip install dvc pandas
```

### Step 1: Initialize the Project
Initialize Git and DVC in the `Q7` directory.

```bash
# Initialize Git (if not already done)
git init

# Initialize DVC
dvc init

# Commit the DVC setup
git add .
git commit -m "Initialize DVC"
```

### Step 2: Track Data
We have created a sample raw dataset in `data/raw/data.csv`. We will track this file using Git (for small files) or DVC (for large files). For this exercise, we'll let DVC manage the pipeline dependencies.

**Project Structure:**
*   `data/raw/data.csv`: The input data.
*   `src/clean.py`: The script to clean the data.
*   `dvc.yaml`: The pipeline configuration file.

### Step 3: Define the Pipeline
We have created a `dvc.yaml` file that defines the cleaning stage.

**File:** [`dvc.yaml`](dvc.yaml)
```yaml
stages:
  clean_data:
    cmd: python src/clean.py
    deps:
      - data/raw/data.csv
      - src/clean.py
    outs:
      - data/processed/cleaned_data.csv
```
This tells DVC:
*   **cmd**: Run `python src/clean.py`.
*   **deps**: Depends on `data/raw/data.csv` and the script itself.
*   **outs**: Produces `data/processed/cleaned_data.csv`.

### Step 4: Run the Pipeline (Reproduce)
Run the pipeline using `dvc repro`. This command checks dependency hashes. If nothing has changed, it won't run. If data or code changes, it re-runs the stage.

```bash
dvc repro
```

**Expected Output:**
DVC will run the clean command, output "Cleaner data...", and generate `data/processed/cleaned_data.csv`.

### Step 5: Versioning and Tracking Changes

1.  **Commit the DVC lock file:** DVC creates a `dvc.lock` file which captures the exact state (hashes) of your dependencies and outputs.
    ```bash
    git add dvc.yaml dvc.lock src/clean.py data/raw/data.csv
    git commit -m "Run data cleaning pipeline"
    ```

2.  **Modify Data and Reproduce:**
    *   Edit `data/raw/data.csv` (e.g., add a new row).
    *   Run `dvc repro` again.
    *   Notice that DVC detects the change and re-runs the `clean_data` stage.

3.  **No Changes:**
    *   Run `dvc repro` immediately after a successful run.
    *   DVC will say "Stage 'clean_data' is up to date." and do nothing. This proves reproducibility.
