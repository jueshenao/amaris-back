from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4

def generate_id():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

class FundBase(BaseModel):
    id: str = Field(default_factory=generate_id)
    name: str
    minimum_amount: int
    category: str
    created_at: str = Field(default_factory=generate_date)
    
class FundCreate(FundBase):
    pass
    
class Fund(FundBase):
    id: str
    
    class Config:
        orm_mode = True