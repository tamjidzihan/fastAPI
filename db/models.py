from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String,Boolean

from db.database import Base



class Dbuser(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    items = relationship("DbArticle",back_populates='user')


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship("Dbuser",back_populates='items')


class DbProducts(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
