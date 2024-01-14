from fastapi import FastAPI
from blogtype import BlogType

app = FastAPI()

@app.get('/')
def index():
    return {'message':'hello world!'}


@app.get('/blog/all')
def get_all_blogs():
    return {
        "message": "All the blogs"
    }


@app.get('/blog/{id}')
def blog(id:int):
    return {
        "message":f"Your Blog id  id {id}"
    }


@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {
        "message":f"Blog type: {type}"
    }



