
"""
=============================================================================
Google AI Studio - Gemini Agent Sample with Function Calling
=============================================================================

This sample demonstrates how to build a basic AI Agent using the official 
Google GenAI SDK (`google-genai`).

Key Concept - Function Calling (Agent Tools):
  Large Language Models (LLMs) cannot execute real-time code or fetch live
  data on their own. By passing Python functions as "tools", Gemini can
  decide when to call a function, retrieve the result, and use it to formulate
  its answer.

How to Run:
  1. Get a free API Key from Google AI Studio: https://aistudio.google.com/
  2. Set the environment variable:
       export GOOGLE_API_KEY="your_api_key_here"
  3. Execute the script:
       python hello_agent.py
=============================================================================
"""

import os
import datetime
from dotenv import load_dotenv, find_dotenv

# Import the Google GenAI SDK
from google import genai
from google.genai import types


# ---------------------------------------------------------------------------
# STEP 1: Define Python Functions (Tools for the Agent)
# ---------------------------------------------------------------------------
# Type hints (e.g. `-> str`) and docstrings are CRITICAL here!
# Gemini inspects the function name, arguments, type annotations, and docstring
# to understand WHAT the tool does and WHEN it should be invoked.
def get_current_time() -> str:
    """Returns the current server date and time as a formatted string."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The current server time is {now}."


# ---------------------------------------------------------------------------
# STEP 2: Main Application Logic
# ---------------------------------------------------------------------------
def main():
    load_dotenv(find_dotenv())
    # 2a. Retrieve the API key from environment variables for security
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY is not set.")
        print("💡 Get your free API key at: https://aistudio.google.com/")
        print("   Then run: export GEMINI_API_KEY='your_key_here'\n")
        return

    # 2b. Initialize the Gemini Client
    # The client handles all API communications with Google AI Studio.
    client = genai.Client(api_key=api_key)

    # 2c. Send a user request to Gemini with Tools attached
    print("🤖 Sending prompt to Gemini Agent...")
    print("   User Prompt: 'What time is it right now? Use your tool to check.'\n")

    chat = client.chats.create(
        # Specify the model. 'gemini-3.5-flash' is fast and supports tool execution.
        model="gemini-3.5-flash",

        # Configure agent behavior, system instructions, and available tools
        config=types.GenerateContentConfig(
            # Pass our Python function in the `tools` list.
            # Gemini automatically converts this function signature into a JSON schema!
            tools=[get_current_time],

            # System instructions give the agent its identity, guidelines, and guardrails
            system_instruction=(
                "You are a helpful AI assistant equipped with function-calling capabilities. "
                "Always use available tools when precise or real-time information is requested."
            )
        )
    )

    response = chat.send_message("What time is it right now? Use your tool to check.")

    # 2d. Print the agent's final text output
    print("--- 💬 Agent Response ---")
    print(response.text)


# Standard Python entry point
if __name__ == "__main__":
    main()
