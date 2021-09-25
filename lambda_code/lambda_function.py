
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamo.Table(os.environ['tablename'])


def result(status, message):
    return{
        'statusCode': status,
        'body': message,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }


def lambda_handler(event, context):
    table = dynamodb.Table('RequestTable2')
    response = table.update_item(
        Key={'RequestID': 5},
        ExpressionAttributeValues={
            ':val': 1
        },
        UpdateExpression="ADD req_counter :val",
        ReturnValues="UPDATED_NEW")
    print(response)
    counted_req = response["Attributes"]["req_counter"]
    return result(200, counted_req)
