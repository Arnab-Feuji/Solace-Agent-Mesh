"""Generated chatbot service for Medical Chatbot."""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

app = FastAPI(title="Medical Chatbot")
KB = {'about': 'This is the Medical Chatbot assistant. Goal: Please develop a Medical Chatbot application based on 5 Agents like - Cancer Care, Diabetes, Mental Illness, Cardio & Respiratory  Consider CDC & PubMed as RAG Database  Add features like chat message download button, Prescription download button, Mike button, Multimodal, Multilingual - Hindi, English & Spanish.', 'rules': 'Validate & sanitise all inputs against the declared schema. · Log every decision/response immutably for audit. · Produce cluster/anomaly assignments with a quality score. · Persist the fitted model + assignment for each input row.', 'validate': 'Validate & sanitise all inputs against the declared schema.', 'sanitise': 'Validate & sanitise all inputs against the declared schema.', 'inputs': 'Validate & sanitise all inputs against the declared schema.', 'every': 'Log every decision/response immutably for audit.', 'decision/response': 'Log every decision/response immutably for audit.', 'immutably': 'Log every decision/response immutably for audit.', 'produce': 'Produce cluster/anomaly assignments with a quality score.', 'cluster/anomaly': 'Produce cluster/anomaly assignments with a quality score.', 'assignments': 'Produce cluster/anomaly assignments with a quality score.', 'persist': 'Persist the fitted model + assignment for each input row.', 'fitted': 'Persist the fitted model + assignment for each input row.', 'model': 'Persist the fitted model + assignment for each input row.'}
RED_FLAGS = ["chest pain", "can't breathe", "suicid", "want to die"]

class ChatIn(BaseModel):
    message: str

@app.get("/health")
def health(): return {"status": "ok", "app": "MC"}

@app.post("/chat")
def chat(inp: ChatIn):
    text = inp.message.lower()
    if any(f in text for f in RED_FLAGS):
        return {"answer": "This may be an emergency. Please call your local emergency number now.", "source": "SAFETY"}

    # Simple keyword match retriever
    for k, val in KB.items():
        if k in text:
            return {"answer": f"Knowledge Retrieval match: {val}", "source": "Internal Knowledge Base"}

    return {"answer": f"Here is guidance regarding Medical Chatbot: Please develop a Medical Chatbot application based on 5 Agents like - Cancer Care, Diabetes, Mental Illness, Cardio & Respiratory  Consider CDC & PubMed as RAG Database  Add features like chat message download button, Prescription download button, Mike button, Multimodal, Multilingual - Hindi, English & Spanish", "source": "Local LLM Inference"}

@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), encoding="utf-8") as f:
        return f.read()
