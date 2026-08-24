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
                    "2. Jobs/Careers: If asked about jobs, hiring, or submitting a CV, explain our high military standards and provide link: [Careers Page](/careers).\n"
                    "3. Services: If asked about what services are offered, use fetch_company_knowledge tool and provide link: [Our Services](/services).\n"
                    "4. Licenses/Legitimacy: If asked about licenses or legal registration, state AMS is Ministry of Interior licensed. Provide link: [Credentials Page](/credentials).\n"
                    "5. Clients/Portfolio: If asked about our clients, use fetch_company_knowledge tool and provide link: [Our Clients](/clients).\n"
                    "6. Location: If asked for the office location, provide ONLY this exact Google Maps link: [Al-Marsoos Head Office](https://www.google.com/maps/search/?api=1&query=Al-Marsoos+Security+Services+Rawalpindi).\n"
                    "7. Contact: If asked for a phone number or how to get in touch, provide ONLY the WhatsApp link: [0310 6460024](https://wa.me/923106460024).\n"
                    "8. Leadership: If asked about the team, directors, or leadership, provide ONLY the link: [Leadership Team](/leadership).\n"
                    "9. Sales: If event guest count provided, use calculate_event_security tool and provide link: [Instant Security Estimator](/contact?calculator=true).\n"
                    "10. CONVERSION RULE: ONLY provide the [Contact Us](/contact) link if you successfully recommended a service, provided a quote, or if the user explicitly asks to contact sales.\n"
                    "11. UI FORMATTING: Do NOT use Markdown asterisks (** for bold or * for lists). Use hyphens (-) for lists. You MUST still format all links strictly as Markdown e.g., [Link Name](/url)."
                )
            }
        )
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
