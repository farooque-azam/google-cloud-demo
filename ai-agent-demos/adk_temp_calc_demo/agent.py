import time
import socket
import platform
import datetime
from google.adk.agents.llm_agent import Agent

def get_current_time() -> str:
    """
    Tool: Returns the current server date, time, and exact server location/host details.
    
    When a user asks for live server time or host/location information, Gemini 
    triggers this function automatically.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tz = time.tzname[0] if time.tzname else "UTC"
    hostname = socket.gethostname()
    os_info = f"{platform.system()} {platform.release()}"
    location_desc = "Google Cloud Shell VM (us-central1 / GCP Infrastructure)"
    data = (
        f"Time: {now} {tz} | "
        f"Server Hostname: {hostname} | "
        f"OS Environment: {os_info} | "
        f"Location: {location_desc}"
    )
    return data

def calculate(expression: str) -> str:
    """
    Tool: Evaluates a mathematical expression safely and returns the numeric result.
    
    Args:
        expression (str): A mathematical expression string, e.g. "254 * 387 + 1024".
    """
    try:
        result_val = eval(expression, {"__builtins__": None}, {})
        return f"Calculation result for '{expression}': {result_val}"
    except Exception as e:
        return f"Error evaluating expression '{expression}': {str(e)}"

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful interactive AI Assistant.',
    instruction=(
        "You are a helpful interactive AI Assistant. "
        "You have access to tools for checking server time/location and calculating math. "
        "Always use available tools when precise, real-time, or system location information is requested. "
        "When presenting server time or location to the user, include the exact server hostname, OS, "
        "and location details returned by the tool. "
        "IMPORTANT: Do NOT use LaTeX math syntax or backslashes like \\( ... \\) or \\times in your output. "
        "Always write math expressions in plain, simple text (e.g., '3 + 4 * 5 = 23')."
    ),
    tools=[get_current_time, calculate]
)
