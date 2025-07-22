from google.adk import Agent
from google.genai import types
from ..searchAgent import search_agent
from google.adk.tools.agent_tool import AgentTool
import time


MODEL = "gemini-2.5-flash"

def get_answer_from_bq(question: str) -> dict:
    """
    Handles questions related to BigQuery.                                                              

    Args: 
        question (str): The user's question about BigQuery.
    Returns: dict with status and response
    """

    return {
        "status": "success",
        "response": types.GenerateContentConfig(
            temperature=1,
        )
    }

def wait_5_seconds() -> dict:
    """
    Waits for 5 seconds, then acknowledges after that time is over.
    Args: none
    Returns: dict with status and response
    """
    seconds = 5
    while seconds > 0:
        time.sleep(1)
        seconds = seconds - 1

    return {
        "status": "success",
        "response": "I have waited for 5 seconds.",
    }


bq_agent = Agent(
    name="bq_agent",
    model=MODEL,
    description="Answer BQ related questions",
    instruction= ("You are an expert in Big Query (BQ)."
        "Your primary goal is to provide factual information about Big Query concepts and features to the user. "
        "If the user says to wait, call wait_5_seconds and then acknowledge that you waited for 5 seconds."
        "If the user says to use google search to answer their question, transfer to the search_agent to do a google search. "
        "If the user doesn't say to wait or to use google search, the default way to proceed in giving the user their response is to use the get_answer_from_bq and answer to the best of your ability."
    ),
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    tools = [get_answer_from_bq, wait_5_seconds,AgentTool(search_agent)],
                                                                                            
)