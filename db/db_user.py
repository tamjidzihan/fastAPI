from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import Dbuser
from db.hash import Hash

def create_user(db: Session,request:UserBase):
    new_user = Dbuser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db:Session):
    return db.query(Dbuser).all()


def get_user(db:Session,id:int):
    user = db.query(Dbuser).filter(Dbuser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User id NO:{id} Do not exist'
            )
    return user



def get_user_by_username(db:Session,username:str):
    user = db.query(Dbuser).filter(Dbuser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with NO:{username} Do not exist'
            )
    return user


def update_user(db:Session,id:int,request: UserBase):
    query_user = db.query(Dbuser).filter(Dbuser.id == id)
    query_user.update(
        {
            Dbuser.username : request.username,
            Dbuser.email : request.email
        }
    )
    db.commit()
    return 'User Data updated'

def delete_user(db:Session,id:int):
    user = db.query(Dbuser).filter(Dbuser.id == id).first()
    db.delete(user)
    db.commit()
    return f'user: {user.username} deleted '