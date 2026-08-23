# ADK Temperature & Calculator Demo

This directory contains an interactive agent built with ADK 2.0 that features custom Python tools (function calling) for calculating mathematical expressions and retrieving the current server time/location.
n![Single Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-single-agent.svg)


## Running the Agent

This agent uses the ADK 2.0 CLI. Ensure your virtual environment is active before running these commands.

### 1. Terminal (Interactive CLI)

To interact with the agent directly in your terminal, use the `adk run` command. The `.` tells ADK to run the agent in the current directory.

```bash
# Assuming you are starting from the ai-agent-demos directory
cd p1_single_tools
adk run .
```
*(Once running, try asking: "What time is it?" or "Calculate 45 * 12")*

### 2. Web UI

To interact with the agent using the visual Web UI, use the `adk web` command.

```bash
# The Web UI must be run from the parent ai-agent-demos directory
adk web --host 127.0.0.1 --allow_origins="*" .
```

*   `--host 127.0.0.1`: Explicitly tells the server to listen only to localhost (avoids Windows firewall popups).
*   `--allow_origins="*"`: Disables CORS restrictions.
*   `.`: Points the server to the current directory.

*(Once the server starts, open http://127.0.0.1:8000 in your browser)*

---

## Project Structure: Flat Directory vs. Module Package

You may notice that this project is structured differently from the `adk-hello-world` example. ADK 2.0 supports two primary ways of organizing your agent files:

### Approach 1: The Module Package Structure (Used in `adk-hello-world`)
In the `adk-hello-world` project, the agent was placed inside a subfolder (`greeting_app`), and its `__init__.py` file contained an explicit import:
```python
from . import agent
```
* **Why do this?** This structure treats the agent as a formal Python package. When you run `adk run greeting_app`, Python loads the `greeting_app` module, the `__init__.py` automatically executes, and it explicitly loads your `agent.py`. This is best for larger, complex applications where you want strict control over how imports and files are loaded.

### Approach 2: The Flat Directory Structure (Used here in `p1_single_tools`)
In this project, everything sits in a single, flat directory (`p1_single_tools`). If you look at the `__init__.py` file here, it is empty (just a comment). 
* **Why do this?** ADK is smart enough to scan the target directory. When you run `adk run .`, even without explicit instructions in `__init__.py`, ADK automatically looks for a file named `agent.py` (or a `root_agent.yaml`) and loads it. 
* This is a faster, more lightweight way to structure simple demos and single-file agents without needing complex Python package plumbing!
