from typing import List
from app.models.client import Client, ClientCreate
from app.crud.client import ClientCRUD

client_crud = ClientCRUD()

def create_new_client(client_data: ClientCreate) -> Client:
    return client_crud.create_client(client_data)

def get_all_clients() -> List[Client]:
    return client_crud.get_clients()

def get_client_by_id(client_id: str) -> Client:
    return client_crud.get_client_by_id(client_id)

def update_existing_client(client_id: str, client_update: dict) -> Client:
    return client_crud.update_client(client_id, client_update)

def delete_client(client_id: str):
    client_crud.delete_client(client_id)