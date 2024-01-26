from fastapi import FastAPI,Response,status
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


@app.get('/blog/{id}/commant/{commant_id}/userid/{user_id}')
def get_commant(id:int,commant_id:int,user_id:int,valid: bool = True, username:Optional[str] = None):
    return {
        "message":f"Your Id is {id}, and your comman ID is {commant_id} , is_valid: {valid}, username : {username} and your userId: {user_id}"
    }



@app.get('/blog/all')
def get_all_blogs(page=1,page_size: Optional[int]=None):
    return {
        "message":f"page: {page}, page_size: {page_size}"
    }



@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def blog(id:int,response:Response):
    if id>20:
        response.status_code = status.HTTP_404_NOT_FOUND
        return{
            "error":f"Blog id {id} not found"
        }
    response.status_code = status.HTTP_200_OK
    return {
        "message":f"Your Blog id is {id}"
    }













