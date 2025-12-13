from pydantic import BaseModel

class TravelRequest(BaseModel):
    destination: str
    departure_date: str
    return_date: str | None = None
    passengers: int = 1

    child_age: int | None = None
    child_heat_sensitive: bool | None = None


class WeatherAssessment(BaseModel):
    destination: str
    average_temperature: float
    weather_condition: str
    heat_risk_level: str | None = None