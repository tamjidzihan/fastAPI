from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from db.database import Base



class Dbuser(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String,unique=True)
    password = Column(String)