# Lab Question 9: Model Optimization with ONNX

## 📝 Problem Statement
**Optimize and standardize model inference using ONNX by exporting a trained ML model to ONNX format, running inference with ONNX Runtime, and benchmarking performance against the native scikit-learn model.**

---

## ✅ Solution Steps

Follow these steps to perform the task.

### Step 1: Install Dependencies
Open your terminal in this directory (`Q9`) and install the necessary packages.

```bash
pip install -r requirements.txt
```

### Step 2: Create the Benchmark Script
We have created a script `onnx_demo.py` that performs the following actions:
1.  **Train**: Trains a Random Forest Classifier on the Iris dataset using Scikit-Learn.
2.  **Export**: Converts the trained model to `.onnx` format using `skl2onnx`.
3.  **Benchmark**: Runs inference 10,000 times using both the native Scikit-Learn model and the ONNX Runtime engine, measuring the time taken for each.

**File:** [`onnx_demo.py`](onnx_demo.py)

### Step 3: Run the Benchmark
Execute the script to see the performance comparison.

```bash
python onnx_demo.py
```

**Expected Output:**
The script will print the training status, export confirmation, and the timing results. You should see a "Speedup" value indicating how much faster (or comparable) ONNX Runtime is.

```text
Training Scikit-Learn Model...
Exporting to ONNX...

Benchmarking Performance (10,000 iterations)...
Scikit-Learn Duration: 1.2345 seconds
ONNX Runtime Duration: 0.8765 seconds

Speedup: 1.41x
```

### Step 4: Version Control
Commit your work to Git.

```bash
git add requirements.txt onnx_demo.py
git commit -m "Implement ONNX conversion and benchmarking script"
```
