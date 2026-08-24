# Al-Marsoos Security - AI Agent Integration SDLC Execution Plan

## 1. Project Goal
Integrate an intelligent AI chatbot into the Al-Marsoos static React website that can fetch live company data (Services, Leadership, Credentials) and mathematically calculate event security guard requirements based on guest count.

---

## 2. Execution Phases

### Phase 1: Knowledge Base Preparation (Frontend)
- **Status:** COMPLETED
- **Description:** Created a Node.js script (scrape_data.js) in the React repository that parses all Markdown and Text content from the /content folder and compiles it into a single JSON file (public/data.json).
- **Outcome:** The frontend now serves a live API at https://[github-pages-url]/data.json containing the single source of truth for all company knowledge.

### Phase 2: Agent Architecture & Tooling (Backend)
- **Status:** COMPLETED
- **Description:** 
  1. Built custom Python tools (	ools.py) capable of making HTTP GET requests to the frontend's data.json to look up services and leadership.
  2. Built the Event Security Calculator tool.
  3. Evaluated Google ADK 2.0 multi-agent router architecture, but ultimately **pivoted to a Single-Agent Architecture** using the standard google-genai SDK for speed and simplicity.
- **Testing Technique:** **Manual API Contract Testing**. We deployed the FastAPI server locally and used curl to verify the JSON payload contract (sending {"message": "..."} and receiving {"response": "..."}).

### Phase 3: API Integration & Security (Full Stack)
- **Status:** COMPLETED
- **Description:** 
  1. Updated the React ChatWidget.jsx to swap mock logic for a live asynchronous etch() POST request to the Python API.
  2. Built the Python backend as a Docker container and deployed it to Google Cloud Run.
  3. Secured the Cloud Run backend by configuring Vertex AI Application Default Credentials, entirely eliminating hardcoded API keys.
- **Testing Technique:** **Graceful Degradation Testing (Fault Injection)**. We intentionally broke the Cloud Run server (and simulated CORS blocks) to verify that the React frontend would not crash. Instead, it successfully degrades gracefully and displays a fallback WhatsApp link to the user.

---

## 3. Deployment Topology
- **Frontend App:** Hosted on GitHub Pages (gh-pages branch).
- **Frontend Data:** Served statically from github-pages/data.json.
- **Backend API:** Hosted on Google Cloud Run (Containerized FastAPI).
- **AI Brain:** Google Vertex AI (Gemini 2.5 Flash).
