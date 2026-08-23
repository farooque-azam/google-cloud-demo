# Coordinator Agent Pattern

This directory demonstrates Pattern 5 from the AI Agent Design Patterns video: the **Coordinator Agent** (also known as the Router Pattern).

![Coordinator Agent Architecture](https://docs.cloud.google.com/static/architecture/images/choose-design-pattern-agentic-ai-system-coordinator.svg)

## Overview
The Coordinator Pattern acts as a "smart manager" that uses **hierarchical task decomposition**. Unlike a Sequential Agent which forces an "assembly line" in a fixed order, the Coordinator analyzes a user's request and dynamically decides which specialized sub-agent to delegate the task to (or if it should use multiple).

## Use Case: Trip Planning
In this example, we replicate a trip planning scenario:
1. **Trip Coordinator**: The primary LLM that analyzes the user's prompt.
2. **Food Agent**: A specialized worker agent containing the `find_restaurant` tool.
3. **Transportation Agent**: A specialized worker agent containing the `get_transit_directions` tool.

## Code Structure (ADK 2.0 Academic Implementation)
- `tools.py`: Contains our mock tools (`find_restaurant` and `get_transit_directions`).
- `agent.py`: Defines the agents. 
  - **Academic Note on ADK 2.0:** While the ADK does not have a dedicated `CoordinatorAgent` Python class, the framework natively supports this pattern using the standard `Agent` class. By passing the workers into the `sub_agents` array of the `trip_coordinator`, the ADK automatically injects a `transfer_to_agent` function tool into the coordinator's context. This allows the LLM to dynamically route the conversation to its sub-agents!

## How to Run
```bash
# Assuming you are in the ai-agent-demos directory
cd p5_coordinator
adk run .
```
You can prompt it with: "I'm starting at my house in downtown and I want to eat pizza." 
The Coordinator will dynamically route you to the food agent, and once complete, route you to the transport agent.

## Pros & Cons

### Pros
- **High Flexibility:** The workflow dynamically adapts. If a user only asks for directions (and already has food), the coordinator skips the food agent entirely.
- **Separation of Concerns:** Each worker agent has a single, focused toolset, preventing the main LLM from getting confused by too many tools.

### Cons
- **Higher Token Cost:** The LLM must "think" and use function calls (`transfer_to_agent`) just to move between tasks, using more tokens than a hardcoded sequence.
- **Potential for Routing Errors:** Since routing relies on the LLM's reasoning rather than a hardcoded Python script, a weak LLM might accidentally route to the wrong agent if the user's prompt is ambiguous.
