from app.domain.models import HeatRiskLevel, TravelPlanStatus, TravelRequest, TravelPlan, WeatherAssessment


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
                          explanation="Travel plan rejected due to high heat risk for heat-sensitive child.")
    
    return TravelPlan(
        final_destination=request.destination,
        status=TravelPlanStatus.APPROVED,
        explanation="No changes made to travel plan."
    )
    