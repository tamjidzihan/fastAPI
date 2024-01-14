from fastapi import FastAPI
from typing import Optional
from blogtype import BlogType

app = FastAPI()


@app.get('/')
def index():
    return {'message':'hello world!'}


# @app.get('/blog/all')
# def get_all_blogs():
#     return {
#         "message": "All the blogs"
#     }


@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {
        "message":f"Blog type: {type.value}"
    }

@app.get('/blog/{id}/commant/{commant_id}')
def get_commant(id:int,commant_id:int,valid: bool = True, username:Optional[str] = None):
    return {
        "message":f"your Id is {id}, and your comman ID is {commant_id} , is_valid: {valid}, username {username}"
    }



@app.get('/blog/all')
def get_all_blogs(page=1,page_size: Optional[int]=None):
    return {
        "message":f"page: {page}, page_size: {page_size}"
    }

@app.get('/blog/{id}')
def blog(id:int):
    return {
        "message":f"Your Blog id  id {id}"
    }





