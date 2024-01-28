from fastapi import APIRouter
from fastapi.params import Depends,Body,Path
from sqlalchemy.orm.session import Session
from schemas import UserBase,DisplayUser
from db.database import get_db
from db import db_user

router =  APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user
@router.post('/', response_model=DisplayUser)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)

# Reade user



# Update user



# Delete user