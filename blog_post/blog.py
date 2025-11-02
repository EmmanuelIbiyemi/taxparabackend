from fastapi import APIRouter

from connection_db.connection import get_Connection
import psycopg2
from model.Infos import Userblog

blogroute = APIRouter()

@blogroute.post("/blogpost")
async def PostBlog(blogs:Userblog):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO blog values(%s , %s)"
                       (blogs.title , blogs.blogpost,))

        conn.commit()

        return {
            "sucessfull":200,
        }
    except psycopg2.IntegrityError as dbError:
        return {"Db_error": f"{dbError}"}
    
    except Exception as e:
        return {"Error":f"{e}"}

@blogroute.get("/blogread")
async def Readblog():
    try:
        conn = get_Connection()
        cursor = conn.cursor()

        cursor.execute("SELECT title , blog from blog")
        
        result = cursor.fetchall()

        conn.commit()

        return {
            # "blogTitle": result[0],
            # "blogPost" : result[0][1],
            "results": result,
            "success": 200
        }

    except psycopg2.IntegrityError as dbError:
        return{
            "Error": f"{dbError}"
        }
    except Exception as e:
        return{
            "Error":f"{e}"
        }
    