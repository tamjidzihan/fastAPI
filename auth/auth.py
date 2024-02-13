from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

from db.database import get_db
from db import db_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '097144aa8c6fc98ae41514c1bce4e263653f3aac88b603aeec63a6338367dd60'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 360

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
  credential_exception =  HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= 'Could not Validate Creadential',
    headers={
      "WWW-Authenticate":"Bearer"
    }
  )
  try:
    payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    username: str = payload.get("sub")
    if username is None:
      raise credential_exception
  except JWTError:
    raise credential_exception
  
  user = db_user.get_user_by_username(db,username)
  if username is None:
    raise credential_exception
  return user