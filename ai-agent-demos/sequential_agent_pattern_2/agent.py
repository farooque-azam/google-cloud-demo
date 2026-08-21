from google.adk.agents import Agent, SequentialAgent
from .tools import find_restaurant, get_transit_directions

food_agent = Agent(
    name="food_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are a food finding agent. 
- You MUST use the `find_restaurant` tool to search for a restaurant based on the user's initial prompt.
- Do NOT ask the user any clarifying questions. Use your best judgment to pick a location and food type if they are missing.
- Never make up restaurant names. Only use the names provided by your tool.""",
    tools=[find_restaurant]
)

transport_agent = Agent(
    name="transport_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are a transportation agent. 
- You MUST use the `get_transit_directions` tool to find the route to the restaurant selected by the food agent.
- Do not provide generic transit directions. Always use the tool.""",
    tools=[get_transit_directions]
)

root_agent = SequentialAgent(
    name="trip_planner",
    description="You are a trip planner. First find a restaurant, then provide directions.",
    sub_agents=[food_agent, transport_agent]
)
