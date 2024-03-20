from datetime import datetime
from typing import Optional, List
from pydantic.v1 import Field

from . import common, domainresource


class Slot(domainresource.DomainResource):
    resourceType = Field("Slot", const=True)

    appointmentType: List[common.CodeableConcept] = Field(
        default=None,
        alias="appointmentType",
        title=(
            "The style of appointment or patient that may be booked in the slot "
            "(not service type)"
        ),
        description=None,
    )

    comment: Optional[str] = Field(
        default=None,
        alias="comment",
        title=(
            "Comments on the slot to describe any extended information. Such as "
            "custom constraints on the slot"
        ),
        description=None,
    )

    start: datetime = Field(
        default=None,
        alias="start",
        title="Date/Time that the slot is to begin",
        description=None,
    )

    end: datetime = Field(
        default=None,
        alias="end",
        title="Date/Time that the slot is to conclude",
        description=None,
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    status: str = Field(
        default=None,
        alias="status",
        title="busy | free | busy-unavailable | busy-tentative | entered-in-error",
        description=None,
        enum_values=[
            "busy",
            "free",
            "busy-unavailable",
            "busy-tentative",
            "entered-in-error",
        ],
    )

    schedule: Optional[common.Reference] = Field(
        default=None,
        alias="schedule",
        title=(
            "The schedule resource that this slot defines an interval of status "
            "information"
        ),
        description=None,
        enum_reference_types=["Schedule"],
    )

    serviceCategory: List[common.CodeableConcept] = Field(
        default=None,
        alias="serviceCategory",
        title=(
            "A broad categorization of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
    )

    specialty: List[common.CodeableConcept] = Field(
        default=None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
    )
