from app.domain.models import TravelRequest, TravelPlan


def plan_trip(request: TravelRequest) -> TravelPlan:
    """
    Temporary Agent v1:
    - No weather logic
    - No decisions
    - Just returns a basic TravelPlan
    """

    return TravelPlan(
        final_destination=request.destination,
        was_modified=False,
        explanation="Initial version – no weather evaluation yet."
    )