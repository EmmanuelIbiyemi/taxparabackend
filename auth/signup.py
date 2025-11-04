from fastapi import  APIRouter 

from model.Infos import UserDetails

# --- This is for the password encryption
from passlib.context import CryptContext

import psycopg2

signup_router = APIRouter()


from connection_db.connection import get_Connection


@signup_router.post("/signup")
def signup(user: UserDetails):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        encryp_pass = pwd_context.hash(user.password)
        results = cursor.execute("INSERT INTO taxusers values (%s , %s , %s)",
                       (user.Username , user.email , encryp_pass,))
        conn.commit()
        return {
                "Registraion Sucessfull": user,
                "Error":"null",
                "Password":encryp_pass,
                "report": 200,
            }
    except psycopg2.IntegrityError as error:
        if "duplicate key value violates unique constraint" in str(error):
            return {"User Email Exist Already": 500, "report":500}
    except Exception as e:
        return {"Error": f"{e}"}    
