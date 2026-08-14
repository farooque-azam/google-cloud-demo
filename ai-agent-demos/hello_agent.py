"""
Sample Google AI Studio Agent using the Gemini API.

To run:
  export GEMINI_API_KEY="your_api_key_from_ai_studio"
  python hello_agent.py
"""

import os
from google import genai
from google.genai import types

def get_current_time() -> str:
    """Returns the current server time."""
    import datetime
    return f"The current server time is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Please set your GEMINI_API_KEY environment variable.")
        print("Get your free API key at: https://aistudio.google.com/")
        return

    client = genai.Client(api_key=api_key)

    print("Sending prompt to Gemini Agent...")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="What time is it right now? Use your tool to check.",
        config=types.GenerateContentConfig(
            tools=[get_current_time],
            system_instruction="You are a helpful AI assistant equipped with function-calling capabilities."
        )
    )

    print("\n--- Agent Response ---")
    print(response.text)

if __name__ == "__main__":
    main()
