from google.adk.agents import Agent

def get_answer_from_cloud_sql(question: str) -> dict:
    """Retrieves the answer for a specified Cloud SQL question.

    Args:
        question (str): A question about Cloud SQL.

    Returns:
        dict: status and result or error message.
    """
    if question:
        return {
            "status": "success",
            "report": (
                "You have retrieved the answer from Cloud SQL."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Information for '{question}' is not available.",
        }

cloud_sql_subagent=Agent(
    name="cloud_sql_subagent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about Cloud SQL."
    ),
    instruction=(
        "You are an agent who can answer user questions about cloud SQL."
    ),
    tools=[get_answer_from_cloud_sql],
)