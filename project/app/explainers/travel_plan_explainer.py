from app.domain.models import TravelPlan, TravelRequest


def explain_travel_plan(request: TravelRequest, plan: TravelPlan) -> str:
    """
    Explainer Agent.

    Responsibilities:
    - Format and explain the final travel plan to the user.
    - Provide a human-readable summary of the decision and reasoning.
    - Include the original request, final decision, and explanation.

    Args:
        request: The original travel request.
        plan: The final travel plan after all agents have processed it.

    Returns:
        A formatted string explanation of the travel plan.
    """

    explanation = f"""
Travel Plan Summary:
====================
Requested Destination: {request.destination}
Final Destination: {plan.final_destination}
Status: {plan.status}
Explanation: {plan.explanation}
"""

    if plan.rejection_reason:
        explanation += f"Rejection Reason: {plan.rejection_reason}\n"

    return explanation
