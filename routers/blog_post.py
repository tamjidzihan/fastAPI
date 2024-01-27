from fastapi import APIRouter,Query,Path,Body
from typing import Optional
from pydantic import BaseModel


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title : str
    content : str
    nb_comment: int
    published : Optional[bool]



@router.post('/new/{id}')
def create_blog(blog: BlogModel,id:int,version:int=1):
    return {
        "id":id,
        "version":version,
        "data":blog
        }


@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel,
    id:int,
    comment_id:int = Query(
        None,
        title= 'id of the comment',
        description='some description of the comment',
        alias='comment ID',
        deprecated=True
        )
    ):
    return {
        "blog": blog,
        "id":id,
        "comment_id":comment_id
    }