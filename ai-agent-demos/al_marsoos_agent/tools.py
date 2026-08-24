import requests

def calculate_event_security(guest_count: int) -> dict:
    """Calculates required guards based on guest count (approx 1 guard per 50 guests)."""
    guards_needed = max(1, guest_count // 50)
    return {
        "recommended_guards": guards_needed,
        "explanation": f"Based on our standard deployment protocol of 1 guard per 50 guests, we recommend {guards_needed} guards for an event of {guest_count} attendees."
    }

def fetch_company_knowledge(category: str) -> dict:
    """Retrieves the Single Source of Truth company data directly from the live React website.
    Valid categories are 'services', 'clients', 'leadership', 'urls', or 'all'.
    """
    url = "https://goshi-f-a.github.io/al-marsoos-security-coy/data.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if category != 'all' and category in data:
            return {category: data[category]}
        return data
    except Exception as e:
        return {"error": f"Failed to fetch company knowledge: {str(e)}"}
