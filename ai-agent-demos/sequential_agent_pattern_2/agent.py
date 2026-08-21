from google.adk.agents import Agent, SequentialAgent
from tools import find_restaurant, get_transit_directions

food_agent = Agent(
    name="food_agent",
    model="gemini-3.5-flash-lite",
    instruction="You are a food finding agent. First, based on the user's request, use your tool to find a restaurant.",
    tools=[find_restaurant]
)

transport_agent = Agent(
    name="transport_agent",
    model="gemini-3.5-flash-lite",
    instruction="You are a transportation agent. Once the food agent has selected a restaurant, use your tool to find transit directions to it.",
    tools=[get_transit_directions]
)

root_agent = SequentialAgent(
    name="trip_planner",
    description="You are a trip planner. First find a restaurant, then provide directions.",
    sub_agents=[food_agent, transport_agent]
)
