from datetime import datetime
from models import (
    Appointment,
    Patient,
    PatientCommunication,
    Id,
    Identifier,
    HumanName,
    ContactPoint,
    Address,
    LanguageCode,
    Date,
)
from models.codes import USCoreRace, USCoreEthnicity, ExtensionFactory

today = datetime.now()

appointment_surg_tomorrow = Appointment(
    resourceType="Appointment",
)
