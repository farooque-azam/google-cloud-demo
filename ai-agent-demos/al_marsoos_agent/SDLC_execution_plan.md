# Agentic Software Development Life Cycle (SDLC) Execution Plan
**Project:** Al-Marsoos Security Virtual Assistant (ADK 2.0)

## The SDLC Journey: From Concept to Agentic AI

Developing an AI agent requires a paradigm shift from traditional procedural programming to **Specification and Behavior-Driven Development (SpecDD & BDD)**. Instead of hardcoding if/else logic, we architect an intelligent system driven by Personas, Tools, and Routing Patterns. 

This document captures the entire end-to-end SDLC journey we followed to engineer the Al-Marsoos Virtual Assistant.

---

### Phase 0: Requirements Engineering & Specifications
**Goal:** Define the system boundaries, behavior, and interfaces before writing any implementation code.

In traditional SDLC, requirements map to database schemas and functions. In Agentic SDLC, requirements map to **Prompts, Personas, and Tools**.

1. **Behavior-Driven Development (BDD):** 
   - *Deliverable:* `docs/REQUIREMENTS.md`
   - *Journey:* We analyzed the core user demographics of Al-Marsoos Security and translated them into 8 distinct User Personas (e.g., Healthcare, Job Seeker, Trust-Seeking). By defining User Stories for each Persona, we established a clear "Grading Rubric" that the AI must satisfy, which serves as the foundation for future Automated Evals.
   
2. **Specification-Driven Development (SpecDD):** 
   - *Deliverable:* `docs/TOOL_SPECS.md`
   - *Journey:* We defined strict JSON schemas (Interfaces) for the tools our AI would need. By mathematically defining the `calculate_event_security` tool's inputs before writing the Python code, we enforced a strict Separation of Concerns. The LLM handles the natural language, while deterministic Python handles the business logic.

---

### Phase 1: Data Extraction (The Single Source of Truth)
**Goal:** Prevent AI Hallucinations by providing real-time, grounded facts.

A major risk in Agentic AI is hallucination—inventing fake prices, services, or broken URLs. We mitigated this by building a bridge between the existing React frontend and the new AI backend.

- *Deliverable:* `scripts/extract_knowledge.js` & `data.json`
- *Journey:* We engineered a Node.js script inside the React repository to parse existing React files (`Services.jsx`, `Clients.jsx`) and the `sitemap.xml`. This script extracts raw business data and compiles it into a `public/data.json` file. 
- *Result:* When deployed to GitHub Pages, this acts as the API's Single Source of Truth. If the website updates, a single `npm run update-ai` command automatically re-trains the AI without touching backend code.

---

### Phase 2: Backend Architecture (The ADK 2.0 Router Pattern)
**Goal:** Build a highly cohesive, decoupled AI backend capable of complex intent routing.

We utilized the **Google Agent Development Kit (ADK 2.0)** to implement the **Routing Pattern**. This prevents "Prompt Bloat" (confusing a single agent with too many rules).

1. **Tool Implementation:**
   - *Deliverable:* `tools.py`
   - *Journey:* We implemented the actual Python business logic mapped from Phase 0. We built the integer division math for event security and the HTTP GET request logic to fetch the `data.json` from Phase 1.
2. **Multi-Agent Orchestration:**
   - *Deliverable:* `agent.py`
   - *Journey:* We combined our 8 Personas into 3 highly cohesive Sub-Agents (`hr_agent`, `trust_agent`, `sales_agent`). We then deployed a `root_agent` to act as the Gateway Router. The Router autonomously analyzes user intent and delegates the conversation to the correct specialist agent.
3. **API Gateway (FastAPI):**
   - *Deliverable:* `main.py`
   - *Journey:* We wrapped the ADK Agent inside a FastAPI web server, utilizing `Pydantic` for strict payload validation and `CORSMiddleware` to secure the API to the official Al-Marsoos domain.

### 2.5 API Interaction & Security (Post-Deployment)
Once deployed to Cloud Run, the FastAPI server provides powerful out-of-the-box features:
- **Interactive Swagger UI:** Appending `/docs` to the URL provides an auto-generated interface to manually test the AI Agent directly from the browser.
- **Programmatic Access:** The API can be queried via terminal commands (e.g., `curl`) or scripts.
- **Security Nuance (CORS vs. Auth):** We locked down `CORSMiddleware` to the GitHub Pages domain. However, students must learn that CORS is a *browser-level* security feature (stopping malicious websites). It does not block terminal scripts or `curl`. For enterprise production, a public chat API must implement **API Keys, reCAPTCHA, or Rate Limiting** to prevent Denial of Wallet script attacks.

---

### Phase 3: Frontend Integration & Deployment
**Goal:** Connect the user-facing React UI to the intelligent backend.

- *Deliverable:* `ChatWidget.jsx` Integration and Cloud Run Deployment
- *Journey:* 
  1. The local FastAPI server will be containerized via Docker and deployed to Google Cloud Run to provide a highly available HTTPS endpoint.
  2. The hardcoded, mock `if/else` logic in the React `ChatWidget.jsx` will be stripped out and replaced with an asynchronous `fetch()` POST request to the live Cloud Run API.
  3. The UI will seamlessly render Markdown links natively provided by the Agent.

---

## Conclusion of the SDLC Journey
By adhering strictly to this phased SDLC, we transformed a static, hardcoded chat widget into an autonomous, tool-calling Agentic system. The separation of Knowledge (Phase 1), Logic (Phase 2), and Presentation (Phase 3) guarantees enterprise-level scalability, maintainability, and deterministic behavior.
