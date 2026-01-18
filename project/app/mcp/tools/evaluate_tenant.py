from app.mcp.contracts.evaluate_tenant_contract import (
    EvaluateTenantInput,
    
)
from app.orchestrator import dubi_evaluate_tenant


def evaluate_tenant(**kwargs):
    """
    Boundary adapter for tenant evaluation.

    Responsibilities:
    - Receive raw JSON from MCP
    - Validate input using EvaluateTenantInput
    - Call DUBI (Supervisor Agent)
    - Return EvaluateTenantOutput (created by DUBI)

    """
    # 1. Validate and parse input
    req = EvaluateTenantInput(**kwargs)

    # 2. Delegate to DUBI
    result = dubi_evaluate_tenant(req)

    # 3. Return output in MCP-friendly format
    return result.model_dump()