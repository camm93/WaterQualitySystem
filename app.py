from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd


class WaterSample(BaseModel):
    pH: float
    Dureza: float
    Sólidos: float
    Cloraminas: float
    Sulfatos: float
    Conductividad: float
    Carbono_orgánico: float
    Trihalometanos: float
    Turbidez: float

    class Config:
        json_schema_extra = {
            "example": {
                "pH": 7.13,
                "Dureza": 173.69,
                "Sólidos": 19309.57,
                "Cloraminas": 6.53,
                "Sulfatos": 372.54,
                "Conductividad": 295.39,
                "Carbono_orgánico": 7.27,
                "Trihalometanos": 88.79,
                "Turbidez": 3.4
            }
        }


# Create a FastAPI instance
app = FastAPI()

# loaded the trained model
model = joblib.load("decision_tree_model.pkl")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Decision Tree Classifier API!"}


@app.post("/predict/")
def predict(data: WaterSample):
    try:
        # convert the input data to a DataFrame
        df = pd.DataFrame.from_dict(data.dict(), orient="index").T
        prediction = model.predict(df)
        prediction_proba = model.predict_proba(df)
        return {
            "prediction": prediction[0],
            "probability": prediction_proba[0].tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
