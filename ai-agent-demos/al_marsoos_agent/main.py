from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import root_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default_session"

@app.get("/")
def read_root():
    return {"message": "Al-Marsoos ADK 2.0 Agent API is Running!"}

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    try:
        # Pass the user's message into the ADK root_agent (the Router)
        # The agent will autonomously route it to the correct sub-agent
        result = root_agent.run_live(req.message)
        
        # ADK returns an object, we extract the text
        response_text = getattr(result, 'text', str(result))
        
        return {"response": response_text}
    except Exception as e:
        return {"error": str(e)}
