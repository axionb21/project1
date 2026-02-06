
from fastapi import FastAPI
from app.api.predict import router
from app.db.crud import init_db

app = FastAPI(title="Silent Drift Detection System")

init_db()
app.include_router(router)
