from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import sqlite3
import os
from http import HTTPStatus

app = FastAPI()

#cors....
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#input 
class NameInput(BaseModel):
    firstName: str
    lastName: str

#look up and erros hand
def find_user_in_db(first_name: str, last_name: str):
    if not first_name or not last_name:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": {"error": "Both first_name and last_name are required."}
        }

    display_name = f"{first_name} {last_name}".lower()

    try:
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned.db'))
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = "SELECT * FROM cleaned WHERE LOWER(display_name) = ?;"
        cursor.execute(query, (display_name,))
        result = cursor.fetchone()

        if result:
            columns = [description[0] for description in cursor.description]
            user_data = {columns[i]: result[i] for i in range(len(columns))}
            return {
                "statusCode": HTTPStatus.OK,
                "body": {"user": user_data}
            }
        else:
            return {
                "statusCode": HTTPStatus.NOT_FOUND,
                "body": {"message": "No matching user found."}
            }

    except Exception as e:
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": {"error": str(e)}
        }
    finally:
        conn.close()

# POST receive name and search in DB
@app.post("/api")
async def receive_name(name_input: NameInput):
    response = find_user_in_db(name_input.firstName, name_input.lastName)
    return JSONResponse(status_code=response["statusCode"], content=response["body"])

# Health check endpoint
@app.get("/api")
async def health_check():
    return {"message": "SUCCESS"}