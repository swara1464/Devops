# Lab Question 10: Model Serving with FastAPI

## 📝 Problem Statement
**Serve a machine learning model using FastAPI by developing a `/predict` REST endpoint with input validation, writing test cases, containerizing the service, and verifying predictions through Postman or curl.**

---

## ✅ Solution Steps

Follow these steps to build, test, and deploy your ML API.

### Step 1: Develop the API (`main.py`)
We have created `main.py` which initializes a FastAPI app, trains a simple Logistic Regression model (mocking a loaded model), and exposes a `/predict` endpoint using Pydantic for input validation.

**File:** [`main.py`](main.py)

### Step 2: Write Test Cases (`test_main.py`)
We have created `test_main.py` using `pytest` to verify the API functionality locally before deployment.

**Run Tests:**
```bash
pip install -r requirements.txt
pytest
```
*Expected Output: `3 passed`*

### Step 3: Containerize (`Dockerfile`)
The `Dockerfile` is set up to install dependencies and run the API using `uvicorn`.

**File:** [`Dockerfile`](Dockerfile)

**Build and Run Image:**
```bash
# Build
docker build -t ml-api:v1 .

# Run
docker run -d -p 8000:8000 ml-api:v1
```

### Step 4: Verify Predictions (Curl/Postman)
Once the container is running, send requests to test the model.

**1. Health Check:**
```bash
curl http://localhost:8000/
```
*Response: `{"status":"running",...}`*

**2. Make a Prediction (Class A):**
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"feature\": 0.5}"
```
*Expected Response:* `{"prediction":0,"class_name":"Class A",...}`

**3. Make a Prediction (Class B):**
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"feature\": 4.5}"
```
*Expected Response:* `{"prediction":1,"class_name":"Class B",...}`

### Step 5: Version Control
Commit the API code to your repository.

```bash
git add main.py test_main.py requirements.txt Dockerfile
git commit -m "Create containerized ML serving API with FastAPI"
```
 
