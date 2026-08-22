from google.adk.agents import Agent
from google.adk.workflow import Workflow, START, JoinNode
from .tools import search_news, search_database

news_agent = Agent(
    name="news_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are the News Researcher. 
- You MUST use the `search_news` tool to find recent news about the user's topic.
- Do NOT ask clarifying questions. Summarize the news result concisely.""",
    tools=[search_news]
)

doc_agent = Agent(
    name="doc_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are the Document Researcher. 
- You MUST use the `search_database` tool to find internal docs about the user's topic.
- Do NOT ask clarifying questions. Summarize the internal doc result concisely.""",
    tools=[search_database]
)

aggregator_agent = Agent(
    name="aggregator_agent",
    model="gemini-3.5-flash-lite",
    instruction="""You are the Aggregator.
- Review the summaries provided by the News Researcher and Document Researcher.
- Combine them into a single, cohesive, final executive summary for the user."""
)

# Join node to wait for both researchers to finish
join_node = JoinNode(name="wait_for_researchers")

root_agent = Workflow(
    name="parallel_researcher",
    description="Searches news and docs in parallel, then synthesizes.",
    edges=[
        (START, news_agent),
        (START, doc_agent),
        (news_agent, join_node),
        (doc_agent, join_node),
        (join_node, aggregator_agent)
    ]
)
