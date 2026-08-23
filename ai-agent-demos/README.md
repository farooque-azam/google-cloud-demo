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
Create a `.env` file inside the `ai-agent-demos/` directory to securely store your key.

```bash
cd ai-agent-demos
# (On Windows, you can just create a new text file and name it .env)
touch .env
```

Open the newly created `.env` file and add the following line, replacing the placeholder with your actual key:
```env
GOOGLE_API_KEY="your_copied_api_key_here"
```
*(Note: Do not commit your `.env` file to GitHub! It is already added to `.gitignore` to prevent accidental uploads).*

### 3. Create & Activate Virtual Environment
Before running the projects, you must create a Python virtual environment and activate it. This keeps the dependencies isolated to this project.

```bash
cd ai-agent-demos
python -m venv .venv

# Activate on Windows (PowerShell/CMD):
.\.venv\Scripts\activate

# Activate on Mac/Linux:
source .venv/bin/activate
```

### 4. Install Dependencies
With your virtual environment activated, install the required packages:

```bash
pip install "google-adk[ui]" "google-adk[eval]" google-genai python-multipart
```
*(Note: The `[ui]` extra and `python-multipart` are required for the Web interface. The `[eval]` extra is required if you want to run automated agent evaluations, as it installs data science libraries like pandas and rouge-score needed to measure agent performance).*

### 5. Running the Agents (CLI vs Web UI)
The Agent Development Kit (ADK) provides two main ways to interact with your agents:

1. **Terminal CLI (`adk run`)**: This is the fastest way to test your agent. Simply navigate to the project directory and execute `adk run .`. You can then interact with the agent directly in your command line.
2. **Web Interface (`adk web`)**: If you prefer a visual chat interface, you can launch a local web server by running `adk web --host 127.0.0.1 --allow_origins="*" .`. Once the server starts, it will provide a **web preview link** in the terminal. Click that link to open the graphical chat UI in your browser!

---

## 1. Single Agent Pattern (`p1_single`)
**Brief Intro:** A foundational "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. It demonstrates the basics of declarative agent design (matching Pattern #1) and uses a standard Python module package structure (`__init__.py` explicitly loads the agent).

**Run Instructions:**
```bash
# Terminal CLI (Assuming you are in the ai-agent-demos directory)
cd p1_single
adk run .

# Web UI
# Must be run from the ai-agent-demos directory
cd ../
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of the workflow and CLI commands, see: `p1_single/WORKFLOW_EXPLANATION.md`*

---

## 2. Single Agent with Tools (`p1_single_tools`)
**Brief Intro:** A more advanced ADK 2.0 agent that implements **custom tools (function calling)** to calculate mathematical expressions and retrieve real-time server information. It demonstrates the tool usage described in Pattern #1 with a lightweight "flat directory" structure.

**Run Instructions:**
```bash
# Terminal CLI (Assuming you are in the ai-agent-demos directory)
cd p1_single_tools
adk run .

# Web UI
# Must be run from the ai-agent-demos directory
cd ../
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of this project and the structural differences, see: `p1_single_tools/WORKFLOW_EXPLANATION.md`*

---

## 3. Sequential Agent Pattern (`p2_sequential`)
**Brief Intro:** This project demonstrates the **Sequential Agent** (Pattern #2) using ADK 2.0. It models a trip planning scenario where a **Food Agent** first selects a dining location, and its output is then passed to a **Transportation Agent** to determine the route.

**Run Instructions:**
```bash
# Terminal CLI (Assuming you are in the ai-agent-demos directory)
cd p2_sequential
adk run .

# Web UI
# Must be run from the ai-agent-demos directory
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of this project, see: `p2_sequential/WORKFLOW_EXPLANATION.md`*

---

## 4. Parallel Agent Pattern (`p3_parallel`)
**Brief Intro:** This project demonstrates the **Parallel Agent** (Pattern #3) using ADK 2.0. It models a research pipeline where a **News Researcher** and **Document Researcher** work simultaneously, followed by an **Aggregator Agent** that synthesizes their findings.

**Run Instructions:**
```bash
# Terminal CLI (Assuming you are in the ai-agent-demos directory)
cd p3_parallel
adk run .

# Web UI
# The Web UI must be run from the ai-agent-demos directory
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of this project, see: `p3_parallel/WORKFLOW_EXPLANATION.md`*

---

## 5. Coordinator Agent Pattern (`p5_coordinator`)
**Brief Intro:** This project demonstrates a **Coordinator Pattern** where a central agent manages the conversation and delegates sub-tasks to specialized worker agents based on the user's input.

**Run Instructions:**
```bash
# Terminal CLI (Assuming you are in the ai-agent-demos directory)
cd p5_coordinator
adk run .

# Web UI
# The Web UI must be run from the ai-agent-demos directory
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of this project, see: `p5_coordinator/WORKFLOW_EXPLANATION.md`*

---

## 6. GenAI SDK Demo (`genai_sdk_demo`)
**Brief Intro:** Unlike the previous two, this project is built using the raw **`google-genai` Python SDK** *without* the ADK framework. It demonstrates how to manually build an interactive chat loop, maintain conversation history, and register tools from scratch.

**Run Instructions:**
```bash
cd genai_sdk_demo
python hello_agent.py          # Run the basic one-off agent execution
python interactive_agent.py    # Run the continuous interactive chat loop
```
*📖 For a deep dive into the architecture, security guardrails, and sequence diagrams for this raw SDK approach, see: `genai_sdk_demo/AGENT_WORKFLOW_EXPLANATION.md`*
