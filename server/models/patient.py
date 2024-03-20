from typing import Optional, List, Any
from datetime import date
from pydantic.v1 import Field

from . import base, common, domainresource


class Patient(domainresource.DomainResource):
    resourceType = Field("Patient", const=True)

    active: bool = Field(
        default=None,
        alias="active",
        title="Whether this patient's record is in active use",
        description=(
            "Whether this patient record is in active use. "
            "Many systems use this property to mark as non-current "
            "patients, such as those that have not been seen for a "
            "period of time based on an organization's business "
            "rules. It is often used to filter patient lists to "
            "exclude inactive patients  Deceased patients may also "
            "be marked as inactive for the same reasons, but may be "
            "active for some time after death."
        ),
    )

    name: List[common.HumanName] = Field(
        default=None,
        alias="name",
        title="A name associated with the patient",
        description="A name associated with the individual.",
    )

    address: List[common.Address] = Field(
        default=None,
        alias="address",
        title="An address for the individual",
        description=None,
    )

    birthDate: date = Field(
        default=None,
        alias="birthDate",
        title="The date of birth for the individual",
        description=None,
    )

    gender: str = Field(
        default=None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that "
            "the patient is considered to have for "
            "administration and record keeping purposes. "
            "The gender might not match the biological sex "
            "as determined by genetics or the individual's "
            "preferred identification."
        ),
        enum_values=["male", "female", "other", "unknown"],
    )

    communication: List["PatientCommunication"] = Field(
        default=None,
        alias="communication",
        title=(
            "A language which may be used to communicate with the patient about his"
            " or her health"
        ),
        description=None,
    )

    photo: Optional[List[common.Base64Binary]] = Field(
        default=None,
        alias="photo",
        title="Image of the patient",
        description=None,
    )

    telecom: List[common.ContactPoint] = Field(
        None,
        alias="telecom",
        title="A contact detail for the individual",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the individual may be contacted."
        ),
    )


class PatientCommunication(base.Base):
    language: common.LanguageCode = Field(
        default=None,
        alias="language",
        title=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-AU" for Australian English.'
        ),
    )

    preferred: bool = Field(
        default=None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the patient prefers this language (over other"
            " languages he masters up a certain level)."
        ),
    )
