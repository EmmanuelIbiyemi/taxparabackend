from fastapi import APIRouter
import psycopg2 

from model.Infos import UserLogin
from connection_db.connection import get_Connection

# --- This is for the password encryption
from passlib.context import CryptContext
loginroute = APIRouter()

@loginroute.post("/login")
def login(user: UserLogin):
    try:
        # Create a CryptContext instance, specifying desired hash schemes
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        conn = get_Connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT fullname , email , password from taxusers where email=%s",
                       (user.email,))
        result = cursor.fetchall()
        conn.commit()

        isVerify = pwd_context.verify(user.password , result[0][2])
        
        if (isVerify):
            return {
                "Users":result,
                "Success":200,
                "Error":"null"
            }
        else:
            return {
                "User":"Invalid User",
                "Error":500,
            }

    except psycopg2.IntegrityError as dbError:
        return {"Database Error": f"{dbError}"}
    except Exception as e:
        return {"Error":f"{e}"}
