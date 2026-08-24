import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from tools import calculate_event_security, fetch_company_knowledge

# Initialize standard Gemini Client
client = genai.Client()

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
                    "If asked to contact leadership or for location, use fetch_company_knowledge or provide WhatsApp 0310 6460024."
                )
            }
        )
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
