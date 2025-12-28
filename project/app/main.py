from datetime import date

from app.agents.travel_agent import (
    decide_travel_plan,
    suggest_alternative_destination,
)
from app.domain.models import TravelPlanStatus, TravelRequest
from app.domain.weather_assessment import assess_weather
from app.tools.weather_tool_api import get_weather_real, City


def main():
    """
    Orchestrator v1.

    Flow:
    1. Try original destination.
    2. If rejected, suggest one alternative destination.
    3. Try the alternative once.
    4. If rejected again, stop intentionally.
    """

    # Initial request (single source of truth for user constraints)
    request = TravelRequest(
        destination=City.DUBAI,
        departure_date=date.today(),
        return_date=None,
        passengers=2,
        child_age=5,
        child_heat_sensitive=True,
    )

    # ---------- First attempt ----------
    weather_data = get_weather_real(
        destination=request.destination,
        date=request.departure_date,
    )
    assessment = assess_weather(weather_data)
    travel_plan = decide_travel_plan(request, assessment)

    print("Initial plan:", travel_plan)
    print("Initial weather data:", weather_data)

    if travel_plan.status == TravelPlanStatus.APPROVED:
        # Success on first attempt
        return

    # ---------- One alternative attempt ----------
    alternative_plan = suggest_alternative_destination(
        request=request,
        rejected_plan=travel_plan,
    )
    # create a popy of the original request with the new destination
    alternative_request = request.model_copy(
        update={"destination": alternative_plan.final_destination}
    )

    weather_data = get_weather_real(
        destination=alternative_request.destination,
        date=alternative_request.departure_date,
    )
    assessment = assess_weather(weather_data)
    final_plan = decide_travel_plan(alternative_request, assessment)

    print("Final plan:", final_plan)
    print("Final weather data:", weather_data)
    

    if final_plan.status == TravelPlanStatus.REJECTED:
        # Stop here intentionally – no further retries
        print("No safe destination found after alternative attempt.")
        return


if __name__ == "__main__":
    main()
