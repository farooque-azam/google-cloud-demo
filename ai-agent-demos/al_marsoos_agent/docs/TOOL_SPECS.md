# Al-Marsoos Agent Tool Specifications (SpecDD)

This document defines the strict technical contracts (JSON Schemas) for the Python tools that the ADK 2.0 Agent will use to satisfy the BDD User Stories. By specifying these contracts before coding, we guarantee deterministic AI behavior.

---

## 1. Tool: `calculate_event_security`

**Description:** Calculates the mathematically recommended number of security guards needed for a specific event based on Al-Marsoos deployment protocols (e.g., 1 guard per 50 guests).

**JSON Schema Contract (Input):**
```json
{
  "name": "calculate_event_security",
  "description": "Calculates required guards based on guest count.",
  "parameters": {
    "type": "object",
    "properties": {
      "guest_count": {
        "type": "integer",
        "description": "The total number of attendees expected at the event."
      }
    },
    "required": ["guest_count"]
  }
}
```

---

## 2. Tool: `fetch_company_knowledge`

**Description:** Performs an HTTP GET request to `https://goshi-f-a.github.io/al-marsoos-security-coy/data.json` to read the live company data directly from the React frontend. 

*Architectural Note:* This JSON file acts as the Single Source of Truth. It contains Services, Client Portfolios, Leadership info, AND the exact `sitemap.xml` URL slugs to ensure the Agent never hallucinates a React router link.

**JSON Schema Contract (Input):**
```json
{
  "name": "fetch_company_knowledge",
  "description": "Retrieves the Single Source of Truth company data containing available services, client portfolios, leadership info, and valid website URLs.",
  "parameters": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "enum": ["services", "clients", "leadership", "urls", "all"],
        "description": "The specific category of knowledge to fetch. Use 'all' if unsure."
      }
    },
    "required": ["category"]
  }
}
```

---

## Technical Notes for Implementation (Phase 2)
*   These JSON schemas must be mapped directly to Google ADK `FunctionDeclaration` objects in our Python backend.
*   By relying entirely on `fetch_company_knowledge` for URL slugs and service lists, the AI becomes dynamically tethered to the React website. If the React website updates, the AI updates automatically without any backend code changes.
