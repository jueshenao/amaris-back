from typing import List
from app.models.client import Client, ClientCreate
import boto3
from boto3.dynamodb.conditions import Key

class ClientCRUD:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('clients')

    def create_client(self, client: ClientCreate) -> Client:
        new_client = Client(**client.dict())
        self.table.put_item(Item=new_client.dict())
        return new_client
    
    def get_clients(self) -> List[Client]:
        response = self.table.scan()
        return [Client(**item) for item in response.get('Items', [])]

    def get_client_by_id(self, client_id: str) -> Client:
        response = self.table.query(
            KeyConditionExpression=Key('id').eq(client_id)
        )
        items = response.get('Items', [])
        if items:
            return Client(**items[0])
        return None

    def update_balance(self, client_id: str, new_balance: float) -> Client:
        self.table.update_item(
            Key={'id': client_id},
            UpdateExpression='SET balance = :val',
            ExpressionAttributeValues={':val': new_balance}
        )
        return self.get_client_by_id(client_id)