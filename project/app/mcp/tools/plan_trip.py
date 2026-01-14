from app.mcp.contracts.plan_trip_contract import PlanTripInput, PlanTripOutput
from app.orchestrator import run_travel_flow


def plan_trip(**kwargs):
    #This is the link between what is allowed to go in and out, and the orchestrator that runs the real flow.
    """
    MCP Tool: plan_trip

    Acts as a boundary adapter between:
    - External MCP input (raw JSON payload)
    - Internal domain orchestrator

    Responsibilities:
    1. Validate and parse input using PlanTripInput contract
    2. Delegate execution to the domain orchestrator
    3. Convert the domain result into a strict MCP output contract

    This function does NOT:
    - Make business decisions
    - Contain orchestration logic
    """

    # If the input is valid, it continues. If not, it stops.
    req = PlanTripInput(**kwargs)

    plan = run_travel_flow(req)

    # It formats and validates the output before returning it.
    return PlanTripOutput.from_domain(plan).model_dump()
