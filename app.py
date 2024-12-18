from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

# Create a FastAPI instance
app = FastAPI()

# loaded the trained model
model = joblib.load("decision_tree_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Decision Tree Classifier API!"}

@app.post("/predict/")
def predict(data: dict):
    try:
        # convert the input data to a DataFrame
        df = pd.DataFrame.from_dict(data, orient="index").T
        prediction = model.predict(df)
        prediction_proba = model.predict_proba(df)
        return {
            "prediction": prediction[0],
            "probability": prediction_proba[0].tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
