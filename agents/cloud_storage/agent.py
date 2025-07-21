from google.adk.agents import Agent

def get_answer_from_cloud_storage(question: str) -> dict:
    """Retrieves the answer for a specified Cloud Storage question.

    Args:
        question (str): A question about Cloud Storage.

    Returns:
        dict: status and result or error message.
    """
    if question:
        return {
            "status": "success",
            "report": (
                "You have retrieved the answer from Cloud Storage."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Information for '{question}' is not available.",
        }

cloud_storage_subagent=Agent(
    name="cloud_storage_subagent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about Cloud Storage."
    ),
    instruction=(
        "You are an agent who can answer user questions about cloud storage."
    ),
    tools=[get_answer_from_cloud_storage],
)