from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime
from typing import Literal

def generate_id():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

class TransactionBase(BaseModel):
    id: str = Field(default_factory=generate_id)
    fund_id: str
    client_id: str
    transaction_type: Literal['apertura', 'cancelacion']
    amount: int
    date: str = Field(default_factory=generate_date)
    created_at: str = Field(default_factory=generate_date)
    
    
class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: str
    
    class Config:
        orm_mode = True