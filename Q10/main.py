from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LogisticRegression

# Initialize App
app = FastAPI(title="ML Prediction Service")

# Mock Model (In a real app, load this from a .pkl file)
# Training a simple dummy model for demonstration
X_train = np.array([[0], [1], [2], [3], [4], [5]])
y_train = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression()
model.fit(X_train, y_train)

# Input Schema
class PredictionRequest(BaseModel):
    feature: float

# Endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Reshape input for sklearn
        input_data = np.array([[request.feature]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0].tolist()
        
        return {
            "prediction": int(prediction),
            "probability": probability,
            "class_name": "Class B" if prediction == 1 else "Class A"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def health_check():
    return {"status": "running", "message": "ML Service is healthy"}
