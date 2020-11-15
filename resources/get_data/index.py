import boto3
from boto3.dynamodb.conditions import Key
import requests
from get_data_type import Student
from user_table import print_ok, UserTable

DYNAMODB = boto3.resource('dynamodb')


def get_table_data(table_name):
    table = DYNAMODB.Table(table_name)
    return table.scan()


def handler(event, _):
    print(event)
    # data2 = get_table_data('sample_table2')

    # print(data2)
    data1 = UserTable.scan_user_data()
    UserTable.create_user('Jam', 24)
    print(data1)
    print_ok()

    return ''
