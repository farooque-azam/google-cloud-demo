# AI Agent Demos Overview

Welcome to the **AI Agent Demos** repository! This workspace contains three distinct subprojects that demonstrate different methods of building AI agents using Google's tools. 

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

### 3. Activate Virtual Environment
Before running any of the projects, ensure you have your virtual environment activated from the root directory:
```bash
cd ~/ai-agent-demos
source .venv/bin/activate
```

---

## 1. ADK Hello World (`adk-hello-world`)
**Brief Intro:** A foundational "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. It demonstrates the basics of declarative agent design and uses a standard Python module package structure (`__init__.py` explicitly loads the agent).

**Run Instructions:**
```bash
cd adk-hello-world/greeting_app
adk run .                                          # Run in Terminal
adk web --host 0.0.0.0 --allow_origins="*" .       # Run Web UI in Cloud Shell
```
*📖 For a detailed explanation of the workflow and CLI commands, see: `adk-hello-world/WORKFLOW_EXPLANATION.md`*

---

## 2. ADK Temperature & Calculator Demo (`adk_temp_calc_demo`)
**Brief Intro:** A more advanced ADK 2.0 agent that implements **custom tools (function calling)** to calculate mathematical expressions and retrieve real-time server information. It demonstrates a lightweight "flat directory" structure where the ADK runner automatically scans for the agent file.

**Run Instructions:**
```bash
cd adk_temp_calc_demo
adk run .                                          # Run in Terminal
adk web --host 0.0.0.0 --allow_origins="*" .       # Run Web UI in Cloud Shell
```
*📖 For a detailed explanation of this project and the structural differences, see: `adk_temp_calc_demo/WORKFLOW_EXPLANATION.md`*

---

## 3. Single Agent Demo (`single-agent-demo`)
**Brief Intro:** Unlike the previous two, this project is built using the raw **`google-genai` Python SDK** *without* the ADK framework. It demonstrates how to manually build an interactive chat loop, maintain conversation history, and register tools from scratch.

**Run Instructions:**
```bash
cd single-agent-demo
python hello_agent.py          # Run the basic one-off agent execution
python interactive_agent.py    # Run the continuous interactive chat loop
```
*📖 For a deep dive into the architecture, security guardrails, and sequence diagrams for this raw SDK approach, see: `single-agent-demo/AGENT_WORKFLOW_EXPLANATION.md`*
