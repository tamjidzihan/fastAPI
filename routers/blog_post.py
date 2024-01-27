from fastapi import APIRouter,Query,Path,Body
from typing import Optional,List
from pydantic import BaseModel


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class ImageModel(BaseModel):
    url: str
    alias:str

class BlogModel(BaseModel):
    title : str
    content : str
    nb_comment: int
    published : Optional[bool]
    tags : List[str] = []
    image: Optional[ImageModel] = None


def required_function():
    return {'message':'Learing FastAPI is important'}



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
            ),
        # content:str = Body('hi how are you') #this is use to add a default value
        content:str = Body(
            ...,
            min_length= 10,
            max_length=100,
            regex='.'
            ),
        v:Optional[List[str]] = Query(['1.0','1.1','1.2'])
    ):
    return {
        "blog": blog,
        "id":id,
        "comment_id":comment_id,
        "content":content,
        "version":v
    }


@router.post('/new/{id}/comment-title/{comment_id}')
def create_comment_title(
        blog: BlogModel,
        id:int,
        comment_title:int = Query(
            None,
            title= 'Title of the comment',
            description='some description of the comment',
            alias='comment Title',
            deprecated=True
            ),
        # content:str = Body('hi how are you') #this is use to add a default value
        content:str = Body(
            ...,
            min_length= 10,
            max_length=100,
            regex='.'
            ),
        v:Optional[List[str]] = Query(['1.0','1.1','1.2']),
        comment_id:int = Path(gt=5,le=10)
    ):
    return {
        "blog": blog,
        "id":id,
        "comment_title":comment_title,
        "content":content,
        "version":v
    }

