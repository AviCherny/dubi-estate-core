from datetime import date
from app.orchestrator import run_travel_flow
from app.domain.models import TravelPlanStatus, TravelRequest
from app.explainers.llm_rejection_explainer import explain_rejection_with_llm
from app.tools.weather_tool import City



def run():

    request = TravelRequest(
        destination=City.DUBAI,
        departure_date=date.today(),
        return_date=None,
        passengers=2,
        child_age=5,
        child_heat_sensitive=True,
    )

    plan = run_travel_flow(request)

    if plan.status == TravelPlanStatus.REJECTED:
        explanation = explain_rejection_with_llm(
            request=request,  
            plan=plan,
        )
        print(explanation)
    else:
        print("Travel approved:", plan.final_destination)


if __name__ == "__main__":
    run()
