import json
import psycopg2  # type: ignore[import-untyped]


from mocks import (
    patient_Douglas_Olson,
    patient_Elidia_Suellen_Hackett,
    patient_Marco_Antonio_Candelaria,
    organization_level1_health_system,
    organization_level2_hospital,
    organization_level3_surgical,
    organizations__level4_operating_rooms,
    appointment_surg_tomorrow,
)

# As of now, no user/password set
conn = psycopg2.connect(database="surgisync", user="", password="", port=5432)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("""DROP TABLE fhir;""")
conn.commit()

# Create fhir table
cur.execute(
    """
    CREATE TABLE fhir (
        id UUID,
        PRIMARY KEY(id),
        resource_type VARCHAR(50),
        resource_data JSONB
    );"""
)
conn.commit()

for resource in [
    patient_Douglas_Olson,
    patient_Elidia_Suellen_Hackett,
    patient_Marco_Antonio_Candelaria,
    organization_level1_health_system,
    organization_level2_hospital,
    organization_level3_surgical,
    *organizations__level4_operating_rooms,
    appointment_surg_tomorrow,
]:
    cur.execute(
        "INSERT INTO fhir (id, resource_type, resource_data) VALUES (%s, %s, %s)",
        (resource.id, resource.resourceType, json.dumps(resource.dict(), default=str)),
    )
    conn.commit()


# Close cursor and communication with the database
cur.close()
conn.close()
