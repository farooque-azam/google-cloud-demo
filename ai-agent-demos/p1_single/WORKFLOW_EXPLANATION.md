# ADK 2.0 Workflow Explanation

This directory contains a "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. ADK 2.0 provides a structured, code-first approach to building multi-agent systems and graph-based workflows.
n![Single Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-single-agent.svg)


## How the ADK Workflow Operates

Unlike building an agent from scratch using the raw `google-genai` SDK, ADK abstracts away the boilerplate of maintaining chat loops, tool execution routing, and session state. 

Here is a step-by-step breakdown of how the ADK workflow operates in this project:

### 1. Application Initialization (`adk create`)
The `p1_single` was generated using the ADK CLI command: `adk create p1_single`. 
This creates a standardized folder structure:
*   **`.env`**: Stores sensitive credentials, specifically the `GOOGLE_API_KEY`.
*   **`agent.py`**: The core definition of your AI agent.
*   **`__init__.py`**: Marks the directory as a Python module.

### 2. Defining the Agent (`agent.py`)
In `agent.py`, we import the base `Agent` class from `google.adk.agents.llm_agent`.
We define our `root_agent` declaratively by passing parameters:
*   `model`: The specific LLM to use (e.g., `gemini-3.5-flash-lite`).
*   `instruction`: The system prompt that dictates the agent's persona and behavior.

```python
root_agent = Agent(
    model='gemini-3.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```
*Note: In more complex applications, you can attach `tools=[my_function]` directly to this definition.*

### 3. Execution via the ADK Runner
ADK uses a built-in runner engine to execute the agent. You don't write the `while True:` input loop yourself.

Assuming your terminal is in the parent directory (`~/ai-agent-demos/`), you can start the agent like this:
```bash
adk run p1_single
```
*(If you are already inside the `p1_single` folder, you would use `adk run .` instead).*

1.  **Context Setup**: The ADK Runner loads `agent.py` and initializes the `root_agent`.
2.  **State Management**: It automatically handles session tracking. Notice in the terminal output that a `Session ID: <UUID>` is generated. ADK manages the history of the conversation tied to this ID.
3.  **Model Invocation**: The Runner sends the user's query, along with the agent's instructions and conversation history, to the Gemini model.
4.  **Response Handling**: The model's response is streamed back to the terminal automatically.

### 4. Interactive Mode
If you run `adk run p1_single` (or `adk run .` if you are already inside the folder) *without* a trailing prompt, the ADK Runner boots into an interactive terminal session, handling user input, history preservation, and error recovery automatically.

## Summary
The ADK 2.0 workflow focuses on **declarative agent design**. You define *what* the agent is and *what tools* it has in `agent.py`, and the ADK execution engine (via the CLI or API server) handles the complex routing, history, and state management required to make it run.

## Understanding the CLI and Virtual Environment

When working with ADK, you will often use the terminal. Here is a brief explanation of the environment setup:

### 1. The Virtual Environment (`python -m venv .venv`)
We installed the `google-adk` package into an isolated folder called `.venv`. 
When you activate it (e.g. `.\.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Linux/Mac), you are telling your terminal to temporarily prioritize looking inside the `.venv` folder for commands before checking your system's global programs.

### 2. The ADK CLI
Installing `google-adk` automatically provided an executable command called `adk` inside that `.venv/Scripts/` folder (or `.venv/bin/` on Linux). This is the **Command Line Interface (CLI)**.
*   The `adk` command is a Python script that loads the ADK source code.
*   You use the CLI to scaffold projects (`adk create p1_single`) and to launch the Runner. For example, executing `adk run p1_single` tells the CLI to look for a module named `p1_single` and execute its root agent.

By activating the environment, your terminal knows exactly where to find the `adk` command and the required source files to execute your agent!

## Python Package Initialization (`__init__.py`)

When you generated the app, ADK created an `__init__.py` file containing a relative import:
```python
from . import agent
```

### What does this syntax mean?
*   `from`: Indicates we are importing something from a specific location.
*   `.` (dot): Means **"the current directory"** (the same folder where `__init__.py` lives).
*   `import agent`: Tells Python to look for `agent.py` in that directory and load it.

### Why is this necessary?
In Python, any folder containing an `__init__.py` file is treated as a **module** (or package). 
If the file were empty, importing the `p1_single` folder wouldn't automatically load the files inside it. By including `from . import agent`, you ensure that whenever the ADK Runner imports the `p1_single` module, it automatically executes and loads your `root_agent` configuration from `agent.py`.

## Running the ADK Web UI

ADK also provides a web-based user interface to interact with your agent visually, track traces, and view conversation history.

### 1. Installations Needed
To use the Web UI, ensure your virtual environment is activated and you have installed the `[ui]` extras for the ADK package.

```bash
# Ensure your virtual environment is active (Windows)
.\.venv\Scripts\activate

# Install the UI extras (this installs dependencies like FastAPI, Uvicorn, and form parsers)
pip install "google-adk[ui]" python-multipart
```

### 2. Invoking the Web UI
To run the Web UI, you must use the `adk web` command and point it to the directory containing your agent (e.g., `p1_single`). 

Assuming you are in the parent directory (`~/ai-agent-demos/`), run:

```bash
adk web --host 127.0.0.1 --allow_origins="*" .
```

*Note: You MUST run the web server from this parent directory. The web UI acts as a dashboard that scans the current directory for agent folders. If you run it from inside `p1_single`, it will not find any sub-agents and will show a "No agents found" error.*

**Understanding the Command Flags:**
When running this server on a local machine, simply running `adk web p1_single` without flags is usually sufficient (it defaults to `127.0.0.1`). However, if you were running this in a remote Google Cloud Shell environment, you would need to bypass network proxy restrictions by using `--host 0.0.0.0` and `--allow_origins="*"`.
*   `--host 127.0.0.1`: Explicitly tells the server to listen only to internal traffic on `localhost`, which is the safest option for local development and avoids firewall warnings.

Once the command is running, you can open your browser to `http://127.0.0.1:8000` to view the UI.
