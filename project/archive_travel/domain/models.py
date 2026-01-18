from enum import Enum
from pydantic import BaseModel
from datetime import date
from archive_travel.tools.weather_tool import City, WeatherCondition

class HeatRiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TravelPlanStatus(str, Enum):
    APPROVED = "approved"
    MODIFIED = "modified"
    REJECTED = "rejected"

class RejectionReason(str, Enum):
    HEAT_RISK = "heat_risk"

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
    rejection_reason: RejectionReason | None = None
