from pydantic import BaseModel

class UserDetails(BaseModel):
    Username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Userblog(BaseModel):
    title:str
    blogsummary:str
    blogPost:str