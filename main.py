from fastapi import FastAPI
from routers import blog_get,blog_post,user
from db import models
from db.database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)


@app.get('/',tags=['home'])
def index():
    return {'message':'hello world!'}


