from datetime import date

from app.tools.weather_tool import get_weather, City
from project.app.domain.weather_assessment import assess_weather


def main():
    weather = get_weather(destination=City.DUBAI, date=date.today())
    assessment = assess_weather(weather)

    print("Weather data:", weather)
    print("Weather assessment:", assessment)


if __name__ == "__main__":
    main()
