from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from datetime import date


class PlanTripInput(BaseModel):
    """
    Input contract for the `plan_trip` MCP tool.

    Defines and validates all data required to request a travel plan.

    This model represents the system boundary:
    - Any invalid or missing data is rejected immediately
    - No business logic is executed unless this contract is valid
    """

    destination: str
    """Requested travel destination."""

    departure_date: date
    """Departure date for the trip."""

    return_date: Optional[date] = None
    """Optional return date. If omitted, the trip is considered one-way."""

    passengers: int = Field(..., gt=0)
    """Number of passengers. Must be a positive integer."""

    child_age: Optional[int] = Field(None, ge=0)
    """Age of the child passenger, if applicable."""

    child_heat_sensitive: bool = False
    """Indicates whether the child is sensitive to high temperatures."""


class PlanTripOutput(BaseModel):
    """
    Output contract for the `plan_trip` MCP tool.

    Represents a final, immutable snapshot of the system decision.

    The output is intentionally strict:
    - Only one decision path is allowed
    - Conflicting states are rejected via validation
    """

    status: Literal["APPROVED", "REJECTED"]
    """Final decision status for the travel request."""

    final_destination: Optional[str] = None
    """
    Final approved destination.
    Must be set only when status is APPROVED.
    """

    rejection_reason: Optional[str] = None
    """
    Human-readable explanation for rejection.
    Must be set only when status is REJECTED.
    """

    @model_validator(mode="after")
    def validate_consistency(self):
        """
        Ensures logical consistency of the output model.

        Business invariants:
        - An APPROVED plan cannot include a rejection reason
        - A REJECTED plan cannot include a final destination

        This validation prevents ambiguous or contradictory system states.
        """
        if self.status == "APPROVED" and self.rejection_reason is not None:
            raise ValueError("Approved plan cannot have rejection_reason")

        if self.status == "REJECTED" and self.final_destination is not None:
            raise ValueError("Rejected plan cannot have final_destination")

        return self
