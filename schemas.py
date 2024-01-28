from pydantic import BaseModel

class UserBase(BaseModel):
    username : str
    email: str
    password : str


class DisplayUser(BaseModel):
    username : str
    email : str

    class config():
        orm_mode = True
