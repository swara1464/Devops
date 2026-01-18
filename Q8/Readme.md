# Lab Question 8: MLflow Experiment Tracking

## 📝 Problem Statement
**Perform experiment tracking using MLflow by training a machine learning model, logging metrics, parameters, and artifacts, and comparing multiple runs to identify the best-performing model.**

---

## ✅ Solution Steps

Follow these steps to set up experiment tracking.

### Step 1: Install Dependencies
Open your terminal in this directory (`Q8`) and install the necessary packages.

```bash
pip install -r requirements.txt
```

### Step 2: Understand the Training Script
We have provided a script `train.py` that trains an ElasticNet model on the Wine Quality dataset. It uses MLflow to:
1.  **Log Parameters**: `alpha` and `l1_ratio`.
2.  **Log Metrics**: RMSE, MAE, and R2 score.
3.  **Log Model**: Saves the trained model as an artifact.

**File:** [`train.py`](train.py)

### Step 3: Run Experiments
Run the training script multiple times with different parameters to simulate different experiments.

**Experiment 1 (Default parameters):**
```bash
python train.py 0.5 0.5
```

**Experiment 2 (Different alpha):**
```bash
python train.py 0.2 0.5
```

**Experiment 3 (Different l1_ratio):**
```bash
python train.py 0.5 0.8
```

### Step 4: Compare Runs in MLflow UI
Launch the MLflow User Interface to visualize and compare the runs.

1.  **Start UI:**
    ```bash
    mlflow ui
    ```
2.  **Access in Browser:** Open [http://localhost:5000](http://localhost:5000).
3.  **Analyze:**
    *   Click on the Experiment name (usually "Default").
    *   You will see a table listing your 3 runs.
    *   Compare the `rmse` and `r2` columns to identify the best model (lowest RMSE, highest R2).
    *   Click on a specific run to view detailed parameters and the logged model artifact.

### Step 5: Git Versioning
Don't forget to track your code changes.

```bash
git add train.py requirements.txt
git commit -m "Add MLflow training script for experiment tracking"
```
