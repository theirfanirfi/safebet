from pydantic import BaseModel, ConfigDict

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool = False

class UserPrivate(User):
    password: str
    

class UserLogin(BaseModel):
    email: str
    password: str
    
class ResetPassword(BaseModel):
    new_password: str
    confirm_password:str

class ForgotPassword(BaseModel):
    email: str