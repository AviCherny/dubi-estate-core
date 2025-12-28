from app.domain.models import HeatRiskLevel, WeatherAssessment
from app.tools.weather_tool import WeatherData


def assess_weather(weatherdata: WeatherData) -> WeatherAssessment:
    """
    Interprets raw weather data into a domain-level weather assessment.
    No decisions are made here.
    """

    temperature = weatherdata.temperature

    if temperature >= 22:
        heat_risk = HeatRiskLevel.HIGH
    elif 18 <= temperature < 22:
        heat_risk = HeatRiskLevel.MEDIUM
    else:
        heat_risk = HeatRiskLevel.LOW

    return WeatherAssessment(
        destination=weatherdata.destination,
        average_temperature=temperature,
        weather_condition=weatherdata.weather_condition,
        heat_risk_level=heat_risk,
    )