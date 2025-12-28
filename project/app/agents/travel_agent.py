from app.domain.models import HeatRiskLevel, RejectionReason, TravelPlanStatus, TravelRequest, TravelPlan, WeatherAssessment
from app.tools.weather_tool import City


def plan_trip(request: TravelRequest) -> TravelPlan:
    """
    Temporary Agent v1:
    - No weather logic
    - No decisions
    - Just returns a basic TravelPlan
    """

    return TravelPlan(
        final_destination=request.destination,
        status=TravelPlanStatus.APPROVED,
        explanation="Initial version – no weather evaluation yet."
    )


def decide_travel_plan(request: TravelRequest, assessment: WeatherAssessment) -> TravelPlan:
    """
    Decision agent that evaluates whether the current travel plan is safe, based on weather assessment and user constraints.
    """

    if request.child_heat_sensitive and assessment.heat_risk_level == HeatRiskLevel.HIGH:
        return TravelPlan(final_destination=request.destination,
                          status=TravelPlanStatus.REJECTED,
                          explanation="Travel plan rejected due to high heat risk for heat-sensitive child.",
                          rejection_reason=RejectionReason.HEAT_RISK)

    return TravelPlan(
        final_destination=request.destination,
        status=TravelPlanStatus.APPROVED,
        explanation="No changes made to travel plan."
    )

def suggest_alternative_destination(
    request: TravelRequest,
    rejected_plan: TravelPlan
) -> TravelPlan:
    """
    Suggests an alternative destination for a rejected travel plan.
    This agent is reactive and assumes it is called only after REJECTED.
    """

    if rejected_plan.status != TravelPlanStatus.REJECTED:
        raise ValueError(
            "DestinationSearchAgent expects a rejected TravelPlan."
        )

    alternative_destination = next(
        city for city in City if city != request.destination
    )

    return TravelPlan(
        final_destination=alternative_destination,
        status=TravelPlanStatus.MODIFIED,
        explanation=(
            "Original travel plan was rejected. "
            "Suggested an alternative destination."
        )
    )