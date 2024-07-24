from typing import List
from app.models.fund import Fund, FundCreate
import boto3
from boto3.dynamodb.conditions import Key

class FundCRUD:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('funds')

    def create_fund(self, fund: FundCreate) -> Fund:
        new_fund = Fund(**fund.dict())
        self.table.put_item(Item=new_fund.dict())
        return new_fund

    def get_funds(self) -> List[Fund]:
        response = self.table.scan()
        return [Fund(**item) for item in response.get('Items', [])]

    def get_fund_by_id(self, fund_id: str) -> Fund:
        response = self.table.query(
            KeyConditionExpression=Key('id').eq(fund_id)
        )
        items = response.get('Items', [])
        if items:
            return Fund(**items[0])
        return None

    def update_fund(self, fund_id: str, fund_update: dict) -> Fund:
        update_expression = "SET " + ", ".join(f"{k} = :{k}" for k in fund_update.keys())
        expression_attribute_values = {f":{k}": v for k, v in fund_update.items()}
        self.table.update_item(
            Key={'id': fund_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        return self.get_fund_by_id(fund_id)

    def delete_fund(self, fund_id: str):
        self.table.delete_item(Key={'id': fund_id})