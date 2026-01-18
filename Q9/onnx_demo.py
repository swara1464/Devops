import numpy as np
import time
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as rt
import onnx

# 1. Train a Scikit-Learn Model
print("Training Scikit-Learn Model...")
iris = load_iris()
X, y = iris.data, iris.target
X = X.astype(np.float32)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

# 2. Export to ONNX
print("Exporting to ONNX...")
initial_type = [('float_input', FloatTensorType([None, 4]))]
onnx_model = convert_sklearn(clf, initial_types=initial_type)
with open("iris_rf.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

# 3. Benchmark Inference
print("\nBenchmarking Performance (10,000 iterations)...")

# Native Scikit-Learn Inference
start_time = time.time()
for _ in range(10000):
    clf.predict(X_test)
sklearn_duration = time.time() - start_time
print(f"Scikit-Learn Duration: {sklearn_duration:.4f} seconds")

# ONNX Runtime Inference
sess = rt.InferenceSession("iris_rf.onnx", providers=["CPUExecutionProvider"])
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

start_time = time.time()
for _ in range(10000):
    sess.run([label_name], {input_name: X_test})
onnx_duration = time.time() - start_time
print(f"ONNX Runtime Duration: {onnx_duration:.4f} seconds")

# speedup
speedup = sklearn_duration / onnx_duration
print(f"\nSpeedup: {speedup:.2f}x")
