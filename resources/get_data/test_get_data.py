from . import index
from .index import handler
import user_table
from user_table import UserTable
from decimal import Decimal


def test_get_data(dynamodb, monkeypatch):
    # print('aaa')
    # print(__name__)
    # print('hello')

    # def mock_return(_table_name):
    #     return 'aaa'

    # class Tracer:
    #     def __init__(self, serice):
    #         pass

    # monkeypatch.setattr('aws_lambda_powertools.Tracer', Tracer)
    monkeypatch.setattr(UserTable, "table", dynamodb.Table('sample_table1_test'))
    UserTable.create_table(dynamodb)
    UserTable.create_user('taro', 12)
    UserTable.create_dummy_data(
        [
            {'id': '1234', 'name': 'taro', 'age': Decimal('12')},
            {'id': '567', 'name': 'taro', 'age': Decimal('12')},
            {'id': '666', 'name': 'taro', 'age': Decimal('12')},
        ]
    )

    data = UserTable.scan_user_data()
    print(data)
    handler('', '')
