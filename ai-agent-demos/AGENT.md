# Project Structure & Rules

This project serves as a monorepo for all AI Agent demonstrations. To keep the project clean and maintainable, please adhere to the following constraints:

## 1. Shared Virtual Environment
- **DO NOT** create a `.venv` or `venv` folder inside any sub-project directories.
- There is a single, shared Python virtual environment located at the root of the project: `ai-agent-demos/.venv`.
- All sub-projects must use this shared virtual environment. 
- When adding new dependencies for a sub-project, install them into the root `.venv`.
- **Python Version Requirement:** The ADK 2.0 framework strictly requires Python 3.10 or higher. When setting up the environment, students MUST ensure they use Python 3.11. On Windows with multiple versions installed, this can be done via `py -3.11 -m venv .venv`.

## 2. Shared Environment Variables
- **DO NOT** create `.env` files inside sub-project directories.
- There is a single, shared `.env` file located at the root of the project: `ai-agent-demos/.env`.
- This file contains all API keys (e.g., `GOOGLE_API_KEY`, `GEMINI_API_KEY`) and configuration settings.
- All scripts in sub-projects should be configured to locate and load this root `.env` file (e.g., using `python-dotenv`'s `find_dotenv()` function or by ensuring scripts are run from the root directory).

## 3. ADK Entry Points
- When creating ADK 2.0 projects, the top-level agent instantiated in your Python file MUST be exactly named `root_agent`. The ADK CLI (`adk run`) looks for this specific variable name by default (e.g., `root_agent = Agent(...)` or `root_agent = SequentialAgent(...)`).

## 4. Sub-Project Documentation & Naming
- **Sequential Naming**: Every new project folder must be prefixed with a sequence number that corresponds to its order in the main `README.md` (e.g., `single_agent_pattern_1`, `sequential_agent_pattern_2`).
- **Local Explanation**: Create a dedicated explanation markdown file (e.g., `WORKFLOW_EXPLANATION.md`) inside every new project folder detailing how it works and how to run it.
- **Main README**: Always add a brief summary and run instructions for the new project to the main root `README.md` file, ensuring the numbering stays consistent.

## 5. Testing Terminology
- **End-to-End (E2E) Execution:** Whenever the user asks to "test" the project or code, it strictly means performing an **End-to-End Test** (or full execution test). This requires actually running the application (for instance, executing `adk run .` with a test prompt via CLI, or running an integration script) to verify that the entire workflow succeeds without runtime errors, rather than merely checking syntax or verifying Python imports.

## 6. .gitignore Rules
- **DO NOT** create `.gitignore` files inside individual sub-project directories.
- All `.gitignore` rules (like ignoring `*.evalset.json` files, environments, or caches) MUST be consolidated into the single parent `.gitignore` file located at the root of `ai-agent-demos/`.

## 7. Architecture & Design Patterns
- The foundational design patterns and terminology for this repository are based on the official [Google Cloud Architecture Guide: Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system).
- When creating documentation for new patterns, always reference the corresponding architecture from this guide and embed the official SVG diagrams where applicable.

## 8. Google Cloud Configuration
- **Project Name:** Gemini Project
- **Project ID:** gen-lang-client-0441613979
- **Billing Account:** 01C43C-BA4B7C-50E6EC
- **Default Region:** us-central1 (Eligible for Free Tier)
