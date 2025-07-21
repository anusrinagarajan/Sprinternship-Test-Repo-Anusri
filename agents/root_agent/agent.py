from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from big_query.agent import big_query_subagent
from compute_engine.agent import compute_engine_subagent
from cloud_storage.agent import cloud_storage_subagent
from cloud_sql.agent import cloud_sql_subagent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description=(
        "An agent that routes questions about various google cloud services to the specialized subagents."
        "This agent does not answer questions directly."
    ),
    instruction=(
        "You are a routing agent for Google Cloud services. Your main job is to "
        "identify the specific Google Cloud service mentioned in the user's question "
        "and pass the question to the appropriate sub-agent. Do not try to answer "
        "the question yourself. If the question doesn't clearly relate to one "
        "of the specific Google Cloud services you know about, respond that you "
        "cannot answer the question."
    ),
    tools=[
        AgentTool(agent=compute_engine_subagent),
        AgentTool(cloud_storage_subagent),
        AgentTool(cloud_sql_subagent),
        AgentTool(big_query_subagent),
    ],
)
