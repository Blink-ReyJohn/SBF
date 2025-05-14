from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from fastapi.responses import JSONResponse
from bson.json_util import dumps
import json

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://reyjohnandraje2002:ReyJohn17@concentrix.txv3t.mongodb.net/?retryWrites=true&w=majority&appName=Concentrix")
db = client["SBF"]
collection = db["user_information"]

@app.get("/check_user/{user_id}")
def check_user_id(user_id: str):
    try:
        user = collection.find_one({"userID": user_id})

        if user:
            user_json = json.loads(dumps(user))  # safely serialize ObjectId and datetime
            return JSONResponse(content={
                "userID": user_id,
                "exists": True,
                "user_data": user_json
            })

        return JSONResponse(content={
            "userID": user_id,
            "exists": False,
            "user_data": None,
            "message": "User not found"
        })

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "data": "Internal Server Error",
                "error": str(e),
                "requestParameters": {
                    "account_number": user_id
                }
            }
        )
