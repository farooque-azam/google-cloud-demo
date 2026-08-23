# Sequential Agent Pattern

![Sequential Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-sequential.svg)

This directory demonstrates Pattern 2 from the AI Agent Design Patterns video: the **Sequential Agent**.

## Overview
The Sequential Pattern uses an "assembly line" approach where specialized agents or nodes work in a fixed, predictable order. The output of one agent serves as the input for the next, providing high reliability and control.

## Use Case: Trip Planning
In this example, we replicate the video's trip planning scenario. This project implements the sequential flow by chaining two LLM agents using ADK's native `SequentialAgent` class:
1. **Food Agent**: Executes first, takes the user's input, and searches for a dining option.
2. **Transportation Agent**: Executes second, reading the selected restaurant, gets directions, and returns the final combined response to the user.

## Code Structure
- `tools.py`: Contains our mock tools (`find_restaurant`, `get_transit_directions`).
- `agent.py`: Defines the two individual agents and strictly chains them together in a linear sequence using `google.adk.agents.SequentialAgent`.

## How to Run

To test this agent in the terminal (CLI):
```bash
# Assuming you are in the ai-agent-demos directory with your venv activated
cd p2_sequential

# Option 1: Provide the prompt directly to kick off the planner immediately
adk run . "I want to eat pizza give me pizza shop"

# Option 2: Run it interactively and type your request when asked
adk run .
```

To view the strict sequential graph visually, launch the ADK Web UI:
```bash
# The Web UI must be run from the parent ai-agent-demos directory
# so it can detect this module in the dropdown
adk web --host 127.0.0.1 --allow_origins="*" .
```
*(Open http://127.0.0.1:8000 in your browser once the server starts).*

## Pros & Cons

### Pros
- **High Reliability:** Ensures tasks are executed in a strict, predictable order.
- **Separation of Concerns:** Each agent has a single, focused instruction (e.g., finding food vs. finding transit), making them easier to test and maintain.

### Cons
- **Less Flexible:** Cannot dynamically adapt the workflow if the user's request doesn't perfectly fit the predefined sequence.
- **Performance Trade-off (Context Caching Invalidated):** When ADK transitions execution from the first agent (e.g., `food_agent`) to the second agent (e.g., `transport_agent`), the underlying system prompt sent to the LLM changes. Because the prompt is no longer static, it causes a **context cache miss**. This results in higher latency and token costs compared to a single-agent architecture that can reuse a cached prompt across multiple turns.
