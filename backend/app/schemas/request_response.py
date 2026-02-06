
from pydantic import BaseModel

class PredictRequest(BaseModel):
    amount: float
    category: str
    user_type: str
    region: str
    week: int

class PredictResponse(BaseModel):
    score: float
    confidence: float
