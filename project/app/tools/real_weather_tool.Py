from app.tools.weather_tool import WeatherData, City, WeatherCondition
from datetime import date
import requests
from typing import Dict, Any




CITY_COORDINATES  = {
    City.DUBAI: (25.276987, 55.296249),
    City.LONDON: (51.507351, -0.127758),
}

def _fetch_weather_from_api(latitude: float, longitude: float, target_date: date) ->  Dict[str, Any]:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max",
        "timezone": "UTC",
    }

    response = requests.get(url, params = params)
    response.raise_for_status()
    return response.json()


def get_weather_real(destination : City, date : date)-> WeatherData:

    coordinates = CITY_COORDINATES.get(destination)
    if not coordinates:
            raise ValueError(f"No coordinates defined for destination: {destination}")
    
    latitude, longitude = coordinates
    raw_data = _fetch_weather_from_api(latitude, longitude, date)
    temperature = raw_data["daily"]["temperature_2m_max"][0]


    return WeatherData(
        destination=destination,
        temperature=temperature,
        weather_condition=WeatherCondition.SUNNY,  # placeholder for now
    )