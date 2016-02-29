# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.

import os
import sys

_BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _BASE_PATH not in sys.path:
    sys.path.append(_BASE_PATH)

from constants.accounts import AWS_ACCOUNTS
from constants.regions import AWS_REGIONS, aws_region
import credentials
import lib.tasks

import boto3


class SessionManager(object):
    def __init__(self):
        self.aws_sessions = {}
        for account in AWS_ACCOUNTS:
            for region in AWS_REGIONS:
                self.aws_sessions[(account, region)] = boto3.Session(
                    aws_access_key_id=credentials.AWS[account]['aws_access_key_id'],
                    aws_secret_access_key=credentials.AWS[account]['aws_secret_access_key'],
                    region_name=aws_region(region))

        self.aws_clients = {}

    def ec2(self, account, region):
        index = (account, region, 'ec2')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('ec2')
        return self.aws_clients[index]

    def autoscaling(self, account, region):
        index = (account, region, 'autoscaling')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('autoscaling')
        return self.aws_clients[index]

    def iam(self, account, region):
        index = (account, region, 'iam')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('iam')
        return self.aws_clients[index]

    def dynamodb(self, account, region):
        index = (account, region, 'dynamodb')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('dynamodb')
        return self.aws_clients[index]

    def logs(self, account, region):
        index = (account, region, 'logs')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('logs')
        return self.aws_clients[index]

    def cloudfront(self, account, region):
        index = (account, region, 'cloudfront')
        if index in self.aws_clients:
            return self.aws_clients[index]

        self.aws_clients[index] = self.aws_sessions[(account, region)].client('cloudfront')
        return self.aws_clients[index]
