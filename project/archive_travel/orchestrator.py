"""
Legacy Travel Orchestration Flow.
Archive - No longer used in production.

This was the original travel planning flow:
1. Accept TravelRequest
2. Get weather data
3. Assess weather conditions
4. Decide if trip is safe
5. Handle rejections with alternative suggestions
6. Explain the final decision to user
"""

from archive_travel.domain.models import TravelRequest, TravelPlan
from archive_travel.domain.weather_assessment import assess_weather
from archive_travel.agents.travel_agent import (
    plan_trip,
    decide_travel_plan,
    suggest_alternative_destination,
)
from archive_travel.explainers.travel_plan_explainer import explain_travel_plan
from archive_travel.tools.weather_tool import get_weather


def run_travel_flow(request: TravelRequest) -> dict:
    """
    Legacy Travel Planning Flow (DEPRECATED).
    
    This was the original orchestration for travel planning.
    It is kept here for historical reference only.
    """
    
    # Step 1: Get weather for destination
    weather_data = get_weather(request.destination, request.departure_date)
    
    # Step 2: Assess weather conditions
    assessment = assess_weather(weather_data)
    
    # Step 3: Initial plan
    plan = plan_trip(request)
    
    # Step 4: Safety decision
    plan = decide_travel_plan(request, assessment)
    
    # Step 5: Handle rejections
    if plan.status.value == "rejected":
        plan = suggest_alternative_destination(request, plan)
    
    # Step 6: Explain final decision
    explanation = explain_travel_plan(request, plan)
    
    return {
        "plan": plan.model_dump(),
        "explanation": explanation,
    }
