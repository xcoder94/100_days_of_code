from pydantic import BaseModel

# Pydantic models for request/response
class UserCreate(BaseModel):
    username: str
    role: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True


class TodoListCreate(BaseModel):
    user_id: int
    name: str


class TodoListOut(BaseModel):
    id: int
    user_id: int
    name: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    todo_list_id: int
    description: str
    is_done: bool


class TaskOut(BaseModel):
    id: int
    todo_list_id: int
    description: str
    is_done: bool

    class Config:
        from_attributes = True


class CheckUser(BaseModel):
    username: str
    password: str


class CheckUserOut(BaseModel):
    id: int
    username: str
    email: str
    # password: str # Added this line temporarily for debugging

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str