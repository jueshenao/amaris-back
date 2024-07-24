from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4

def generate_id():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

class ClientBase(BaseModel):
    id: str = Field(default_factory=generate_id)
    balance: int
    email: str
    created_at: str = Field(default_factory=generate_date)

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: str

    class Config:
        orm_mode = True