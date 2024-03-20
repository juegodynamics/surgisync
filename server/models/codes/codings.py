from typing import Dict
from models.coding import Coding


class USCoreRace(Dict[str, Coding]):
    White: Coding = Coding(
        system="urn:oid:2.16.840.1.113883.6.238", code="2106-3", display="White"
    )
    Black: Coding = Coding(
        system="urn:oid:2.16.840.1.113883.6.238",
        code="2054-5",
        display="Black or African American",
    )


class USCoreEthnicity(Dict[str, Coding]):
    HispanicOrLatino: Coding = Coding(
        system="urn:oid:2.16.840.1.113883.6.238",
        code="2135-2",
        display="Hispanic or Latino",
    )
    NotHispanicOrLatino: Coding = Coding(
        system="urn:oid:2.16.840.1.113883.6.238",
        code="2186-5",
        display="Not Hispanic or Latino",
    )


class IdentifierType(Dict[str, Coding]):
    AC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AC",
        display="Accreditation/Certification Identifier",
    )
    ACSN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ACSN",
        display="Accession ID",
    )
    AIN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AIN",
        display="Animal Identification Number (US Official)",
    )
    AM: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AM",
        display="American Express",
    )
    AMA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AMA",
        display="American Medical Association Number",
    )
    AN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AN",
        display="Account number",
    )
    ANC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ANC",
        display="Account number Creditor",
    )
    AND: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="AND",
        display="Account number debitor",
    )
    ANON: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ANON",
        display="Anonymous identifier",
    )
    ANT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ANT",
        display="Temporary Account Number",
    )
    APRN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="APRN",
        display="Advanced Practice Registered Nurse number",
    )
    ASID: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ASID",
        display="Ancestor Specimen ID",
    )
    BA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BA",
        display="Bank Account Number",
    )
    BC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BC",
        display="Bank Card Number",
    )
    BCFN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BCFN",
        display="Birth Certificate File Number",
    )
    BCT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BCT",
        display="Birth Certificate",
    )
    BR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BR",
        display="Birth registry number",
    )
    BRN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BRN",
        display="Breed Registry Number",
    )
    BSNR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="BSNR",
        display="Primary physician office number",
    )
    CAAI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="CAAI",
        display="Consumer Application Account Identifier",
    )
    CC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="CC",
        display="Cost Center number",
    )
    CONM: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="CONM",
        display="Change of Name Document",
    )
    CY: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="CY",
        display="County number",
    )
    CZ: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="CZ",
        display="Citizenship Card",
    )
    DC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DC",
        display="Death Certificate ID",
    )
    DCFN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DCFN",
        display="Death Certificate File Number",
    )
    DDS: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DDS",
        display="Dentist license number",
    )
    DEA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DEA",
        display="Drug Enforcement Administration registration number",
    )
    DFN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DFN",
        display="Drug Furnishing or prescriptive authority Number",
    )
    DI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DI",
        display="Diner's Club card",
    )
    DL: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DL",
        display="Driver's license number",
    )
    DN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DN",
        display="Doctor number",
    )
    DO: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DO",
        display="Osteopathic License number",
    )
    DP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DP",
        display="Diplomatic Passport",
    )
    DPM: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DPM",
        display="Podiatrist license number",
    )
    DR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DR",
        display="Donor Registration Number",
    )
    DS: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DS",
        display="Discover Card",
    )
    DSG: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="DSG",
        display="Diagnostic Study Group",
    )
    EI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="EI",
        display="Employee number",
    )
    EN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="EN",
        display="Employer number",
    )
    ESN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="ESN",
        display="Staff Enterprise Number",
    )
    FDR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="FDR",
        display="Fetal Death Report ID",
    )
    FDRFN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="FDRFN",
        display="Fetal Death Report File Number",
    )
    FGN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="FGN",
        display="Filler Group Number",
    )
    FI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="FI",
        display="Facility ID",
    )
    FILL: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="FILL",
        display="Filler Identifier",
    )
    GI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="GI",
        display="Guarantor internal identifier",
    )
    GIN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="GIN",
        display="Animal Group Identifier (US Official)",
    )
    GL: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="GL",
        display="General ledger number",
    )
    GN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="GN",
        display="Guarantor external identifier",
    )
    HC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="HC",
        display="Health Card Number",
    )
    IND: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="IND",
        display="Indigenous/Aboriginal",
    )
    IRISTEM: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="IRISTEM",
        display="An IRI stem",
    )
    JHN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="JHN",
        display="Jurisdictional health number",
    )
    LACSN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="LACSN",
        display="Laboratory Accession ID",
    )
    LANR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="LANR",
        display="Lifelong physician number",
    )
    LI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="LI",
        display="Labor and industries number",
    )
    L_and_I: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="L&I",
        display="Labor and industries number",
    )
    LN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="LN",
        display="License number",
    )
    LR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="LR",
        display="Local Registry ID",
    )
    MA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MA",
        display="Patient Medicaid number",
    )
    MB: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MB",
        display="Member Number",
    )
    MC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MC",
        display="Patient's Medicare number",
    )
    MCD: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MCD",
        display="Practitioner Medicaid number",
    )
    MCN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MCN",
        display="Microchip Number",
    )
    MCR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MCR",
        display="Practitioner Medicare number",
    )
    MCT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MCT",
        display="Marriage Certificate",
    )
    MD: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MD",
        display="Medical License number",
    )
    MI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MI",
        display="Military ID number",
    )
    MR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MR",
        display="Medical record number",
    )
    MRT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MRT",
        display="Temporary Medical Record Number",
    )
    MS: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="MS",
        display="MasterCard",
    )
    NBSNR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NBSNR",
        display="Secondary physician office number",
    )
    NCT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NCT",
        display="Naturalization Certificate",
    )
    NE: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NE",
        display="National employer identifier",
    )
    NH: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NH",
        display="National Health Plan Identifier",
    )
    NI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NI",
        display="National unique individual identifier",
    )
    NII: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NII",
        display="National Insurance Organization Identifier",
    )
    NIIP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NIIP",
        display="National Insurance Payor Identifier (Payor)",
    )
    NNxxx: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NNxxx",
        display="National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code",
    )
    NP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NP",
        display="Nurse practitioner number",
    )
    NPI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="NPI",
        display="National provider identifier",
    )
    OBI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="OBI",
        display="Observation Instance Identifier",
    )
    OD: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="OD",
        display="Optometrist license number",
    )
    PA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PA",
        display="Physician Assistant number",
    )
    PC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PC",
        display="Parole Card",
    )
    PCN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PCN",
        display="Penitentiary/correctional institution Number",
    )
    PE: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PE",
        display="Living Subject Enterprise Number",
    )
    PEN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PEN",
        display="Pension Number",
    )
    PGN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PGN",
        display="Placer Group Number",
    )
    PHC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PHC",
        display="Public Health Case Identifier",
    )
    PHE: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PHE",
        display="Public Health Event Identifier",
    )
    PHO: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PHO",
        display="Public Health Official ID",
    )
    PI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PI",
        display="Patient internal identifier",
    )
    PIN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PIN",
        display="Premises Identifier Number (US Official)",
    )
    PLAC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PLAC",
        display="Placer Identifier",
    )
    PN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PN",
        display="Person number",
    )
    PNT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PNT",
        display="Temporary Living Subject Number",
    )
    PPIN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PPIN",
        display="Medicare/CMS Performing Provider Identification Number",
    )
    PPN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PPN",
        display="Passport number",
    )
    PRC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PRC",
        display="Permanent Resident Card Number",
    )
    PRN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PRN",
        display="Provider number",
    )
    PT: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="PT",
        display="Patient external identifier",
    )
    QA: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="QA",
        display="QA number",
    )
    RI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RI",
        display="Resource identifier",
    )
    RN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RN",
        display="Registered Nurse Number",
    )
    RPH: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RPH",
        display="Pharmacist license number",
    )
    RR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RR",
        display="Railroad Retirement number",
    )
    RRI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RRI",
        display="Regional registry ID",
    )
    RRP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="RRP",
        display="Railroad Retirement Provider",
    )
    SAMN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SAMN",
        display="SAMN# accession Number",
    )
    SB: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SB",
        display="Social Beneficiary Identifier",
    )
    SID: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SID",
        display="Specimen ID",
    )
    SL: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SL",
        display="State license",
    )
    SN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SN",
        display="Subscriber Number",
    )
    SNBSN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SNBSN",
        display="State assigned NDBS card Identifier",
    )
    SNO: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SNO",
        display="Serial Number",
    )
    SP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SP",
        display="Study Permit",
    )
    SR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SR",
        display="State registry ID",
    )
    SRX: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SRX",
        display="SRA Accession number",
    )
    SS: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="SS",
        display="Social Security number",
    )
    STN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="STN",
        display="Shipment Tracking Number",
    )
    TAX: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="TAX",
        display="Tax ID number",
    )
    TN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="TN",
        display="Treaty Number/ (Canada)",
    )
    TPR: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="TPR",
        display="Temporary Permanent Resident (Canada)",
    )
    TRL: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="TRL",
        display="Training License Number",
    )
    U: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="U",
        display="Unspecified identifier",
    )
    UDI: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="UDI",
        display="Universal Device Identifier",
    )
    UPIN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="UPIN",
        display="Medicare/CMS (formerly HCFA)'s Universal Physician Identification numbers",
    )
    USID: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="USID",
        display="Unique Specimen ID",
    )
    VN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="VN",
        display="Visit number",
    )
    VP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="VP",
        display="Visitor Permit",
    )
    VS: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="VS",
        display="VISA",
    )
    WC: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="WC",
        display="WIC identifier",
    )
    WCN: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="WCN",
        display="Workers' Comp Number",
    )
    WP: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="WP",
        display="Work Permit",
    )
    XV: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="XV",
        display="Health Plan Identifier",
    )
    XX: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v2-0203",
        code="XX",
        display="Organization identifier",
    )


class BirthSex(Dict[str, Coding]):
    F: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender",
        code="F",
        display="Female",
    )
    M: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender",
        code="M",
        display="Male",
    )
    ASKU: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        code="ASKU",
        display="asked but unknown",
    )
    OTH: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        code="OTH",
        display="other",
    )
    UNK: Coding = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
        code="UNK",
        display="unknown",
    )


class ParticipantType(Dict[str, Coding]):
    PART = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="PART",
        display="Participation",
    )
    _ParticipationAncillary = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="_ParticipationAncillary",
        display="ParticipationAncillary",
    )
    ADM = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ADM",
        display="admitter",
    )
    ATND = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ATND",
        display="attender",
    )
    CALLBCK = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CALLBCK",
        display="callback contact",
    )
    CON = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CON",
        display="consultant",
    )
    DIS = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DIS",
        display="discharger",
    )
    ESC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ESC",
        display="escort",
    )
    REF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="REF",
        display="referrer",
    )
    _ParticipationInformationGenerator = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="_ParticipationInformationGenerator",
        display="ParticipationInformationGenerator",
    )
    AUT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="AUT",
        display="author (originator)",
    )
    INF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="INF",
        display="informant",
    )
    TRANS = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="TRANS",
        display="Transcriber",
    )
    ENT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ENT",
        display="data entry person",
    )
    WIT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="WIT",
        display="witness",
    )
    NOTARY = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="NOTARY",
        display="notary",
    )
    CST = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CST",
        display="custodian",
    )
    DIR = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DIR",
        display="direct target",
    )
    ALY = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ALY",
        display="analyte",
    )
    BBY = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="BBY",
        display="baby",
    )
    CAT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CAT",
        display="catalyst",
    )
    CSM = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CSM",
        display="consumable",
    )
    TPA = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="TPA",
        display="therapeutic agent",
    )
    DEV = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DEV",
        display="device",
    )
    NRD = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="NRD",
        display="non-reuseable device",
    )
    RDV = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="RDV",
        display="reusable device",
    )
    DON = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DON",
        display="donor",
    )
    EXPAGNT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="EXPAGNT",
        display="ExposureAgent",
    )
    EXPART = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="EXPART",
        display="ExposureParticipation",
    )
    EXPTRGT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="EXPTRGT",
        display="ExposureTarget",
    )
    EXSRC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="EXSRC",
        display="ExposureSource",
    )
    PRD = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="PRD",
        display="product",
    )
    SBJ = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="SBJ",
        display="subject",
    )
    SPC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="SPC",
        display="specimen",
    )
    IND = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="IND",
        display="indirect target",
    )
    BEN = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="BEN",
        display="beneficiary",
    )
    CAGNT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="CAGNT",
        display="causative agent",
    )
    COV = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="COV",
        display="coverage target",
    )
    GUAR = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="GUAR",
        display="guarantor party",
    )
    HLD = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="HLD",
        display="holder",
    )
    RCT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="RCT",
        display="record target",
    )
    RCV = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="RCV",
        display="receiver",
    )
    IRCP = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="IRCP",
        display="information recipient",
    )
    NOT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="NOT",
        display="ugent notification contact",
    )
    PRCP = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="PRCP",
        display="primary information recipient",
    )
    REFB = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="REFB",
        display="Referred By",
    )
    REFT = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="REFT",
        display="Referred to",
    )
    TRC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="TRC",
        display="tracker",
    )
    LOC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="LOC",
        display="location",
    )
    DST = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DST",
        display="destination",
    )
    ELOC = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ELOC",
        display="entry location",
    )
    ORG = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="ORG",
        display="origin",
    )
    RML = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="RML",
        display="remote",
    )
    VIA = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="VIA",
        display="via",
    )
    PRF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="PRF",
        display="performer",
    )
    DIST = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="DIST",
        display="distributor",
    )
    PPRF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="PPRF",
        display="primary performer",
    )
    SPRF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="SPRF",
        display="secondary performer",
    )
    RESP = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="RESP",
        display="responsible party",
    )
    VRF = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="VRF",
        display="verifier",
    )
    AUTHEN = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="AUTHEN",
        display="authenticator",
    )
    LA = Coding(
        system="http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        code="LA",
        display="legal authenticator",
    )


class OrganizationType(Dict[str, Coding]):
    prov = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="prov",
        display="Healthcare Provider",
    )
    dept = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="dept",
        display="Hospital Department",
    )
    team = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="team",
        display="Organizational team",
    )
    govt = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="govt",
        display="Government",
    )
    ins = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="ins",
        display="Insurance Company",
    )
    pay = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="pay",
        display="Payer",
    )
    edu = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="edu",
        display="Educational Institute",
    )
    reli = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="reli",
        display="Religious Institution",
    )
    crs = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="crs",
        display="Clinical Research Sponsor",
    )
    cg = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="cg",
        display="Community Group",
    )
    bus = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="bus",
        display="Non-Healthcare Business or Corporation",
    )
    other = Coding(
        system="http://terminology.hl7.org/CodeSystem/organization-type",
        code="other",
        display="Other",
    )
