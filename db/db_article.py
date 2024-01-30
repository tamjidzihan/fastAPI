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
    return db.query(DbArticle).filter(DbArticle.id == id).first()
