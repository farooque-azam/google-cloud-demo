# Parallel Agent Pattern

![Parallel Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-parallel.svg)

This directory demonstrates Pattern 3 from the AI Agent Design Patterns video: the **Parallel Agent**.

## Overview
The Parallel Agent pattern dispatches tasks to multiple specialized agents to be executed concurrently. This is highly efficient for reducing latency when subtasks are independent of one another. Once all parallel tasks are complete, an aggregator agent synthesizes the results.

## Use Case: Multi-source Researcher
In this example, we implement a concurrent research pipeline:
1. **News Researcher**: Searches the web for recent news about a given topic.
2. **Document Researcher**: Searches internal databases for company policies about the same topic.
3. **Aggregator Agent**: Waits for both researchers to finish, then synthesizes their independent findings into a single executive summary.

## Update: API Rate Limits & Mock Tools
Due to strict free-tier rate limits on the Gemini API (`429 RESOURCE_EXHAUSTED`), testing parallel LLM calls concurrently can easily blow through API quotas. To ensure the demo works reliably, this pattern uses **mock tools** (`search_news` and `search_database`) that return hardcoded data instead of live search results. Be aware that queries for real-world events (e.g. "Iran war") will return the mock company data.

## Code Structure
- `tools.py`: Contains our mock tools (`search_news`, `search_database`).
- `agent.py`: Uses ADK's `ParallelAgent` and `SequentialAgent` classes. The two researchers are bundled into a `ParallelAgent` so they execute simultaneously. That block is then chained sequentially with the `aggregator_agent` so the aggregator waits for both to finish before synthesizing the results.

## How to Run

To test this agent in the terminal (CLI):
```bash
# Assuming you are in the ai-agent-demos directory with your venv activated
cd p3_parallel

# Option 1: Provide the prompt directly to kick off the research immediately
adk run . "Acme Corp"

# Option 2: Run it interactively and type your topic when asked
adk run .
```

To view the strict parallel execution graph in the browser:
```bash
# The Web UI must be run from the parent ai-agent-demos directory
# so it can detect this module in the dropdown
adk web --host 127.0.0.1 --allow_origins="*" .
```

## Pros & Cons

### Pros
- **Reduced Latency:** Significant performance improvements for large tasks, as independent subtasks are executed at the exact same time rather than sequentially.
- **Modularity:** It is trivial to add a third or fourth researcher agent to the parallel pool without disrupting the existing ones.

### Cons
- **Aggregation Complexity:** If one of the parallel agents fails or hallucinates, the aggregator agent must be robust enough to handle partial or conflicting data.
- **Cost & Quotas:** Running multiple LLM agents concurrently consumes more tokens and can easily trigger API rate limits (HTTP 429) if not properly throttled.
