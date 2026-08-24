# Concept Note - Requirements Engineering for AI Agents

## Traditional SDLC vs. Persona-Driven Specification (SpecDD & BDD)

When engineering traditional software (like a database application), user inputs are strictly controlled by buttons, forms, and dropdown menus. Therefore, traditional Requirements Engineering focuses heavily on defining UI constraints and data models.

However, when engineering **Agentic AI**, the user inputs are unpredictable, open-ended natural language. To successfully build robust AI agents, we must adapt the 4 classic phases of Requirements Engineering into a **Persona-Driven (BDD)** approach.

---

### Phase 1: Requirements Elicitation (Gathering)

* **Traditional Approach:** Stakeholders ask, *"What screens do we need?"* and *"What fields go in the database?"*
* **AI-Driven Approach (Persona Identification):** We ask, *"Who is talking to this bot?"* We identify the core **Personas** (e.g., The Event Planner, The Job Seeker). We gather the conversational intents and goals of these specific human beings rather than gathering UI features.
  * *Example:* Instead of designing a "Quote Calculator Web Form", we define a Persona: **"The Corporate Client who wants a fast price estimate for a wedding."**

### Phase 2: Requirements Analysis (Modeling & Negotiation)

* **Traditional Approach:** Drawing Entity-Relationship (ER) diagrams, resolving conflicts between database tables, and removing contradictory features.
* **AI-Driven Approach (User Story Mapping):** We write **User Stories** to map the user's intent to the Agent's expected behavior. We analyze overlapping intents and resolve them via Architecture.
  * *Example:* We notice both the Sales Persona and the HR Persona frequently ask about the company's office location. We analyze this overlap and negotiate a technical solution: We will create a shared get_company_location() Python tool that both sub-agents can use.

### Phase 3: Requirements Specification (Documenting)

* **Traditional Approach:** Writing a massive, formal **SRS (Software Requirements Specification)** document containing rigid rules (e.g., *"Section 1.1: The system shall display a red Submit button. Section 1.2: The system shall return a 200 OK."*).
* **AI-Driven Approach (BDD Scenarios):** Because LLMs generate unpredictable natural language, rigid rules fail. Instead, we write strict **BDD (Behavior-Driven Development)** documents using the Given / When / Then format.
  * *Example:*
    * **Given** the user is an Event Planner Persona...
    * **When** they provide a guest count of 500 people...
    * **Then** the agent must use the math tool to recommend exactly 10 guards.

### Phase 4: Requirements Validation (Testing)

* **Traditional Approach:** Stakeholders manually read the SRS document and sign off on it to confirm it represents their wishes before coding begins.
* **AI-Driven Approach (Agentic Evaluations / Evals):** The BDD User Stories are literally converted into **Automated Evals**. The beauty of this approach is that the Specification Document *is* the testing framework.
  * *Example:* We write a Python test script that sends the text *"I have 500 guests"* to the AI Agent. The script then mathematically grades the AI's response to validate if it successfully output the number "10", proving the requirement was met!
