import boto3
from botocore.exceptions import ClientError
from sys import argv
import requests



RECIPIENT = "sachin.saini@cloverbaytechnologies.com"
SENDER = "yogesh.p@cloverbaytechnologies.com"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("\r\n"
            )
'http://100.25.211.184:8080/job/demo/build?token=newjob'
