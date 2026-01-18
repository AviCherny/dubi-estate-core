from archive_travel.domain.models import (
    HeatRiskLevel,
    RejectionReason,
    TravelPlanStatus,
    TravelRequest,
    TravelPlan,
    WeatherAssessment,
)
from archive_travel.tools.weather_tool import City


def plan_trip(request: TravelRequest) -> TravelPlan:
    """
    Deprecated Agent (v1).

    This was an early experiment before the system was split into
    Assessment + Decision Agents.

    It is intentionally kept here:
    - As a reference point
    - To show the evolution of the architecture

    It is NOT used in the current flow and should not be extended.
    """

    return TravelPlan(
        final_destination=request.destination,
        status=TravelPlanStatus.APPROVED,
        explanation="Initial version – no weather evaluation yet.",
    )


def decide_travel_plan(request: TravelRequest, assessment: WeatherAssessment) -> TravelPlan:
    """
    SafetyAgent.

    Responsibilities:
    - Decide whether the travel plan is safe or not.
    - Produce a final APPROVED or REJECTED decision.
    - If REJECTED, attach a clear rejection_reason.

    Important:
    - This agent does NOT search for alternatives.
    - This agent does NOT fix problems.
    - It only decides and explains *why*.
    """

    if request.child_heat_sensitive and assessment.heat_risk_level == HeatRiskLevel.HIGH:
        return TravelPlan(
            final_destination=request.destination,
            status=TravelPlanStatus.REJECTED,
            rejection_reason=RejectionReason.HEAT_RISK,
            explanation="Travel plan rejected due to high heat risk for heat-sensitive child.",
        )

    return TravelPlan(
        final_destination=request.destination,
        status=TravelPlanStatus.APPROVED,
        explanation="No changes made to travel plan.",
    )


def suggest_alternative_destination(
    request: TravelRequest,
    rejected_plan: TravelPlan,
) -> TravelPlan:
    """
    DestinationSearchAgent.

    This agent reacts to *why* the travel plan was rejected,
    not just to the fact that it was rejected.

    It assumes:
    - SafetyAgent already made the decision.
    - rejection_reason is present and valid.

    This agent does NOT re-evaluate safety.
    It only proposes a modification strategy.
    """

    if rejected_plan.rejection_reason is None:
        raise ValueError(
            "DestinationSearchAgent requires a rejection_reason to operate."
        )

    if rejected_plan.rejection_reason == RejectionReason.HEAT_RISK:
        # Simple deterministic strategy for now:
        # choose any destination different from the original one.

        # status = what happened
        # rejection_reason = why it happened
        # agents react to the reason, not just the status
        alternative_destination = next(
            city for city in City if city != request.destination
        )
    else:
        # This makes missing strategies explicit and visible.
        raise NotImplementedError(
            f"No alternative strategy for rejection reason: {rejected_plan.rejection_reason}"
        )

    return TravelPlan(
        final_destination=alternative_destination,
        status=TravelPlanStatus.MODIFIED,
        explanation=(
            "Original travel plan was rejected due to heat risk. "
            "Suggested an alternative destination."
        ),
    )
