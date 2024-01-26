from fastapi import APIRouter,Response,status
from typing import Optional
from blogtype import BlogType

router = APIRouter(
    prefix='/blog',
    tags=['blog']
    )

# @router.get('/blog/all')
# def get_all_blogs():
#     return {
#         "message": "All the blogs"
#     }


@router.get(
        '/type/{type}',
        summary='Retrive all blogs',
        description='This api call simulates fetching all blogs',
        response_description='The list of availabale blogs'
        )
def blog_type(type: BlogType):
    return {
        "message":f"Blog type: {type.value}"
    }


@router.get(
        '/{id}/commant/{commant_id}/userid/{user_id}',
        tags=['comment'],
        summary='Retrive all comments',
        )
def get_commant(id:int,commant_id:int,user_id:int,valid: bool = True, username:Optional[str] = None):
    '''
    Simulate retrieving a comment of a blog
    - **id** mandetory path parameter,
    - **comment_id** mandetory path parameter,
    - **user_id** mandetory path parameter,
    - **valid** optional query patameter,
    - **username** optional query patameter
    '''
    return {
        "message":f"Your Id is {id}, and your comman ID is {commant_id} , is_valid: {valid}, username : {username} and your userId: {user_id}"
    }



@router.get(
        '/all'
        )
def get_all_blogs(page=1,page_size: Optional[int]=None):
    return {
        "message":f"page: {page}, page_size: {page_size}"
    }



@router.get(
        '/{id}',
         status_code=status.HTTP_200_OK
         )
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