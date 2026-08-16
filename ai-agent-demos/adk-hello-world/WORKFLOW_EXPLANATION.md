# ADK 2.0 Workflow Explanation

This directory contains a "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. ADK 2.0 provides a structured, code-first approach to building multi-agent systems and graph-based workflows.

## How the ADK Workflow Operates

Unlike building an agent from scratch using the raw `google-genai` SDK, ADK abstracts away the boilerplate of maintaining chat loops, tool execution routing, and session state. 

Here is a step-by-step breakdown of how the ADK workflow operates in this project:

### 1. Application Initialization (`adk create`)
The `greeting_app` was generated using the ADK CLI command: `adk create greeting_app`. 
This creates a standardized folder structure:
*   **`.env`**: Stores sensitive credentials, specifically the `GOOGLE_API_KEY`.
*   **`agent.py`**: The core definition of your AI agent.
*   **`__init__.py`**: Marks the directory as a Python module.

### 2. Defining the Agent (`agent.py`)
In `agent.py`, we import the base `Agent` class from `google.adk.agents.llm_agent`.
We define our `root_agent` declaratively by passing parameters:
*   `model`: The specific LLM to use (e.g., `gemini-3.5-flash`).
*   `instruction`: The system prompt that dictates the agent's persona and behavior.

```python
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```
*Note: In more complex applications, you can attach `tools=[my_function]` directly to this definition.*

### 3. Execution via the ADK Runner
ADK uses a built-in runner engine to execute the agent. You don't write the `while True:` input loop yourself.

When you run the command:
```bash
adk run greeting_app "Hello! I am just starting out with ADK 2.0."
```
1.  **Context Setup**: The ADK Runner loads `greeting_app/agent.py` and initializes the `root_agent`.
2.  **State Management**: It automatically handles session tracking. Notice in the terminal output that a `Session ID: <UUID>` is generated. ADK manages the history of the conversation tied to this ID.
3.  **Model Invocation**: The Runner sends the user's query, along with the agent's instructions and conversation history, to the Gemini model.
4.  **Response Handling**: The model's response is streamed back to the terminal automatically.

### 4. Interactive Mode
If you run `adk run greeting_app` *without* a trailing prompt, the ADK Runner boots into an interactive terminal session, handling user input, history preservation, and error recovery automatically.

## Summary
The ADK 2.0 workflow focuses on **declarative agent design**. You define *what* the agent is and *what tools* it has in `agent.py`, and the ADK execution engine (via the CLI or API server) handles the complex routing, history, and state management required to make it run.

## Understanding the CLI and Virtual Environment

When working with ADK, you will often use the terminal. Here is a brief explanation of the environment setup:

### 1. The Virtual Environment (`source .venv/bin/activate`)
We installed the `google-adk` package into an isolated folder called `.venv`. 
When you run `source .venv/bin/activate`, you are telling your normal bash terminal to temporarily prioritize looking inside the `.venv/bin/` folder for commands before checking your system's global programs.

### 2. The ADK CLI
Installing `google-adk` automatically provided an executable command called `adk` inside that `.venv/bin/` folder. This is the **Command Line Interface (CLI)**.
*   The `adk` command is a Python script that loads the ADK source code (stored in `.venv/lib/python3.X/site-packages/google/adk/`).
*   You use the CLI to scaffold projects (`adk create`) and to launch the Runner (`adk run`).

By activating the environment, your terminal knows exactly where to find the `adk` command and the required source files to execute your agent!
