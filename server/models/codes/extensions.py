from models.coding import Coding
from models.extension import Extension


class ExtensionFactory:
    @staticmethod
    def USCoreRace(coding: Coding) -> Extension:
        return Extension(
            url="http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
            extension=[
                Extension(
                    url="ombCategory",
                    value={"coding": coding},
                ),
                Extension(url="text", value={"string": coding.display}),
            ],
        )

    @staticmethod
    def USCoreEthnicity(coding: Coding) -> Extension:
        return Extension(
            url="http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
            extension=[
                Extension(
                    url="ombCategory",
                    value={"coding": coding},
                ),
                Extension(url="text", value={"string": coding.display}),
            ],
        )

    @staticmethod
    def mothersMaidenName(value: str) -> Extension:
        return Extension(
            url="http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
            value={"string": value},
        )

    @staticmethod
    def USCoreBirthSex(code: str) -> Extension:
        return Extension(
            url="http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
            value={"code": code},
        )

    @staticmethod
    def OperatingRoom() -> Extension:
        return Extension(
            # TODO
            url="operating-room",
            value={"boolean": True},
        )

    @staticmethod
    def SurgicalTeam() -> Extension:
        return Extension(
            # TODO
            url="surgical-team",
            value={"boolean": True},
        )
