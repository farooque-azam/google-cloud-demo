# AI Agent Demos Overview

Welcome to the **AI Agent Demos** repository! This workspace contains three distinct subprojects that demonstrate different methods of building AI agents using Google's tools. 

## Reference Materials
These examples are inspired by the following Google Cloud Tech tutorials. Here is a summary of the agent design patterns discussed in these videos:

### [Video 1: AI agent design patterns](https://youtu.be/GDm_uH6VxPY)
This video provides an introductory guide to **AI agent design patterns** using the *Agent Development Kit (ADK)*. It outlines three core architectures for building AI-driven systems:

1. **Single Agent (1:01 - 3:05):** The most fundamental pattern. It is simple to implement and effective for straightforward tasks using tools, but it can become unreliable and harder to control as tasks grow more complex.
2. **Sequential Agent (3:05 - 5:21):** An "assembly line" approach where specialized agents work in a fixed, predictable order. The output of one agent serves as the input for the next, providing high reliability and control, though it is less flexible for dynamic scenarios.
3. **Parallel Agent (5:21 - 7:08):** This pattern involves running multiple specialized agents concurrently to perform independent subtasks. It is highly efficient for reducing latency, often followed by a final aggregator agent to synthesize the results.

### [Video 2: 3 Advanced AI agent design patterns](https://youtu.be/89KKm_a4M7A)
This video explores **three advanced AI agent design patterns** for creating dynamic, multi-agent systems using the *Agent Development Kit (ADK)*. These patterns help developers build systems that can iterate, self-correct, and dynamically route tasks.

4. **The Loop Pattern (Review & Critique):** (1:09 - 3:08)
This pattern is ideal for tasks requiring strict constraints (e.g., ensuring a hotel is within 30 minutes of an event). It uses a **generator agent** to create content and a **critique agent** to evaluate it against specific conditions, creating an iterative refinement loop until the requirement is met.

5. **The Coordinator (Router) Pattern:** (3:08 - 5:33)
This acts as a "smart manager" that uses **hierarchical task decomposition**. The coordinator analyzes a user request and delegates specific subtasks to specialized sub-agents (such as a *food and transportation agent* or *nearby places agent*), allowing the system to handle complex, multi-step problems.

6. **The Agent as Tool Pattern:** (5:33 - 6:49)
Similar to the coordinator, this pattern uses a primary agent, but treats sub-agents as **stateless tools**. Instead of delegating full control, the primary agent invokes sub-agents to perform specific functions and retains full control over the system state, acting like a craftsman picking up specific tools for each part of a job.

## Getting Started & Setup

If you have forked this repository to run the demos yourself, you must first set up your environment and obtain a free API key to authenticate with the Gemini models.

### 1. Get a Gemini API Key
1. Go to **[Google AI Studio](https://aistudio.google.com/)** and sign in with your Google account.
2. Click on **"Get API key"** in the left navigation menu.
3. Click **"Create API key"** and copy the generated key.

### 2. Configure Your Environment
Create a `.env` file in the root `ai-agent-demos/` directory to securely store your key.

```bash
cd ~/ai-agent-demos
touch .env
```

Open the newly created `.env` file and add the following line, replacing the placeholder with your actual key:
```env
GOOGLE_API_KEY="your_copied_api_key_here"
```
*(Note: Do not commit your `.env` file to GitHub! It is already added to `.gitignore` to prevent accidental uploads).*

### 3. Install Dependencies
Before running the projects, you must install the required Python packages into your virtual environment.

```bash
cd ~/ai-agent-demos
source .venv/bin/activate
pip install "google-adk[ui]" google-genai
```

*(Note: The `[ui]` extra is required to run the ADK Web interface).*

### 4. Activate Virtual Environment
Before running any of the projects, ensure you have your virtual environment activated from the root directory:
```bash
cd ~/ai-agent-demos
source .venv/bin/activate
```

### 5. Running the Agents (CLI vs Web UI)
The Agent Development Kit (ADK) provides two main ways to interact with your agents:

1. **Terminal CLI (`adk run`)**: This is the fastest way to test your agent. Simply navigate to the project directory and execute `adk run .`. You can then interact with the agent directly in your command line.
2. **Web Interface (`adk web`)**: If you prefer a visual chat interface, you can launch a local web server by running `adk web --host 0.0.0.0 --allow_origins="*" .`. Once the server starts, it will provide a **web preview link** in the terminal. Click that link to open the graphical chat UI in your browser!

---

## 1. Single Agent Pattern (`single_agent_pattern_1`)
**Brief Intro:** A foundational "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. It demonstrates the basics of declarative agent design (matching Pattern #1) and uses a standard Python module package structure (`__init__.py` explicitly loads the agent).

**Run Instructions:**
```bash
cd single_agent_pattern_1/greeting_app
adk run .                                          # Run in Terminal
adk web --host 0.0.0.0 --allow_origins="*" .       # Run Web UI in Cloud Shell
```
*📖 For a detailed explanation of the workflow and CLI commands, see: `single_agent_pattern_1/WORKFLOW_EXPLANATION.md`*

---

## 2. Single Agent with Tools (`single_agent_with_tools_1`)
**Brief Intro:** A more advanced ADK 2.0 agent that implements **custom tools (function calling)** to calculate mathematical expressions and retrieve real-time server information. It demonstrates the tool usage described in Pattern #1 with a lightweight "flat directory" structure.

**Run Instructions:**
```bash
cd single_agent_with_tools_1
adk run .                                          # Run in Terminal
adk web --host 0.0.0.0 --allow_origins="*" .       # Run Web UI in Cloud Shell
```
*📖 For a detailed explanation of this project and the structural differences, see: `single_agent_with_tools_1/WORKFLOW_EXPLANATION.md`*

---

## 3. Sequential Agent Pattern (`sequential_agent_pattern_2`)
**Brief Intro:** This project demonstrates the **Sequential Agent** (Pattern #2) using ADK 2.0. It models a trip planning scenario where a **Food Agent** first selects a dining location, and its output is then passed to a **Transportation Agent** to determine the route.

**Run Instructions:**
```bash
cd sequential_agent_pattern_2
adk run .                                          # Run in Terminal
adk web --host 0.0.0.0 --allow_origins="*" .       # Run Web UI in Cloud Shell
```
*📖 For a detailed explanation of this project, see: `sequential_agent_pattern_2/WORKFLOW_EXPLANATION.md`*

---

## 4. GenAI SDK Demo (`genai_sdk_demo`)
**Brief Intro:** Unlike the previous two, this project is built using the raw **`google-genai` Python SDK** *without* the ADK framework. It demonstrates how to manually build an interactive chat loop, maintain conversation history, and register tools from scratch.

**Run Instructions:**
```bash
cd genai_sdk_demo
python hello_agent.py          # Run the basic one-off agent execution
python interactive_agent.py    # Run the continuous interactive chat loop
```
*📖 For a deep dive into the architecture, security guardrails, and sequence diagrams for this raw SDK approach, see: `genai_sdk_demo/AGENT_WORKFLOW_EXPLANATION.md`*
