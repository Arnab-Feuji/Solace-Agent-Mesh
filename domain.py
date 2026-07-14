"""Domain logic for Medical Chatbot — driven by build_spec (BRD ACs + backlog + architecture)."""
from __future__ import annotations

import json
import os
import re
from typing import Any

BUILD_SPEC: dict[str, Any] = {
  "version": 1,
  "project_key": "MC",
  "project_name": "Medical Chatbot",
  "app_type": "Conversational AI Chatbot ",
  "app_kind": "chatbot",
  "summary": "Develop a medical chatbot application featuring agents specialized in cancer care, diabetes, mental illness, cardiovascular, and respiratory conditions. Utilize CDC and PubMed as the primary resources for retrieval-augmented generation databases, and include features like chat me",
  "requirement_text": "Organisation: Feuji Software Solution Pvt. Ltd.\nSegment: Healthcare\n\nAI SUGGESTED & EDITED PARAMETERS:\nAPP TYPE: Conversational AI Chatbot\nSEGMENT: Healthcare\nPROBLEM: Develop a medical chatbot application featuring agents specialized in cancer care, diabetes, mental illness, cardiovascular, and respiratory conditions. Utilize CDC and PubMed as the primary resources for retrieval-augmented generation databases, and include features like chat message download, prescription download, a mic button for voice input, multimodal interaction, and support for English, Hindi, and Spanish.\nTOOLS AND TECH STACKS: Python, FastAPI, React, TensorFlow, MongoDB\nKNOWLEDGE BASE SOURCES: CDC, PubMed, peer-reviewed medical journals\nLLM FOUNDATION MODEL: MedGPT-Plus for medical dialogue and Claude Health for emotional support\nSUPPORTED LANGUAGES: English, Hindi, Spanish\nMULTIMODAL FEATURES: Text, voice, and document parsing capabilities\nPERSONA AND TONE: Trustworthy, compassionate, and informative; aligned with healthcare communication standards\nCUSTOM FEATURES: Chat message download, prescription download capability, voice input support, multilingual options\nEXPECTED OUTCOME: Achieve high user satisfac",
  "requestor": "ad_isi03@hotmail.com",
  "deploy_port": 8095,
  "api": {
    "health": "/health",
    "meta": "/meta",
    "primary": "/chat",
    "stories": "/stories",
    "criteria": "/criteria"
  },
  "acceptance_criteria": [
    {
      "id": "AC-1",
      "given": "a valid request",
      "when": "rule BR-1 applies",
      "then": "Validate & sanitise all inputs against the declared schema."
    },
    {
      "id": "AC-2",
      "given": "a valid request",
      "when": "rule BR-2 applies",
      "then": "Log every decision/response immutably for audit."
    },
    {
      "id": "AC-3",
      "given": "a valid request",
      "when": "rule BR-3 applies",
      "then": "Produce cluster/anomaly assignments with a quality score."
    },
    {
      "id": "AC-4",
      "given": "a valid request",
      "when": "rule BR-4 applies",
      "then": "Persist the fitted model + assignment for each input row."
    }
  ],
  "business_rules": [
    {
      "id": "BR-1",
      "statement": "Validate & sanitise all inputs against the declared schema.",
      "rationale": ""
    },
    {
      "id": "BR-2",
      "statement": "Log every decision/response immutably for audit.",
      "rationale": ""
    },
    {
      "id": "BR-3",
      "statement": "Produce cluster/anomaly assignments with a quality score.",
      "rationale": ""
    },
    {
      "id": "BR-4",
      "statement": "Persist the fitted model + assignment for each input row.",
      "rationale": ""
    }
  ],
  "backlog": {
    "project": "MC",
    "total_points": 30,
    "epic_count": 4,
    "story_count": 6
  },
  "stories": [
    {
      "id": "S1",
      "title": "Cancer Care specialty agent + RAG citations",
      "points": 5,
      "epic": "Conversational UX",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S2",
      "title": "Diabetes specialty agent + RAG citations",
      "points": 5,
      "epic": "Conversational UX",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S3",
      "title": "Mental Illness specialty agent + RAG citations",
      "points": 5,
      "epic": "RAG & Specialty Agents",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S4",
      "title": "Cardiology specialty agent + RAG citations",
      "points": 5,
      "epic": "RAG & Specialty Agents",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S5",
      "title": "Respiratory specialty agent + RAG citations",
      "points": 5,
      "epic": "RAG & Specialty Agents",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    },
    {
      "id": "S5",
      "title": "Voice, multilingual, prescription export",
      "points": 5,
      "epic": "Safety & Multimodal",
      "acceptance_criteria_ids": [],
      "acceptance_criteria": []
    }
  ],
  "architecture": {
    "has_diagram": True,
    "modules": [
      "api",
      "domain",
      "ui",
      "data",
      "orchestration",
      "context"
    ],
    "services": [],
    "render_url": "https://mermaid.ink/img/pako:eNpVz70KgzAUBeBXuWRqodK_zaEgHULBYgkUh9ThNrliaKxwjZUivnurm8sZzneWMwjTWBKxKH3Tmwo5QKoeb4B7S7zSUxZriKITyFwntwtIDNTjt5g2Mp8lU2edsamoDYyh4dn-5YznnVYU2NGHGLagErnkvZYdsmV0vl3KQafpFUr0_onmtbSjTjrrQiE2oiau0VkRDyJUVE9fLJXY-SDG8Qdt6UWF",
    "excerpt": "%% C4 Context\nflowchart LR\n  User([User]) --> GW[API Gateway]\n  GW --> ORC[Orchestrator]\n  ORC --> C0[Retriever / RAG]\n  ORC --> C1[Guardrails]\n  ORC --> C2[LLM fallback]\n  ORC --> C3[Audit]\n\n%% Sequence\nsequenceDiagram\n  User->>ORC: message\n  ORC->>SAFE: guardrail check\n  ORC->>RAG: retrieve (sources)\n  RAG-->>ORC: passages + citation\n  ORC-->>User: answer + source\n\n%% ER\nerDiagram\n  MC_REQUEST ||--o| MC_RESPONSE : yields\n  MC_REQUEST ||--o{ AUDIT_EVENT : logs"
  },
  "modules": [
    "api",
    "domain",
    "ui",
    "data",
    "orchestration",
    "context"
  ],
  "input_fields": [
    {
      "name": "feature_a",
      "dtype": "float",
      "description": ""
    },
    {
      "name": "feature_b",
      "dtype": "float",
      "description": ""
    }
  ],
  "sample_input": {
    "feature_a": 42.5,
    "feature_b": 88.2
  },
  "output_fields": [],
  "rag_sources": [
    "CDC",
    "PubMed"
  ],
  "domains": [
    "Cancer Care",
    "Diabetes",
    "Mental Illness",
    "Cardiology",
    "Respiratory"
  ],
  "agents": [
    {
      "id": "A1",
      "name": "Cancer Care",
      "domain": "Cancer Care",
      "persona": "caring, knowledgeable, patient-centric"
    },
    {
      "id": "A2",
      "name": "Diabetes Agent",
      "domain": "Diabetes",
      "persona": "caring, knowledgeable, patient-centric"
    },
    {
      "id": "A3",
      "name": "Mental Illness Agent",
      "domain": "Mental Illness",
      "persona": "caring, knowledgeable, patient-centric"
    },
    {
      "id": "A4",
      "name": "Cardiology Agent",
      "domain": "Cardiology",
      "persona": "caring, knowledgeable, patient-centric"
    },
    {
      "id": "A5",
      "name": "Respiratory Agent",
      "domain": "Respiratory",
      "persona": "caring, knowledgeable, patient-centric"
    },
    {
      "id": "A6",
      "name": "General Care Agent",
      "domain": "General Care",
      "persona": "caring, knowledgeable, patient-centric"
    }
  ],
  "languages": [
    "en",
    "hi",
    "es"
  ],
  "features": {
    "chat_download": True,
    "prescription_download": True,
    "voice_input": True,
    "multimodal": True,
    "multilingual": True
  },
  "constraints": [],
  "nonfunctional": [],
  "escalation_phrases": [
    "can't breathe"
  ],
  "model": {},
  "demo_scope": {
    "strategy": "sprint1_stories",
    "story_ids": [
      "S1",
      "S2",
      "S3",
      "S4",
      "S5"
    ],
    "ac_ids": [
      "AC-1",
      "AC-2",
      "AC-3",
      "AC-4"
    ],
    "rule_ids": [
      "BR-1",
      "BR-2",
      "BR-3",
      "BR-4"
    ]
  }
}

_SPEC_PATH = os.path.join(os.path.dirname(__file__), "build_spec.json")


def load_spec() -> dict[str, Any]:
    try:
        with open(_SPEC_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return BUILD_SPEC


def meta() -> dict[str, Any]:
    s = load_spec()
    return {
        "project_key": s.get("project_key"),
        "project_name": s.get("project_name"),
        "app_type": s.get("app_type"),
        "app_kind": s.get("app_kind"),
        "summary": s.get("summary"),
        "primary_api": (s.get("api") or {}).get("primary"),
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "rule_ids": [r.get("id") for r in (s.get("business_rules") or [])],
        "modules": s.get("modules") or [],
        "architecture_services": (s.get("architecture") or {}).get("services") or [],
        "demo_scope": s.get("demo_scope") or {},
        "backlog": s.get("backlog") or {},
        "agents": s.get("agents") or [],
        "languages": s.get("languages") or ["en"],
        "features": s.get("features") or {},
        "rag_sources": s.get("rag_sources") or [],
        "domains": s.get("domains") or [],
    }


def list_stories() -> list[dict[str, Any]]:
    return list((load_spec().get("stories") or []))


def list_criteria() -> list[dict[str, Any]]:
    return list((load_spec().get("acceptance_criteria") or []))


def _norm_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (name or "").strip().lower()).strip("_")


def _clean_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {_norm_key(k): v for k, v in (payload or {}).items()}


def evaluate_rules(payload: dict[str, Any]) -> dict[str, Any]:
    """Deterministic decision engine from BRD business rules."""
    s = load_spec()
    rules = s.get("business_rules") or []
    clean = _clean_payload(payload)
    reasons: list[str] = []
    checked: list[str] = []
    approved = True

    if not rules:
        return {
            "decision": "APPROVED",
            "reasons": ["No BRD business rules supplied — demo auto-approve."],
            "checked_rules": [],
            "echo": payload,
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        }

    for r in rules:
        rid = r.get("id") or "BR"
        stmt = str(r.get("statement") or "")
        checked.append(rid)
        stmt_clean = (stmt.replace("≤", "<=").replace("≥", ">=")
                          .replace("&le;", "<=").replace("&ge;", ">="))
        match = re.search(
            r"([a-zA-Z_][a-zA-Z0-9_\s-]*)\s*(>=|<=|==|!=|>|<|=)\s*([0-9.,]+)",
            stmt_clean,
        )
        if not match:
            # Soft text rule: fail closed if statement demands a requirement and no matching value present
            tokens = [w for w in re.findall(r"[a-zA-Z]{4,}", stmt_clean.lower()) if w not in {"must", "should", "shall", "only", "with", "from", "that", "this"}]
            hit = False
            for val in clean.values():
                if isinstance(val, str) and any(t in val.lower() for t in tokens[:4]):
                    hit = True
                    break
            if (not hit) and any(w in stmt_clean.lower() for w in ("must", "shall", "require", "only")):
                approved = False
                reasons.append(f"Failed {rid}: {stmt}")
            else:
                reasons.append(f"Noted {rid}: {stmt}")
            continue

        var_name = _norm_key(match.group(1))
        op = match.group(2).strip()
        if op == "=":
            op = "=="
        target = float(match.group(3).replace(",", ""))

        # FOIR special case often seen in lending BRDs
        if "foir" in var_name and "monthly_income" in clean:
            try:
                existing = float(clean.get("existing_emis", 0) or 0)
                new_emi = float(clean.get("new_emi", 0) or clean.get("emi", 0) or 0)
                income = float(clean["monthly_income"])
                actual = ((existing + new_emi) / income) * 100 if income else 999.0
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: cannot compute FOIR")
                continue
        elif var_name in clean:
            try:
                actual = float(clean[var_name])
            except Exception:
                approved = False
                reasons.append(f"Failed {rid}: field '{var_name}' is not numeric")
                continue
        else:
            approved = False
            reasons.append(f"Missing required field '{var_name}' for {rid}")
            continue

        passed = {
            ">=": actual >= target,
            "<=": actual <= target,
            ">": actual > target,
            "<": actual < target,
            "==": actual == target,
            "!=": actual != target,
        }.get(op, False)
        if not passed:
            approved = False
            reasons.append(f"Failed {rid}: {stmt} (actual {var_name}={actual})")
        else:
            reasons.append(f"Passed {rid}: {stmt}")

    return {
        "decision": "APPROVED" if approved else "DECLINED",
        "reasons": reasons,
        "checked_rules": checked,
        "echo": payload,
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
    }


def build_knowledge() -> dict[str, str]:
    """Legacy keyword map kept for tests; primary chat path uses specialty RAG packs."""
    s = load_spec()
    kb: dict[str, str] = {
        "about": f"{s.get('project_name')} — {s.get('summary') or 'Forge lite demo'}",
        "project": str(s.get("project_key") or ""),
    }
    for src in (s.get("rag_sources") or []):
        kb[_norm_key(str(src))] = f"Knowledge source configured: {src}"
    for dom in (s.get("domains") or []):
        kb[_norm_key(str(dom))] = f"In-scope domain: {dom}"
    for r in (s.get("business_rules") or []):
        stmt = str(r.get("statement") or "")
        kb[_norm_key(r.get("id") or "rule")] = stmt
    for a in (s.get("acceptance_criteria") or []):
        then = str(a.get("then") or "")
        kb[_norm_key(a.get("id") or "ac")] = then
    for st in (s.get("stories") or []):
        title = str(st.get("title") or "")
        kb[_norm_key(st.get("id") or "story")] = f"Story {st.get('id')}: {title}"
    return kb


def specialty_rag_pack() -> dict[str, list[dict[str, str]]]:
    """CDC / PubMed-style lite knowledge snippets for specialty agents."""
    return {
        "cancer care": [
            {"id": "CDC-CA-1", "source": "CDC", "title": "Cancer awareness",
              "text": "Early detection improves outcomes. Know family history, attend age-appropriate screenings, and report unexplained weight loss, lumps, or persistent pain to a clinician."},
            {"id": "PM-CA-1", "source": "PubMed", "title": "Supportive care",
              "text": "Evidence-based cancer care includes symptom control, nutrition support, and mental-health follow-up alongside oncology treatment plans."},
            {"id": "CDC-CA-2", "source": "CDC", "title": "Prevention",
              "text": "Reduce risk with tobacco cessation, limited alcohol, sun protection, physical activity, and vaccination where recommended (e.g., HPV)."},
        ],
        "diabetes": [
            {"id": "CDC-DB-1", "source": "CDC", "title": "Blood sugar basics",
              "text": "Track fasting and post-meal glucose. Seek urgent care for very high readings with vomiting, confusion, or rapid breathing."},
            {"id": "PM-DB-1", "source": "PubMed", "title": "Lifestyle foundation",
              "text": "Medical nutrition therapy, daily activity, medication adherence, and foot checks reduce diabetes complications."},
            {"id": "CDC-DB-2", "source": "CDC", "title": "Hypoglycemia",
              "text": "Symptoms include shakiness, sweating, and confusion. Use fast-acting carbohydrate and recheck; ask your clinician about an action plan."},
        ],
        "mental illness": [
            {"id": "CDC-MH-1", "source": "CDC", "title": "Mental health support",
              "text": "Anxiety and depression are treatable. Sleep, social connection, counseling, and clinician-guided medication can help."},
            {"id": "PM-MH-1", "source": "PubMed", "title": "Crisis awareness",
              "text": "If you feel unsafe or have thoughts of self-harm, contact local emergency services or a crisis line immediately."},
            {"id": "CDC-MH-2", "source": "CDC", "title": "Daily coping",
              "text": "Breathing exercises, brief walks, journaling, and limiting late caffeine can reduce symptom intensity between care visits."},
        ],
        "cardiology": [
            {"id": "CDC-CD-1", "source": "CDC", "title": "Heart risk factors",
              "text": "Control blood pressure, cholesterol, blood sugar, and tobacco use. Report chest pain, sudden weakness, or severe shortness of breath urgently."},
            {"id": "PM-CD-1", "source": "PubMed", "title": "Heart-healthy habits",
              "text": "Mediterranean-style eating, moderate aerobic activity, sodium awareness, and medication adherence improve cardiac outcomes."},
            {"id": "CDC-CD-2", "source": "CDC", "title": "Blood pressure",
              "text": "Home monitoring helps detect trends. Sit quietly, use a validated cuff, and share readings with your clinician."},
        ],
        "respiratory": [
            {"id": "CDC-RS-1", "source": "CDC", "title": "Breathing symptoms",
              "text": "Seek urgent care for severe breathlessnes, blue lips, high fever with cough, or oxygen saturation that your clinician flags as unsafe."},
            {"id": "PM-RS-1", "source": "PubMed", "title": "Asthma / COPD basics",
              "text": "Use controller and rescue inhalers as prescribed, avoid smoke/triggers, and keep an updated action plan."},
            {"id": "CDC-RS-2", "source": "CDC", "title": "Infection prevention",
              "text": "Hand hygiene, vaccination when recommended, and staying home while contagious reduce respiratory infection spread."},
        ],
        "general care": [
            {"id": "CDC-GN-1", "source": "CDC", "title": "General wellness",
              "text": "Hydration, sleep, movement, and primary-care checkups support recovery. This assistant shares education, not a diagnosis."},
            {"id": "PM-GN-1", "source": "PubMed", "title": "When to escalate",
              "text": "Worsening pain, neurological changes, chest pain, severe distress, or inability to keep fluids down needs clinician review."},
        ],
    }


def _normalize_domain(name: str) -> str:
    n = (name or "").lower()
    if any(k in n for k in ("cancer", "oncolog")):
        return "cancer care"
    if "diabetes" in n or "glucose" in n:
        return "diabetes"
    if any(k in n for k in ("mental", "depress", "anxiety", "psych")):
        return "mental illness"
    if any(k in n for k in ("cardio", "heart", "cardiac")):
        return "cardiology"
    if any(k in n for k in ("respir", "lung", "asthma", "breath", "copd")):
        return "respiratory"
    return "general care"


def detect_agent(message: str, preferred: str | None = None) -> dict[str, Any]:
    s = load_spec()
    agents = s.get("agents") or []
    text = (message or "").lower()
    if preferred:
        for a in agents:
            if preferred.lower() in str(a.get("id", "")).lower() or preferred.lower() in str(a.get("name", "")).lower():
                return a
    scored = []
    for a in agents:
        dom = _normalize_domain(str(a.get("domain") or a.get("name") or ""))
        keys = dom.split()
        score = sum(1 for k in keys if k in text)
        # synonym boosts
        boosts = {
            "cancer care": ["cancer", "tumor", "oncology", "chemo"],
            "diabetes": ["diabetes", "sugar", "insulin"],
            "mental illness": ["mental", "anxiety", "depression", "stress"],
            "cardiology": ["heart", "cardio", "pressure", "chest"],
            "respiratory": ["breath", "asthma", "lung", "cough", "respir"],
        }
        score += sum(2 for k in boosts.get(dom, []) if k in text)
        scored.append((score, a))
    scored.sort(key=lambda x: x[0], reverse=True)
    if scored and scored[0][0] > 0:
        return scored[0][1]
    for a in agents:
        if "general" in str(a.get("domain") or "").lower() or "general" in str(a.get("name") or "").lower():
            return a
    return agents[-1] if agents else {"id": "A1", "name": "General Care Agent", "domain": "General Care"}


def retrieve_snippets(domain: str, message: str, limit: int = 2) -> list[dict[str, str]]:
    pack = specialty_rag_pack()
    key = _normalize_domain(domain)
    docs = list(pack.get(key) or pack["general care"])
    text = (message or "").lower()
    ranked = []
    for d in docs:
        blob = (d.get("title", "") + " " + d.get("text", "")).lower()
        score = sum(1 for w in re.findall(r"[a-z]{4,}", text) if w in blob)
        ranked.append((score, d))
    ranked.sort(key=lambda x: x[0], reverse=True)
    top = [d for _, d in ranked[:limit]]
    return top or docs[:limit]


def _localize(text: str, language: str) -> str:
    lang = (language or "en").lower()
    prefix = {
        "hi": "hindi guidance · ",
        "es": "orientación en español · ",
        "en": "",
    }.get(lang[:2], "")
    disclaimer = {
        "hi": " यह सामान्य शिक्षा है, चिकित्सकीय सलाह नहीं।",
        "es": " Esto es educación general, no un diagnóstico médico.",
        "en": " This is general education, not a medical diagnosis.",
    }.get(lang[:2], " This is general education, not a medical diagnosis.")
    return prefix + text + disclaimer


def compose_prescription(agent: dict[str, Any], snippets: list[dict[str, str]]) -> dict[str, Any]:
    tips = [s.get("text", "")[:120] for s in snippets[:2]]
    return {
        "title": f"Care tip sheet — {agent.get('name') or 'Care Agent'}",
        "agent": agent.get("name"),
        "domain": agent.get("domain"),
        "recommendations": tips or ["Follow up with your clinician for personalized advice."],
        "disclaimer": "Educational demo only. Not a clinical prescription.",
    }


def chat_answer(
    message: str,
    language: str = "en",
    agent_id: str | None = None,
    attachment_note: str | None = None,
) -> dict[str, Any]:
    s = load_spec()
    text = (message or "").strip()
    low = text.lower()
    escalations = [p.lower() for p in (s.get("escalation_phrases") or [])]
    # Always escalate clear self-harm / emergency language
    hard = ["suicid", "want to die", "kill myself", "chest pain", "can't breathe", "cannot breathe"]
    if any(p and p in low for p in (escalations + hard)):
        return {
            "answer": _localize(
                f"Safety escalation via {s.get('project_name')}. If this is an emergency, call local emergency services now.",
                language,
            ),
            "source": "SAFETY",
            "agent": {"id": "SAFE", "name": "Safety Guardrail"},
            "citations": [],
            "prescription": None,
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
        }

    agent = detect_agent(text, preferred=agent_id)
    snippets = retrieve_snippets(str(agent.get("domain") or ""), text, limit=2)
    sources = s.get("rag_sources") or ["CDC", "PubMed"]
    cite_bits = []
    answer_parts = []
    if attachment_note:
        answer_parts.append(f"I noted your attachment/context: {attachment_note[:120]}.")
    answer_parts.append(
        f"{agent.get('name') or 'Care Agent'} here - focusing on {agent.get('domain') or 'your concern'}."
    )
    for sn in snippets:
        answer_parts.append(sn.get("text") or "")
        cite_bits.append({"id": sn.get("id"), "source": sn.get("source"), "title": sn.get("title")})
    if "not feeling" in low or "unwell" in low or "sick" in low:
        answer_parts.append(
            "Since you feel unwell, share main symptoms (fever, pain location, duration). "
            "I can route you to the most relevant specialty agent."
        )
    if any(k in low for k in ("awareness", "aware", "prevent", "educat")):
        answer_parts.append(
            "For awareness campaigns: use trusted {0} materials, community screening drives, "
            "and clear call-to-action for early checkups.".format("/".join(sources[:2]))
        )
    answer = _localize(" ".join(p for p in answer_parts if p), language)
    rx = compose_prescription(agent, snippets)
    return {
        "answer": answer,
        "source": "AGENT_RAG",
        "agent": agent,
        "citations": cite_bits,
        "rag_sources": sources,
        "language": language or "en",
        "prescription": rx,
        "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
    }


def predict_payload(payload: dict[str, Any], model: Any = None) -> dict[str, Any]:
    s = load_spec()
    model_cfg = s.get("model") or {}
    feats = list(model_cfg.get("independent_variables") or [])
    target = model_cfg.get("dependent_variable")
    clean = _clean_payload(payload)
    if model is None:
        # Lightweight demo prediction from features so QA has project-specific output
        vals = [float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats] or [0.0]
        score = sum(vals) / max(len(vals), 1)
        return {
            "prediction": round(score, 4),
            "target": target,
            "features_used": feats,
            "mode": "heuristic_demo",
            "ac_ids": [a.get("id") for a in (s.get("acceptance_criteria") or [])],
            "story_ids": [st.get("id") for st in (s.get("stories") or [])],
        }
    import numpy as np
    x = np.array([[float(clean.get(_norm_key(f), clean.get(f, 0) or 0)) for f in feats]])
    try:
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(x)[0].tolist()
            pred = model.predict(x)[0]
            try:
                pred = pred.item()
            except Exception:
                pass
            return {"prediction": pred, "proba": proba, "target": target, "features_used": feats, "mode": "model"}
        pred = model.predict(x)[0]
        try:
            pred = pred.item()
        except Exception:
            pass
        return {"prediction": pred, "target": target, "features_used": feats, "mode": "model"}
    except Exception as e:
        return {"error": str(e), "features_used": feats}
