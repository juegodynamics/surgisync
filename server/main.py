import os
import sys
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.db import DBAccessWrapper
from models import Id, Appointment

# Get the parent directory of the current script.
# Note that __file__ is the filename of the current script.
# os.path.dirname gets the directory of a file, and os.path.abspath gets the absolute path.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(script_dir))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/resources/{resourceType}/{id}")
async def getResource(resourceType: str, id: str):
    db = DBAccessWrapper()
    return db.get_resource(resourceType=resourceType, id=Id(id))


@app.get("/v1/patients")
async def getPatients():
    db = DBAccessWrapper()
    return db.get_patients()


@app.get("/v1/appointments/participant/{participant_id}")
async def getAppointmentsByParticipantId(participant_id: str):
    db = DBAccessWrapper()
    return db.get_appointments_by_participant(participant_id)


@app.post("/v1/appointments/")
async def insertAppointment(appointment: dict):
    if "id" not in appointment:
        appointment["id"] = Id(uuid.uuid4())
    resource = Appointment.parse_obj(appointment)

    db = DBAccessWrapper()
    db.insert_resource(resource)
    return {"success": True}


@app.post("/v1/appointments/{appointment_id}")
async def updateAppointment(appointment_id, appointment: dict):
    if "id" not in appointment:
        appointment["id"] = Id(appointment_id)
    resource = Appointment.parse_obj(appointment)

    db = DBAccessWrapper()
    db.update_resource(resource)
    return {"success": True}


@app.delete("/v1/appointments/{appointment_id}")
async def deleteAppointment(appointment_id: str):
    db = DBAccessWrapper()
    db.delete_resource(Id(appointment_id), "Appointment")
    return {"success": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
