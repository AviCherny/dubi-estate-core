from datetime import date

from app.agents.travel_agent import (
    decide_travel_plan,
    suggest_alternative_destination,
)
from app.domain.models import TravelPlan, TravelPlanStatus, TravelRequest
from app.domain.weather_assessment import assess_weather
from app.tools.weather_tool_api import get_weather_real, City


def run_travel_flow(request: TravelRequest) -> TravelPlan:
    """
    Orchestrator v1.

    Flow:
    1. Try original destination.
    2. If rejected, suggest one alternative destination.
    3. Try the alternative once.
    4. If rejected again, stop intentionally.
    """

    # ---------- First attempt ----------
    weather_data = get_weather_real(
        destination=request.destination,
        date=request.departure_date,
    )
    assessment = assess_weather(weather_data)
    travel_plan = decide_travel_plan(request, assessment)


    if travel_plan.status == TravelPlanStatus.APPROVED:
        # Success on first attempt
        return travel_plan
    
    # ---------- One alternative attempt ----------
    alternative_suggestion = suggest_alternative_destination(
        request=request,
        rejected_plan=travel_plan,
    )
    # create a copy of the original request with the new destination
    alternative_request = request.model_copy(
        update={"destination": alternative_suggestion.final_destination}
    )

    weather_data = get_weather_real(
        destination=alternative_request.destination,
        date=alternative_request.departure_date,
    )
    assessment = assess_weather(weather_data)
    final_plan = decide_travel_plan(alternative_request, assessment)

    return final_plan
