import dataclasses
from typing import Any
import boto3
from boto3.dynamodb.conditions import Key
import uuid
import os

TABLE_NAME = os.getenv('SAMPLE_TABLE_NAME', 'sample_table1_test')
DYNAMODB = boto3.resource('dynamodb')


@dataclasses.dataclass
class UserTable:
    table: Any = DYNAMODB.Table(TABLE_NAME)

    @classmethod
    def create_table(cls, mock_dynamodb) -> None:
        mock_dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {'AttributeName': "id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )

    @classmethod
    def create_user(cls, user_name: str, user_age: int) -> None:
        cls.table.put_item(
            Item={'id': str(uuid.uuid4()), 'name': user_name, 'age': user_age}
        )

    @classmethod
    def get_user_data(cls, user_id: str) -> Any:
        user_data = cls.table.query(KeyConditionExpression=Key('id').eq(user_id))
        return user_data['Items']

    @classmethod
    def scan_user_data(cls) -> Any:
        return cls.table.scan()['Items']

    @classmethod
    def create_dummy_data(cls, dummy_data_list: list) -> Any:
        with cls.table.batch_writer() as batch:
            for item in dummy_data_list:
                batch.put_item(Item=item)


def print_ok():
    print('OK')
