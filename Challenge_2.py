import json
import boto3

conn = boto3.client('ec2')
def lambda_handler(event, context):

    response = conn.modify_instance_metadata_options(InstanceId='i-09af8cdd3ef246bc8')
    data=json.dumps(response)
    print('data',data)
    return data
