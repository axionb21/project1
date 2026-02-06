
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASELINE_PATH = os.path.join(BASE_DIR, "baseline", "baseline.json")

def load_baseline():
    try:
        with open(BASELINE_PATH, "r") as f:
            return json.load(f)
    except:
        return {}
