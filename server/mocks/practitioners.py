from models import (
    Patient,
    PatientCommunication,
    Practitioner,
    Id,
    Identifier,
    HumanName,
    ContactPoint,
    Address,
    LanguageCode,
    Date,
)
from models.codes import USCoreRace, USCoreEthnicity, ExtensionFactory

practitioner_surgeon_1 = Practitioner(
    resourceType="Practitioner",
    active=True,
    name=[HumanName(family="Mills", given=["Ambrose"], prefix=["Dr."])],
    telecom=[],
)

practitioner_surgeon_2 = Practitioner(
    resourceType="Practitioner",
    active=True,
    name=[HumanName(family="Muller", given=["Mora"], prefix=["Dr."])],
    telecom=[],
)

practitioner_surgeon_3 = Practitioner(
    resourceType="Practitioner",
    active=True,
    name=[HumanName(family="Camarillo", given=["José"], prefix=["Dr."])],
    telecom=[],
)
