from fastapi import APIRouter, HTTPException
from typing import List
from app.models.transactions import Transaction, TransactionCreate
from app.core.transaction_service import (
    get_all_transactions,
    get_transaction_by_id,
    get_transactions_by_client_id,
    get_transactions_by_fund_id,
    subscribe_to_fund,
    unsubscribe_from_fund
)

router = APIRouter()

@router.get("/transactions/", response_model=List[Transaction])
def list_transactions():
    return get_all_transactions()

@router.get("/transactions/fund/{fund_id}", response_model=List[Transaction])
def read_transactions_by_fund(fund_id: str):
    transactions = get_transactions_by_fund_id(fund_id)
    if not transactions:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return transactions

@router.get("/transactions/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: str):
    transaction = get_transaction_by_id(transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/client/{client_id}", response_model=List[Transaction])
def read_transactions_by_client(client_id: str):
    transactions = get_transactions_by_client_id(client_id)
    if not transactions:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return transactions

@router.post("/transactions/subscribe/", response_model=dict)
def subscribe(transaction: TransactionCreate):
    return subscribe_to_fund(transaction)

@router.post("/transactions/unsubscribe/", response_model=dict)
def unsubscribe(transaction: TransactionCreate):
    return unsubscribe_from_fund(transaction)