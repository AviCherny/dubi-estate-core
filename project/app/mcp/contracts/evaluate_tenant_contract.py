from pydantic import BaseModel, Field
from typing import Optional, Literal


class EvaluateTenantInput(BaseModel):
    """
    Contract for evaluating a tenant.

    This model answers four core questions:
    1. Does the tenant have money?
    2. Is the tenant financially stable?
    3. Is the tenant legally allowed to live here?
    4. Is there a clear risk from past behavior?
    """

    # 1. Does the tenant have money?
    monthly_income: float = Field(..., gt=0, description="Tenant monthly income")

    credit_score: int = Field(
        ..., ge=300, le=850, description="Tenant credit score (300-850 range)"
    )

    # 2. Is the tenant stable?
    employment_status: Literal[
        "employed",
        "self_employed",
        "student",
        "unemployed"
    ] = Field(..., description="Tenant employment stability status")

    has_debts: bool = Field(
        ..., description="Whether the tenant has significant existing debts"
    )

    has_guarantor: bool = Field(
        ..., description="Whether the tenant has a guarantor"
    )

    # 3. Is the tenant legal?
    legal_status: Literal[
        "citizen",
        "resident",
        "work_visa",
        "student_visa",
        "unknown"
    ] = Field(..., description="Tenant legal residency status")

    # 4. Is there a risk from the past?
    eviction_history: bool = Field(
        ..., description="Whether the tenant was evicted in the past"
    )

    criminal_record: Literal["yes", "no", "unknown"] = Field(
        "unknown",
        description="Whether the tenant has a criminal record (if known)"
    )

class EvaluateTenantOutput(BaseModel):
    """
    Output for tenant evaluation.

    This is the MCP response back to the client after DUBI processing.
    """
    tenant_id: str = Field(
        default="unknown",
        description="Identifier for the tenant being evaluated"
    )

    evaluation_score: float = Field(
        ..., ge=0, le=100, description="Evaluation score from 0 (bad) to 100 (excellent)"
    )

    evaluation_details: dict = Field(
        default_factory=dict,
        description="Detailed breakdown of the evaluation"
    )

    is_approved: bool = Field(
        ..., description="Whether the tenant is approved or not"
    )
