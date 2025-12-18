from enum import Enum
from pydantic import BaseModel
from datetime import date


from app.tools.weather_tool import City, WeatherCondition

class HeatRiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TravelPlanStatus(str, Enum):
    APPROVED = "approved"
    MODIFIED = "modified"
    REJECTED = "rejected"

class TravelRequest(BaseModel):
    destination: City
    departure_date: date | None = None
    return_date: date | None = None
    passengers: int = 1

    child_age: int | None = None
    child_heat_sensitive: bool | None = None

class WeatherAssessment(BaseModel):
    destination: City
    average_temperature: float
    weather_condition: WeatherCondition
    heat_risk_level: HeatRiskLevel

class TravelPlan(BaseModel):
    final_destination: City
    status: TravelPlanStatus
    explanation: str

class HeatAssessment(BaseModel): # הערכת סיכוני חום
    heat_risk_level: HeatRiskLevel

    