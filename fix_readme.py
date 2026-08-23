import os

readme_path = "ai-agent-demos/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

bad_text = """### 1. Single Agent Pattern
*A basic "Hello World" application.*
```bash
# 1. To run the agent directly in your terminal:
cd p1_single
adk run greeting_app

# 2. To run the Web UI, you MUST run it from the parent folder (p1_single)
# so the UI dashboard can detect 'greeting_app' as a selectable agent in its dropdown:
**Run Instructions:**
```bash
# Terminal CLI
cd p2_sequential"""

good_text = """## 1. Single Agent Pattern (`p1_single`)
**Brief Intro:** A foundational "Hello World" application built using Google's **Agent Development Kit (ADK) 2.0**. It demonstrates the basics of declarative agent design (matching Pattern #1) and uses a standard Python module package structure (`__init__.py` explicitly loads the agent).

**Run Instructions:**
```bash
# 1. To run the agent directly in your terminal:
cd p1_single
adk run greeting_app

# 2. To run the Web UI, you MUST run it from the parent folder (p1_single)
# so the UI dashboard can detect 'greeting_app' as a selectable agent in its dropdown:
cd p1_single
adk web --host 127.0.0.1 --allow_origins="*" .
```
*📖 For a detailed explanation of the workflow and CLI commands, see: `p1_single/WORKFLOW_EXPLANATION.md`*

---

## 2. Single Agent with Tools (`p1_single_tools`)
**Brief Intro:** A more advanced ADK 2.0 agent that implements **custom tools (function calling)** to calculate mathematical expressions and retrieve real-time server information. It demonstrates the tool usage described in Pattern #1 with a lightweight "flat directory" structure.

**Run Instructions:**
```bash
# Terminal CLI
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
# Terminal CLI
cd p2_sequential"""

content = content.replace(bad_text, good_text)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
print("done")
