import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from tools import calculate_event_security, fetch_company_knowledge

# Initialize standard Gemini Client using Vertex AI (for Cloud Run)
client = genai.Client(
    vertexai=True, 
    project="gen-lang-client-0441613979", 
    location="us-central1"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    try:
        # Create a single, synchronous Gemini model using google-genai
        # This replaces the complex ADK streaming generator and router
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=req.message,
            config={
                'tools': [calculate_event_security, fetch_company_knowledge],
                'system_instruction': (
                    "You are the Virtual Assistant for Al-Marsoos Security (AMS). Tone: Military-professional, concise.\n\n"
                    "RULES:\n"
                    "1. Guardrail: Refuse questions unrelated to Al-Marsoos or physical security.\n"
                    "2. HR/Jobs: Explain high military standards. Provide link: [Careers Page](/careers).\n"
                    "3. Trust/Licenses: State AMS is Ministry of Interior licensed and led by retired Pakistan Army officers. Provide link: [Credentials Page](/credentials).\n"
                    "4. Contact/Location: Provide link [Leadership Team](/leadership), WhatsApp (0310 6460024), and this exact Google Maps link: [Al-Marsoos Head Office](https://www.google.com/maps/search/?api=1&query=Al-Marsoos+Security+Services+Rawalpindi).\n"
                    "5. Sales: If event guest count provided, use calculate_event_security tool and provide link: [Instant Security Estimator](/contact?calculator=true).\n"
                    "6. CONVERSION RULE: ONLY provide the [Contact Us](/contact) link if you successfully recommended a service, provided a quote, or if the user explicitly asks to contact sales.\n"
                    "7. UI FORMATTING: Do NOT use Markdown asterisks (** for bold or * for lists). Output plain text. Use hyphens (-) for lists."
                )
            }
        )
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
