from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantOutput


def dubi_evaluate_tenant(req):
    """
    DUBI – Supervisor Agent (stub)

    Responsibilities:
    - Receive clean domain input
    - Decide which agents to call (future)
    - Aggregate results (future)

    For now:
    - Return a stub response
    """

    return EvaluateTenantOutput(
        status="REVIEW",
        score=50,
        reason="Stub response from DUBI – agents not implemented yet"
    )
