from google.adk.agents import Agent

def get_answer_from_bigquery(question: str) -> dict:
    """Retrieves the answer for a specified bigquery question.

    Args:
        question (str): A question about bigquery.

    Returns:
        dict: status and result or error msg.
    """
    if question:
        return {
            "status": "success",
            "report": (
                "You have retrieved the answer from bigquery."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Information for '{question}' is not available.",
        }

big_query_subagent=Agent(
    name="big_query_subagent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about bigquery."
    ),
    instruction=(
        "You are an agent who can answer user questions about bigquery."
    ),
    tools=[get_answer_from_bigquery],
)