import re

from datetime import date, time, datetime
from typing import Optional, List, Any
from pydantic.v1 import Field
from pydantic.v1.types import ConstrainedStr, ConstrainedInt, ConstrainedBytes

from models.base import Base
from models.coding import Coding
from models.codes.codings import IdentifierType


class Id(ConstrainedStr):
    regex = re.compile(r"^[A-Za-z0-9\-.]+$")
    min_length = 1
    max_length = 64


class Date(date):
    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2]"
        r"[0-9]|3[0-1]))?)?"
    )

    @classmethod
    def to_string(self, value):
        if isinstance(value, (date, time, datetime)):
            value = value.isoformat()
        assert isinstance(value, str)
        return value


class DateTime(datetime):
    regex = re.compile(
        r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|"
        r"[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|"
        r"3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|"
        r"60)(\.[0-9]+)?(Z|([+\-])((0[0-9]|"
        r"1[0-3]):[0-5][0-9]|14:00)))?)?)?"
    )

    @classmethod
    def to_string(self, value):
        if isinstance(value, (date, time, datetime)):
            value = value.isoformat()
        assert isinstance(value, str)
        return value


class LanguageCode(ConstrainedStr):
    regex = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")


class Base64Binary(ConstrainedBytes):
    """A stream base64 encoded (RFC 4648 ) bytes"""

    regex = re.compile(r"^(\s*([0-9a-zA-Z+=]){4}\s*)+$")


class CodeableConcept(Base):
    coding: List[Coding] = Field(
        default=None,
        alias="coding",
        title="Code defined by a terminology system",
        description=("A reference to a code defined by a terminology system."),
    )

    text: Optional[str] = Field(
        default=None,
        alias="text",
        title="Plain text representation of the concept",
        description=(
            "A human language representation of the concept as"
            "seen/selected/uttered by the user who entered the"
            "data and/or which represents the intended meaning"
            "of the user."
        ),
    )

    @staticmethod
    def from_coding(coding: Coding) -> "CodeableConcept":
        return CodeableConcept(coding=[coding], text=coding.display)


class PositiveInt(ConstrainedInt):
    regex = re.compile(r"^\+?[1-9][0-9]*$")
    gt = 0


class CodeableReference(Base):
    concept: Optional[CodeableConcept] = Field(
        default=None,
        alias="concept",
        title="Reference to a concept (by class)",
        description=(
            "A reference to a concept - e.g. the information is "
            "identified by its general class to the degree of "
            "precision found in the terminology."
        ),
    )
    reference: Optional["Reference"] = Field(
        default=None,
        alias="reference",
        title="Reference to a resource (by instance)",
        description=(
            "A reference to a resource the provides exact details "
            "about the information being referenced."
        ),
    )


class Identifier(Base):
    system: str = Field(
        default=None,
        alias="system",
        title="The namespace for the identifier value",
        description=(
            "Establishes the namespace for the value - that"
            "is, an absolute URL that describes a set values"
            "that are unique."
        ),
    )

    value: str = Field(
        default=None,
        alias="value",
        title="The value that is unique",
        description=(
            "The portion of the identifier typically relevant"
            "to the user and which is unique within the context"
            "of the system."
        ),
    )

    type: Optional[CodeableConcept] = Field(
        default=None,
        alias="type",
        title="Description of identifier",
        description=(
            "A coded type for the identifier that can be used "
            "to determine which identifier to use for a specific purpose."
        ),
    )

    use: Optional[str] = Field(
        default=None,
        alias="use",
        title="usual | official | temp | secondary | old (If known)",
        description="The purpose of this identifier.",
        enum_values=["usual", "official", "temp", "secondary", "old"],
    )

    @staticmethod
    def social_security_number(value: str) -> "Identifier":
        return Identifier(
            type=CodeableConcept.from_coding(IdentifierType.SS),
            system="http://hl7.org/fhir/sid/us-ssn",
            value=value,
        )

    @staticmethod
    def drivers_license_number(value: str) -> "Identifier":
        return Identifier(
            type=CodeableConcept.from_coding(IdentifierType.DL),
            system="urn:oid:2.16.840.1.113883.4.3.25",
            value=value,
        )

    @staticmethod
    def passport_number(value: str) -> "Identifier":
        return Identifier(
            type=CodeableConcept.from_coding(IdentifierType.PPN),
            system="http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber",
            value=value,
        )


class HumanName(Base):
    family: Optional[str] = Field(
        default=None,
        alias="family",
        title="Family name (often called 'Surname')",
        description=(
            "The part of a name that links to the genealogy. In some cultures (e.g."
            " Eritrea) the family name of a son is the first name of his father."
        ),
    )

    given: List[Optional[str]] = Field(
        default=None,
        alias="given",
        title="Given names (not always 'first'). Includes middle names",
        description="Given name.",
    )

    prefix: List[Optional[str]] = Field(
        default=None,
        alias="prefix",
        title="Parts that come before the name",
        description=(
            "Part of the name that is acquired as a title due to academic, legal, "
            "employment or nobility status, etc. and that appears at the start of "
            "the name."
        ),
    )

    suffix: List[Optional[str]] = Field(
        default=None,
        alias="suffix",
        title="Parts that come after the name",
        description=(
            "Part of the name that is acquired as a title due to academic, legal, "
            "employment or nobility status, etc. and that appears at the end of "
            "the name."
        ),
    )

    text: str = Field(
        default=None,
        alias="text",
        title="Text representation of the full name",
        description=(
            "Specifies the entire name as it should be displayed e.g. on an "
            "application UI. This may be provided instead of or as well as the "
            "specific parts."
        ),
    )

    use: Optional[str] = Field(
        default=None,
        alias="use",
        title="usual | official | temp | nickname | anonymous | old | maiden",
        description="Identifies the purpose for this name.",
        enum_values=[
            "usual",
            "official",
            "temp",
            "nickname",
            "anonymous",
            "old",
            "maiden",
        ],
    )


class Address(Base):
    city: str = Field(
        default=None,
        alias="city",
        title="Name of city, town etc.",
        description=(
            "The name of the city, town, suburb, village or other community or "
            "delivery center."
        ),
    )

    country: str = Field(
        default=None,
        alias="country",
        title="Country (e.g. may be ISO 3166 2 or 3 letter code)",
        description="Country - a nation as commonly understood or generally accepted.",
    )

    district: str = Field(
        default=None,
        alias="district",
        title="District name (aka county)",
        description="The name of the administrative area (county).",
    )

    line: List[Optional[str]] = Field(
        default=None,
        alias="line",
        title="Street name, number, direction & P.O. Box etc.",
        description=(
            "This component contains the house number, apartment number, street "
            "name, street direction,  P.O. Box number, delivery hints, and similar "
            "address information."
        ),
    )

    postalCode: str = Field(
        default=None,
        alias="postalCode",
        title="Postal code for area",
        description="A postal code designating a region defined by the postal service.",
    )

    state: str = Field(
        default=None,
        alias="state",
        title="Sub-unit of country (abbreviations ok)",
        description=(
            "Sub-unit of a country with limited sovereignty in a federally "
            "organized country. A code may be used if codes are in common use (e.g."
            " US 2 letter state codes)."
        ),
    )

    text: str = Field(
        default=None,
        alias="text",
        title="Text representation of the address",
        description=(
            "Specifies the entire address as it should be displayed e.g. on a "
            "postal label. This may be provided instead of or as well as the "
            "specific parts."
        ),
    )


class ContactPoint(Base):
    system: str = Field(
        default=None,
        alias="system",
        title="phone | fax | email | pager | url | sms | other",
        description=(
            "Telecommunications form for contact point - what communications system"
            " is required to make use of the contact."
        ),
        enum_values=["phone", "fax", "email", "pager", "url", "sms", "other"],
    )

    value: str = Field(
        default=None,
        alias="value",
        title="The actual contact point details",
        description=(
            "The actual contact point details, in a form that is meaningful to the "
            "designated communication system (i.e. phone number or email address)."
        ),
    )

    use: Optional[str] = Field(
        default=None,
        alias="use",
        title="home | work | temp | old | mobile - purpose of this contact point",
        description="Identifies the purpose for the contact point.",
        enum_values=["home", "work", "temp", "old", "mobile"],
    )


class ExtendedContactDetail(Base):
    address: Optional[Address] = Field(
        default=None,
        alias="address",
        title="Address for the contact",
        description=None,
    )

    name: Optional[List[HumanName]] = Field(
        default=None,
        alias="name",
        title="Name of an individual to contact",
        description=(
            "The name of an individual to contact, some types of contact detail are"
            " usually blank."
        ),
    )

    organization: Optional["Reference"] = Field(
        None,
        alias="organization",
        title="This contact detail is handled/monitored by a specific organization",
        description=(
            "This contact detail is handled/monitored by a specific organization. "
            "If the name is provided in the contact, then it is referring to the "
            "named individual within this organization."
        ),
        enum_reference_types=["Organization"],
    )

    purpose: Optional[CodeableConcept] = Field(
        None,
        alias="purpose",
        title="The type of contact",
        description="The purpose/type of contact.",
    )

    telecom: Optional[List[ContactPoint]] = Field(
        None,
        alias="telecom",
        title="Contact details (e.g.phone/fax/url)",
        description="The contact details application for the purpose defined.",
    )


class Reference(Base):
    reference: str = Field(
        default=None,
        alias="reference",
        title="Literal reference, Relative, internal or absolute URL",
        description=(
            "A reference to a location at which the other resource"
            "is found. The reference may be a relative reference,"
            "in which case it is relative to the service base URL,"
            "or an absolute URL that resolves to the location where"
            "the resource is found. The reference may be version"
            "specific or not. If the reference is not to a FHIR"
            "RESTful server, then it should be assumed to be version"
            "specific. Internal fragment references (start with '#')"
            "refer to contained resources."
        ),
    )

    display: Optional[str] = Field(
        default=None,
        alias="display",
        title="Text alternative for the resource",
        description=(
            "Plain text narrative that identifies the resource in"
            "addition to the resource reference."
        ),
    )

    type: Optional[str] = Field(
        default=None,
        alias="type",
        title=(
            'Type the reference refers to (e.g. "Patient") - '
            "must be a resource in resources"
        ),
        description=(
            "The expected type of the target of the reference. If "
            "both Reference.type and Reference.reference are populated"
            "and Reference.reference is a FHIR URL, both SHALL be"
            "consistent."
        ),
    )

    @staticmethod
    def from_resource(resource: Any) -> "Reference":
        return Reference(
            type=resource.resourceType, reference=resource.id, display=str(resource)
        )
