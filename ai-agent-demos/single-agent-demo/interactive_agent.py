"""
=============================================================================
Interactive Gemini AI Agent with Function Calling (Tools)
=============================================================================

WHAT THIS SCRIPT DEMONSTRATES:
1. Agentic AI & Tool Execution:
   Large Language Models (LLMs) do not have real-time access to live server
   data or system information on their own. By attaching Python functions as 
   "tools", Gemini can automatically decide WHEN to run code, RETRIEVE real-time
   data (e.g. server time/location or math calculations), and incorporate those
   results into its final answer.

2. SDK Usage (`google-genai`):
   Uses the official Google GenAI SDK (`google.genai`) to create a persistent 
   multi-turn chat session (`client.chats.create`) with system guardrails 
   and tool definitions.

3. Resilient Error Handling & Fallbacks:
   Includes automatic retry logic that gracefully switches between Gemini Flash 
   models if a temporary high-demand spike (503/500) occurs.

HOW TO RUN THIS SCRIPT:
  python3 ai-agent-demos/interactive_agent.py
=============================================================================
"""

import os
import sys
import time
import socket
import platform
import datetime
from dotenv import load_dotenv, find_dotenv

# Import the official Google GenAI SDK and its configuration types
from google import genai
from google.genai import types


# ===========================================================================
# STEP 1: DEFINE AGENT TOOLS (PYTHON FUNCTIONS)
# ===========================================================================
# IMPORTANT CONCEPT - TOOL REGISTRATION:
# Type annotations (e.g., `-> str`) and docstrings (the triple-quoted descriptions)
# are CRITICAL! Gemini reads the docstring to understand WHAT the tool does,
# and inspects parameter types to know HOW to supply arguments to it.

def get_current_time() -> str:
    """
    Tool: Returns the current server date, time, and exact server location/host details.
    
    When a user asks for live server time or host/location information, Gemini 
    triggers this function automatically.
    """
    # Print a visible log to show when the AI Agent decides to invoke this tool
    print("\n---> call function: get_current_time()")
    
    # 1. Fetch current server timestamp and timezone
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tz = time.tzname[0] if time.tzname else "UTC"
    
    # 2. Gather system hardware and network details
    hostname = socket.gethostname()
    os_info = f"{platform.system()} {platform.release()}"
    location_desc = "Google Cloud Shell VM (us-central1 / GCP Infrastructure)"

    # 3. Format the data string to return back to Gemini
    data = (
        f"Time: {now} {tz} | "
        f"Server Hostname: {hostname} | "
        f"OS Environment: {os_info} | "
        f"Location: {location_desc}"
    )

    # Print log showing the data being sent back to Gemini
    print(f"---> receiving data from function: {data}\n")
    
    # Return string result to the model
    return data


def calculate(expression: str) -> str:
    """
    Tool: Evaluates a mathematical expression safely and returns the numeric result.
    
    Args:
        expression (str): A mathematical expression string, e.g. "254 * 387 + 1024".
    """
    # Print a log showing the argument Gemini supplied to this tool
    print(f"\n---> call function: calculate(expression='{expression}')")
    
    try:
        # Safely evaluate mathematical expressions without allowing arbitrary code execution
        result_val = eval(expression, {"__builtins__": None}, {})
        data = f"Calculation result for '{expression}': {result_val}"
        print(f"---> receiving data from function: {data}\n")
        return data
    except Exception as e:
        err_msg = f"Error evaluating expression '{expression}': {str(e)}"
        print(f"---> receiving data from function: {err_msg}\n")
        return err_msg


# List of primary and backup models for resilient fallback
MODELS = ["gemini-3.6-flash", "gemini-3.5-flash"]


# ===========================================================================
# STEP 2: MAIN APPLICATION LOGIC
# ===========================================================================
def main():
    load_dotenv(find_dotenv())
    # -----------------------------------------------------------------------
    # 2a. Check API Key Authentication
    # -----------------------------------------------------------------------
    # Retrieve the API key from environment variables for security (never hardcode keys!)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY environment variable is not set.")
        print("💡 Set your API key in terminal: export GEMINI_API_KEY='your_key'")
        sys.exit(1)

    # Initialize the Google GenAI Client
    client = genai.Client(api_key=api_key)

    # Print UI Header
    print("=" * 65)
    print("🤖 Welcome to the Interactive Gemini AI Agent!")
    print("   Type your prompt below. Type 'exit', 'quit', or 'q' to end.")
    print("=" * 65 + "\n")

    current_model_idx = 0

    # -----------------------------------------------------------------------
    # 2b. Helper Function to Create Chat Session
    # -----------------------------------------------------------------------
    def get_chat(model_name):
        """
        Creates a multi-turn chat session with tools and system instructions attached.
        """
        return client.chats.create(
            model=model_name,
            config=types.GenerateContentConfig(
                # Pass our Python functions in the `tools` list.
                # Gemini automatically converts these functions into JSON schema definitions!
                tools=[get_current_time, calculate],
                
                # System instructions define the agent's identity, guidelines, and guardrails
                system_instruction=(
                    "You are a helpful interactive AI Assistant. "
                    "You have access to tools for checking server time/location and calculating math. "
                    "Always use available tools when precise, real-time, or system location information is requested. "
                    "When presenting server time or location to the user, include the exact server hostname, OS, "
                    "and location details returned by the tool. "
                    "IMPORTANT: Do NOT use LaTeX math syntax or backslashes like \\( ... \\) or \\times in your output. "
                    "Always write math expressions in plain, simple text (e.g., '3 + 4 * 5 = 23')."
                )
            )
        )

    # Initialize chat with the primary model
    chat = get_chat(MODELS[current_model_idx])

    # -----------------------------------------------------------------------
    # 2c. Interactive User Input Loop
    # -----------------------------------------------------------------------
    while True:
        try:
            # Get user prompt from terminal input
            user_input = input("👤 You: ").strip()
            
            # Skip empty lines
            if not user_input:
                continue

            # Check if user wants to exit
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\n👋 Goodbye!")
                break

            response = None
            max_retries = 3

            # ---------------------------------------------------------------
            # 2d. Send Message with Resilient Retry & Fallback
            # ---------------------------------------------------------------
            for attempt in range(max_retries):
                try:
                    # Send prompt to Gemini chat session
                    response = chat.send_message(user_input)
                    break  # Success! Exit retry loop
                except Exception as e:
                    err_str = str(e)
                    # If high-demand (503/500/UNAVAILABLE) occurs, switch to fallback model
                    if any(code in err_str for code in ["503", "500", "UNAVAILABLE", "INTERNAL"]):
                        current_model_idx = (current_model_idx + 1) % len(MODELS)
                        new_model = MODELS[current_model_idx]
                        print(f"⚠️ High demand on current model. Switching to fallback model '{new_model}'...")
                        chat = get_chat(new_model)
                        time.sleep(1)
                    else:
                        raise e

            # Print the final AI Agent response to the terminal
            if response:
                print(f"\n🤖 Agent: {response.text}\n")
                print("-" * 65)
            else:
                print("\n❌ Service temporarily busy. Please try your prompt again.\n")

        # Handle clean exit when user presses Ctrl+C or closes terminal stream
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Chat session ended.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


# Standard Python entry point
if __name__ == "__main__":
    main()
