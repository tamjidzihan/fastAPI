from fastapi import APIRouter
from fastapi.params import Depends,Body,Path
from sqlalchemy.orm.session import Session
from typing import List
from schemas import UserBase,DisplayUser
from db.database import get_db
from db import db_user

router =  APIRouter(
    prefix='/user',
    tags=['user']
)

# user CRUD operation:

# Create user
@router.post('/', response_model=DisplayUser)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)

# Reade ALL user
@router.get('/',response_model=List[DisplayUser])
def display_all_user(db:Session = Depends(get_db)):
    return db_user.get_all_user(db)

# Reade one user
@router.get('/{id}')
def display_user(id:int,db:Session=Depends(get_db)):
    return db_user.get_user(db,id)



# Update user



# Delete user