from datetime import date

from app.agents.travel_agent import decide_travel_plan
from app.domain.models import TravelPlanStatus, TravelRequest
from app.domain.weather_assessment import assess_weather
from app.tools.weather_tool_api import get_weather_real, City

def main():
    base_request = TravelRequest(
        destination=City.DUBAI,  # placeholder, לא באמת בשימוש
        departure_date=date.today(),
        return_date=None,
        passengers=2,
        child_age=5,
        child_heat_sensitive=True,
    )

# Iterate over all possible destinations.
# Each iteration represents a new travel attempt with the same user constraints
# but a different destination.
    for destination in City:
        request = TravelRequest(
# Create a new TravelRequest for this iteration.
# We copy all constant user constraints from base_request
# and set only the destination for this specific attempt.
# This keeps requests immutable and avoids shared state.
            **base_request.model_dump(exclude={"destination"}),
            destination=destination,
        )
        
# Fetch real weather data for the destination of the current travel attempt.
        weather_data = get_weather_real(
            destination=request.destination,
            date=request.departure_date,
        )

        assessment = assess_weather(weather_data)
        travel_plan = decide_travel_plan(request, assessment)

        print(travel_plan)
        print(assessment)

        if travel_plan.status == TravelPlanStatus.APPROVED:
            break


if __name__ == "__main__":
    main()
