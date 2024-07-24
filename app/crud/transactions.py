from typing import List
from app.models.transactions import Transaction, TransactionCreate
import boto3
from boto3.dynamodb.conditions import Key

class TransactionCRUD:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('transactions')

    def create_transaction(self, transaction: TransactionCreate) -> Transaction:
        new_transaction = Transaction(**transaction.dict())
        self.table.put_item(Item=new_transaction.dict())
        return new_transaction

    def get_transactions(self) -> List[Transaction]:
        response = self.table.scan()
        return [Transaction(**item) for item in response.get('Items', [])]

    def get_transactions_by_id(self, transaction_id: str) -> Transaction:
        response = self.table.query(
            KeyConditionExpression=Key('id').eq(transaction_id)
        )
        items = response.get('Items', [])
        if items:
            return Transaction(**items[0])
        return None
    
    def get_transactions_by_fund_id(self, fund_id: str) -> List[Transaction]:
        response = self.table.query(
            IndexName='fund_id-index',
            KeyConditionExpression=Key('fund_id').eq(fund_id)
        )
        return [Transaction(**item) for item in response.get('Items', [])]
    
    def get_transactions_by_client_id(self, client_id: str) -> List[Transaction]:
        response = self.table.query(
            IndexName='client_id-index',
            KeyConditionExpression=Key('client_id').eq(client_id)
        )
        return [Transaction(**item) for item in response.get('Items', [])]