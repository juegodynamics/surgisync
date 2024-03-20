from models import (
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

"""============================================================================
   Section A: Patients with Extensions

   These patients have additional extension fields, currently unused in any
   feature
   ============================================================================
"""

Patient.update_forward_refs()

patient_Douglas_Olson = Patient(
    resourceType="Patient",
    id=Id("22c7dbd1-8de4-b7c3-b2ed-63dded3aca23"),
    active=True,
    extension=[
        ExtensionFactory.USCoreRace(USCoreRace.White),
        ExtensionFactory.USCoreEthnicity(USCoreEthnicity.NotHispanicOrLatino),
        ExtensionFactory.mothersMaidenName("Kimber McLaughlin"),
        ExtensionFactory.USCoreBirthSex("M"),
    ],
    identifier=[
        Identifier.social_security_number("999-14-3860"),
        Identifier.drivers_license_number("S99976928"),
        Identifier.passport_number("X66542052X"),
    ],
    name=[
        HumanName(
            use="official",
            family="Olson",
            given=["Douglas", "Marshall"],
            prefix=["Mr."],
        )
    ],
    telecom=[ContactPoint(system="phone", value="555-729-6709", use="home")],
    gender="male",
    birthDate=Date(year=1988, month=3, day=21),
    address=[
        Address(
            line=["113 Torphy Bridge"],
            city="Beacon",
            state="NY",
            postalCode="12508",
            country="US",
        )
    ],
)

patient_Elidia_Suellen_Hackett = Patient(
    resourceType="Patient",
    id=Id("373c94e6-93e4-12e9-447b-d64af4a8c7c3"),
    active=True,
    extension=[
        ExtensionFactory.USCoreRace(USCoreRace.Black),
        ExtensionFactory.USCoreEthnicity(USCoreEthnicity.NotHispanicOrLatino),
        ExtensionFactory.mothersMaidenName("Inocencia Rodriguez"),
        ExtensionFactory.USCoreBirthSex("F"),
    ],
    identifier=[
        Identifier.social_security_number("999-14-3860"),
        Identifier.drivers_license_number("S99913927"),
        Identifier.passport_number("X58028001X"),
    ],
    name=[
        HumanName(
            use="official",
            family="Hackett",
            given=["Elidia", "Suellen"],
            prefix=["Mrs."],
        ),
        HumanName(
            use="maiden",
            family="Skiles",
            given=["Elidia", "Suellen"],
            prefix=["Mrs."],
        ),
    ],
    telecom=[ContactPoint(system="phone", value="555-570-6576", use="home")],
    gender="female",
    birthDate=Date(year=1966, month=9, day=10),
    address=[
        Address(
            line=["940 Crooks Meadow"],
            city="Greece",
            state="NY",
            postalCode="14626",
            country="US",
        )
    ],
)

patient_Marco_Antonio_Candelaria = Patient(
    resourceType="Patient",
    id=Id("9ebd9944-1ffb-a0d3-902c-1cb8a7416785"),
    active=True,
    extension=[
        ExtensionFactory.USCoreRace(USCoreRace.Black),
        ExtensionFactory.USCoreEthnicity(USCoreEthnicity.HispanicOrLatino),
        ExtensionFactory.mothersMaidenName("María José Rolón"),
        ExtensionFactory.USCoreBirthSex("M"),
    ],
    identifier=[
        Identifier.social_security_number("999-58-4064"),
    ],
    name=[
        HumanName(
            use="official",
            family="Candelaria",
            given=["Marco Antonio", "Eduardo"],
        ),
    ],
    telecom=[ContactPoint(system="phone", value="555-198-2280", use="home")],
    gender="male",
    birthDate=Date(year=2001, month=11, day=24),
    address=[
        Address(
            line=["291 Lowe Viaduct", "Unit 56"],
            city="New York",
            state="NY",
            postalCode="11001",
            country="US",
        )
    ],
    communication=[PatientCommunication(language=LanguageCode("es"))],
)

"""============================================================================
   Section B: Other Patients

   These patients have additional extension fields, currently unused in any
   feature
   ============================================================================
"""
