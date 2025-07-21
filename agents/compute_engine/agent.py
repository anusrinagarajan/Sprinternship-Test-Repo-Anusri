from google.adk.agents import Agent

def get_answer_from_compute_engine(question: str) -> dict:
    """Retrieves the answer for a specified compute question.

    Args:
        question (str): A question about compute engine.

    Returns:
        dict: status and result or error message.
    """
    if question:
        return {
            "status": "success",
            "report": (
                "You have retrieved the answer from compute engine."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Information for '{question}' is not available.",
        }

compute_engine_subagent=Agent(
    name="compute_engine_subagent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about Compute Engine."
    ),
    instruction=(
        "You are an agent who can answer user questions about compute engine."
    ),
    tools=[get_answer_from_compute_engine],
)