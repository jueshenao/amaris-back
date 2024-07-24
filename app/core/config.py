import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class DynamoDBConfig:
    def __init__(self, region_name: str = "us-west-2"):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)

    def create_tables(self):
        try:
            # Crear tabla para fondos
            funds_table = self.dynamodb.create_table(
                TableName='funds',
                KeySchema=[
                    {'AttributeName': 'id', 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'id', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            funds_table.meta.client.get_waiter('table_exists').wait(TableName='funds')
            print("Tabla (Funds) creada")
            
            # Crear tabla de transacciones
            transactions_table = self.dynamodb.create_table(
                TableName='transactions',
                KeySchema=[
                    {'AttributeName': 'id', 'KeyType': 'HASH'},
                    {'AttributeName': 'date', 'KeyType': 'RANGE'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'id', 'AttributeType': 'S'},
                    {'AttributeName': 'date', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            transactions_table.meta.client.get_waiter('table_exists').wait(TableName='transactions')
            print("Tabla (Transactions) creada")
            
            # Crear tabla de clientes
            clients_table = self.dynamodb.create_table(
                TableName='clients',
                KeySchema=[
                    {'AttributeName': 'id', 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'id', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            clients_table.meta.client.get_waiter('table_exists').wait(TableName='clients')
            print("Tabla (clientes) creada")
            
        except (NoCredentialsError, PartialCredentialsError):
            print("Credenciales no validas")
        except Exception as e:
            print(f"Error al crear las tablas: {e}")