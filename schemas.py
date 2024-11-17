from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username : str
    email: str
    password : str



class Article(BaseModel):
    title : str
    content : str
    published : bool
    class config():
        orm_mode = True
        
class DisplayUser(BaseModel):
    username : str
    email : str
    items : List[Article] = []
    class config():
        orm_mode = True



class ArticleBase(BaseModel):
    title : str
    content : str
    published : bool
    creator_id : int



class User(BaseModel):
    id:int
    username : str
    class config():
        orm_mode = True


class DisplayArticle(BaseModel):
    id : int
    title : str
    content : str
    published : bool
    user : User
    class config():
        orm_mode = True