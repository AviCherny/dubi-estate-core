from app.domain.models import TravelRequest, TravelPlan
from app.infra.llm_client import LLMClient


def explain_rejection_with_llm(
    request: TravelRequest,
    plan: TravelPlan,
) -> str:
    """
    Uses LLM to explain why a travel plan was rejected.

    Assumptions:
    - plan.status == REJECTED
    - rejection_reason is present
    """

    client = LLMClient()

    prompt = f"""
You are an explanation assistant.

The travel plan was already rejected by the system.
You are NOT allowed to change the decision.
You are NOT allowed to suggest alternative destinations.

Explain clearly and simply why the plan was rejected.

User request:
- Destination: {request.destination}
- Passengers: {request.passengers}
- Child age: {request.child_age}
- Child heat sensitive: {request.child_heat_sensitive}

System decision:
- Rejection reason: {plan.rejection_reason}
- Internal explanation: {plan.explanation}

Return a short, calm, human-friendly explanation.
"""

    print("DEBUG LLM PROMPT:\n", prompt)

    response = client.generate_text(prompt)

    print("DEBUG LLM RESPONSE:\n", response)

    return response.strip()
