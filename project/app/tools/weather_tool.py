from datetime import date
from enum import Enum

from pydantic import BaseModel

from datetime import date



class WeatherCondition(str, Enum):  # we need str to make it JSON serializable in other words to avoid do .value calls
    SUNNY = "sunny"
    RAINY = "rainy"
    CLOUDY = "cloudy"

class City(str, Enum):
    DUBAI = "Dubai"
    LONDON = "London"
    PARIS = "Paris"
    ROME = "Rome"
    BANGKOK = "Bangkok"

MOCK_WEATHER_BY_DESTINATION = {
    City.DUBAI: {
        "temperature": 38,
        "condition": WeatherCondition.SUNNY,
    },
    City.LONDON: {
        "temperature": 18,
        "condition": WeatherCondition.CLOUDY,
    },
    City.PARIS: {
        "temperature": 22,
        "condition": WeatherCondition.CLOUDY,
    },
    City.ROME: {
        "temperature": 30,
        "condition": WeatherCondition.SUNNY,
    },
    City.BANGKOK: {
    "temperature": 36,
    "condition": WeatherCondition.SUNNY,
},
}

class WeatherData(BaseModel):
    """
    Raw weather facts returned by weather tools.
    Contains no interpretation or decisions.
    """
    destination: City
    temperature: float
    weather_condition: WeatherCondition

def get_weather(destination: City, date: date) -> WeatherData:
    """
    Weather Tool – mock implementation.
    Returns raw weather facts only.
    """

    data = MOCK_WEATHER_BY_DESTINATION.get(destination)

    if not data:
        raise ValueError(f"No mock weather for destination: {destination}")


    return WeatherData(
    destination=destination,
    temperature=data["temperature"],
    weather_condition=data["condition"]
)


