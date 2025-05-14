from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://reyjohnandraje2002:ReyJohn17@concentrix.txv3t.mongodb.net/?retryWrites=true&w=majority&appName=Concentrix")
db = client["SBF"]
collection = db["user_information"]

# Pydantic model (optional if expanding later)
class UserResponse(BaseModel):
    userID: str
    exists: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None

@app.get("/check_user/{user_id}", response_model=UserResponse)
def check_user_id(user_id: str):
    user = collection.find_one({"userID": user_id})
    if user:
        return {
            "userID": user_id,
            "exists": True,
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name")
        }
    return {"userID": user_id, "exists": False}
