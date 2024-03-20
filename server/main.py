import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.db import DBAccessWrapper
from models import Id

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


@app.get("/v1/schedules")
async def getSurgicalSchedule():
    return {"test": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
