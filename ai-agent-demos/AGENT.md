# Project Structure & Rules

This project serves as a monorepo for all AI Agent demonstrations. To keep the project clean and maintainable, please adhere to the following constraints:

## 1. Shared Virtual Environment
- **DO NOT** create a `.venv` or `venv` folder inside any sub-project directories.
- There is a single, shared Python virtual environment located at the root of the project: `ai-agent-demos/.venv`.
- All sub-projects must use this shared virtual environment. 
- When adding new dependencies for a sub-project, install them into the root `.venv`.

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
