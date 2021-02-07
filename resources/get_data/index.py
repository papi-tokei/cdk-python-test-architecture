import boto3
from boto3.dynamodb.conditions import Key
import requests
from get_data_type import Student
from user_table import print_ok, UserTable
from aws_lambda_powertools import Tracer, Logger
import os

DYNAMODB = boto3.resource('dynamodb')
if os.getenv('AWS_REGION'):
    # if: 実際にLambda上で動作している場合のみ適用する
    tracer = Tracer(service="booking")
logger = Logger(
    service="payment",
    level="INFO",
    sampling_rate=None,
    xray_trace_id=None,
    timestamp=None,
    location=None,
)


def get_table_data(table_name):
    table = DYNAMODB.Table(table_name)
    return table.scan()


# @tracer.capture_lambda_handler
def handler(event, _):
    print(event)
    # data2 = get_table_data('sample_table2')

    # print(data2)
    data1 = UserTable.scan_user_data()
    UserTable.create_user('Jam', 24)
    print(data1)
    logger.info(data1)
    logger.info({'test': 123})
    print_ok()

    return 'Return value'
