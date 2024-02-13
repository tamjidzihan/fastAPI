from fastapi import APIRouter,Response,status,Header
from fastapi.params import Depends,Body,Path
from sqlalchemy.orm.session import Session
from typing import List,Optional
from schemas import UserBase,DisplayUser

from db.database import get_db
from db import db_user
from auth.auth import get_current_user

router =  APIRouter(
    prefix='/user',
    tags=['user']
)


# Custom Header
admin_user = ['admin','root','user']
@router.get('/withheader')
def get_user_name(
    response:Response,
    custom_header: Optional[List[str]] = Header(None)
    ):
    return admin_user



# user CRUD operation:

# Create user
@router.post('/', response_model=DisplayUser)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)

# Reade ALL user
@router.get('/',response_model=List[DisplayUser])
def display_all_user(
    db:Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
    ):
    return db_user.get_all_user(db)

# Reade one user
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=DisplayUser)
def display_user(id:int,response:Response,db:Session=Depends(get_db)):
    if db_user.get_user(db,id):
        response.status_code = status.HTTP_200_OK
        return db_user.get_user(db,id)    
    else:
        response.status_code = status.HTTP_200_OK
        return {"error":"User Not found"}
        
# Update user
@router.post('/update/{id}')
def update_user_data(id:int,request:UserBase,db:Session = Depends(get_db)):
    return db_user.update_user(db,id,request)

# Delete user
@router.get('/delete/{id}')
def delete_user_data(id:int,db:Session = Depends(get_db)):
    return db_user.delete_user(db,id)