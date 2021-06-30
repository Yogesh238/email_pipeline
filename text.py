import boto3
from botocore.exceptions import ClientError
from sys import argv
import requests



RECIPIENT = "yogesh.p@cloverbaytechnologies.com"
SENDER = "sachin.saini@cloverbaytechnologies.com"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


# The email body for recipients with non-HTML email clients.
 BODY_HTML = """<html>
                <head></head>
                <body>
                  <h3>http://100.25.211.184:8080/job/demo/build?token=newjob</h3>
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
