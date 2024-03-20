from models import Organization, Id, CodeableConcept, Reference
from models.codes import OrganizationType, ExtensionFactory

organization_level1_health_system = Organization(
    resourceType="Organization",
    id=Id("8e5571b4-18c4-37fb-b62a-c57a646b7771"),
    active=True,
    name="Fabric Health System",
    type=[CodeableConcept.from_coding(OrganizationType.prov)],
)

organization_level2_hospital = Organization(
    resourceType="Organization",
    id=Id("d44bc028-1f09-3d1c-820b-2318193ea02d"),
    active=True,
    name="Fabric Hospital New York City",
    type=[CodeableConcept.from_coding(OrganizationType.prov)],
    partOf=Reference.from_resource(organization_level1_health_system),
)

organization_level3_surgical = Organization(
    resourceType="Organization",
    id=Id("95ad675a-5851-3de7-941b-654d088ba6de"),
    active=True,
    name="FHNY: Medical Surgical Unit",
    type=[CodeableConcept.from_coding(OrganizationType.dept)],
    partOf=Reference.from_resource(organization_level2_hospital),
)


_preallocated_ids = [
    "328ddb8a-8229-4d7a-b2cf-30973b8cc85e",
    "c84caeba-0f8b-4393-8640-b715fc4a9614",
    "f62996eb-930a-4ad1-a14e-2ff903506979",
    "49656d43-81a0-4a07-951d-117cff52a5e5",
    "399cb413-d884-4e39-8fe7-fb1ce3ba6c0d",
    "597cce2c-dd98-4af1-9bcd-23bd44b0dcec",
    "bcf22ac8-575d-451a-978d-f05f7f7b26b8",
    "fc7dc66a-2cab-4828-8607-55e1412640d8",
    "719851ef-50a5-402a-ab35-3eb54f5bc8f7",
    "9421beab-8241-4c7a-a4ef-e74ac59ba42c",
    "8a908df1-b8a5-45a6-8154-d0c2c7df04d6",
    "ab62ca73-dc8f-436f-bfa2-b91b1b9346d1",
    "eaa69d66-a0a5-4b73-97ed-8d6feb0565e7",
    "e7d5fd55-28d5-46ea-9d26-2c02352b54f4",
    "5358ad10-feb5-48a9-ad77-056e00eb9b8e",
    "52f49714-4759-4ece-a99e-4af55baeedd7",
    "60aacfa1-42ed-4afc-bb3d-639567714564",
    "14979ee7-ce74-4ed7-b8ad-0b64ea2c3559",
    "122e7139-fc87-4a03-8d1f-efad3a75c505",
    "1f6b3b31-bdc5-485b-b41f-b513fa317dab",
]

organizations__level4_operating_rooms = [
    Organization(
        resourceType="Organization",
        id=Id(_preallocated_ids[room]),
        extension=[ExtensionFactory.OperatingRoom()],
        active=True,
        name=f"FHNY: Surgical - Operating Room {room+1}",
        type=[CodeableConcept.from_coding(OrganizationType.dept)],
        partOf=Reference.from_resource(organization_level3_surgical),
    )
    for room in range(20)
]

organization_level4_surgicalteam = Organization(
    resourceType="Organization",
    id=Id("20243188-67d0-3644-a90c-9520c0f59194"),
    extension=[ExtensionFactory.SurgicalTeam()],
    active=True,
    name="FHNY: Surgical Team",
    type=[CodeableConcept.from_coding(OrganizationType.team)],
    partOf=Reference.from_resource(organization_level3_surgical),
)
