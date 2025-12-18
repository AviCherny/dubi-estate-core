from app.domain.models import HeatAssessment, HeatRiskLevel, WeatherAssessment
from app.tools.weather_tool import WeatherData


def assess_heat(temperature: float) -> HeatAssessment:
    if temperature >= 35:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.HIGH)
    elif 25 <= temperature < 35:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.MEDIUM)
    else:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.LOW)


def assess_weather(weatherdata: WeatherData) -> WeatherAssessment:
    heat = assess_heat(weatherdata.temperature)

    return WeatherAssessment(
        destination=weatherdata.destination,
        average_temperature=weatherdata.temperature,
        weather_condition=weatherdata.weather_condition,
        heat_risk_level=heat.heat_risk_level)