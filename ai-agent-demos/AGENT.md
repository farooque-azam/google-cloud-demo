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
