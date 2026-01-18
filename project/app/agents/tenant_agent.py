from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantInput

# -------------------------
# Risk policy configuration
# -------------------------

# Penalties (how much each risk factor reduces the score)
LOW_INCOME_PENALTY = 40
LOW_CREDIT_PENALTY = 30
DEBT_PENALTY = 15
EVICTION_PENALTY = 25
CRIMINAL_RECORD_PENALTY = 40

# Thresholds
MIN_MONTHLY_INCOME = 5000
MIN_CREDIT_SCORE = 600

# Final decision threshold
APPROVAL_THRESHOLD = 70


def evaluate_tenant_risk(req: EvaluateTenantInput):
    """
    Tenant Agent.

    Receives a validated domain object (EvaluateTenantInput).
    Applies risk policy.
    Returns a partial risk evaluation.

    This agent:
    - Does NOT know about MCP
    - Does NOT know about JSON
    - Does NOT orchestrate flows
    - Only evaluates tenant risk
    """

    # Start from a perfect score
    score = 100
    reasons = []

    # 1. Income check
    if req.monthly_income < MIN_MONTHLY_INCOME:
        score -= LOW_INCOME_PENALTY
        reasons.append("Low monthly income")

    # 2. Credit score check
    if req.credit_score < MIN_CREDIT_SCORE:
        score -= LOW_CREDIT_PENALTY
        reasons.append("Low credit score")

    # 3. Existing debts
    if req.has_debts:
        score -= DEBT_PENALTY
        reasons.append("Has existing debts")

    # 4. Eviction history
    if req.eviction_history:
        score -= EVICTION_PENALTY
        reasons.append("Past eviction history")

    # 5. Criminal record
    if req.criminal_record == "yes":
        score -= CRIMINAL_RECORD_PENALTY
        reasons.append("Criminal record")

    # Keep score within 0–100
    score = max(0, min(100, score))

    # Final local decision
    approved = score >= APPROVAL_THRESHOLD

    return {
        "approved": approved,
        "score": score,
        "reasons": reasons or ["No significant risks detected"]
    }
