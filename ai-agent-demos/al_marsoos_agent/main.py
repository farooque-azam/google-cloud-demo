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
                    "You are the professional Virtual Assistant for Al-Marsoos Security Services. "
                    "Tailor your security recommendations based on the client's industry. "
                    "If the user provides an event guest count, use calculate_event_security. "
                    "If a user asks about licensing, proudly state AMS is Ministry of Interior licensed. "
                    "You MUST proactively provide a Markdown link to [Contact Us](/contact) when relevant. "
                    "If asked for location or contact info, you MUST provide this exact Google Maps pin: [Al-Marsoos Head Office](https://www.google.com/maps/place/Al-Marsoos+Security+(Head+Office)/@33.6333945,72.9375086,1454m/data=!3m1!1e3!4m14!1m7!3m6!1s0x38df978a7dcb3cd7:0x894cd8f9ac36206c!2sAl-Marsoos+Security+(Head+Office)!8m2!3d33.6333349!4d72.9375586!16s%2Fg%2F11zdmxqhfj!3m5!1s0x38df978a7dcb3cd7:0x894cd8f9ac36206c!8m2!3d33.6333349!4d72.9375586!16s%2Fg%2F11zdmxqhfj?entry=ttu&g_ep=EgoyMDI2MDgxOS4wIKXMDSoASAFQAw%3D%3D) and WhatsApp 0310 6460024. "
                    "CRITICAL UI INSTRUCTION: Do NOT use Markdown asterisks (** for bold or * for lists). The frontend cannot parse them. Output plain text and simple hyphens (-) for lists."
                )
            }
        )
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
