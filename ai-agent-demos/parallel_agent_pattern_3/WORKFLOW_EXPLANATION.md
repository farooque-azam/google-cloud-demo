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
- `agent.py`: Uses ADK's `Workflow` API and `JoinNode`. The execution graph branches out from `START` to both researchers simultaneously, and then uses a `JoinNode` to block the `aggregator_agent` until both branches have completed successfully.

## How to Run

To test this agent in the terminal (CLI):
```bash
cd ~/ai-agent-demos
source .venv/bin/activate
cd parallel_agent_pattern_3
adk run . "Acme Corp"
```

To view the strict parallel execution graph in the browser:
```bash
cd ~/ai-agent-demos
source .venv/bin/activate
cd parallel_agent_pattern_3
adk web --host 0.0.0.0 --allow_origins="*" .
```

## Pros & Cons

### Pros
- **Reduced Latency:** Significant performance improvements for large tasks, as independent subtasks are executed at the exact same time rather than sequentially.
- **Modularity:** It is trivial to add a third or fourth researcher agent to the parallel pool without disrupting the existing ones.

### Cons
- **Aggregation Complexity:** If one of the parallel agents fails or hallucinates, the aggregator agent must be robust enough to handle partial or conflicting data.
- **Cost & Quotas:** Running multiple LLM agents concurrently consumes more tokens and can easily trigger API rate limits (HTTP 429) if not properly throttled.
