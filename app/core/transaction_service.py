from typing import List
from app.models.transactions import Transaction, TransactionCreate
from app.crud.transactions import TransactionCRUD
from app.crud.client import ClientCRUD
from app.crud.fund import FundCRUD
from fastapi import HTTPException

transaction_crud = TransactionCRUD()
client_crud = ClientCRUD()
fund_crud = FundCRUD()

def create_new_transaction(transaction_data: TransactionCreate) -> Transaction:
    return transaction_crud.create_transaction(transaction_data)

def get_all_transactions() -> List[Transaction]:
    return transaction_crud.get_transactions()

def get_transaction_by_id(transaction_id: str) -> Transaction:
    return transaction_crud.get_transactions_by_id(transaction_id)

def get_transactions_by_fund_id(fund_id: str) -> List[Transaction]:
    return transaction_crud.get_transactions_by_fund_id(fund_id)

def get_transactions_by_client_id(client_id: str) -> List[Transaction]:
    return transaction_crud.get_transactions_by_client_id(client_id)

def subscribe_to_fund(transaction_data: TransactionCreate) -> dict:
    client = client_crud.get_client_by_id(client_id=transaction_data.client_id)
    fund = fund_crud.get_fund_by_id(fund_id=transaction_data.fund_id)
    
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    if not fund:
        raise HTTPException(status_code=404, detail="Fondo no encontrado.")

    if client.balance < fund.minimum_amount:
        raise HTTPException(status_code=400, detail=f"No tiene saldo disponible para vincularse al fondo {fund.name}")
    
    if transaction_data.amount < fund.minimum_amount:
        raise HTTPException(status_code=400, detail=f"El monto de la transacción debe ser al menos {fund.minimum_amount}.")

    updated_client = client_crud.update_balance(client.id, client.balance - transaction_data.amount)
    transaction_crud.create_transaction(transaction_data)
    
    return {"message": f"La apertura al fondo {fund.name} realizada con éxito.", "balance": updated_client.balance}

def unsubscribe_from_fund(transaction_data: TransactionCreate) -> dict:
    client = client_crud.get_client_by_id(client_id=transaction_data.client_id)
    fund = fund_crud.get_fund_by_id(fund_id=transaction_data.fund_id)
    
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    if not fund:
        raise HTTPException(status_code=404, detail="Fondo no encontrado.")
    
    existing_transactions = transaction_crud.get_transactions_by_fund_id(transaction_data.fund_id)
    subscription_found = any(transaction.transaction_type == "apertura" for transaction in existing_transactions)
    if not subscription_found:
        raise HTTPException(status_code=404, detail="Suscripción no encontrada.")

    updated_client = client_crud.update_balance(client.id, client.balance + transaction_data.amount)
    transaction_crud.create_transaction(transaction_data)
    
    return {"message": f"Cancelación del fondo {fund.name} realizada.", "balance": updated_client.balance}