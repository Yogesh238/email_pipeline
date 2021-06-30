import boto3
from botocore.exceptions import ClientError
from sys import argv
import requests



RECIPIENT = "yogesh.p@cloverbaytechnologies.com"
SENDER = "sachin.saini@cloverbaytechnologies.com"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"

BODY_TEXT = ("\r\n"
            )
# The email body for recipients with non-HTML email clients.
SUBJECT = "Approve the Production Job"
BODY_HTML = """<html>
                <head></head>
                <body>
                  Hi,
                  
                  Please login in Jenkins & approve the production job so that deployment process can start.
                </body>
                </html>
                            """
client = boto3.client('ses',region_name=AWS_REGION)
try:
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        #ConfigurationSetName=CONFIGURATION_SET,
    )

except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
