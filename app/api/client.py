from fastapi import APIRouter, HTTPException
from typing import List
from app.models.client import Client, ClientCreate
from app.core.client_services import (
    create_new_client,
    get_all_clients,
    get_client_by_id,
    update_existing_client,
    delete_client
)

router = APIRouter()

@router.post("/clients/", response_model=Client)
def create_client(client: ClientCreate):
    return create_new_client(client)

@router.get("/clients/", response_model=List[Client])
def read_clients():
    return get_all_clients()

@router.get("/clients/{client_id}", response_model=Client)
def read_client(client_id: str):
    client = get_client_by_id(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@router.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: str, client_update: dict):
    client = update_existing_client(client_id, client_update)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@router.delete("/clients/{client_id}")
def remove_client(client_id: str):
    delete_client(client_id)
    return {"detail": "Cliente no encontrado"}