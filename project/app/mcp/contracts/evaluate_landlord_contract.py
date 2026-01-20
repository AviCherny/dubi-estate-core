from pydantic import BaseModel, Field
from datetime import date


class EvaluateLandlordInput(BaseModel):
    """
    Represents the property listing and landlord policy.
    This is NOT about the tenant, only about what the landlord offers and requires.
    """

    # Property listing facts
    rent_monthly: float = Field(..., gt=0)
    deposit_months: int = Field(..., ge=0, le=6)
    available_from: date
    min_lease_months: int = Field(..., ge=1)
    allows_pets: bool

    # Landlord policy (requirements)
    min_credit_score: int = Field(..., ge=0, le=900)
    min_income_multiplier: float = Field(..., ge=1.0)
    requires_guarantor: bool
