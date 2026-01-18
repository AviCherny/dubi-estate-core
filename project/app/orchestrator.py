from app.agents.tenant_agent import evaluate_tenant_risk
from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantOutput


def dubi_evaluate_tenant(req):
    """
    DUBI – Supervisor Agent (v1)

    Responsibilities:
    - Receive clean domain input (EvaluateTenantInput)
    - Decide which agents to call
    - Aggregate their results
    - Build the final system decision (MCP output)

    Current version:
    - Uses a single agent: Tenant Agent
    - Designed to scale to multiple agents later
    """

    # 1. Call Tenant Agent
    tenant_result = evaluate_tenant_risk(req)

    # 2. Translate agent result into system-level decision
    status = "APPROVED" if tenant_result["approved"] else "REJECTED"

    # 3. Build final MCP contract output
    return EvaluateTenantOutput(
    tenant_id="unknown",
    evaluation_score=tenant_result["score"],
    evaluation_details={
        "approved": tenant_result["approved"],
        "reasons": tenant_result["reasons"]
    },
    is_approved=tenant_result["approved"]
)
