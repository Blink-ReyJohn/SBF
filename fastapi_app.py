from fastapi import FastAPI
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi.responses import JSONResponse

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://reyjohnandraje2002:ReyJohn17@concentrix.txv3t.mongodb.net/?retryWrites=true&w=majority&appName=Concentrix")
db = client["SBF"]
collection = db["user_information"]

@app.get("/check_user/{user_id}")
def check_user_id(user_id: str):
    user = collection.find_one({"userID": user_id})

    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return JSONResponse(content={
            "userID": user_id,
            "exists": True,
            "user_data": user
        })

    return JSONResponse(content={
        "userID": user_id,
        "exists": False,
        "user_data": None,
        "message": "User not found"
    })
