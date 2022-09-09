#NOTE = IAM role has to be created to send data to the AWS IoT Core
import json
import boto3

client = boto3.client('iot')

def lambda_handler(event, context):
    
    
    
    iot = boto3.client('iot-data','us-east-1') 
    for i in range(100):
        res = {
            "temperature" : 35
        }
        iot.publish(
            topic='device/12/IoT_alert',
            qos=0,
            payload=json.dumps(res))
        print(i)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
