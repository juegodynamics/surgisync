from datetime import datetime, timedelta
from models import (
    Appointment,
    AppointmentParticipant,
    Reference,
    CodeableConcept,
    Coding,
    CodeableReference,
    Id,
)


tomorrow = datetime.now() + timedelta(days=1)
schedule_datetime_start = datetime(
    tomorrow.year, tomorrow.month, tomorrow.day, 12, 0, 0
)
schedule_datetime_end = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 18, 0, 0)

Appointment.update_forward_refs()

appointment_surg_tomorrow = Appointment(
    id=Id("7cf53c33-3150-42f2-a5f3-59019c339f06"),
    resourceType="Appointment",
    status="booked",
    subject=Reference(reference="22c7dbd1-8de4-b7c3-b2ed-63dded3aca23", type="Patient"),
    participant=[
        AppointmentParticipant(
            actor=Reference(
                reference="328ddb8a-8229-4d7a-b2cf-30973b8cc85e", type="Organization"
            ),
            required=True,
            status="accepted",
            type=[
                CodeableConcept(
                    coding=[
                        Coding(
                            system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            code="ATND",
                            display="attender",
                        )
                    ],
                    text="attender",
                )
            ],
        )
    ],
    reason=CodeableReference(
        concept=CodeableConcept(
            coding=[
                Coding(
                    system="http://hl7.org/fhir/ValueSet/icd-10",
                    code="K35.80",
                    display="Unspecified acute appendicitis",
                )
            ],
            text="Unspecified acute appendicitis",
        ),
    ),
    start=schedule_datetime_start,
    end=schedule_datetime_end,
)
