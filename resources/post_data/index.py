import boto3
from boto3.dynamodb.conditions import Key

from post_data_type import Student3

DYNAMODB = boto3.resource('dynamodb')


def handler(event, _):
    print(event)
    table1 = DYNAMODB.Table('sample_table1')
    table2 = DYNAMODB.Table('sample_table2')
    response1 = table1.scan()
    response2 = table2.scan()
    print(response1)
    print(response2)
    return ''
