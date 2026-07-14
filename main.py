"""Generated Forge lite application for Medical Chatbot (MC).
Built from build_spec.json (BRD ACs + backlog + architecture).
"""
from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from domain import chat_answer, evaluate_rules, list_criteria, list_stories, meta, predict_payload

app = FastAPI(title="Medical Chatbot", version="1.0.0")
class ChatIn(BaseModel):
    message: str
    language: str | None = "en"
    agent_id: str | None = None
    attachment_note: str | None = None


@app.get("/health")
def health():
    m = meta()
    return {
        "status": "ok",
        "app": m.get("project_key"),
        "app_kind": m.get("app_kind"),
        "stories": len(m.get("story_ids") or []),
        "acceptance_criteria": len(m.get("ac_ids") or []),
    }


@app.get("/meta")
def get_meta():
    return meta()


@app.get("/stories")
def get_stories():
    return {"stories": list_stories()}


@app.get("/criteria")
def get_criteria():
    return {"acceptance_criteria": list_criteria()}


@app.post("/chat")
def chat(inp: ChatIn):
    return chat_answer(
        inp.message,
        language=inp.language or "en",
        agent_id=inp.agent_id,
        attachment_note=inp.attachment_note,
    )


@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), encoding="utf-8") as f:
        return f.read()
