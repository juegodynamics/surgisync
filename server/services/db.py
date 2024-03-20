import json
import psycopg2  # type: ignore[import-untyped]

from models import Id
from models.domainresource import DomainResource


def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {key: clean_nones(val) for key, val in value.items() if val is not None}
    else:
        return value


class DBAccessWrapper:
    def __init__(self):
        # As of now, no user/password set
        self.conn = psycopg2.connect(
            database="surgisync", user="", password="", port=5432
        )

        # Open a cursor to perform database operations
        self.cursor = self.conn.cursor()

    def get_resource(self, resourceType: str, id: Id):
        self.cursor.execute(
            f"SELECT resource_data FROM fhir WHERE resource_type = '{resourceType}' AND id = '{id}'"
        )

        resource_data = self.cursor.fetchone()[0]
        return clean_nones(resource_data)

    def get_resources(self, resourceType: str, limit: int = 20):
        self.cursor.execute(
            f"SELECT resource_data FROM fhir WHERE resource_type = '{resourceType}'"
        )

        resource_data = self.cursor.fetchmany()[0]
        return clean_nones(resource_data)

    def insert_resource(self, resource: DomainResource):
        self.cursor.execute(
            "INSERT INTO fhir (id, resource_type, resource_data) VALUES (%s, %s, %s)",
            (
                resource.id,
                resource.resourceType,
                json.dumps(resource.dict(), default=str),
            ),
        )

        self.conn.commit()
        return
