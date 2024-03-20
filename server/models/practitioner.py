from typing import Optional, List
from pydantic.v1 import Field

from . import base, common, domainresource


class Practitioner(domainresource.DomainResource):
    resourceType = Field("Practitioner", const=True)

    active: bool = Field(
        default=None,
        alias="active",
        title="Whether this practitioner's record is in active use",
        description=None,
    )

    name: List[common.HumanName] = Field(
        default=None,
        alias="name",
        title="The name(s) associated with the practitioner",
        description="A name associated with the individual.",
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

    photo: Optional[List[common.Base64Binary]] = Field(
        default=None,
        alias="photo",
        title="Image of the patient",
        description=None,
    )

    qualification: List["PractitionerQualification"] = Field(
        default=None,
        alias="qualification",
        title=(
            "Qualifications, certifications, accreditations, licenses, training, "
            "etc. pertaining to the provision of care"
        ),
        description=(
            "The official qualifications, certifications, accreditations, training, "
            "licenses (and other types of educations/skills/capabilities) that "
            "authorize or otherwise pertain to the provision of care by the "
            "practitioner.  For example, a medical license issued by a medical "
            "board of licensure authorizing the practitioner to practice medicine "
            "within a certain locality."
        ),
    )

    communication: List["PractitionerCommunication"] = Field(
        default=None,
        alias="communication",
        title="A language which may be used to communicate with the practitioner",
        description=(
            "A language which may be used to communicate with the practitioner, "
            "often for correspondence/administrative purposes.  The "
            "`PractitionerRole.communication` property should be used for "
            "publishing the languages that a practitioner is able to communicate "
            "with patients (on a per Organization/Role basis)."
        ),
    )


class PractitionerQualification(base.Base):
    code: common.CodeableConcept = Field(
        default=None,
        alias="code",
        title="Coded representation of the qualification",
        description=None,
    )

    identifier: Optional[List[common.Identifier]] = Field(
        default=None,
        alias="identifier",
        title="An identifier for this qualification for the practitioner",
        description="An identifier that applies to this person's qualification.",
    )

    issuer: common.Reference = Field(
        None,
        alias="issuer",
        title="Organization that regulates and issues the qualification",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )


class PractitionerCommunication(base.Base):
    language: common.LanguageCode = Field(
        default=None,
        alias="language",
        title=("The language code used to communicate with the practitioner"),
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
            "Indicates whether or not the person prefers this language "
            "(over other languages he masters up a certain level)."
        ),
    )
