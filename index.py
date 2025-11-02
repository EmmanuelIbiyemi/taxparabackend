from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

##--- auths
from auth.signup import signup_router
from auth.login import loginroute

#--- blogs
from blog_post.blog import blogroute

app = FastAPI(
    title="TIN MOBILE BACKEND",
    debug=True
)

# Adding CORSMiddleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:8080",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def Home():
    return ("Welcome To TAX app backend")


app.include_router(router=signup_router)
app.include_router(router=loginroute)
app.include_router(router=blogroute)