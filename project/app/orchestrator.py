from app.agents.tenant_agent import evaluate_tenant_risk
from app.mcp.contracts.evaluate_tenant_contract import EvaluateTenantOutput
from app.agents.landlord_agent import evaluate_landlord_constraints


def dubi_evaluate_tenant(req):
    tenant_result = evaluate_tenant_risk(req)

    status = "APPROVED" if tenant_result["approved"] else "REJECTED"

    score = tenant_result.get("score", 50)
    reasons = tenant_result.get("reasons", ["No explanation provided"])

    return EvaluateTenantOutput(
        status=status,
        score=score,
        reason=", ".join(reasons)
    )
