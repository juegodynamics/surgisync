from typing import Optional, List
from pydantic.v1 import Field

from . import common, domainresource


class Organization(domainresource.DomainResource):
    resourceType = "Organization"

    active: bool = Field(
        default=None,
        alias="active",
        title="Whether the organization's record is still in active use",
        description=None,
    )

    name: str = Field(
        default=None,
        alias="name",
        title="Name used for the organization",
        description="A name associated with the organization.",
    )

    type: List[common.CodeableConcept] = Field(
        default=None,
        alias="type",
        title="Kind of organization",
        description="The kind(s) of organization that this is.",
    )

    alias: List[Optional[str]] = Field(
        default=None,
        alias="alias",
        title=(
            "A list of alternate names that the organization is known as, or was "
            "known as in the past"
        ),
        description=None,
    )

    contact: Optional[List[common.ExtendedContactDetail]] = Field(
        default=None,
        alias="contact",
        title="Official contact details for the Organization",
        description=(
            "The contact details of communication devices available relevant to the"
            " specific Organization. This can include addresses, phone numbers, fax"
            " numbers, mobile numbers, email addresses and web sites."
        ),
    )

    partOf: Optional[common.Reference] = Field(
        default=None,
        alias="partOf",
        title="The organization of which this organization forms a part",
        description=None,
        enum_reference_types=["Organization"],
    )

    def __str__(self) -> str:
        return f"Organization: {self.name}"
