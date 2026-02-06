
from fastapi import APIRouter
import numpy as np
from app.schemas.request_response import PredictRequest, PredictResponse
from app.core.model_loader import load_model
from app.db.crud import insert_prediction

router = APIRouter()
model = load_model()

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):

    category_map = {"A":0,"B":1,"C":2}
    user_map = {"new":0,"old":1}
    region_map = {"north":0,"south":1}

    X = np.array([[
        req.amount,
        category_map.get(req.category,0),
        user_map.get(req.user_type,0),
        region_map.get(req.region,0)
    ]])

    score = float(model.predict_proba(X)[0][1])
    confidence = abs(score - 0.5) * 2

    insert_prediction(
        req.amount,
        req.category,
        req.user_type,
        req.region,
        score,
        confidence,
        req.week
    )

    return {"score": score, "confidence": confidence}
