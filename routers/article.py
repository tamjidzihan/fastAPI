from fastapi import APIRouter
from fastapi.params import Depends,Body,Path
from sqlalchemy.orm.session import Session
from typing import List

from schemas import ArticleBase,DisplayArticle,UserBase
from db.database import get_db
from db import db_article
from auth.auth import oauth2_scheme,get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create Acticle
@router.post('/',response_model=DisplayArticle)
def create_article_data(
    request:ArticleBase,
    db:Session = Depends(get_db),
    current_user : UserBase = Depends(get_current_user)
    ):
    return db_article.create_article(db,request)


# Read All Article
@router.get('/',response_model=List[DisplayArticle])
def display_all_article(db:Session=Depends(get_db)):
    return db_article.get_all_article(db)


# Read Article ID Wise
@router.get('/{id}',response_model=DisplayArticle)
def display_article_idwise(
    id:int,
    db:Session = Depends(get_db),
    current_user : UserBase = Depends(get_current_user)
    ):
    return db_article.get_article_idwise(db,id)


# Update Article
@router.post('/update/{id}')
def update_article_data(id:int,request:ArticleBase,db:Session = Depends(get_db)):
    return db_article.update_article(db,id,request)


@router.get('/delete/{id}')
def delete_article_data(id:int,db:Session = Depends(get_db)):
    return db_article.delete_article(db,id)