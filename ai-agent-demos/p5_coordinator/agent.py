from google.adk.agents import Agent, SequentialAgent
from .tools import find_restaurant, get_transit_directions

food_agent = Agent(
    name="food_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are a food finding agent.
- If the user greets you, politely ask what they would like to eat and where they are.
- If the user asks for food/restaurant recommendations, you MUST use the `find_restaurant` tool to search.
- Never make up restaurant names. Only use the names provided by your tool.""",
    tools=[find_restaurant]
)

transport_agent = Agent(
    name="transport_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are a transportation agent. 
- Wait until the food agent has provided a specific restaurant name.
- Once a restaurant is selected, use the `get_transit_directions` tool to find the route from the user's starting location.
- Do not provide generic transit directions. Always use the tool.""",
    tools=[get_transit_directions]
)

# Note: In ADK 2.0, a true Coordinator uses a standard `Agent` with `sub_agents`.
# The LLM acts as the router and dynamically invokes the correct sub-agent
# using its built-in `transfer_to_agent` function call.
root_agent = Agent(
    name="trip_coordinator",
    model="gemini-3.5-flash-lite",
    instruction="""You coordinate a trip. You act as a router.
- Analyze the user's request. 
- If they want food, transfer to the food_agent.
- If they have a restaurant and want directions, transfer to the transport_agent.
- Do not answer the question yourself, always delegate to the correct sub-agent.""",
    sub_agents=[food_agent, transport_agent]
)
