"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

from fastapi import Request

# In-memory activity database
activities = {
    "Baseball Team": {
        "description": "Join the varsity baseball team and compete in regional tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Develop tennis skills and participate in friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "grace@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Play instruments and perform in school concerts",
        "schedule": "Mondays and Fridays, 3:45 PM - 4:45 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and critical thinking skills",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu"]
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}

# DELETE endpoint to remove a participant from an activity
@app.delete("/activities/{activity_name}/participants/{email}")
async def remove_participant(activity_name: str, email: str, request: Request):
    decoded_activity = activity_name
    decoded_email = email
    # Decode in case of URL encoding
    try:
        from urllib.parse import unquote
        decoded_activity = unquote(activity_name)
        decoded_email = unquote(email)
    except Exception:
        pass
    if decoded_activity not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    if decoded_email not in activities[decoded_activity]["participants"]:
        raise HTTPException(status_code=404, detail="Participant not found in this activity")
    activities[decoded_activity]["participants"].remove(decoded_email)
    return {"message": f"{decoded_email} removed from {decoded_activity}"}
    "Baseball Team": {
        "description": "Join the varsity baseball team and compete in regional tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu"]
        },
        "Tennis Club": {
        "description": "Develop tennis skills and participate in friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu"]
        },
        "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "grace@mergington.edu"]
        },
        "Music Ensemble": {
        "description": "Play instruments and perform in school concerts",
        "schedule": "Mondays and Fridays, 3:45 PM - 4:45 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu"]
        },
        "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
        },
        "Debate Team": {
        "description": "Develop public speaking and critical thinking skills",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu"]
        },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
# Validate student is not already signed up
if email in activity["participants"]:
    raise HTTPException(status_code=400, detail="Student is already signed up")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
