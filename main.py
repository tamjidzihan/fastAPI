from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import blog_get,blog_post,user,article
from db import models
from db.database import engine
from auth import authentication

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)



@app.get('/',tags=['home'])
def index():
    return {'message':'hello world!'}



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],

)