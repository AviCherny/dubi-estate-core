from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantOutput


def dubi_evaluate_tenant(req):
    """
    DUBI – Supervisor Agent (stub)

    Responsibilities:
    - Receive clean domain input (EvaluateTenantInput)
    - Decide which agents to call (future)
    - Aggregate results (future)
    - Route to appropriate Real Estate agents

    For now:
    - Return a stub response

    This is the entry point for the Real Estate AI Agent architecture.
    Future agents will be composed here:
    - CreditScoreAgent
    - EmploymentVerificationAgent
    - EvictionHistoryAgent
    - etc.
    """

    return EvaluateTenantOutput(
        tenant_id=getattr(req, 'tenant_id', 'unknown'),
        evaluation_score=50.0,
        evaluation_details={
            "status": "REVIEW",
            "reason": "Stub response from DUBI – Real Estate agents not implemented yet"
        },
        is_approved=False
    )
