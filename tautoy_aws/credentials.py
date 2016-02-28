# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.


class AwsCredential(object):
    def __init__(self, access_key_id, secret_access_key):
        self.__access_key_id = access_key_id
        self.__secret_access_key = secret_access_key

    @property
    def access_key_id(self):
        return self.__access_key_id

    @property
    def secret_access_key(self):
        return self.__secret_access_key

    def __str__(self):
        return 'AwsCredential("%s")' % self.__access_key_id


class AwsCredentials(object):
    def __init__(self, aws_credentials={}):
        if not isinstance(aws_credentials, dict):
            raise TypeError()
        self._aws_credentials = {}
        for profile, aws_credential in aws_credentials.iteritems():
            if not isinstance(aws_credential, AwsCredential):
                raise TypeError()
            self._aws_credentials[profile] = aws_credential

    def __getattr__(self, profile):
        if profile in self._aws_credentials:
            return self._aws_credentials[profile]
        raise AttributeError('No such profile "%d" is registered.' % profile)
