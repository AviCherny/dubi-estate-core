from datetime import date

from app.agents.travel_agent import decide_travel_plan
from app.domain.models import TravelRequest
from app.domain.weather_assessment import assess_weather
from app.tools.weather_tool_api import get_weather_real, City

def main():



    request = TravelRequest(
        destination = City.DUBAI,
        departure_date=date.today(),
        return_date=None, 
        passengers=2,
        child_age=5, 
        child_heat_sensitive=True)
    
    
    weather_data = get_weather_real(destination=request.destination, date=request.departure_date)
    assessment = assess_weather(weather_data)

    travel_plan = decide_travel_plan(request, assessment)
    print(travel_plan)
    print(assessment)


if __name__ == "__main__":
    main()
