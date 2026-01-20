from datetime import date
from app.mcp.contracts.evaluate_landlord_contract import EvaluateLandlordInput


def evaluate_landlord_constraints(req: EvaluateLandlordInput):
    """
    Landlord Agent.

    Evaluates:
    1. Is the listing itself reasonable and usable?
    2. How strict is the landlord policy?
    """

    listing_ok = True
    policy_strictness = 0
    reasons = []

    # --- Listing checks (is the deal reasonable) ---
def evaluate_landlord_constraints(req):
    # Stub – landlord logic not implemented yet
    return {
        "approved": True,
        "reasons": ["Landlord policy not implemented yet"]
    }

    if req.min_lease_months > 24:
        listing_ok = False
        reasons.append("Lease duration requirement is very long")

    if req.available_from > date.today().replace(month=date.today().month + 6):
        listing_ok = False
        reasons.append("Property availability is too far in the future")

    # --- Policy strictness checks ---
    if req.min_credit_score > 750:
        policy_strictness += 30
        reasons.append("Credit score requirement is very strict")

    if req.min_income_multiplier > 4:
        policy_strictness += 25
        reasons.append("Income requirement is unusually high")

    if req.requires_guarantor:
        policy_strictness += 15
        reasons.append("Guarantor is mandatory")

    policy_strictness = min(100, policy_strictness)

    policy_ok = policy_strictness <= 60

    return {
        "listing_ok": listing_ok,
        "policy_ok": policy_ok,
        "strictness_score": policy_strictness,
        "reasons": reasons or ["Landlord conditions are reasonable"]
    }
