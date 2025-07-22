from google.adk import Agent
from google.genai import types
from google.adk.tools import google_search

MODEL = "gemini-2.5-flash"

search_agent = Agent(
    name="search_agent",
    model=MODEL,
    description="Agent that performs a google search when given a request.",
    instruction="You are an agent that performs a Google Search when given a user's request. Make sure to always cite your sources.",
    tools=[google_search],
)