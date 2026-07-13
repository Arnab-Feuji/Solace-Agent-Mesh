"""Generated model-serving API for Medical Chatbot (Fraud Modelling Application)."""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Any
import os, joblib

app = FastAPI(title="Medical Chatbot")
FEATURES = []
TARGET = None
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
_model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@app.get("/health")
def health(): return {"status": "ok", "model_loaded": _model is not None}

@app.post("/predict")
def predict(payload: dict[str, Any]):
    if _model is None:
        return {"error": "model not trained yet — run train.py first"}
    import numpy as np
    x = np.array([[float(payload.get(f, 0)) for f in FEATURES]])
    try:
        if hasattr(_model, "predict_proba"):
            proba = _model.predict_proba(x)[0].tolist()
            pred = _model.predict(x)[0]
            return {"prediction": _to_native(pred), "proba": proba, "target": TARGET}
        pred = _model.predict(x)[0]
        return {"prediction": _to_native(pred), "target": TARGET}
    except Exception as e:
        return {"error": str(e)}

def _to_native(v):
    try: return v.item()
    except Exception: return v

@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), encoding="utf-8") as f:
        return f.read()
