from google.adk.agents.llm_agent import Agent

# In ADK 2.0, the Agent object is defined declaratively. 
# We do not write execution loops (like 'while True:') here. 
# The ADK Runner (invoked via `adk run`) handles the session, memory, and execution flow.
root_agent = Agent(
    # Specify the underlying LLM model to power this agent.
    model='gemini-3.5-flash',
    
    # Internal name for the agent (useful when building multi-agent workflows).
    name='root_agent',
    
    # A brief description of what this agent does.
    description='A helpful assistant for user questions.',
    
    # System instructions that dictate the agent's persona and behavior.
    instruction='Answer user questions to the best of your knowledge',
)
