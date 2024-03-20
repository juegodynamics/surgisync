from typing import Optional, List
from pydantic.v1 import Field
from datetime import datetime

from . import base, common, domainresource


class AppointmentCancellationReason:
    level: int
    code: str
    display: str

    def __init__(self, level: int, code: str, display: str) -> None:
        self.level = level
        self.code = code
        self.display = display


APPOINTMENT_CANCELLATION_SYSTEM_URL = (
    "http://terminology.hl7.org/CodeSystem/appointment-cancellation-reason"
)
APPOINTMENT_CANCELLATION_REASONS = [
    AppointmentCancellationReason(1, "pat", "Patient"),
    AppointmentCancellationReason(
        2, "pat-crs", "Patient: Canceled via automated reminder system"
    ),
    AppointmentCancellationReason(2, "pat-cpp", "Patient: Canceled via Patient Portal"),
    AppointmentCancellationReason(2, "pat-dec", "Patient: Deceased"),
    AppointmentCancellationReason(2, "pat-fb", "Patient: Feeling Better"),
    AppointmentCancellationReason(2, "pat-lt", "Patient: Lack of Transportation"),
    AppointmentCancellationReason(2, "pat-mt", "Patient: Member Terminated"),
    AppointmentCancellationReason(2, "pat-mv", "Patient: Moved"),
    AppointmentCancellationReason(2, "pat-preg", "Patient: Pregnant"),
    AppointmentCancellationReason(2, "pat-swl", "Patient: Scheduled from Wait List"),
    AppointmentCancellationReason(2, "pat-ucp", "Patient: Unhappy/Changed Provider"),
    AppointmentCancellationReason(
        1,
        "prov",
        "Provider",
    ),
    AppointmentCancellationReason(2, "prov-pers", "Provider: Personal"),
    AppointmentCancellationReason(2, "prov-dch", "Provider: Discharged"),
    AppointmentCancellationReason(2, "prov-edu", "Provider: Edu/Meeting"),
    AppointmentCancellationReason(2, "prov-hosp", "Provider: Hospitalized"),
    AppointmentCancellationReason(
        2, "prov-labs", "Provider: Labs Out of Acceptable Range"
    ),
    AppointmentCancellationReason(
        2, "prov-mri", "Provider: MRI Screening Form Marked Do Not Proceed"
    ),
    AppointmentCancellationReason(
        2, "prov-onc", "Provider: Oncology Treatment Plan Changes"
    ),
    AppointmentCancellationReason(1, "maint	Equipment", "Maintenance/Repair"),
    AppointmentCancellationReason(1, "meds-inc", "Prep/Med Incomplete"),
    AppointmentCancellationReason(
        1,
        "other",
        "Other",
    ),
    AppointmentCancellationReason(
        2, "oth-cms", "Other: CMS Therapy Cap Service Not Authorized"
    ),
    AppointmentCancellationReason(2, "oth-err", "Other: Error"),
    AppointmentCancellationReason(2, "oth-fin", "Other: Financial"),
    AppointmentCancellationReason(
        2, "oth-iv", "Other: Improper IV Access/Infiltrate IV"
    ),
    AppointmentCancellationReason(2, "oth-int", "Other: No Interpreter Available"),
    AppointmentCancellationReason(2, "oth-mu", "Other: Prep/Med/Results Unavailable"),
    AppointmentCancellationReason(2, "oth-room", "Other: Room/Resource Maintenance"),
    AppointmentCancellationReason(2, "oth-oerr", "Other: Schedule Order Error"),
    AppointmentCancellationReason(2, "oth-swie", "Other: Silent Walk In Error"),
    AppointmentCancellationReason(2, "oth-weath", "Other: Weather"),
]


class Appointment(domainresource.DomainResource):
    resourceType = Field("Appointment", const=True)

    status: str = Field(
        default=None,
        alias="status",
        title=(
            "proposed | pending | booked | arrived | fulfilled | "
            "cancelled | noshow | entered-in-error | checked-in | waitlist"
        ),
        description=(
            "The overall status of the Appointment. Each of the participants"
            "has their own participation status which indicates their"
            "involvement in the process, however this status indicates the"
            "shared status."
        ),
        enum_values=[
            "proposed",
            "pending",
            "booked",
            "arrived",
            "fulfilled",
            "cancelled",
            "noshow",
            "entered-in-error",
            "checked-in",
            "waitlist",
        ],
    )

    subject: common.Reference = Field(
        default=None,
        alias="subject",
        title="The patient or group associated with the appointment",
        description=(
            "The patient or group associated with the appointment, if"
            "they are to be present (usually) then they should also be"
            "included in the participant backbone element."
        ),
        enum_reference_types=["Patient", "Group"],
    )

    participant: List["AppointmentParticipant"] = Field(
        default=None,
        alias="participant",
        title="Participants involved in appointment",
        description="List of participants involved in the appointment.",
    )

    reason: common.CodeableReference = Field(
        default=None,
        alias="reason",
        title="Reason this appointment is scheduled",
        description=(
            "The reason that this appointment is being scheduled. This "
            "is more clinical than administrative. This can be coded, "
            "or as specified using information from another resource. "
            "When the patient arrives and the encounter begins it may "
            "be used as the admission diagnosis. The indication will "
            "typically be a Condition (with other resources referenced "
            "in the evidence.detail), or a Procedure."
        ),
        enum_reference_types=[
            "Condition",
            "Procedure",
            "Observation",
            "ImmunizationRecommendation",
        ],
    )

    cancellationReason: Optional[common.CodeableConcept] = Field(
        default=None,
        alias="cancellationReason",
        title="The coded reason for the appointment being cancelled",
    )

    start: Optional[datetime] = Field(
        default=None,
        alias="start",
        title="When appointment is to take place",
        description=("Date/Time that the appointment is to take place."),
    )

    end: Optional[datetime] = Field(
        default=None,
        alias="end",
        title="Date/Time that the appointment is to conclude.",
        description=("When appointment is to conclude"),
    )

    minutesDuration: Optional[common.PositiveInt] = Field(
        default=None,
        alias="minutesDuration",
        title="Can be less than start/end (e.g. estimate)",
        description=(
            "Number of minutes that the appointment is to take."
            "This can be less than the duration between the start"
            "and end times. For example, where the actual time of"
            "appointment is only an estimate or if a 30 minute"
            "appointment is being requested, but any time would work."
            "Also, if there is, for example, a planned 15 minute break"
            "in the middle of a long appointment, the duration may be"
            "15 minutes less than the difference between the start"
            "and end."
        ),
    )


class AppointmentParticipant(base.Base):
    actor: common.Reference = Field(
        default=None,
        alias="actor",
        title=(
            "The individual, device, location, or service participating in the "
            "appointment"
        ),
        description=None,
        enum_reference_types=[
            "Patient",
            "Group",
            "Practitioner",
            "PractitionerRole",
            "CareTeam",
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    required: bool = Field(
        default=None,
        alias="required",
        title="The participant is required to attend (optional when false)",
        description=(
            "Whether this participant is required to be present at the meeting. If "
            "false, the participant is optional."
        ),
    )

    status: str = Field(
        None,
        alias="status",
        title="accepted | declined | tentative | needs-action",
        description="Participation status of the actor.",
        enum_values=["accepted", "declined", "tentative", "needs-action"],
    )

    type: List[common.CodeableConcept] = Field(
        None,
        alias="type",
        title="Role of participant in the appointment",
        description=None,
    )
