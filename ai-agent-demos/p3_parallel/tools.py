def search_news(query: str) -> str:
    """Searches the live news web for the query."""
    return f"[News Result for '{query}']: The company just announced a new AI product line today."

def search_database(query: str) -> str:
    """Searches the internal company database/docs for the query."""
    return f"[Database Result for '{query}']: Internal policy requires all new AI products to undergo privacy review."
