# Sequential Agent Pattern

This directory demonstrates Pattern 2 from the AI Agent Design Patterns video: the **Sequential Agent**.

## Overview
The Sequential Pattern uses an "assembly line" approach where specialized agents work in a fixed, predictable order. The output of one agent serves as the input for the next. This provides high reliability and control.

## Use Case: Trip Planning
In this example, we replicate the video's trip planning scenario:
1. **Food Agent**: Executes first to search for a dining option based on the user's initial input (e.g. location and food preference).
2. **Transportation Agent**: Executes second, taking the dining location determined by the first agent, and provides travel directions from the start location.

## Code Structure
- `tools.py`: Contains our mock tools (`find_restaurant` and `get_transit_directions`).
- `agent.py`: Defines the two specialized agents and connects them using ADK's `sequential` workflow function.

## How to Run
```bash
cd ~/ai-agent-demos/sequential_agent_pattern_2
adk run .
```
You can prompt it with: "I'm starting at my house in downtown and I want to eat pizza."
