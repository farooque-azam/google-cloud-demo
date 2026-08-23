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

# Note: Even though we use SequentialAgent under the hood, the conversational
# back-and-forth makes this act conceptually as a Coordinator pattern.
root_agent = SequentialAgent(
    name="trip_coordinator",
    description="You coordinate a trip. You delegate to the food agent, then the transport agent.",
    sub_agents=[food_agent, transport_agent]
)
