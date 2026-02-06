
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)
