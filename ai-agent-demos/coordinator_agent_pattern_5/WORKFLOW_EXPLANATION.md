# Coordinator Agent Pattern

This directory demonstrates Pattern 5 from the AI Agent Design Patterns video: the **Coordinator Agent**.

n![Coordinator Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-coordinator.svg)

## Overview
The Coordinator Pattern uses an "assembly line" approach where specialized agents work in a fixed, predictable order. The output of one agent serves as the input for the next. This provides high reliability and control.

## Use Case: Trip Planning
In this example, we replicate the video's trip planning scenario:
1. **Food Agent**: Executes first to search for a dining option based on the user's initial input (e.g. location and food preference).
2. **Transportation Agent**: Executes second, taking the dining location determined by the first agent, and provides travel directions from the start location.

## Code Structure
- `tools.py`: Contains our mock tools (`find_restaurant` and `get_transit_directions`).
- `agent.py`: Defines the two specialized agents and connects them using ADK's `sequential` workflow function.

## How to Run
```bash
cd ~/ai-agent-demos/coordinator_agent_pattern_5
adk run .
```
You can prompt it with: "I'm starting at my house in downtown and I want to eat pizza."

## Pros & Cons

### Pros
- **High Reliability:** Ensures tasks are executed in a strict, predictable order.
- **Separation of Concerns:** Each agent has a single, focused instruction (e.g., finding food vs. finding transit), making them easier to test and maintain.

### Cons
- **Less Flexible:** Cannot dynamically adapt the workflow if the user's request doesn't perfectly fit the predefined sequence.
- **Performance Trade-off (Context Caching Invalidated):** When ADK transitions execution from the first agent (e.g., `food_agent`) to the second agent (e.g., `transport_agent`), the underlying system prompt sent to the LLM changes. Because the prompt is no longer static, it causes a **context cache miss**. This results in higher latency and token costs compared to a single-agent architecture that can reuse a cached prompt across multiple turns.
