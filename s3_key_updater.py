# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import boto3
import time
import datetime

class S3KeyUpdater:
    def __init__(self):
        self.client = boto3.client('s3')

    def update_key(self, public_key, bucket, filename):
        self.client.put_object(Body=public_key, Bucket=bucket, Key=filename)

