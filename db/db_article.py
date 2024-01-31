from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle


def create_article(db:Session,request:ArticleBase):
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all_article(db:Session):
    return db.query(DbArticle).all()


def get_article_idwise(db:Session,id:int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Article id NO: {id} not foud'
            )
    return article

def update_article(db:Session,id:int,request:ArticleBase):
    query_article = db.query(DbArticle).filter(DbArticle.id==id)
    query_article.update(
        {
            DbArticle.title : request.title,
            DbArticle.content : request.content,
            DbArticle.published : request.published
        }
    )
    db.commit()
    return f'Article Updated'

def delete_article(db:Session,id:int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    db.delete(article)
    db.commit()
    return f'Article {article.title} Deleted'
